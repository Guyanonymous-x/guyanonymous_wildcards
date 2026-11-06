"""v106 (from v105) - bulge phrase tied to garment class (tight, brief, jock, medium, loose); detailed pair-posture geometry with torsos turned toward each other; hands placed and kept off the groin; two-person panels state both are men or both women. v105 - structured grid-panel scenes per adult level and cast (woman+man, two women, two men).
Each panel introduces every person once, places every hand, arm and leg by side, states clothing/nudity and what is in view."""
import random
R = random.Random(10500)
PF = 'a woman __apose_person_f__,'
PM = 'a man __apose_person_m__,'
PF2 = 'a second woman __apose_person_f__,'
PM2 = 'a second man __apose_person_m__,'
CLW = ['a fitted knee-length dress', 'a loose blouse and a long skirt', 'a soft sweater and jeans', 'a wrap dress', 'a leather jacket and black jeans', 'a flowered sundress', 'a pleated skirt and a cardigan', 'a white linen jumpsuit', 'a red raincoat and tights', 'a striped shirt and a denim skirt', 'a knitted tunic and wide trousers', 'a satin blouse and tailored shorts']
CLM = ['a button-up shirt and trousers', 'a t-shirt and jeans', 'a jumper and chinos', 'a linen shirt and shorts', 'a hoodie and joggers', 'a denim jacket and jeans', 'a checked flannel shirt and corduroys', 'a polo shirt and shorts', 'a suit jacket over a t-shirt and dark trousers', 'a football shirt and tracksuit bottoms', 'a cable-knit jumper and trousers', 'a leather jacket and black jeans']
UNW = ['a lace bra and matching briefs', 'a silk slip', 'a camisole and lace shorts', 'a satin bra and high-cut briefs', 'a sports bra and cotton briefs', 'a mesh bodysuit', 'a cotton vest and high-waisted briefs', 'a balconette bra and a thong', 'a ribbed bralette and briefs']
UNM = ['tight cotton briefs', 'boxer shorts', 'fitted boxer briefs', 'a low-cut brief', 'a jockstrap', 'silk boxer shorts', 'long cotton boxers', 'thin swim trunks', 'white compression tights', 'black running tights']
TIGHTG = {'fitted cycling shorts', 'white compression tights', 'white compression tights with a built-in support sleeve at the front', 'black running tights', 'black running tights with a built-in support sleeve at the front', 'grey compression tights'}
BRIEFG = {'tight cotton briefs', 'fitted boxer briefs', 'a low-cut brief', 'thin swim trunks'}
JOCKG = {'a jockstrap'}
MEDG = {'faded jeans', 'dark suit trousers', 'chinos', 'swim trunks', 'linen trousers'}
def cls(g): return 'tight' if g in TIGHTG else 'brief' if g in BRIEFG else 'jock' if g in JOCKG else 'medium' if g in MEDG else 'loose'
def pairm(lst):
    g = R.choice(lst); return g, '__male_bulge_%s__' % cls(g)
LASTC = ['loose']
BOTF = ['low-rise jeans','a knee-length cotton skirt','pyjama bottoms','high-waisted linen trousers','a denim miniskirt','soft grey leggings','a satin skirt','cotton shorts','a long floral skirt']
BOTM = ['faded jeans','dark suit trousers','board shorts','pyjama trousers','grey joggers','chinos','swim trunks','linen trousers','cotton shorts','white compression tights with a built-in support sleeve at the front','black running tights with a built-in support sleeve at the front','fitted cycling shorts']
COVER = ['a white bath towel wrapped once around the hips and tucked in at the waist, hanging straight down to the upper thighs', 'a patterned cotton sarong tied at one hip, hanging straight down to mid-thigh', 'a white bedsheet wrapped around the hips toga-style and tucked at the waist, falling to mid-thigh', 'a denim jacket tied around the waist by its sleeves, the body of the jacket hanging down over the groin', 'a short satin robe pulled down to the waist and tied with its belt, hanging to the upper thighs', 'a chunky knitted throw wrapped around the hips and tucked at the side, falling to the knees', 'a long linen shirt tied around the waist by its sleeves, the shirt hanging down over the groin', 'a dark wool scarf-blanket wrapped around the hips and tucked at the waist, falling to mid-thigh']
def lvl_state(L, sex, k):
    """returns (attire sentence about 'she'/'he'). """
    if L == 1: return {'f': 'She wears ' + R.choice(CLW) + '.', 'm': 'He wears ' + R.choice(CLM) + '.'}[sex]
    if L == 2:
        if sex == 'f': return 'She wears ' + R.choice(UNW) + '.'
        g, t = pairm(UNM); LASTC[0] = t; return 'He wears ' + g + '.'
    if L == 3: return ''
    return {'f': 'She is nude.', 'm': 'He is nude.'}[sex]
