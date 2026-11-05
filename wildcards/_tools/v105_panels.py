"""v105 - structured grid-panel scenes per adult level and cast (woman+man, two women, two men).
Each panel introduces every person once, places every hand, arm and leg by side, states clothing/nudity and what is in view."""
import random
R = random.Random(10500)
PF = 'a woman __apose_person_f__,'
PM = 'a man __apose_person_m__,'
PF2 = 'a second woman __apose_person_f__,'
PM2 = 'a second man __apose_person_m__,'
CLW = ['a fitted knee-length dress', 'a loose blouse and a long skirt', 'a soft sweater and jeans', 'a wrap dress']
CLM = ['a button-up shirt and trousers', 'a t-shirt and jeans', 'a jumper and chinos', 'a linen shirt and shorts']
UNW = ['a lace bra and matching briefs', 'a silk slip', 'a camisole and lace shorts', 'a satin bra and high-cut briefs']
UNM = ['tight cotton briefs', 'boxer shorts', 'fitted boxer briefs', 'a low-cut brief']
COVER = ['a white bath towel wrapped once around the hips and tucked in at the waist, hanging straight down to the upper thighs', 'a patterned cotton sarong tied at one hip, hanging straight down to mid-thigh', 'a white bedsheet wrapped around the hips toga-style and tucked at the waist, falling to mid-thigh', 'a denim jacket tied around the waist by its sleeves, the body of the jacket hanging down over the groin', 'a short satin robe pulled down to the waist and tied with its belt, hanging to the upper thighs', 'a chunky knitted throw wrapped around the hips and tucked at the side, falling to the knees', 'a long linen shirt tied around the waist by its sleeves, the shirt hanging down over the groin', 'a dark wool scarf-blanket wrapped around the hips and tucked at the waist, falling to mid-thigh']
def lvl_state(L, sex, k):
    """returns (attire sentence about 'she'/'he'). """
    if L == 1: return {'f': 'She wears ' + R.choice(CLW) + '.', 'm': 'He wears ' + R.choice(CLM) + '.'}[sex]
    if L == 2: return {'f': 'She wears ' + R.choice(UNW) + '.', 'm': 'He wears ' + R.choice(UNM) + '.'}[sex]
    return {'f': 'She is nude.', 'm': 'He is nude.'}[sex]
# posture skeletons for woman+man: (text with {W},{M} intros, camera)
WM = [
 ("{W} and {M} stand facing each other close together. His right hand is on her waist and his left hand is on the back of her neck, and her hands rest flat on his chest while her head is tilted up toward him.", 'The shot shows both bodies from head to knees.'),
 ("{W} and {M} sit side by side on a sofa. His right arm is around her shoulders and his left hand rests on her knee, and her left hand rests on his thigh while her head leans against his shoulder.", 'The shot shows both bodies from head to knees.'),
 ("{W} and {M} lie on their sides on a bed facing each other. His top arm lies over her waist, her top leg is draped over his hip, and her left hand is on his cheek.", 'The shot shows both bodies from the side.'),
 ("{W} and {M} kneel on a bed facing each other with their knees touching. His hands rest on her hips, and her arms are around his neck with her forehead against his.", 'The shot shows both bodies from head to knees.'),
 ("{M} stands behind {W}. His arms wrap around her waist, his chin rests on her shoulder, and her hands rest over his forearms while she looks toward the camera.", 'The shot shows both bodies from head to knees.'),
 ("{W} sits on the lap of {M} facing him. Her knees are on either side of his hips, her arms are around his neck, and his hands rest on the small of her back.", 'The shot shows both bodies from the side.'),
 ("{M} lies on his back on a bed, and {W} lies on top of him chest to chest, her chin resting on her folded hands on his chest and her legs stretched out between his.", 'The shot shows both bodies from the side.'),
 ("{W} leans forward over a table with her forearms on it and her back slightly arched. {M} stands behind her with both hands on her hips.", 'The shot shows both bodies from the side.')]
EXPR = ['She is smiling and he is looking at her.', 'Her eyes are closed and he is kissing her cheek.', 'They are looking at each other and laughing.', 'Her mouth is slightly open and his eyes are closed.']
def wm_exposed(L, i):
    if L == 1: return ''
    if L == 2: return ' The fabric over his groin shows __male_bulge_clothed__.'
    if L == 3: return ' Their pelvises are hidden by ' + R.choice(COVER) + '; her breasts and his chest are bare. The wrap over his groin shows __male_bulge_covered__.'
    return ' Her breasts and her vulva are in view, and his penis hangs soft over his scrotum and is in view.'
