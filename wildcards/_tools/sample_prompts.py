import os, re, sys, random, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from expand import load, expand, clean, REF
from paths import wc_dir
files = load([wc_dir()])
TIER = re.compile(r'_(basic|practical|standard|fine|luxury|showpiece)$')
COMP = re.compile(r'(_top|_bottom|_outer|_head|_feet|_extras|_mask_.*|_texture|_closure|_hair|_eyes|_mouth|_cover|_subject|_hilt|_culture|_condition|_rail|_tail|_fins|_stringer|_pattern|_deck|_nose|_rocker|_historic|_modern|_pacific|_sword|_knife|_axe|_spear|_club|_bow|_other|_helmet|_armor|_gauntlet|_codpiece|_cape|_shield|_greave|_short|_type|_types|_material|_materials|_mat|_mat_all|_mat_odd|_name|_names|_hardware|_trim|_lining|_finish|_cluster.*|_design|_tech|_extras|_practical.*|_whimsy.*|_feature|_fit|_hinge|_nosepad|_armtip|_lens|_frame|_colour|_color|_base|_feat|_detail|_adj.*|_carry|_interior)$')
SKIP_PRE = ('f_', 'm_', 'age', 'bt_', 'dem_', 'world_', 'countries', 'head', 'eye', 'nose', 'lip', 'ear', 'neck', 'hand', 'hair', 'musc', 'mark_', 'style_', 'styl_', 'photostyle', 'illustration', 'logo_', 'art_', 'tattoo_', 'cam_', 'lite_', 'aoo_', 'filename')
cats = collections.OrderedDict()
def want(n):
    b = TIER.sub('', n)
    if b in ('category', 'filename_changes'): return None
    if 'create_random' in b and not b.startswith('any_create_random_person_base'): return b
    if 'prompt' in b:
        if re.match(r'^[fm]_', b) and re.search(r'age\d', b): return None
        if b.startswith(('aoo_', 'bt_', 'illustration', 'photostyle', 'style_', 'styl_')) or re.match(r'^age\d', b): return None
        if re.search(r'_(short|wear_one)$', b): return None
        return b
    if COMP.search(b): return None
    if b.startswith(('obj_', 'scene_', 'pose_', 'wardrobe_', 'costume_', 'wx_', 'skin_tan', 'weapon', 'armor', 'surfboard', 'hair_state')) and not b.startswith(SKIP_PRE): return b
    return None
for n in sorted(files):
    b = want(n)
    if b and b not in cats: cats[b] = n
# keep the tier-less name if it exists, else the first tier file
for b in list(cats):
    cats[b] = b if b in files else cats[b]
# skip a family pool when its dedicated prompt covers it
rng = random.Random(41)
out, lab = [], []; skipped = 0; n_cat = 0
for b, n in cats.items():
    pool = [l for l in files[n] if l.strip()]
    if not pool: continue
    got, tries = [], 0
    while len(got) < 5 and tries < 80:
        tries += 1
        t = clean(expand(files, rng.choice(pool), rng))
        if REF.search(t) or len(t.split()) < 7 or t in got: continue
        got.append(t)
    if len(got) < 3: skipped += 1; continue
    n_cat += 1
    for t in got: out.append(t); lab.append(f'{b}\t{t}')
open(sys.argv[1] + '.txt', 'w', encoding='utf8', newline='\n').write('\n'.join(out) + '\n')
open(sys.argv[1] + '_labelled.tsv', 'w', encoding='utf8', newline='\n').write('category\tprompt\n' + '\n'.join(lab) + '\n')
print(n_cat, 'categories,', len(out), 'prompts,', skipped, 'skipped')
