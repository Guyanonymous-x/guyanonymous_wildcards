"""Test expander - shows what a template turns into, without needing your image tool.
   python _tools/expand.py prompt_master_by_age            -> 3 sample prompts
   python _tools/expand.py prompt_master_by_age 5 42       -> 5 prompts, random seed 42
   python _tools/expand.py --check                         -> verify that every __reference__ points to an existing file
   (Handles __name__ and {a|b|} choices. It does not understand "5::" weight prefixes, so lines that use them show the prefix.)"""
import re, sys, random, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from paths import wc_dir
def load(dirs):
    files = {}
    for d in reversed(dirs):
        for f in os.listdir(d):
            if f.endswith('.txt'): files[f[:-4]] = [l.rstrip('\r\n') for l in open(os.path.join(d, f), encoding='utf8', errors='replace')]
    return files
REF = re.compile(r'__([A-Za-z0-9_\-/]+)__')
def check(files, names):
    bad = {}
    for n in names:
        for l in files[n]:
            for r in REF.findall(l):
                if r not in files: bad.setdefault(n, set()).add(r)
    return bad
def expand(files, text, rng):
    for _ in range(25):
        new = re.sub(r'\{([^{}]*)\}', lambda m: rng.choice(m.group(1).split('|')), text)
        new = REF.sub(lambda m: rng.choice(files[m.group(1)]) if m.group(1) in files else m.group(0), new)
        if new == text: break
        text = new
    return text
def clean(s):
    s = re.sub(r'\s+', ' ', s); s = re.sub(r'\s+([.,;:])', r'\1', s); s = re.sub(r'([.,;:])\1+', r'\1', s); return s.strip()
if __name__ == '__main__':
    a = [x for x in sys.argv[1:] if not os.path.isdir(x)]; files = load([wc_dir()])
    if a and a[0] == '--check':
        bad = check(files, list(files)); print(len(files), 'wildcard files;', 'every reference resolves' if not bad else f'{len(bad)} files have unresolved references:')
        for k, v in list(bad.items())[:30]: print('  ', k, '->', sorted(v)[:6])
        sys.exit(1 if bad else 0)
    tpl = a[0] if a else 'prompt_master_by_age'; n = int(a[1]) if len(a) > 1 else 3; seed = int(a[2]) if len(a) > 2 else None
    if tpl not in files: sys.exit(f'No wildcard file named {tpl}.txt in {wc_dir()}')
    rng = random.Random(seed)
    for _ in range(n): print(clean(expand(files, rng.choice(files[tpl]), rng))); print()
