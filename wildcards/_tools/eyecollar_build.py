"""v39: fully described eyeglasses (acc_eyewear*) and collars (acc_collar*). Every form is explained by its parts, shape, material and fit, so the name never carries the meaning alone. Runs after bodypres_build / bondage_acc_build and overwrites their thin versions."""
import os, re, sys, random, zlib
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from paths import FINAL
def S(x): return [i.strip() for i in x.split(';') if i.strip()]
def RR(*k): return random.Random(zlib.crc32('|'.join(map(str, k)).encode()))
# ---------- EYEGLASSES: name | what it is | materials ----------
FR = [
("round wire-rimmed glasses","thin circular metal rims about the width of the eye socket, a slim wire bridge and thin straight arms ending in small curved tips","fine gold wire; silver wire; matte black wire; bronze wire; rose-gold wire"),
("thick square acetate glasses","chunky square rims moulded from glossy plastic, a broad keyhole bridge and wide flat arms with a metal core","black acetate; clear acetate; deep red acetate; navy acetate; olive acetate"),
("cat-eye glasses","rims that sweep up and outward into pointed upper outer corners, with a narrow bridge and slim arms joined high on the frame","black acetate; tortoiseshell acetate; burgundy acetate; ivory acetate; metal with a plastic brow"),
("aviator glasses","large teardrop-shaped lenses in thin metal rims, a double bridge bar across the nose and slim arms with curved ear tips","gold-toned metal; silver-toned metal; gunmetal metal; thin black metal"),
("browline glasses","a heavy plastic bar across the top of each lens that rises at the outer ends, with thin metal wire holding the lower half of the lens","black and gold; tortoiseshell and silver; navy and silver; grey and gunmetal"),
("oversized round glasses","very large circular lenses that cover much of the cheek and brow, in a rim of even thickness with a short bridge","black acetate; tortoiseshell acetate; clear acetate; thin gold metal"),
("rimless rectangular glasses","rectangular lenses held only by small screws at the bridge and temples, with no rim around the edge and slim arms","titanium; stainless steel; gold-toned metal"),
("tortoiseshell oval glasses","softly oval rims in mottled brown-and-amber plastic, a gently curved bridge and medium-width arms","tortoiseshell acetate; honey acetate; dark havana acetate"),
("half-rim glasses","a thin rim that runs along the top of each lens only, with a fine nylon thread holding the bottom edge","black metal; silver metal; brown metal"),
("hexagonal glasses","six-sided rims with flat edges and angled corners, a low bridge and slim arms","thin gold metal; black metal; silver metal; clear acetate"),
("butterfly glasses","wide rims that flare out and up at the outer corners like wings, deeper on the lower outer edge, with a short bridge","black acetate; tortoiseshell acetate; white acetate; metal with acetate trim"),
("wayfarer glasses","trapezoid rims that are wider across the top than the bottom, thick plastic fronts with angled corners and sturdy arms","black acetate; tortoiseshell acetate; matte grey acetate; crystal acetate"),
("angular geometric glasses","rims cut into sharp polygon shapes with straight edges and pointed corners, slim flat arms","black metal; matte gold metal; coloured acetate; clear acetate"),
("pince-nez","two small lenses joined by a springy bridge that pinches the nose, with no arms at all, often hanging from a fine cord or chain","gold-toned wire; silver wire; steel wire"),
("monocle","one round lens in a thin rim worn over a single eye, held by the brow and cheek or hung from a fine chain","gold-toned metal; silver-toned metal; black enamelled metal"),
("steampunk goggles","round lenses set in thick riveted metal rims with a leather strap that wraps the head, a metal nose bridge and small side shields","brass and leather; copper and leather; blackened steel and leather"),
("wraparound sport glasses","one curved lens or two joined lenses that bend around the sides of the face, with a lightweight frame and rubber grips on the arms","lightweight nylon; matte black plastic; coloured plastic"),
("shield visor glasses","a single large curved lens panel that spans both eyes in one piece, with short arms attached to its edges","clear polycarbonate; tinted polycarbonate; mirrored polycarbonate"),
("semi-rimless glasses","a rim along the top of each lens and part of the sides, with the lower edge left bare","titanium; steel; brown metal; black metal"),
("transparent plastic glasses","clear see-through plastic frames with a smooth glossy finish, medium-thick rims and a soft curved bridge","clear acetate; tinted clear acetate; smoky clear acetate"),
("neon-coloured glasses","brightly saturated plastic frames in thick rims with a smooth finish and flat arms","neon pink plastic; neon green plastic; neon yellow plastic; neon orange plastic"),
("double-bridge metal glasses","thin metal rims with two bars crossing the nose, one near the top of the lenses and one lower, and slim arms","gold-toned metal; silver-toned metal; brass; gunmetal"),
("chained cat-eye reading glasses","pointed cat-eye rims with a fine chain that runs from each arm and hangs round the back of the neck","black acetate; red acetate; tortoiseshell acetate; metal with beads"),
("narrow rectangular glasses","slim rectangular lenses much wider than tall, in thin rims with a low bridge","black metal; gunmetal; slim acetate; tortoiseshell acetate"),
("heart-shaped novelty glasses","rims moulded into hearts, with the point of each heart at the bottom and a short bridge","pink plastic; red plastic; glittery plastic; white plastic"),
("star-shaped novelty glasses","rims moulded into five-pointed stars, with the points reaching out past the edge of the lens","gold plastic; silver plastic; glittery plastic; pink plastic"),
("mirrored sunglasses","dark lenses with a reflective coating that works like a mirror from the outside, in a light frame","thin metal; black plastic; matte metal"),
("small round tinted glasses","small circular lenses in thin rims with a coloured tint, a fine bridge and slim arms","thin black metal; gold wire; silver wire"),
("ski goggles","a wide curved lens panel with a foam-lined frame and an elastic strap that runs around the head and over a helmet","soft flexible plastic; matte plastic"),
("swim goggles","two small moulded eye cups with soft silicone seals, a nose bridge and an adjustable strap that wraps the head","silicone and plastic; clear plastic"),
("welding goggles","round dark lenses in thick, heat-resistant rims with side vents and an elastic strap","blackened steel; heavy plastic"),
("clear safety glasses","a wrap-around clear lens in a lightweight frame with side shields and a snug bridge","clear polycarbonate; tinted polycarbonate"),
("red-and-cyan paper 3D glasses","a folded card frame holding one red and one cyan film lens, with thin card arms","card and coloured film"),
("opera glasses on a stick","two small magnifying lenses side by side in a mount held up to the eyes by a slim handle","gilded metal; mother-of-pearl; black enamel"),
("lorgnette","a pair of lenses joined by a fine bridge, held up on a slim handle that folds, often worn from a chain","silver-toned metal; gold-toned metal; tortoiseshell; enamel"),
("low-perched reading glasses","small lenses that sit low on the nose so the wearer looks over the top of them, in light frames","thin metal; thin acetate; wire"),
("half-moon reading glasses","narrow lenses cut into half-circles with the flat edge along the top, so the wearer can look over them","tortoiseshell acetate; gold wire; black acetate"),
("flip-up clip-on glasses","a tinted lens frame that clips on the front of ordinary glasses with a hinge so it can be lifted up","thin metal; plastic"),
("thick-lens magnifying glasses","visibly thick, rounded lenses that make the eyes look larger, in sturdy rims","heavy acetate; steel"),
("loupe glasses","a small round magnifying lens set into a pivoting mount in front of each eye, on a head-hugging frame","steel; black plastic"),
("blue-light-filter glasses","slightly yellow-tinged clear lenses in a lightweight modern frame","black acetate; tortoiseshell acetate; clear acetate; thin metal"),
("gradient-lens fashion glasses","lenses dark at the top and fading to clear at the bottom, in a fashion-forward frame","black acetate; tortoiseshell acetate; gold metal"),
("taped glasses","a cracked frame mended with a wrap of tape at the bridge, with a slightly crooked fit","black plastic; wire frame"),
("rhinestone vintage cat-eye glasses","upswept frames set along the outer corners with rows of small clear stones, with slim arms","black acetate; ivory acetate; tortoiseshell acetate; pink acetate"),
("1920s round tortoiseshell glasses","large perfectly round lenses in mottled brown frames, with a keyhole bridge and straight arms","tortoiseshell; horn; acetate"),
("1950s sharp cat-eye glasses","strongly upswept frames with pointed outer corners and tapering arms","black acetate; tortoiseshell; red acetate; ivory acetate"),
("1970s oversized aviator glasses","very large teardrop lenses with a thin frame, a double bridge and a slightly tinted gradient","gold-toned metal; silver-toned metal; brown metal"),
("1980s huge square glasses","very large squared-off lenses in thick frames with a straight top line","black acetate; clear acetate; coloured acetate"),
("1990s thin rectangular glasses","narrow rectangular lenses in very slim metal rims with a small bridge","silver metal; gold metal; titanium"),
("2000s tiny oval glasses","small oval lenses in thin frames that sit high on the nose","slim metal; slim acetate; coloured plastic"),
("bold thick-rimmed glasses","very thick, rounded rims in a solid colour with a keyhole bridge and wide flat arms","black acetate; cobalt acetate; deep green acetate; clear acetate"),
("pilot-style double-bridge glasses","slightly squared teardrop lenses with a metal double bridge and thin arms","gunmetal; gold-toned metal; matte black"),
("round John-Lennon-style glasses","small circular lenses in very thin metal rims, a fine nose bridge and thin arms","fine gold wire; fine silver wire; thin black metal"),
("hinged folding glasses","a slim frame with a hinged bridge so that the whole thing folds in half for a small case","thin metal; plastic"),
]
LENS = [
("clear lenses","completely transparent lenses with no tint"),
("light grey-tinted lenses","a pale grey wash that dims light without changing colours"),
("dark black-tinted lenses","a very dark tint that hides the eyes completely"),
("amber-tinted lenses","a warm yellow-orange tint that adds contrast"),
("rose-tinted lenses","a soft pink tint that warms everything"),
("blue-tinted lenses","a light blue tint that gives the eyes a cool cast"),
("green-tinted lenses","a classic green tint that is easy on the eyes"),
("yellow-tinted lenses","a light yellow tint often used for low light"),
("silver-mirrored lenses","a reflective silver coating that shows the surroundings"),
("blue-mirrored lenses","a reflective blue coating with a cool sheen"),
("gold-mirrored lenses","a reflective gold coating with a warm sheen"),
("gradient lenses","a tint that is dark across the top and fades to clear towards the bottom"),
("polarised brown lenses","a brown tint that cuts glare off surfaces such as water"),
("half-darkened photochromic lenses","lenses that have partly darkened in the light"),
("anti-reflective coated lenses","clear lenses with a coating that removes reflections"),
("thick prescription lenses","visibly thick lenses at the edge of the rim, changing how large the eyes appear"),
]
HINGE = S("small metal hinges with tiny screws; spring hinges that flex outward slightly; flat hinges set into the frame; riveted hinges with a visible silver dot")
PADS = S("clear silicone nose pads on thin arms; moulded nose pads built into the frame; small oval metal nose pads; soft pads with a faint yellow tint; no separate pads, the bridge rests directly on the nose")
WEAR = S("; ; ; ; the frame is spotless and the lenses are polished; the frame is slightly scratched at the edges; the lenses carry a few faint smudges; the frame has been bent and straightened; the arms are worn smooth by years of use; a hairline scratch crosses one lens")
ARM_END = S("with plain curved tips; with tips covered in soft rubber; with slim straight ends; with ends that bend down behind the ear")
CONTACTS = [
("natural-looking brown contact lenses","thin clear soft lenses printed with a brown iris pattern that matches ordinary brown eyes"),
("bright blue contact lenses","soft lenses with a vivid blue iris colour that overlays the natural eye colour"),
("green cat-eye contact lenses","soft lenses with a green iris and a narrow vertical slit pupil"),
("red demon contact lenses","soft lenses printed in red, with a black slit pupil, covering the iris"),
("solid black sclera lenses","large lenses that cover the white of the eye with solid black"),
("white zombie contact lenses","opaque white lenses that cover the iris and hide the pupil"),
("yellow wolf-eye contact lenses","soft lenses printed with a yellow iris and a thin dark pupil"),
("glowing UV contact lenses","lenses with a pigment that glows under ultraviolet light"),
("mismatched contact lenses","two soft lenses of different colours, one in each eye"),
("spiral-patterned contact lenses","soft lenses printed with a spiral pattern across the iris"),
("mirror-finish contact lenses","lenses with a reflective silver finish over the whole eye"),
("small-pupil contact lenses","lenses printed with a tiny black pupil in a pale iris"),
("star-pupil contact lenses","lenses printed with a bright iris and a star-shaped pupil"),
]
def eyewear():
    G = {}; lines = []; frames = []
    for name, what, mats in FR:
        M = S(mats); frames.append(f"{name}, which have {what}")
        for i in range(10):
            R = RR('eye', name, i); pool = [l for l in LENS if (('mirror' in name) == ('mirrored' in l[0])) and not (name.startswith('red-and-cyan') or 'safety' in name or 'blue-light' in name or 'gradient' in name or 'taped' in name)] or LENS; lens = R.choice(pool); m = R.choice(M)
            if any(k in name for k in ('welding','swim','ski')): lens = R.choice([LENS[0], LENS[2], LENS[8], LENS[7]])
            if 'gradient' in name: lens = LENS[11]
            if 'blue-light' in name: lens = LENS[14]
            if 'safety' in name: lens = LENS[0]
            if name.startswith('red-and-cyan'): lens = ('one red and one cyan film lens', 'two thin sheets of coloured film')
            if 'mirror' in name and 'mirrored' not in lens[0]: lens = LENS[8]
            tail = R.choice(WEAR)
            nm = name
            if 'goggles' in nm or nm.startswith(('red-and-cyan', 'opera', 'lorgnette', 'monocle', 'pince', 'loupe')):
                s = f"{name[0].upper()+name[1:]}, {what}. Made of {m}, with lenses of {lens[0].replace(' lenses','')}, {lens[1]}."
            else:
                s = f"{name[0].upper()+name[1:]}, {what}. Made of {m}, with {R.choice(HINGE)}, {R.choice(PADS)}, and arms {R.choice(ARM_END)}. The lenses are {lens[0].replace('-tinted lenses',' tint').replace(' lenses','')}, {lens[1]}."
            if tail.strip(): s += f" {tail.strip()[0].upper()+tail.strip()[1:]}." if not tail.strip().endswith('.') else ''
            lines.append(s)
    G['acc_eyewear'] = sorted(set(lines))
    G['acc_eyewear_frame'] = frames
    G['acc_eyewear_lens'] = [f"{n}, which are {d}" for n, d in LENS]
    G['acc_eyewear_hinge'] = HINGE; G['acc_eyewear_nosepad'] = PADS; G['acc_eyewear_armtip'] = ARM_END
    G['acc_eyewear_contact'] = [f"{n}, which are {d}" for n, d in CONTACTS]
    G['acc_eyewear_prompt'] = ['__acc_eyewear__', 'Wearing __acc_eyewear_frame__.', 'Wearing __acc_eyewear_contact__.']
    return G
