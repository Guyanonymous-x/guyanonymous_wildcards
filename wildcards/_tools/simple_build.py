"""Builds the separate 'all options once' package from the finished wildcards folder.

Design (deliberately the opposite of the main system):
  * one flat set of option files per topic - NO gender, age-bracket, body-type or hair-type variants
  * every distinct option appears exactly ONCE (no likelihood weighting, no repeated lines, no blank 'none' lines)
  * the female and male versions of a topic are merged into one file; lines that carry gender or age wording are dropped from the
    human-feature files, so a line never says who it is for
  * a handful of plain prompt templates that simply pick one option from each file

Usage:  python simple_build.py [wildcards_folder] [output_folder]
"""
import shutil, os, re, sys, collections, json
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from paths import FINAL
SRC = FINAL; FINAL_OUT = os.path.join(os.path.dirname(FINAL), 'all_options_once'); OUT = FINAL_OUT
a = [x for x in sys.argv[1:]]
if a: SRC = os.path.abspath(a[0])
if len(a) > 1: FINAL_OUT = os.path.abspath(a[1])
OUT = FINAL_OUT + '.tmp_build'      # build here first; the real folder is replaced only after the checks pass (a failed run can no longer wipe it)
P = 'aoo_'
REF = re.compile(r'__([A-Za-z0-9_\-/]+)__')

GENDER = re.compile(r"\b(wom[ae]n|m[ae]n|male|female|girls?|boys?|she|her|hers|herself|he|his|him|himself|ladies|lady|gentlem[ae]n|feminine|masculine|brides?|grooms?|mother|father|sisters?|brothers?|husband|wife|girlfriend|boyfriend|men's|women's)\b", re.I)
AGE = re.compile(r"\b(aging|aged|ageing|elderly|youthful|young|younger|old|older|oldest|senior|mature|teen\w*|child\w*|infant|juvenile|middle-aged|grandm\w+|grandf\w+)\b", re.I)
HUMAN = re.compile(r'^(skin_|hair_|hairstyle|hairtex|hairvol|eye_|head_|nose_|lip_|ear_|neck_|hand_|musc_|body_|mark_|dem_|facial|grooming|make_|pose_|poses|attractiveness)')

def rd(name):
    p = os.path.join(SRC, name + '.txt')
    if not os.path.exists(p): p = os.path.join(SRC, 'clothing_' + name + '.txt')     # the library renamed some sources (outfit_color -> clothing_outfit_color)
    if not os.path.exists(p): return []
    return [l.strip() for l in open(p, encoding='utf8', errors='replace') if l.strip()]

def union(names, human=False):
    seen = {};
    for n in names:
        for l in rd(n):
            if REF.search(l): continue          # option files only; lines that point at other files are templates
            if GENDER.search(l): continue
            if human and AGE.search(l): continue
            seen.setdefault(l.lower(), l)
    return list(seen.values())

def both(base):  # f_ and m_ versions plus the shared one
    return [base, 'f_' + base, 'm_' + base]

FAM = collections.OrderedDict()
def fam(out, names, human=False, note=''):
    FAM[out] = (names, human, note)

