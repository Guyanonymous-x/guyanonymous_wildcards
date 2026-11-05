"""v105 - full range of sex acts for levels 5 and 6 (by type) and kink/BDSM/fetish panels."""
import random
R = random.Random(10501)
PF = 'a woman __apose_person_f__,'; PM = 'a man __apose_person_m__,'; PF2 = 'a second woman __apose_person_f__,'; PM2 = 'a second man __apose_person_m__,'
TAIL = ' The scene is in __apose_place__. The light is __apose_light__. '
SEMF = {'belly': 'He has pulled out, and semen leaves the tip of his penis __semen_amount__, and it lands across her stomach; it is __semen_look__. __semen_after__',
        'back': 'He has pulled out, and semen leaves the tip of his penis __semen_amount__, and it lands across her lower back and buttocks; it is __semen_look__. __semen_after__',
        'face': 'Semen leaves the tip of his penis __semen_amount__, and it lands on her cheek and lips; it is __semen_look__. __semen_after__',
        'chest': 'He has pulled out, and semen leaves the tip of his penis __semen_amount__, and it lands on her chest; it is __semen_look__. __semen_after__'}
SQ = 'Thin, clear, watery fluid comes out of her vaginal opening __squirt_form__ onto the sheet beneath her. The fluid is transparent, not white, and it falls downward.'
# (text, camera, finish-key or None)
WM_VAG = [
 ("{W} lies on her back on a bed with her knees bent and her legs wrapped around the waist of {M}, her hands gripping his upper arms. He kneels between her thighs, leaning over her with his hands on the mattress beside her shoulders. His erect penis is inside her vagina, and the join between his pelvis and hers is in view.", 'The shot is from the foot of the bed showing both bodies.', 'belly'),
 ("{M} lies on his back on a bed, and {W} sits astride his hips facing him with her knees on either side of his waist, her hands on his chest and his hands holding her hips. His erect penis is inside her vagina, and the join between their pelvises is in view.", 'The shot is from the side showing both bodies.', 'chest'),
 ("{M} lies on his back on a bed, and {W} sits astride his hips facing his feet with her hands on his knees and her back to the camera. His erect penis is inside her vagina, and the join between their pelvises is in view.", 'The shot is from behind showing both bodies.', None),
 ("{W} kneels on all fours on a bed with her arms straight and her back arched, and {M} kneels behind her holding her hips with both hands. His erect penis is inside her vagina from behind, and she is looking back over her shoulder at him.", 'The shot is from behind and slightly to the side showing both bodies.', 'back'),
 ("{W} and {M} lie on their sides on a bed, her back against his chest, his top arm around her waist and her top leg raised and bent. His erect penis is inside her vagina from behind, and his face is against her neck.", 'The shot is from the front showing both bodies.', None),
 ("{W} lies on her back at the edge of a bed with her ankles resting on the shoulders of {M}, who stands on the floor holding her thighs. His erect penis is inside her vagina, and her hands grip the sheet.", 'The shot is from the side showing both bodies.', 'belly'),
 ("{M} stands holding {W} up against a wall, her legs wrapped around his waist and her arms around his neck, his hands under her buttocks. His erect penis is inside her vagina.", 'The shot is from the side showing both bodies.', None),
 ("{M} sits in a chair and {W} sits on his lap facing him with her feet on the floor either side of the chair, her arms around his neck and his hands on her waist. His erect penis is inside her vagina.", 'The shot is from the side showing both bodies.', None)]
WM_ORAL = [
 ("{W} lies on her back on a bed with her thighs apart and her hands in the hair of {M}. He lies on his stomach between her thighs with his face at her vulva and his hands holding her thighs, and his tongue is on her vulva.", 'The shot is from the foot of the bed showing both bodies.', 'SQ'),
 ("{M} sits on the edge of a bed with his knees apart and his hands in the hair of {W}. She kneels on the floor between his knees, her right hand around the base of his erect penis, and his penis is in her mouth.", 'The shot is from the side showing both bodies.', 'face'),
 ("{W} and {M} lie on their sides on a bed in opposite directions, her face at his erect penis and his face at her vulva. Her right hand is around the base of his penis, his hands hold her thighs, his tongue is on her vulva and his penis is in her mouth.", 'The shot is from the side showing both bodies.', None),
 ("{M} stands with his back against a wall and {W} kneels in front of him. Her left hand is on his hip and her right hand is around the base of his erect penis, and the head of his penis is in her mouth while she looks up at him.", 'The shot is from the side showing both bodies.', 'face'),
 ("{W} sits on the edge of a table with her legs spread and her hands behind her, and {M} kneels on the floor between her knees with his face at her vulva and his hands on her inner thighs, and his tongue is on her vulva.", 'The shot is from the front showing both bodies.', 'SQ'),
 ("{W} lies on her back with her head hanging over the edge of a bed, and {M} stands at the edge holding her head with both hands. His erect penis is in her mouth and her throat is in a straight line.", 'The shot is from the side showing both bodies.', None)]
