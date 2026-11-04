"""v50: furniture broken into parts. Beds (headboard, footboard, frame, feet, mattress, bedding, size), chairs, sofas, tables, desks, credenzas, wardrobes, bookcases, stools, benches and lamps each get one file per part (headboard and footboard can be absent, every part has its own styles and materials) and a `<item>_built` prompt that assembles them. Mixed phrase files feed rooms and poses. Idempotent; runs after v49."""
import os, re, sys, glob, random, zlib
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from paths import FINAL
import v50_data as D, v50_data2 as D2
def _wr(folder, name, lines): open(os.path.join(folder, name + '.txt'), 'w', encoding='utf8', newline='\n').write('\n'.join(lines) + '\n')
# item -> (noun, [(part keys in sentence order with sentence template)])
T = {
 'bed': ('bed', ['The bed is __furn_bed_size__.', 'It has __furn_bed_boards__.', 'The frame is __furn_bed_frame__, and it stands on __furn_bed_feet__.', 'It has __furn_bed_mattress__.', 'It is dressed with __furn_bed_bedding__.']),
 'chair': ('chair', ['The chair has __furn_chair_seat__.', 'It has __furn_chair_back__.', 'It has __furn_chair_arms__.', 'It stands on __furn_chair_legs__.', 'It also has __furn_chair_extras__.']),
 'sofa': ('sofa', ['The sofa is __furn_sofa_shape__, __furn_sofa_cover__.', 'It has __furn_sofa_back__ and __furn_sofa_arms__.', 'It has __furn_sofa_cushions__.', 'It stands on __furn_sofa_base__.']),
 'table': ('table', ['The table is __furn_table_size__.', 'It has __furn_table_top__ made of __furn_table_top_material__, with __furn_table_edge__.', 'It stands on __furn_table_legs__.', 'It has __furn_table_extras__.']),
 'desk': ('desk', ['The desk has __furn_desk_top__ made of __furn_desk_material__.', 'It has __furn_desk_storage__.', 'It stands on __furn_desk_base__.', 'It also has __furn_desk_extras__.']),
 'credenza': ('credenza', ['The credenza has __furn_credenza_body__.', 'It has __furn_credenza_doors__ and __furn_credenza_drawers__.', 'The handles are __furn_credenza_handles__.', 'It stands on __furn_credenza_base__, with __furn_credenza_top__.']),
 'wardrobe': ('wardrobe', ['The wardrobe has __furn_wardrobe_frame__.', 'It has __furn_wardrobe_doors__ with __furn_wardrobe_handles__.', 'Inside it has __furn_wardrobe_inside__.', 'It stands on __furn_wardrobe_feet__.']),
 'bookcase': ('bookcase', ['The bookcase has __furn_bookcase_frame__.', 'It has __furn_bookcase_shelves__, with __furn_bookcase_back__.', 'It has __furn_bookcase_doors__.', 'It stands on __furn_bookcase_base__.']),
 'stool': ('stool', ['The stool is __furn_stool_height__.', 'It has __furn_stool_seat__.', 'It stands on __furn_stool_legs__, with __furn_stool_footrest__.']),
 'bench': ('bench', ['The bench is __furn_bench_length__.', 'It has __furn_bench_seat__.', 'It stands on __furn_bench_legs__.', 'It has __furn_bench_back__ and __furn_bench_arms__.']),
 'lamp': ('lamp', ['The lamp is __furn_lamp_type__.', 'It has __furn_lamp_base__ and __furn_lamp_stem__.', 'It has __furn_lamp_shade__.', 'It is switched on by __furn_lamp_switch__.']),
}
MIX = {'furn_beds': ['bed', 'bunk_bed', 'daybed'], 'furn_tables': ['table', 'bedside_table', 'conference_table'], 'furn_storage': ['credenza', 'wardrobe', 'bookcase', 'chest_of_drawers', 'display_cabinet', 'tv_stand', 'filing_cabinet', 'wall_shelf', 'shoe_rack', 'blanket_chest'], 'furn_office': ['desk', 'office_chair', 'reception_desk', 'drafting_table'], 'furn_lighting': ['lamp', 'chandelier', 'pendant_light', 'wall_sconce', 'candlestick'], 'seat': ['chair', 'sofa', 'stool', 'bench', 'armchair', 'rocking_chair'], 'furn_bathroom': ['toilet', 'bathtub', 'washbasin', 'shower'], 'furn_kitchen': ['kitchen_sink', 'cooker', 'refrigerator', 'dishwasher', 'kitchen_cabinet', 'kitchen_island'], 'furn_decor': ['mirror', 'curtains', 'rug', 'wall_clock', 'vase', 'room_divider'], 'home_electronics': ['television', 'radio', 'microwave', 'oven'], 'home_cleaning': ['vacuum_cleaner', 'fan', 'space_heater'], 'home_cookware': ['kettle', 'toaster'], 'gear_laundry': ['washing_machine', 'tumble_dryer']}
BOARDS_WOOD = [('a tall headboard of {m} with vertical slats', 'a low footboard of {m} with matching vertical slats'), ('a carved headboard of {m} with a peaked top', 'a lower carved footboard of {m} with a matching peaked top'), ('a wide panelled headboard of {m} with a raised centre', 'a shorter panelled footboard of {m} with a matching raised centre'), ('a low plain headboard of {m}', 'a matching low plain footboard of {m}'), ('a curved sleigh headboard of {m}', 'a matching curved sleigh footboard of {m}, slightly lower'), ('a tall headboard of {m} with turned posts at each end', 'a lower footboard of {m} with matching turned posts at each end')]
BOARDS_FABRIC = [('a tall upholstered headboard in {m} with button tufting', 'a low upholstered footboard in the same {m} with matching button tufting'), ('a curved padded headboard in {m}', 'a low curved padded footboard in the same {m}'), ('a winged headboard in {m} that curves forward at the sides', 'a low padded footboard in the same {m}'), ('a plain padded headboard in {m}', 'a plain padded footboard in the same {m}')]
BOARDS_METAL = [('a wrought-iron headboard with curling scrolls in {m}', 'a lower footboard with matching curling scrolls in {m}'), ('a headboard formed of horizontal bars in {m}', 'a footboard formed of matching horizontal bars in {m}'), ('a headboard of curved bars in {m}', 'a matching footboard of curved bars in {m}, slightly lower')]
def boards():
    L = ['no headboard and no footboard', 'no headboard and no footboard', 'a headboard of woven cane in a rounded shape and no footboard', 'a plain headboard of pale wood and no footboard']
    for h, f in BOARDS_WOOD:
        for m in D.WOOD: L.append(f'{h.format(m=m)}, and {f.format(m=m)}')
    for h, f in BOARDS_FABRIC:
        for m in D.FABRIC[:9]: L.append(f'{h.format(m=m)}, and {f.format(m=m)}')
    for h, f in BOARDS_METAL:
        for m in D.METAL: L.append(f'{h.format(m=m)}, and {f.format(m=m)}')
    return L