ACTS_WM = [
 ("{W} lies on her back on a bed with her knees bent and her legs wrapped around the waist of {M}, her hands gripping his upper arms. He kneels between her thighs, leaning over her with his hands on the mattress beside her shoulders. His erect penis is inside her vagina, and the join between his pelvis and hers is in view.", 'The shot is from the foot of the bed showing both bodies.', ('belly', 1)),
 ("{M} lies on his back on a bed, and {W} sits astride his hips facing him. Her knees are on either side of his waist, her hands rest on his chest, and his hands hold her hips. His erect penis is inside her vagina, and the join between their pelvises is in view.", 'The shot is from the side showing both bodies.', ('belly', 0)),
 ("{W} kneels on all fours on a bed with her arms straight and her back arched, and {M} kneels behind her holding her hips with both hands. His erect penis is inside her vagina from behind, and she is looking back over her shoulder at him.", 'The shot is from behind and slightly to the side showing both bodies.', ('back', 1)),
 ("{W} and {M} lie on their sides on a bed, her back against his chest. His top arm is around her waist and her top leg is raised and bent. His erect penis is inside her vagina from behind, and his face is against her neck.", 'The shot is from the front showing both bodies.', ('belly', 0)),
 ("{W} lies on her back on a bed with her thighs apart and her hands in the hair of {M}. He lies on his stomach between her thighs with his face at her vulva and his hands holding her thighs. His tongue is on her vulva.", 'The shot is from the foot of the bed showing both bodies.', None),
 ("{M} sits on the edge of a bed with his knees apart and his hands in the hair of {W}. She kneels on the floor between his knees, her right hand around the base of his erect penis, and his penis is in her mouth.", 'The shot is from the side showing both bodies.', ('face', 0))]
FIN_WM = {'belly': ['He has pulled out, and semen leaves the tip of his penis __semen_amount__, and it lands across her stomach; it is __semen_look__. __semen_after__'],
          'back': ['He has pulled out, and semen leaves the tip of his penis __semen_amount__, and it lands across her buttocks and lower back; it is __semen_look__. __semen_after__'],
          'face': ['Semen leaves the tip of his penis __semen_amount__, and it lands on her lips, cheek and chin; it is __semen_look__. __semen_after__']}
FIN_SQ = ['Thin, clear, watery fluid comes out of her vaginal opening __squirt_form__ onto the sheet beneath her. The fluid is transparent, not white, and it falls downward.']
# two women
WW = [
 ("{W} and {W2} sit back to back on a rug with their shoulders touching. The first woman's right hand rests on her own knee and her head is tilted toward the second woman. The second woman's left hand rests on the floor and her head is tilted toward the first woman.", 'The shot shows both bodies from head to knees.'),
 ("{W} and {W2} lie on their sides on a rug facing each other. The first woman's right hand rests on the second woman's waist, the second woman's left hand rests on the first woman's cheek, and their legs are loosely tangled.", 'The shot shows both bodies from above.'),
 ("{W} and {W2} stand facing each other close together. The first woman's hands rest on the second woman's hips and the second woman's arms are around the first woman's neck, with their foreheads touching.", 'The shot shows both bodies from head to knees.'),
 ("{W} sits on a sofa and {W2} sits beside her. The first woman's left arm is around the second woman's shoulders, the second woman's right hand rests on the first woman's thigh, and they look at each other.", 'The shot shows both bodies from head to knees.'),
 ("{W} kneels on a bed facing {W2}, who also kneels. Their knees touch, the first woman's hands are in the second woman's hair, and the second woman's hands rest on the first woman's waist as they kiss.", 'The shot shows both bodies from the side.'),
 ("{W} stands behind {W2}. The first woman's arms wrap around the second woman's waist and her chin rests on the second woman's shoulder, while the second woman's hands rest over the first woman's forearms.", 'The shot shows both bodies from head to knees.')]
def ww_att(L):
    if L == 1: return ' The first woman wears ' + R.choice(CLW) + ' and the second woman wears ' + R.choice(CLW) + '.'
    if L == 2: return ' The first woman wears ' + R.choice(UNW) + ' and the second woman wears ' + R.choice(UNW) + '.'
    if L == 3: return ' Both women are nude with their breasts bare and their pelvises hidden by ' + R.choice(COVER) + '.'
    return ' Both women are nude, with both their breasts and their vulvas in view.'
