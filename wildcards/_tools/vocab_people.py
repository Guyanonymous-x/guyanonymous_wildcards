"""Vocabulary expansion, demographic / person-level files, hair types, poses, expressions, male grooming."""
import itertools, random
from vocab_lib import S, sample, seed_of, consistent
from vocab_face import R, reg, dims
from vocab_scene import P

# ---------------------------------------------------------------- dem_bone
reg('dem_bone', 'facial bone structure', [S("broad, narrow, delicate, strong, angular, rounded, high-boned, low-boned, prominent, subtle, symmetrical, slightly asymmetrical, sturdy, fine, long, short, wide-set, compact, balanced, sculpted, flat-planed, deep-set"),
    S("with high cheekbones, with low cheekbones, with a strong brow ridge, with a soft brow ridge, with a wide jaw, with a narrow jaw, with a prominent chin, with a recessed chin, with a broad nasal bone, with a narrow nasal bone, with wide-set orbits, with deep orbits, with a rounded skull, with a long skull, with a short skull, with a flat face profile, with a projecting mid-face, with a gentle forehead slope, with a high forehead, with a low forehead")], k=2, n=260, fmt='{a} {noun} {b}')

# ---------------------------------------------------------------- dem_ethnicity / dem_heritage
PEOPLES = S("""
Yoruba, Igbo, Akan, Hausa, Fulani, Wolof, Mandinka, Zulu, Xhosa, Sotho, Tswana, Shona, Swahili coast, Maasai, Kikuyu, Luo, Baganda, Amhara, Oromo, Tigrayan, Somali, Afar, Sudanese Arab, Nubian, Egyptian, Berber, Tuareg, Moroccan, Algerian, Tunisian, Libyan, Malagasy, Khoisan, Himba, Gullah, Garifuna, Afro-Brazilian, Afro-Colombian, Afro-Cuban, Afro-Jamaican, Haitian Creole,
Gulf Arab, Levantine, Iraqi, Yemeni, Bedouin, Persian, Kurdish, Azeri, Turkish, Armenian, Georgian, Assyrian, Pashtun, Tajik, Hazara, Baloch, Punjabi, Sindhi, Gujarati, Marathi, Bengali, Odia, Telugu, Tamil, Kannada, Malayali, Kashmiri, Assamese, Sinhalese, Nepali, Bhutanese, Tibetan, Mongolian, Kazakh, Kyrgyz, Uzbek, Turkmen, Uyghur, Buryat, Yakut, Evenki, Tuvan,
Han Chinese, Cantonese, Hokkien, Hakka, Manchu, Zhuang, Yi, Naxi, Taiwanese Hoklo, Taiwanese indigenous, Japanese, Okinawan, Ainu, Korean, Vietnamese, Thai, Lao, Khmer, Burmese, Shan, Karen, Hmong, Malay, Javanese, Sundanese, Minangkabau, Balinese, Bugis, Dayak, Filipino Tagalog, Visayan, Igorot, Papuan, Aboriginal Australian, Torres Strait Islander, Maori, Samoan, Tongan, Native Hawaiian, Fijian, Tahitian, Chamorro, Marshallese, Melanesian,
Irish, Scottish Highlander, Welsh, English, Breton, Cornish, French, Basque, Catalan, Castilian Spanish, Galician, Portuguese, Northern Italian, Southern Italian, Sicilian, Sardinian, Maltese, Greek, Cypriot, Albanian, Bosnian, Serbian, Croatian, Slovenian, Macedonian, Bulgarian, Romanian, Moldovan, Hungarian, Slovak, Czech, Polish, Lithuanian, Latvian, Estonian, Belarusian, Ukrainian, Russian, Finnish, Sami, Swedish, Norwegian, Danish, Icelandic, Faroese, German, Austrian, Swiss, Dutch, Flemish, Luxembourgish, Roma, Ashkenazi Jewish, Sephardi Jewish, Mizrahi Jewish,
Navajo, Apache, Cherokee, Lakota, Ojibwe, Cree, Haida, Inuit, Yupik, Aleut, Quechua, Aymara, Maya, Nahua, Zapotec, Mixtec, Guarani, Mapuche, Yanomami, Mestizo Mexican, Mestizo Peruvian, Andean mestizo, Cuban, Puerto Rican, Dominican, Brazilian mixed, Argentine European-descended, Chilean, Colombian, Venezuelan, Cape Verdean, Louisiana Creole, Cajun, Pennsylvania German, Appalachian, Texan Tejano, Hawaiian local
""")
ANC_FORM = S("{p} ancestry, {p} heritage, {p} lineage, {p} features, {p} traits, {p} phenotype, {p} facial structure, {p} roots, {p} descent, {p} background")
def _eth(o):
    out = []
    rng = random.Random(seed_of('dem_ethnicity'))
    for p in PEOPLES:
        for f in rng.sample(ANC_FORM, 3): out.append(f.format(p=p))
    return sample(out, 400, 'dem_ethnicity_s')
