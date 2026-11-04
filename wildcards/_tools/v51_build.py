"""v51 build: static quality fixes applied to every wildcard file (idempotent).
 - repeated words inside a line ('flannel flannel shirt' -> 'flannel shirt'); __refs__ and a short whitelist of real doubles are left alone
 - liquid_look article (A amber -> An amber)"""
import os, re, sys, glob
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from paths import FINAL
OK = {'that', 'had', 'very', 'bye', 'tutu', 'bora', 'dumdum', 'mama', 'papa', 'cha', 'murmur', 'pom', 'boom', 'tom', 'hula', 'baba', 'coco', 'dodo', 'kiwi', 'poi', 'yoyo'}
DBL = re.compile(r'(?<![\w_])([A-Za-z][A-Za-z\-]{2,}) \1(?![\w_])', re.I)
NOCLOTH = re.compile(r'^[^:"]{1,60}: "no clothing,\s*([^"]+)"\s*$')
def fix_line(l):
    m = NOCLOTH.match(l)
    if m:
        d = m.group(1).strip(); l = d[:1].lower() + d[1:] if not re.match(r'[A-Z]{2}', d) else d
    parts = re.split(r'(__[A-Za-z0-9_\-/]+__)', l)
    out = []
    for p in parts:
        if p.startswith('__') and p.endswith('__'): out.append(p); continue
        out.append(DBL.sub(lambda m: m.group(0) if m.group(1).lower() in OK else m.group(1), p))
    out2 = ''.join(out)
    out2 = re.sub(r'^A (?=[aeiou][a-z]+ liquid)', 'An ', out2)
    return out2
    # a word repeated across a reference boundary is left alone (cannot be known statically)
    return ''.join(out)
BADHAIR = re.compile(r'balding patches|shaved bald hairline|mostly bald crown', re.I)
def drop_conflicts(folder):
    n = 0
    for p in glob.glob(os.path.join(folder, '*hair*.txt')):
        if not re.search(r'hairvol|hair_line', os.path.basename(p)): continue
        t = open(p, encoding='utf-8').read().split('\n'); keep = [l for l in t if not BADHAIR.search(l)]
        if len(keep) != len(t) and any(l.strip() for l in keep): open(p, 'w', encoding='utf-8').write('\n'.join(keep)); n += 1
    return n
def run(folder=FINAL):
    n = lines = 0
    for p in glob.glob(os.path.join(folder, '*.txt')):
        if os.path.basename(p) in ('README.txt', 'CHANGELOG.txt', 'HOW_TO_RUN.txt'): continue
        t = open(p, encoding='utf-8').read().split('\n'); new = [fix_line(l) for l in t]
        c = sum(a != b for a, b in zip(t, new))
        if c: open(p, 'w', encoding='utf-8').write('\n'.join(new)); n += 1; lines += c
    return n, lines, drop_conflicts(folder)
def export_aoo(out, prefix='aoo_'): return run(out)
if __name__ == '__main__':
    a = [x for x in sys.argv[1:] if os.path.isdir(x)]; print('v51 repeated words fixed:', run(os.path.abspath(a[0]) if a else FINAL))