# ---------- COLLARS ----------
CL = [
("wide leather collar","a band of thick leather about four centimetres wide that sits snugly around the middle of the neck, with a strap-and-buckle closure at the back and a metal D-ring at the front","black leather; brown leather; oxblood leather; navy leather"),
("slim leather day collar","a narrow strap of soft leather about one centimetre wide that sits close under the jaw, with a small buckle at the back and a tiny ring at the front","black leather; tan leather; red leather; white leather"),
("locking collar with padlock","a sturdy leather or steel band closed with a small padlock and hasp at the back, so it cannot be removed without the key","black leather with steel hardware; stainless steel; brass-plated steel"),
("posture collar","a tall stiff band of leather that rises from the collarbone to just under the chin, keeping the head upright; it closes with straps at the back","black leather; stiff brown leather; rigid black plastic"),
("spiked collar","a wide strap of leather studded all the way round with short metal spikes that point outward","black leather with steel spikes; brown leather with brass spikes"),
("studded collar","a leather band set with rows of small round or pyramid-shaped metal studs","black leather with silver studs; red leather with gold studs"),
("rolled-leather collar","a narrow round tube of stitched leather like a thick cord, with a ring at the front and a buckle at the back","black leather; brown leather; green leather"),
("rope collar","a thick length of twisted rope knotted into a neat loop around the neck, with the ends tucked in and a simple knot at the front","natural hemp rope; black cotton rope; red nylon rope"),
("chain collar","a heavy chain of linked metal rings worn like a necklace close around the neck, closed with a clasp at the back","steel chain; brass chain; gunmetal chain"),
("steel slave-style collar","a smooth rigid steel band about two centimetres wide that closes with a screw or lock at the back and has a ring on the front","polished stainless steel; blackened steel; chrome-plated steel"),
("velvet choker","a narrow, soft strip of velvet that wraps closely round the neck, closing with a hook or ribbon tie at the back","black velvet; deep red velvet; navy velvet; emerald velvet"),
("ribbon choker","a flat strip of satin ribbon tied round the neck in a bow at the back, with the ends hanging down","black satin; red satin; white satin; pink satin"),
("lace collar","a narrow band of fine lace wrapped round the neck, with a small clasp at the back","black lace; ivory lace; white lace"),
("pearl collar","several rows of small pearls set in a band that sits around the neck like a choker, held by a clasp at the back","white pearls; grey pearls; black pearls"),
("rhinestone collar","a band of sparkling clear stones set in a metal frame around the neck, with a clasp at the back","silver-toned metal with clear stones; gold-toned metal with clear stones"),
("padded collar","a thick, soft band of leather padded on the inside with foam, giving a smooth and comfortable fit","black leather; tan leather; white leather"),
("neck brace-style medical collar","a firm foam or plastic sleeve that wraps all the way round the neck from jaw to collarbone, closed with a hook-and-loop strap at the back","white foam with a plastic frame; beige foam; light grey foam"),
("soft foam cervical collar","a thick foam ring that wraps round the neck and holds it still, fastened at the back with a hook-and-loop strap","white foam; light grey foam; beige foam with a white cover"),
("neon dog-collar-style band","a wide nylon strap in a bright colour with a plastic clip buckle at the back and a metal ring on the front","neon pink nylon; neon green nylon; neon orange nylon"),
("dog-collar-style collar with tag","a leather or nylon strap with a buckle at the back and a small ring at the front from which a small metal tag hangs","tan leather; black leather; red nylon; blue nylon"),
("bell collar","a narrow strap of leather or ribbon with a small round brass bell hung from the front ring","black leather; red ribbon; green leather"),
("name-plate collar","a wide leather band with a small metal plate on the front engraved with a name","brown leather with a brass plate; black leather with a steel plate"),
("collar with a leash ring","a firm leather or webbing band with a stout metal ring at the front, designed for a lead or short leash to clip to","black leather; brown leather; nylon webbing"),
("Victorian ribbon collar","a narrow ribbon bound closely round the neck and fastened at the back, often holding a small cameo at the front","black velvet ribbon; deep red velvet ribbon; ivory satin ribbon"),
("cameo collar","a narrow ribbon or velvet band with an oval cameo brooch set at the centre front","black velvet with ivory cameo; navy velvet with white cameo"),
("spiral coil neck rings","a stack of many thin coiled metal rings that wrap round the neck and rise in a column from the collarbone to the chin","brass coils; gold-toned coils; silver coils"),
("torc","a rigid, open neck ring in thick twisted metal with decorated ends that sit at the front of the throat","bronze; gold-toned metal; silver"),
("beaded ceremonial collar","a wide, flat collar of tightly strung beads in bands of colour that spreads out across the collarbones and upper chest","multicoloured glass beads; turquoise and gold beads; red and white beads"),
("broad usekh-style collar","a wide, semicircular collar of rows of beads and tubes in bright colours that rests flat on the chest and shoulders","faience beads; gold and turquoise beads; blue and gold beads"),
("neck ruff collar","a wide, stiff pleated collar made from layers of starched linen that stands out round the neck in a full circle","white linen; cream linen; white lace"),
("high stiff military collar","a tall, firm standing collar that closes at the front with hooks and bars and rises to the jaw","dark wool; black wool; navy wool"),
("clerical collar","a narrow, stiff white band that circles the neck and closes at the back, with a small white tab at the front","white plastic; white linen-covered card"),
("lace jabot collar","a ruffled fall of lace that hangs down the front of the chest from a narrow neckband","white lace; ivory lace; cream lace"),
("bondage collar with side rings","a wide leather collar with metal rings on each side and one at the front, for attaching cuffs or clips","black leather with steel rings; brown leather with brass rings"),
("silicone collar","a wide, flexible silicone band that follows the neck with a smooth finish and a snap clasp at the back","black silicone; translucent silicone; red silicone"),
("neoprene collar","a soft stretch band of neoprene fabric with a hook-and-loop closure","black neoprene; navy neoprene"),
("plush novelty collar","a thick tube of plush fabric with a hook-and-loop closure, soft and puffy","pink plush; grey plush; white plush"),
("harness collar","a collar connected to a chest harness by a vertical strap, worn as part of a leather body harness","black leather; brown leather"),
("breakaway collar","a stretchy fabric band with a safety clip that releases if the collar is pulled","black elastic and plastic; coloured elastic and plastic"),
]
DETAIL = S("a brass buckle; a steel buckle; a quick-release buckle; a hasp and padlock; a hook-and-loop strap at the back; a snap clasp; a lobster clasp; a front O-ring; a front D-ring; a ring on each side; a small bell hung from the front ring; a small engraved name tag; short metal studs spaced evenly round the band; pyramid-shaped studs; a row of small rivets along each edge; a soft lining on the inside; contrast stitching along the edges; a thin metal plate at the front; small stones set along the centre; a thin chain hanging from the front ring")
DL = S("contrast stitching along both edges; a row of small rivets along each edge; a soft lining on the inside; short metal studs spaced evenly round the band; a brass buckle and keeper loop; a steel buckle and keeper loop; a front O-ring; a ring on each side; a thin metal plate at the front")
DM = S("a polished edge; a screw closure at the back; a front O-ring; a lobster clasp; a hasp and padlock; a ring on each side")
WL = S("; ; ; the leather has softened and creased with use; the edges are scuffed; the surface is spotless and glossy; the stitching is slightly frayed")
WM = S("; ; ; the metal is polished; the metal is dulled and fingerprinted; a few fine scratches cross the surface")
WS = S("; ; ; the surface is fresh and clean; the fabric is slightly creased; the colour is a little faded")
FIT = S("sitting snugly at the base of the throat; resting low across the collarbones; fitted tightly enough for two fingers to slip underneath; loose enough to turn freely; sitting high under the jaw; resting low and flat on the neck")
WEARC = S("; ; ; ; the surface is spotless and glossy; the edges are scuffed; the metal is polished; the metal is dulled and fingerprinted; the leather has softened and creased with use")
def collar():
    G = {}; lines = []; types = []
    for name, what, mats in CL:
        types.append(f"{name}, which is {what}")
        for i in range(8):
            R = RR('col', name, i); m = R.choice(S(mats)); f = R.choice(FIT)
            lm = m.lower(); soft = any(k in lm for k in ('velvet','satin','lace','ribbon','foam','neoprene','plush','pearl','bead','elastic','linen','wool','card','silicone','rope','faience'))
            if 'leather' in lm and 'leather' in what.lower()+lm: d = R.choice(DL); w = R.choice(WL).strip()
            elif any(k in lm for k in ('steel','brass','bronze','silver','gold','chain','metal','coil')) and not soft: d = R.choice(DM); w = R.choice(WM).strip()
            else: d = ''; w = R.choice(WS).strip()
            if name in ('posture collar','cameo collar','neck brace-style medical collar','soft foam cervical collar','torc','spiral coil neck rings','neck ruff collar','clerical collar','high stiff military collar','lace jabot collar'): d = ''; f = 'resting on the chest'
            if name in ('spiral coil neck rings','neck ruff collar','torc'): f = 'standing out round the neck'
            if name.startswith('dog-collar') or name in ('bell collar','name-plate collar') : d = d or ''
            s = f"{name[0].upper()+name[1:]}, {what}. Made of {m}" + (f", with {d}" if d else '') + f", {f}."
            if w: s += f" {w[0].upper()+w[1:]}."
            lines.append(s)
    G['acc_collar'] = sorted(set(lines)); G['acc_collar_type'] = types
    G['acc_collar_material'] = sorted({m for _, _, ms in CL for m in S(ms)})
    G['acc_collar_feature'] = DETAIL; G['acc_collar_fit'] = FIT
    G['acc_collar_prompt'] = ['__acc_collar__', 'Wearing a __acc_collar_type__.']
    return G
def build():
    G = eyewear(); G.update(collar()); return G
def run(final):
    G = build()
    for n, l in G.items(): open(os.path.join(final, n + '.txt'), 'w', encoding='utf8', newline='\n').write('\n'.join(l) + '\n')
    print('eyewear and collars:', len(G), 'files'); return G
def export_aoo(out, prefix='aoo_'):
    G = build(); names_ = set(G); ref = re.compile(r'__([A-Za-z0-9_\-/]+)__'); n = 0
    for name, lines in G.items():
        keep = list(dict.fromkeys(ref.sub(lambda m: '__' + prefix + m.group(1) + '__' if m.group(1) in names_ else m.group(0), l) for l in lines))
        if not name.endswith('prompt'): random.Random(zlib.crc32(name.encode())).shuffle(keep)
        open(os.path.join(out, prefix + name + '.txt'), 'w', encoding='utf8', newline='\n').write('\n'.join(keep) + '\n'); n += 1
    return n
if __name__ == '__main__':
    a = [x for x in sys.argv[1:] if os.path.isdir(x)]; run(os.path.abspath(a[0]) if a else FINAL)
