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
ORD = ['first', 'second', 'third', 'fourth', 'fifth', 'sixth']
HEAD = 'A grid of 6 equal photographic panels arranged in two rows of three columns, separated by thin plain white gaps. Every panel is a separate scene with its own person or people, and nothing is shared between panels.'
LIMB = ' The person has one head, two arms and two legs, and every hand, foot and limb belongs to that person.'
GREYBG = 'against a plain pale grey background under soft even studio light'
NUDE = ' The person is completely nude, wearing no clothing at all, with nothing covering any part of the body.'
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
SKINSEG = re.compile(r'undertone|^(?:[a-z,\- ]*)skin (?:tone|pale|fair|olive|brown|golden|tan|rosy|pink|colou?r|a |the same|matching|close|evenly|deeper|with a (?:matte|slight))|\b(?:pale|fair|olive|brown|golden|tan|porcelain|alabaster|ebony|ivory|copper|bronze|beige|peach|sunburned)[a-z\- ]* skin\b|^(?:slightly rough|smooth|soft|firm|clear|matte|fine)[a-z, \-]* skin\b')
def strip_skin(c, key):
    if key.startswith(('skin', 'age')): return c
    c = re.sub(r'\b(?:(?:pale|light|medium|dark|deep|fair|olive|tan|brown|pink|freckled|warm|rich|golden|dusky|rosy|ivory|ebony|copper|bronze|beige|reddish)[ ,-]+)+(?=perianal skin)', '', c)
    segs = [x.strip() for x in c.split(';')]
    segs = [x for x in segs if not SKINSEG.search(x)]
    c = '; '.join(segs)
    c = re.sub(r', (?:with )?skin tone matching the (?:vulva|surrounding skin)|,? matching the surrounding skin tone|, (?:and )?skin matching [^;,]*', '', c)
    return re.sub(r'\s+', ' ', c).strip().rstrip(';,')
STOP = set('a an the and with of to in on at is are her his their its that as by from into over under it be has have for this which while very slightly about'.split())
def _toks(c): return {w for w in re.findall(r"[a-z]+", c.lower()) if w not in STOP}
TRAITS = {'nipples': [r'width of a thumbnail', r'two centimetres', r'three and a half centimetres', r'five centimetres', r'seven centimetres', r'inverted|flat nipple|puffy'],
 'breasts': [r'small|petite|tiny', r'large|full|heavy', r'teardrop', r'flat|slim', r'sag|droop|low', r'round'],
 'buttocks_f': [r'flat', r'round|full|bubble|heavy|large', r'muscular|athletic', r'sag|low', r'small|compact|petite', r'shelf|high'],
 'buttocks_m': [r'flat', r'round|full|heavy|large', r'muscular|athletic', r'sag|low', r'small|compact|petite', r'wide'],
 'vulva': [r'slim|flat', r'prominent|full|plump', r'asymmetr|one side', r'tucked|thin pink line', r'extend|peek out', r'hood|glans'],
 'pubic_hair_f': [r'shav|smooth|bare|no visible', r'triangle', r'strip', r'dense|full|bush|untrimmed|thick', r'trim', r'sparse|fine|light'],
 'penis_flaccid': [r'small|short|below', r'above|large|long', r'uncircumcised', r'\\bcircumcised', r'average', r'vein'],
 'penis_erect': [r'shorter', r'longer|longer than', r'uncircumcised', r'\\bcircumcised', r'average', r'curv|upward|upright'],
 'pecs_nipples_m': [r'small|tiny', r'large|broad|wide', r'flat', r'puffy', r'hairy|hair', r'smooth'],
 'face_shape': [r'full, soft, rounded face', r'gaunt, bony face', r'narrows sharply to a small pointed chin', r'long, narrow face', r'broad, square face', r'balanced oval face|widens to a broad heavy jaw'],
 'anus_f': [r'small, tight rosette', r'wide rosette', r'flat, smooth rosette', r'ring of dense dark hair|dense dark', r'few scattered fine hairs|light dusting|pale hairs', r'puckered|raised ring|off the centre line'],
 'anus_m': [r'small, tight rosette', r'wide rosette', r'smooth, hairless rosette', r'dense, dark, curly hair|thick hair', r'light scatter of fine hairs|sparse hairs|pale hairs', r'puckered|raised ring|deep in a long crease']}
def diverse(cands, n, r, traits=None):
    """greedy farthest-first selection of n cells that differ most in wording, one start chosen at random."""
    cands = list(dict.fromkeys(cands))
    if len(cands) <= n: return cands
    T = [_toks(c) for c in cands]
    def dist(i, j): return 1 - len(T[i] & T[j]) / (len(T[i] | T[j]) or 1)
    pick = []
    for t in (traits or []):
        if len(pick) >= n: break
        m = [i for i, c in enumerate(cands) if i not in pick and re.search(t, c, re.I)]
        if m: pick.append(r.choice(m))
    if not pick: pick = [r.randrange(len(cands))]
    while len(pick) < n:
        best = max((i for i in range(len(cands)) if i not in pick), key=lambda i: min(dist(i, j) for j in pick))
        pick.append(best)
    return [cands[i] for i in pick]