R['dem_ethnicity'] = _eth
REGIONS = S("West African, East African, North African, Southern African, Horn of Africa, Arab, Levantine, Persian, Turkic, Caucasian, South Asian, Himalayan, Central Asian, Mongolic, East Asian, Southeast Asian, Pacific Islander, Aboriginal Australian, Polynesian, Melanesian, Northern European, Western European, Southern European, Eastern European, Slavic, Celtic, Nordic, Mediterranean, Iberian, Balkan, Baltic, Native North American, Arctic, Mesoamerican, Andean, Amazonian, Caribbean, Latin American mestizo")
def _her(o):
    out = [f'{a} and {b} heritage mix' for a, b in itertools.combinations(REGIONS, 2)]
    out += [f'mixed {a} and {b} ancestry' for a, b in itertools.combinations(REGIONS, 2)]
    out += [f'{a} and {b} features blended' for a, b in itertools.combinations(REGIONS, 2)]
    out += [f'mostly {a} with some {b} ancestry' for a, b in itertools.permutations(REGIONS, 2)]
    out += [f'{r} heritage with a distinct local look' for r in REGIONS]
    return sample(out, 420, 'dem_heritage')
R['dem_heritage'] = _her

# ---------------------------------------------------------------- dem_tone (more shades; depth variants are more numerous for the more common depths)
DEPTH = [("very pale", 1), ("pale", 3), ("fair", 7), ("light", 10), ("light-medium", 12), ("medium", 16), ("olive-medium", 14), ("tan", 14), ("golden-brown", 14), ("warm brown", 16), ("medium-deep brown", 16), ("deep brown", 14), ("very deep brown", 8), ("dark ebony-brown", 5)]
UND = S("with warm golden undertones, with warm peach undertones, with cool pink undertones, with cool blue-pink undertones, with neutral undertones, with olive-green undertones, with yellow undertones, with red undertones, with copper-red undertones, with bronze undertones, with beige undertones, with a balanced mix of warm and cool undertones, with subtle olive undertones, with golden-olive undertones, with rosy undertones")
SURF = S("skin, skin with a matte look, skin with a healthy glow, skin with a slight sheen, skin that tans easily, skin that burns easily, skin with an even tone, skin with natural variation across the face, skin that is slightly darker on the hands and neck")
def _tone(o):
    out = []
    for d, n in DEPTH:
        pool = [f'{d} {s}, {u}' for s in SURF for u in UND]
        out += sample(pool, n * 3, 'tone' + d)
    return out
R['dem_tone'] = _tone

