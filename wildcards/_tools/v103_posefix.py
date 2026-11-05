"""v103 - people and scene layers for adult poses: every pose line names a distinct adult (age, heritage, skin, build, hair) and gets a setting, light and framing clause."""
import re, random
def lines(final, name):
    import os
    return [l.strip() for l in open(os.path.join(final, name + '.txt'), encoding='utf8') if l.strip()]
SUFFIX = re.compile(r'\s+(background|ancestry|heritage|descent|roots|features|facial structure|traits|lineage|phenotype)$')
BADB = re.compile(r'child|boy|girl|teen|youth|minor|juvenile|little|tiny', re.I)
AFR = re.compile(r'Afro|Akan|Mandinka|Yoruba|Igbo|Zulu|Xhosa|Somali|Amhara|Afar|Oromo|Jamaican|Haitian|Nigerian|Ghana|Ethiopian|Kenyan|African|Aboriginal|Melanesian|Papua|Fijian|Senegal|Wolof|Tigray|Hausa|Fulani', re.I)
EUR = re.compile(r'Nordic|European|Slavic|Celtic|Mediterranean|Anglo|German|Scandinav|Baltic|Iberian|Italian|Greek|Irish|French|Dutch|Polish|Russian|Swedish|Norweg|Danish|Finn|English|Scot|Welsh|Croat|Serb|Czech|Slovak|Hungar|Roman|Bulgar|Ukrain|Albani|Sicilian|Spanish|Portug|Appalachian|Moldov|Argentine', re.I)
DECADES = [('twenties', 'early', 'mid', 'late', 28), ('thirties', 'early', 'mid', 'late', 26), ('forties', 'early', 'mid', 'late', 18), ('fifties', 'early', 'mid', 'late', 14), ('sixties', 'early', 'mid', 'late', 9), ('seventies', 'early', 'mid', 'late', 5)]
def person(r, sex, eth, builds):
    d = r.choices(range(6), [x[4] for x in DECADES])[0]; dec = DECADES[d]
    pos = r.choice(dec[1:4]); if_age = '%s %s' % (pos, dec[0])
    group, skin = eth
    pron = 'her' if sex == 'f' else 'his'
    if EUR.search(group): base = r.choice(['black', 'dark brown', 'chestnut brown', 'light brown', 'dark blond', 'honey blond', 'auburn', 'copper red', 'strawberry blond'])
    else: base = r.choice(['black', 'black', 'black', 'dark brown', 'dark brown', 'deep brown'])
    if d <= 1: hc = base
    elif d == 2: hc = r.choice([base, base, base + ' with a few grey strands'])
    elif d == 3: hc = r.choice([base + ' with grey streaks', 'salt-and-pepper ' + base, 'silver-grey'])
    elif d == 4: hc = r.choice(['silver-grey', 'grey', 'white-grey', 'salt-and-pepper'])
    else: hc = r.choice(['white', 'silver-white', 'thin grey'])
    if sex == 'f':
        if AFR.search(group): st = r.choice(['tight natural coils', 'a rounded natural afro', 'long braids', 'twist-out curls', 'a short tapered cut', 'locs past the shoulders', 'a high puff'])
        else: st = r.choice(['long straight', 'long wavy', 'shoulder-length wavy', 'a chin-length bob of', 'a short pixie crop of', 'loose curly', 'a high bun of', 'a low ponytail of', 'a sleek shoulder-length', 'a messy updo of', 'a side braid of', 'a layered shaggy'])
        hair = '%s %s hair' % (st, hc) if not AFR.search(group) else '%s in %s' % (st, hc)
        if st.startswith(('a ', 'tight', 'long braids', 'locs', 'twist')): hair = '%s, %s hair' % (st, hc) if AFR.search(group) else '%s %s hair' % (st, hc)
        extra = ''
    else:
        if AFR.search(group): st = r.choice(['a close-cropped', 'a short tapered', 'a short natural', 'locs of', 'a tight twist-out of', 'a shaved'])
        else: st = r.choice(['short neat', 'short tousled', 'a close crop of', 'medium-length swept-back', 'wavy collar-length', 'a buzz cut of', 'short curly', 'a side-parted'])
        if d >= 3 and r.random() < 0.35: hair = 'a receding hairline with %s hair at the sides' % hc
        elif d >= 4 and r.random() < 0.25: hair = 'a bald head with %s hair at the sides' % hc
        else: hair = '%s %s hair' % (st, hc)
        fh = r.choice(['clean-shaven', 'light stubble', 'a short trimmed beard', 'a full beard', 'a moustache', 'clean-shaven', 'dark stubble'])
        if d >= 3 and fh not in ('clean-shaven',): fh = fh.replace('dark', 'grey-flecked')
        hair += ', ' + fh
    return 'of %s, in %s late'.replace(' late', '') % (group, 'PLACEHOLDER')

