"""Adult-sized onesies (onesie_*): every uniform, costume and cosplay archetype in uniform_data as a full-body one-piece suit.
Three modes:
  printed  a fitted jersey onesie covered edge to edge in a flat print of the outfit (the trompe-l'oeil genre, like the printed tees)
  plush    a soft three-dimensional onesie built from real layers of fabric and fabric-like materials (felt, fleece, minky, faux fur, quilting, faux leather, foam padding)
  hybrid   a printed onesie with raised plush layers (collars, pockets, belts, badges) sewn on top
Files: onesie_<mode>[_<group>][_<male|female|sexy_male|sexy_female>], onesie_<mode>_back_<group> (printed), onesie_<mode>_random, onesie, onesie_gendered,
       onesie_tone[_<tone>][_<version>] (mixed modes, skin tone fixed), onesie_random (any mode, version, tone),
       parts: onesie_type onesie_feet onesie_fabric onesie_fabric_odd onesie_layer onesie_plush_note onesie_printed_note onesie_style
Adult people only; every line says adult-sized.  Original wording, deterministic."""
import os, sys, re, shutil
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from paths import FINAL
import uniform_build as ub
from uniform_build import U, rows, variant, rg, art, cap, join, sleeves, armpart, sheer, skinbits, STYLE, SKINBITS, NOFIG, HANDS, PRINTLOW, PRINTHEAD, VLABEL, SKIN

SHORTLEG = re.compile(r"shorts|kilt|skirt|bloomers|swim|trunks|leotard|tutu|loincloth|mini|culottes|lederhosen|pantaloons|hot pants|boy-?shorts|speedo|briefs", re.I)
def legs(r): return 'short' if SHORTLEG.search(r['lo'] or '') else 'long'

FEATURE = ["zip-front", "hooded zip-front", "button-front union-suit style", "snap-front", "pull-on stretch", "shawl-collar zip-front", "drop-hood zip-front", "crew-neck pull-on", "double-zip", "henley-placket"]
FEET = ["footed with built-in soles", "footless with elasticated ankle cuffs", "with built-in slipper feet", "with grippy sock-style feet", "with sewn-in bootie feet"]
FEET_SHORT = ["with bare calves and ankles", "with elasticated knee-length leg openings"]
JERSEY = ["soft cotton jersey", "stretch cotton-blend jersey", "brushed fleece", "waffle-knit cotton", "velour", "thermal knit", "bamboo-blend jersey", "French terry", "lightweight performance knit", "ribbed knit"]
SL_LONG, SL_SHORT = "long-sleeved", "short-sleeved"
LG_LONG = ["full-length-legged", "long-legged", "ankle-length"]
LG_SHORT = ["short-legged romper-style", "shorts-length", "knee-length"]
ADULT = ["adult-sized", "grown-up-sized", "roomy adult-sized", "straight-cut adult-sized", "slightly oversized adult-sized", "easy-fitting adult-sized"]

