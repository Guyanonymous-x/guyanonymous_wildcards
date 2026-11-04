"""v84 showcase: 40 adult prompts (8 per level) built only from wildcard text plus joining words, plus a style line from the photography lists."""
import sys, os, random
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import expand as E
from paths import FINAL
from v74_showcase import sizes
import v84_ad
files = E.load([FINAL])
RATIOS = [(4, 5), (3, 2), (1, 1), (4, 5), (3, 2), (2, 3), (1, 1), (3, 2)]
GENS = ['pose', 'body', 'setting', 'object', 'group', 'location', 'solo_prompt', 'group_prompt']
def one(ref, seed):
    r = random.Random(seed); return ' '.join(E.clean(E.expand(files, ref, r)).split())
def build(off=0):
    S = []
    for L in range(1, 6):
        for k, g in enumerate(GENS):
            n = (L - 1) * 8 + k; seed = 8400 + off + n * 7
            ref = '__adult_l%d_%s__' % (L, g) if not g.endswith('prompt') else '__adult_l%d_%s__' % (L, g)
            scene = one(ref, seed).rstrip('.')
            style = one('__photostyle_lighting__', seed + 3).rstrip('.')
            scene = scene[0].upper() + scene[1:]
            text = scene + '. Photographed with ' + style[0].lower() + style[1:] + '.'
            S.append(('A%02d' % (n + 1), 'L%d %s' % (L, g), RATIOS[k], text))
    return S
if __name__ == '__main__':
    for i, t, ratio, text in build(): print('##', i, t, ratio, len(text)); print(text); print()
