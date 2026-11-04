"""Surfboards and wave-riding boards: historic Hawaiian and Pacific Islander boards through modern designs. Descriptions of the boards only (no people, no brands, no real shapers)."""
import os, re, sys, random, zlib
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from paths import FINAL
def rg(*k): return random.Random(zlib.crc32('|'.join(map(str, k)).encode()))
def S(x): return [i.strip() for i in x.split(';') if i.strip()]
# kind: name | era | length | form | build | fins | tail | features
T = [l.split('|') for l in """
alaia|traditional Hawaiian|about 6 to 9 feet|a thin, flat, finless plank, nearly rectangular with a rounded nose and a squared or gently rounded tail, only about an inch thick|hand-planed koa or breadfruit-tree wood, oiled and polished|no fins at all|squared or lightly rounded|a smooth, slightly convex bottom, a hand-rubbed oil finish and no stringer
olo|traditional Hawaiian (chiefly)|about 14 to 18 feet|a long, narrow, heavy plank with a gently tapered nose and tail and a subtle belly|hand-shaped wiliwili or koa wood, rubbed with kukui-nut oil and charcoal-black finish|finless|rounded or squared|a polished dark finish and a thick centre ridge of wood
paipo|traditional Hawaiian and Pacific|about 3 to 4 feet|a short, flat, rounded-nose belly board|a slab of light wood or a hand-shaped plank|finless|squared|a hand-hold groove and a simple oiled finish
kiko'o|traditional Hawaiian|about 6 to 8 feet|a small, broad board|breadfruit wood or similar light wood, smoothly sanded|finless|rounded|a plain oiled finish
papa he'e nalu|traditional Hawaiian|about 8 to 12 feet|a wave-sliding board, long and narrow|koa or wiliwili wood hand-adzed to shape|finless|squared|a deep rich colour from repeated oiling
Tahitian horue|traditional Tahitian|about 6 to 8 feet|a narrow wooden board with a slight rocker|a hand-carved plank of light island wood|finless|rounded|simple carved lines
Tongan and Samoan belly board|traditional Pacific|about 4 to 6 feet|a plain wooden board for riding on the stomach|lightweight island wood or woven plank|finless|rounded|a lashed or smoothed surface
Peruvian caballito de totora|ancient Peruvian reed craft|about 10 to 13 feet|a pointed-nose reed craft, curved up at the front and hollow-bottomed|bundles of dried totora reeds lashed together|finless|squared flat tail|a pale golden reed finish with tight cord lashings
hollow wooden board|1930s early modern|about 10 to 12 feet|a long, hollow, light wooden surfboard with a pointed nose|chambered redwood or pine with a skin of thin plywood|a single large wooden skeg|pin or round|a flat deck with visible wood grain and rounded rails
redwood plank|1930s-1940s|about 10 to 12 feet|a heavy flat plank with a squared tail|solid redwood|a large wooden fin|squared|a flat deck and strips of contrasting wood
balsa gun|1940s-1950s|about 9 to 10 feet|a long narrow board with a pointed nose and pin tail|balsa wood with thin stringer lines|a single glassed-on fin|pin|a glossy resin coat and a visible stringer
single-fin longboard|1960s|about 9 to 10 feet|a wide round-nosed board with a fine-turned rail, a nose that curls up|polyurethane foam with one wooden stringer, fibreglass|a single large fin|round, pin or squared|soft rails, a nose rocker and classic stripes
hull board|1960s-1970s|about 7 to 9 feet|a long gliding board with a keel-like bottom|polyurethane foam, fibreglass|single or twin fixed fins|pin or round|a flat deck and a V-shaped bottom
pig board|1970s|about 6 to 8 feet|a board with a wide hip and a narrow pin tail|polyurethane foam, fibreglass|single fin|pin|a wide nose and a heavy weight
twin-fin retro fish|1970s revival|about 5 to 6 feet|a short, wide board with a swallow tail and flat rocker|polyurethane or epoxy foam, fibreglass|two keel fins|swallow|a flat low-rocker bottom and a fat outline
keel fish|1970s|about 5 to 6 feet|a short wide board with a deep swallow tail|polyurethane foam, fibreglass|two big keel fins|swallow|a fat flat bottom
egg|1990s-2000s|about 6 to 8 feet|a rounded, egg-shaped board with soft rails|polyurethane foam or epoxy, fibreglass|single fin or tri fin|round|a generous nose and a gentle rocker
mini-mal (mini-malibu)|1990s-present|about 7 to 8 feet|a wide round-nosed board, easy to paddle|polyurethane foam or epoxy, fibreglass|tri-fin setup|round|a stable thick deck
longboard|1950s-present|about 9 to 10 feet|a long, wide board with a rounded nose and a flat-to-gently-rockered bottom|foam core with a wooden stringer and fibreglass|a single fin or 2+1 set|round, pin or squared|a classic noserider design with soft rails
funboard|1980s-present|about 6 to 8 feet|a medium-length board with a rounded nose|polyurethane or epoxy foam|tri-fin or quad|round|a forgiving outline and thick rails
thruster shortboard|1980s-present|about 5 to 6.5 feet|a high-performance pointed-nose board with a narrow outline|polyurethane foam with a stringer or epoxy foam, fibreglass|three fins in a thruster set|squash, round pin or swallow|thin rails, a pronounced rocker and a lightweight build
quad fin shortboard|1990s-present|about 5 to 6 feet|a speedy board with a pronounced rail line|epoxy or polyurethane foam|four fins|squash or swallow|a wider tail, a thin nose
twin-fin shortboard|1970s-present|about 5 to 6.5 feet|a short, wide-tail board with a pointed nose|polyurethane or EPS foam|two fins|swallow or round|a loose, fast feel
step-up|modern|about 6 to 7 feet|a longer, narrower shortboard for bigger waves|polyurethane or epoxy foam, fibreglass|three fins|pin or round pin|extra length and a controlled rocker
big-wave gun|modern|about 8 to 10 feet|a long narrow board with a pointed nose and a pin tail|polyurethane foam with heavy fibreglass and stringers|three fins or single|pin|thick rails and a thick tail
tow-in board|modern|about 5 to 6 feet|a short, heavy board with foot straps|dense foam, carbon-reinforced|three fins, deep set|pin|foot straps and a heavy weight
hybrid fish|modern|about 5 to 6 feet|a shortboard-fish blend with a pointed nose and a swallow tail|epoxy or polyurethane foam|tri or quad fin|swallow|a flat-ish rocker and a bit of volume
bonzer|1970s-present|about 5 to 6.5 feet|a board with three channels in the tail and two side fins|polyurethane foam|three fins, two bonzer fins and one centre|squash or round|concave channels on the bottom
mid-length glider|modern|about 7 to 8 feet|a wide round-nosed board with a flat rocker|epoxy foam|2+1 fin set|round pin|a fluid, gliding feel
soft-top foam board|modern|about 6 to 9 feet|a beginner board with a soft foam deck and rounded nose|a foam core with a soft deck and slick bottom|three plastic fins|round|soft rails and a bright deck
stand-up paddleboard|modern|about 9 to 12 feet|a wide thick board for standing and paddling|an epoxy core with a carbon or fibreglass skin, or an inflatable drop-stitch build|a large centre fin plus side fins|round or pin|a deck pad, a leash plug and an inset handle
inflatable paddleboard|modern|about 10 to 12 feet|a thick wide board that inflates with air|drop-stitch PVC|a removable centre fin|rounded|bungee cord on the front and a deck pad
bodyboard|1970s-present|about 3.5 to 4.5 feet|a small foam board for lying on the front, with a rounded nose|a foam core with a slick bottom and a deck skin|finless|crescent or bat-tail|a wrist leash and hand grips
kneeboard|1960s-present|about 5 to 6 feet|a short wide board for kneeling|foam with a thick deck|twin fins|square or round|a padded deck
skimboard|modern|about 3.5 to 4.5 feet|a thin, round, finless board for the shore break|wood or foam, fibreglass|finless|rounded|a thin flat profile and a wide nose
wave ski|modern|about 7 to 9 feet|a narrow sit-on board with a seat and foot straps|a moulded polyethylene or foam core|a single centre fin|squared|a deep seat and straps
foil surfboard|modern|about 4 to 6 feet|a small, buoyant board with a mast below|a carbon fibre or EPS build|a mast and hydrofoil wing|squared|a foil mounted on a track
handplane|traditional-present|about 1 foot|a small paddle-like body-surfing plane|wood or foam|finless|rounded|a hand strap
wooden alaia revival|modern|about 6 to 8 feet|a finless thin plank like the historic board|paulownia or cedar planks|none|squared|a clean oiled finish
hollow wood paulownia board|modern|about 8 to 10 feet|a hollow board built from thin ribs and planks|paulownia or cedar|a wooden fin or a removable fin|round or pin|exposed wood grain and a gloss varnish
""".strip().split('\n')]
RAILS = S("soft rounded rails; hard-edged rails; boxy rails; 50/50 rails; down rails; thin low-volume rails; full thick rails; tucked-under rails; double-edged rails")
TAILS = S("squash tail; round tail; pin tail; rounded pin tail; swallow tail; diamond tail; square tail; bat tail; wing swallow tail; fish tail")
FINS = S("a single large fin; a single fin with a flexible tip; a twin fin set; a thruster (three-fin) set; a quad fin set; a 2+1 fin set; a five-fin plug system; a glass-on fin set; a removable plug-in fin; a keel fin pair; a bonzer fin set; a finless design")
MAT = S("polyurethane foam and fibreglass; epoxy foam and fibreglass; expanded polystyrene and epoxy; balsa wood and resin; hollow paulownia wood; redwood plank; solid koa wood; carbon fibre reinforced foam; bamboo veneer over foam; cedar and varnish; recycled foam and bio-resin; plywood stringer and foam; carbon rail wrap and foam")
STR = S("a single wooden stringer; a double stringer; a carbon stringer; a stringerless build; a bamboo stringer; a coloured wood stringer; a parabolic carbon flex strip")
COL = S("white; sea-foam green; sunset orange; deep ocean blue; coral red; bright yellow; teal; gloss black; pale pink; pastel mint; lavender; navy blue; ochre; sand; clear glass; cherry red; turquoise; two-tone blue-and-white; forest green; sky blue; hot pink; cream; charcoal")
PAT = S("a pinline around the rail; bold racing stripes; a sunburst in orange and yellow; a hand-painted palm-leaf pattern; a resin swirl; a fade from blue to white; a tapa-cloth-inspired geometric pattern in dark brown and cream; a polynesian-inspired wave-and-shell border pattern; a tropical flower print; a cutlap panel in a contrasting tint; checkerboard panels; wavy lines; an airbrushed ocean-sunset scene; a marbled swirl in two colours; tie-dye resin; a woven rattan look; a camouflage-style spray; hand-painted fish and waves; a diamond-pattern deck; dotted lines along the rails; a sun face mural; wood-strip inlay in bands; a plain clear gloss finish; a speckled spray; pastel colour blocks")
DECK = S("a full-length traction pad; a three-piece deck pad; wax-coated texture; a bare gloss deck with wax; a deck made from visible wood strips; a soft grippy foam deck; foot straps; a leash plug at the tail; an inset handle in the deck; a nose-guard rail strip")
NOSE = S("a pointed nose; a round nose; a wide round nose; a slightly turned-up nose; a blunt nose; a pulled-in nose")
ROCK = S("a flat rocker; a medium rocker; a pronounced rocker; a continuous curve; a stepped rocker; a low-entry rocker")
def desc(R, t):
    name, era, ln, form, build, fins, tail, feat = t
    return f"{name.capitalize()} ({era}): {ln} long, {form}, built from {build}, with {fins}, a {tail} tail, and {feat}."