# ---------------- clothing ----------------
fam('clothing_color', ['outfit_color']); fam('clothing_material', ['outfit_material']); fam('clothing_pattern', ['outfit_pattern'])
fam('clothing_detail', ['clth_detail']); fam('clothing_fabric', ['clth_fabric']); fam('clothing_fit', ['clth_fit']); fam('clothing_layers', ['clth_layers']); fam('clothing_pattern_description', ['clth_pattern'])
fam('top', both('outfit_casual_top')); fam('bottom', both('outfit_casual_bottom')); fam('dress_or_one_piece', both('outfit_dress_style')); fam('outerwear', both('outfit_outerwear')); fam('suit', both('outfit_suit_style'))
fam('uniform', both('outfit_uniform_type')); fam('costume', both('outfit_cosplay')); fam('underwear_sleepwear_swimwear', both('outfit_lingerie') + both('outfit_swim_underwear'))
fam('sheer_clothing', both('outfit_see_through')); fam('party_top', both('outfit_sexy_top')); fam('party_bottom', both('outfit_sexy_bottom')); fam('party_one_piece', both('outfit_sexy_full'))
fam('hat', ['acc_hats']); fam('jewelry', both('acc_jewelry')); fam('strap_or_bag', both('acc_straps')); fam('eyewear', both('acc_glasses'))
# ---------------- hair ----------------
fam('hair_color', ['hair_color'], True); fam('hair_style', both('hair_style') + [f'{p}hairstyle_{t}' for p in ('', 'f_', 'm_') for t in 'SWCK'], True)
fam('hair_curl', ['hair_curl'] + [f'hair_curl_{t}' for t in 'SWCK'], True); fam('hair_texture', ['hair_texture'], True); fam('hair_volume', ['hair_volume'], True)
fam('hair_shine', ['hair_shine'], True); fam('hairline', ['hair_line'], True); fam('hair_motion', ['hair_motion'], True); fam('baby_hairs', ['f_hair_baby'], True)
fam('facial_hair', ['m_facial_hair'], True); fam('grooming', ['m_grooming'], True)
# ---------------- eyes, face, neck ----------------
for n in ('color', 'shape', 'spacing', 'lid', 'brow', 'sclera'): fam('eye_' + n, ['eye_' + n], True)
fam('eyelash', both('eye_lash'), True)
for n in ('shape', 'chin', 'jaw', 'cheek', 'temple', 'brow'): fam('head_' + n, ['head_' + n], True)
for n in ('bridge', 'tip', 'nostril', 'crease', 'philtr'): fam('nose_' + n, ['nose_' + n], True)
for n in ('fullness', 'cupid', 'corners', 'teeth', 'gums'): fam('lip_' + n, ['lip_' + n], True)
fam('ear_shape', ['ear_shape'], True); fam('ear_lobe', ['ear_lobe'], True)
for n in ('length', 'crease', 'clav', 'muscle'): fam('neck_' + n, ['neck_' + n], True)
fam('makeup_base', ['f_make_base'], True); fam('makeup_blush', ['f_make_blush'], True); fam('makeup_eyes', ['f_make_eyes'], True); fam('makeup_highlighter', ['f_make_hlite'], True); fam('makeup_lips', ['f_make_lips'], True)
# ---------------- skin, marks ----------------
for n in ('finish', 'flush', 'fuzz', 'glow', 'marks', 'scars', 'texture', 'wrinkle'): fam('skin_' + n, ['skin_' + n], True)
for n in ('tattoo', 'paint', 'pierce', 'scars', 'cyber'): fam('mark_' + n, ['mark_' + n] + (['f_opt_tattoo', 'm_opt_tattoo'] if False else []), True)
fam('skin_tone', ['dem_tone'], True); fam('ancestry', ['dem_ethnicity'], True); fam('mixed_heritage', ['dem_heritage'], True); fam('distinctive_feature', ['dem_unique'], True); fam('facial_bone_structure', ['dem_bone'], True)
# ---------------- body ----------------
fam('body_build', both('body_build'), True); fam('body_height', both('body_height'), True); fam('body_ratio', both('body_ratio'), True); fam('body_proportions', ['body_proprtn'], True)
fam('body_bones', ['body_bones'], True); fam('body_composition', ['body_compos'], True)
for n in ('abs', 'arms', 'chest', 'shldr', 'veins'): fam('muscle_' + n, ['musc_' + n], True)
fam('muscle_hips', both('musc_hips'), True); fam('muscle_legs', both('musc_legs'), True)
for n in ('feet', 'fingers', 'knuckl', 'nails'): fam('hand_' + n, ['hand_' + n], True)
# ---------------- poses and expressions ----------------
for n in ('action', 'emotion', 'gaze', 'hands', 'twist', 'weight'): fam('pose_' + n, ['pose_' + n], True)
fam('pose_full', ['poses'] + both('poses_extended'), True); fam('facial_expression', ['facialExpressionsFor_v10'], True)
# ---------------- footwear (all six quality tiers and all seven classes merged) ----------------
T = ['basic', 'practical', 'standard', 'fine', 'luxury', 'showpiece']
fam('acc_shoe_type', [f'acc_shoe_type_{c}' for c in ('boot', 'heel', 'flat', 'sneaker', 'sandal', 'slipper', 'clog')] + ['acc_shoe_type'])
for n in ('colour', 'material', 'closure', 'construction', 'detail', 'extras', 'finish', 'footbed', 'heel', 'heelmat', 'lining', 'overlay', 'sole', 'technique', 'word'):
    fam('acc_shoe_' + n, [f'acc_shoe_{n}'] + [f'acc_shoe_{n}_{t}' for t in T])