BODY = [['taut, smooth, even skin','taut, smooth skin with an even tone'],['smooth, firm skin','smooth skin with good firmness'],['smooth skin with the first faint lines around the eyes and mouth','smooth skin with faint expression lines'],['fine lines on the face and slightly softer skin on the chest and belly','fine lines on the face and softening skin over the chest and belly'],['thinner skin with fine wrinkles, softening muscle and a few small age spots','thinner skin with fine wrinkles and a few small age spots'],['thin skin with creases, visible veins, a lower-set chest and belly and age spots','thin creased skin with visible veins and scattered age spots'],['thin crepey skin with many fine wrinkles, loosening skin at the chest, belly, arms and thighs, and age spots','crepey skin with many fine wrinkles, loose skin on the arms and thighs and age spots'],['very thin, deeply wrinkled skin with prominent ribs, collarbones and veins, sagging folds and many age spots','very thin, deeply wrinkled skin with prominent collarbones and veins and many age spots'],['paper-thin, deeply creased skin over a frail, stooped frame, with prominent bones and veins, hanging folds and large age spots','paper-thin, deeply creased skin over a frail, stooped frame with prominent veins and large age spots']]
HAND = [['taut, smooth skin with no lines'],['smooth, firm skin'],['smooth skin with the first faint lines across the knuckles'],['fine lines across the back of the hand and slightly more visible veins'],['thinner skin with visible veins and a few small age spots'],['thin skin with fine creases, visible veins and age spots'],['thin crepey skin with many fine wrinkles, prominent veins and age spots'],['very thin, deeply wrinkled skin with prominent tendons, veins and many age spots'],['paper-thin, deeply creased skin with sharply prominent tendons and veins and large age spots']]
def ladders():
    G = {}; ep = []
    for i in range(9):
        G['age_step%d_body_skin' % (i + 1)] = BODY[i]; G['age_step%d_hand_skin' % (i + 1)] = HAND[i]
        ep += ['age_step%d_body_skin' % (i + 1), 'age_step%d_hand_skin' % (i + 1)]
    return G, ep

HAND_MILD = ['with slightly thickened joints at the knuckles', 'with mildly enlarged knuckles and a stiff, careful grip', 'with slightly thickened middle finger joints', 'with gently enlarged knuckles and faint bony bumps at the fingertip joints', 'with slightly stiff, lightly curved fingers', 'with a slight sideways lean of the fingers at the joints']
HAND_MARKED = ['with clearly enlarged knuckles, small hard bony bumps at the fingertip joints and fingers that lean slightly sideways', 'with thickened, bony finger joints and fingers curving a little toward the little finger', 'with enlarged, firm knuckle joints and fingers that no longer lie fully straight', 'with prominent bony nodules at the middle and end finger joints and slightly bent fingers', 'with stiff, thickened joints, a visibly curved index and middle finger and a flattened palm hollow', 'with swollen-looking, ridged knuckle joints that stay in proportion to the fingers and fingers bent a little at the middle joints']
def hand_condition():
    return {'hand_condition_mild': HAND_MILD, 'hand_condition_marked': HAND_MARKED, 'hand_condition': HAND_MILD + HAND_MARKED}, ['hand_condition_mild', 'hand_condition_marked', 'hand_condition']