COORD = {
 'buttocks_f': [(r'flat|minimal projection|little definition', 'a straight narrow waist, narrow hips and slim straight thighs'), (r'shelf|high-projection|bubble|very large|sweeping', 'a small waist, strongly flared wide hips and very full heavy thighs'), (r'muscular|athletic|toned|sprinter|lifted|firm', 'a defined waist, strong hips and toned muscular thighs'), (r'sag|low-set|drooping|relaxed|soft', 'softer lower-set hips and soft fuller upper thighs'), (r'small|compact|petite|neat|tight', 'a slim waist, narrow to medium hips and slim thighs'), (r'broad|wide|heavy|full|round|pear|large|plump', 'a defined waist, wide hips and full heavy thighs')],
 'buttocks_m': [(r'flat|narrow|little projection', 'a narrow waist, narrow hips and slim straight thighs'), (r'muscular|hard|athletic|round|compact', 'a tapered waist, strong hips and thick muscular thighs'), (r'sag|low-set|soft|pear|heavy|wide|large|full', 'a thicker waist, wide soft hips and heavy thighs')],
 'breasts': [(r'asymmetr|resection|mastectomy|reconstruct|implant', ''), (r'small|petite|flat|tiny|slim|narrow', 'a slim narrow ribcage, narrow shoulders and a flat stomach'), (r'large|full|heavy|dense|bubble|huge|big', 'a wider ribcage, fuller shoulders and a softer fuller midsection'), (r'teardrop|tall|elongated|long', 'a long slender torso with a narrow waist'), (r'sag|droop|low|pendulous', 'a softer torso with a fuller midsection')],
 'nipples': [(r'small|tiny|petite', 'small, high breasts on a slim chest'), (r'large|wide|broad|expansive|big|puffy|full', 'full, heavy breasts on a broad chest'), (r'flat|inverted', 'smaller, softer breasts on a slim chest')],
 'vulva': [(r'slim|flat|narrow|tucked|thin pink', 'a flat lower belly, narrow hips and slim thighs'), (r'prominent|full|plump|cushion|rounded|raised', 'a fuller pubic mound, wider hips and fuller thighs'), (r'asymmetr|one side|extend|peek|ruffled', 'softly rounded hips and medium thighs')],
 'pubic_hair_f': [(r'shav|smooth|bare|no visible', 'a flat lower belly and narrow hips'), (r'dense|full|bush|untrimmed|thick|coarse', 'wide rounded hips and fuller thighs'), (r'strip|triangle|trim', 'medium hips and toned thighs')],
 'penis_flaccid': [(r'small|below average|short', 'slim hips, a flat lower belly and lean thighs'), (r'above|large|long|big|thick|girth', 'broader hips, a stronger lower torso and thick muscular thighs'), (r'average', 'medium hips and ordinary thighs')],
 'penis_erect': [(r'shorter|small|below average', 'slim hips, a flat lower belly and lean thighs'), (r'longer|above|large|big|thick|girth|very', 'broader hips, a stronger lower torso and thick muscular thighs'), (r'average', 'medium hips and ordinary thighs')]}
COORD['anus_f'] = [(r'wide|deep|loosely', 'the buttocks around it are full and rounded, with a deep crease between them'),
                   (r'tight|tightly|small|flat|neat|puckered', 'the buttocks around it are firm and compact, with a narrow crease between them')]
COORD['anus_m'] = [(r'wide|deep|loosely', 'the buttocks around it are heavy and muscular, with a long deep crease between them'),
                   (r'tight|tightly|small|flat|neat|puckered', 'the buttocks around it are hard and flat, with a shallow crease between them')]
COORD['face_shape'] = [(r'puffy|bloated|heavy-jowled|round|pear', 'a full, soft, rounded face with fleshy cheeks, a soft fold under the jaw and a thick soft neck'),
                      (r'emaciated|sunken|hollow|gaunt|thin', 'a gaunt, bony face with hollow cheeks, a thin neck with visible tendons and sharp collarbones'),
                      (r'inverted|inverted-triangle|heart-shaped|heart|V-shaped|kite-shaped|kite|diamond-shaped|diamond', 'a face wide at the temples that narrows sharply to a small pointed chin, on a slim neck'),
                      (r'triangular|triangle', 'a face narrow across the forehead that widens to a broad heavy jaw, on a thick neck'),
                      (r'long|oblong|elongated-oval|elongated|lantern-shaped|lantern|rectangular|narrow|compressed', 'a long, narrow face, clearly taller than it is wide, on a long slender neck'),
                      (r'square|rounded-square|block|boxy|wide|angular', 'a broad, square face, almost as wide as it is tall, with a wide angular jaw on a thick strong neck'),
                      (r'oval|egg-shaped|egg|symmetrical', 'a balanced oval face, a little taller than it is wide, on a medium neck')]