# ---------------------------------------------------------------- dem_unique (small individual quirks)
UQ_MARK = S("a small mole, a beauty mark, a pale birthmark, a freckle cluster, a patch of freckles, a single dimple, a faint dimple, a small crescent-shaped mark, a light patch of skin, a darker patch of skin, a small raised mole, a cluster of tiny moles, a mole with a hair, a flat brown spot")
UQ_PLACE = S("above the lip, beside the nose, on one cheek, on the chin, near the eye, at the temple, on the forehead, under the eye, at the corner of the mouth, on the jawline, on the neck, on the collarbone, behind the ear, on the upper lip, between the eyebrows")
UQ_TRAIT = S("a slightly crooked smile, a gap between the front teeth, one canine tooth sitting higher than the rest, a slight overbite, a slight underbite, a deep cleft chin, a dimpled chin, one eyebrow set higher than the other, a slightly crooked nose, a nose with a small bump, a prominent philtrum, a wide-set pair of eyes, eyes with a slight asymmetry, a prominent Adam's apple, a long neck, unusually long eyelashes, naturally curled lashes, a widow's peak, a cowlick at the hairline, a double crown in the hair, a white streak in the hair, a lock of hair that never sits flat, an upturned nose, a roman nose, a button nose, ears that stick out slightly, ears with attached lobes, a prominent chin, a very strong jaw, a slim face, very high cheekbones, naturally full lips, naturally thin lips, naturally pink lips, a lopsided grin, a lazy eye, a squint when smiling, deep-set eyes, hooded eyelids, round cheeks, a strong brow, a faint scar through the eyebrow, naturally arched brows, thick natural brows, a small gap in one eyebrow, freckles across the shoulders, freckles on the hands, a prominent collarbone, a tall forehead, a low hairline, a broad smile that shows the gums, a quiet half-smile, a habitually raised eyebrow, a slight head tilt, a distinct laugh line, smile creases on one side only, a small tooth chip, a tooth with a gold cap, braces on the teeth, a retainer wire, a tongue piercing glint, a nose stud, a septum ring, stretched earlobes, a beauty mark on the lip")
def _uq(o):
    out = [f'{m} {p}' for m in UQ_MARK for p in UQ_PLACE] + UQ_TRAIT
    return sample(out, 260, 'dem_unique')
R['dem_unique'] = _uq

# ---------------------------------------------------------------- attractiveness / expressions / poses / extras
ATT_A = (S("Striking, Attractive, Classic, Conventionally attractive, Handsome or beautiful in an understated way, Warm-looking, Pleasant-looking, Approachable"),
         S("A fictional adult with balanced proportions and an easy, natural look, A fictional adult with soft, pleasing features, A fictional adult with expressive eyes and an open face, A fictional adult with a kind face, A fictional adult with harmonious features and a relaxed expression, A fictional adult with clear, even features"))
ATT_B = (S("Plain, Average, Unremarkable at a glance, Ordinary, Everyday-looking"),
         S("A fictional adult with an everyday, relatable appearance, A fictional adult with typical proportions and ordinary features, A fictional adult with features that blend easily into a crowd, A fictional adult with a face that is neither striking nor plain"))
ATT_C = (S("Distinctive, Memorable, Rugged, Delicate, Quirky, Unconventional, Interesting-looking, Strong-featured, Soft-featured"),
         S("A fictional adult with distinctive features that stand out, A fictional adult with an unusual but compelling face, A fictional adult with strong, defined features, A fictional adult with slightly irregular features that add character, A fictional adult with an intense, memorable face, A fictional adult with a face that changes a lot with expression, A fictional adult with a face that looks best in profile"))
R['attractiveness'] = lambda o: sample(P('{0}: {1}', *ATT_A) + P('{0}: {1}', *ATT_B) + P('{0}: {1}', *ATT_C), 200, 'attractiveness')

EXPR_BASE = S("annoyed, anxious, astonished, bewildered, blank, concerned, deadpan, delighted, disgusted, exhausted, fearful, frowning, furious, gentle, gloomy, glowering, grinning, heartbroken, impish, irate, joyful, melancholic, mildly offended, mischievous, pensive, sad, scared, sheepish, shocked, silly, skeptical, smiling broadly, sneering, sobbing, surprised, suspicious, teary-eyed, terrified, thoughtful, tired, triumphant, worried, winking, amused, bashful, bored, calm, cheerful, confident, content, curious, determined, disappointed, dreamy, embarrassed, enthusiastic, flirtatious, focused, grateful, hopeful, indifferent, jealous, lonely, nervous, nostalgic, optimistic, playful, proud, relaxed, relieved, resigned, serene, shy, smug, stern, stunned, sympathetic, tender, uneasy, wary, wistful")
EXPR_MOD = S("slightly, openly, barely, deeply, almost, visibly, quietly, suddenly, politely, nervously, warmly, coolly")
EXPR_PART = S("with the eyes crinkling, with the brows drawn together, with the brows raised, with one brow lifted, with the mouth slightly open, with the lips pressed together, with the jaw clenched, with the head tilted, with the chin lowered, with the eyes wide, with the eyes narrowed, with the eyes cast down, with the corners of the mouth lifting, with the corners of the mouth turned down, with the nostrils flaring, with a long exhale")
R['facialExpressionsFor_v10'] = lambda o: EXPR_BASE + sample([x for x in P('{0}, {1}', EXPR_BASE, EXPR_PART) if consistent(x)], 260, 'fx2')

