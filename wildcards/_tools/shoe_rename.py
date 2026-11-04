"""Renames the footwear files to the accessory naming scheme:  shoe_<x>_t<n> -> acc_shoe_<x>_<grade>,  shoe_<x> -> acc_shoe_<x>.  References inside every file are rewritten too.  Idempotent."""
import os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from paths import FINAL
GR = {'1': 'basic', '2': 'practical', '3': 'standard', '4': 'fine', '5': 'luxury', '6': 'showpiece'}
def new(n):
    n = re.sub(r'_t([1-6])$', lambda m: '_' + GR[m.group(1)], n)
    return 'acc_' + n
def run(final=FINAL):
    names = {f[:-4] for f in os.listdir(final) if f.startswith('shoe_') and f.endswith('.txt')}
    mp = {n: new(n) for n in names}
    ref = re.compile(r'__(shoe_[A-Za-z0-9_\-]+)__')
    for f in os.listdir(final):
        if not f.endswith('.txt') or f.startswith('acc_shoe_'): continue
        p = os.path.join(final, f); s = open(p, encoding='utf8').read()
        t = ref.sub(lambda m: '__' + mp.get(m.group(1), new(m.group(1))) + '__', s)
        if f[:-4] in mp:
            open(os.path.join(final, mp[f[:-4]] + '.txt'), 'w', encoding='utf8', newline='\n').write(t); os.remove(p)
        elif t != s: open(p, 'w', encoding='utf8', newline='\n').write(t)
    open(os.path.join(final, 'acc_shoe_prompt.txt'), 'w', encoding='utf8', newline='\n').write('__acc_shoe_prompt_master__\n')
    print('shoe files renamed:', len(mp))
if __name__ == '__main__':
    a = [x for x in sys.argv[1:] if os.path.isdir(x)]; run(os.path.abspath(a[0]) if a else FINAL)
