"""v88 showcase: 40 prompts - pinbacks, insignia, adult achievements, kilts, pony, torn clothing."""
import sys, os, random, re
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import expand as E
from paths import FINAL
from v74_showcase import sizes
files = E.load([FINAL])
RATIOS = [(4, 5), (3, 2), (1, 1), (4, 5), (3, 2), (2, 3), (1, 1), (3, 2)]
def one(ref, seed):
    r = random.Random(seed); return ' '.join(E.clean(E.expand(files, ref, r)).split())
import lightfit
def light(seed):
    return '@@L%d@@' % seed
def up(t): return t[0].upper() + t[1:]
NAMES = ['rolls_royce', 'mini', 'land_rover', 'volkswagen', 'bmw', 'mercedes_benz', 'toyota', 'tesla', 'louis_vuitton', 'gucci', 'hermes', 'ralph_lauren', 'lacoste', 'tiffany_and_co', 'lego', 'vans', 'converse', 'pepsi', 'guinness', 'starbucks', 'mcdonalds', 'braun', 'nintendo', 'rolex', 'harley_davidson']
def build(off=0):
    S = []; n = 0
    def add(title, ratio, text):
        nonlocal n; n += 1; S.append(('E%02d' % n, title, ratio, text))
    sd = lambda: 8800 + off + n * 7
    for i, b in enumerate(NAMES):
        add('brand ' + b + (' named' if i % 2 else ''), RATIOS[n % 8], one('__maker_bs_%s%s__' % (b, '_named' if i % 2 else ''), sd()) + ' ' + one('The subject is __bs_subject_any__, designed completely in that style and __bs_view__.', sd() + 1))
    for b in NAMES[:15]:
        add('brand ' + b + ' again', RATIOS[n % 8], one('__maker_bs_%s__' % b, sd()) + ' ' + one('The subject is __bs_subject_any__, designed completely in that style and __bs_view__.', sd() + 1))
    return S
if __name__ == '__main__':
    for i, t, ratio, text in build(): print('##', i, t, ratio, len(text)); print(text); print()