# ---- v107 audit: one clear, high-contrast descriptor per panel, spread across real classes, with a plain visual clause
SEGKEEP = {'eyes': [0, 4], 'nose': [0, 1], 'cheeks_jaw': [0, 1], 'lips': [0], 'eyebrows': [0], 'eyelashes': [1], 'hands': [0], 'expr_general': [0]}
TEX = {'hair_curly': 'curly, coily hair', 'hair_kinky': 'tightly coiled hair', 'hair_straight': 'straight hair', 'hair_wavy': 'wavy hair'}
CLS = {
 'eyes': [(r'hooded|heavy upper lid', 'heavy upper lids fold down over the creases, so the lids barely show'), (r'monolid|single eyelid|single-fold', 'smooth upper lids with no visible crease'),
          (r'deep-set|deeply|sunken', 'deep-set eyes in shadowed sockets under the brow'), (r'downturned|droop', 'eyes that slope clearly down at the outer corners'),
          (r'cat-like|almond|slanted|upward tilt|lifted outer|upturned', 'almond eyes that tilt clearly upward at the outer corners'), (r'large|round|wide|doe-like|bulging|prominent', 'large, round, wide-open eyes with white showing around the iris'),
          (r'narrow|small|close|tight', 'small, narrow eyes set close together'), (r'.', 'medium almond eyes, evenly set')],
 'nose': [(r'crooked|broken|asymmetric|lean to one side|off-centre|off-center|bent|deviated', 'a nose that bends visibly to one side'), (r'swollen|inflamed', 'a swollen, reddened nose tip'), (r'aquiline|hooked|roman|humped|bump|convex|arched', 'a nose with a clear hump on the bridge'),
          (r'flat|wide|broad|boxy|bulbous|fleshy|thick', 'a broad, flat nose with a wide rounded tip and wide nostrils'), (r'upturned|button|upward tilt|tiny|small|snub', 'a small nose whose tip turns up, showing the nostrils'),
          (r'long|drooping|downward', 'a long nose whose tip points down'), (r'.', 'a narrow, straight nose with a fine tip')],
 'nose_profile': [(r'crooked|deviated|asymmetric|lean|bent', 'a bridge that leans visibly to one side'), (r'aquiline|hooked|roman|humped|bump|convex', 'in profile a clear hump on the bridge'), (r'upturned|button|upward', 'in profile a scooped bridge and a tip that turns up'),
          (r'bulbous|round heavy|blunt|wide|thick|fleshy|swollen', 'in profile a heavy rounded tip'), (r'drooping|downward|long', 'in profile a long bridge and a tip that hangs down'), (r'.', 'in profile a straight, flat bridge')],
 'lips': [(r'plump top|fuller lower|top lip thin|thin bottom', 'one lip clearly fuller than the other'), (r'asymmetric|crooked|uneven', 'lips that are uneven from side to side'),
          (r'thin|narrow|subtle|delicate|small', 'thin lips, the upper lip a narrow line'), (r'full|thick|lush|large|generous|heavy|broad|plump|voluminous|fleshy|massive|puffy|pillowy|cosmetic', 'very full, thick, pillowy lips'), (r'bow', "a sharply peaked Cupid's bow on medium lips"), (r'.', 'medium lips')],
 'cheeks_jaw': [(r'hollow|sunken|lean|narrow', 'hollow cheeks below sharp cheekbones'), (r'plump|fleshy|full|padded|rounded', 'round, full, padded cheeks'),
          (r'high|prominent|sculpted|bony', 'high, sharp cheekbones'), (r'square|wide jaw|disproportionate|broad thick', 'a wide, square jaw with sharp corners'),
          (r'asymmetric|uneven', 'cheeks uneven in height from side to side'), (r'broad|flat|wide', 'wide, flat cheeks across a broad face'), (r'V-shaped|pointed|slender tapered|delicate', 'a narrow jaw that tapers to the chin'), (r'.', 'a soft, rounded jaw with no sharp angle')],
 'hands': [(r'calloused|rough|dirty|hard-working|cracked', 'rough, calloused, work-worn hands'), (r'long|slender|graceful|narrow|elegant|thin|bony|gaunt|slim', 'long, slender fingers on a narrow hand'),
          (r'thick|broad|square|stubby|chunky', 'short, thick fingers on a broad hand'), (r'small|compact|petite|short', 'a small hand with short fingers'), (r'crooked|bent|asymmetric', 'fingers with crooked, bent joints'), (r'manicured|smooth|soft', 'smooth, soft, carefully manicured hands'), (r'.', 'a medium hand with even fingers')]}
TRAITS.update({
 **{k: [re.escape(x[1]) for x in v if x[0] != '.'] for k, v in CLS.items()},
 'eyebrows': [r'thick|full|bushy|heavy', r'sparse|thin|faint|gap', r'arched|peak', r'straight', r'shaved', r'untamed|long|elongated'],
 'eyelashes': [r'long|curl|flare|fluttery|doll', r'sparse|thin|gappy', r'short', r'dense|thick', r'fine|delicate|natural', r'separated|clump'],
 'neck': [r'long|swan|elegant', r'short|squat', r'thick|stocky|broad|strong', r'gaunt|tendons|jutting|sharp|protruding', r'padded|soft', r'medium'],
 'ears': [r'large|cupped|protruding', r'small|compact|tucked', r'pointed|elf', r'cauliflower|battered|torn|split', r'attached|plump|fleshy', r'low-set|high-set'],
 'feet': [r'wide|broad|thick', r'narrow|slender|small', r'high|arch', r'flat|collapsed', r'calloused|rough|dirty', r'long toes|second toe'],
 'legs_hips': [r'skinny|thin|stick|slender', r'heavy|plump|rolls|fleshy|rounded legs', r'muscular|sculpted|powerful|toned', r'wide pelvis|broad|developed|sturdy hips', r'narrow|flat|slim|lean hips', r'knock|bow'],
 'body_ratio': [r'pear|broad-hipped|low hip', r'inverted|V-shaped|wide-shouldered|athletic', r'balanced|equal', r'slender|narrow', r'long-torso|long legs', r'shorter legs'],
 'chest_hair': [r'dense|mat|thick', r'line|sternum|trail', r'shaved|hairless|smooth', r'moderate|natural', r'trimmed', r'stubble'],
 'expr_general': [r'joy|laugh|love|relief', r'anger|irritation|fury', r'sad|disappoint|brood|melanchol', r'surprise|shock|fear', r'calm|bored', r'smug|suspicion|doubt']})
