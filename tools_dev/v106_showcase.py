"""v106 showcase: 40 prompts - bulge classes in panels, three-person groups, wrestling, structured locations, level 3 solo."""
import sys, os, random, re
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import expand as E
from paths import FINAL
from v74_showcase import sizes
files = E.load([FINAL])
RATIOS = [(4, 5), (3, 2), (1, 1), (4, 5), (3, 2), (2, 3), (1, 1), (3, 2)]
def one(ref, seed):
    r = random.Random(seed); t = ' '.join(E.clean(E.expand(files, ref, r)).split())
    if '_group__' in ref or '_location__' in ref:
        for k in range(400):
            if len(t) > 500: break
            t = ' '.join(E.clean(E.expand(files, ref, r)).split())
    return t
import lightfit
def light(seed):
    return '@@L%d@@' % seed
def up(t): return t[0].upper() + t[1:]
NAMES = ['windows_95_era_interface', 'grundig', 'lotus', 'meccano', 'opel', 'kia', 'nissan', 'fujifilm', 'lanvin', 'pocky_glico', 'stanley', 'parker_pens', 'technics', 'motorola', 'mary_quant', 'chris_craft', 'coleman', 'brompton', 'fjallraven', 'steinway_and_sons', 'lenovo_thinkpad', 'nikon', 'a_bathing_ape', 'the_body_shop', 'rickenbacker', 'swissair', 'schiaparelli', 'xiaomi', 'telefunken', 'schwinn', 'opinel', 'bottega_veneta', 'sonos', 'peugeot', 'quiksilver', 'google_material_design', 'in_n_out', 'sas', 'rip_curl', 'selfridges']
KINDS = ['building', 'accessory', 'madeup_vehicle', 'any', 'fashion', 'home', 'tech', 'packaging']
CLIN = ['a clinical three-quarter view', 'a clinical front view', 'a clinical side view', 'a clinical front view']
REFS = (['__adult_l2_panel_wm__'] * 2 + ['__adult_l3_panel_wm__'] * 2 + ['__adult_l2_panel_mm__'] + ['__adult_l3_panel_mm__'] * 2 + ['__adult_l3_panel_ww__']
        + ['__adult_l4_panel_wm__', '__adult_l4_panel_mm__', '__adult_l5_panel_wm_vaginal__', '__adult_l6_panel_mm_oral__', '__adult_l6_panel_ww_scissor__', '__adult_l6_panel_wm_anal__']
        + ['__adult_l1_panel_wm__', '__adult_l1_panel_mm__', '__adult_l2_panel_ww__']
        + ['__adult_l%d_group__' % n for n in range(1, 7)]
        + ['__adult_l4_wrestling_mm__', '__adult_l5_wrestling_mm__', '__adult_l6_wrestling_mm__']
        + ['__adult_l%d_location__' % n for n in range(1, 7)]
        + ['__adult_l3_masturbation_f__', '__adult_l3_masturbation_m__', '__adult_l3_solo_prompt__', '__adult_l3_solo_prompt__']
        + ['__kink_panel_wm__', '__kink_panel_ww__', '__adult_l2_pose_scene__', '__adult_l5_pose_scene__'])
SCENES = ('fluid_scene_semen', 'fluid_scene_squirt')
def build(off=0):
    S = []; n = 0
    for ref in REFS:
        n += 1; seed = 9700 + off + n * 7
        if False:
            t = open(os.path.join(FINAL, ref.strip('_') + '.txt')).read().rstrip('\n').split('\n'); k = sum(1 for x in REFS[:n] if x == ref) - 1
            text = ' '.join(E.clean(E.expand(files, t[k % len(t)], random.Random(seed))).split())
        else:
            text = one(ref, seed)
        text = text[0].upper() + text[1:]
        if False:
            text = 'A %s of the bare pelvis of an adult man standing, on a plain pale grey background with soft even studio lighting. %s' % (CLIN[n % 4].replace('a clinical', 'clinical'), text)
        text = text.replace(', .', '.').replace(',.', '.')
        S.append(('M%02d' % n, ref.strip('_'), RATIOS[n % 8], text))
    return S
if __name__ == '__main__':
    for i, t, ratio, text in build(): print('##', i, t, ratio, len(text)); print(text); print()
