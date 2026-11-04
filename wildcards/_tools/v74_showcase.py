"""v74 showcase: 40 prompts built only from wildcard text plus joining words. usage: python3 v74_showcase.py [seed_offset]"""
import sys, os, re, random, math, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import expand as E
from paths import FINAL
files = E.load([FINAL])
BAD = re.compile(r'cameltoe|nude|topless|bottomless|lingerie|fetish|latex|bikini|swimsuit|underwear|sheer|see-through|\bbra\b|boxer|snorkel|lounge ?wear|pyjama|robe\b', re.I)
def pull(ref, seed):
    r = random.Random(seed)
    for _ in range(300):
        t = E.clean(E.expand(files, ref, r))
        if not BAD.search(t): return ' '.join(t.split())
    return t
def sentence(t): return t if t[-1:] in '.!?' else t + '.'
def cap(t): return t[0].upper() + t[1:]
ORD3 = ['top left', 'top centre', 'top right', 'middle left', 'centre', 'middle right', 'bottom left', 'bottom centre', 'bottom right']
ORD2 = ['top left', 'top right', 'bottom left', 'bottom right']
def grid(n, what, refs, seed, tail=''):
    cells = []
    for i in range(n):
        for k in range(40):
            c = pull(refs[i] if isinstance(refs, list) else refs, seed + i * 13 + k * 1009).rstrip('.')
            c = re.sub(r'^(A collectable piece|Ephemera for a collection), ', '', c)
            if c not in cells: break
        cells.append(c)
    if n == 9: head = 'A grid of nine separate images in three rows of three, each cell showing a different %s on a plain neutral background with even spacing.' % what; names = ORD3
    else: head = 'A grid of four separate images in two rows of two, each cell showing a different %s on a plain neutral background with even spacing.' % what; names = ORD2
    return ' '.join([head] + ['In the %s cell, %s.' % (names[i], c[0].lower() + c[1:] if not c.startswith(('"',)) else c) for i, c in enumerate(cells)] + ([tail] if tail else []))
def sizes(rw, rh):
    out = []
    for P in (1024 * 1024, 1408 * 1408):
        w = math.sqrt(P * rw / rh); w16 = round(w / 16) * 16; h16 = round(P / w16 / 16) * 16
        out.append((w16, h16))
    return out