FABRIC = ["felt", "fleece", "minky plush", "faux fur", "sherpa", "velour", "quilted padding", "brushed flannel", "terry cloth", "corduroy", "satin", "faux suede", "faux leather", "vinyl-look fabric", "mesh", "tulle", "canvas", "wool-blend suiting", "polar fleece", "chenille", "velvet", "denim", "knit jersey", "padded foam sheet", "metallic lamé", "sequin fabric", "organza", "ribbed knit", "cotton twill", "crushed velvet", "boucle", "plush towelling"]
FABRIC_ODD = ["foam-padded pleather", "glow-in-the-dark fabric", "holographic foil fabric", "flocked velour", "reflective tape fabric", "fuzzy pom-pom fringe", "stuffed quilted nylon", "neoprene", "fluffy shag pile", "puffer-jacket quilting", "tinsel fringe", "heat-embossed vinyl", "rubberised cloth", "chunky cable knit", "sculpted EVA foam covered in fabric", "crocheted yarn", "patchwork of mixed scraps"]
LAYER = ["Layers of different fabrics are cut, stacked and sewn on top of each other, so lapels, collars, pockets, belts and badges stand out in soft relief.", "Each part of the outfit is its own separate piece of fabric sewn onto a padded base, giving a stuffed, three-dimensional look.", "The outfit is built up in overlapping layers: a soft padded body, appliqué panels sewn over it, and raised stitched trims on top.", "Quilted padding gives the shoulders, chest and thighs a gentle puffiness, with the outfit's details sewn on as raised fabric shapes.", "Fabric shapes are stuffed lightly and stitched down so buttons, badges, pockets and straps puff out from the surface.", "Soft sculpted layers imitate the outfit's garments: folded collars, rolled cuffs, belts and panels are real pieces of cloth, stacked over one another."]
PL_NOTE = ["It is a cuddly, three-dimensional costume version of the outfit, with visible stitching, soft folds and a slightly puffy look, but still clearly a one-piece onesie.", "The whole suit looks like a plush stuffed-toy version of the uniform, made for an adult to lounge or party in.", "Every detail is real soft fabric with depth and texture, not a flat picture: seams, pockets, buttons and trims are all sewn on.", "It reads as a soft sculpture of the outfit worn as pyjama-style loungewear, comfortable, padded and fully three-dimensional."]
PR_NOTE = ["The onesie is a flat-printed illusion: the outfit appears on a plain stretch jersey suit with no real collars, belts or pockets.", "It is a trompe-l'oeil onesie, a plain one-piece suit pretending to be the outfit through printing alone.", "The print runs continuously across the front, back, sleeves, legs and hood without a break at the seams.", "Printed shadows and fold lines suggest the garments, but the suit itself is smooth, flat and uniform in material."]
HY_NOTE = ["The print gives the whole outfit, and raised layers of soft fabric are sewn on over it for the collar, pockets, belt, buttons and badges, so the suit is half picture and half sculpture.", "A printed base shows the full outfit, while felt, fleece and faux-leather pieces are stitched over the key details to give them real depth.", "Printed and plush together: the outfit is printed all over, with padded appliqué parts standing out from the surface."]
PR_FILL = ["The print covers every part of the onesie edge to edge: body, sleeves and legs, and the hood, gloves and feet wherever the suit has them, with no plain fabric showing except the zip and a ribbed cuff or two.", "The outfit's design is wrapped around the entire suit as one continuous print from the collar to the ankles, wrapping around the sides to the back.", "No blank jersey shows: the printed outfit runs from the neckline down the arms and legs to the cuffs, and over the hood if there is one.", "The whole suit is the outfit: front, back, arms and legs (and any hood, gloves or feet) are printed as the matching parts of it, with the seams and the zip hidden in the pattern."]
PR_BACK = ["The back of the suit shows the matching back of the outfit, printed edge to edge, from the collar or hood to the ankles or feet.", "Turn it round and the back carries the rear of the outfit, with nothing left plain.", "Front and back are both fully printed, the back showing how the outfit looks from behind."]
PR_CLEAN = ["No background colour or plain jersey shows around the print, on the shoulders, sleeves or legs.", "The outfit's own cloth reaches every seam, cuff and hem with no border or backdrop.", "There is no separate background: the print is cut to the onesie's shape."]
PR_ARMS = ["The arms hang straight down in the sleeves and no arm or hand crosses the front of the body.", "Arms are printed only along the sleeves, and the front is one unbroken panel."]
PR_SIL = ["The outline is exactly a onesie's: nothing sticks out past the suit's edges, and no coat tails, skirts, capes, extra sleeves or loose layers hang outside it.", "The silhouette is a plain one-piece suit, with every part of the outfit printed inside its shape and none beyond it."]
OSTYLE = [x.replace('looks like a real photograph of the outfit', "shows the outfit's cloth in lifelike detail").replace('a lifelike photographic full-coverage print', 'a lifelike full-coverage print of the cloth') for x in STYLE]
PR_TUBE = ["Every sleeve and every leg of the suit is a tube covered completely, all the way round, in the outfit's cloth for that limb (sleeve cloth, trouser, tights or leg fabric), so no grey, blue or coloured background shows on the arms, legs, sides or back.", "The outfit's cloth wraps the whole suit like a pattern: the body, the outside and inside of each sleeve and each leg, and the sides, so there are no plain coloured side panels or background patches anywhere.", "The print is applied to the suit's own pattern pieces: front, back, each sleeve and each leg are fully covered in the matching cloth of the outfit, with no leftover background colour between them."]
PR_BARE = ["Where the outfit leaves arms or legs bare, the suit itself is cut sleeveless, short-sleeved or short-legged at that point, so the wearer's own limbs show; no printed arm, leg, hand, foot or skin appears on the suit's fabric.", "No limbs are printed on the suit: bare arms and legs are never drawn as skin on the fabric, and the suit is simply cut short or sleeveless wherever the outfit would show them.", "There are no printed arms, hands, fingers, legs or feet and no printed skin on the suit, except a small printed neckline detail where the outfit is open."]
PR_NOFIG = ["The hood carries only hood cloth: no face, hair, ears or head is printed on it, and no crowd, audience, stage, lights or scene appears anywhere on the suit, only the outfit's own cloth.", "It is not a drawing of a person standing in the middle of the suit: no body, no head, no limbs and no figure are pictured, only the outfit's cloth, trims and fastenings spread over the whole suit.", "No standing figure, torso, arms or legs are depicted; the suit's own shape is the body, and the print is only the outfit's fabric covering it from edge to edge."]
PR_FLAT = ["Everything is flat ink on opaque stretch jersey: lace, fur, metal, leather and sequins are printed patterns, never real raised or see-through material.", "The suit is solid and opaque and nothing is real but the jersey: textures and sheens are printed pictures only."]
PR_SHEER = ["Wherever the outfit is sheer, lace, mesh or net, the print includes {skin} underneath, printed flat on opaque jersey so it reads as skin seen through the material, with no real transparency.", "The sheer parts of the outfit are printed over {skin}, all flat ink on opaque jersey."]
PR_ARM = ["The outfit has {part} on the forearm and wrist, so the onesie's sleeves run to the wrist and the printed {part} sit at the sleeve ends, with nothing beyond the cuffs.", "To show the {part} on the forearms, the sleeves are long and the printed {part} appear on them, ending at the wrist hems."]
PL_ARM = ["The outfit has {part} on the forearm and wrist, shown as separate sewn-on fabric pieces at the ends of long sleeves.", "At the wrists, the {part} are made from layered fabric stitched onto the end of each long sleeve."]
PL_SKIN = ["Only the face and hands show skin, in {skin}, with the neckline zipped to show a little chest or collarbone.", "Skin shows at the face, hands and the open neckline, in {skin}.", "Bare {skin} appears only at the face, hands and a partly open zip."]
PL_BODY = ["The top half is {up}, built from stacked pieces of {m1} and {m2} sewn over a padded base of {m3}.", "On the body it is {up}, made of {m1} layered with {m2}, with details in {m3}.", "The chest and sleeves form {up}, cut from {m1}, {m2} and {m3}."]
PL_LOW = ["The legs are {lo}, made from {m}.", "The lower half is shaped as {lo} in {m}.", "The trouser or skirt legs are {lo}, sewn in {m}."]
PL_HEAD = ["The hood is shaped and padded to look like {he}, made from {m}.", "A sewn-on hood is built as {he} in {m}.", "The hood is a soft sculpted version of {he}, in {m}."]
PL_FEET = ["The feet are plush padded versions of {fe}.", "Built-in soft feet are shaped as {fe}.", "The feet are sewn as {fe}, in soft padded fabric."]
PL_CARRY = ["A soft stuffed version of {ca} is sewn onto the hip.", "A padded fabric replica of {ca} hangs from the belt.", "A plush {ca} is attached at the side with a loop of fabric."]
HY_LAYERS = ["collar and lapels", "pockets", "belt and buckle", "buttons", "badges and patches", "epaulettes", "cuffs", "hood trim", "medals and ribbons", "straps and holsters"]
HY_MAT = ["felt", "fleece", "faux leather", "faux fur", "quilted padding", "chenille", "velvet"]
TONES = {'very_deep_brown': 'very deep brown', 'deep_brown': 'deep brown', 'mid_brown_tan': 'mid-tone brown tanned', 'golden_olive': 'golden olive', 'light_tan': 'light tan', 'fair_pale': 'fair and pale'}
MODES = ['printed', 'plush', 'hybrid']
MODES_ALL = MODES + ['bodysuit', 'shortie', 'romper', 'leisure', 'sewn_onesie', 'sewn_romper', 'sewn_leisure', 'sewn_bodysuit']

