"""v87 showcase: 40 prompts - pinbacks, insignia, adult achievements, kilts, pony, torn clothing."""
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
def build(off=0):
    S = []; n = 0
    def add(title, ratio, text):
        nonlocal n; n += 1
        m = re.search(r'@@L(\d+)@@', text)
        if m:
            ls = lightfit.pick(text[:m.start()], one, int(m.group(1))); text = text[:m.start()] + 'Photographed with ' + ls[0].lower() + ls[1:] + '.'
        S.append(('D%02d' % n, title, ratio, text))
    sd = lambda: 8700 + off + n * 7
    for L in (1, 2, 3, 1, 2, 3, 1, 2, 3):
        add('L%d men wrestling' % L, RATIOS[n % 8], up(one('__adult_l%d_wrestling_mm__' % L, sd()).rstrip('.')) + ', ' + one('__adult_l%d_expression__' % L, sd() + 1) + '. ' + light(sd() + 3))
    for k in ['slogans', 'music', 'fandom', 'cause', 'identity', 'adult']:
        add('pinback ' + k, RATIOS[n % 8], up(one('__pinback_%s__' % k, sd()).rstrip('.')) + '.')
    for s_ in ('police', 'ambulance'):
        add('insignia ' + s_, RATIOS[n % 8], up(one('__insignia_%s__' % s_, sd()).rstrip('.')) + '.')
    for b in ['off_white', 'bosch_professional', 'makita', 'sodastream', 'off_white_named', 'bosch_professional_named', 'makita_named', 'sodastream_named']:
        add('brand ' + b, RATIOS[n % 8], one('__maker_bs_%s__' % b, sd()) + ' ' + one('The subject is __bs_subject_any__, designed completely in that style and __bs_view__.', sd() + 1))
    for L, g in [(1, 'pose'), (2, 'body'), (3, 'pose'), (4, 'setting'), (5, 'group'), (2, 'location'), (3, 'object'), (4, 'pose'), (5, 'pose')]:
        add('L%d %s' % (L, g), RATIOS[n % 8], up(one('__adult_l%d_%s__' % (L, g), sd()).rstrip('.')) + ', ' + one('__adult_l%d_expression__' % L, sd() + 1) + '. ' + light(sd() + 3))
    for L, k in [(2, 'pony'), (4, 'pony'), (3, 'torn'), (6, 'torn'), (5, 'kilts'), (4, 'kilts')]:
        add('L%d %s' % (L, k), RATIOS[n % 8], up(one('__adult_l%d_%s__' % (L, k), sd()).rstrip('.')) + '. ' + light(sd() + 3))
    return S
if __name__ == '__main__':
    for i, t, ratio, text in build(): print('##', i, t, ratio, len(text)); print(text); print()
