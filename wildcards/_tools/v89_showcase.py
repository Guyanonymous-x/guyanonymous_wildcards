"""v89 showcase: 40 prompts - pinbacks, insignia, adult achievements, kilts, pony, torn clothing."""
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
NAMES = ['vans', 'converse', 'land_rover']
def build(off=0):
    S = []; n = 0
    def add(title, ratio, text):
        nonlocal n; n += 1; S.append(('F%02d' % n, title, ratio, text))
    sd = lambda: 8900 + off + n * 7
    for i in range(40):
        b = NAMES[i % 3]; nm = (i // 3) % 2
        add('brand ' + b + (' named' if nm else ''), RATIOS[n % 8], one('__maker_bs_%s%s__' % (b, '_named' if nm else ''), sd()) + ' ' + one('The subject is __bs_subject_any__, designed completely in that style and __bs_view__.', sd() + 1))
    return S
if __name__ == '__main__':
    for i, t, ratio, text in build(): print('##', i, t, ratio, len(text)); print(text); print()
