"""Body-feature grid showcase (separate from the release showcase; never committed to git)."""
import sys, os, random, re
sys.path.insert(0, '/home/claude/w/wildcards/_tools')
import expand as E
from paths import FINAL
files = E.load([FINAL])
W = 'woman'; M = 'man'
A = 'age25_34_'
def g(ref, r): return ' '.join(E.clean(E.expand(files, ref, r)).split())
ANUS = ['smooth, evenly pigmented perianal skin in a warm medium brown, with a small tight closed rosette of fine radial folds',
 'pale pink perianal skin with a small tight rosette, smooth and hairless',
 'light tan perianal skin with a soft rosette and a faint scatter of fine pale hairs around it',
 'deep dark brown perianal skin with a slightly darker ring around a closed, softly folded rosette',
 'olive perianal skin with a relaxed rosette showing gentle radial folds and a light dusting of dark hair',
 'rosy beige perianal skin, smooth, with a neat tight rosette and a slight ridge of skin at one side',
 'freckled fair perianal skin with a small closed rosette and a few fine reddish hairs',
 'honey-toned perianal skin with a gently puckered rosette and a smooth surrounding area',
 'dark espresso skin with a deep, evenly pigmented tight rosette, hairless and smooth',
 'tan perianal skin with moderately dense dark hair framing a soft, closed rosette',
 'pale olive skin with a slightly darker pigmented ring and a small relaxed rosette',
 'warm brown skin with fine radial folds and a thin line of paler skin along the cleft']
# spec: key, label, sex, group, cell template, frames (list of (sex, frame, bg-subject)), ncells
def S(key, label, group, tpl, frames, n=(6, 6, 9), pool=None, free=False):
    return dict(key=key, label=label, group=group, tpl=tpl, frames=frames, n=n, pool=pool, free=free)