ARM = S("Arms outstretched, Arms spread wide, Arms crossed over the chest, One arm extended forward, One arm raised overhead, Both arms raised, Arms folded loosely, Arms hanging relaxed at the sides, One hand on the hip, Both hands on the hips, Hands clasped in front, Hands clasped behind the back, Hands resting on the knees, One hand touching the chin, Both hands in the pockets, One hand running through the hair, A hand resting on the neck, A hand shading the eyes, One hand holding the opposite elbow, Hands pressed together, Both hands behind the head, One hand reaching out, A hand on the chest, One hand on a railing, A hand tucking hair behind the ear")
BODYP = S("leaning slightly forward, leaning back, leaning to one side, standing tall, standing with weight on one leg, standing with feet wide, standing with feet together, sitting with legs crossed, sitting with knees apart, sitting forward, kneeling on one knee, crouching low, walking forward, stepping to one side, turning at the waist, bending slightly at the waist, twisting the torso, arching the back, rocking on the heels, balancing on tiptoe, stretching up, lunging forward, swaying gently")
GAZEP = S("gazing downward, gazing upward, looking straight ahead, looking over one shoulder, looking off to the side, looking back at the camera, looking into the distance, with eyes closed, with a sidelong glance, with the head tilted, with the chin raised, with the head bowed, with a soft smile, with a calm face, with a thoughtful look, with a playful look")
R['poses'] = lambda o: sample(P('{0}, {1}, {2}', ARM, BODYP, GAZEP), 400, 'poses')

COMP_F = S("her best friend, her sister, her older sister, her younger sister, her fraternal twin sister, her identical twin sister, her two sisters, her cousin, her two cousins, her mother, her grandmother, her daughter, her colleague, her roommate, her neighbour, her classmate, her teammate, her dance partner, her partner, her wife, her husband, her boyfriend, her girlfriend, her brother, her father, her uncle, her aunt, her friend group of four, a stranger she just met, her dog, her cat, a small group of friends, a child she is minding, an elderly neighbour, her bandmates, her study group, her travelling companion")
COMP_M = [c.replace('her ', 'his ').replace('his wife', 'his wife').replace('her husband', 'his husband').replace('his husband', 'his husband').replace('his boyfriend', 'his boyfriend').replace('his girlfriend', 'his girlfriend').replace('his sister', 'his sister') for c in COMP_F]
COMP_M = [c.replace('his boyfriend', 'his partner (a man)').replace('his girlfriend', 'his girlfriend') for c in COMP_M]
POS_X = S("standing beside, sitting next to, posing with, laughing with, walking with, leaning against, hugging, holding hands with, with an arm around, back to back with")
def _extras(g):
    comp = COMP_F if g == 'f' else COMP_M
    pron = 'her' if g == 'f' else 'his'
    out = [f'and {c}' for c in comp] + [f'{p} {c}' for p in POS_X for c in comp] + [f'beside a lifesize cardboard cut-out of {"herself" if g=="f" else "himself"} in a different outfit']
    return sample(out, 260, 'extras' + g)
R['f_extrasinphoto'] = lambda o: _extras('f'); R['m_extrasinphoto'] = lambda o: _extras('m')