def audit_cell(key, c):
    if key in SEGKEEP:
        sg = [x.strip() for x in c.split(';')]; c = '; '.join(sg[i] for i in SEGKEEP[key] if i < len(sg))
    if key == 'lips': c = re.sub(r',? (?:in a [^,;]*expression|in a soft smile|with the lips pressed together)', '', c)
    if key == 'chest_hair': c = re.sub(r', (?:that [^,;]*|on a [^,;]* chest)$', '', c)
    if key == 'pecs_nipples_m': c = re.sub(r'\b(?:and )?(?:pale pink|dark brown|medium brown|light brown|tan|pink|brown)\b,? ?', '', c).replace('are small ', 'are small, ').replace('are wide ', 'are wide, ').replace('are large ', 'are large, ')
    if key in ('penis_flaccid', 'penis_erect'):
        c = re.sub(r', with (?:a few faint veins|a pronounced vein pattern|smooth shaft skin and almost no visible veins)[^,;]*', '', c); c = re.sub(r',? with an? [^;]*?scrotum(?: slightly darker than the surrounding skin)?', '', c); c = c.replace(' slightly darker than the surrounding skin', '')
        c = re.sub(r'\b(slightly below average|small|shorter but thick)\b', r'\1, clearly short', c, 1); c = re.sub(r'\b(large|longer than average)\b', r'\1, clearly long and heavy', c, 1)
    if key in CLS:
        sg = [re.split(r', | with | under | framed | in a ', x.strip())[0] for x in c.split(';')]
        probe = sg[0] if key in ('eyes', 'cheeks_jaw') else ' '.join(sg)
        cl = next(cl for rx, cl in CLS[key] if re.search(r'\b(?:%s)' % rx, probe, re.I))
        c = '; '.join(sg) + '; ' + cl
    if key in TEX: c = TEX[key] + ', ' + c
    return c
def cell_ok(key, c):
    if key == 'pubic_hair_f': return bool(re.search(r'hair|shav', c, re.I))
    return True
def shape_cell(key, c):
    if key == 'face_shape': c = c.split(';')[0].strip()
    if key in ('anus_f', 'anus_m') and re.search(r'cheek', c, re.I): return c
    if key in ('buttocks_f', 'buttocks_m'): c = c.split(';')[0].strip()
    elif key == 'vulva': c = '; '.join(x.strip() for x in c.split(';')[:2])
    elif key == 'pubic_hair_f':
        c = c.split(';')[0].strip(); c = re.sub(r',? in a natural hair colour that suits her skin and her head hair', ', in the same hair colour as her head hair', c)
    elif key in ('penis_flaccid', 'penis_erect'):
        c = re.sub(r', below [^,]*(?:pubic|hair)[^,]*', '', c); c = re.sub(r', with shaft skin [^,]*', '', c)
    for rx, clause in COORD.get(key, []):
        if re.search(r'\b(?:%s)\b' % rx, c, re.I):
            return c + ('; ' + clause if clause else '')
    return c
LADDER = re.compile(r'centimetres|thumbnail')
def cands_for(sp, sex, r, tries=150):
    out = []
    for _ in range(tries):
        c = shape_cell(sp['key'], strip_skin(tidy(B.clean_cell(B.cell(sp, sex, r))), sp['key']))
        c = audit_cell(sp['key'], c) if c else c
        if c and not cell_ok(sp['key'], c): continue
        if c and not re.search(r'reconstruct|mastectomy|resection|implant|surgical|scar|tattoo|prosthe', c, re.I): out.append(c)
    if sp['key'] == 'face_shape': out = [c for c in out if '; ' in c]
    if sp['key'] == 'nipples':
        lad = list(dict.fromkeys(c for c in out if LADDER.search(c)))
        if len(lad) >= 6: return lad
    return out
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
for _sp in B.SPECS:
    if _sp['key'] == 'anus_f': _sp['tpl'] = '__f_body_anus__'
    if _sp['key'] == 'anus_m': _sp['tpl'] = '__m_body_anus__'
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
    return ', '.join(parts)
