"""v94 showcase: 40 prompts - fake name system (signs, labels, packaging, people, media)."""
import sys, os, random
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import expand as E
from paths import FINAL
from v74_showcase import sizes
files = E.load([FINAL])
RATIOS = [(4, 5), (3, 2), (1, 1), (4, 5), (3, 2), (2, 3), (1, 1), (3, 2)]
def one(ref, seed):
    r = random.Random(seed); return ' '.join(E.clean(E.expand(files, ref, r)).split())
OUT = ['name_liquor_store_sign', 'name_bar_sign', 'name_pharmacy_sign', 'name_bookshop_sign', 'name_bakery_sign', 'name_grocery_sign', 'name_cafe_sign', 'name_hotel_sign', 'name_garage_sign', 'name_cinema_sign', 'name_sign_shopfront', 'name_sign_company', 'name_sign_restaurant', 'name_vehicle_livery', 'name_pub_sign']
IN = ['name_label_product_soft', 'name_label_product_sweet', 'name_label_product_spirit', 'name_label_product_household', 'name_label_price', 'name_tag_person', 'name_tag_clothing', 'name_poster', 'name_hero', 'name_comic_cover', 'name_book_cover', 'name_record', 'name_movie', 'name_game', 'name_business_card', 'name_business_card', 'name_business_card', 'name_business_card_simple', 'name_logo', 'name_logo', 'name_cap', 'name_cap', 'name_cap', 'name_tshirt', 'name_tshirt', 'name_tshirt', 'name_merch_other', 'name_print']
ITEMS = [(x, 'out') for x in OUT[:15]] + [(x, 'in') for x in IN[:25]]
def build(off=0):
    S = []; n = 0
    for it, m in ITEMS:
        n += 1; seed = 9400 + off + n * 7
        ref = '__%s_prompt__' % it
        base = one(ref, seed)
        light = one('__name_light_night__' if ('neon' in base or 'night' in base.lower()) else '__name_light_%sdoor__' % ('out' if m == 'out' else 'in'), seed + 3)
        text = base + ' Photographed in ' + light.rstrip('.').lstrip() + '.'
        S.append(('K%02d' % n, it.replace('name_', ''), RATIOS[n % 8], text))
    return S
if __name__ == '__main__':
    for i, t, ratio, text in build(): print('##', i, t, ratio, len(text)); print(text); print()
