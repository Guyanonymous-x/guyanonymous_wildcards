"""v108 fixes found in the 2026-11-05 review of every library file changed in v106 and v107.
fix(G) takes {file name: list of lines} and returns it repaired. Applied at the end of v108_build, and once directly to the working library."""
import re
NIPPLE = ['a tiny, flat nipple, barely raised', 'a small, neat nipple', 'a medium nipple standing a little proud', 'a long, prominent nipple', 'a thick, wide nipple', 'an inverted nipple, drawn inward', 'a small nipple']
AREOLA = ['a very small areola about the width of a thumbnail', 'a small, tight areola about two centimetres across', 'a medium areola about three and a half centimetres across',
          'a wide areola about five centimetres across', 'a very wide areola about seven centimetres across, covering much of the front of the breast']
SURF = ['a shade darker than the surrounding skin', 'clearly darker than the surrounding skin and smooth', 'a little darker than the surrounding skin, with small raised bumps near its edge',
        'only slightly darker than the surrounding skin', 'with a softly wrinkled surface']
def nipples(lines):
    import random
    r = random.Random(108); keep = [l for l in lines if not re.search(r'centimetres|thumbnail', l)]
    for a in AREOLA:
        for i, n in enumerate(NIPPLE):
            if i == len(NIPPLE) - 1: keep.append('each breast has %s set in %s, the areola puffy and rising in a soft dome' % (n, a))
            else: keep.append('each breast has %s, set in %s, the areola %s' % (n, a, r.choice(SURF)))
    return keep
DIMPLE_LONG = r'with a small shallow dimple low on the middle of the chin tip, a soft spot of shadow about the size of a fingernail, not a long line'
def chin(lines):
    out = []
    for l in lines:
        if re.match(r'^chin with a faint small dimple in the middle of the tip and ', l) or re.match(r'^cleft chin with a small shallow dimple', l): continue
        l = l.replace('a cleft chin, with a small shallow dimple low on the middle of the chin tip, a soft spot of shadow about the size of a fingernail, not a long line, the outline of the chin smooth and unbroken',
                      'a chin with a small, shallow dimple in the middle of its tip, the outline of the chin smooth and unbroken')
        l = l.replace('a cleft chin showing only a small shallow dimple low on the middle of the chin tip, a soft spot of shadow about the size of a fingernail, not a long line, the chin one smooth rounded shape on either side of it',
                      'a chin with a small, shallow dimple in the middle of its tip, the chin one smooth, rounded shape')
        l = l.replace('a chin with a faint dimple in the middle of its tip, no longer than a fingernail and well below the lower lip, no vertical line', 'a chin with a faint, small dimple in the middle of its tip')
        l = l.replace(DIMPLE_LONG, 'with a small, shallow dimple in the middle of its tip')
        out.append(l)
    return out
REPL = {'act_dance_classes_action': [('mid-spin with a skirt flared out', 'mid-spin with the hair flying out')],
        'act_dance_classes_equip': [('a sprung wooden floor', 'a stack of exercise mats')],
        'act_yoga_action': [('lying in a final rest with the arms open', 'lying flat on the back in a final rest pose with the arms open at the sides')],
        'f_body_anus': [('a rosette with a slightly darker ring around it than the surrounding skin', 'a rosette ringed by skin slightly darker than the skin around it')]}
SCENE = {'act_yoga_scene_prompt': 'yoga', 'act_dance_classes_scene_prompt': 'dance_classes', 'act_martial_arts_scene_prompt': 'martial_arts'}
def fix(G):
    for k in [k for k in G if re.match(r'adult_l\d_group$', k)]: G[k] = list(dict.fromkeys(G[k]))
    if 'f_body_nipples' in G: G['f_body_nipples'] = nipples(G['f_body_nipples'])
    if 'head_chin' in G: G['head_chin'] = chin(G['head_chin'])
    for k, pairs in REPL.items():
        if k in G:
            for a, b in pairs: G[k] = [b if x == a else x for x in G[k]]
    for k, a in SCENE.items():
        if k in G: G[k] = [x.replace('__act_%s_equip__ can be seen.' % a, 'There is __act_%s_equip__ in view.' % a) for x in G[k]]
    return G