FEATURE_HOOD = ["hooded zip-front", "drop-hood zip-front", "hooded pull-on", "hooded snap-front", "hooded double-zip"]
FEATURE_NOHOOD = ["zip-front", "button-front union-suit style", "snap-front", "pull-on stretch", "shawl-collar zip-front", "crew-neck pull-on", "double-zip", "henley-placket"]
HOOD_YES = ["with an attached hood", "with a big attached hood", "with a deep attached hood"]
HOOD_NO = ["hoodless, with a ribbed collar", "with no hood and a plain collar", "with no hood, just a neckline and collar"]
GLOVE_YES = ["with attached gloves sewn into the sleeves", "with attached fold-over mitten cuffs", "with built-in gloves at the sleeve ends"]
GLOVE_NO = ["with plain ribbed cuffs and no gloves", "with simple wrist cuffs and no attached gloves", "with open cuffs and bare hands"]
FEET_YES = ["footed with built-in soles", "with built-in slipper feet", "with grippy sock-style feet", "with sewn-in bootie feet"]
FEET_NO = ["footless with elasticated ankle cuffs", "footless, ending in plain ankle cuffs with bare feet", "footless with stirrup-free ankle hems"]
GLV = __import__('re').compile(r"glove|gauntlet|mitten|mitt", __import__('re').I)
CREAT = re.compile(r"\b(animal|creature|dragon|unicorn|beast|monster|mascot|bear|cat|dog|wolf|fox|rabbit|bunny|bird|owl|insect|bug|moth|dinosaur|werewolf|pegasus|griffin|phoenix|yeti|alien|imp|demon|devil|fairy|elf|goblin|troll|ogre|mermaid|lion|tiger|horse|centaur|gargoyle|fish|shark|frog)\b", re.I)
def suit(r, R, plush=False):
    sk, sph, snote = ub.sleeve_style(r); sl = sk if sk in ('long', 'short') else 'cut'; lg = legs(r)
    sleeve = SL_LONG if sl == 'long' else SL_SHORT if sl == 'short' else sph
    leg = R.choice(LG_LONG if lg == 'long' else LG_SHORT)
    hood = True if (r['he'] or CREAT.search(r['name'])) else R.random() < .3
    gl = R.random() < (.85 if GLV.search(r['up'] + ' ' + r['ca']) else .3) and sl in ('long', 'cut')
    ft = lg == 'long' and R.random() < (.65 if r['fe'] else .4)
    feet = R.choice(FEET_YES if ft else FEET_NO) if lg == 'long' else R.choice(FEET_SHORT)
    base = R.choice(JERSEY) if not plush else R.choice(['soft fleece', 'plush minky', 'thick velour', 'padded fleece'])
    feat = R.choice(FEATURE_HOOD if hood else FEATURE_NOHOOD)
    d = f"{art(R.choice(ADULT))} {sleeve}, {leg}, {feat} onesie, {R.choice(HOOD_YES if hood else HOOD_NO)}, {R.choice(GLOVE_YES if gl else GLOVE_NO)}, and {feet}, in {base}"
    return d, sl, dict(hood=hood, gloves=gl, feet=ft)

def printed_line(r, seed, hybrid=False):
    r = ub.nobody(r); R = rg(seed, r['name'], 'ones-h' if hybrid else 'ones-p'); n = ub.tee_name(r['name']); s, sl, o = suit(r, R); ap = armpart(r)
    t = f"{cap(s)}, a real plain stretch suit and not a real garment, covered edge to edge in {R.choice(OSTYLE)}, designed to make the onesie look like the outfit of {art(n)}. {R.choice(PR_FILL)} The print shows {r['up']}"
    t += (f", {r['lo']}" if r['lo'] else '') + (f", with {r['he']} printed on the hood" if r['he'] and o['hood'] else ', with a plain hood printed in the outfit\'s colours' if o['hood'] else ', with no headwear shown because the suit has no hood' if r['he'] else '') + (f", {r['fe']} printed on the feet" if r['fe'] and o['feet'] else ', with the feet printed in the outfit\'s colours' if o['feet'] else ', with no footwear shown because the suit is footless' if r['fe'] else '') + (', and printed gloves on the attached gloves at the sleeve ends' if o['gloves'] else ', and the sleeves end in plain cuffs with no hands printed') + '.'
    if r.get('style') and ub.tee_style(r['style']): t += f" The outfit is {ub.tee_style(r['style'])}."
    snote = ub.sleeve_style(r)[2]; t += (' ' + snote if snote else '') + (R.choice(ub.ANGNOTE) if ub.sleeve_angle(r) else '') + f" {R.choice(PR_BACK)} {R.choice(PR_CLEAN)} {R.choice(PR_TUBE)} {R.choice(PR_BARE)} {R.choice(ub.NOBACK)} {R.choice(ub.EDGE).replace('shirt','suit')} {R.choice(PR_SIL)} {R.choice(ub.FULLSHAPE).replace('T-shirt','suit').replace('shirt','suit')} {R.choice(PR_FLAT) if not hybrid else 'The printed parts are flat ink on stretch jersey.'} {R.choice(PR_NOFIG)}"
    if skinbits(r, R): t += ' It may also show ' + R.choice(SKINBITS).format(skin='__uniform_tee_skin__') + ', all as flat ink.'
    if ap: t += ' ' + R.choice(PR_ARM).format(part=ap)
    if sheer(r): t += ' ' + R.choice(PR_SHEER).format(skin='__uniform_tee_skin__')
    if r['lo'] and R.random() < .5: t += ' ' + R.choice(PRINTLOW).format(lo=r['lo']).capitalize() + '.'
    if hybrid:
        parts = R.sample(HY_LAYERS, 3); mats = R.sample(HY_MAT, 3)
        t += ' ' + f"Raised plush layers are sewn on over the print: the {parts[0]} in {mats[0]}, the {parts[1]} in {mats[1]} and the {parts[2]} in {mats[2]}, standing out from the surface. " + R.choice(HY_NOTE)
    else: t += ' ' + R.choice(PR_NOTE)
    return t

def plush_line(r, seed):
    r = ub.nobody(r); R = rg(seed, r['name'], 'ones-l'); n = ub.tee_name(r['name']); s, sl, o = suit(r, R, True)
    fab = R.sample(FABRIC, 6); odd = R.random() < .3
    if odd: fab[5] = R.choice(FABRIC_ODD)
    t = f"{cap(s)}, made as a three-dimensional plush version of the outfit of {art(n)}, with real layers of fabric and fabric-like materials. "
    t += R.choice(PL_BODY).format(up=r['up'], m1=fab[0], m2=fab[1], m3=fab[2])
    if r['lo']: t += ' ' + R.choice(PL_LOW).format(lo=r['lo'], m=fab[3])
    if o['hood']: t += ' ' + (R.choice(PL_HEAD).format(he=r['he'], m=fab[4]) if r['he'] else f"The attached hood is a soft padded hood in {fab[4]}, in the outfit's colours.")
    elif r['he']: t += ' The suit has no hood, so the headwear is left off.'
    if o['feet']: t += ' ' + (R.choice(PL_FEET).format(fe=r['fe']) if r['fe'] else 'The built-in feet are soft padded feet in the outfit\'s colours.')
    elif r['fe']: t += ' The suit is footless, so the footwear is left off.'
    t += (" The attached gloves are padded fabric gloves in the outfit's trim colours, sewn onto the ends of the sleeves." if o['gloves'] else ' The sleeves end in plain cuffs, with bare hands showing.')
    if r['ca']: t += ' ' + R.choice(PL_CARRY).format(ca=re.sub(r'^(a|an|the|some) ', '', r['ca']))
    if r.get('style') and ub.tee_style(r['style']): t += f" The outfit is {ub.tee_style(r['style'])}."
    ap = armpart(r)
    if ap: t += ' ' + R.choice(PL_ARM).format(part=ap)
    snote = ub.sleeve_style(r)[2]
    if snote: t += ' ' + snote
    t += ' ' + R.choice(LAYER) + ' ' + R.choice(PL_SKIN).format(skin='__onesie_skin__') + ' ' + R.choice(PL_NOTE)
    return t