FACEF = [(W, 'a tight front-facing close-up', "an adult woman in her early thirties"), (M, 'a tight front-facing close-up', "an adult man in his early thirties"), (W, 'a tight three-quarter close-up', "an adult woman in her late twenties")]
FACEP = [(W, 'a tight side-profile close-up', "an adult woman in her early thirties"), (M, 'a tight side-profile close-up', "an adult man in his early thirties"), (M, 'a tight front-facing close-up', "an adult man in his late thirties")]
SPECS = [
 S('face_shape', 'face shape', 'general', '__head_shape__ with __A_head_cheek__, __A_head_jaw__ and __head_chin__', FACEF),
 S('eyes', 'eyes', 'general', 'eyes with __eye_shape__, __A_eye_lid__, __A_eye_brow__, __eye_spacing__ and __eye_color__', FACEF),
 S('eyelashes', 'eyelashes and lids', 'general', 'eyes with __A_eye_lid__ and __SEX_eye_lash__', [(W, 'an extreme close-up of both eyes from the front', 'an adult woman in her early thirties'), (M, 'an extreme close-up of both eyes from the front', 'an adult man in his early thirties'), (W, 'an extreme close-up of one eye in three-quarter view', 'an adult woman in her late twenties')]),
 S('eyebrows', 'eyebrows and forehead', 'general', 'eyebrows that are __A_eye_brow__, above a forehead that is __head_brow__', FACEF),
 S('nose', 'nose', 'general', 'a nose with __nose_bridge__, __nose_tip__, __nose_nostril__ and __nose_philtr__', FACEF + FACEP[:1], n=(6, 6, 9, 6)),
 S('nose_profile', 'nose in profile', 'general', 'a nose with __nose_bridge__ and __nose_tip__', FACEP),
 S('lips', 'lips and mouth', 'general', 'lips that are __A_lip_fullness__, with __A_lip_cupid__ and __A_lip_corners__', FACEF),
 S('teeth', 'teeth and gums', 'general', 'a wide smile showing __A_lip_teeth__ and __A_lip_gums__', FACEF),
 S('ears', 'ears', 'general', 'ears that are __ear_shape__ with __ear_lobe__', [(W, 'a close-up of the side of the head showing one ear', 'an adult woman with her hair tied back'), (M, 'a close-up of the side of the head showing one ear', 'an adult man with short hair'), (W, 'a close-up of the side of the head showing one ear', 'an adult woman with her hair tied back')]),
 S('cheeks_jaw', 'cheeks, jaw and temples', 'general', 'a face with __A_head_cheek__, __A_head_jaw__ and __A_head_temple__', FACEP),
 S('neck', 'neck and collarbones', 'general', 'a neck that is __neck_length__ with __neck_clav__', [(W, 'a close-up of the neck and collarbones from the front', 'an adult woman'), (M, 'a close-up of the neck and collarbones from the front', 'an adult man'), (W, 'a close-up of the neck and collarbones in three-quarter view', 'an adult woman')]),
 S('skin_tone', 'skin tone', 'general', 'a face with __dem_tone__', FACEF),
 S('hair_curly', 'hairstyle: curly and coily', 'general', 'hair that is __SEX_HSTYLE_C__', [(W, 'a head and shoulders view from the front', 'an adult woman'), (M, 'a head and shoulders view from the front', 'an adult man'), (W, 'a head and shoulders view from behind', 'an adult woman')]),
 S('hair_kinky', 'hairstyle: tightly coiled', 'general', 'hair that is __SEX_HSTYLE_K__', [(W, 'a head and shoulders view from the front', 'an adult woman'), (M, 'a head and shoulders view from the front', 'an adult man'), (W, 'a head and shoulders view from behind', 'an adult woman')]),
 S('hair_straight', 'hairstyle: straight', 'general', 'hair that is __SEX_HSTYLE_S__', [(W, 'a head and shoulders view from the front', 'an adult woman'), (M, 'a head and shoulders view from the front', 'an adult man'), (W, 'a head and shoulders view from behind', 'an adult woman')]),
 S('hair_wavy', 'hairstyle: wavy', 'general', 'hair that is __SEX_HSTYLE_W__', [(W, 'a head and shoulders view from the front', 'an adult woman'), (M, 'a head and shoulders view from the front', 'an adult man'), (W, 'a head and shoulders view from behind', 'an adult woman')]),
 S('hair_volume_line', 'hair volume and hairline', 'general', 'hair with __SEX_HVOL_C__ and a hairline that is __SEX_HLINE__', [(W, 'a close-up of the hairline and forehead from the front', 'an adult woman'), (M, 'a close-up of the hairline and forehead from the front', 'an adult man'), (W, 'a close-up of the hairline and forehead in three-quarter view', 'an adult woman')]),
 S('facial_hair', 'facial hair', 'general', 'a lower face with __m_age25_34_facial_hair__', [(M, 'a tight front-facing close-up of the lower face', 'an adult man in his thirties')]*3),
 S('chest_hair', 'chest hair', 'general', 'a chest with __m_body_chesthair__', [(M, 'a close-up of the bare chest from the front', 'an adult man in his thirties')]*2),
 S('hands', 'hands and fingers', 'general', 'hands with __A_hand_fingers__ and __A_hand_knuckl__', [(W, 'a close-up of one hand held open in front of the camera', 'an adult woman'), (M, 'a close-up of one hand held open in front of the camera', 'an adult man'), (W, 'a close-up of one hand curled into a loose fist', 'an adult woman')]),
 S('nails', 'fingernails', 'general', 'fingernails that are __A_hand_nails__', [(W, 'a close-up of one hand with the fingers spread', 'an adult woman'), (M, 'a close-up of one hand with the fingers spread', 'an adult man')]),
 S('feet', 'feet and toes', 'general', 'feet with __A_hand_feet__', [(W, 'a close-up of one bare foot seen from above', 'an adult woman'), (M, 'a close-up of one bare foot seen from above', 'an adult man'), (W, 'a close-up of one bare foot seen from the side', 'an adult woman')]),
 S('body_ratio', 'body proportions', 'general', 'a figure with __SEX_RATIO__', [(W, 'a full-length view from the front in plain fitted grey underwear', 'an adult woman'), (M, 'a full-length view from the front in plain fitted grey underwear', 'an adult man')], n=(6, 6)),
 S('legs_hips', 'legs and hips', 'general', 'legs and hips with __SEX_MLEGS__ and __SEX_MHIPS__', [(W, 'a view from the waist down from the front in plain fitted grey underwear', 'an adult woman'), (M, 'a view from the waist down from the front in plain fitted grey underwear', 'an adult man')], n=(6, 6)),
 S('expr_general', 'facial expressions', 'general', 'a face showing __pose_emotion__ with a gaze that is __pose_gaze__', [(W, 'a tight front-facing close-up', 'an adult woman in her early thirties'), (M, 'a tight front-facing close-up', 'an adult man in his early thirties'), (W, 'a tight three-quarter close-up', 'an adult woman in her late twenties')]),
 S('skin_face', 'skin colour (face)', 'general', 'a face with __dem_tone__', FACEF),
 S('skin_body', 'skin colour (shoulders and arms)', 'general', 'bare shoulders and upper arms with __dem_tone__', [(W, 'a close-up of the bare shoulder and upper arm', 'an adult woman'), (M, 'a close-up of the bare shoulder and upper arm', 'an adult man'), (W, 'a close-up of the bare forearm and hand', 'an adult woman')]),
 S('skin_heritage', 'skin colour and undertone', 'general', 'a face with @@SKINPROFILE@@', FACEF),
 # adult
 S('breasts', 'breasts', 'adult', '__f_body_breasts__', [(W, 'a clinical three-quarter view of the bare chest', 'an adult woman'), (W, 'a clinical front view of the bare chest', 'an adult woman')]),
 S('nipples', 'nipples and areolas', 'adult', '__f_body_nipples__', [(W, 'a clinical close-up of one breast in three-quarter view', 'an adult woman'), (W, 'a clinical close-up of one breast from the front', 'an adult woman')]),
 S('buttocks_f', "the woman's buttocks", 'adult', '@@BUTT_f@@', [(W, 'a clinical three-quarter view from behind, framed from the waist to the mid-thigh, of the bare lower body', 'an adult woman'), (W, 'a clinical side view, framed from the waist to the mid-thigh, of the bare lower body', 'an adult woman')], free=True),
 S('vulva', 'vulva', 'adult', '@@VULVA@@', [(W, 'a clinical close view from low in front at a three-quarter angle, with the thighs apart, showing the full length of the labia from the mons down between the thighs to the perineum and the opening of the vagina,', 'an adult woman reclining on a plain examination couch with her knees bent and apart'), (W, 'a clinical close view from low in front, with the thighs apart, showing the full length of the labia from the mons down between the thighs to the perineum and the opening of the vagina,', 'an adult woman standing with her feet wide apart'), (W, 'a clinical close side-on three-quarter view with the thighs apart, showing the full depth of the labia from the mons down to the perineum and the opening of the vagina,', 'an adult woman reclining on a plain examination couch with her knees bent and apart')], n=(6, 6, 9)),
 S('pubic_hair_f', "the woman's pubic hair", 'adult', '@@PUBIC@@', [(W, 'a clinical front view of the bare pelvis', 'an adult woman standing'), (W, 'a clinical close view from low in front with the thighs apart, showing the mons and the full length of the labia down to the perineum,', 'an adult woman reclining on a plain examination couch with her knees bent and apart')], n=(6, 9)),
 S('penis_flaccid', 'penis (soft)', 'adult', '__m_body_genitals__', [(M, 'a clinical three-quarter view of the bare pelvis', 'an adult man standing'), (M, 'a clinical front view of the bare pelvis', 'an adult man standing')]),
 S('penis_erect', 'penis (erect)', 'adult', '__m_body_genitals_erect__', [(M, 'a clinical three-quarter view of the bare pelvis', 'an adult man standing'), (M, 'a clinical side view of the bare pelvis', 'an adult man standing')]),
 S('buttocks_m', "the man's buttocks", 'adult', '@@BUTT_m@@', [(M, 'a clinical three-quarter view from behind, framed from the waist to the mid-thigh, of the bare lower body', 'an adult man'), (M, 'a clinical side view, framed from the waist to the mid-thigh, of the bare lower body', 'an adult man')], free=True),
 S('pecs_nipples_m', "the man's chest and nipples", 'adult', '__m_body_pecs__ and __m_body_nipples__', [(M, 'a clinical three-quarter view of the bare chest', 'an adult man'), (M, 'a clinical front view of the bare chest', 'an adult man')]),
 S('anus_f', 'anal area (woman)', 'adult', '@@ANUS@@', [(W, 'a clinical three-quarter view of the bare buttocks and cleft from behind', 'an adult woman bending forward slightly'), (W, 'a clinical close view of the cleft and anal area in three-quarter view', 'an adult woman bending forward slightly')]),
 S('anus_m', 'anal area (man)', 'adult', '@@ANUS@@', [(M, 'a clinical three-quarter view of the bare buttocks and cleft from behind', 'an adult man bending forward slightly'), (M, 'a clinical close view of the cleft and anal area in three-quarter view', 'an adult man bending forward slightly')]),
]
for lv, rng in (('l1', 'adult_l1_expression'), ('l2', 'adult_l2_expression'), ('l3', 'adult_l3_expression'), ('l4', 'adult_l4_expression'), ('l5', 'adult_l5_expression'), ('l6', 'adult_l6_expression')):
    pass