ACTS_WW = [
 "{W} lies on her back on a bed with her thighs apart and her hands in the hair of {W2}. The second woman lies on her stomach between the first woman's thighs with her face at the first woman's vulva and her hands holding the first woman's thighs. The second woman's tongue is on the first woman's vulva.",
 "{W} and {W2} lie on their sides on a bed in opposite directions, each with her face between the other's thighs. Each woman's hands hold the other woman's hips, and each woman's tongue is on the other woman's vulva.",
 "{W} lies on her back on a bed with her knees apart, and {W2} lies beside her on her left side. The second woman's right hand is between the first woman's thighs with the index and middle fingers inside the first woman's vagina, and the first woman's head is back with her mouth open.",
 "{W} and {W2} sit facing each other on a bed with their legs interlocked, their vulvas pressed together. Each woman's hands rest on the other woman's knees and each woman's head is tipped back."]
# two men
MM = [
 ("{M} and {M2} stand side by side. The first man's right arm is around the second man's shoulders and the second man's left hand rests on the first man's waist, and they look toward the camera.", 'The shot shows both bodies from head to knees.'),
 ("{M} and {M2} sit close together on a couch. The first man's left arm lies along the back of the couch behind the second man's shoulders, and the second man's right hand rests on the first man's knee.", 'The shot shows both bodies from head to knees.'),
 ("{M} and {M2} lie on their sides on a bed facing each other. The first man's top arm lies over the second man's waist, and the second man's top leg is draped over the first man's hip.", 'The shot shows both bodies from the side.'),
 ("{M} and {M2} stand facing each other close together. The first man's hands rest on the second man's hips and the second man's arms are around the first man's neck as they kiss.", 'The shot shows both bodies from head to knees.'),
 ("{M} stands behind {M2}. The first man's arms wrap around the second man's waist and his chin rests on the second man's shoulder, while the second man's hands rest over the first man's forearms.", 'The shot shows both bodies from head to knees.'),
 ("{M} lies on his back on a bed and {M2} lies on top of him chest to chest. The second man's forearms rest on the bed beside the first man's head and the first man's hands rest on the second man's back.", 'The shot shows both bodies from the side.')]
def mm_att(L):
    if L == 1: return ' The first man wears ' + R.choice(CLM) + ' and the second man wears ' + R.choice(CLM) + '.'
    if L == 2: return ' The first man wears ' + R.choice(UNM) + ' and the second man wears ' + R.choice(UNM) + '. The fabric over the first man\'s groin shows __male_bulge_clothed__, and the fabric over the second man\'s groin shows __male_bulge_clothed__.'
    if L == 3: return ' Both men are nude with their chests bare and their pelvises hidden by ' + R.choice(COVER) + '. The wrap over the first man\'s groin shows __male_bulge_covered__, and the wrap over the second man\'s groin shows __male_bulge_covered__.'
    return ' Both men are nude, with both their chests and their penises and scrotums in view, the penises hanging soft.'
ACTS_MM = [
 "{M} sits on the edge of a bed with his knees apart, and {M2} kneels on the floor between his knees. The second man's right hand is around the base of the first man's erect penis and the first man's penis is in the second man's mouth, while the first man's hands rest in the second man's hair.",
 "{M} and {M2} sit facing each other on a bed with their legs apart. The first man's right hand is around the second man's erect penis and the second man's right hand is around the first man's erect penis, both stroking, and their foreheads are touching.",
 "{M} kneels on all fours on a bed with his back arched, and {M2} kneels behind him holding his hips with both hands. The second man's erect penis is inside the first man's anus, and the first man is looking back over his shoulder."]