# posture skeletons for woman+man: (text with {W},{M} intros, camera)
WM = [
 ("{W} and {M} stand facing each other a hand's width apart with their feet flat on the floor and their torsos turned toward each other. His right hand is on her waist and his left hand is on the back of her neck, her hands rest flat on his chest, and her head is tilted up toward him. His hips are square to hers.", 'The camera sees them in three-quarter view from one side, showing both bodies from head to knees.'),
 ("{W} and {M} sit side by side on a sofa with their hips touching, both facing the camera, his knees apart and her knees together and angled toward him. His right arm lies along the back of the sofa behind her shoulders, his left hand rests on his own thigh, her left hand rests on his thigh and her head leans against his shoulder.", 'The shot shows both bodies from head to knees.'),
 ("{W} and {M} lie on their sides on a bed facing each other with their chests a hand apart, each with a head on a pillow. His top arm lies over her waist, his bottom arm is under her neck, her top leg is draped over his hip and her left hand is on his cheek.", 'The shot is from the side, at mattress height, showing both bodies full length.'),
 ("{W} and {M} kneel upright on a bed facing each other with their knees touching and their torsos turned toward each other. His hands rest on her hips, her arms are around his neck and her forehead is against his.", 'The camera sees them in three-quarter view from one side, showing both bodies from head to knees.'),
 ("{M} stands directly behind {W} with his chest against her back and both feet flat on the floor, standing a little to one side of her so that the front of his hips is visible beside hers. His forearms are crossed over her waist, his chin rests on her right shoulder, and her hands rest over his forearms while she looks toward the camera.", 'The shot shows both bodies from head to knees.'),
 ("{M} sits upright on a sofa with his feet flat on the floor and his knees apart, and {W} sits on his thighs facing him with her knees on the cushion either side of his hips. Her arms are around his neck, his hands rest on the small of her back, and their torsos are turned toward each other.", 'The shot is from the side, showing both bodies full length.'),
 ("{M} lies flat on his back on a bed with his head on a pillow and his legs straight, and {W} lies fully on top of him, her chest against his chest, her stomach against his stomach and her hips on his hips, her legs straight and outside his legs. Her cheek rests against his collarbone and her forearms rest on the bed either side of his shoulders.", 'The shot is from the side, at mattress height, showing both bodies full length.'),
 ("{W} stands bent forward at the hips at a table with her forearms flat on it, her back slightly arched and her feet apart. {M} stands directly behind her with his chest upright and both hands on her hips, turned a little so that the front of his hips shows beside hers.", 'The shot is from the side showing both bodies.')]
