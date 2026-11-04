"""v81 stage A - robots (rb_). 25 robot types, each with its own body, head, eyes, arms, hands, movement and feature lists, plus shared colour, wear,
marking (quoted text), scale, place and shot pools. Fully described looks only; no real robot names or brands."""
import os, sys, re
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from famlib import P
from v81_rb_data1 import A1
from v81_rb_data2 import A2
from v81_rb_data3 import A3
ARCH = {}; ARCH.update(A1); ARCH.update(A2); ARCH.update(A3)
STYLE = {'tin': 'toy', 'pet': 'toy', 'clock': 'antique', 'micro': 'strange', 'snake': 'strange', 'alien': 'strange',
         'spider': 'rugged', 'rover': 'rugged', 'tread': 'rugged', 'mech': 'rugged', 'war': 'rugged', 'sub': 'rugged', 'space': 'rugged', 'exo': 'rugged'}
def style(k): return STYLE.get(k, 'modern')
COLOUR = {
 'toy': "bright red and yellow with printed rivets; sky blue with white trim; a fading green with an orange chest panel; shiny silver with red details; pastel pink and cream; cherry red with a white face; mustard yellow with blue arms; mint green and white; two-tone orange and cream; glossy black with gold stars; royal blue with silver buttons; a rainbow of printed panels",
 'modern': "pure white with pale grey trim; matte black with a thin blue light; white with bright orange accents; two-tone grey with yellow warning marks; pearl white with a teal band; graphite grey with copper highlights; satin silver with black joints; pale green and white; bright yellow and charcoal; soft cream with a navy stripe; gunmetal with red trim; glossy white with a single coloured band",
 'rugged': "dull olive green with black joints; sand tan with brown panels; flat black with grey trim; hazard orange with grey underbody; desert camouflage in tan and brown; dark navy with white lettering; yellow with black stripes; stone grey with a rust-red stripe; gloss white with orange tips; forest camouflage in green and black; gunmetal with a white numeral; matte dark grey with red markings",
 'antique': "polished brass with copper rivets; warm copper with green verdigris; dark bronze with gold edges; blackened iron with brass trim; cream enamel with gold lines; ivory and brass; deep red lacquer with gold; blue enamel and polished steel; weathered nickel with brass keys; black lacquer with silver stripes",
 'strange': "oily black with a purple sheen; pale bone white with glowing lines; deep green with gold veins; translucent glass with a blue core; glossy red like wet paint; milky pearl with rainbow edges; dark violet with silver circuits; rust brown with a glowing orange seam; chrome with pink light; pale yellow with black markings"}
WEAR = {
 'toy': "lightly scuffed with a few chips in the paint; spotless and boxed new; rubbed through to bare tin at the corners; dented on one side; faded by years in sunlight; scratched with a missing printed detail; polished and well loved; speckled with small rust spots; brand new and gleaming; patched with tape on one arm",
 'modern': "factory clean and spotless; lightly scuffed from daily use; dusty after long standing; covered in fingerprints; scratched along the panels; stained with oil near the joints; dull with sun-fade; neat with a few small stickers; polished and new; worn at the edges where hands hold it",
 'rugged': "caked in mud and dust; scorched and scratched; dented with patched armour; salt-stained and weathered; sun-bleached with peeling paint; covered in fine red dust; oily with rusty bolts; heavily scarred but clean; frosted with ice; battered with a cracked lens",
 'antique': "polished to a mirror shine; dark with age and a green patina; scratched with a worn gilt finish; oily at every joint; stained with soot; recently restored and bright; dented with a mended seam; tarnished brown in the creases; dusty in a museum case; chipped enamel showing bare metal",
 'strange': "flawless and unnaturally clean; cracked and leaking faint light; covered in a layer of frost; scorched along one side; slick with a thin film of water; dusted in fine glittering powder; dull and dormant; pulsing with fresh light; half buried in sand; tangled in thin roots"}