SPECS += [
 S('expr_adult_l12', 'adult expressions, mild (levels 1 and 2)', 'adult', '@@EXPR12@@', [(W, 'a tight front-facing close-up', 'an adult woman in her early thirties'), (M, 'a tight front-facing close-up', 'an adult man in his early thirties')]),
 S('expr_adult_l34', 'adult expressions, aroused (levels 3 and 4)', 'adult', '@@EXPR34@@', [(W, 'a tight front-facing close-up', 'an adult woman in her early thirties'), (M, 'a tight front-facing close-up', 'an adult man in his early thirties')]),
 S('expr_adult_l56', 'adult expressions, intense (levels 5 and 6)', 'adult', '@@EXPR56@@', [(W, 'a tight front-facing close-up', 'an adult woman in her early thirties'), (M, 'a tight front-facing close-up', 'an adult man in his early thirties')]),
]
def cell(spec, sex, r):
    t = spec['tpl']
    sx = 'f' if sex == W else 'm'
    if t.startswith('@@BUTT_'):
        x = t[7]
        tex = ['smooth, even skin with a soft sheen', 'matte skin with faint cellulite dimpling across the buttocks and thighs', 'fine pale stretch marks across the hips and sides of the buttocks', 'light freckles and a few small moles across the skin', 'smooth skin with a few faint veins visible at the backs of the thighs', 'firm tight skin with a glossy healthy sheen', 'soft skin with gentle dimpling and fine creases below the buttocks', 'fine body hair and gentle goosebump texture on the skin', 'clear skin with a subtle tan line across the hips', 'slightly rough skin with small blemishes and a few scars']
        if x == 'm': tex = [q for q in tex if 'stretch' not in q] + ['visible muscle striations and fine body hair across the skin']
        if x == 'm':
            parts = ['his buttocks are ' + g('__m_butt_shape__', r) + ', and ' + g('__m_butt_cleft__', r), g('__m_butt_surround__', r), g('__m_butt_surround__', r), g('__m_butt_texture__', r), g('__m_butt_texture__', r)]
            parts = [(p.strip().rstrip('.')[:1].lower() + p.strip().rstrip('.')[1:]) for p in parts]
            return '; '.join(parts)
        parts = [g('__%s_body_buttocks__' % x, r), g('__%s_musc_legs__' % x, r), g('__dem_tone__', r).replace('across the face', 'across the skin'), r.choice(tex)]
        parts = [(p.strip().rstrip('.')[:1].lower() + p.strip().rstrip('.')[1:]) for p in parts]
        parts[0] = re.sub(r', with (?:a )?(?:slightly darker skin tone than the thighs|stretch marks|visible muscle definition when standing|soft skin that moves slightly with the body|smooth skin)$', '', parts[0])
        return '; '.join(parts)
    if t == '@@PUBIC@@':
        return (lambda h: h if 'shaved' in h else h + ', in a natural hair colour that suits her skin and her head hair')(r.choice(SAFE_HAIR)) + '; ' + r.choice(['smooth, softly closed outer labia', 'full, cushioned outer labia', 'slim outer labia with a narrow cleft', 'soft outer labia with fine creases']) + '; ' + g('__dem_tone__', r)
    if t == '@@VULVA@@':
        parts = [g('__f_body_labia_majora__', r), r.choice(SAFE_LABIA), g('__f_body_clitoris__', r), 'skin ' + g('__f_body_vulva_tone__', r), r.choice(['a softly closed vaginal opening between the inner labia', 'a visible vaginal opening framed by the inner labia', 'an opening partly sheltered by the inner folds', 'a relaxed vaginal opening with moist pink inner tissue']), (lambda h: h if 'shaved' in h else h + ', in a natural hair colour that suits her skin and her head hair')(r.choice(SAFE_HAIR))]
        parts = [(p.strip().rstrip('.')[:1].lower() + p.strip().rstrip('.')[1:]) for p in parts]
        return '; '.join(parts)
    if t == '@@ANUS@@': return r.choice(ANUS)
    if '@@SKINPROFILE@@' in t:
        import glob
        fs = sorted(glob.glob('/home/claude/w/wildcards/dem_skin_profile_*.txt')); fn = os.path.basename(r.choice(fs))[:-4]
        return t.replace('@@SKINPROFILE@@', g('__%s__' % fn, r))
    if t.startswith('@@EXPR'):
        lv = {'12': ('adult_l1_expression', 'adult_l2_expression'), '34': ('adult_l3_expression', 'adult_l4_expression'), '56': ('adult_l5_expression', 'adult_l6_expression')}[t[6:-2]]
        return g('__%s__' % r.choice(lv), r)
    t = t.replace('__A_', '__' + A).replace('__SEX_eye_lash__', '__%s_%seye_lash__' % (sx, A))
    t = t.replace('__SEX_HSTYLE_C__', '__%s_%shairstyle_C__' % (sx, A)).replace('__SEX_HSTYLE_K__', '__%s_%shairstyle_K__' % (sx, A)).replace('__SEX_HSTYLE_S__', '__%s_%shairstyle_S__' % (sx, A)).replace('__SEX_HSTYLE_W__', '__%s_%shairstyle_W__' % (sx, A))
    t = t.replace('__SEX_HVOL_C__', '__%s_%shairvol_C__' % (sx, A)).replace('__SEX_HLINE__', '__%s_%shair_line__' % (sx, A))
    t = t.replace('__SEX_RATIO__', '__%s_body_ratio__' % sx).replace('__SEX_MLEGS__', '__%s_musc_legs__' % sx).replace('__SEX_MHIPS__', '__%s_musc_hips__' % sx)
    return g(t, r)