EXPR = ['She is smiling and he is looking at her.', 'Her eyes are closed and he is kissing her cheek.', 'They are looking at each other and laughing.', 'Her mouth is slightly open and his eyes are closed.']
HV = ' His hands stay clear of his groin.'
def wm_exposed(L, i):
    if L == 1: return ''
    if L == 2: return ' The fabric over his groin shows ' + LASTC[0] + '.' + HV
    if L == 3:
        g, t = pairm(BOTM); return ' Her breasts and his chest are bare. She wears ' + R.choice(BOTF) + ' and he wears ' + g + '. The fabric over his groin shows ' + t + '.' + HV
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
 ("{W} and {W2} sit back to back on a rug with their shoulders touching and their legs crossed. The first woman's right hand rests on her own knee and her head is tilted toward the second woman. The second woman's left hand rests on the floor and her head is tilted toward the first woman.", 'The shot shows both bodies from head to knees.'),
 ("{W} and {W2} lie on their sides on a rug facing each other with their chests a hand apart. The first woman's right hand rests on the second woman's waist, the second woman's left hand rests on the first woman's cheek, and their legs are loosely tangled.", 'The shot shows both bodies from above.'),
 ("{W} and {W2} stand facing each other a hand's width apart with their torsos turned toward each other. The first woman's hands rest on the second woman's hips and the second woman's arms are around the first woman's neck, with their foreheads touching.", 'The camera sees them in three-quarter view from one side, showing both bodies from head to knees.'),
 ("{W} sits on a sofa and {W2} sits beside her with their hips touching, both facing the camera. The first woman's left arm lies along the back of the sofa behind the second woman's shoulders, the second woman's right hand rests on the first woman's thigh, and their heads are tilted toward each other.", 'The shot shows both bodies from head to knees.'),
 ("{W} and {W2} kneel upright on a bed facing each other with their knees touching and their torsos turned toward each other. The first woman's hands are in the second woman's hair and the second woman's hands rest on the first woman's waist as they kiss.", 'The camera sees them in three-quarter view from one side, showing both bodies from head to knees.'),
 ("{W} stands directly behind {W2} with her chest against the second woman's back. The first woman's forearms are crossed over the second woman's waist and her chin rests on the second woman's right shoulder, while the second woman's hands rest over the first woman's forearms and both look toward the camera.", 'The shot shows both bodies from head to knees.')]
def ww_att(L):
    B = ' Both people in this panel are women.'
    if L == 1: return B + ' The first woman wears ' + R.choice(CLW) + ' and the second woman wears ' + R.choice(CLW) + '.'
    if L == 2: return B + ' The first woman wears ' + R.choice(UNW) + ' and the second woman wears ' + R.choice(UNW) + '.'
    if L == 3: return B + ' Both women are topless. The first woman wears ' + R.choice(BOTF) + ' and the second woman wears ' + R.choice(BOTF) + '.'
    return B + ' Both women are nude, with both their breasts and their vulvas in view.'
ACTS_WW = [
 "{W} lies on her back on a bed with her thighs apart and her hands in the hair of {W2}. The second woman lies on her stomach between the first woman's thighs with her face at the first woman's vulva and her hands holding the first woman's thighs. The second woman's tongue is on the first woman's vulva.",
 "{W} and {W2} lie on their sides on a bed in opposite directions, each with her face between the other's thighs. Each woman's hands hold the other woman's hips, and each woman's tongue is on the other woman's vulva.",
 "{W} lies on her back on a bed with her knees apart, and {W2} lies beside her on her left side. The second woman's right hand is between the first woman's thighs with the index and middle fingers inside the first woman's vagina, and the first woman's head is back with her mouth open.",
 "{W} and {W2} sit facing each other on a bed with their legs interlocked, their vulvas pressed together. Each woman's hands rest on the other woman's knees and each woman's head is tipped back."]
