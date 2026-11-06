"""v106 - solo masturbation pools: L3 uses real bottoms with the person topless/shirtless (no towels, sheets, throws or held pillows as cover-ups);
L1/L2 women no longer have a hand flat on the stomach (reads as pregnancy); the hand goes to the thigh or hip instead."""
import re, v105_solo as S
BF = ['faded jeans', 'soft grey leggings', 'cotton pyjama bottoms', 'denim shorts', 'a long cotton skirt', 'a satin skirt']
BM = ['grey joggers', 'pyjama trousers', 'faded jeans', 'cotton shorts', 'board shorts', 'linen trousers']
L3F = ["lies topless on her back on a bed in {G}, her right hand pressed over the front of the fabric and moving slowly, her left hand on her own breast, her eyes closed.",
 "sits topless in an armchair in {G}, her right hand pressed between her thighs over the fabric and her left hand gripping the armrest, her head tipped back and her mouth open.",
 "lies topless on her side on a sofa in {G}, her right hand slid inside the waistband so that the fabric moves over her wrist, her left arm under her head and her eyes closed.",
 "sits topless on the edge of a bath in {G}, her right hand pressed over the front of the fabric and her left hand on the bath rim, her head back.",
 "lies topless on a rug on her back in {G} with her knees bent, her right hand moving over the fabric between her thighs and her left arm above her head, her face flushed.",
 "kneels topless on a bed in {G}, her right hand pressed between her thighs over the fabric and her left hand on the headboard, her eyes shut.",
 "leans back against a kitchen counter topless in {G}, her right hand pressed over the front of the fabric and her left hand gripping the counter edge, her eyes closed.",
 "lies topless on her stomach on a bed in {G}, her right hand beneath her hips pressed against the fabric, her cheek on her left forearm, her eyes closed.",
 "sits topless on the floor against a sofa in {G} with her knees up, her right hand pressed between her thighs over the fabric, her left arm across her chest, her head tipped back.",
 "stands topless in a bedroom in {G} with her back against the wall, her right hand pressed over the front of the fabric and her left hand flat on the wall beside her head."]
L3M = ["lies shirtless on his back on a bed in {G}, his right hand pressed over the front of the fabric and moving slowly, his left hand behind his head, his eyes closed.",
 "sits shirtless in an armchair in {G}, his right hand pressed over the front of the fabric and his left hand gripping the armrest, his head tipped back and his mouth open.",
 "lies shirtless on his side on a sofa in {G}, his right hand slid inside the waistband so that the fabric moves over his wrist, his left arm under his head and his eyes closed.",
 "sits shirtless on the edge of a bath in {G}, his right hand pressed over the front of the fabric and his left hand on the bath rim, his head back.",
 "lies shirtless on a rug on his back in {G} with his knees bent, his right hand moving over the fabric at his groin and his left arm above his head, his face flushed.",
 "kneels shirtless on a bed in {G}, his right hand pressed over the front of the fabric and his left hand on the headboard, his eyes shut.",
 "leans back against a kitchen counter shirtless in {G}, his right hand pressed over the front of the fabric and his left hand gripping the counter edge, his eyes closed.",
 "lies shirtless on his stomach on a bed in {G}, his right hand beneath his hips pressed against the fabric, his cheek on his left forearm, his eyes closed.",
 "sits shirtless on the floor against a sofa in {G} with his knees up, his right hand pressed over the front of the fabric, his left arm across his chest, his head tipped back.",
 "stands shirtless in a bedroom in {G} with his back against the wall, his right hand pressed over the front of the fabric and his left hand flat on the wall beside his head."]
S.G[(3, 'f')] = (BF, L3F); S.G[(3, 'm')] = (BM, L3M)
def _fix(k, sx):
    gs, sk = S.G[(k, sx)]
    sk = [re.sub(r'her right hand (?:flat )?(?:low )?on her (?:stomach|belly)', 'her right hand resting against her inner thigh over her clothes', x) for x in sk]
    S.G[(k, sx)] = (gs, sk)
for k in (1, 2): _fix(k, 'f')
COVER = re.compile(r'towel|sheet|duvet|throw|blanket|robe lying|sarong|scarf|lying open over|spread over|draped|pillow (?:held|between|against)', re.I)
STOM = re.compile(r'her right hand (?:resting |pressed |flat )*(?:low )?(?:on|against) her (?:stomach|belly)(?: just above her hip)?')
def build(final):
    out = S.build(final)
    for name, v in out.items():
        if not isinstance(v, list): continue
        if name.startswith('adult_l3_masturbation_'): out[name] = [x for x in v if not COVER.search(x)]
        elif name in ('adult_l1_masturbation_f', 'adult_l2_masturbation_f'):
            out[name] = list(dict.fromkeys(STOM.sub('her right hand resting on her hip', x) for x in v))
    return out