# ---- shirt-attached-to-bottoms modes: bodysuit tee (leotard cut) and shortie (romper tee with shorts) ----
BS_CUT = ["a high-cut leotard-style bottom with finished leg openings", "a classic leotard cut with smooth finished leg openings", "a boy-leg bodysuit bottom with hemmed leg openings", "a sleek bodysuit bottom with hemmed leg openings and a plain lined gusset"]
SH_CUT = ["short shorts ending at the upper thigh", "mid-thigh shorts", "fitted short shorts", "boxer-length shorts", "playsuit shorts ending above the knee"]
BS_NOTE = ["It is an adult bodysuit tee: a T-shirt top that flows seamlessly into a leotard-style bottom, all one piece of printed cloth.", "The top is the outfit and the bottom is a finished leotard-style cut, as in a printed adult dancewear bodysuit.", "A one-piece printed bodysuit with a T-shirt top and a smooth, hemmed, leotard-style bottom."]
SH_NOTE = ["It is a one-piece romper tee: a T-shirt top attached to matching shorts, with the outfit's top and bottom printed as one continuous piece.", "The top half shows the outfit's upper garment and the shorts show the outfit's lower garment cut to short-leg length, joined at the waist as one suit.", "A printed adult playsuit: shirt top and shorts in one piece, with the outfit's own cloth on both halves."]
BS_ALL = ["The outfit's cloth covers the whole piece in one continuous print, collar, shoulders, sleeves, body and leg openings all in the outfit's own colours and textures.", "Every part of the garment, from the collar band to the leg openings, is printed in the outfit's own cloth.", "The print is cut to the garment's exact shape, so the neck, shoulders, sleeves and leg openings are all covered in the outfit's own fabric."]
def bodysuit_line(r, seed, short=False):
    r = ub.nobody(r); R = rg(seed, r['name'], 'ones-s' if short else 'ones-b'); n = ub.tee_name(r['name'])
    sk, sph, snote = ub.sleeve_style(r); sl = sk if sk in ('long', 'short') else 'cut'
    sleeve = SL_LONG if sl == 'long' else SL_SHORT if sl == 'short' else sph
    neck = R.choice(['crew-neck', 'V-neck', 'scoop-neck', 'boat-neck', 'ringer-style', 'henley-placket'])
    cut = R.choice(SH_CUT if short else BS_CUT)
    t = f"{cap(art(R.choice(ADULT)))} {sleeve} {neck} printed {'romper tee' if short else 'bodysuit tee'} in {R.choice(JERSEY)}, a one-piece T-shirt top joined to {cut}, covered edge to edge in {R.choice(OSTYLE)}, designed to look like the outfit of {art(n)}. "
    t += f"{R.choice(PR_FILL_B)} The top shows {r['up']}"
    if short and r['lo']: t += f", and the shorts show {r['lo']} cut to short-leg length"
    elif r['lo'] and R.random() < .4: t += f", with a belt or waistband like {r['lo']} at the waist"
    t += '.'
    if r.get('style') and ub.tee_style(r['style']): t += f" The outfit is {ub.tee_style(r['style'])}."
    t += (' ' + snote if snote else '') + (R.choice(ub.ANGNOTE) if ub.sleeve_angle(r) else '') + (f" An attached hood at the neck is printed as {r['he']}." if r['he'] else '')
    t += f" {R.choice(PR_BACK)} {R.choice(BS_ALL)} {R.choice(ub.EDGE).replace('shirt', 'garment')} {R.choice(SH_NOTE if short else BS_NOTE)} {R.choice(ub.FLAT).replace('shirt', 'garment')} {R.choice(ub.NOFIG).replace('shirt', 'garment')}"
    ap = armpart(r)
    if skinbits(r, R): t += ' It may also show ' + R.choice(SKINBITS).format(skin='__uniform_tee_skin__') + ', all as flat ink.'
    if ap: t += ' ' + R.choice(PR_ARM).format(part=ap)
    if sheer(r): t += ' ' + R.choice(PR_SHEER).format(skin='__uniform_tee_skin__')
    return t
PR_FILL_B = ["The print covers every part of the garment edge to edge, from the neckline to the hem of the bottom.", "The outfit's design is wrapped around the entire piece as one continuous print, wrapping around the sides to the back.", "The whole garment is the outfit: front, back, sleeves and bottom printed as the matching parts of it."]

