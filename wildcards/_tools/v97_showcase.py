"""v97 showcase: 40 prompts - pinbacks, insignia, adult achievements, kilts, pony, torn clothing."""
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
REFS = ['__acc_keychain_prompt__', '__acc_glove_prompt__', '__acc_hat_prompt__', '__acc_backpack_prompt__', '__acc_umbrella_prompt__', '__acc_lanyard_prompt__', '__acc_shoe_prompt__', '__acc_necklace_prompt__', '__acc_apron_prompt__', '__clothing_couture_prompt__', '__clothing_garment_prompt__', '__clothing_outerwear_prompt__', '__clothing_garment_shop_prompt__', '__obj_drink_prompt__', '__obj_food_prompt__', '__obj_instrument_prompt__', '__obj_armor_prompt__',
 '__name_business_card_prompt__', '__name_logo_prompt__', '__name_cap_prompt__', '__name_tshirt_prompt__', '__name_merch_other_prompt__', '__name_liquor_store_sign_prompt__', '__name_pharmacy_sign_prompt__', '__name_diner_sign_prompt__', '__name_label_product_soft_prompt__', '__name_label_product_spirit_prompt__', '__name_book_cover_prompt__', '__name_comic_cover_prompt__', '__name_record_prompt__', '__bs_prompt__', '__bs_prompt__', '__bs_building_prompt__', '__bs_accessory_prompt__', '__clothing_onesie_hybrid_medical_female__', '__clothing_uniform_tee_cosplay_archetypes__', '__clothing_onesie_plush_formal__', '__name_hero_prompt__', '__name_movie_prompt__', '__name_print_prompt__']
def build(off=0):
    S = []; n = 0
    for ref in REFS:
        n += 1; seed = 9700 + off + n * 7
        text = one(ref, seed); text = text[0].upper() + text[1:]
        if not ('name_' in ref or 'bs_' in ref): text = text.rstrip() + ('' if text.rstrip().endswith('.') else '.') + ' Shown in a clean studio photograph with soft even light.'
        S.append(('M%02d' % n, ref.strip('_'), RATIOS[n % 8], text))
    return S
if __name__ == '__main__':
    for i, t, ratio, text in build(): print('##', i, t, ratio, len(text)); print(text); print()