BOOKS = ['__book_%s_phrase__' % s for s in ('novel', 'cookbook', 'field_guide', 'textbook', 'picture_book', 'poetry_collection', 'detective_story', 'technical_manual')] + ['__book_phrase__']
SIGNS = ['__sign_%s_look__' % s for s in ('shop_fascia', 'hanging_pub_sign', 'neon_sign', 'chalkboard_menu', 'enamel_plate', 'street_name_plate', 'ship_name_board', 'licence_plate', 'brass_nameplate')]
ADS = ['__ad_%s_look__' % s for s in ('enamel_advertising_sign', 'tin_advertising_sign', 'neon_advertising_sign', 'cardboard_shop_display', 'mirror_advertisement', 'thermometer_sign', 'cinema_poster', 'trade_calendar', 'clock_advertisement')]
CONT = ['__container_%s_look__' % s for s in ('biscuit_tin', 'tea_caddy', 'sardine_tin', 'glass_jar', 'glass_bottle', 'cylinder_canister', 'paint_can', 'cigar_box', 'cardboard_carton')]
def build(off=0):
    S = []   # (id, title, ratio, text, note)
    add = lambda i, t, ratio, text: S.append((i, t, ratio, text))
    P = lambda ref, s: pull(ref, off + s)
    add('S01', 'reading scene with a person', (4, 5), 'A cosy reading scene. ' + P('__f_create_random_woman_w_clothes__', 1) + ' ' + cap(P('__reading_scene_prompt__', 2)))
    add('S02', 'shop front with lettering', (3, 2), 'A street corner at a shop. ' + P('__sign_shopfront_prompt__', 3) + ' ' + P('__setting_conditions_any__', 4))
    add('S03', 'run of shop signs', (16, 9), P('__sign_street_scene_prompt__', 5) + ' ' + P('__setting_conditions_any__', 6))
    add('S04', 'painted wall ads', (4, 5), P('__ad_wall_scene_prompt__', 7))
    add('S05', 'pantry shelf of labelled containers', (3, 2), P('__container_pantry_prompt__', 8))
    add('S06', 'sports car interior', (3, 2), P('__vint2_sports_car_scene_prompt__', 9))
    add('S07', 'airliner flight deck', (3, 2), P('__vint2_airliner_flight_deck_scene_prompt__', 10))
    add('S08', 'ship bridge', (16, 9), P('__vint2_ship_bridge_scene_prompt__', 11))
    add('S09', 'steam locomotive cab', (4, 5), P('__vint2_steam_locomotive_cab_scene_prompt__', 12))
    add('S10', 'Tudor house', (4, 5), P('__bld_s_tudor_scene__', 13))
    add('S11', 'machiya townhouse', (3, 2), P('__bld_v_machiya_scene__', 14))
    add('S12', 'kasbah', (1, 1), P('__bld_v_kasbah_scene__', 15))
    add('S13', 'brutalist building', (2, 3), P('__bld_s_brutalist_scene__', 16))
    add('S14', 'three-source chimera', (3, 2), P('__cb_prompt_three__', 17))
    add('S15', 'human and animal hybrid', (4, 5), P('__cb_prompt_human__', 18))
    add('S16', 'winged creature', (16, 9), P('__cb_prompt_winged__', 19))
    add('S17', 'person using fire magic', (3, 2), P('__pw_person_who__', 20) + ' The person is using a power in ' + P('__cb_habitat__', 21) + '. ' + P('__pw_fire_magic_prompt__', 22))
    add('S18', 'lightning power scene', (16, 9), 'A dramatic scene in ' + P('__cb_habitat__', 23) + '. ' + P('__pw_lightning_magic_prompt__', 24) + ' A creature, ' + P('__cb_hybrid_two__', 25) + ', faces it.')
    add('S19', 'postcards', (3, 2), P('__postcard_spread_prompt__', 26))
    add('S20', 'atlas', (1, 1), P('__atlas_prompt__', 27))
    add('S21', 'ephemera spread', (3, 2), P('__eph_spread_prompt__', 28))
    add('S22', 'stamp', (1, 1), P('__stamp_prompt__', 29))
    add('S23', 'graded trading card', (2, 3), P('__card_graded_prompt__', 30))
    add('S24', 'rare book', (4, 5), P('__rb_prompt__', 31))
    add('S25', 'graded comic', (2, 3), P('__graded_comic_prompt__', 32))
    add('G01', 'books grid', (1, 1), grid(9, 'book', BOOKS, off + 40))
    add('G02', 'magazines grid', (1, 1), grid(4, 'magazine cover', '__mag_short__', off + 41))
    add('G03', 'signs grid', (1, 1), grid(9, 'sign', SIGNS, off + 42))
    add('G04', 'advertising signs grid', (1, 1), grid(9, 'advertisement', ADS, off + 43))
    add('G05', 'tins and containers grid', (1, 1), grid(9, 'labelled container', CONT, off + 44))
    add('G06', 'vehicle interiors grid', (1, 1), grid(4, 'vehicle interior', ['__vint2_%s_short__' % c for c in ('sports_car', 'train_carriage', 'ship_bridge', 'steam_locomotive_cab')], off + 45))
    add('G07', 'architectural styles grid', (1, 1), grid(9, 'building', '__bld_style_short__', off + 46))
    add('G08', 'vernacular buildings grid', (1, 1), grid(9, 'building', '__bld_vern_short__', off + 47))
    add('G09', 'single-animal creatures grid', (1, 1), grid(9, 'creature', '__cb_one__', off + 48))
    add('G10', 'hybrids grid', (1, 1), grid(4, 'hybrid creature', '__cb_hybrid_two__', off + 49))
    add('G11', 'powers grid', (1, 1), grid(9, 'magical or energy effect', '__pw_short__', off + 50))
    add('G12', 'stamps grid', (1, 1), grid(9, 'postage stamp', '__stamp_look__', off + 51))
    add('G13', 'trading cards grid', (1, 1), grid(9, 'trading card', '__card_look__', off + 52))
    add('G14', 'postcards grid', (1, 1), grid(4, 'postcard', '__postcard_prompt__', off + 53))
    add('G15', 'ephemera grid', (1, 1), grid(9, 'paper item', '__eph_prompt__', off + 54))
    return S
if __name__ == '__main__':
    off = int(sys.argv[1]) if len(sys.argv) > 1 else 0
    S = build(off); json.dump(S, open('/tmp/v74_showcase_draft.json', 'w'), indent=1)
    for i, t, ratio, text in S: print('##', i, t, ratio, len(text)); print(text); print()