SAFE_HAIR = ['smoothly shaved with no visible hair', 'neatly trimmed short dark hair over the mons', 'a thin trimmed vertical strip of dark hair', 'a bikini-line trim leaving a small natural triangle of hair', 'a natural, full bush of dark curly hair', 'dense, dark, coarse hair across the mons and the outer labia', 'sparse, fine, light hair over the mons', 'soft, fine, downy blonde hair', 'a natural medium-brown triangle of hair with a slight curl', 'auburn hair trimmed short', 'grey-streaked natural hair, trimmed short', 'fine straight black hair, lightly trimmed']
SAFE_LABIA = ['inner labia fully tucked between the outer labia, only a thin pink line visible', 'inner labia just visible at the edge of the outer labia, a few millimetres past it', 'inner labia that peek out about a centimetre as smooth, soft folds', 'inner labia that extend about a centimetre on one side and sit tucked on the other, a natural left-right difference', 'inner labia that extend about two centimetres with softly ruffled, slightly darker edges', 'inner labia of medium length with gently wavy edges and slightly deeper pigmentation', 'short, neat inner labia with smooth edges that sit flush with the outer labia', 'inner labia with fine wrinkles along their edges, extending about one and a half centimetres']
ORD = ['first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh', 'eighth', 'ninth']
LAYOUT = {4: ('two rows of two columns', 4), 6: ('two rows of three columns', 6), 8: ('two rows of four columns', 8), 9: ('three rows of three columns', 9)}
CTX = re.compile(r',? (?:in|from) (?:profile|soft light|side light|direct light|bright light|shadow|dim light|three-quarter view|close-up|the sunlight|sunlight)\b|,? from (?:the front|below|above|behind|the side)\b|,? when (?:the eyes are open wide|the hand is open|relaxed|looking sideways|looking down|looking up|looking away)\b|,? in (?:a )?(?:neutral|relaxed) (?:pose|state)\b', re.I)
def clean_cell(c):
    c = re.sub(r' that is slightly darker on the hands and neck| even when standing or sitting', '', c); c = CTX.sub('', c).strip().rstrip('.').rstrip(',')
    if c[:1].isupper() and not c[:2].isupper(): c = c[0].lower() + c[1:]
    return c