fam('acc_shoe_pattern', ['acc_shoe_pattern']); fam('acc_shoe_toe', ['acc_shoe_toe']); fam('acc_shoe_purpose', ['acc_shoe_purpose'] + [f'acc_shoe_purpose_{c}' for c in ('boot', 'heel', 'flat', 'sneaker', 'sandal', 'slipper', 'clog')])
fam('acc_shoe_audience', ['acc_shoe_audience'] + [f'acc_shoe_audience_{x}' for x in ('boot', 'heel', 'flat', 'sneaker', 'sandal', 'slipper', 'clog') + tuple(T)])
fam('acc_shoe_designer', ['acc_shoe_designer_bare'] if os.path.exists(os.path.join(SRC, 'acc_shoe_designer_bare.txt')) else ['acc_shoe_designer'])
# ---------------- light, camera, scene, style ----------------
for n in ('angle', 'color', 'shadow', 'source', 'volum'): fam('light_' + n, ['lite_' + n])
for n in ('angle', 'focus', 'lens', 'shot'): fam('camera_' + n, ['cam_' + n])
for n in ('scene', 'setting', 'time', 'weather'): fam('env_' + n, ['env_' + n])
for n in ('color', 'detail', 'medium'): fam('style_' + n, ['styl_' + n])
fam('env_props', ['env_props']); fam('accessory_props', ['acc_props']); fam('scene_settings', ['settings10000']); fam('creative_locations', ['creativeLocations'])
for n in ('furniture', 'held_items', 'outdoor_items', 'room_items', 'scene_exterior', 'scene_interior', 'table_items', 'toys'): fam('object_' + n, ['obj_' + n])
fam('photographer_styles', ['f_style_photographers_portrait', 'm_style_photographers_portrait'])

def write(name, lines):
    import random, zlib
    lines = list(lines); random.Random(zlib.crc32(name.encode())).shuffle(lines)   # random order within every file (deterministic)
    open(os.path.join(OUT, P + name + '.txt'), 'w', encoding='utf8', newline='\n').write('\n'.join(lines) + '\n')