# ---- romper and one-piece zipper leisure suit modes (uniform print treatment) ----
from garment_wear_data import F as _GW
RO_STYLE = ["button-front", "tie-shoulder", "smocked-bodice", "halter-neck", "strapless", "wrap-front", "zip-front", "polo-collar", "camp-collar", "sailor-collar", "henley-placket", "square-neck", "one-shoulder", "ruffled", "utility-pocket", "drawstring-waist", "belted"]
RO_LEG = ["short shorts ending at the upper thigh", "mid-thigh shorts", "shorts ending just above the knee", "culotte-length legs ending at the knee", "balloon-leg shorts", "cuffed shorts", "wide-leg shorts", "bubble-hem shorts", "fitted knee-length legs"]
LE_STYLE = ["wide-collar", "pointed-collar", "stand-collar", "shawl-collar", "open-collar", "spread-collar", "zip-to-the-neck", "zip-to-the-sternum", "belted", "racing-stripe", "patch-pocket", "double-zip"]
LE_LEG = ["flared bell-bottom legs", "straight full-length legs", "tapered legs ending in ankle cuffs", "wide full-length legs", "slightly flared full-length legs", "full-length legs with hemmed ankles", "short leisure-suit legs ending above the knee"]
LE_NOTE = ["It is a one-piece zipper leisure suit: a single garment with a full-length front zipper, a collar, pockets, a waist and legs, made in one piece of printed cloth.", "A one-piece leisure jumpsuit with a zip front from collar to waist, the whole garment printed as the outfit.", "The suit is a single piece with a front zipper, a wide collar and a fitted waist seam, the print continuing from top to ankles."]
RO_NOTE = ["It is a one-piece adult romper: a top and shorts joined at the waist as one garment, printed as the outfit.", "A printed adult playsuit romper, the outfit's upper garment on top and its lower garment cut to short length below, all one piece of cloth.", "The romper is a single garment, top and shorts joined at the waist, in one continuous print."]
def suit2_line(r, seed, kind):
    r = ub.nobody(r); R = rg(seed, r['name'], 'ones-' + kind); n = ub.tee_name(r['name'])
    sk, sph, snote = ub.sleeve_style(r); sl = sk if sk in ('long', 'short') else 'cut'
    sleeve = SL_LONG if sl == 'long' else SL_SHORT if sl == 'short' else sph
    if kind == 'romper':
        mats = _GW['romper']['mats']; st = R.choice(RO_STYLE); leg = R.choice(RO_LEG); gname = 'romper'; note = RO_NOTE
    else:
        mats = _GW['leisure_onepiece']['mats']; st = R.choice(LE_STYLE); leg = R.choice(LE_LEG); gname = 'one-piece zipper leisure suit'; note = LE_NOTE
    t = f"{cap(art(R.choice(ADULT)))} {sleeve} {st} printed {gname} in {R.choice(mats)}, with {leg}, covered edge to edge in {R.choice(OSTYLE)}, designed to look like the outfit of {art(n)}. "
    t += f"{R.choice(PR_FILL_B)} The top shows {r['up']}"
    if r['lo']: t += f", and the {'shorts' if kind == 'romper' else 'legs'} show {r['lo']}" + (' cut to short-leg length' if kind == 'romper' or 'short' in leg else '')
    t += '.'
    if r.get('style') and ub.tee_style(r['style']): t += f" The outfit is {ub.tee_style(r['style'])}."
    t += (' ' + snote if snote else '') + (R.choice(ub.ANGNOTE) if ub.sleeve_angle(r) else '') + (f" An attached hood at the neck is printed as {r['he']}." if r['he'] else '')
    t += f" {R.choice(PR_BACK)} {R.choice(BS_ALL)} {R.choice(ub.EDGE).replace('shirt', 'garment')} {R.choice(note)} {R.choice(ub.FLAT).replace('shirt', 'garment')} {R.choice(ub.NOFIG).replace('shirt', 'garment')}"
    ap = armpart(r)
    if skinbits(r, R): t += ' It may also show ' + R.choice(SKINBITS).format(skin='__uniform_tee_skin__') + ', all as flat ink.'
    if ap: t += ' ' + R.choice(PR_ARM).format(part=ap)
    if sheer(r): t += ' ' + R.choice(PR_SHEER).format(skin='__uniform_tee_skin__')
    return t

# ---- sewn modes: the whole uniform made as a real fabric one-piece (no print) ----
ASSEMBLY = ["The garment is assembled from cut panels of fabric joined with visible seams, topstitching and piping, and it hangs as one coherent piece with every part in the outfit's own cloth.", "Every part is real fabric: panels cut, stitched together and finished with seam binding, with the outfit's details made as sewn pieces.", "It is tailored like a real garment, with proper seams, darts, hems and stitching lines, entirely in the outfit's own colours and cloths.", "The suit is built from layered fabric pieces sewn together, colour-blocked in the outfit's colours, with finished edges and neat stitching throughout."]
SW_TOP = ["The top half is built as {up}, cut from {m1} and {m2} in the outfit's colours, with a real sewn collar, real pockets, buttons or fastenings, and trims stitched on.", "The upper body is made as {up}, in {m1} with {m2} trims, every collar, lapel, strap and pocket a separate sewn piece.", "On the upper body it is {up}, sewn from {m1} and {m2}, with belts, badges and buttons attached as real pieces."]
SW_LOW = ["The lower half is made as {lo} in {m}, joined to the top as one piece.", "The legs are sewn as {lo} in {m}, continuing the same one-piece garment.", "{lo} forms the bottom half in {m}, stitched seamlessly into the top."]
SWKIND = {'onesie': 'onesie', 'romper': 'romper', 'leisure': 'one-piece zipper leisure suit', 'bodysuit': 'bodysuit'}
def sewn_line(r, seed, mode):
    kind = mode.split('_', 1)[1]; r = ub.nobody(r); R = rg(seed, r['name'], 'ones-' + mode); n = ub.tee_name(r['name'])
    fab = R.sample(FABRIC, 4); sk, sph, snote = ub.sleeve_style(r); sl = sk if sk in ('long', 'short') else 'cut'
    sleeve = SL_LONG if sl == 'long' else SL_SHORT if sl == 'short' else sph
    o = None
    if kind == 'onesie':
        d, _, o = suit(r, R, False); head = d
    elif kind == 'romper':
        head = f"{cap(art(R.choice(ADULT)))} {sleeve} {R.choice(RO_STYLE)} romper in {fab[3]}, with {R.choice(RO_LEG)}"
    elif kind == 'leisure':
        head = f"{cap(art(R.choice(ADULT)))} {sleeve} {R.choice(LE_STYLE)} one-piece zipper leisure suit in {fab[3]}, with {R.choice(LE_LEG)}"
    else:
        head = f"{cap(art(R.choice(ADULT)))} {sleeve} {R.choice(['crew-neck', 'V-neck', 'scoop-neck', 'boat-neck'])} bodysuit in {fab[3]}, with {R.choice(BS_CUT)}"
    t = f"{head}, sewn entirely from real fabric as a wearable version of the outfit of {art(n)}. "
    t += R.choice(SW_TOP).format(up=r['up'], m1=fab[0], m2=fab[1])
    if r['lo']: t += ' ' + R.choice(SW_LOW).format(lo=r['lo'], m=fab[2])
    if o:
        if o['hood']: t += ' ' + (f"The attached hood is sewn as {r['he']} in {fab[0]}." if r['he'] else f"The attached hood is made in {fab[0]}, in the outfit's colours.")
        elif r['he']: t += ' The suit has no hood, so the headwear is left off.'
        if o['feet']: t += ' ' + (f"The built-in feet are sewn as {r['fe']}." if r['fe'] else "The built-in feet are made in the outfit's colours.")
        elif r['fe']: t += ' The suit is footless, so the footwear is left off.'
        t += (" The attached gloves are sewn from fabric in the outfit's trim colours." if o['gloves'] else ' The sleeves end in plain finished cuffs.')
    if r.get('style') and ub.tee_style(r['style']): t += f" The outfit is {ub.tee_style(r['style'])}."
    if kind != 'onesie' and r['he']: t += f" An attached hood at the neck is sewn as {r['he']} in {fab[0]}."
    t += (' ' + snote if snote else '') + (R.choice(ub.ANGNOTE) if ub.sleeve_angle(r) else '')
    ap = armpart(r)
    if ap: t += f" The {ap} are sewn on as fabric pieces at the ends of the sleeves."
    if sheer(r): t += " The sheer parts of the outfit are real sheer lace, net or mesh sewn over a lining in __onesie_skin__."
    if r['ca']: t += f" A fabric version of {re.sub(r'^(a|an|the|some) ', '', r['ca'])} is stitched onto the suit."
    t += ' ' + R.choice(ASSEMBLY) + ' ' + R.choice(ub.FULLSHAPE).replace('T-shirt', 'garment').replace('shirt', 'garment')
    return t

