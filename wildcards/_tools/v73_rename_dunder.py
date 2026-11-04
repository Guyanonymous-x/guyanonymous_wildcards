"""v73: rename wildcard files whose NAME contains a double underscore (e.g. acc_x_display__material.txt) to a single underscore and fix every reference.
A name like __acc_x_display__material__ can be read by a __name__ parser as two references. The mapping is saved in _tools/backup_v72/dunder_map.json (--restore reverses it).
Builders that still generate the old names must be followed by this script (run it with the other v73 scripts, after any rebuild)."""
import os, re, sys, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from paths import FINAL
MP = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'backup_v72', 'dunder_map.json')
REF = re.compile(r'__([A-Za-z0-9_\-/]+?)__(?=[^_A-Za-z0-9]|$)')
def sub_refs(text, mp):
    # references are written __name__; a name that itself contains '__' is matched by trying every known old name longest first
    for old in sorted(mp, key=len, reverse=True):
        text = text.replace('__' + old + '__', '__' + mp[old] + '__')
    return text
if '--restore' in sys.argv:
    mp = json.load(open(MP)); inv = {v: k for k, v in mp.items()}
    for f in sorted(os.listdir(FINAL)):
        if f.endswith('.txt'):
            p = os.path.join(FINAL, f); t = open(p, encoding='utf8').read(); n = sub_refs(t, inv)
            if n != t: open(p, 'w', encoding='utf8', newline='\n').write(n)
    for new, old in inv.items():
        if os.path.exists(os.path.join(FINAL, new + '.txt')): os.rename(os.path.join(FINAL, new + '.txt'), os.path.join(FINAL, old + '.txt'))
    print('restored', len(inv)); sys.exit()
names = [f[:-4] for f in os.listdir(FINAL) if f.endswith('.txt')]
mp = {n: re.sub(r'_{2,}', '_', n) for n in names if '__' in n}
assert not any(v in names for v in mp.values()), 'collision'
assert len(set(mp.values())) == len(mp), 'duplicate targets'
if not mp: print('nothing to do'); sys.exit()
os.makedirs(os.path.dirname(MP), exist_ok=True)
old = json.load(open(MP)) if os.path.exists(MP) else {}; old.update(mp); json.dump(old, open(MP, 'w'), indent=1)
ch = 0
for f in sorted(os.listdir(FINAL)):
    if not f.endswith('.txt'): continue
    p = os.path.join(FINAL, f); t = open(p, encoding='utf8').read()
    if '__' not in t: continue
    n = sub_refs(t, mp)
    if n != t: open(p, 'w', encoding='utf8', newline='\n').write(n); ch += 1
for o, nw in mp.items(): os.rename(os.path.join(FINAL, o + '.txt'), os.path.join(FINAL, nw + '.txt'))
print('renamed', len(mp), 'files; references fixed in', ch, 'files')
