"""Updated body-feature / pose / age showcase in the new layout: 2x2 grids, every panel a self-contained photograph in its own wrapper,
feature lists joined with semicolons under a label (no 'eyes with round eyes' doubling), colours named, adult scene panels from the v106 structured pools."""
import sys, os, re, random, glob
sys.argv = ['x']
sys.path.insert(0, '/home/claude/w/wildcards/_tools')
import body_showcase as B
import expand as E
from paths import FINAL
SCR = '/tmp/claude-0/-home-claude/f4f177e0-8597-507c-b7de-4fd3dcc5cfda/scratchpad/v106_out'
F2 = E.load([SCR, FINAL])
B.files = F2
def g2(ref, r): return ' '.join(E.clean(E.expand(F2, ref, r)).split())
ORD = ['first', 'second', 'third', 'fourth']
HEAD = 'A grid of 4 equal photographic panels arranged in two rows of two columns, separated by thin plain white gaps. Every panel is a separate scene with its own person or people, and nothing is shared between panels.'
LIMB = ' The person has one head, two arms and two legs, and every hand, foot and limb belongs to that person.'
GREYBG = 'against a plain pale grey background under soft even studio light'
TPL = {
 'face_shape': '__head_shape__; __A_head_cheek__; __A_head_jaw__; __head_chin__',
 'chin': '__head_chin_show__',
 'eyes': '__eye_shape__; __A_eye_lid__; __A_eye_brow__; __eye_spacing__; __eye_color__',
 'eyelashes': '__A_eye_lid__; __SEX_eye_lash__',
 'eyebrows': '__A_eye_brow__; __head_brow__',
 'nose': '__nose_bridge__; __nose_tip__; __nose_nostril__; __nose_philtr__',
 'nose_profile': '__nose_bridge__; __nose_tip__',
 'lips': '__A_lip_fullness__; __A_lip_cupid__; __A_lip_corners__',
 'teeth': '__A_lip_teeth__; __A_lip_gums__',
 'ears': '__ear_shape__; __ear_lobe__',
 'cheeks_jaw': '__A_head_cheek__; __A_head_jaw__; __A_head_temple__',
 'neck': '__neck_length__; __neck_clav__',
 'hair_volume_line': '__SEX_HVOL_C__; hairline: __SEX_HLINE__',
 'hands': '__A_hand_fingers__; __A_hand_knuckl__',
 'nails': '__A_hand_nails__', 'feet': '__A_hand_feet__',
 'legs_hips': '__SEX_MLEGS__; __SEX_MHIPS__',
 'expr_general': '__pose_emotion__; gaze: __pose_gaze__',
 'skin_body': '__dem_tone__'}
for sp in B.SPECS:
    if sp['key'] in TPL: sp['tpl'] = TPL[sp['key']]
LAB = {'hairstyle': 'Hairstyle', 'skin colour (face)': 'Skin colour', 'skin colour (shoulders and arms)': 'Skin colour'}
def label(sp):
    l = sp['label']; l = l.split(':')[0]
    if sp['key'].startswith('expr_adult'): return 'Expression'
    if sp['key'] in ('penis_flaccid', 'penis_erect'): return 'Penis, ' + ('soft' if 'flaccid' in sp['key'] else 'erect')
    l = re.sub(r"^the (?:woman|man)'s ", '', l); l = re.sub(r' \(.*?\)$', '', l)
    return LAB.get(sp['label'], l[:1].upper() + l[1:])
def tidy(c):
    c = re.sub(r'\.? and His', '; his', c); c = c.replace('; The ', '; the '); c = re.sub(r'\b(\w+) \1\b', r'\1', c)
    c = re.sub(r'^(?:an? )?(?:eyes|eyebrows|lips|ears|hair|feet|hands|fingernails|nose|face|neck|figure|chest) (?:with|that are|that is) ', '', c)
    c = re.sub(r', (?:in|under) (?:a )?(?:soft|side|direct|bright) (?:gaze|light)', '', c)
    return c.strip().rstrip('.').rstrip(',')
