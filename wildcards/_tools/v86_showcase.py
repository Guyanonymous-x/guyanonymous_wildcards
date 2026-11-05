"""v86 showcase: 40 prompts - pinbacks, insignia, adult achievements, kilts, pony, torn clothing."""
import sys, os, random
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import expand as E
from paths import FINAL
from v74_showcase import sizes
files = E.load([FINAL])
RATIOS = [(4, 5), (3, 2), (1, 1), (4, 5), (3, 2), (2, 3), (1, 1), (3, 2)]
def one(ref, seed):
    r = random.Random(seed); return ' '.join(E.clean(E.expand(files, ref, r)).split())
def light(seed):
    s = one('__photostyle_lighting__', seed).rstrip('.'); return 'Photographed with ' + s[0].lower() + s[1:] + '.'
def up(t): return t[0].upper() + t[1:]
def build(off=0):
    S = []; n = 0
    def add(title, ratio, text):
        nonlocal n; n += 1; S.append(('C%02d' % n, title, ratio, text))
    sd = lambda: 8600 + off + n * 7
    def item(ref): return up(one(ref, sd()).rstrip('.')) + '.'
    for k in ['slogans', 'music', 'fandom', 'cause', 'identity', 'event', 'adult', 'designs', 'slogans', 'music']:
        add('pinback ' + k, RATIOS[n % 8], item('__pinback_%s__' % k))
    for s in ['police', 'fire', 'ambulance', 'military']:
        for f in ['', 'medal_', 'pin_']:
            if len([1 for _ in S]) >= 22: break
            add('insignia %s%s' % (f, s), RATIOS[n % 8], item('__insignia_%s%s__' % (f, s)))
    for f in ['badge_ambulance', 'badge_fire']:
        add('insignia ' + f, RATIOS[n % 8], item('__insignia_%s__' % f))
    for f in ['meritbadge', 'medal', 'pin', 'badge']:
        for a in ['dating', 'kink', 'sex', 'fetish']:
            if n >= 34: break
            add('achievement %s %s' % (f, a), RATIOS[n % 8], item('__acc_%s_adult_%s__' % (f, a)))
    for L, k in [(4, 'kilts'), (5, 'kilts'), (6, 'kilts'), (1, 'pony'), (3, 'pony'), (5, 'torn')]:
        add('L%d %s' % (L, k), RATIOS[n % 8], up(one('__adult_l%d_%s__' % (L, k), sd()).rstrip('.')) + '. ' + light(sd() + 3))
    return S
if __name__ == '__main__':
    for i, t, ratio, text in build(): print('##', i, t, ratio, len(text)); print(text); print()