# ---- review batch 4 (adult panels L1-L3)
OCCLUDED = re.compile(r'lies fully on top of him|sits on his thighs facing him')
BULGE1 = re.compile(r' The fabric over his groin shows __male_bulge_\w+__\. His hands stay clear of his groin\.')
BULGE2 = re.compile(r" The fabric over the first man's groin shows __male_bulge_\w+__, and the fabric over the second man's groin shows __male_bulge_\w+__\. Neither man's hands are near his own groin\.")
def panels(G):
    for k in [k for k in G if re.match(r'(adult_l\d_panel|kink_panel)', k)]:
        out = []
        for x in G[k]:
            x = x.replace('Both people in this panel are women.', 'Both people are women.').replace('Both people in this panel are men.', 'Both people are men.')
            if OCCLUDED.search(x): x = BULGE2.sub('', BULGE1.sub('', x))
            out.append(x)
        G[k] = out
    return G
_fix0 = fix
def fix(G): return panels(_fix0(G))

# ---- review batch 5 (adult panels L4): name only the body parts the pose actually shows
L4_SEEN = 'Her breasts and her vulva are in view, and his penis hangs soft over his scrotum and is in view.'
L4_VIEW = [(re.compile(r'lies fully on top of him, her chest against his chest'), 'Their bodies are pressed together from chest to hips.'),
           (re.compile(r'sits on his thighs facing him'), 'Her breasts are in view from the side.'),
           (re.compile(r'stands bent forward at the hips at a table'), 'Her breasts hang in view, and his penis hangs soft over his scrotum and is in view beside her hips.')]
MM_TOP = re.compile(r'lies fully on top of him, his chest against the first man')
MM_SEEN = 'Both men are nude, with both their chests and their penises and scrotums in view, the penises hanging soft.'
def l4(G):
    for k in [k for k in G if re.match(r'adult_l4_panel_(wm|mm)$', k)]:
        out = []
        for x in G[k]:
            for rx, rep in L4_VIEW:
                if rx.search(x): x = x.replace(L4_SEEN, rep)
            if MM_TOP.search(x): x = x.replace(MM_SEEN, 'Both men are nude, their bodies pressed together from chest to hips.')
            out.append(x)
        G[k] = out
    return G
_fix1 = fix
def fix(G): return l4(_fix1(G))

# ---- review batch 6 (adult panels L5/L6): 69 lines ungrammatical ("with the first man's head is level with ...")
def sixtynine(G):
    for k in [k for k in G if re.match(r'(adult_l\d_panel|adult_l\d_position)', k)]:
        G[k] = [x.replace(' head is level with', ' head level with') if 'in opposite directions' in x else x for x in G[k]]
    return G
_fix2 = fix
def fix(G): return sixtynine(_fix2(G))

# ---- review batch 7 (adult positions L5/L6)
FLOOR_OLD = 'sits on the edge of a bed with his feet apart and a woman __apose_person_f__, lies back on the floor between his thighs, her legs over his thighs.'
FLOOR_NEW = 'sits on the edge of a bed with his feet flat on the floor and a woman __apose_person_f__, sits astride his lap facing him with her knees on the mattress either side of his hips and her arms around his neck.'
def positions(G):
    for k in [k for k in G if re.match(r'adult_l\d_position', k)]:
        out = []
        for x in G[k]:
            x = x.replace(FLOOR_OLD, FLOOR_NEW)
            if 'All of them are nude' in x: x = x.replace('showing both bodies full length', 'showing all three bodies full length')
            body = x.split('The shot is')[0]
            if not re.search(r'\bbed\b|mattress|pillow|lies |on all fours', body) and re.search(r'stand|chair|sofa|wall|table', body): x = x.replace('The shot is from the side, at mattress height,', 'The shot is from the side, at hip height,')
            elif re.search(r'\bbed\b|mattress|pillow|lies |on all fours', body) and not re.search(r'stands|chair|sofa|wall|table', body): x = x.replace('The shot is from the side, at hip height,', 'The shot is from the side, at mattress height,')
            out.append(x)
        G[k] = out
    return G