# ---------------------------------------------------------------- body build / height (files weighted by likelihood; the apply step keeps their proportions)
BUILD_W = S("slender, lean, athletic, toned, muscular, stocky, sturdy, broad, compact, petite, average, medium, soft, rounded, curvy, full-figured, heavyset, thick-set, rangy, wiry, willowy, solid, balanced, strong, light, slight, long-limbed, barrel-chested, broad-shouldered, narrow-shouldered, pear-shaped, apple-shaped, hourglass, rectangular, inverted-triangle, V-shaped")
BUILD_X = S("with a long torso, with a short torso, with long legs, with short legs, with narrow hips, with wide hips, with a defined waist, with a straight waist, with a soft midsection, with a flat stomach, with strong shoulders, with sloping shoulders, with a deep chest, with a narrow chest, with sturdy thighs, with slim thighs, with a generally even distribution of weight, with weight carried low, with weight carried high, with good posture")
def _bb(o): return sample([f'{a} build {x}' for a in BUILD_W for x in BUILD_X if consistent(f'{a} build {x}')], 240, 'bb')
R['f_body_build'] = _bb; R['m_body_build'] = _bb
HT = S("very short, short, below-average height, slightly below-average height, average height, medium height, slightly above-average height, above-average height, tall, very tall, towering")
HT_X = S("with a slim frame, with a sturdy frame, with a broad frame, with long limbs, with short limbs, with a long torso, with long legs, with a compact build, with a slight build, with an athletic build, with a rangy build, with a graceful bearing, with an upright bearing, with a relaxed bearing, with a stooped bearing, with a confident presence, with a quiet presence, who appears taller in heels or boots, who appears shorter next to others, who looks tall against doorways, who looks small next to furniture")
def _bh(o): return sample([f'{a} stature {x}' for a in HT for x in HT_X if consistent(f'{a} {x}')], 220, 'bh')
R['f_body_height'] = _bh; R['m_body_height'] = _bh

R['f_hair_baby'] = None
reg('f_hair_baby', 'baby hairs', [S("fine, soft, wispy, sparse, dense, short, long, curly, straight, wavy, feathery, fluffy, delicate, light, fuzzy, neat, stray, swooped, sleek, gelled, natural, tousled, tiny, silky, thin, thick"),
    S("along the forehead, at the temples, along the nape of the neck, around the ears, along the whole hairline, in front of the ears, at the corners of the forehead, framing the face, swept to one side, laid in small swirls, left natural, brushed flat, lifting in the light, tucked away")], k=2, n=220, fmt='{a} {noun} {b}')

# ---------------------------------------------------------------- male grooming, facial hair, chest hair
BEARD = S("full beard, short boxed beard, long beard, stubble, heavy stubble, light stubble, goatee, soul patch, Van Dyke, chin strap beard, chinstrap with a mustache, mutton chops, sideburns only, handlebar mustache, pencil mustache, horseshoe mustache, walrus mustache, toothbrush mustache, Fu Manchu mustache, imperial mustache, balbo beard, anchor beard, garibaldi beard, French fork beard, ducktail beard, circle beard, patchy beard, wispy beard, braided beard, forked beard, beardless chin with a mustache, clean-shaven face, nearly clean-shaven face with a shadow, designer stubble, lumberjack beard, mountain-man beard, trimmed beard with a sharp neckline, soft natural beard, salt-pepper-free beard")
BEARD = [b for b in BEARD if 'free' not in b]
BEARD_X = S("neatly groomed, slightly unkempt, shaped with sharp edges, left natural, oiled and glossy, lightly combed, freshly trimmed, thick and full, thin and patchy, even all over, denser along the jaw, sparser on the cheeks, fading into the sideburns, connected to the mustache, with a clean-shaven cheek line, with a defined neckline, with a clean upper lip, with a long chin section, with a rounded bottom, with a pointed bottom")
def _art(b):
    if b.split()[-1] in ('stubble', 'chops', 'only', 'sideburns') or b.endswith(('stubble', 'only', 'chops')) or b.startswith(('clean-shaven', 'nearly', 'beardless')): return b
    return ('an ' if b[0] in 'aeiou' else 'a ') + b