SCALE = P("a toy-sized; a hand-sized; a small desk-sized; a knee-high; a waist-high; a human-sized; a tall human-sized; a twice human-sized; a van-sized; a building-sized; a very tall; a squat; a compact; a slender; a hulking; a delicate")
SCALE_GENTLE = P("a small; a hand-sized; a knee-high; a waist-high; a human-sized; a tall; a compact; a slender; a hulking; a delicate; a sturdy; a lean")
TEXT_UNIT = P('"UNIT 04"; "RX-9"; "MK II"; "B-12"; "HELPER"; "SERIES 3"; "NO. 17"; "ZETA"; "TOBY"; "PIP"; "CLEAR"; "A1"; "ORBIT"; "SCOUT"; "HUGO"; "MODEL 9"; "OPAL"; "BOLT"; "WORKER 31"; "NOVA"; "MARGO"')
TEXT_WARN = P('"CAUTION"; "DANGER"; "KEEP CLEAR"; "THIS SIDE UP"; "STOP"; "HOT"; "LIFT HERE"; "HANDLE WITH CARE"; "EMERGENCY STOP"; "PRESS TO START"; "NO ENTRY"; "AUTHORISED ONLY"')
MARKS = ["with the name __rb_text_unit__ painted on its chest", "with the name __rb_text_unit__ stencilled on one shoulder", "with a small plate on its back that reads __rb_text_unit__", "with a warning label that reads __rb_text_warn__", "with a sticker on its side that reads __rb_text_warn__", "with a row of panel lines and a tiny serial number __rb_text_unit__", "with a yellow tag tied on that reads __rb_text_unit__", "with a faded stripe and the word __rb_text_warn__ below it", "with a number painted on its front that reads __rb_text_unit__", "with a name badge on its chest that reads __rb_text_unit__", "with plain panels and no writing", "with a small printed label on its leg that reads __rb_text_warn__"]
PLACES = {
 'indoor': "in a warm living room beside an armchair; on a kitchen table next to a bowl of fruit; on a bedroom rug in morning light; in a quiet hallway with a coat rack; on a wooden shelf among books; on a sofa with a folded blanket; beside a window with a view of rain; at a cafe table; on a staircase landing; in a bright playroom; on a desk beside a lamp",
  'toy': "in a toy shop window; on a nursery shelf beside a teddy bear; on a bedroom rug among building blocks; in a bright playroom; on a kitchen table beside a bowl of fruit; on a wooden shelf among picture books; on a windowsill in morning light; in a glass cabinet of old toys",
 'work': "on a building site beside a pile of bricks; in a busy warehouse aisle; on a loading dock at sunrise; in a workshop with tools on the walls; in a clean corridor of an office block; on a factory floor beside a conveyor; in a hardware store aisle; in a power plant control room; at a bus depot; on a construction scaffold",
 'factory': "in a bright assembly hall with long conveyor belts; on a factory floor with painted yellow lines; in a dim warehouse between tall shelves; inside a fenced work cell with warning lights; beside a stack of crates; at a loading bay; in a spotless packing hall; in front of a wall of control panels",
 'lab': "in a bright laboratory with glass benches; in a clean room with white walls; on a steel table under a bright lamp; in a hospital theatre with soft blue light; in a research workshop full of wires; in front of a microscope bench; in a classroom lab; under a hood lamp in a quiet corridor",
 'outdoor': "on a rocky hillside in late sun; on a sandy plain with long shadows; on a forest path with fallen leaves; on a snow field under a pale sky; on a gravel road beside a stream; on a rough quarry floor; in a sunlit meadow; on a dusty red plain; on a wet beach at low tide; on a cracked dry lake bed",
 'rugged': "on a rubble-strewn street after a storm; in a dusty quarry; at the mouth of a collapsed tunnel; on a muddy field in the rain; in a smoke-filled corridor; on a flooded road; on a steep rocky slope; beside a burned-out wall; at a snowy checkpoint; in a ruined hall with fallen beams",
 'sky': "high above a rolling green valley; over a wide grey sea; above a city rooftop at dusk; hovering in a bright blue sky; flying through a pine forest; above a golden wheat field; beside a tall wind turbine; over a river bend at dawn",
 'battlefield': "on a smoking field at dusk; in a ruined city street; on a rocky ridge under a stormy sky; in front of a burning wall; on a wet road in the rain; in a desert canyon; in a snowy ruin with falling snow; beside a toppled tower",
 'water': "on a dark seabed with floating particles; beside a coral reef in blue light; beside a sunken wreck; over a field of kelp; in open dark water with light rays above; beside a rocky cliff underwater; over a muddy seafloor; near an undersea vent",
 'space': "on a dusty grey plain with a black sky; in orbit with the curve of a blue planet behind; against a red desert and a pale sky; beside a long white truss in space; on a rocky asteroid with sharp shadows; on a moon plain with a big planet in the sky; in a dim hangar with a spacecraft; on a pale icy plain",
 'antique': "on a wooden workbench in a clock workshop; in a velvet-lined glass case; on a polished table in a Victorian parlour; in a cluttered inventor's attic; in a dim shop with ticking clocks; on a fairground stall; on a marble mantelpiece; at the foot of a spiral staircase",
 'strange': "on a smooth black plain under two moons; inside a cavern of glowing crystals; in a misty valley of bone-white trees; in a vast silent hall of mirrors; floating in a pool of dark water; on a bare plateau under a green sky; in a dark room lit only by its own light; in an empty desert with a spiral on the sand"}