def prompts():
    out = []; idx = 0
    for sp in SPECS:
        for k, (sex, frame, subj) in enumerate(sp['frames']):
            idx += 1
            n = sp['n'][k % len(sp['n'])]
            r = random.Random(7000 + idx * 31)
            cells = []; seen = set()
            tries = 0
            while len(cells) < n and tries < 200:
                tries += 1
                c = clean_cell(cell(sp, sex, r))
                if c not in seen: seen.add(c); cells.append(c)
            lay = LAYOUT[n][0]
            if sp.get('free'):
                who = 'a different adult woman' if sex == W else 'a different adult man'
                lab = sp['label'].replace("the woman's ", '').replace("the man's ", '')
                if sp['key'] == 'buttocks_m':
                    head = ('A grid of %d equal photographic panels arranged in %s, separated by thin plain white gaps. Every panel is %s of %s with the same medium olive skin tone in every panel, on a plain pale grey background with identical soft even studio lighting. The skin colour never changes between panels; only the body does: the waist, back, hips, buttocks and thighs change shape, size, hair and skin texture, so each panel shows a clearly different body with its own %s.' % (n, lay, frame, who, lab))
                else:
                    head = ('A grid of %d equal photographic panels arranged in %s, separated by thin plain white gaps. Every panel is %s of %s, on a plain pale grey background with identical soft even studio lighting. The whole lower body is different in every panel: the waist, hips, buttocks and thighs change shape and proportion together, and the skin tone and skin texture change as well, so each panel shows a clearly different body with its own %s.' % (n, lay, frame, who, lab))
            else:
              who2 = re.sub(r'^an adult', 'a different adult', subj) if subj.startswith('an adult') else subj
              fl = sp['label'].split(':')[0].split(' (')[0]
              head = ('A grid of %d equal photographic panels arranged in %s, separated by thin plain white gaps. Every panel is %s of %s, on a plain pale grey background with identical soft even studio lighting, and the %s fills the whole panel. Any neighbouring parts of the body that appear in the frame change naturally from panel to panel to suit the %s, in their shape, proportion, skin tone and skin texture, so each panel looks like a real, different person.' % (n, lay, frame, who2, fl, fl))
            body = ' '.join('The %s panel: %s.' % (ORD[i], c) for i, c in enumerate(cells))
            out.append((sp, sex, n, head + ' ' + body, idx))
    return out