def _fh(o):
    out = []
    for b in BEARD:
        if b.startswith(('clean-shaven', 'nearly', 'beardless')):
            out += [f'{_art(b)}, {x}' for x in S("with a defined jawline, with smooth even skin, with a faint shadow along the jaw, with a crisp neckline, freshly shaved, with a hint of stubble after a long day")]
            continue
        must_only = 'mustache' in b and not any(k in b for k in ('beard', 'goatee', 'and', 'chops', 'patch'))
        for x in BEARD_X:
            if must_only and any(k in x for k in ('chin', 'bottom', 'cheek', 'jaw', 'neckline', 'sideburn', 'connected', 'upper lip')): continue
            if consistent(f'{b} {x}'): out.append(f'{_art(b)}, {x}')
    return sample(out, 260, 'fh')
R['m_facial_hair'] = _fh
GRM = S("a barber-fresh edge-up along the hairline, a carefully lined-up beard edge, a clean skincare finish with a natural matte look, a faint sweat sheen from heat, a freshly shaved glossy jaw, a light concealer on small blemishes, a light stage powder to reduce shine, a post-workout flush with damp hair, a tidy mustache with waxed tips, a touch of lip balm, a well-kept barbered look with a crisp neckline, an unkempt hurried morning look, bare skin with no products at all, beard oil giving the beard a healthy sheen, clear nail polish on neat nails, a light hair product giving the hair texture, hair gel giving the hair a wet look, pomade slicking the hair, a splash of cologne-fresh look, moisturised skin with a soft finish, sunscreen leaving a faint white cast, a fresh shave with a tiny nick, hair still wet from a shower, a fresh haircut with visible clipper lines, neatly trimmed eyebrows, nose hair trimmed, neatly clipped nails, a signet ring and a watch, aftershave glow, a fresh lineup and a faded neckline")
GRM_X = S("in warm light, in cool light, in soft light, in harsh light, in the morning, in the evening, after a long day, before an event, at ease, with a confident look")
R['m_grooming'] = lambda o: sample(P('{0}, {1}', GRM, GRM_X), 250, 'grm') + GRM
CH = S("smooth chest, a light scattering of chest hair, a moderate natural covering of chest hair, a dense mat of chest hair, patchy chest hair, a thin line of hair along the sternum, chest hair spreading to the shoulders, a trimmed neat chest hair pattern, a freshly shaved chest, a hairless chest with a faint shadow of stubble, chest hair that is curly, chest hair that is straight, chest hair that is fine and soft, chest hair that is coarse, chest hair that tapers into the stomach")
CH_X = S("on a narrow chest, on a deep chest, on a lean chest, on a broad chest, on a soft chest, on a muscular chest, that is evenly spread, that is concentrated at the centre, that is concentrated at the sides, that is darker than the arm hair, that is lighter than the arm hair, that matches the beard")
R['m_body_chesthair'] = lambda o: sample(P('{0} {1}', CH, CH_X), 200, 'ch') if False else sample([f'{c}, {x}' for c in CH for x in CH_X], 200, 'ch')

# ---------------------------------------------------------------- hair types: coily/curly/wavy/straight patterns (used by hair_build through CURL_TYPE)
CURL_TYPE = {}
def _curl(adjs, forms, where, n, name):
    out = [f'{a} {f} {w}' for a in adjs for f in forms for w in where]
    return sample([o for o in out if consistent(o)], n, name)