SHOT = P("a front view with the whole robot visible; a low angle looking up at it; a three-quarter view from the side; a wide shot showing the robot small in its place; a side view in profile; a close-up of its joints and details; an eye-level view with soft background blur; a view from behind and above; a close-up of its surface and markings")
SHOT_FACE = P("a close-up on the head and chest; a close-up of its face; a close-up of its hands and arms; a portrait of its head and shoulders")
FACED = ("tin", "human", "android", "butler", "dog", "pet", "face", "mech", "war", "clock", "alien", "exo")
LIGHT = P("soft window light; low golden sunlight; cool blue evening light; harsh midday sun; warm lamp light; bright studio light; dim light with a glow from the robot; grey overcast light; neon light from the side; early morning mist and low sun")
def norm(s):
    s = s.strip()
    m = re.match(r'no [\w\- ]+?(?:,| but) (?:but |only |just )?(.*)', s)
    if m: return m.group(1)
    if re.fullmatch(r'no [\w\- ]+', s): return 'absent'
    return s
ABS = {'head': 'no head', 'arms': 'no arms', 'eyes': 'no visible eyes', 'hands': 'nothing at all', 'move': 'no means of movement', 'feat': 'nothing special', 'body': 'no body'}
COL = r'(?:white|black|yellow|grey|gray|red|orange|silver|cream|pink|olive|gunmetal|green|blue|beige|brown|purple|tan)'
COLRE = re.compile(r'\b' + COL + r'(?:(?:,| and) ' + COL + r')*\s+', re.I)
COLEND = re.compile(r'\b(?:in|of) ' + COL + r'(?:(?:,| and) ' + COL + r')*\s+(?=with\b|and\b|,|\.|;|$)', re.I)
def decol(x): return re.sub(r'\ba (?=(?:[aeio]|und|upp|upo)\w*)', 'an ', COLRE.sub('', COLEND.sub('', x)))
def slot(name, items):
    out = [ABS[name] if norm(x) == 'absent' else norm(x) for x in P(items)]
    return [decol(x) for x in out] if name in ('body', 'head', 'arms', 'hands', 'move') else out
def pl(n):
    if n.endswith('mouse'): return n[:-5] + 'mice'
    if n.endswith('s'): return n
    if n.endswith('y') and n[-2] not in 'aeiou': return n[:-1] + 'ies'
    if n.endswith(('ch', 'sh', 'x')): return n + 'es'
    return n + 's'