def frame_phrase(frame, who):
    frame = frame.strip().rstrip(',')
    if ',' in frame:
        base, rest = frame.split(',', 1); rest = rest.strip()
        rest = re.sub(r'(^|, )of the bare', lambda m: m.group(1) + 'showing the bare', rest)
    else: base, rest = frame, ''
    return '%s of %s' % (base, who) + (', ' + rest if rest else '')
def cap(s): return s[:1].upper() + s[1:]
def wrap(inner, n_people='one person', extra=''):
    n = ('exactly ' + n_people) if n_people in ('one person', 'two people') else n_people
    return '(This panel is a self-contained photograph of %s, and nothing from any other panel appears in it. %s%s Everything outside this panel, including %s, is different from this one.)' % (n, inner, extra, 'the person' if n_people == 'one person' else 'the people, room and light')
def assemble(cells, tail=''):
    return ' '.join(HEAD.split()) + ' ' + ' '.join('The %s panel: %s' % (ORD[i], c) for i, c in enumerate(cells)) + tail
rows = []   # (key, sex, kind, text, seed, lora)
seed = 7100
LIMBKEYS = {'body_ratio'}
# ---- body features: ONE person per grid, only the feature in focus changes; close-ups turned partly to the left of frame
F2['head_chin_show'] = ['a sharp pointed chin, narrow and V-shaped', 'a heavy square jutting chin, flat across the bottom', 'a receding chin sloping back under the lower lip',
 'a soft rounded double chin with a fold of flesh beneath it', 'a small round chin with a single small dimple in the middle of its tip, a soft spot of shadow with no vertical line', 'a long narrow chin that comes to a gentle rounded point']
B.SPECS.insert(10, B.S('chin', 'chin', 'general', '__head_chin_show__', B.FACEF[:2] + B.FACEF[2:3]))
HAIR_P = ['dark brown hair pulled back off the face', 'black hair pulled back off the face', 'chestnut hair tied back from the face', 'light brown hair pulled back off the face', 'dark blond hair swept back off the face']
CLR = ['navy', 'charcoal grey', 'forest green', 'white', 'black', 'burgundy']
PARTS = {'face_shape': 'the face and jaw', 'chin': 'the chin and lower jaw', 'eyes': 'the eyes and brows', 'eyelashes': 'the eyes and lids', 'eyebrows': 'the eyebrows and forehead',
 'nose': 'the nose', 'lips': 'the lips and mouth', 'teeth': 'the smiling mouth and teeth', 'ears': 'one ear', 'cheeks_jaw': 'the cheeks, jaw and temples', 'neck': 'the neck and collarbones',
 'skin_tone': 'the face', 'skin_face': 'the face', 'skin_heritage': 'the face', 'expr_general': 'the face', 'facial_hair': 'the lower face', 'chest_hair': 'the bare chest',
 'hands': 'one open hand', 'nails': 'one hand with the fingers spread', 'feet': 'one bare foot', 'skin_body': 'the bare shoulder and upper arm'}
HEADK = {'face_shape', 'chin', 'eyes', 'eyelashes', 'eyebrows', 'nose', 'lips', 'teeth', 'ears', 'cheeks_jaw', 'skin_tone', 'skin_face', 'skin_heritage', 'expr_general', 'facial_hair'}
IDC = {}
def identity(sp, sex, r):
    ck = (sp['key'], sex)
    if ck not in IDC: IDC[ck] = identity0(sp, sex, random.Random(sum(map(ord, sp['key'])) * 17 + (7 if sex == B.W else 11)))
    return IDC[ck]