BU = ['a raised, rounded shape under the fabric where his semi-erect penis pushes the cloth outward, the fabric unbroken and fully wraping him, stretched smooth and clinging over the shape and creasing softly around it, angled toward his left hip', 'a long raised ridge under the fabric where his erect penis pushes the cloth upward toward his navel, the fabric unbroken and fully wraping him, clinging closely to the ridge and defining its length, with a slightly rounder swell at the top', 'a soft rounded swelling under the fabric where his semi-erect penis lies along his right thigh, the fabric unbroken and fully wraping him, draped and clinging over it, with small folds running toward it', 'a firm raised ridge under the fabric angled up toward his right hip where his erect penis pushes the cloth outward, the fabric unbroken and fully wraping him, pulled snug over a rounder swell near the waistband', 'a thick raised ridge running diagonally up from his groin under the fabric, the cloth unbroken and fully wraping him, hugging the shape closely and shaded by the folds around it, with his testicles making a softer rounded swelling beneath', 'a gentle rounded rise under the fabric that lifts the cloth slightly away from his body, the fabric unbroken and fully wraping him and clinging over the shape', 'a long raised ridge under the fabric angled upward and to the left, the cloth unbroken and fully wraping him, pulled taut over the shape with fine tension creases radiating from it, a rounded swell near the top', 'a soft heavy swelling under the fabric hanging toward his left thigh, the cloth unbroken and fully wraping him and draped closely over it, with a rounder shape beneath for his testicles']
BC = ['a tall raised peak in the wrap where his erect penis pushes the cloth upward, the wrap unbroken and fully wraping him, pulled tight and clinging over the peak with creases running down from it', 'a gentle raised ridge in the wrap where his semi-erect penis lifts it slightly away from his groin, the wrap unbroken and fully wraping him, draped smoothly over the shape', 'a raised ridge in the wrap angled toward his left hip where his erect penis pushes it up, the wrap unbroken and fully wraping him, clinging over the shape with soft folds around it', 'a soft rounded rise in the wrap angled toward his right thigh where his half-hard penis presses against it, the wrap unbroken and fully wraping him and draped over the shape']
def exp(): return R.choice(EXPR)
def build(final):
    G = {}; ep = []
    for L in range(1, 7):
        wm = []; ww = []; mm = []
        if L <= 4:
            for i, (t, cam) in enumerate(WM):
                for k in range(2):
                    s = t.format(W=PF, M=PM) + ' ' + lvl_state(L, 'f', k) + ' ' + lvl_state(L, 'm', k) + wm_exposed(L, i) + ' ' + exp() + ' The scene is in __apose_place__. The light is __apose_light__. ' + cam
                    s = s.replace('She is nude. He is nude.', 'Both are nude.') if L >= 3 else s
                    wm.append(s)
            for i, (t, cam) in enumerate(WW):
                for k in range(2): ww.append(t.format(W=PF, W2=PF2) + ww_att(L) + ' The scene is in __apose_place__. The light is __apose_light__. ' + cam)
            for i, (t, cam) in enumerate(MM):
                for k in range(2): mm.append(t.format(M=PM, M2=PM2) + mm_att(L) + ' The scene is in __apose_place__. The light is __apose_light__. ' + cam)
        else:
            for t, cam, fin in ACTS_WM:
                base = t.format(W=PF, M=PM) + ' Both are nude.'
                wm.append(base + ' The scene is in __apose_place__. The light is __apose_light__. ' + cam)
                if L == 6:
                    if fin: wm[-1] = base + ' ' + R.choice(FIN_WM[fin[0]]) + ' The scene is in __apose_place__. The light is __apose_light__. ' + cam
                    elif 'tongue is on her vulva' in t: wm[-1] = base + ' ' + FIN_SQ[0] + ' The scene is in __apose_place__. The light is __apose_light__. ' + cam
                    wm.append(wm[-1].replace('__apose_place__', '__apose_place__'))
            for t in ACTS_WW:
                base = t.format(W=PF, W2=PF2) + ' Both women are nude.'
                s = base + ' The scene is in __apose_place__. The light is __apose_light__. The shot is from the side showing both bodies.'
                if L == 6 and 'vulva' in t: s = base + ' ' + FIN_SQ[0] + ' The scene is in __apose_place__. The light is __apose_light__. The shot is from the side showing both bodies.'
                ww.append(s)
            for t in ACTS_MM:
                base = t.format(M=PM, M2=PM2) + ' Both men are nude.'
                s = base + ' The scene is in __apose_place__. The light is __apose_light__. The shot is from the side showing both bodies.'
                if L == 6 and 'handjob' not in t and 'right hand is around the second man' in t:
                    s = base + ' Semen leaves the tip of the first man\'s penis __semen_amount__, and it lands on the second man\'s hand and stomach; it is __semen_look__. The scene is in __apose_place__. The light is __apose_light__. The shot is from the side showing both bodies.'
                mm.append(s)
        for nm, v in (('wm', wm), ('ww', ww), ('mm', mm)):
            v = list(dict.fromkeys(v)); G['adult_l%d_panel_%s' % (L, nm)] = v; ep.append('adult_l%d_panel_%s' % (L, nm))
    G['male_bulge_clothed'] = BU; G['male_bulge_covered'] = BC; ep += ['male_bulge_clothed', 'male_bulge_covered']
    G['v105_panels_entry_points'] = ep
    return G