def an(n): return ('An ' if n[:1].lower() in 'aeiou' else 'A ') + n
LOOKS = ["Its body is __rb_%(k)s_body__. It has __rb_%(k)s_head__. Its sensors and face show __rb_%(k)s_eyes__. It has __rb_%(k)s_arms__, ending in __rb_%(k)s_hands__. For movement it has __rb_%(k)s_move__. A notable detail is __rb_%(k)s_feature__.",
         "It has __rb_%(k)s_head__, with __rb_%(k)s_eyes__. Its body is __rb_%(k)s_body__, with __rb_%(k)s_arms__, ending in __rb_%(k)s_hands__. It moves on __rb_%(k)s_move__. It also has __rb_%(k)s_feature__.",
         "Built with __rb_%(k)s_body__, it has __rb_%(k)s_head__, which shows __rb_%(k)s_eyes__. It has __rb_%(k)s_arms__, ending in __rb_%(k)s_hands__. For movement it has __rb_%(k)s_move__. Look for __rb_%(k)s_feature__."]
def build(final=None):
    G = {}; ep = []; kinds = []
    G['rb_text_unit'] = TEXT_UNIT; G['rb_text_warn'] = TEXT_WARN; G['rb_marks'] = MARKS; G['rb_shot'] = SHOT; G['rb_shot_face'] = SHOT_FACE; G['rb_shot_any'] = SHOT + SHOT_FACE; G['rb_light'] = LIGHT
    G['rb_scale'] = SCALE; G['rb_scale_gentle'] = SCALE_GENTLE
    for g, v in COLOUR.items(): G['rb_colour_%s' % g] = P(v)
    for g, v in WEAR.items(): G['rb_wear_%s' % g] = P(v)
    for g, v in PLACES.items(): G['rb_place_%s' % g] = P(v)
    for k, (noun, pg, body, head, eyes, arms, hands, move, feat) in ARCH.items():
        st = style(k)
        G['rb_%s_body' % k] = slot('body', body); G['rb_%s_head' % k] = slot('head', head); G['rb_%s_eyes' % k] = slot('eyes', eyes)
        G['rb_%s_arms' % k] = slot('arms', arms); G['rb_%s_hands' % k] = slot('hands', hands); G['rb_%s_move' % k] = slot('move', move); G['rb_%s_feature' % k] = slot('feat', feat)
        G['rb_%s_look' % k] = [t % {'k': k} for t in LOOKS]
        G['rb_%s_prompt' % k] = [an(noun).rstrip() + '. __rb_%s_look__ Its colours are __rb_colour_%s__, __rb_marks__. It looks __rb_wear_%s__. It is __rb_place_%s__, in __rb_light__, and the image is __rb_shot%s__.' % (k, st, st, pg, '_any' if k in FACED else '')]
        G['rb_%s_short' % k] = [an(noun) + ' with __rb_%s_head__, __rb_%s_body__, and __rb_%s_move__, finished in __rb_colour_%s__.' % (k, k, k, st)]
        G['rb_%s_group_prompt' % k] = ['Three %s are shown together %s. The first has __rb_%s_head__ and __rb_%s_body__, finished in __rb_colour_%s__. The second has __rb_%s_head__ and __rb_%s_body__, finished in __rb_colour_%s__. The third has __rb_%s_head__ and __rb_%s_body__, finished in __rb_colour_%s__. They are __rb_wear_%s__, in __rb_light__.' % ((pl(noun), '__rb_place_%s__' % pg) + (k, k, st) * 3 + (st,))]
        kinds.append(k)
        ep += ['rb_%s_prompt' % k]
    for s_ in ('prompt', 'group_prompt', 'short'): G['rb_' + s_] = ['__rb_%s_%s__' % (k, s_) for k in kinds]
    G['rb_types'] = [ARCH[k][0] for k in kinds]
    ep = ['rb_prompt', 'rb_group_prompt', 'rb_short'] + ep
    G['v81_rb_entry_points'] = ep
    return G
if __name__ == '__main__':
    G = build(); print(len(G));
    import random
    for k in ('tin', 'snake', 'orb'):
        print(G['rb_%s_prompt' % k][0][:300])