def identity0(sp, sex, r):
    key = sp['key']; who = 'woman' if sex == B.W else 'man'
    age = r.choice(['early thirties', 'late twenties', 'late thirties', 'early forties'])
    parts = ['adult %s in %s %s' % (who, 'her' if sex == B.W else 'his', age)]
    if not key.startswith('skin'):
        tone = re.sub(r' that is slightly darker on the hands and neck', '', B.g('__dem_tone__', r)); t = re.split(r', with | with ', tone)[0]; parts.append(t if 'skin' in t else t + ' skin')
    clinical = sp['group'] == 'adult' and not key.startswith('expr')
    if not clinical and not key.startswith('hair') and key not in ('hair_volume_line', 'facial_hair'):
        parts.append(r.choice(HAIR_P) if sex == B.W or key not in HEADK else r.choice(HAIR_P).replace('pulled back off the face', 'cut short'))
    if not clinical and (key in HEADK or key.startswith('hair') or key in ('neck', 'skin_body', 'hair_volume_line')): parts.append('wearing a plain %s crew-neck t-shirt' % r.choice(CLR))
    return ', '.join(parts)
def view(sp, frame):
    key = sp['key']
    if key == 'nose_profile': return 'A tight side-profile close-up of the nose'
    if 'clinical' in frame: return cap(frame_phrase(frame, 'the same person')) if False else None
    if key.startswith('hair') or key == 'hair_volume_line': return 'A head and shoulders view with the head turned about thirty degrees toward the left side of the frame, so that the front and the side of the hair are both in view'
    if key in ('body_ratio', 'legs_hips'): return 'A full-length view turned partly toward the left side of the frame, in plain fitted grey underwear, so that the front and a little of the side contour are both in view'
    part = PARTS.get(key, 'the ' + sp['label'])
    if key in HEADK or key == 'neck': return 'A tight close-up of %s with the head turned about thirty degrees toward the left side of the frame, so that the front of %s and a little of the side profile are both in view' % (part, part)
    return 'A close-up of %s, turned partly toward the left side of the frame so that the front and a little of the side contour are both in view' % part
for sp in B.SPECS:
    for k, (sex, frame, subj) in enumerate(sp['frames']):
        for rep in range(2):
            seed += 13; r = random.Random(seed); cells = []; seen = set(); tries = 0
            ident = identity(sp, sex, r); lab = label(sp); ll = lab.lower()
            v = view(sp, frame)
            if v is None:
                who = re.sub(r'^an adult', 'the same adult', subj) if subj.startswith('an adult') else subj
                v = cap(frame_phrase(frame, who))
            while len(cells) < 4 and tries < 300:
                tries += 1; c = tidy(B.clean_cell(B.cell(sp, sex, r)))
                if c in seen: continue
                seen.add(c)
                ex = LIMB if sp['key'] in LIMBKEYS else ' The hand has five fingers and belongs to one arm.' if sp['key'] in ('hands', 'nails') else ' The foot has five toes.' if sp['key'] == 'feet' else ''
                inner = '%s. %s: %s.' % (v, lab, c)
                cells.append('(This panel is a photograph of exactly one person, the same %s, %s, and nothing else from any other panel appears in it. %s%s Everything about this person other than the feature listed under %s is identical to the other panels.)' % (ident, GREYBG, inner, ex, lab))
            head = 'A grid of 4 equal photographic panels arranged in two rows of two columns, separated by thin plain white gaps. Every panel shows the same person in the same light against the same background; only the feature listed under %s changes from panel to panel.' % lab
            rows.append((sp['key'], sex, 'feature', ' '.join((head + ' ' + ' '.join('The %s panel: %s' % (ORD[i], c) for i, c in enumerate(cells))).split()), seed, False))