def view(sp, frame):
    key = sp['key']
    if key == 'nose_profile': return 'A tight side-profile close-up of the nose'
    if 'clinical' in frame: return cap(frame_phrase(frame, 'the same person')) if False else None
    if key.startswith('hair') or key == 'hair_volume_line': return 'A head and shoulders view with the head turned about thirty degrees toward the left side of the frame, so that the front and the side of the hair are both in view'
    if key in ('body_ratio', 'legs_hips'): return 'A full-length view of the whole nude body turned partly toward the left side of the frame, so that the front and a little of the side contour are both in view'
    part = PARTS.get(key, 'the ' + sp['label'])
    if key in HEADK or key == 'neck': return 'A tight close-up of %s with the head turned about thirty degrees toward the left side of the frame, so that the front of %s and a little of the side profile are both in view' % (part, part)
    return 'A close-up of %s, turned partly toward the left side of the frame so that the front and a little of the side contour are both in view' % part
USED = {}
SAME = {'eyes': 'skin colour and hair colour', 'skin': 'hair colour, eye colour, face and build'}
for sp in B.SPECS:
    for k, (sex, frame, subj) in enumerate(sp['frames']):
        for rep in range(2):
            seed += 13; r = random.Random(seed); cells = []; seen = set(); tries = 0
            ident = identity(sp, sex, r); lab = label(sp); ll = lab.lower()
            v = view(sp, frame)
            if v is None:
                who = re.sub(r'^an adult', 'the same adult', subj) if subj.startswith('an adult') else subj
                v = cap(frame_phrase(frame, who))
            used = USED.setdefault((sp['key'], sex), set()); tr = list(TRAITS.get(sp['key'], [])); r.shuffle(tr)
            allc = list(dict.fromkeys(cands_for(sp, sex, r))); pool_ = [c for c in allc if c not in used]
            if sp['key'] in CLS or sp['key'] in ('face_shape', 'penis_erect', 'penis_flaccid') and len(pool_) < 6: pool_ = allc   # spread across classes matters more than never repeating a wording
            if len(pool_) < 4:
                if rep == 1: continue
                pool_ = allc
            n_ = 6 if len(pool_) >= 6 else 4 if len(pool_) >= 4 else 0
            if not n_: continue
            if sp['key'] == 'vulva':
                seen2 = {}; [seen2.setdefault(c.split(';')[1].strip() if ';' in c else c, c) for c in r.sample(pool_, len(pool_))]; pool_ = list(seen2.values())
                n_ = 6 if len(pool_) >= 6 else 4 if len(pool_) >= 4 else n_
            picks = diverse(pool_, n_, r, tr); used.update(picks)
            for c in picks:
                ex = LIMB if sp['key'] in LIMBKEYS else ' The hand has five fingers and belongs to one arm.' if sp['key'] in ('hands', 'nails') else ' The foot has five toes.' if sp['key'] == 'feet' else ''
                inner = '%s. %s: %s.' % (v, lab, c)
                cells.append(('(This panel is a photograph of exactly one person, the same %s, %s, and nothing else from any other panel appears in it. %s%s' + NUDE + ' This is the same person in every panel, with the same ' + SAME.get(sp['key'][:4] if sp['key'].startswith('skin') else sp['key'], 'skin colour, hair colour and eye colour') + '; only the feature listed under %s changes. Any neighbouring parts of the body in the frame, such as the hips, waist, thighs, torso or limbs, change naturally to suit the feature listed under %s, in shape and proportion' + ('' if sp['key'].startswith('skin') else ' but never in skin colour') + '.)') % (ident, GREYBG, inner, ex, lab, lab))
            head = ('A grid of %d equal photographic panels arranged in two rows of %s columns,' % (n_, 'three' if n_ == 6 else 'two')) + ' separated by thin plain white gaps. Every panel shows the same person in the same light against the same background; only the feature listed under %s changes from panel to panel.' % lab
            rows.append((sp['key'], sex, 'feature', ' '.join((head + ' ' + ' '.join('The %s panel: %s' % (ORD[i], c) for i, c in enumerate(cells))).split()), seed, False))
# ---- age progression (same person across panels)
AG = B.AGES
HS = B.HSKIN
AGC = {}
SETS = [[0, 2, 4, 6, 7, 8], [1, 3, 4, 5, 7, 8]]
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
            cells.append('(This panel is a photograph of exactly one person, the same adult %s with %s and %s shown in every panel, ' % (who, tshort if kind == 'face' else tone, 'the same eye colour and bone structure' if kind == 'face' else 'the same hand shape') + GREYBG + ', and nothing else from any other panel appears in it. %s. The person is completely nude, wearing no clothing at all, with nothing covering any part of the body. Age: %s. Only the age-related features change from panel to panel.)' % (cap(fr), re.sub(r'\.$', '', clean := c)))
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
def gridhead(focus, nude=False):
    who = 'the same completely nude person, wearing no clothing at all,' if nude else 'the same person in the same plain clothing,'
    return 'A grid of 6 equal photographic panels arranged in two rows of three columns, separated by thin plain white gaps. Every panel shows %s in the same light against the same background; only the %s changes from panel to panel.' % (who, focus)
def pan(ident, inner, extra='', focus=''):
    return '(This panel is a photograph of exactly one person, the same %s, %s, and nothing else from any other panel appears in it. %s%s Everything about this person other than the %s is identical to the other panels.)' % (ident, GREYBG, inner, extra, focus)
def addrow(key, sex, focus, cells, nude=False):
    global seed
    rows.append((key, sex, 'pose', ' '.join((gridhead(focus, nude) + ' ' + ' '.join('The %s panel: %s' % (ORD[i], c) for i, c in enumerate(cells))).split()), seed, True))
