"""v41: plastic and novelty ranges for lighters and keychains, wired into acc_lighter / acc_keychain; also replaces brand-style words in the lighter files."""
import os, re, sys, glob, random, zlib
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from paths import FINAL
from v40_data_a import E
import v40_build as V
LP = E("""
disposable plastic lighter|a slim, throwaway lighter with a clear plastic fuel tank, a metal spark wheel on top that is turned with the thumb and a small metal flame guard|clear plastic; opaque plastic; tinted plastic
child-proof disposable lighter|a slim throwaway lighter with a stiff metal safety bar over the spark wheel that has to be pressed before it will light|opaque plastic; tinted plastic
push-button plastic lighter|a small plastic lighter that lights with a single press of a button on the top, with a flame hood at the front|moulded plastic; ABS plastic
refillable plastic lighter|a chunky lighter body in hard plastic with a refill valve on the base and an adjustable flame wheel|ABS plastic; polycarbonate
clear see-through plastic lighter|a lighter with a fully transparent body so that the fuel level and the inner mechanism are visible|clear acrylic; clear polycarbonate
translucent jelly-colour plastic lighter|a lighter with a glossy, see-through body in a saturated colour|tinted acrylic; tinted polycarbonate
glow-in-the-dark plastic lighter|a plastic lighter whose body glows green in the dark after exposure to light|phosphorescent plastic
glitter plastic lighter|a lighter with a clear body filled with suspended glitter|glittered acrylic
metallic-finish plastic lighter|a plastic lighter coated with a thin metallic layer that looks like chrome or gold|metallised plastic
printed-wrap plastic lighter|a plastic lighter whose entire body is wrapped in a printed pattern, such as flowers, stripes, stars or flames|plastic with a printed sleeve
marbled plastic lighter|a plastic lighter with swirled streaks of two or three colours through the body|swirled resin; swirled plastic
rubberised plastic lighter|a soft-touch lighter with a rubbery, slightly matte coating over a hard plastic frame|rubber-coated plastic
utility plastic lighter|a long, slim lighter with a bendable neck and a trigger, for lighting stoves and candles|plastic and steel
flip-lid plastic lighter|a lighter with a plastic body and a hinged plastic lid over the flame, that snaps shut|moulded plastic
square plastic pocket lighter|a flat-sided rectangular lighter in plastic with a recessed spark wheel and a lanyard hole|ABS plastic
mini plastic lighter|a very small lighter about the length of a finger, in a bright plastic body|moulded plastic
jumbo plastic lighter|an oversized plastic lighter about the size of a hand, with a big spark wheel|moulded plastic
electric plastic lighter|a rechargeable lighter with a plastic body, a USB port and a pair of arcs that glow across the top|plastic with metal electrodes
plastic clip-on lighter|a lighter with a plastic body and a spring clip on the back that grips a pocket or belt|plastic
stackable plastic lighter|a lighter with a flat plastic body that snaps together with others in a row|moulded plastic
""")
LN = E("""
animal-shaped novelty lighter|a lighter moulded into the shape of a small animal, such as a cat, frog, fish or owl, with the flame coming from the mouth or top|painted resin; plastic; enamelled metal
food-shaped novelty lighter|a lighter shaped like a piece of food, such as a burger, a slice of pizza or a banana|painted plastic; resin
skull-shaped novelty lighter|a lighter shaped like a human skull with the flame coming from the top|resin; metal; plastic
sneaker-shaped novelty lighter|a lighter shaped like a miniature trainer with a laced upper and a thick sole|plastic; resin
camera-shaped novelty lighter|a lighter shaped like a miniature box camera, flame hidden behind the lens|metal; plastic
telephone-shaped novelty lighter|a lighter shaped like an old desk telephone with a dial and receiver|plastic; metal
cassette-shaped novelty lighter|a flat lighter shaped like an old audio cassette tape|plastic; metal
radio-shaped novelty lighter|a boxy lighter shaped like a retro radio with a dial and a speaker grille|plastic; metal
bottle-shaped novelty lighter|a lighter shaped like a miniature bottle with a cap that flips open|glass; plastic; metal
car-shaped novelty lighter|a lighter shaped like a small vintage car with a flame between the headlights|diecast metal; plastic
rocket-shaped novelty lighter|a tall lighter shaped like a rocket on its fins, with a flame at the nose|metal; plastic
lipstick-shaped novelty lighter|a slim cylindrical lighter that looks like a tube of lipstick|metal; plastic
pen-shaped novelty lighter|a slim lighter shaped like a pen with a pocket clip|metal; plastic
heart-shaped novelty lighter|a lighter in the shape of a heart, with a lid at the top point|enamelled metal; plastic
musical-note novelty lighter|a lighter shaped like a musical note with a head and a stem|plastic; resin
coloured flame novelty lighter|a lighter that produces a differently coloured flame such as blue, green or purple|metal; plastic
lantern-shaped novelty lighter|a lighter shaped like a small hanging lantern with a glass cage|metal and glass
tiny gadget novelty lighter|a lighter styled as a mini gadget, with working dials and switches that are only for show|metal; plastic
talking novelty lighter|a lighter that plays a short recorded sound when lit|plastic; metal
spinning novelty lighter|a lighter with a rotating top or ring that spins when pressed|metal; plastic
light-up novelty lighter|a lighter with a small light-emitting diode ring that glows in several colours as it lights|plastic; metal
fidget-spinner novelty lighter|a lighter with a ball-bearing wheel built into the body|metal; plastic
mini bucket novelty lighter|a lighter shaped like a miniature ice bucket with a lid|metal; plastic
pocket-watch novelty lighter|a round lighter with a face like a pocket watch|metal
robot-shaped novelty lighter|a lighter in the form of a small boxy robot with arms and a head|metal; plastic
mushroom-shaped novelty lighter|a lighter shaped like a toadstool with a spotted cap|painted resin; plastic
flower-shaped novelty lighter|a lighter shaped like a flower with petals around the flame|enamelled metal; plastic
bone-shaped novelty lighter|a lighter shaped like a long bone with knobbed ends|resin
tiny-tool novelty lighter|a lighter shaped like a miniature hand tool such as a wrench or hammer|metal; plastic
""")
KP = E("""
acrylic keychain|a flat see-through acrylic tag, cut into a shape with a hole near the top and a small metal ring|clear acrylic; tinted acrylic; mirrored acrylic
printed acrylic keychain|a flat acrylic tag with a printed image on one side and a clear back|printed acrylic
glitter acrylic keychain|a flat acrylic tag with suspended glitter between two layers|glittered acrylic
epoxy-dome keychain|a small metal or plastic tag with a glossy clear domed resin top covering a picture|resin; plastic
PVC rubber keychain|a soft rubber figure or logo shape moulded in two or three colours with a loop at the top|soft PVC
silicone keychain|a bendable silicone tag or figure with a hole through the top|silicone
silicone wristlet keychain|a stretchy silicone bracelet with a ring for keys|silicone
foam keychain|a lightweight foam shape that floats and has a ring at the top|closed-cell foam
plastic tag keychain|a rectangular plastic tag with a blank space for a name and a small ring|hard plastic
plastic bottle opener keychain|a flat plastic keychain with a metal bottle opener built in|plastic and steel
plastic carabiner keychain|a lightweight plastic clip with a spring gate that hooks onto keys|plastic
plastic flashlight keychain|a small plastic torch with a button that lights a tiny lamp|plastic
plastic whistle keychain|a small plastic whistle with a ring at the end|plastic
plastic bobblehead keychain|a small plastic figure with a head on a spring that nods|plastic
plastic photo-frame keychain|a small plastic frame holding a tiny photo behind a clear window|plastic
plastic fidget keychain|a small plastic toy with a pop-up button or spinning part for fidgeting|plastic
plastic coin-holder keychain|a small plastic tag with a slot for a shopping-cart token|plastic
plastic retractable keychain|a plastic reel with a thin cord that pulls out and retracts, with a clip for the belt|plastic
plastic mini-calculator keychain|a tiny plastic calculator with small buttons and a display|plastic
plastic laminated name-tag keychain|a rectangular plastic sleeve holding a printed card|laminated plastic
plastic magnifier keychain|a small plastic frame holding a magnifying lens|plastic
plastic mini-torch keychain|a pocket light with a bright lens, in a small tube|plastic
plastic bead keychain|many small plastic beads threaded onto a cord, with a ring at one end|plastic beads
""")
KN = E("""
miniature book novelty keychain|a tiny closed book with a cloth or paper cover and miniature pages|cloth; paper
miniature shoe novelty keychain|a small shoe with laces and a sole, hanging from a ring|resin; felt; plastic
miniature food novelty keychain|a tiny model of food such as a sandwich, a doughnut or a cupcake|resin; felt; polymer clay
mini instrument novelty keychain|a tiny guitar, piano or drum with small details|metal; resin; wood
tiny globe novelty keychain|a small globe that spins on a stand within a ring|metal and plastic
mini bell novelty keychain|a small round bell hanging from a ring|brass; plastic
plush animal novelty keychain|a small stuffed animal with a loop at the neck|plush fabric; felt
pom-pom novelty keychain|a fluffy pom-pom ball on a short cord|acrylic yarn; faux fur
tassel novelty keychain|a bunch of silky threads gathered in a cap, attached to a ring|silk thread; cotton thread
mini toolkit novelty keychain|a set of tiny folding tools such as a screwdriver and a knife-shaped opener|stainless steel
mini compass novelty keychain|a small round compass with a hinged lid|brass; plastic
mini hourglass novelty keychain|a tiny glass hourglass with coloured sand|glass and brass
miniature lantern novelty keychain|a tiny lantern with a LED light|metal and plastic
mini license-plate novelty keychain|a tiny metal plate with an embossed pattern|stamped metal
dice novelty keychain|a pair of small plastic dice hanging on a ring|plastic
puzzle novelty keychain|a small interlocking metal puzzle that comes apart and goes together|steel
mini game-console novelty keychain|a tiny console with a screen that plays a simple game|plastic
mini camera novelty keychain|a miniature camera with a viewfinder and a tiny picture reel|plastic
mini bottle novelty keychain|a tiny glass bottle with a cork stopper|glass and cork
lucky charm novelty keychain|a small tag with a clover, horseshoe or elephant charm|enamelled metal
mini bag novelty keychain|a miniature bag with handles hanging on a ring|leather; plastic
mini bike novelty keychain|a tiny bicycle with turning wheels|metal
mini lock and key novelty keychain|a miniature padlock and a tiny key|brass
fruit novelty keychain|a tiny model of a fruit such as a pineapple, strawberry or lemon|resin; felt
rubber duck novelty keychain|a small yellow rubber duck with a ring at the top|rubber; plastic
sea-shell novelty keychain|a real or moulded shell with a ring|shell; resin
LED sign novelty keychain|a tiny sign with a glowing word-less pattern|plastic
tiny mirror novelty keychain|a small round mirror in a frame|metal; plastic
mini fan novelty keychain|a small fan with turning blades powered by a battery|plastic
mini clock novelty keychain|a tiny clock with hands that move|metal; plastic
""")
CL = ["red","blue","green","yellow","orange","pink","purple","black","white","teal","lime green","silver","gold","turquoise","clear","smoke grey","magenta","navy"]
BRAND = {'Zippo-style': 'hinged-lid windproof', 'Dunhill-style': 'slim rolled-edge', 'zippo-style': 'hinged-lid windproof', 'dunhill-style': 'slim rolled-edge', 'bullet-style': 'cylinder-shaped'}
def build():
    G = {}
    for pre, rows in (('acc_lighter_plastic', LP), ('acc_lighter_novelty', LN), ('acc_keychain_plastic', KP), ('acc_keychain_novelty', KN)):
        G.update(V.group(pre, rows, CL, 6))
        G[f'{pre}_prompt'] = [f'__{pre}__']
    return G
