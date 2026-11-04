"""v55 - food and tableware in parts, and a consolidation pass (index, quick start, model notes)."""
import os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from paths import FINAL
import v55_data as D
from v53_build import _wr, decolon, REF
def slug(s): return re.sub(r'[^a-z]+', '_', s.lower()).strip('_')
def an(w): return ('an ' if w[:1].lower() in 'aeiou' else 'a ') + w
def build(final=FINAL):
    G = {}
    for cat, items in D.FOODS.items():
        G['food_%s' % cat] = ['%s, which %s %s' % (n[:1].upper() + n[1:], 'is' if re.match(r'(a|an|the) ', d) else 'are', d) for n, d in items.items()]
        st, ga = ('food_state_drink', 'food_garnish_drink') if cat == 'drink' else (('food_state', 'food_garnish_raw') if cat in ('fruit', 'vegetable', 'cheese') else ('food_state', 'food_garnish'))
        G['food_%s_name' % cat] = [n[:1].upper() + n[1:] for n in items]
        G['food_%s_prompt' % cat] = ['__food_%s__, %s, %s, __food_surface__, __food_light__.' % (cat, '__%s__' % st, '__%s__' % ga)]
    G['food_state'] = D.STATE; G['food_state_drink'] = D.STATE_DRINK; G['food_garnish_raw'] = D.GARNISH_RAW; G['food_garnish_drink'] = D.GARNISH_DRINK; G['food_garnish'] = D.GARNISH; G['food_surface'] = D.SURFACE; G['food_light'] = D.LIGHT
    G['food_categories'] = sorted(D.FOODS)
    G['food_any'] = ['__food_%s__' % c for c in D.FOODS]
    G['food_prompt'] = ['__food_%s_prompt__' % c for c in D.FOODS]
    for t, p in D.WARE.items():
        s = slug(t)
        for k, v in p.items(): G['ware_%s_%s' % (s, k)] = v
        G['ware_%s_prompt' % s] = ['%s, which is __ware_%s_shape__, made of __ware_%s_material__, with __ware_%s_pattern__, and its finish is __ware_%s_finish__.' % (t[:1].upper() + t[1:], s, s, s, s)]
    G['ware_types'] = sorted(D.WARE)
    G['ware_prompt'] = ['__ware_%s_prompt__' % slug(t) for t in D.WARE]
    G['table_layout'] = D.LAYOUT; G['table_cloth'] = D.CLOTH
    G['table_setting_prompt'] = ['A table setting that is __table_layout__, on __table_cloth__. The plates are made of __ware_dinner_plate_material__ and the glasses of __ware_glass_material__. The food is __food_dish_name__, __food_light__.']
    G['meal_prompt'] = ['__food_dish_prompt__', '__table_setting_prompt__', '__food_prompt__']
    G['v55_entry_points'] = ['food_prompt', 'food_dish_prompt', 'food_cheese_prompt', 'food_fruit_prompt', 'food_drink_prompt', 'ware_prompt', 'table_setting_prompt', 'meal_prompt']
    return G
def run(final):
    G = build(final)
    for n, l in G.items(): _wr(final, n, l)
    print('v55:', len(G), 'files'); print('no-colon rule:', decolon(final)); return G
def export_aoo(out, prefix='aoo_'):
    G = {k: v for k, v in build(FINAL).items() if k != 'v55_entry_points'}; names_ = set(G); n = 0
    for name, lines in G.items():
        keep = list(dict.fromkeys(REF.sub(lambda m: '__' + prefix + m.group(1) + '__' if (m.group(1) in names_ or os.path.exists(os.path.join(out, prefix + m.group(1) + '.txt'))) else m.group(0), l) for l in lines))
        _wr(out, prefix + name, keep); n += 1
    decolon(out); return n
if __name__ == '__main__':
    a = [x for x in sys.argv[1:] if os.path.isdir(x)]; run(os.path.abspath(a[0]) if a else FINAL)