PUBIC_STUBBLE = ['pubic hair shaved a day or two ago, now a fine dark stubble across the whole area', 'a short, even pubic stubble a few days old, soft and slightly prickly looking', 'pubic hair grown back as light stubble over the mound and just a little longer at the top', 'a freshly clipped pubic area with a very short, even stubble about a millimetre long', 'fine regrowth stubble across the pubic mound, denser at the top and sparser along the sides', 'pubic hair worn as a close, uniform stubble with sharply defined edges along the hip creases', 'a faint shadow of stubble over an otherwise smooth pubic area', 'two-day pubic stubble with a few longer hairs standing out', 'short, coarse stubble over the mound and the top of the thighs after shaving']
PUBIC_PATCHY = ['pubic hair in uneven patches, thicker over the mound and bare at the sides', 'patchy pubic hair with small bare gaps scattered through short, soft hair', 'sparse, patchy pubic hair, a few clusters of hair with smooth skin showing between them', 'pubic hair that grows in two separate patches either side of the centre, with bare skin between', 'a thin, uneven pubic patch that is denser at the top and nearly bare lower down', 'pubic hair in scattered small tufts over smooth skin', 'partly shaved pubic hair, with a ragged edge where some patches are cut short and others left longer', 'patchy regrowth, short hair coming back unevenly with a few smooth bare spots', 'a thin, irregular pubic covering with bare skin showing through along the edges']
PUBIC_SHAPE = ['shaved into the shape of a small heart, the surrounding skin smooth', 'trimmed into an arrow pointing downward, the surrounding skin smooth', 'trimmed into a narrow vertical line, the rest of the area smooth', 'trimmed into a neat triangle with sharply defined edges, the rest of the area smooth', 'trimmed into an inverted triangle pointing down, the surrounding skin smooth', 'shaved into a small diamond shape, the surrounding skin smooth', 'trimmed into a lightning bolt, the surrounding skin smooth', 'trimmed into a small five-pointed star, the surrounding skin smooth', 'shaved into two parallel vertical stripes, the skin around and between them smooth', 'trimmed into a small round circle of hair, the surrounding skin smooth', 'trimmed into a narrow rectangle, the surrounding skin smooth', 'shaved into a small crescent moon shape, the surrounding skin smooth', 'trimmed into a thin horizontal bar above a short vertical line, the surrounding skin smooth', 'trimmed into a small butterfly shape, the surrounding skin smooth', 'trimmed into a short row of three small dots, the surrounding skin smooth', 'trimmed into a small flame shape, the surrounding skin smooth', 'trimmed into a thin arrow pointing upward, the surrounding skin smooth', 'trimmed into a small cross, the surrounding skin smooth']
def pubic(final):
    G = {'pubic_hair_stubble': PUBIC_STUBBLE, 'pubic_hair_patchy': PUBIC_PATCHY, 'pubic_hair_shape': PUBIC_SHAPE}
    for sx in ('f', 'm'):
        base = lines(final, '%s_pubichair' % sx)
        G['%s_pubichair_all' % sx] = base + PUBIC_STUBBLE + PUBIC_PATCHY + PUBIC_SHAPE
    return G, ['pubic_hair_stubble', 'pubic_hair_patchy', 'pubic_hair_shape', 'f_pubichair_all', 'm_pubichair_all']