_fix3 = fix
def fix(G): return positions(_fix3(G))

# ---- review batch 8 (adult locations): wet or hot places get swimwear at levels 1 and 3
WET = re.compile(r'open-air shower|steam room|cedar sauna|plunge pool|hot tub|dock of a quiet forest lake')
def locations(G):
    for L in (1, 3):
        k = 'adult_l%d_location' % L
        if k not in G: continue
        out = []
        for x in G[k]:
            if WET.search(x):
                if L == 1:
                    x = re.sub(r'He wears [^.]*\.', 'He wears swim shorts and an open linen shirt.', x)
                    x = re.sub(r'She wears [^.]*\.', 'She wears a one-piece swimsuit with a sarong tied at the waist.', x)
                else:
                    x = re.sub(r'He is shirtless and wears [^.]*\. The fabric over his groin shows __male_bulge_\w+__\.', 'He is shirtless and wears swim trunks. The fabric over his groin shows __male_bulge_medium__.', x)
                    x = re.sub(r'She is topless and wears [^.]*\.', 'She is topless and wears bikini bottoms.', x)
            out.append(x)
        G[k] = out
    return G
_fix4 = fix
def fix(G): return locations(_fix4(G))

# ---- review batch 9 (solo scenes, level 3 poses): no "nude" next to a garment; garment words match
POSE3 = [('in low-slung jeans bends to pick up a dropped book, the bare side of his thigh and buttock exposed', 'in low-slung jeans bends to pick up a dropped book, the waistband slipping to show the top of his buttocks'),
         ('kneeling nude on a bed, one arm across his abdomen and the other behind his head, shot from the side in boxer briefs', 'kneeling on a bed in boxer briefs and nothing else, one arm across his abdomen and the other behind his head, shot from the side'),
         ('kneels on a bed in only stockings, a lace thong on and her breasts bare', 'kneels on a bed in stockings and a lace thong, her breasts bare'),
         ('on all fours on a bed, nude, photographed from the side in cotton briefs', 'on all fours on a bed in cotton briefs and nothing else, photographed from the side'),
         ('recline nude on a rug, one lying with her head on the other\'s hip, a thin lace thong on each', 'recline on a rug in thin lace thongs and nothing else, one lying with her head on the other\'s hip')]
def solo(G):
    for k in ('adult_l3_pose_person', 'adult_l3_pose_scene'):
        if k in G:
            out = []
            for x in G[k]:
                for a, b in POSE3: x = x.replace(a, b)
                out.append(x)
            G[k] = out
    for k in ('adult_l2_masturbation_m', 'adult_l2_masturbation_f'):
        if k in G:
            out = []
            for x in G[k]:
                if 'swim trunks' in x: x = x.replace('his underwear', 'his swim trunks')
                if 'mesh bodysuit' in x: x = x.replace('her underwear', 'her bodysuit')
                out.append(x)
            G[k] = out
    return G
_fix5 = fix
def fix(G): return solo(_fix5(G))

# ---- review batch 10 (wrestling): genitals named only in holds that show them
WR_SEEN = 'Both men are nude, with their penises and scrotums in view, hanging soft, and their skin shiny with sweat.'
WR_HIDDEN = re.compile(r"legs wrapped around the second man's waist|lies face down on a mat|legs scissored around|presses chest to chest")
def wrestling(G):
    k = 'adult_l4_wrestling_mm'
    if k in G: G[k] = [x.replace(WR_SEEN, 'Both men are nude, their skin shiny with sweat.') if WR_HIDDEN.search(x) else x for x in G[k]]
    return G
