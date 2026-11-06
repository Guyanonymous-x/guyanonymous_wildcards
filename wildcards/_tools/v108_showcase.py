"""v108 showcase: 40 prompts - level-6 same-sex endings, level-1 and level-3 wet locations in swimwear, level-1 panels, activity frame and scene prompts with on-location styles, and navel close-ups."""
import sys, os, random, re
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import expand as E
from paths import FINAL
from v74_showcase import sizes
files = E.load([FINAL])
RATIOS = [(4, 5), (3, 2), (1, 1), (4, 5), (3, 2), (2, 3), (1, 1), (3, 2)]
BG = 'against a plain pale grey background under soft even studio light'
NAVF = ('A clinical close-up of the bare stomach of an adult woman in her early thirties standing upright facing the camera, ' + BG + '. The frame runs from just below her ribs to just above her hips, with the navel in the centre. She is completely nude, wearing no clothing at all. The close-up shows __body_navel__.')
NAVM = ('A clinical close-up of the bare stomach of an adult man in his early thirties standing upright facing the camera, ' + BG + '. The frame runs from just below his ribs to just above his hips, with the navel in the centre. He is completely nude, wearing no clothing at all. The close-up shows __body_navel__.')
WET = re.compile(r'swim|bikini')
FRAMES = ['archery', 'boxing', 'piano', 'surfing', 'pottery', 'chess_and_board_games', 'rock_climbing', 'baking', 'cycling', 'violin']
SCENES = ['dj_and_electronic_music', 'beekeeping', 'rowing', 'stargazing', 'woodworking', 'sailing']
REFS = (['__adult_l6_panel_mm__'] * 4 + ['__adult_l6_panel_mm_anal__', '__adult_l6_panel_mm_oral__']
        + ['__adult_l6_panel_ww__'] * 4 + ['__adult_l6_panel_ww_scissor__', '__adult_l6_panel_ww_oral__']
        + ['__adult_l6_location__'] * 2 + ['__adult_l1_location__'] * 3 + ['__adult_l3_location__'] * 2 + ['__adult_l1_panel_wm__'] * 2
        + ['__act_%s_frame_prompt__' % a for a in FRAMES] + ['__act_%s_scene_prompt__' % a for a in SCENES]
        + [NAVF, NAVM, NAVF])
def one(ref, seed):
    r = random.Random(seed); t = ' '.join(E.clean(E.expand(files, ref, r)).split())
    if ref in ('__adult_l1_location__', '__adult_l3_location__'):
        for k in range(2000):
            if WET.search(t): break
            t = ' '.join(E.clean(E.expand(files, ref, r)).split())
    return t
def build(off=0):
    S = []; n = 0; seen = set()
    for ref in REFS:
        n += 1; seed = 10800 + off + n * 7
        text = one(ref, seed)
        while text in seen: seed += 1; text = one(ref, seed)
        seen.add(text)
        text = text[0].upper() + text[1:]
        text = text.replace(', .', '.').replace(',.', '.')
        tag = 'body_navel' if ref in (NAVF, NAVM) else ref.strip('_')
        S.append(('M%02d' % n, tag, RATIOS[n % 8] if ref.startswith('__') else (1, 1), text))
    return S
if __name__ == '__main__':
    for i, t, ratio, text in build(): print('##', i, t, ratio, len(text)); print(text); print()