WM_ANAL = [
 ("{W} kneels on all fours on a bed with her chest low on the mattress and her buttocks raised, and {M} kneels behind her with his hands on her buttocks, spreading them. His erect penis is inside her anus, and she is looking back over her shoulder.", 'The shot is from behind and slightly to the side showing both bodies.', 'back'),
 ("{W} lies on her back with her knees pulled up toward her chest, and {M} kneels in front of her holding her thighs. His erect penis is inside her anus, and her hands grip the sheet.", 'The shot is from the foot of the bed showing both bodies.', 'belly'),
 ("{M} lies on his back and {W} squats over his hips facing away from him with her hands on his knees. His erect penis is inside her anus, and her back is to the camera.", 'The shot is from behind showing both bodies.', None)]
WW_ORAL = [
 "{W} lies on her back on a bed with her thighs apart and her hands in the hair of {W2}. The second woman lies on her stomach between the first woman's thighs with her face at the first woman's vulva and her hands holding the first woman's thighs, and her tongue is on the first woman's vulva.",
 "{W} and {W2} lie on their sides on a bed in opposite directions, each with her face between the other's thighs, each woman's hands holding the other woman's hips and each woman's tongue on the other woman's vulva.",
 "{W} sits on the edge of a sofa with her legs spread and her hands gripping the cushions, and {W2} kneels on the floor between her knees with her face at the first woman's vulva and her hands on the first woman's inner thighs, her tongue on the first woman's vulva."]
WW_SCISSOR = [
 "{W} and {W2} sit facing each other on a bed with their legs interlocked in a scissoring position, the first woman's right leg over the second woman's left leg, their vulvas pressed together. Each woman's hands rest on the other woman's knees and each woman's head is tipped back.",
 "{W} lies on her back on a bed with her left leg raised and {W2} lies on her side in front of her, scissoring, with her right thigh between the first woman's legs and their vulvas pressed together. The second woman's hand is on the first woman's raised thigh and the first woman's hands grip the sheet.",
 "{W} and {W2} lie on their backs on a bed with their hips together and their legs crossed in a scissor, their vulvas pressed together, and they hold each other's hands above their hips."]
WW_OTHER = [
 "{W} lies on her back on a bed with her knees apart, and {W2} lies beside her on her left side. The second woman's right hand is between the first woman's thighs with the index and middle fingers inside the first woman's vagina, and the first woman's head is back with her mouth open.",
 "{W} lies on her back on a bed with her knees apart, and {W2} kneels between her thighs wearing a black strap-on harness with a silicone dildo. The dildo is inside the first woman's vagina, and the first woman's legs are wrapped around the second woman's waist.",
 "{W} kneels on all fours on a bed, and {W2} kneels behind her wearing a leather strap-on harness with a silicone dildo. The dildo is inside the first woman's vagina and the second woman holds the first woman's hips with both hands.",
 "{W} sits on the face of {W2}, who lies on her back on a bed. The first woman kneels with her thighs on either side of the second woman's head, her hands on the headboard, and the second woman's hands hold the first woman's hips."]
MM_ORAL = [
 "{M} sits on the edge of a bed with his knees apart and his hands in the hair of {M2}. The second man kneels on the floor between his knees with his right hand around the base of the first man's erect penis, and the first man's penis is in the second man's mouth.",
 "{M} and {M2} lie on their sides on a bed in opposite directions, each with his face at the other's erect penis, each man's hands holding the other man's hips and each man's penis in the other man's mouth.",
 "{M} stands with his back against a wall and {M2} kneels in front of him with his left hand on the first man's hip and his right hand around the base of the first man's erect penis, and the head of the first man's penis is in the second man's mouth."]
MM_ANAL = [
 "{M} kneels on all fours on a bed with his back arched, and {M2} kneels behind him holding his hips with both hands. The second man's erect penis is inside the first man's anus, and the first man is looking back over his shoulder.",
 "{M} lies on his back on a bed with his knees pulled up toward his chest, and {M2} kneels in front of him holding the first man's thighs. The second man's erect penis is inside the first man's anus.",
 "{M} and {M2} lie on their sides on a bed, the first man's back against the second man's chest and the second man's arm around the first man's waist. The second man's erect penis is inside the first man's anus."]
