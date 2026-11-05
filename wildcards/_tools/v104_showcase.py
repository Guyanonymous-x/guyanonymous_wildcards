"""v104 showcase: 40 prompts - circumcision modifier on men, pubic hair shapes, stubble and patchy."""
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
NAMES = ['windows_95_era_interface', 'grundig', 'lotus', 'meccano', 'opel', 'kia', 'nissan', 'fujifilm', 'lanvin', 'pocky_glico', 'stanley', 'parker_pens', 'technics', 'motorola', 'mary_quant', 'chris_craft', 'coleman', 'brompton', 'fjallraven', 'steinway_and_sons', 'lenovo_thinkpad', 'nikon', 'a_bathing_ape', 'the_body_shop', 'rickenbacker', 'swissair', 'schiaparelli', 'xiaomi', 'telefunken', 'schwinn', 'opinel', 'bottega_veneta', 'sonos', 'peugeot', 'quiksilver', 'google_material_design', 'in_n_out', 'sas', 'rip_curl', 'selfridges']
KINDS = ['building', 'accessory', 'madeup_vehicle', 'any', 'fashion', 'home', 'tech', 'packaging']
CLIN = ['a clinical three-quarter view', 'a clinical front view', 'a clinical side view', 'a clinical front view']
REFS = (['__m_body_genitals_semi_v2__'] * 4 + ['__m_body_genitals_post_v2__'] * 4 + ['__v104_show_man_flaccid__'] * 2 + ['__v104_show_man_erect__'] * 2
        + ['__fluid_scene_semen__'] * 4 + ['__fluid_scene_squirt__'] * 4
        + ['__adult_l%d_masturbation_%s__' % (L, 'f' if L % 2 else 'm') for L in range(1, 7)]
        + ['__groom_f_hygiene_prompt__'] * 2 + ['__groom_m_hygiene_prompt__'] * 2 + ['__groom_m_grooming_prompt__'] * 2 + ['__groom_f_beauty_prompt__'] * 2 + ['__groom_unisex_care_prompt__'] * 2
        + ['__v104_show_woman_shape__'] * 1 + ['__v104_show_woman_stubble__'] * 1 + ['__v104_show_woman_patchy__'] * 1 + ['__v104_show_man_shape__'] * 1)
SCENES = ('fluid_scene_semen', 'fluid_scene_squirt')
def build(off=0):
    S = []; n = 0
    for ref in REFS:
        n += 1; seed = 9700 + off + n * 7
        if ref.startswith('__fluid_scene_'):
            t = open(os.path.join(FINAL, ref.strip('_') + '.txt')).read().rstrip('\n').split('\n'); k = sum(1 for x in REFS[:n] if x == ref) - 1
            text = ' '.join(E.clean(E.expand(files, t[k % len(t)], random.Random(seed))).split())
        else:
            text = one(ref, seed)
        text = text[0].upper() + text[1:]
        if ref in ('__m_body_genitals_semi_v2__', '__m_body_genitals_post_v2__'):
            text = 'A %s of the bare pelvis of an adult man standing, on a plain pale grey background with soft even studio lighting. %s' % (CLIN[n % 4].replace('a clinical', 'clinical'), text)
        text = text.replace(', .', '.').replace(',.', '.')
        S.append(('M%02d' % n, ref.strip('_'), RATIOS[n % 8], text))
    return S
if __name__ == '__main__':
    for i, t, ratio, text in build(): print('##', i, t, ratio, len(text)); print(text); print()