# ---- creature onesies: always hooded, always with the features that identify the creature ----
import creature_data as CD
CRFAB = ["plush fleece", "soft minky", "faux fur", "velour", "sherpa fleece", "fuzzy flannel fleece", "brushed plush", "cosy terry fleece"]
CRFAB_SCALE = ["glossy scale-pattern fabric", "sequinned scale fabric", "shimmering scaled velvet", "embossed scale-textured velour"]
SCALEY = re.compile(r"dragon|snake|crocodile|alligator|lizard|gecko|iguana|chameleon|fish|shark|mermaid|naga|basilisk|wyvern|komodo|pufferfish|goldfish|clownfish|seahorse|kraken|nessie", re.I)
CR_HOOD = ["The attached hood is shaped as the creature's head, with {hood}.", "The hood forms the creature's head, complete with {hood}.", "A deep attached hood is sewn as the creature's head, with {hood}."]
CR_BODY = ["The body carries {body}.", "On the suit you also see {body}.", "The suit is finished with {body}."]
CR_LIMB = ["It ends in {limb}.", "Hands and feet are made as {limb}.", "The sleeves and legs finish as {limb}."]
CR_ID = ["The creature is instantly recognisable as {art}, from the hood's shape and the sewn-on features.", "Every feature is sewn on in real fabric so the {name} costume reads clearly as a {name} from any angle.", "The hood, tail and body details together make it unmistakably {art}."]
CR_END = ["It is a cosy adult animal-costume onesie with a zip front, made entirely of sewn fabric.", "A full-body adult costume onesie, stitched from layered fabric panels, comfortable and playful.", "It is a real fabric costume onesie for an adult, assembled from sewn panels with neat seams."]
def creature_lines(cls, row, k=6):
    name, cols, hood, body, limb = row; cols = [c.strip() for c in cols.split(',')]; out = set(); R = rg('creature', name)
    for i in range(k):
        R2 = rg('creature', name, i); col = cols[i % len(cols)]
        fab = R2.choice(CRFAB_SCALE if SCALEY.search(name) else CRFAB)
        t = f"{cap(art(R2.choice(ADULT)))} {R2.choice([SL_LONG, SL_LONG, SL_LONG, SL_SHORT])}, {R2.choice(LG_LONG)}, hooded zip-front animal-costume onesie in {col} {fab}, made as {art(col + ' ' + name) if not col.startswith(('all',)) else art(name)}. "
        t += R2.choice(CR_HOOD).format(hood=hood) + ' ' + R2.choice(CR_BODY).format(body=body) + ' ' + R2.choice(CR_LIMB).format(limb=limb) + ' '
        t += R2.choice(CR_ID).format(art=art(name), name=name) + ' ' + R2.choice(CR_END)
        t += ' ' + embellish(R2, 'sewn') + ' Extra creature details include a stitched-on nose, embroidered eyes and a tufted tail.'
        out.add(t)
    return sorted(out)


# ---- novelty embellishment: fun, visual and tactile details added to every onesie ----
EMB_TEX = ["chunky pom-pom trim along the hood edge and cuffs", "faux-fur cuffs and collar", "quilted puffy panels on the chest", "soft chenille patches", "terry-loop textured stripes", "ruffled fabric frills along the seams", "fluffy sherpa patches at the elbows and knees", "knitted rib panels with raised cable texture", "velvety flocked appliqué shapes", "tufted boucle accents", "padded 3D patch pockets", "scalloped felt edging", "corduroy ridged panels", "satin ribbon bows and piping", "dangling fabric tassels on the zip pull and hood", "braided cord drawstrings with knotted ends"]
EMB_SHINE = ["rows of sequins sewn in swirling patterns", "metallic foil-print accents that catch the light", "glitter-flecked tulle layered at the hem", "holographic appliqué badges", "glow-in-the-dark stitched details", "iridescent shimmer-mesh overlays", "mirrored sequin stars and shapes", "beaded fringe along the hem", "rhinestone buttons down the front", "gold-tone and silver-tone zipper pulls shaped like charms", "lurex-thread embroidery", "enamel-style pins and patches"]
EMB_FUN = ["oversized novelty buttons in contrasting colours", "embroidered badges and crests with stitched lettering", "a stuffed 3D tail or accent piece that sticks out", "layered ruffle cape-like shoulders", "puffy padded shoulder pieces", "dangling jingle bells and charms", "hand-stitched patchwork appliqué in bright colours", "contrast panels in clashing, playful colours", "fabric flames, stars or stripes sewn along the sleeves and legs", "a quilted belt-like waist band with a big buckle shape", "pocket flaps and straps added just for fun", "a bold embroidered emblem across the chest", "a rainbow of rickrack, ribbon and braid trim", "mismatched sleeves and legs in different textures", "fuzzy pom-pom fringe down the back"]
EMB_END = ["It is a novelty costume garment, made to be bright, playful, over-the-top and a pleasure to touch.", "Everything is chosen to be fun to look at and tactile to feel: bumpy, fluffy, shiny and soft in turn.", "The embellishments are sewn on as real raised fabric, so the suit has depth, texture and sparkle from every angle.", "It reads as a joyful, exaggerated novelty onesie, stuffed with texture and detail."]
EMB_PRINT = ['a chunky pom-pom zipper pull', 'contrast-colour ribbed cuffs and ankle bands', 'a fluffy pom-pom at the tip of the hood', 'bright contrast piping along the outer seams only', 'a large metallic zipper with a charm pull', 'a fleece-lined hood interior in a bright colour', 'soft terry-loop cuff trim', 'a ruffled neck frill', 'glittery elastic cuffs', 'a fuzzy collar edge']
def embellish(R, mode, costume=False):
    if costume and mode != 'printed':
        pk = R.sample(EMB_TEX[:2] + EMB_TEX[2:4] + EMB_TEX[4:6] + EMB_SHINE[:4] + ['oversized novelty buttons in contrasting colours', 'fuzzy pom-pom fringe down the back', 'a stuffed 3D accent piece that sticks out'], 3)
        return f"Novelty embellishments: {', '.join(pk[:-1])} and {pk[-1]}. {R.choice(EMB_END)}"
    n = 3 if mode in ('plush', 'hybrid') or mode.startswith('sewn') else 2
    pool = R.sample(EMB_TEX, 2) + R.sample(EMB_SHINE, 1) + R.sample(EMB_FUN, 1)
    if mode == 'printed':
        pr = R.sample(EMB_PRINT, 3)
        return f"Sewn-on novelty extras, kept to the edges so the print stays unbroken: {', '.join(pr[:-1])} and {pr[-1]}. It is a bright, playful novelty onesie that is fun to touch."
    pick = R.sample(pool, n + (1 if mode in ('plush', 'hybrid') else 0) if mode != 'printed' else 2)
    return f"Novelty embellishments: {', '.join(pick[:-1])} and {pick[-1]}. {R.choice(EMB_END)}"