def posegrid(key, who, pool):
    global seed
    for rep in range(3):
        seed += 11; r = random.Random(seed); ident = pid(who, r, key=pool); col = PCOL.setdefault((pool, who), r.choice(COL)); cells = []; seen = set()
        while len(cells) < 6:
            c = B.clean_cell(B.g('__age25_34_%s__' % pool, r))
            if PROP.search(c) or c in seen: continue
            seen.add(c)
            cells.append(pan(ident, 'A full-length view in plain fitted %s sportswear, %s. The pose: %s.' % (col, TURN, c.rstrip('.')), LIMB, 'pose'))
        addrow(key, who, 'pose', cells)
for who in ('woman', 'man'):
    for rep in range(3):
        seed += 7; r = random.Random(seed); ident = pid(who, r, hair=False, key='skin_marks'); cells = []; seen = set()
        while len(cells) < 6:
            c = re.sub(r', that .*$', '', B.g('__age25_34_skin_marks__', r)).rstrip('.')
            if c in seen: continue
            seen.add(c); cells.append(pan(ident, 'A close-up of the bare skin where the mark is, %s. The skin mark: %s.' % (TURN, c), NUDE, 'skin mark'))
        addrow('skin_marks_' + who, who, 'skin mark', cells, nude=True)
    for rep in range(3):
        seed += 7; r = random.Random(seed); ident = pid(who, r, hair=False, key='tattoo'); cells = []; seen = set()
        while len(cells) < 6:
            c = re.sub(r'^(They have|He has|She has) ', '', B.g('__any_age25_34_opt_tattoo__', r)).rstrip('.')
            if c in seen: continue
            seen.add(c); cells.append(pan(ident, 'A close-up of the tattooed area of bare skin, %s. The tattoo: %s.' % (TURN, c), NUDE, 'tattoo'))
        addrow('tattoos_' + who, who, 'tattoo', cells, nude=True)
for who in ('woman', 'man'):
    for rep in range(3 if who == 'woman' else 2):
        seed += 5; r = random.Random(seed); ident = pid(who, r, key='makeup'); cells = []; seen = set()
        while len(cells) < 6:
            c = re.sub(r'^Special makeup, ', '', B.g('__body_makeup__', r), flags=re.I).rstrip('.')
            if re.search(r'no makeup|bare face|without', c, re.I) or c in seen: continue
            seen.add(c); cells.append(pan(ident, 'A tight close-up of the face with the head turned about thirty degrees toward the left side of the frame, so that the front of the face and a little of its side are both in view. The makeup: %s.' % c, NUDE, 'makeup'))
        addrow('makeup_' + who, who, 'makeup', cells, nude=True)
# ---- poses (last): solo, two-person and three-person grids; the same people in the same outfits in every panel, outfits chosen to suit the pose
OUT = {'sport': ('a fitted %s sports top and leggings', 'a fitted %s t-shirt and running shorts'), 'yoga': ('a fitted %s leotard and leggings', 'a fitted %s sleeveless top and yoga shorts'),
       'casual': ('a plain %s blouse and dark jeans', 'a plain %s shirt and dark jeans'), 'formal': ('a knee-length %s evening dress', 'a dark suit with a %s shirt open at the collar'),
       'weight': ('a plain %s t-shirt and dark jeans', 'a plain %s t-shirt and dark jeans')}
CL2 = ['navy', 'forest green', 'burgundy', 'charcoal', 'teal', 'plum', 'mustard yellow', 'white']
def outfit(kind, sex, i): return OUT[kind][0 if sex == 'woman' else 1] % CL2[i % len(CL2)]
def rdesc(who, key): return pid(who, random.Random(1), key=key)
def two(kind, pair, c, names):
    wl, wr = {'wm': ('woman', 'man'), 'ww': ('woman', 'woman'), 'mm': ('man', 'man')}[pair]
    a, b = rdesc(wl, 'duo_%s_%s_l' % (names, pair)), rdesc(wr, 'duo_%s_%s_r' % (names, pair))
    if wl == wr and a == b: b = rdesc(wr, 'duo_%s_%s_r2' % (names, pair))
    oa, ob = outfit(kind, wl, 0), outfit(kind, wr, 3)
    return a, b, oa, ob
SOLO = [('pose_action', 'sport', 'poses: action'), ('pose_twist', 'yoga', 'poses: twisting and bending'), ('pose_weight', 'weight', 'poses: weight shifts')]
for who in ('woman', 'man'):
    for pool, kind, nm in SOLO:
        for rep in range(2):
            seed += 11; r = random.Random(seed); ident = pid(who, r, key=pool) + ', wearing ' + outfit(kind, who, 1 if who == 'woman' else 2); cells = []; seen = set(); tries = 0
            while len(cells) < 6 and tries < 400:
                tries += 1; c = B.clean_cell(B.g('__age25_34_%s__' % pool, r))
                if PROP.search(c) or c in seen: continue
                seen.add(c); cells.append(pan(ident, 'A full-length view, %s. The pose: %s.' % (TURN, c.rstrip('.')), LIMB, 'pose'))
            addrow('pose_solo_%s_%s' % (pool[5:], who), who, 'pose', cells)