CURL_TYPE['S'] = _curl(S("smooth, sleek, silky, fine, thick, heavy, glossy, flat, slightly bent, perfectly straight, naturally straight, soft, shiny, blunt, wispy, light"), S("straight hair, straight strands, a straight fall of hair, a smooth straight curtain of hair, straight hair with a natural fall"), S("from root to tip, with a gentle bend at the ends, with a slight flip at the ends, with a natural parting, with a slight lift at the crown, with a clean line at the ends, that hangs close to the head, that falls heavily past the shoulders, that stays flat against the head, that swings with movement, that holds a blunt edge"), 220, 'curlS')
CURL_TYPE['W'] = _curl(S("loose, soft, gentle, deep, wide, beachy, irregular, tousled, defined, flowing, relaxed, S-shaped, rippling, uneven, airy, tight-wave"), S("waves, wavy hair, a wavy pattern, waves with some body"), S("from the mid-lengths to the ends, from the roots, at the nape, in the front sections, throughout, with a few straight sections, with a few curls underneath, with a bit of frizz, with clear definition, with soft definition, that relax as the day goes on, that spring back when touched, that fall in broad bends, that form soft curves around the face"), 220, 'curlW')
CURL_TYPE['C'] = _curl(S("loose, tight, springy, bouncy, defined, big, small, uniform, mixed, spiral, corkscrew, ringlet, voluminous, soft, loosely coiled, airy"), S("curls, curly hair, a curl pattern, spiral curls, ringlet curls"), S("from root to tip, with a halo of frizz, with clear definition, with soft definition, that shrink up when dry, that stretch when wet, that clump into ringlets, that spring back when pulled, that bounce when moving, that are tighter at the crown, that are looser at the nape, that sit close to the head, that stand away from the head, with different curl sizes through the layers"), 220, 'curlC')
CURL_TYPE['K'] = _curl(S("tight, small, springy, dense, defined, soft, cottony, fine, coarse, zig-zag, z-pattern, shrunken, stretched, voluminous, compact, airy"), S("coils, coily hair, kinky coils, a coil pattern, tight coils, afro-textured hair"), S("from root to tip, with strong shrinkage, with clear definition, with soft definition, that stretch when wet, that spring back, that sit in tight clusters, that stand away from the head, that form a rounded shape, that clump together, that look longer when stretched, that catch the light along each coil, with a cotton-soft feel, with a springy bounce"), 220, 'curlK')


# ---------------------------------------------------------------- extra coily-hair hairstyles (used by hair_model.KCAT / KCAT_M)
K_LEN = S("short, chin-length, shoulder-length, collarbone-length, mid-back-length, waist-length")
K_ST_F = S("box braids, knotless braids, goddess braids, feed-in braids, cornrows, patterned cornrows, twists, passion twists, Senegalese twists, flat twists, a twist-out, a braid-out, locs, faux locs, a natural afro, a tapered afro, a high puff, a low puff, Bantu knots, two-strand twists, crochet braids, fulani braids, a silk press, a wash-and-go")
K_FIN_F = S("worn loose, pulled into a high bun, tied back in a low ponytail, worn half up, decorated with beads, decorated with cuffs, pinned up in a crown, wrapped with a silk scarf, held back by a headband, with sculpted edges, with a deep side part, with a center part, parted in a zigzag, tucked behind the ears, swept to one side")
K_FADE = S("a low fade, a mid fade, a high-top fade, a taper fade, a drop fade, a temple fade, a skin fade, a burst fade, a bald fade")
K_TOP = S("a sponge-twist top, a curly coil top, a twist-out top, defined coils on top, a textured crop top, a flat top, a 360 wave pattern, a faux-hawk of twists, short twists on top, a freeform top, a sharp lineup, a hard part, a shaped part, a dyed-tip top")
def k_styles(g):
    rng = random.Random(seed_of('kstyles' + g))
    if g == 'f':
        out = [f'{l} {s} {f}' for l in K_LEN for s in K_ST_F for f in K_FIN_F]
        out = [o for o in out if not ('short' in o and 'waist' in o) and not (o.startswith('short') and ('bun' in o) and 'locs' in o)]
    else:
        out = [f'{f} with {t}' for f in K_FADE for t in K_TOP] + [f'{l} {s} {fi}' for l in K_LEN for s in S("box braids, cornrows, twists, locs, two-strand twists, a twist-out, a braid-out, a natural afro, a tapered afro, freeform locs, dreadlocks") for fi in S("worn loose, tied back, pulled into a bun, half up, with beads, with sculpted edges, with a deep side part, with a center part, tucked behind the ears")]
    out = sample(out, 260, 'kst' + g)
    return [(o, 0.45, ('flat',)) for o in out]