# two men
MM = [
 ("{M} and {M2} stand side by side with their shoulders touching, both facing the camera. The first man's right arm is around the second man's shoulders and the second man's left hand rests on the first man's waist, and the other arm of each man hangs relaxed at his side.", 'The shot shows both bodies from head to knees.'),
 ("{M} and {M2} sit close together on a couch with their thighs touching and their knees apart, both facing the camera. The first man's left arm lies along the back of the couch behind the second man's shoulders, the second man's right hand rests on the first man's knee, and the first man's right hand and the second man's left hand rest on their own knees.", 'The shot shows both bodies from head to knees.'),
 ("{M} and {M2} lie on their sides on a bed facing each other with their chests a hand apart, each with a head on a pillow. The first man's top arm lies over the second man's waist, his bottom arm is under the second man's neck, and the second man's top leg is draped over the first man's hip.", 'The shot is from the side, at mattress height, showing both bodies full length.'),
 ("{M} and {M2} stand facing each other close together with their torsos turned toward each other. The first man's hands rest on the second man's hips and the second man's arms are around the first man's neck as they kiss, their hips a hand's width apart.", 'The camera sees them in three-quarter view from one side, showing both bodies from head to knees.'),
 ("{M} stands directly behind {M2} with his chest against the second man's back, standing a little to one side so that the front of the second man's hips is visible. The first man's forearms are crossed over the second man's waist and his chin rests on the second man's right shoulder, while the second man's hands rest over the first man's forearms and both look toward the camera.", 'The shot shows both bodies from head to knees.'),
 ("{M} lies flat on his back on a bed with his head on a pillow and his legs straight, and {M2} lies fully on top of him, his chest against the first man's chest, his hips over the first man's hips and his legs outside the first man's legs, his weight held on his forearms either side of the first man's head. The first man's hands rest on the second man's back.", 'The shot is from the side, at mattress height, showing both bodies full length.')]
def mm_att(L):
    B = ' Both people in this panel are men.'
    if L == 1: return B + ' The first man wears ' + R.choice(CLM) + ' and the second man wears ' + R.choice(CLM) + '.'
    if L == 2:
        g1, t1 = pairm(UNM); g2, t2 = pairm([x for x in UNM if x != g1]); return B + ' The first man wears ' + g1 + ' and the second man wears ' + g2 + '. The fabric over the first man\'s groin shows ' + t1 + ', and the fabric over the second man\'s groin shows ' + t2 + '. Neither man\'s hands are near his own groin.'
    if L == 3:
        g1, t1 = pairm(BOTM); g2, t2 = pairm([x for x in BOTM if x != g1]); return B + ' Both men are shirtless. The first man wears ' + g1 + ' and the second man wears ' + g2 + '. The fabric over the first man\'s groin shows ' + t1 + ', and the fabric over the second man\'s groin shows ' + t2 + '. Neither man\'s hands are near his own groin.'
    return B + ' Both men are nude, with both their chests and their penises and scrotums in view, the penises hanging soft.'
ACTS_MM = [
 "{M} sits on the edge of a bed with his knees apart, and {M2} kneels on the floor between his knees. The second man's right hand is around the base of the first man's erect penis and the first man's penis is in the second man's mouth, while the first man's hands rest in the second man's hair.",
 "{M} and {M2} sit facing each other on a bed with their legs apart. The first man's right hand is around the second man's erect penis and the second man's right hand is around the first man's erect penis, both stroking, and their foreheads are touching.",
 "{M} kneels on all fours on a bed with his back arched, and {M2} kneels behind him holding his hips with both hands. The second man's erect penis is inside the first man's anus, and the first man is looking back over his shoulder."]
def exp(): return R.choice(EXPR)
def build(final):
    G = {}; ep = []
    for L in range(1, 7):
        wm = []; ww = []; mm = []
        if L <= 4:
            for i, (t, cam) in enumerate(WM):
                for k in range(2):
                    s = t.format(W=PF, M=PM) + ' ' + lvl_state(L, 'f', k) + ' ' + lvl_state(L, 'm', k) + wm_exposed(L, i) + ' ' + exp() + ' The scene is in __apose_place__. The light is __apose_light__. ' + cam
                    s = s.replace('She is nude. He is nude.', 'Both are nude.') if L >= 4 else s
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
            v = list(dict.fromkeys(' '.join(x.split()) for x in v)); G['adult_l%d_panel_%s' % (L, nm)] = v; ep.append('adult_l%d_panel_%s' % (L, nm))
    import v106_bulge
    for k, v in v106_bulge.build('').items(): G[k] = v; ep.append(k)
    G['v105_panels_entry_points'] = ep
    return G