def auto_T(item, noun, parts):
    keys = list(parts)
    def sent(k, first):
        r = f'__furn_{item}_{k}__'
        if k in ('finish','colour','material','pattern'): return f'Its {k} is {r}.'
        if k in ('size','length','shape','type','pile','panels'): return f'Its {k} is {r}.'
        if k in ('extras','extra'): return f'It also has {r}.'
        return f'The {noun} has {r}.' if first else f'It has {r}.'
    return noun, [sent(k, i==0) for i,k in enumerate(keys)]
def build():
    G = {'part_wood': D.WOOD, 'part_fabric': D.FABRIC, 'part_metal': D.METAL}
    G['furn_bed_boards'] = boards()
    for item, (noun, parts) in D2.MORE.items():
        D.PARTS[item] = parts; T[item] = auto_T(item, noun, parts)
    for item, parts in D.PARTS.items():
        for part, opts in parts.items():
            G[f'furn_{item}_{part}'] = opts; G[f'furn_{item}_{part}_prompt'] = [f"The {T[item][0]}'s {part.replace('_', ' ')} is __furn_{item}_{part}__."]
        noun, sents = T[item]
        full = ' '.join(sents)
        G[f'furn_{item}_built'] = [full]
        if item == 'bed':
            ind = full.replace('It has __furn_bed_boards__.', 'It has __furn_bed_headboard__. It has __furn_bed_footboard__.')
            G['furn_bed_built'] = [full] * 3 + [ind]; G['furn_bed_built_phrase'] = None
        G[f'furn_{item}_built_short'] = [' '.join(sents[:3])]
        if item == 'bed': G['furn_bed_built_phrase'] = [f'{an(noun)}. ' + x for x in G['furn_bed_built']]
        else: G[f'furn_{item}_built_phrase'] = [f'{an(noun)}. ' + full]
        G[f'furn_{item}_prompt'] = [f'__furn_{item}_built__']
    for mix, items in MIX.items():
        G[mix + '_mix_phrase'] = [f'__{mix}_phrase__'] + [f'__furn_{i}_built_phrase__' for i in items for _ in range(2)]
    G['furn_bed_boards_prompt'] = ["The bed's headboard and footboard are __furn_bed_boards__."]
    G['furn_built_prompt'] = [f'__furn_{i}_built__' for i in D.PARTS]
    G['v50_entry_points'] = ['__furn_built_prompt__'] + [f'__furn_{i}_built__' for i in D.PARTS]
    return G
def run(final):
    G = build()
    for n, l in G.items(): _wr(final, n, l)
    print('v50:', len(G), 'files'); return G
def export_aoo(out, prefix='aoo_'):
    G = build(); names_ = set(G); ref = re.compile(r'__([A-Za-z0-9_\-/]+)__'); n = 0
    for name, lines in G.items():
        keep = list(dict.fromkeys(ref.sub(lambda m: '__' + prefix + m.group(1) + '__' if (m.group(1) in names_ or os.path.exists(os.path.join(out, prefix + m.group(1) + '.txt'))) else m.group(0), l) for l in lines))
        if not (name.endswith(('built', 'built_short', 'built_phrase', 'prompt', 'entry_points')) or '_mix_' in name): random.Random(zlib.crc32(name.encode())).shuffle(keep)
        _wr(out, prefix + name, keep); n += 1
    return n
def an(w): return ('an ' if w[0].lower() in 'aeiou' else 'a ') + w
def strip_blank(folder):
    import glob
    n = 0
    for p in glob.glob(os.path.join(folder, '*.txt')):
        t = open(p, encoding='utf-8').read()
        if ('\n\n' in t or t.startswith('\n')) and t.strip():
            open(p, 'w', encoding='utf-8').write('\n'.join(l for l in t.split('\n') if l != '') + '\n'); n += 1
    return n
if __name__ == '__main__':
    a = [x for x in sys.argv[1:] if os.path.isdir(x)]; run(os.path.abspath(a[0]) if a else FINAL); print('blank-line files fixed:', strip_blank(os.path.abspath(a[0]) if a else FINAL))