AGES = ['age18_24', 'age25_34', 'age35_44', 'age45_54', 'age55_64', 'age65_74', 'age75_84', 'age85_94', 'age95_120']
HSKIN = ['taut, smooth skin with no lines', 'smooth, firm skin', 'smooth skin with the first faint lines across the knuckles', 'fine lines across the back of the hand and slightly more visible veins', 'thinner skin with visible veins and a few small age spots', 'thin skin with fine creases, visible veins and age spots', 'thin crepey skin with many fine wrinkles, prominent veins and age spots', 'very thin, deeply wrinkled skin with prominent tendons, veins and many age spots', 'paper-thin, deeply creased skin with sharply prominent tendons and veins and large age spots']
def age_prompts():
    out = []; idx = 0
    for sex, frame, kind in ((W, 'a tight front-facing close-up of the face and hair', 'face'), (M, 'a tight front-facing close-up of the face and hair', 'face'), (W, 'a close-up of one bare hand held open', 'hands'), (M, 'a close-up of one bare hand held open', 'hands')):
        idx += 1; r = random.Random(8000 + idx * 17); sx = 'f' if sex == W else 'm'
        tone = re.sub(r' that is slightly darker on the hands and neck', '', g('__dem_tone__', r)); eyes = g('__eye_color__', r)
        tshort = re.split(r', with | with ', tone)[0]; tshort = tshort if 'skin' in tshort else tshort + ' skin'
        if kind == 'hands': tone = tshort
        cells = []
        for a in AGES:
            yrs = g('__%s_age_years__' % a, r)
            if kind == 'face':
                c = '%s; %s; eyes with %s; hair with %s' % (yrs, g('__%s_%s_aging_summary__' % (sx, a), r).rstrip('.'), g('__%s_eye_lid__' % a, r), g('__%s_%s_hair_line__' % (sx, a), r))
            else:
                c = '%s; %s hand with %s, %s and %s' % (yrs, tshort, HSKIN[AGES.index(a)], g('__%s_hand_fingers__' % a, r), g('__%s_hand_knuckl__' % a, r))
            cells.append(clean_cell(c))
        who = 'an adult woman' if sex == W else 'an adult man'
        head = ('A grid of 9 equal photographic panels arranged in three rows of three columns, separated by thin plain white gaps. Every panel is %s of the same %s, on a plain pale grey background with identical soft even studio lighting. The same person is shown in every panel, with %s and %s, and only the age-related features change from panel to panel, from youngest at the first panel to oldest at the ninth.' % (frame, who.replace('an adult ', ''), eyes, tone))
        body = ' '.join('The %s panel: %s.' % (ORD[i], c) for i, c in enumerate(cells))
        out.append(dict(key='age_%s_%s' % (kind, 'woman' if sex == W else 'man'), label='ageing (%s)' % kind, group='age'), ) if False else None
        out.append((dict(key='age_%s_%s' % (kind, 'woman' if sex == W else 'man'), label='age progression', group='age'), sex, 9, head + ' ' + body, 900 + idx))
    return out
