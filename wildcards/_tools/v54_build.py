"""v54 - animals (kingdom/class, salt/fresh), insects, plants, architecture and vehicles in parts."""
import os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from paths import FINAL
import v54_animals as A, v54_data as D
from v53_build import _wr, decolon, REF
def slug(s): return re.sub(r'[^a-z]+', '_', s.lower()).strip('_')
def title(n): return n
def build(final=FINAL):
    G = {}
    groups = {}   # (kingdom, class, water) -> names
    for nm in A.load():
        r = A.classify(nm)
        if not r: continue
        k, c, w = r
        groups.setdefault((k, c), {'fresh': [], 'salt': [], 'none': []})
        d = A.display(nm); d = d[:1].upper() + d[1:]
        for key in (['fresh', 'salt'] if w == 'both' else [w or 'none']):
            groups[(k, c)][key].append(d)
    kingdoms = {}; prompts = []; aquatic = {'salt': [], 'fresh': []}
    for pk, pv in D.POOL.items():
        for key, vals in pv.items():
            G['animal_kind_%s_%s' % (pk, key)] = vals
    for (k, c), wd in sorted(groups.items()):
        kind = D.KIND.get(c, 'mammal'); pool = D.POOL[kind]; cs = slug(c)
        allnames = sorted(set(wd['fresh'] + wd['salt'] + wd['none']))
        G['animal_' + cs] = allnames; kingdoms.setdefault(k, []).append('animal_' + cs)
        def line(namefile, hab):
            return '__animal_kind_%s_view__ of the __%s__, shown __animal_kind_%s_pose__, __%s__, __animal_kind_%s_detail__.' % (kind, namefile, kind, hab, kind)
        if wd['salt'] or wd['fresh']:
            for w in ('salt', 'fresh'):
                if not wd[w]: continue
                G['animal_%s_%s' % (w, cs)] = sorted(wd[w])
                hab = 'animal_kind_%s_habitat_%s' % (kind, w) if ('habitat_' + w) in pool else 'animal_kind_%s_habitat' % kind
                G['animal_%s_%s_prompt' % (w, cs)] = [line('animal_%s_%s' % (w, cs), hab)]
                aquatic[w].append('animal_%s_%s' % (w, cs))
                prompts.append(('animal_%s_%s_prompt' % (w, cs), len(wd[w])))
            if wd['none']:
                G['animal_' + cs + '_prompt'] = [line('animal_' + cs, 'animal_kind_%s_habitat' % kind if 'habitat' in pool else 'animal_kind_%s_habitat_salt' % kind)]
                prompts.append(('animal_%s_prompt' % cs, len(wd['none'])))
        else:
            G['animal_%s_prompt' % cs] = [line('animal_' + cs, 'animal_kind_%s_habitat' % kind)]
            prompts.append(('animal_%s_prompt' % cs, len(allnames)))
    for k, v in kingdoms.items(): G['animal_kingdom_' + slug(k)] = ['__%s__' % x for x in v]
    G['animal_classes'] = ['__%s__' % x for v in kingdoms.values() for x in v]
    G['animal_class_list'] = [c for (k, c) in sorted(groups)]
    # weighted by number of names so every animal is equally likely
    G['animal_prompt'] = ['__%s__' % n for n, w in prompts for _ in range(max(1, w // 10))]
    for w in ('salt', 'fresh'):
        G['animal_aquatic_%s' % w] = ['__%s__' % x for x in aquatic[w]]
        G['animal_aquatic_%s_prompt' % w] = ['__%s_prompt__' % x for x in aquatic[w]]
    G['animal_insect_prompt'] = ['__animal_insects_prompt__']
    # plants
    G['plant_names'] = sorted(D.PLANTS); G['plant_state'] = D.PLANT_STATE; G['plant_setting'] = D.PLANT_SETTING
    for n, look in D.PLANTS.items(): pass
    def an(w): return ('An ' if w[:1] in 'aeiou' else 'A ') + w
    for n in D.PLANTS: G['plant_hab_' + slug(n)] = D.PLANT_HAB[n]
    G['plant_prompt'] = ['%s with %s, __plant_state__, __plant_hab_%s__.' % (an(n), look, slug(n)) for n, look in D.PLANTS.items()]
    G['nature_prompt'] = ['__plant_prompt__', '__animal_prompt__']
    # architecture
    TPL = {
     'house': 'A house with __arch_house_roof__, __arch_house_walls__, __arch_house_door__, __arch_house_windows__, and __arch_house_extra__.',
     'apartment block': 'An apartment block that is __arch_apartment_block_form__, with __arch_apartment_block_facade__, __arch_apartment_block_roof__, __arch_apartment_block_ground__, and __arch_apartment_block_extra__.',
     'temple': 'A temple with __arch_temple_roof__, __arch_temple_walls__, __arch_temple_entrance__, and __arch_temple_extra__.',
     'castle': 'A castle with __arch_castle_towers__, __arch_castle_walls__, and __arch_castle_gate__, standing __arch_castle_setting__.',
     'bridge': 'A bridge that is __arch_bridge_form__, crossing __arch_bridge_crossing__, with __arch_bridge_detail__.',
     'skyscraper': 'A skyscraper that is __arch_skyscraper_form__, with __arch_skyscraper_facade__ and __arch_skyscraper_top__, seen __arch_skyscraper_setting__.',
     'barn': 'A barn with __arch_barn_roof__, __arch_barn_walls__, and __arch_barn_door__, standing __arch_barn_setting__.',
     'lighthouse': 'A lighthouse that is __arch_lighthouse_tower__, with __arch_lighthouse_lamp__, standing __arch_lighthouse_base__, with __arch_lighthouse_extra__.',
     'market hall': 'A market hall with __arch_market_hall_roof__, __arch_market_hall_walls__, __arch_market_hall_stalls__, and __arch_market_hall_extra__.'}
    VT = {
     'bicycle': 'A bicycle with __veh_bicycle_frame__, __veh_bicycle_wheels__, __veh_bicycle_seat__, and __veh_bicycle_extra__. Its finish is __veh_bicycle_finish__.',
     'car': 'A car that is __veh_car_body__, with __veh_car_finish__, __veh_car_wheels__, and __veh_car_extra__.',
     'bus': 'A bus that is __veh_bus_body__, with __veh_bus_finish__, __veh_bus_doors__, and __veh_bus_extra__.',
     'train': 'A train that is __veh_train_form__, with __veh_train_finish__, seen __veh_train_setting__, with __veh_train_extra__.',
     'boat': 'A boat that is __veh_boat_hull__, with __veh_boat_finish__, shown __veh_boat_setting__, with __veh_boat_extra__.',
     'aeroplane': 'An aircraft that is __veh_aeroplane_form__, with __veh_aeroplane_finish__, shown __veh_aeroplane_setting__.',
     'tractor': 'A tractor that is __veh_tractor_body__, with __veh_tractor_finish__, __veh_tractor_wheels__, and __veh_tractor_implement__, shown __veh_tractor_setting__.',
     'excavator': 'An excavator that is __veh_excavator_body__, with __veh_excavator_arm__ and __veh_excavator_tracks__, with __veh_excavator_finish__, shown __veh_excavator_setting__.',
     'crane': 'A crane that is __veh_crane_form__, with __veh_crane_finish__, shown __veh_crane_setting__, with __veh_crane_extra__.',
     'motorbike': 'A motorbike that is __veh_motorbike_body__, with __veh_motorbike_finish__ and __veh_motorbike_extra__.',
     'cart': 'A cart that is __veh_cart_form__, with __veh_cart_finish__, __veh_cart_load__.',
     'sled': 'A sled that is __veh_sled_form__, shown __veh_sled_setting__, with __veh_sled_extra__.'}
    for pre, DD, T in (('arch', D.ARCH, TPL), ('veh', D.VEH, VT)):
        for t, parts in DD.items():
            ts = slug(t)
            for key, vals in parts.items(): G['%s_%s_%s' % (pre, ts, key)] = vals
            G['%s_%s_prompt' % (pre, ts)] = [T[t]]
        G['%s_types' % pre] = sorted(DD)
        G['%s_prompt' % pre] = ['__%s_%s_prompt__' % (pre, slug(t)) for t in DD]
    G['machinery_prompt'] = ['__veh_%s_prompt__' % s for s in ('tractor', 'excavator', 'crane')]
    G['v54_entry_points'] = ['animal_prompt', 'animal_insect_prompt', 'animal_aquatic_salt_prompt', 'animal_aquatic_fresh_prompt', 'plant_prompt', 'nature_prompt', 'arch_prompt', 'veh_prompt', 'machinery_prompt', 'animal_classes', 'animal_kingdom_animals', 'animal_class_list']
    # insects prompt alias
    if 'animal_insects_prompt' not in G and 'animal_insects' in G: pass
    return G
def run(final):
    G = build(final)
    for n, l in G.items(): _wr(final, n, l)
    print('v54:', len(G), 'files'); print('no-colon rule:', decolon(final)); return G
def export_aoo(out, prefix='aoo_'):
    G = {k: v for k, v in build(FINAL).items() if k != 'v54_entry_points'}; names_ = set(G); n = 0
    for name, lines in G.items():
        keep = list(dict.fromkeys(REF.sub(lambda m: '__' + prefix + m.group(1) + '__' if (m.group(1) in names_ or os.path.exists(os.path.join(out, prefix + m.group(1) + '.txt'))) else m.group(0), l) for l in lines))
        _wr(out, prefix + name, keep); n += 1
    decolon(out); return n
if __name__ == '__main__':
    a = [x for x in sys.argv[1:] if os.path.isdir(x)]; run(os.path.abspath(a[0]) if a else FINAL)