# activity poses from the v107 pools, in the clothing that activity is actually done in
ACTS = [('yoga', 'act_yoga_action', 'act_yoga_clothes'), ('dance', 'act_dance_classes_action', 'act_dance_classes_clothes'), ('martial', 'act_martial_arts_action', 'act_martial_arts_clothes')]
def lib(fn): return [l.strip() for l in open('/home/claude/w/wildcards/%s.txt' % fn, encoding='utf8') if l.strip()]
for who in ('woman', 'man'):
    for nm, af, cf in ACTS:
        acts = lib(af); cl = [c for c in lib(cf) if 'loose stretchy' not in c]
        out = cl[0 if who == 'woman' else min(1, len(cl) - 1)]
        for gi in range(2):
            seed += 11; r = random.Random(seed)
            ident = pid(who, r, key='act_' + nm) + ', wearing ' + out
            grp = acts[gi * 6:gi * 6 + 6]
            if len(grp) < 6: break
            cells = [pan(ident, 'A full-length view, %s. The pose: the person is %s.' % (TURN, c.rstrip('.')), LIMB, 'pose') for c in grp]
            addrow('pose_solo_%s_%s_%d' % (nm, who, gi + 1), who, 'pose', cells)
PAIRSETS = [('sport', ['arm_wrestle', 'carry', 'chase', 'duel_fists', 'pull_rope', 'piggyback_race', 'pass_baton', 'lift_box']),
            ('formal', ['dance_ballroom', 'dance_folk', 'dance_slow', 'lesson_dance', 'embrace', 'hug_goodbye']),
            ('casual', ['argument', 'back_to_back', 'cards', 'chess', 'comfort', 'confess', 'cooking', 'gift', 'handshake', 'interview', 'kiss_cheek', 'laugh', 'read_together', 'repair', 'selfie', 'toast', 'trade', 'whisper', 'stare_down', 'photo'])]
for pair in ('wm', 'ww', 'mm'):
    for kind, names in PAIRSETS:
        groups = [names[i:i + 6] for i in range(0, len(names), 6)]
        groups = [g_ for g_ in groups if len(g_) == 6] or [names[:6]]
        for gi, grp in enumerate(groups):
            seed += 29; r = random.Random(seed); a, b, oa, ob = two(kind, pair, None, '%s%d' % (kind, gi)); cells = []
            for nm in grp:
                arr = ' '.join(open('/home/claude/w/wildcards/pi_%s_arrangement.txt' % nm, encoding='utf8').read().split())
                cells.append('(This panel is a photograph of exactly two people, the same two people in every panel: the person on the left is the same %s, wearing %s; the person on the right is the same %s, wearing %s. %s. A view from head to knees of both people. The pose: %s Each person has one head, two arms and two legs, and every hand, foot and limb belongs to the person it is described with. Nothing from any other panel appears in it. Everything about these two people other than their pose is identical to the other panels.)' % (a, oa, b, ob, GREYBG.replace('against', 'They are against').replace('under', 'under'), arr))
            rows.append(('pose_pair_%s_%s_%d' % (pair, kind, gi + 1), pair, 'pose', ' '.join(('A grid of 6 equal photographic panels arranged in two rows of three columns, separated by thin plain white gaps. Every panel shows the same two people in the same clothes against the same background; only their pose changes from panel to panel. ' + ' '.join('The %s panel: %s' % (ORD[i], c) for i, c in enumerate(cells))).split()), seed, True))
TRIO = {'wwm': (['the first woman', 'the second woman', 'the man'], ['woman', 'woman', 'man']), 'wmm': (['the woman', 'the first man', 'the second man'], ['woman', 'man', 'man']),
        'mmm': (['the first man', 'the second man', 'the third man'], ['man', 'man', 'man']), 'www': (['the first woman', 'the second woman', 'the third woman'], ['woman', 'woman', 'woman'])}
TRIOHEAD = {'wwm': 'a woman ; a second woman ; and a man ', 'wmm': 'a woman ; a man ; and a second man ', 'mmm': 'a man ; a second man ; and a third man ', 'www': 'a woman ; a second woman ; and a third woman '}
l1 = [x.strip() for x in open('/home/claude/w/wildcards/adult_l1_group.txt', encoding='utf8') if len(x) > 500]
for combo, (roles, sexes) in TRIO.items():
    lines = [x for x in l1 if re.sub(r'__apose_person_[fm]__', '', re.match(r'This scene shows three adults, which is (.*?)\. ', x).group(1)) == TRIOHEAD[combo]]
    seed += 31; ds = [rdesc(sx, 'trio_%s_%d' % (combo, k)) for k, sx in enumerate(sexes)]
    outs = [outfit('casual', sx, k + 1) for k, sx in enumerate(sexes)]
    who_ = '; '.join('%s is the same %s, wearing %s' % (rl, d, o) for rl, d, o in zip(roles, ds, outs))
    cells = []
    for ln in lines[:6]:
        body = re.match(r'This scene shows three adults, which is .*?\. (.*)', ln).group(1)
        sents = [x for x in re.split(r'(?<=\.) ', body) if ' wears ' not in x and not x.startswith(('The scene is', 'The light is', 'The shot shows')) and 'groin' not in x]
        cells.append('(This panel is a photograph of exactly three people, the same three people in every panel: %s. %s They are against a plain pale grey background under soft even studio light. A view from head to knees of all three. Each person has one head, two arms and two legs, and every hand, foot and limb belongs to the person it is described with. Nothing from any other panel appears in it. Everything about these three people other than their pose is identical to the other panels.)' % (who_, ' '.join(sents)))
    rows.append(('pose_trio_%s' % combo, combo, 'pose', ' '.join(('A grid of 6 equal photographic panels arranged in two rows of three columns, separated by thin plain white gaps. Every panel shows the same three people in the same clothes against the same background; only their pose changes from panel to panel. ' + ' '.join('The %s panel: %s' % (ORD[i], c) for i, c in enumerate(cells))).split()), seed, True))