# ---- object / food / mascot costume rows: the onesie IS the costume, not the outfit of someone wearing it ----
COST_NAME = re.compile(r"costume wearer|mascot|costume$", re.I)
COST_UP = re.compile(r"\b(foam|inflatable|plush|furry|padded|rubber)\b.*\bsuit\b|\bcostume\b|^an? (\w+ )?swimsuit\b", re.I)
def costume_row(r): return bool(COST_NAME.search(r['name']) or COST_UP.search(r['up'] or ''))
def costume_subject(r):
    m = re.match(r"^an? ((?:\w+ )?swimsuit)\b", r['up'] or '')
    if m: return m.group(1)
    n = re.sub(r"\b(costume wearer|costume|wearer|character|human|giant|inflatable|walking|seller|sports team|town)\b", '', r['name'], flags=re.I)
    n = re.sub(r"\s+", ' ', n).strip(' -')
    return n or re.sub(r"^(a|an) ", '', r['up'])
CO_FAB = {'plush': ["soft plush minky", "fluffy faux fur", "thick velour", "padded fleece"], 'sewn': ["soft padded fleece", "plush minky", "quilted jersey", "brushed fleece"], 'hybrid': ["stretch jersey with raised plush panels", "soft jersey with sewn plush layers"], 'printed': ["stretch jersey"]}
CO_SHAPE = ["The whole onesie is shaped and coloured as the {sub} itself: the body is the {sub}, with its true shape, colours and surface details sewn on in padded fabric.", "From head to toe the onesie is the {sub}: the hood forms the top or head of the {sub} and the body carries its main shape, colours and markings.", "It is a plush novelty costume of the {sub}, with the {sub}'s recognisable parts, colours and textures built from layered fabric, filling the whole suit."]
CO_SPEC = ["The costume idea is {up}, turned into a soft onesie.", "The design follows {up}, but as a cosy plush onesie.", "It takes {up} and makes it a squishy wearable onesie."]
CO_END = ["There is no separate jacket, vest, belt, uniform or accessories: the {sub} costume is the entire onesie, with only a zip, hood, small details and the sewn-on features that make the {sub} readable at a glance.", "Nothing is added that a {sub} would not have; it is one soft, simple, instantly readable {sub} onesie.", "It reads from across a room as a {sub}, with large simple shapes, clear colours and exaggerated, funny proportions."]
def costume_line(r, seed, mode):
    R = rg(seed, r['name'], 'cost-' + mode); sub = costume_subject(r); m = 'sewn' if mode.startswith('sewn') else mode
    sk, sph, _ = ub.sleeve_style(r)
    t = f"{cap(art(R.choice(ADULT)))} {R.choice([SL_LONG, SL_LONG, SL_SHORT])}, {R.choice(LG_LONG)}, hooded zip-front novelty costume onesie in {R.choice(CO_FAB[m])}, made as {art(sub)} costume. "
    t += R.choice(CO_SHAPE).format(sub=sub) + ' ' + R.choice(CO_SPEC).format(up=r['up'] or art(sub))
    if r['he']: t += f" The hood adds {r['he']}."
    if r['fe'] and 'bare' not in r['fe']: t += f" The feet are made as {r['fe']}."
    if mode == 'printed': t += ' The whole suit is covered edge to edge in a flat print of the ' + sub + ' costume, with no figure pictured and no background.'
    elif mode == 'hybrid': t += ' Printed colours form the base and raised plush shapes are sewn over them.'
    t += ' ' + R.choice(CO_END).format(sub=sub)
    return t

CMP = ["It is a complete costume of {n} in one piece, shown full length from collar to ankles: {parts}. The upper half carries the top and the leg tubes carry the lower garment, so the whole outfit reads at once.", "The suit is the whole {n} outfit, not just a top: {parts}. It is shown in full, from the neckline down to the ankle cuffs.", "A full {n} costume, head to toe in a single suit: {parts}. Nothing of the outfit is missing and the legs of the suit show the lower garment."]
def complete_note(r, R, mode):
    n = ub.tee_name(r['name']); parts = [r['up']]
    if r['lo']: parts.append(r['lo'] + ' on the legs')
    if r['he']: parts.append(r['he'] + ' (as the hood)')
    if r['fe']: parts.append(r['fe'] + ' (as the feet)')
    if r['ca']: parts.append(r['ca'] + ' sewn or attached to the suit')
    return R.choice(CMP).format(n=n, parts=', '.join(parts))

def lines(r, seed, k, mode):
    if costume_row(r) and mode in ('printed', 'plush', 'hybrid', 'sewn_onesie'):
        out = sorted({costume_line(r, f'{seed}{i}', mode) for i in range(k)}); return [o + ' ' + embellish(rg(seed, r['name'], 'emb', o[:40], mode), mode, True) for o in out]
    out = []
    for i in range(k):
        s = f'{seed}{i}'
        out.append(sewn_line(r, s, mode) if mode.startswith('sewn_') else printed_line(r, s) if mode == 'printed' else plush_line(r, s) if mode == 'plush' else bodysuit_line(r, s) if mode == 'bodysuit' else bodysuit_line(r, s, True) if mode == 'shortie' else suit2_line(r, s, mode) if mode in ('romper', 'leisure') else printed_line(r, s, True))
    out = [o + ' ' + complete_note(r, rg(seed, r['name'], 'cmp', o[:40]), mode) + ' ' + embellish(rg(seed, r['name'], 'emb', o[:40], mode), mode) for o in out]
    return sorted(set(out))

def back_lines(r, seed):
    R = rg(seed, r['name'], 'ones-b'); sl = sleeves(r['up'], r); lg = legs(r)
    return f"{cap(art(R.choice(ADULT)))} {SL_LONG if sl == 'long' else SL_SHORT}, {R.choice(LG_LONG if lg == 'long' else LG_SHORT)} onesie seen from behind, the whole back printed edge to edge with the back of the outfit of {art(ub.tee_name(r['name']))}: the back of {r['up']}{(', ' + r['lo']) if r['lo'] else ''}, running from the collar or hood over the shoulder blades and down the sleeves and legs. The front is not shown. It is a flat print on a plain stretch suit, with no background colour showing and no arm crossing the torso."

