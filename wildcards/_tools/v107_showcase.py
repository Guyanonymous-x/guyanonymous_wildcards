"""v107 showcase: 40 prompts - yoga, dance-class and martial-arts prompts from the fuller v107 lists, the areola/nipple ladder and the anal-area files."""
import sys, os, random, re
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import expand as E
from paths import FINAL
from v74_showcase import sizes
files = E.load([FINAL])
RATIOS = [(2, 3), (4, 5), (3, 2), (1, 1)]
BG = 'against a plain pale grey background under soft even studio light'
NUDE = 'She is completely nude, wearing no clothing at all.'
NIP = ('A clinical close-up of one bare breast of an adult woman in her early thirties, turned partly toward the left side of the frame, ' + BG + '. ' + NUDE + ' Nipple and areola: __f_body_nipples__.')
AF = ('A clinical close view from behind of the bare buttocks and anal area of an adult woman in her early thirties bending forward slightly, in three-quarter view, ' + BG + '. ' + NUDE + ' Anal area: __f_body_anus__.')
AM = ('A clinical close view from behind of the bare buttocks and anal area of an adult man in his early thirties bending forward slightly, in three-quarter view, ' + BG + '. He is completely nude, wearing no clothing at all, and his scrotum hangs naturally visible between his thighs. Anal area: __m_body_anus__.')
REFS = []
for a in ('yoga', 'dance_classes', 'martial_arts'):
    REFS += ['__act_%s_prompt__' % a] * 5 + ['__act_%s_frame_prompt__' % a] * 2 + ['__act_%s_scene_prompt__' % a]
REFS += [NIP] * 8 + [AF] * 4 + [AM] * 4
def one(ref, seed):
    r = random.Random(seed)
    if ref == NIP:   # walk the size ladder in order across the eight nipple prompts
        lad = [l.strip() for l in open(os.path.join(FINAL, 'f_body_nipples.txt'), encoding='utf8') if 'centimetres' in l or 'thumbnail' in l]
        return ref.replace('__f_body_nipples__', lad[(seed // 7) * 5 % len(lad)])
    return ' '.join(E.clean(E.expand(files, ref, r)).split())
def build(off=0):
    S = []; n = 0
    for ref in REFS:
        n += 1; seed = 10700 + off + n * 7
        text = one(ref, seed); text = text[0].upper() + text[1:]
        text = text.replace(', .', '.').replace(',.', '.')
        tag = 'f_body_nipples' if ref == NIP else 'f_body_anus' if ref == AF else 'm_body_anus' if ref == AM else ref.strip('_')
        S.append(('M%02d' % n, tag, RATIOS[n % 4] if ref.startswith('__') else (1, 1), text))
    return S