CAPL = {sp['key']: label(sp) for sp in B.SPECS}
def caplabel(key):
    if key in CAPL: return CAPL[key]
    for pre, l in (('pose_pair', 'Two-Person Pose'), ('pose_trio', 'Three-Person Pose'), ('pose_', 'Pose'), ('skin_marks', 'Skin marks'), ('tattoos', 'Tattoos'), ('makeup', 'Makeup'), ('age_face', 'Age: face'), ('age_hands', 'Age: hands'), ('adult_pose_', 'Pose scene'), ('adult_scene', 'Scene')):
        if key.startswith(pre): return l
    return None
TITLES = {'Face shape': 'Face Shape', 'Eyes': 'Eye', 'Eyelashes and lids': 'Eyelash', 'Eyebrows and forehead': 'Eyebrow', 'Nose': 'Nose', 'Nose in profile': 'Nose Profile', 'Lips and mouth': 'Lip',
 'Teeth and gums': 'Teeth', 'Ears': 'Ear', 'Cheeks, jaw and temples': 'Cheek and Jaw', 'Chin': 'Chin', 'Neck and collarbones': 'Neck', 'Skin tone': 'Skin Tone', 'Hairstyle': 'Hairstyle',
 'Hair volume and hairline': 'Hairline', 'Facial hair': 'Facial Hair', 'Chest hair': 'Chest Hair', 'Hands and fingers': 'Hand', 'Fingernails': 'Fingernail', 'Feet and toes': 'Foot',
 'Body proportions': 'Body Proportion', 'Legs and hips': 'Leg and Hip', 'Facial expressions': 'Expression', 'Expression': 'Expression', 'Skin colour': 'Skin Colour', 'Skin colour and undertone': 'Skin Colour',
 'Breasts': 'Breast', 'Nipples and areolas': 'Nipple', 'Buttocks': 'Buttock', 'Vulva': 'Vulva', 'Pubic hair': 'Pubic Hair', 'Penis, soft': 'Penis', 'Penis, erect': 'Penis', 'Chest and nipples': 'Chest',
 'Anal area': 'Anal Area', 'Pose': 'Pose', 'Two-Person Pose': 'Two-Person Pose', 'Three-Person Pose': 'Three-Person Pose', 'Skin marks': 'Skin Mark', 'Tattoos': 'Tattoo', 'Makeup': 'Makeup', 'Age: face': 'Face Age', 'Age: hands': 'Hand Age', 'Scene': 'Scene', 'Pose scene': 'Pose Scene'}
def title(l): return TITLES.get(l, l) + ' Variations'
def tail(l):
    return " In the bottom left corner of the whole image, not inside any panel, there is small plain white text reading \u201c%s\u201d, appearing once only, with a second line in smaller white text directly beneath it reading \u201cGuyanonymous' Wildcards\u201d." % title(l)
def captioned(key, t):
    l = caplabel(key)
    if not l: return t
    return ' '.join(t.split()) + tail(l)
import math
def sz(P): return (round(math.sqrt(P) / 16) * 16,) * 2
def write(od):
    os.makedirs(od, exist_ok=True)
    for name, P in (('1024', 1024 * 1024), ('1408', 1408 * 1408)):
        out = []
        for key, sex, kind, t, sd, lora in rows:
            w, h = B.sizes(*((1, 1) if 'grid of 4 ' in t[:20] else (3, 2)))[0 if name == '1024' else 1]
            t = captioned(key, ' '.join(t.split())).replace('"', '\\"')
            out.append('--prompt "%s%s" --steps 50 --cfg_scale 3.75 --seed %d --width %d --height %d' % ('<lora:MOSSwSh4rpD3tails:0.5> ' if lora else '', t, sd, w, h))
        open(od + 'Guyanonymous_Wildcards_showcase_updated_%s.txt' % name, 'w', encoding='utf8').write('\n'.join(out))
    open(od + 'Guyanonymous_Wildcards_showcase_updated_key.tsv', 'w').write('line\tkey\tkind\tsex\tseed\tchars\tcheck\n' + '\n'.join(
        '%d\t%s\t%s\t%s\t%d\t%d\t%s' % (i + 1, k, kd, sx, sd, len(t), ('TOKEN ' if ('__' in t or '@@' in t) else '') + ('SPACING' if '  ' in t else '') or 'ok') for i, (k, sx, kd, t, sd, lo) in enumerate(rows)))
    print(len(rows), 'prompts')
rows.sort(key=lambda x: x[0].startswith('pose_'))
if __name__ == '__main__': write('/mnt/user-data/outputs/bodyshow2/')