_fix6 = fix
def fix(G): return wrestling(_fix6(G))

# ---- review batch 11 (group scenes L4): the nude sentence names only the bodies in that trio
G4_OLD = 'Everyone is nude, with breasts and penises and scrotums in view, the penises hanging soft.'
G4_NEW = {'mmm': 'Everyone is nude, with all three men\'s penises and scrotums in view, hanging soft.',
          'www': 'Everyone is nude, with all three women\'s breasts and vulvas in view.',
          'wmm': 'Everyone is nude, with the woman\'s breasts and vulva and both men\'s penises, hanging soft, in view.',
          'wwm': 'Everyone is nude, with both women\'s breasts and vulvas and the man\'s penis, hanging soft, in view.'}
def combo(x):
    head = re.match(r'This scene shows three adults, which is (.*?)\. ', x)
    if not head: return None
    h = re.sub(r'__apose_person_[fm]__;?', '', head.group(1)); h = ' '.join(h.split())
    return {'a man a second man and a third man': 'mmm', 'a woman a second woman and a third woman': 'www',
            'a woman a man and a second man': 'wmm', 'a woman a second woman and a man': 'wwm'}.get(h)
def groups(G):
    k = 'adult_l4_group'
    if k in G:
        out = []
        for x in G[k]:
            c = combo(x)
            if c and G4_OLD in x: x = x.replace(G4_OLD, G4_NEW[c])
            out.append(x)
        G[k] = out
    return G
_fix7 = fix
def fix(G): return groups(_fix7(G))

# ---- user decisions 2026-11-05: table pose out of level 1; L6 same-sex endings; no "not white"; activity templates
def l1_table(G):
    k = 'adult_l1_panel_wm'
    if k in G: G[k] = [x for x in G[k] if 'stands bent forward at the hips at a table' not in x]
    return G
SEM = ' Semen leaves the tip of %s penis __semen_amount__, and it lands %s; it is __semen_look__. __semen_after__'
OUT = ' %s has pulled out, and semen leaves the tip of his penis __semen_amount__, and it lands %s; it is __semen_look__. __semen_after__'
MM6 = [("sits on the edge of a bed with his knees apart and his hands in the hair", SEM % ("the first man's", "on the second man's lips and chin")),
       ("lie on their sides on a bed facing each other in a 69", SEM % ("the first man's", "on the second man's lips and chin")),
       ("kneels over him in a 69", SEM % ("the second man's", "on the first man's lips and chin")),
       ("stands with his back against a wall and a second man", SEM % ("the first man's", "on the second man's lips and chin")),
       ("lies on his stomach between the first man's legs", SEM % ("the first man's", "on the second man's lips and chin")),
       ("kneels on all fours on a bed with his arms straight", OUT % ("The second man", "across the first man's lower back and buttocks")),
       ("knees pulled up against his chest", OUT % ("The second man", "on the first man's stomach")),
       ("lie on their right sides on a bed facing the same direction", OUT % ("The second man", "across the first man's lower back")),
       ("squats over his hips facing him", " The second man has lifted off, and semen leaves the tip of the first man's penis __semen_amount__, and it lands on the first man's stomach; it is __semen_look__. __semen_after__"),
       ("stands bent forward at the waist beside a table", OUT % ("The second man", "across the first man's lower back and buttocks")),
       ("sit facing each other on a bed with their legs apart", SEM % ("the first man's", "on the second man's stomach")),
       ("lie side by side on a bed on their backs", SEM % ("each man's", "on his own stomach")),
       ("lie chest to chest on a bed", SEM % ("the first man's", "between their stomachs")),
       ("holding both of their erect penises together", SEM % ("the first man's", "on the first man's stomach"))]