def build():
    G = {}; R = rg('surf')
    types = [t[0] for t in T]; G['surfboard_type'] = types
    G['surfboard_historic'] = [t[0] for t in T if re.search(r'traditional|ancient|193|194|195', t[1])]
    G['surfboard_modern'] = [t[0] for t in T if t[0] not in G['surfboard_historic']]
    G['surfboard_pacific'] = [t[0] for t in T if re.search(r'Hawaiian|Tahitian|Pacific|Peruvian', t[1])]
    G['surfboard_rail'] = RAILS; G['surfboard_tail'] = TAILS; G['surfboard_fins'] = FINS; G['surfboard_material'] = MAT
    G['surfboard_stringer'] = STR; G['surfboard_colour'] = COL; G['surfboard_pattern'] = PAT; G['surfboard_deck'] = DECK; G['surfboard_nose'] = NOSE; G['surfboard_rocker'] = ROCK
    base = [desc(R, t) for t in T]; G['surfboard_basic'] = base
    full = set(base)
    for t in T:
        for i in range(12):
            r2 = rg('sf', t[0], i); name, era, ln, form, build_, fins, tail, feat = t
            hist = t[0] in G['surfboard_historic']
            if hist:
                full.add(f"{name.capitalize()} ({era}): {ln}, {form}; made of {build_}; {fins}; {tail} tail; {feat}. The surface is {r2.choice(['hand-rubbed with natural oil', 'polished to a deep sheen', 'scuffed from use with visible wood grain', 'dark and glossy from age'])}, with {r2.choice(['no paint at all', 'a simple carved line', 'a few worn marks', 'a light wood grain pattern'])}.")
            else:
                full.add(f"{r2.choice(COL).capitalize()} {name}: {ln}, {form}; {r2.choice(MAT)}; {r2.choice(NOSE)}; {r2.choice(ROCK)}; {r2.choice(RAILS)}; {r2.choice(TAILS)}; {r2.choice(FINS)}; {r2.choice(STR)}. Finish: {r2.choice(PAT)}. Deck: {r2.choice(DECK)}.")
    G['surfboard'] = sorted(full)
    G['surfboard_design'] = [f"{c} with {p}" for c in COL for p in PAT[:12]][:200]
    G['surfboard_prompt'] = ['A __surfboard__.', 'A surfboard shown standing upright: __surfboard__.', 'A surfboard laid flat, top and bottom visible: __surfboard__.', 'A __surfboard_type__ with __surfboard_pattern__ in __surfboard_colour__, __surfboard_rail__ and __surfboard_fins__.', 'A pair of surfboards: __surfboard__ and __surfboard__.', 'A rack of surfboards, including a __surfboard_type__ and a __surfboard_type__.']
    G['surfboard_prompt_historic'] = [f'A {x} surfboard.' for x in G['surfboard_historic']]
    return G
def run(final):
    G = build()
    for n, l in G.items():
        assert l and all(l) and not any(re.search(r'[{}|]', x) for x in l if '__' not in x), n
        open(os.path.join(final, n + '.txt'), 'w', encoding='utf8', newline='\n').write('\n'.join(l) + '\n')
    print('surfboards:', len(G), 'files;', len(G['surfboard']), 'descriptions'); return G
def export_aoo(out, prefix='aoo_'):
    G = build(); names_ = set(G); ref = re.compile(r'__([A-Za-z0-9_\-/]+)__'); n = 0
    for name, lines in G.items():
        keep = list(dict.fromkeys(ref.sub(lambda m: '__' + prefix + m.group(1) + '__' if m.group(1) in names_ else m.group(0), l) for l in lines))
        if not name.startswith('surfboard_prompt'): random.Random(zlib.crc32(name.encode())).shuffle(keep)
        open(os.path.join(out, prefix + name + '.txt'), 'w', encoding='utf8', newline='\n').write('\n'.join(keep) + '\n'); n += 1
    return n
if __name__ == '__main__':
    a = [x for x in sys.argv[1:] if os.path.isdir(x)]; run(os.path.abspath(a[0]) if a else FINAL)