MM_HAND = [
 "{M} and {M2} sit facing each other on a bed with their legs apart. The first man's right hand is around the second man's erect penis and the second man's right hand is around the first man's erect penis, both stroking, and their foreheads are touching.",
 "{M} and {M2} lie side by side on a bed, each man stroking his own erect penis with his right hand, and each man's left hand resting on the other man's chest.",
 "{M} and {M2} lie chest to chest on a bed with their erect penises pressed together between their stomachs, the first man's hand wrapped around both."]
FIN_MM = " Semen leaves the tip of the first man's penis __semen_amount__, and it lands on the second man's hand and stomach; it is __semen_look__. __semen_after__"
# ---- kink
K_WM = [
 "{W} kneels on a bed with her wrists tied behind her back with red rope and a rope harness crossing her chest and shoulders. She wears black latex stockings. {M} stands in front of her in black leather trousers with his chest bare, holding the end of the rope in his left hand and lifting her chin with his right hand. She is looking up at him and smiling.",
 "{W} kneels on a rug wearing a black leather collar with a metal ring and a leather harness across her chest, and she holds her hands behind her back. {M} sits in an armchair holding a leather leash in his right hand attached to the ring of her collar. He wears a dark shirt unbuttoned and black trousers.",
 "{M} sits on the edge of a bed and {W} lies face down across his lap with her buttocks raised and her hands on the floor. His right hand is raised above her buttocks, which are red, and his left hand rests on her lower back. She wears black thigh-high stockings and a garter belt.",
 "{W} lies on her back on a bed with her wrists in padded leather cuffs clipped to the headboard and a black silk blindfold over her eyes. {M} kneels between her thighs, naked, holding her hips with both hands. His erect penis is inside her vagina.",
 "{W} stands in a black leather corset, thigh-high boots and long gloves, holding a leather riding crop in her right hand, with her left boot resting on the back of {M}, who kneels on all fours on the floor wearing a leather collar and nothing else. He is looking at the floor.",
 "{M} stands in a metal chastity cage with his wrists cuffed behind his back, naked. {W} stands in front of him in a black latex dress and heels, holding a small key on a chain in her right hand and tracing the cage with her left index finger.",
 "{W} stands wearing a black leather strap-on harness with a silicone dildo, and {M} bends forward over the edge of a bed with his hands gripping the sheet. She holds his hips with both hands, and the dildo is inside his anus.",
 "{W} lies on her back on a bed in a spread-eagle position with her wrists and ankles strapped to the four bedposts with black leather straps and a ball gag in her mouth. {M} kneels between her thighs, naked, with his hands on her thighs. His erect penis is inside her vagina."]
K_WW = [
 "{W} kneels on a bed in a black latex catsuit open at the chest, with a leather collar around her neck, and {W2} stands over her in a leather corset and thigh-high boots, holding a leash attached to the collar in her left hand and a riding crop in her right hand.",
 "{W} lies on her back on a bed with her wrists in leather cuffs clipped to the headboard and a blindfold over her eyes, and {W2} kneels between her thighs wearing a black strap-on harness with a silicone dildo. The dildo is inside the first woman's vagina.",
 "{W} lies on her back with her wrists tied above her head with white rope, wearing only black stockings, and {W2} sits on her face in a latex corset, her thighs either side of the first woman's head and her hands on the headboard.",
 "{W} sits on a chair in a black latex catsuit with her ankles strapped to the chair legs, and {W2} kneels in front of her wearing a leather harness, holding a vibrating wand massager against the first woman's vulva, which is in view.",
 "{W} kneels on a rug wearing a leather harness over her bare chest, and {W2} stands in front of her in glossy thigh-high boots, one boot lifted toward the first woman's mouth, and the first woman is kissing the toe of the boot."]
K_MM = [
 "{M} kneels on a rug wearing a leather chest harness and a leather collar, and {M2} stands over him in black leather trousers holding a leash attached to the collar in his right hand, with his left hand on the first man's head.",
 "{M} lies on his back on a bed with his wrists in leather cuffs clipped to the headboard, naked, and {M2} kneels over his hips wearing a leather harness, holding a black leather paddle in his right hand.",
 "{M} stands with his wrists chained to an overhead bar, naked, and {M2} stands behind him in a leather vest and black leather chaps, with his right hand on the first man's hip and his left hand holding a short leather flogger.",
 "{M} kneels on all fours with a ball gag in his mouth and rope around his thighs, and {M2} stands over him in thigh-high leather boots, with one boot resting on the first man's back.",
 "{M} stands in a metal chastity cage, naked, with his wrists tied behind his back with rope, and {M2} stands in front of him in a latex shirt and leather trousers holding the key on a chain."]