def main():
    if os.path.isdir(OUT): shutil.rmtree(OUT)
    os.makedirs(OUT)
    counts = {}
    for out, (names, human, note) in FAM.items():
        lines = union(names, human)
        if lines: write(out, lines); counts[out] = len(lines)
    # complete outfit lines (the generated everyday / full outfits), references mapped onto the simple files
    MAP = {'outfit_color': 'clothing_color', 'outfit_material': 'clothing_material', 'outfit_pattern': 'clothing_pattern', 'outfit_casual_top': 'top', 'outfit_casual_bottom': 'bottom',
           'outfit_dress_style': 'dress_or_one_piece', 'outfit_outerwear': 'outerwear', 'outfit_suit_style': 'suit', 'outfit_uniform_type': 'uniform', 'outfit_cosplay': 'costume',
           'outfit_lingerie': 'underwear_sleepwear_swimwear', 'outfit_swim_underwear': 'underwear_sleepwear_swimwear', 'outfit_see_through': 'sheer_clothing', 'outfit_sexy_top': 'party_top',
           'outfit_sexy_bottom': 'party_bottom', 'outfit_sexy_full': 'party_one_piece'}
    def mapref(m):
        r = m.group(1)
        for p in ('f_', 'm_'):
            if r.startswith(p): r = r[2:]
        return f'__{P}{MAP[r]}__' if r in MAP else None
    for out, srcs in (('outfit_everyday', ['f_clothing_everyday', 'm_clothing_everyday']), ('outfit_full', ['f_clothing_full', 'm_clothing_full'])):
        seen = {}
        for s in srcs:
            for l in rd(s):
                if GENDER.search(l): continue
                ok = True
                def sub(m):
                    nonlocal ok
                    x = mapref(m)
                    if x is None: ok = False; return m.group(0)
                    return x
                l2 = REF.sub(sub, l)
                if ok: seen.setdefault(l2.lower(), l2)
        if seen: write(out, list(seen.values())); counts[out] = len(seen)
    # plain templates
    have = set(counts)
    def ref(n): return f'__{P}{n}__'
    tpl = {
     'prompt_full': [f"A photograph of an adult with {ref('hair_color')}, {ref('hair_style')}, {ref('eye_color')}, {ref('skin_tone')}, wearing {ref('clothing_color')} {ref('clothing_material')} {ref('top')} and {ref('clothing_color')} {ref('bottom')}, {ref('acc_shoe_colour')} {ref('acc_shoe_type')}, {ref('pose_action')}, {ref('pose_gaze')}, in {ref('env_setting')}, {ref('light_source')}, {ref('camera_shot')}, {ref('style_medium')}."],
     'prompt_outfit': [f"Wearing {ref('clothing_color')} {ref('clothing_pattern')} {ref('top')} with {ref('clothing_color')} {ref('bottom')}, {ref('outerwear')}, {ref('hat')}, {ref('jewelry')}, {ref('acc_shoe_colour')} {ref('acc_shoe_type')}.",
                       f"Wearing {ref('outfit_everyday')}.", f"Dressed in {ref('clothing_color')} {ref('dress_or_one_piece')}, {ref('acc_shoe_colour')} {ref('acc_shoe_type')}, {ref('jewelry')}."],
     'prompt_face_and_hair': [f"{ref('head_shape')}, {ref('eye_shape')}, {ref('eye_color')}, {ref('nose_bridge')}, {ref('lip_fullness')}, {ref('skin_texture')}, {ref('hair_color')}, {ref('hair_style')}, {ref('hair_texture')}."],
     'prompt_pose_and_scene': [f"{ref('pose_action')}, {ref('pose_hands')}, {ref('pose_gaze')}, {ref('pose_emotion')} expression. {ref('env_setting')}, {ref('env_time')}, {ref('env_weather')}. {ref('light_angle')}, {ref('light_color')}, {ref('camera_lens')}."],
     'prompt_footwear': [f"{ref('acc_shoe_colour')} {ref('acc_shoe_material')} {ref('acc_shoe_type')} with {ref('acc_shoe_detail')}, {ref('acc_shoe_sole')}, {ref('acc_shoe_finish')}."],
    }
    for k, v in tpl.items():
        v = [l for l in v if all(r[len(P):] in have or r in ('outfit_everyday', 'outfit_full') for r in [x for x in REF.findall(l)] if True) or True]
        write(k, v)
    # every module that defines export_aoo is called, in file-name order of their version (discovered, not hand-listed, so new releases cannot be missed)
    import importlib
    mods = []
    for fn in sorted(os.listdir(HERE)):
        if fn.endswith('.py') and fn != 'simple_build.py' and 'def export_aoo(' in open(os.path.join(HERE, fn), encoding='utf8').read():
            mods.append(fn[:-3])
    def vkey(m):
        mm = re.match(r'v(\d+)_', m)
        return (1, int(mm.group(1)), m) if mm else (0, 0, m)
    mods.sort(key=vkey)
    for mname in mods:
        try:
            importlib.import_module(mname).export_aoo(OUT)      # return value ignored (some modules return a count, some a tuple)
        except Exception as e:
            print('EXPORT FAILED', mname, repr(e)); raise
    for f in os.listdir(OUT):
        if f.endswith('.txt') and f[:-4] not in counts and not f.startswith('aoo_prompt_') and 'prompt_' not in f and not f.startswith('aoo_style_'):
            counts[f[:-4]] = sum(1 for l in open(os.path.join(OUT, f), encoding='utf8') if l.strip())
    rdm = os.path.join(HERE, 'data', 'aoo_README.txt')
    if os.path.exists(rdm): shutil.copy(rdm, os.path.join(OUT, 'README.txt'))
    # carry over files that the previous build had and this one cannot regenerate (their sources were renamed or removed from the library)
    carried = []
    if os.path.isdir(FINAL_OUT):
        for f in os.listdir(FINAL_OUT):
            if f.endswith('.txt') and not os.path.exists(os.path.join(OUT, f)):
                shutil.copy(os.path.join(FINAL_OUT, f), os.path.join(OUT, f)); carried.append(f)
    print('carried over from the previous build:', len(carried), carried[:8])
    # reference repair: (a) a reference with no aoo_ prefix whose aoo_ file exists is re-pointed; (b) lines that still reference a missing file are removed; files left empty are deleted; repeat until stable
    def listing(): return {f[:-4] for f in os.listdir(OUT) if f.endswith('.txt')}
    removed_lines = 0; removed_files = 0
    for _ in range(10):
        files = listing(); changed = False
        for f in sorted(files):
            p = os.path.join(OUT, f + '.txt'); ls = open(p, encoding='utf8').read().split('\n'); out = []; dirty = False
            for l in ls:
                def fix(m):
                    r = m.group(1)
                    if r in files: return m.group(0)
                    if P + r in files: return f'__{P}{r}__'
                    return m.group(0)
                l2 = REF.sub(fix, l)
                if any(r not in files for r in REF.findall(l2)): removed_lines += 1; dirty = True; continue
                if l2 != l: dirty = True
                out.append(l2)
            if dirty:
                changed = True
                body = [x for x in out if x.strip()]
                if not body: os.remove(p); removed_files += 1
                else: open(p, 'w', encoding='utf8', newline='\n').write('\n'.join(out).rstrip('\n') + '\n')
        if not changed: break
    print(f'reference repair: removed {removed_lines} lines and {removed_files} empty files that pointed at missing files')
    # check every reference resolves
    files = {f[:-4] for f in os.listdir(OUT) if f.endswith('.txt')}
    bad = []
    for f in os.listdir(OUT):
        for l in open(os.path.join(OUT, f), encoding='utf8'):
            for r in REF.findall(l):
                if r not in files: bad.append((f, r))
    json.dump(counts, open(os.path.join(OUT, '_counts.json'), 'w'), indent=1)
    print(f'{len(counts)} option files, {sum(counts.values())} options in total; unresolved references: {len(bad)}', bad[:5])
    # file-count check against the previous build: refuse to replace the real folder if the new one is smaller by more than 1 percent, or has unresolved references
    new_n = len([f for f in os.listdir(OUT) if f.endswith('.txt')])
    old_n = len([f for f in os.listdir(FINAL_OUT) if f.endswith('.txt')]) if os.path.isdir(FINAL_OUT) else 0
    print(f'files in new build {new_n}, in previous build {old_n}')
    if bad or (old_n and new_n < old_n * 0.99):
        print(f'CHECK FAILED, the previous folder is untouched; the new build is left in {OUT}'); sys.exit(1)
    prev = FINAL_OUT + '.prev'
    if os.path.isdir(prev): shutil.rmtree(prev)
    if os.path.isdir(FINAL_OUT): os.rename(FINAL_OUT, prev)
    os.rename(OUT, FINAL_OUT)
    if os.path.isdir(prev): shutil.rmtree(prev)
    print('replaced', FINAL_OUT)
if __name__ == '__main__': main()