def run(final=FINAL):
    F = {}; G = list(U); VARS = list(VLABEL); ALLV = ['neutral'] + VARS
    K = {'printed': 3, 'plush': 3, 'hybrid': 3, 'bodysuit': 3, 'shortie': 3, 'romper': 3, 'leisure': 3, 'sewn_onesie': 3, 'sewn_romper': 3, 'sewn_leisure': 3, 'sewn_bodysuit': 3}; KV = 1
    for m in MODES_ALL:
        for g in G:
            F[f'onesie_{m}_{g}'] = sorted({l for r in rows(g) for l in lines(r, g, K[m], m)})
            for v in VARS:
                F[f'onesie_{m}_{g}_{v}'] = sorted({l for r in rows(g) for l in lines(variant(r, v), g + v, KV, m)})
        F[f'onesie_{m}'] = [f'__onesie_{m}_{g}__' for g in G]
        for v in VARS: F[f'onesie_{m}_{v}'] = [f'__onesie_{m}_{g}_{v}__' for g in G]
        F[f'onesie_{m}_random'] = [f'__onesie_{m}_{g}__' for g in G] + [f'__onesie_{m}_{v}__' for v in VARS]
    for cls, rows_ in CD.C.items(): F[f'onesie_creature_{cls}'] = sorted({l for row in rows_ for l in creature_lines(cls, row)})
    F['onesie_creature'] = [f'__onesie_creature_{c}__' for c in CD.C]; F['onesie_creature_random'] = [f'__onesie_creature_{c}__' for c in CD.C for _ in range(max(1, len(CD.C[c]) // 10))]
    F['onesie_creature_name'] = sorted({row[0] for v in CD.C.values() for row in v}); F['onesie_creature_features'] = sorted({x.strip() for v in CD.C.values() for row in v for x in row[2].split(',')})
    for g in G: F[f'onesie_printed_back_{g}'] = sorted({back_lines(r, g) for r in rows(g)})
    F['onesie_printed_back'] = [f'__onesie_printed_back_{g}__' for g in G]
    F['onesie'] = [f'__onesie_{m}__' for m in MODES_ALL] + ['__onesie_creature__']
    F['onesie_sewn'] = [f'__onesie_{m}__' for m in MODES_ALL if m.startswith('sewn_')]; F['onesie_sewn_random'] = [f'__onesie_{m}_{g}__' for m in MODES_ALL if m.startswith('sewn_') for g in G] + [f'__onesie_{m}_{v}__' for m in MODES_ALL if m.startswith('sewn_') for v in VARS]
    F['onesie_gendered'] = [f'__onesie_{m}_{v}__' for m in MODES_ALL for v in VARS]
    for tk, tn in TONES.items():
        for v in ALLV:
            ls = []
            for g in G:
                for r in rows(g):
                    r2 = r if v == 'neutral' else variant(r, v); m = rg(tk, v, r['name']).choice(MODES_ALL); l = lines(r2, g + v + tk, 1, m)[0]
                    l = l.replace('__uniform_tee_skin__', f'a flat printed {tn} skin tone').replace('__onesie_skin__', f'{tn} skin')
                    ls.append(l + (f" Any printed skin is in a flat printed {tn} skin tone." if m != 'plush' else f" Skin on the face and hands is {tn}."))
            F[f'onesie_tone_{tk}_{v}'] = sorted(set(ls))
        F[f'onesie_tone_{tk}'] = [f'__onesie_tone_{tk}_{v}__' for v in ALLV]
    F['onesie_tone'] = [f'__onesie_tone_{tk}__' for tk in TONES]
    F['onesie_random'] = [f'__onesie_tone_{tk}__' for tk in TONES for _ in range(2 if tk == 'mid_brown_tan' else 1)]
    F['onesie_skin'] = ['mid-tone brown tanned skin'] * 2 + ['warm mid-brown tanned skin', 'deep brown skin', 'very deep brown skin', 'golden olive skin', 'light tan skin', 'fair pale skin', 'rich medium-brown skin']
    F['onesie_type'] = [f"{art(a)} {s}, {l}, {f} onesie {ft}" for a in ADULT[:3] for s in (SL_LONG, SL_SHORT) for l in (LG_LONG[0], LG_SHORT[0]) for f in FEATURE[:5] for ft in FEET[:2]]
    F['onesie_feet'] = FEET_YES + FEET_NO + FEET_SHORT; F['onesie_hood'] = HOOD_YES + HOOD_NO; F['onesie_gloves'] = GLOVE_YES + GLOVE_NO; F['onesie_fabric'] = FABRIC; F['onesie_fabric_odd'] = FABRIC_ODD; F['onesie_layer'] = LAYER; F['onesie_fullshape'] = [x.replace('T-shirt','suit').replace('shirt','suit') for x in ub.FULLSHAPE]
    F['onesie_plush_note'] = PL_NOTE; F['onesie_printed_note'] = PR_NOTE; F['onesie_hybrid_note'] = HY_NOTE; F['onesie_style'] = OSTYLE; F['onesie_jersey'] = JERSEY; F['onesie_feature'] = FEATURE
    os.makedirs(final, exist_ok=True)
    for n, l in F.items():
        assert l and all(l) and not any(re.search(r'[{}|]', x) or re.match(r'\d+::', x) for x in l), (n, [x for x in l if re.search(r'[{}|]', x)][:1])
        open(os.path.join(final, n + '.txt'), 'w', encoding='utf8', newline='\n').write('\n'.join(l) + '\n')
    print('onesies:', len(F), 'files')
    return F

def export_aoo(out, prefix='aoo_'):
    import random, zlib
    tmp = os.path.join(out, '_o_tmp'); os.makedirs(tmp, exist_ok=True); F = run(tmp); shutil.rmtree(tmp)
    names = set(F); ref = re.compile(r'__([A-Za-z0-9_\-/]+)__'); n = 0
    for name, lines_ in F.items():
        keep = list(dict.fromkeys(l for l in lines_ if l.strip()))
        keep = [ref.sub(lambda m: '__' + prefix + m.group(1) + '__' if (m.group(1) in names or m.group(1) == 'uniform_tee_skin') else m.group(0), l) for l in keep]
        if not any('__' in l for l in keep): random.Random(zlib.crc32(name.encode())).shuffle(keep)
        open(os.path.join(out, prefix + name + '.txt'), 'w', encoding='utf8', newline='\n').write('\n'.join(keep) + '\n'); n += 1
    return n

if __name__ == '__main__':
    a = [x for x in sys.argv[1:] if os.path.isdir(x)]; run(os.path.abspath(a[0]) if a else FINAL)