K_F = [
 "{W} sits on a bed wearing a black latex catsuit with her wrists locked in leather cuffs in front of her and a ball gag strapped in her mouth, a vibrating wand massager held against her vulva between her thighs, her head tipped back.",
 "{W} kneels on a rug naked except for a leather collar with a ring and black thigh-high stockings, her wrists tied behind her back with red rope and a rope harness across her chest, her chin raised.",
 "{W} stands in a black leather corset, fishnet stockings and thigh-high boots against a studio wall, holding a leather riding crop in both hands in front of her with a confident look."]
K_M = [
 "{M} kneels on a rug wearing a leather collar with a ring and a leather chest harness, his wrists locked in cuffs behind his back, naked below the waist with his erect penis visible, his head bowed.",
 "{M} stands naked in a metal chastity cage with his wrists chained to an overhead bar and a black leather blindfold over his eyes, his head tilted back.",
 "{M} stands in a black latex shirt, leather chaps with his buttocks and genitals bare, and a leather cap, holding a leather paddle in his right hand against his thigh."]
def mk(lst, **kw):
    out = []
    for t in lst:
        if isinstance(t, tuple):
            text, cam, fin = t
        else: text, cam, fin = t, 'The shot is from the side showing both bodies.', None
        out.append((text.format(**kw), cam, fin))
    return out
def build(final):
    G = {}; ep = []
    def put(name, items):
        G[name] = list(dict.fromkeys(items)); ep.append(name)
    for L in (5, 6):
        def line(text, cam, fin, who='wm'):
            s = text + ' Both are nude.' if who == 'wm' else text
            if L == 6 and fin == 'SQ': s += ' ' + SQ
            elif L == 6 and fin in SEMF: s += ' ' + SEMF[fin]
            return s + TAIL + cam
        for nm, lst in (('wm_vaginal', WM_VAG), ('wm_oral', WM_ORAL), ('wm_anal', WM_ANAL)):
            put('adult_l%d_panel_%s' % (L, nm), [line(t, c, f) for t, c, f in mk(lst, W=PF, M=PM)])
        def ww(t, cam='The shot is from the side showing both bodies.'):
            s = t + ' Both women are nude.'
            if L == 6 and 'vulva' in t and 'strap-on' not in t: s += ' ' + SQ.replace('her vaginal opening',"the first woman's vaginal opening").replace('beneath her','beneath her')
            return s + TAIL + cam
        put('adult_l%d_panel_ww_oral' % L, [ww(t.format(W=PF, W2=PF2)) for t in WW_ORAL])
        put('adult_l%d_panel_ww_scissor' % L, [ww(t.format(W=PF, W2=PF2)) for t in WW_SCISSOR])
        put('adult_l%d_panel_ww_other' % L, [ww(t.format(W=PF, W2=PF2)) for t in WW_OTHER])
        def mm(t):
            s = t + ' Both men are nude.'
            if L == 6 and 'right hand is around the second man' in t: s += FIN_MM
            return s + TAIL + 'The shot is from the side showing both bodies.'
        put('adult_l%d_panel_mm_oral' % L, [mm(t.format(M=PM, M2=PM2)) for t in MM_ORAL])
        put('adult_l%d_panel_mm_anal' % L, [mm(t.format(M=PM, M2=PM2)) for t in MM_ANAL])
        put('adult_l%d_panel_mm_hand' % L, [mm(t.format(M=PM, M2=PM2)) for t in MM_HAND])
        # union files replace the earlier ones
        for pre, parts in (('wm', ['wm_vaginal', 'wm_oral', 'wm_anal']), ('ww', ['ww_oral', 'ww_scissor', 'ww_other']), ('mm', ['mm_oral', 'mm_anal', 'mm_hand'])):
            put('adult_l%d_panel_%s' % (L, pre), [x for p in parts for x in G['adult_l%d_panel_%s' % (L, p)]])
    put('kink_panel_wm', [t.format(W=PF, M=PM) + TAIL + 'The shot shows both bodies from head to knees.' for t in K_WM])
    put('kink_panel_ww', [t.format(W=PF, W2=PF2) + TAIL + 'The shot shows both bodies from head to knees.' for t in K_WW])
    put('kink_panel_mm', [t.format(M=PM, M2=PM2) + TAIL + 'The shot shows both bodies from head to knees.' for t in K_MM])
    put('kink_panel_f', [t.format(W=PF) + TAIL + 'The shot shows the whole body.' for t in K_F])
    put('kink_panel_m', [t.format(M=PM) + TAIL + 'The shot shows the whole body.' for t in K_M])
    G['v105_acts_entry_points'] = ep
    return G