SQ = ' Thin, clear, watery fluid comes out of %s vaginal opening __squirt_form__ %s. The fluid is clear and transparent, and it falls downward.'
WW6 = [("her hands in the hair of a second woman", SQ % ("the first woman's", "onto the sheet beneath her")),
       ("lie on their sides on a bed facing each other in a 69", SQ % ("the first woman's", "onto the sheet beneath her")),
       ("kneels over her in a 69", SQ % ("the second woman's", "onto the first woman's chin and chest")),
       ("sits on the edge of a sofa with her legs spread", SQ % ("the first woman's", "onto the cushion beneath her")),
       ("kneels over her face", SQ % ("the second woman's", "onto the first woman's chin and chest")),
       ("sit facing each other on a bed with their hips close together", SQ % ("the first woman's", "onto the sheet between them")),
       ("with her right thigh between the first woman's legs", SQ % ("the first woman's", "onto the sheet beneath her")),
       ("lie on their backs on a bed with their heads at opposite ends", SQ % ("the first woman's", "onto the sheet between them")),
       ("index and middle fingers inside", SQ % ("the first woman's", "around the second woman's fingers onto the sheet")),
       ("kneels between her thighs wearing a black strap-on", SQ % ("the first woman's", "onto the sheet beneath her")),
       ("kneels upright behind her wearing a leather strap-on", SQ % ("the first woman's", "onto the sheet beneath her")),
       ("sits upright astride the hips of a second woman", SQ % ("the first woman's", "onto the second woman's stomach"))]
def l6_endings(G):
    for k in [k for k in G if re.match(r'adult_l6_panel_(mm|ww)', k)]:
        table, tag = (MM6, 'Both men are nude.') if '_mm' in k else (WW6, 'Both women are nude.')
        out = []
        for x in G[k]:
            if 'semen leaves' not in x.lower() and 'watery fluid' not in x:
                for rx, end in table:
                    if rx in x: x = x.replace(tag, tag + end, 1); break
            out.append(x)
        G[k] = out
    return G
def not_white(G):
    for k in G:
        G[k] = [x.replace('transparent, not white, and it falls downward', 'clear and transparent, and it falls downward').replace('transparent like water, not white, and', 'clear and transparent like water, and') for x in G[k]]
    return G
STYLE = ['a candid documentary photograph', 'a natural-light lifestyle photograph', 'a cinematic photograph with subtle film grain',
         'a travel photograph with true-to-life colour', 'an editorial photograph taken on location', 'a clean contemporary magazine photograph taken on location']
def activities(G):
    for k in [k for k in G if re.match(r'act_.+_scene_prompt$', k)]:
        G[k] = [re.sub(r'(__act_[a-z_]+_equip__) can be seen\.', r'There is \1 in view.', x).replace('A place for dj and', 'A place for DJ and') for x in G[k]]
    for k in [k for k in G if re.match(r'act_.+_frame_prompt$', k)]:
        G[k] = [x.replace(' __frame_person_style__, __frame_person_full__', ' It is __act_frame_style__. __frame_person_full__') for x in G[k]]
    G['act_frame_style'] = STYLE
    return G
_fix8 = fix
def fix(G): return activities(not_white(l6_endings(l1_table(_fix8(G)))))
def cast(G):
    for k in [k for k in G if k.startswith('adult_')]:
        G[k] = [re.sub(r'^This scene shows (two|three) adults(, both (?:men|women))?(?::|, which is|, with) ', r'This scene shows \1 adults\2. They are ', x) for x in G[k]]
    return G
_fix9 = fix
def fix(G): return cast(_fix9(G))
def scene_incl(G):
    for k in [k for k in G if re.match(r'act_.+_scene_prompt$', k)]:
        G[k] = [re.sub(r'There is (__act_[a-z_]+_equip__) in view\.', r'The scene includes \1.', x) for x in G[k]]
    return G
_fix10 = fix
def fix(G): return scene_incl(_fix10(G))
