"""v85 showcase: 40 prompts from wildcard text plus joining words - level 6 scenes, messy, wrestling, gear, and L1-L5 scenes with expression and body-change modifiers."""
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
        nonlocal n; n += 1; S.append(('B%02d' % n, title, ratio, text))
    sd = lambda: 8500 + off + n * 7
    for g in ['pose', 'body', 'setting', 'object', 'group', 'location', 'solo_prompt', 'group_prompt']:
        ref = '__adult_l6_%s__' % g
        add('L6 ' + g, RATIOS[n % 8], up(one(ref, sd()).rstrip('.')) + '. ' + light(sd() + 3))
    for L in (1, 2, 3, 4, 5, 6, 3, 5):
        add('L%d messy' % L, RATIOS[n % 8], up(one('__adult_l%d_messy__' % L, sd()).rstrip('.')) + ', ' + one('__adult_l%d_expression__' % L, sd() + 1) + '. ' + light(sd() + 3))
    for L in (1, 2, 3, 4, 5, 6, 2, 4):
        add('L%d wrestling' % L, RATIOS[n % 8], up(one('__adult_l%d_wrestling__' % L, sd()).rstrip('.')) + ', ' + one('__adult_l%d_bodychange__' % L, sd() + 1) + '. ' + light(sd() + 3))
    for g in ['kilts', 'tailoring', 'uniforms', 'materials', 'garments', 'furniture', 'roleplay', 'fetish_focus']:
        add('gear ' + g, RATIOS[n % 8], up(one('__adult_gear_%s__' % g, sd()).rstrip('.')) + '. ' + light(sd() + 3))
    for L in (1, 2, 3, 4, 5, 1, 3, 5):
        g = ['pose', 'body', 'setting', 'object', 'group', 'location'][n % 6]
        add('L%d %s + modifiers' % (L, g), RATIOS[n % 8], up(one('__adult_l%d_%s__' % (L, g), sd()).rstrip('.')) + ', ' + one('__adult_l%d_expression__' % L, sd() + 1) + ', ' + one('__adult_l%d_bodychange__' % L, sd() + 2) + '. ' + light(sd() + 3))
    return S
if __name__ == '__main__':
    for i, t, ratio, text in build(): print('##', i, t, ratio, len(text)); print(text); print()