# ---- age progression (same person across panels)
AG = B.AGES
HS = B.HSKIN
AGC = {}
SETS = [[0, 2, 4, 6], [1, 3, 5, 7], [3, 5, 7, 8]]
for sex, kind in ((B.W, 'face'), (B.M, 'face'), (B.W, 'hands'), (B.M, 'hands')):
    for si, idxs in enumerate(SETS):
        seed += 17; r = random.Random(seed); sx = 'f' if sex == B.W else 'm'
        if (kind, sex) not in AGC: AGC[(kind, sex)] = (re.sub(r' that is slightly darker on the hands and neck', '', B.g('__dem_tone__', random.Random(900 + (kind == 'hands') * 3 + (sex == B.W)))), B.g('__eye_color__', random.Random(901)))
        tone, eyes = AGC[(kind, sex)]
        tshort = re.split(r', with | with ', tone)[0]; tshort = tshort if 'skin' in tshort else tshort + ' skin'
        who = 'woman' if sex == B.W else 'man'; cells = []
        for a in [AG[i] for i in idxs]:
            yrs = B.g('__%s_age_years__' % a, r)
            if kind == 'face': c = '%s; %s; eyes: %s; hair: %s' % (yrs, tidy(B.g('__%s_%s_aging_summary__' % (sx, a), r)), B.g('__%s_eye_lid__' % a, r), B.g('__%s_%s_hair_line__' % (sx, a), r))
            else: c = '%s; %s hand: %s; %s; %s' % (yrs, tshort, HS[AG.index(a)], B.g('__%s_hand_fingers__' % a, r), B.g('__%s_hand_knuckl__' % a, r))
            fr = 'a tight close-up of the face and hair with the head turned about thirty degrees toward the left side of the frame' if kind == 'face' else 'a close-up of one bare hand held open'
            cells.append('(This panel is a photograph of exactly one person, the same adult %s with %s and %s shown in every panel, ' % (who, tshort if kind == 'face' else tone, 'the same eye colour and bone structure' if kind == 'face' else 'the same hand shape') + GREYBG + ', and nothing else from any other panel appears in it. %s. Age: %s. Only the age-related features change from panel to panel.)' % (cap(fr), re.sub(r'\.$', '', clean := c)))
        rows.append(('age_%s_%s_%d' % (kind, who, si + 1), who, 'age', assemble(cells), seed, False))
# ---- poses, skin marks, tattoos, makeup: ONE person per grid, only the feature in focus changes
COL = ['navy', 'forest green', 'burgundy', 'mustard yellow', 'charcoal', 'teal', 'plum']
PROP = re.compile(r'\b(balcony|scooter|bicycle|bike|counter|table|umbrella|bus|curb|kerb|stairs?|steps|car|doorway|doorframe|door|chair|bench|wall|window|seat|sofa|couch|bed|desk|railing|fence|rail|tree|bag|phone|camera|cup|mug|coffee|drink|book|newspaper|map|ladder|stool|crate|box|rock|boulder|log|shopping|dog|ball|guitar)\b', re.I)
PCOL = {}
TURN = 'turned partly toward the left side of the frame so that the front and a little of the side are both in view'
PC = {}
def pid(who, r, hair=True, key=''):
    if (key, who) not in PC: PC[(key, who)] = pid0(who, random.Random(sum(map(ord, key)) * 31 + (3 if who == 'woman' else 5)), hair)
    return PC[(key, who)]
def pid0(who, r, hair=True):
    sex = B.W if who == 'woman' else B.M
    age = r.choice(['early thirties', 'late twenties', 'late thirties', 'early forties'])
    tone = re.sub(r' that is slightly darker on the hands and neck', '', B.g('__dem_tone__', r)); t = re.split(r', with | with ', tone)[0]; t = t if 'skin' in t else t + ' skin'
    h = (', ' + r.choice(HAIR_P if who == 'woman' else [x.replace('pulled back off the face', 'cut short') for x in HAIR_P])) if hair else ''
    return 'adult %s in %s %s, %s%s' % (who, 'her' if who == 'woman' else 'his', age, t, h)
def gridhead(focus): return 'A grid of 4 equal photographic panels arranged in two rows of two columns, separated by thin plain white gaps. Every panel shows the same person in the same plain clothing, in the same light against the same background; only the %s changes from panel to panel.' % focus
def pan(ident, inner, extra='', focus=''):
    return '(This panel is a photograph of exactly one person, the same %s, %s, and nothing else from any other panel appears in it. %s%s Everything about this person other than the %s is identical to the other panels.)' % (ident, GREYBG, inner, extra, focus)
def addrow(key, sex, focus, cells):
    global seed
    rows.append((key, sex, 'pose', ' '.join((gridhead(focus) + ' ' + ' '.join('The %s panel: %s' % (ORD[i], c) for i, c in enumerate(cells))).split()), seed, True))
