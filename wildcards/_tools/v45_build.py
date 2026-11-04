"""v45: adults-only accessories (objects only): merkins, pasties, butt plugs, dildos, vibrators, general adult toys, sensation-play toys, and chastity devices split by anatomy (chastity_penis, _vagina, _clitoris, _nipple, _anus) replacing the single acc_chastity family. Idempotent."""
import os, re, sys, glob, random, zlib
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from paths import FINAL
import v44_build as B4, v45_data as D
CL = B4.CL
FAM = [('acc_merkin', D.MERKIN), ('acc_pasties', D.PASTIES), ('acc_buttplug', D.BUTTPLUG), ('acc_dildo', D.DILDO), ('acc_vibrator', D.VIBR), ('acc_adulttoy', D.ATOY), ('acc_sensation', D.SENS)]
def build():
    G = {}
    for pre, rows in FAM:
        G.update(B4.grp(pre, rows, 5)); G[pre + '_prompt'] = [f'__{pre}__']
    ch = []
    for part, rows in D.CH.items():
        pre = 'chastity_' + part; G.update(B4.grp(pre, rows, 5)); G[pre + '_prompt'] = [f'__{pre}__']; ch.append(f'__{pre}_prompt__')
    G['chastity_prompt'] = ch; G['acc_chastity_prompt'] = ch
    G['v45_entry_points'] = [f'__{p}_prompt__' for p, _ in FAM] + ch
    return G
def _wr(folder, name, lines): open(os.path.join(folder, name + '.txt'), 'w', encoding='utf8', newline='\n').write('\n'.join(lines) + '\n')
def run(final, prefix=''):
    for f in glob.glob(os.path.join(final, prefix + 'acc_chastity*.txt')): os.remove(f)
    G = build()
    for n, l in G.items(): _wr(final, prefix + n, l)
    # keep old entry points resolvable
    for f in glob.glob(os.path.join(final, prefix + 'v38_entry_points.txt')):
        t = open(f, encoding='utf8').read(); open(f, 'w', encoding='utf8', newline='\n').write(t)
    print('v45:', len(G), 'files'); return G
def export_aoo(out, prefix='aoo_'):
    for f in glob.glob(os.path.join(out, prefix + 'acc_chastity*.txt')): os.remove(f)
    G = build(); names_ = set(G); ref = re.compile(r'__([A-Za-z0-9_\-/]+)__'); n = 0
    for name, lines in G.items():
        keep = list(dict.fromkeys(ref.sub(lambda m: '__' + prefix + m.group(1) + '__' if m.group(1) in names_ else m.group(0), l) for l in lines))
        if not name.endswith('prompt') and 'entry_points' not in name: random.Random(zlib.crc32(name.encode())).shuffle(keep)
        _wr(out, prefix + name, keep); n += 1
    return n
if __name__ == '__main__':
    a = [x for x in sys.argv[1:] if os.path.isdir(x)]; run(os.path.abspath(a[0]) if a else FINAL)