def build(final):
    E = [l for l in lines(final, 'dem_ethnicity_skin')]
    eths = {}
    for l in E:
        p = l.split(', with ')
        if len(p) < 2: continue
        group = SUFFIX.sub('', p[0].strip()); m = re.match(r'^(.*? skin)', p[1].strip())
        if not m or ' that ' in m.group(1): m2 = re.match(r'^(.*?skin)', p[1].strip().split(' that ')[0] + ' skin') if not m else None
        sk = m.group(1) if m else None
        if sk and ' that ' in sk: sk = sk.split(' that ')[0] + ' skin'
        if not sk: continue
        eths.setdefault(group, []).append(sk)
    groups = sorted(eths)
    fb = sorted(set(x for x in lines(final, 'f_body_build') if not BADB.search(x)))
    mb = sorted(set(x for x in lines(final, 'm_body_build') if not BADB.search(x)))
    G = {}
    r = random.Random(1033)
    for sex, builds in (('f', fb), ('m', mb)):
        out = []; noun = 'woman' if sex == 'f' else 'man'
        for i in range(1600):
            g = r.choice(groups); skin = r.choice(eths[g]); eth = (g, skin)
            d = r.choices(range(6), [x[4] for x in DECADES])[0]; dec = DECADES[d]; pos = r.choice(dec[1:4])
            age = 'in %s %s %s' % ('her' if sex == 'f' else 'his', pos, dec[0])
            # hair
            if EUR.search(g): base = r.choice(['black', 'dark brown', 'chestnut brown', 'light brown', 'dark blond', 'honey blond', 'auburn', 'copper red', 'strawberry blond'])
            else: base = r.choice(['black', 'black', 'black', 'dark brown', 'dark brown', 'deep brown'])
            if d <= 1: hc = base
            elif d == 2: hc = r.choice([base, base, base + ' with a few grey strands'])
            elif d == 3: hc = r.choice([base + ' with grey streaks', 'salt-and-pepper ' + base, 'silver-grey'])
            elif d == 4: hc = r.choice(['silver-grey', 'grey', 'white-grey', 'salt-and-pepper'])
            else: hc = r.choice(['white', 'silver-white', 'thin grey'])
            afr = bool(AFR.search(g))
            if sex == 'f':
                if afr: hair = r.choice(['tight natural coils', 'a rounded natural afro', 'long braids', 'twist-out curls', 'a short tapered cut', 'locs past the shoulders', 'a high puff']) + ' in ' + hc if False else 'hair in ' + r.choice(['tight natural coils', 'a rounded natural afro', 'long braids', 'twist-out curls', 'a short tapered cut', 'locs past the shoulders', 'a high puff']) + ', ' + hc
                else: hair = r.choice(['long straight', 'long wavy', 'shoulder-length wavy', 'chin-length', 'short cropped', 'loose curly', 'sleek shoulder-length', 'layered shaggy']) + ' hair in ' + hc
                if not afr and r.random() < 0.25: hair = r.choice(['hair in a high bun, ', 'hair in a low ponytail, ', 'hair in a messy updo, ', 'hair in a side braid, ']) + hc
            else:
                if afr: hair = r.choice(['close-cropped', 'short tapered', 'short natural', 'twisted', 'shaved']) + ' hair in ' + hc
                else: hair = r.choice(['short neat', 'short tousled', 'close-cropped', 'medium-length swept-back', 'wavy collar-length', 'buzz-cut', 'short curly', 'side-parted']) + ' hair in ' + hc
                if d >= 3 and r.random() < 0.35: hair = 'a receding hairline with hair at the sides in ' + hc
                elif d >= 4 and r.random() < 0.25: hair = 'a bald head with hair at the sides in ' + hc
                fh = r.choice(['clean-shaven', 'light stubble', 'a short trimmed beard', 'a full beard', 'a moustache', 'clean-shaven', 'dark stubble'])
                if d >= 3: fh = fh.replace('dark stubble', 'grey-flecked stubble')
                hair += ' and ' + fh if fh != 'clean-shaven' else ' and a clean-shaven face'
            b = r.choice(builds)
            gg = g[0].upper() + g[1:]
            out.append('of %s heritage, %s, with %s, %s and %s' % (gg, age, skin, b, hair))
        G['apose_person_' + sex] = out
    G['apose_place'] = [x for x in 'a bright sunlit kitchen; a small tiled bathroom; a hotel room with a view over the city; a wooden cabin; a rooftop terrace; a garden shed turned studio; a plain white photography studio; a laundry room; a quiet back garden; a loft apartment with white brick walls; a beach house with pale wooden floors; a cluttered artist studio; a modern glass-walled living room; a country farmhouse bedroom; a hallway with a long mirror; a sunroom full of plants; a basement flat with low ceilings; a hotel corridor; a van converted into a bedroom; a sauna with pale wood benches; a bright dressing room; a woodland clearing; a rocky lakeside; a stone-floored conservatory; a narrow city balcony; a spacious attic room; a tiled courtyard; a small sparse bedsit; a library with tall shelves; a hotel pool terrace'.split('; ')]
    G['apose_light'] = [x for x in 'soft morning daylight through a window; bright midday sun; flat overcast daylight; low golden-hour sun; warm late-afternoon sun with long shadows; soft evening light from a window; even bright studio light; a mix of window light and a table lamp; warm tungsten room light; soft diffused bathroom light; dappled sunlight through leaves; the grey light of a rainy afternoon; bright white winter light; clear early morning light; hazy summer sunlight'.split('; ')]
    G['apose_frame'] = ['The whole body from head to feet is in the frame.', 'The shot is wide enough to show the whole body and the whole head.', 'The camera is far enough back to include the whole head and all of the body.', 'The photograph is framed at a medium-wide distance with the head fully in view.']
    out = []
    for L in range(1, 7):
        P = lines(final, 'adult_l%d_pose' % L); a = []; b = []
        for l in P:
            t = l
            def sub(noun, tok, s):
                return re.sub(r'\b' + noun + r"\b(?!['’]s)", noun + ' __' + tok + '__,', s, count=1)
            for kind, tok in (('women', 'apose_person_f'), ('men', 'apose_person_m')):
                t = re.sub(r'\b[Tt]wo (nude |naked |topless |shirtless |bare-chested |bare chested )?' + kind + r'\b', lambda m: m.group(0) + ', the first __' + tok + '__ and the second __' + tok + '__,', t, count=1)
            two = re.search(r'\b(two|three) (women|men)\b|\bcouple\b|\bwomen\b|\bmen\b', t)
            if not two:
                if re.search(r'\bwoman\b', t): t = sub('woman', 'apose_person_f', t)
                if re.search(r'\bman\b', t): t = sub('man', 'apose_person_m', t)
            t = re.sub(r',\s*,', ',', t)
            if re.search(r'\bpenis\b', t) and not re.search(r'foreskin|circumcis|\buncut\b|outline|bulge|beneath|under|through|fabric|chastity|cage|condom|\bring\b|sleeve|trouser|brief|underwear|boxer|thong|jock|pants|harness|strap|plug|sheath', t, re.I):
                _tok = 'penis_look_erect' if re.search(r'erect|hard|semi|stiff|rigid', t, re.I) else 'penis_look'
                t = re.sub(r'\bpenis\b', 'penis, __%s__,' % _tok, t, count=1)
                t = re.sub(r',\s*,', ',', t)
                t = re.sub(r'(__penis_look(?:_erect)?__),(?=\s*(?:\.|$))', r'\1', t)
            # the person clause lives inside commas, so the comma after the token closes it
            a.append(t)
            closeup = re.search(r'close-up|crop|extreme|detail|macro|only the|from (above|below|behind|the side|overhead)|\\bview\\b|angle|\\bshot\\b|framed|frame|photograph|seen\\b|silhouett', l, re.I)
            place = re.search(r'\b(rooftop|board|deck|dock|pier|patio|terrace|yard|sunlit|stage|studio|bar|cart|garage|street|alley|pavement|sidewalk|courtyard|stairwell|elevator|lift|cabin|tent|van|train|bus|plane|cockpit|stool|booth|sand|sea|water|rock|hill|field|grass|lawn|dune|snow|desert|shore|lake|river|hallway|fireplace|rug|carpet|mattress|cushion|pillow|bed|sofa|couch|chair|stool|kitchen|bath|shower|pool|car|balcon|doorway|door|desk|table|floor|rug|beach|garden|wall|window|stairs|hallway|mirror|chaise|armchair|bench|counter|hotel|tub|room|office|gym|forest|park|street|tent|boat|hammock|massage|towel|yoga)\w*', l, re.I)
            s = t
            if not place: s += ' The scene is in __apose_place__.'
            if not re.search(r'light|lamp|sun|candle|glow|dark|dim|shadow|neon|fire|moon|golden|daylight|bright|lit\b|lighting|streetlight|dusk|dawn|sunset|sunrise', l, re.I): s += ' The light is __apose_light__.'
            if not closeup: s += ' __apose_frame__'
            b.append(s)
        G['adult_l%d_pose_person' % L] = a; G['adult_l%d_pose_scene' % L] = b
        out += ['adult_l%d_pose_person' % L, 'adult_l%d_pose_scene' % L]
    LG, lep = ladders(); G.update(LG); out += lep
    HG, hep = hand_condition(); G.update(HG); out += hep
    PG, pep = pubic(final); G.update(PG); out += pep
    G['v103_posefix_entry_points'] = out + ['apose_person_f', 'apose_person_m', 'apose_place', 'apose_light', 'apose_frame']
    return G