def posegrid(key, who, pool):
    global seed
    for rep in range(3):
        seed += 11; r = random.Random(seed); ident = pid(who, r, key=pool); col = PCOL.setdefault((pool, who), r.choice(COL)); cells = []; seen = set()
        while len(cells) < 4:
            c = B.clean_cell(B.g('__age25_34_%s__' % pool, r))
            if PROP.search(c) or c in seen: continue
            seen.add(c)
            cells.append(pan(ident, 'A full-length view in plain fitted %s sportswear, %s. The pose: %s.' % (col, TURN, c.rstrip('.')), LIMB, 'pose'))
        addrow(key, who, 'pose', cells)
for who in ('woman', 'man'):
    for pool in ('pose_action', 'pose_twist', 'pose_weight'): posegrid('%s_%s' % (pool, who), who, pool)
    for rep in range(3):
        seed += 7; r = random.Random(seed); ident = pid(who, r, hair=False, key='skin_marks'); cells = []; seen = set()
        while len(cells) < 4:
            c = re.sub(r', that .*$', '', B.g('__age25_34_skin_marks__', r)).rstrip('.')
            if c in seen: continue
            seen.add(c); cells.append(pan(ident, 'A close-up of the bare skin where the mark is, %s. The skin mark: %s.' % (TURN, c), '', 'skin mark'))
        addrow('skin_marks_' + who, who, 'skin mark', cells)
    for rep in range(3):
        seed += 7; r = random.Random(seed); ident = pid(who, r, hair=False, key='tattoo'); cells = []; seen = set()
        while len(cells) < 4:
            c = re.sub(r'^(They have|He has|She has) ', '', B.g('__any_age25_34_opt_tattoo__', r)).rstrip('.')
            if c in seen: continue
            seen.add(c); cells.append(pan(ident, 'A close-up of the tattooed area of bare skin, %s. The tattoo: %s.' % (TURN, c), '', 'tattoo'))
        addrow('tattoos_' + who, who, 'tattoo', cells)
for who in ('woman', 'man'):
    for rep in range(3 if who == 'woman' else 2):
        seed += 5; r = random.Random(seed); ident = pid(who, r, key='makeup'); cells = []; seen = set()
        while len(cells) < 4:
            c = re.sub(r'^Special makeup, ', '', B.g('__body_makeup__', r), flags=re.I).rstrip('.')
            if re.search(r'no makeup|bare face|without', c, re.I) or c in seen: continue
            seen.add(c); cells.append(pan(ident, 'A tight close-up of the face with the head turned about thirty degrees toward the left side of the frame, so that the front of the face and a little of its side are both in view. The makeup: %s.' % c, '', 'makeup'))
        addrow('makeup_' + who, who, 'makeup', cells)
# ---- adult scene grids from the v106 structured panel pools
POOLS = {'l12': [('adult_l%d_panel_%s' % (L, s)) for L in (1, 2) for s in ('wm', 'ww', 'mm')],
         'l34': [('adult_l%d_panel_%s' % (L, s)) for L in (3, 4) for s in ('wm', 'ww', 'mm')],
         'l56': [n for L in (5, 6) for n in ('adult_l%d_panel_%s' % (L, s) for s in ('wm', 'ww', 'mm', 'wm_vaginal', 'wm_oral', 'wm_anal', 'ww_oral', 'ww_scissor', 'mm_oral', 'mm_anal', 'mm_hand')) if n in F2]}