import math
def sizes(rw, rh):
    o = []
    for P in (1024 * 1024, 1408 * 1408):
        w = math.sqrt(P * rw / rh); w16 = round(w / 16) * 16; h16 = round(P / w16 / 16) * 16; o.append((w16, h16))
    return o
RATIO = {4: (1, 1), 6: (3, 2), 8: (3, 2), 9: (1, 1)}
def write(od):
    allp = prompts() + age_prompts()
    files_ = {'general': ([], [], []), 'adult': ([], [], []), 'age': ([], [], [])}
    for sp, sex, n, t, i in allp:
        grp = sp['group']; rw, rh = RATIO[n]; sz = sizes(rw, rh); seed = 6000 + i * 13
        chk = []
        if t.count('"') % 2: chk.append('odd quotes')
        if '  ' in t or ' ,' in t: chk.append('spacing')
        if len(t) > 6500: chk.append('long')
        for k in (0, 1):
            w, h = sz[k]; files_[grp][k].append('--prompt "%s" --steps 50 --cfg_scale 3.75 --seed %d --width %d --height %d' % (t.replace('"', '\\"'), seed, w, h))
        files_[grp][2].append('\t'.join([sp['key'], sex, str(n), '%d:%d' % (rw, rh), '%dx%d' % sz[0], '%dx%d' % sz[1], str(seed), str(len(t)), '; '.join(chk) or 'ok']))
    names = {'general': 'bodyfeatures_general', 'adult': 'bodyfeatures_adult', 'age': 'bodyfeatures_age_progression'}
    for grp, (a, b, kk) in files_.items():
        base = od + 'Guyanonymous_Wildcards_' + names[grp]
        open(base + '_1024.txt', 'w').write('\n'.join(a)); open(base + '_1408.txt', 'w').write('\n'.join(b))
        open(base + '_key.tsv', 'w').write('key\tsex\tcells\tratio\tsize_1024eq\tsize_1408eq\tseed\tchars\tcheck\n' + '\n'.join(kk))
        print(grp, len(a))
if __name__ == '__main__' and len(sys.argv) > 1 and sys.argv[1] == 'write':
    write('/mnt/user-data/outputs/bodyshow/')
elif __name__ == '__main__':
    P = prompts(); print(len(P), 'prompts', sum(1 for p in P if p[0]['group'] == 'general'), 'general', sum(1 for p in P if p[0]['group'] == 'adult'), 'adult')
    for sp, sex, n, t, i in P[:2] + P[40:42]: print(i, sp['key'], len(t)); print(t[:900]); print()