def _wr(folder, name, lines): open(os.path.join(folder, name + '.txt'), 'w', encoding='utf8', newline='\n').write('\n'.join(lines) + '\n')
def _wire(folder, prefix=''):
    for fam in ('lighter', 'keychain'):
        for kind, extra in (('prompt', ['__acc_{f}_plastic_prompt__'] * 3 + ['__acc_{f}_novelty_prompt__'] * 3), ('short', ['__acc_{f}_plastic_short__'] * 3 + ['__acc_{f}_novelty_short__'] * 3)):
            p = os.path.join(folder, f'{prefix}acc_{fam}_{kind}.txt')
            if not os.path.exists(p): continue
            t = open(p, encoding='utf8').read().rstrip('\n').split('\n')
            add = [x.format(f=fam).replace('__acc_', '__' + prefix + 'acc_') for x in extra]
            if any(a in t for a in add): continue
            _wr(folder, f'{prefix}acc_{fam}_{kind}', t + add)
def _brand(folder, prefix=''):
    for f in glob.glob(os.path.join(folder, f'{prefix}acc_lighter*.txt')) + glob.glob(os.path.join(folder, f'{prefix}acc_keychain*.txt')):
        t = open(f, encoding='utf8').read(); u = t
        for a, b in BRAND.items(): u = u.replace(a, b)
        if u != t: open(f, 'w', encoding='utf8', newline='\n').write(u)
def run(final):
    G = build()
    for n, l in G.items(): _wr(final, n, l)
    _wire(final); _brand(final); print('lighters/keychains:', len(G), 'files'); return G
def export_aoo(out, prefix='aoo_'):
    G = build(); names_ = set(G); ref = re.compile(r'__([A-Za-z0-9_\-/]+)__'); n = 0
    for name, lines in G.items():
        keep = list(dict.fromkeys(ref.sub(lambda m: '__' + prefix + m.group(1) + '__' if m.group(1) in names_ else m.group(0), l) for l in lines))
        if not name.endswith('prompt'): random.Random(zlib.crc32(name.encode())).shuffle(keep)
        _wr(out, prefix + name, keep); n += 1
    _wire(out, prefix); _brand(out, prefix); return n
if __name__ == '__main__':
    a = [x for x in sys.argv[1:] if os.path.isdir(x)]; run(os.path.abspath(a[0]) if a else FINAL)