for pair, pools in POOLS.items():
    for rep in range(4):
        seed += 19; r = random.Random(seed); cells = []; used = set(); tries = 0
        while len(cells) < 4 and tries < 100:
            tries += 1; pn = r.choice(pools); lines = [l for l in F2[pn] if l.strip()]; j = r.randrange(len(lines)); key = (pn.split('_panel_')[1].split('_')[0], j // 2)
            if (pn, j // 2) in used: continue
            used.add((pn, j // 2)); t = cap(g2('__%s__' % pn if False else lines[j], r))
            n = 'exactly two people' if not ('second man __' in lines[j] and 'second woman' in lines[j]) and 'third' not in lines[j] else 'the people described'
            cells.append(wrap(t + ' Each person in this panel has one head, two arms and two legs, and every hand, foot and limb belongs to the person it is described with.', n_people=n))
        rows.append(('adult_scene_' + pair, 'any', 'scene', assemble(cells), seed, True))
# ---- adult single-person / couple pose scenes (adult_lN_pose_scene), 2x2, one scene per panel
for pair, lv in (('l12', (1, 2)), ('l34', (3, 4)), ('l56', (5, 6))):
    for rep in range(4):
        seed += 23; r = random.Random(seed); cells = []; seen = set(); tries = 0
        while len(cells) < 4 and tries < 200:
            tries += 1; L = r.choice(lv); t = g2('__adult_l%d_pose_scene__' % L, r)
            t = cap(re.sub(r'\s+', ' ', t).strip().rstrip('.')) + '.'
            if t in seen: continue
            seen.add(t)
            n = 'one person' if re.match(r'^(A|An) (man|woman|nonbinary adult|person)\b', t) and not re.search(r'\b(second|another|two|each other|partner)\b', t) else 'the people described'
            cells.append(wrap(t + ' Each person in this panel has one head, two arms and two legs, and every hand, foot and limb belongs to the person it is described with.', n_people=n))
        rows.append(('adult_pose_' + pair, 'any', 'scene', assemble(cells), seed, True))
CAPL = {sp['key']: label(sp) for sp in B.SPECS}
def caplabel(key):
    if key in CAPL: return CAPL[key]
    for pre, l in (('pose_', 'Pose'), ('skin_marks', 'Skin marks'), ('tattoos', 'Tattoos'), ('makeup', 'Makeup'), ('age_face', 'Age: face'), ('age_hands', 'Age: hands'), ('adult_pose_', 'Pose scene'), ('adult_scene', 'Scene')):
        if key.startswith(pre): return l
    return None
def captioned(key, t):
    l = caplabel(key)
    if not l: return t
    cap_ = ' In the bottom left corner of this panel there is small plain white text reading \u201c%s\u201d.' % l
    parts = re.split(r'(?=The (?:first|second|third|fourth) panel: )', t)
    out = [parts[0]]
    for p in parts[1:]:
        p = p.rstrip()
        out.append(p[:-1] + cap_ + ')' if p.endswith(')') else p + cap_)
    return ' '.join(' '.join(out).split())
import math
def sz(P): return (round(math.sqrt(P) / 16) * 16,) * 2
def write(od):
    os.makedirs(od, exist_ok=True)
    for name, P in (('1024', 1024 * 1024), ('1408', 1408 * 1408)):
        w, h = sz(P); out = []
        for key, sex, kind, t, sd, lora in rows:
            t = captioned(key, ' '.join(t.split())).replace('"', '\\"')
            out.append('--prompt "%s%s" --steps 50 --cfg_scale 3.75 --seed %d --width %d --height %d' % ('<lora:MOSSwSh4rpD3tails:0.5> ' if lora else '', t, sd, w, h))
        open(od + 'Guyanonymous_Wildcards_showcase_updated_%s.txt' % name, 'w', encoding='utf8').write('\n'.join(out))
    open(od + 'Guyanonymous_Wildcards_showcase_updated_key.tsv', 'w').write('line\tkey\tkind\tsex\tseed\tchars\tcheck\n' + '\n'.join(
        '%d\t%s\t%s\t%s\t%d\t%d\t%s' % (i + 1, k, kd, sx, sd, len(t), ('TOKEN ' if ('__' in t or '@@' in t) else '') + ('SPACING' if '  ' in t else '') or 'ok') for i, (k, sx, kd, t, sd, lo) in enumerate(rows)))
    print(len(rows), 'prompts')
if __name__ == '__main__': write('/mnt/user-data/outputs/bodyshow2/')
