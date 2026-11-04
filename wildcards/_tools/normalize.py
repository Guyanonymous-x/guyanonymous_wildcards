"""Removes the inline-choice characters  { } |  from every wildcard file of a workspace (called by build_all.py after the build steps).
  {a|b|}            -> __opt_inl_<id>__   a small file listing the alternatives, one per line (an empty alternative becomes a blank line = "nothing")
  {5::a|5::b}       -> same, the 5:: weights become repeated lines
  a b c|d|e         -> bare pipes: split into separate lines (a b c / a b d / a b e), or a __opt_inl_<id>__ reference when the pipes sit inside a long comma-separated prompt
So no file needs your tool to understand { } or |, and nothing is shown literally in the output."""
import os, re, sys, zlib
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from paths import wc_dir
GROUP = re.compile(r'\{([^{}]*)\}')
def alts(body):
    out = []
    for a in body.split('|'):
        m = re.match(r'^\s*(\d+)::(.*)$', a)
        n, t = (int(m.group(1)), m.group(2)) if m else (1, a)
        out += [t.strip()] * max(1, min(n, 10))
    return out
def ensure(wc, items, made):
    key = '\n'.join(items); name = 'opt_inl_%08x' % (zlib.crc32(key.encode('utf8')) & 0xffffffff)
    if name not in made:
        made[name] = items
    return name
def norm_line(line, wc, made):
    if '{' not in line and '|' not in line:
        return [line]
    for _ in range(10):                                   # innermost groups first
        def sub(m):
            body = m.group(1); lead = ' ' if body.startswith(' ') else ''
            if '|' not in body: return body
            items = alts(body)
            if len(set(items)) == 1 and items[0] == '': return ''
            return lead + '__' + ensure(wc, items, made) + '__'
        new = GROUP.sub(sub, line)
        if new == line: break
        line = new
    line = line.replace('{', '').replace('}', '')
    if '|' in line:
        if line.count(',') >= 2 or '__' in line:           # long prompt: comma-delimited alternatives
            def seg(m):
                items = [x.strip() for x in m.group(0).split('|')]
                return '__' + ensure(wc, items, made) + '__'
            line = re.sub(r'[^,|]+(?:\|[^,|]+)+', seg, line)
            return [line]
        parts = line.split('|'); first = parts[0].rstrip()
        if ' ' in first and all(' ' not in p.strip() for p in parts[1:]):
            prefix = first[: first.rindex(' ') + 1]; return [prefix + first[first.rindex(' ') + 1:]] + [prefix + p.strip() for p in parts[1:]]
        return [p.strip() for p in parts]
    return [line]
def run(wc):
    made = {}; changed = 0
    for f in sorted(os.listdir(wc)):
        if not f.endswith('.txt') or f.startswith('opt_inl_'): continue
        p = os.path.join(wc, f); raw = open(p, encoding='utf8', errors='replace').read()
        if not any(c in raw for c in '{}|'): continue
        out = []
        for l in raw.split('\n')[:-1] if raw.endswith('\n') else raw.split('\n'): out += norm_line(l, wc, made)
        open(p, 'w', encoding='utf8', newline='\n').write('\n'.join(out) + '\n'); changed += 1
    for name, items in made.items():
        items = [norm_line(i, wc, made)[0] if ('{' in i or '|' in i) else i for i in items]
        open(os.path.join(wc, name + '.txt'), 'w', encoding='utf8', newline='\n').write('\n'.join(items) + '\n')
    # prune option files nothing refers to any more
    ref = re.compile(r'__(opt_inl_[0-9a-f]{8})__'); alln = {f[:-4] for f in os.listdir(wc) if f.endswith('.txt')}; used = set(); stack = []
    for f in alln:
        if f.startswith('opt_inl_'): continue
        stack += ref.findall(open(os.path.join(wc, f + '.txt'), encoding='utf8', errors='replace').read())
    while stack:
        x = stack.pop()
        if x in used or x not in alln: continue
        used.add(x); stack += ref.findall(open(os.path.join(wc, x + '.txt'), encoding='utf8', errors='replace').read())
    for f in alln:
        if f.startswith('opt_inl_') and f not in used: os.remove(os.path.join(wc, f + '.txt'))
    print(f'normalize: {changed} files cleaned, {len(made)} option files created')
if __name__ == '__main__': run(wc_dir())
