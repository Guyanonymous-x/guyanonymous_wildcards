"""Cigarette cases, lighters and contact lenses (colour-changing, novelty, cosmetic)."""
from vocab_lib import S
from vocab_acc_wardrobe2 import SL, P
from vocab_acc_wardrobe3 import SLOTS as S3
from vocab_acc_wardrobe4 import HW
NEW = ['cigcase', 'lighter', 'contact']
CLS = {'cigcase': 'ear', 'lighter': 'ear', 'contact': 'lens'}
TECHC = {'cigcase': 'metal', 'lighter': 'metal', 'contact': 'lens'}
PAIR = {'contact'}
MATS = {'lens': {'low': S("soft hydrogel, thin hydrogel, plain disposable hydrogel, standard soft polymer, basic tinted hydrogel, daily-wear soft polymer, printed hydrogel, light-tint polymer"),
  'mid': S("silicone hydrogel, breathable silicone hydrogel, hydrophilic soft polymer, UV-blocking silicone hydrogel, moisture-lock hydrogel, layered-tint silicone hydrogel, gas-permeable polymer, enclosed-print hydrogel, soft toric polymer"),
  'high': S("custom-fitted silicone hydrogel, hand-painted scleral polymer, custom-printed gas-permeable polymer, premium moisture-lock silicone hydrogel, prosthetic-grade painted polymer, hand-layered scleral lens material, photochromic polymer, ultra-thin breathable polymer")}}
CONS = {'lens': {'low': S("machine-tinted, printed with a flat colour, pad-printed, moulded in one piece, edge-trimmed"), 'mid': S("multi-layer printed, enclosed-tint, pad-printed in three layers, hand-checked, edge-polished"), 'high': S("hand-painted layer by layer, custom-fitted, individually sculpted, hand-finished, painted under a clear dome")}}
TECHLENS = ({'low': S("printed in a flat ring, printed with a simple iris pattern, tinted evenly, printed with a dot pattern"), 'mid': S("printed in layered dots, printed with a radial iris pattern, printed with a limbal ring, printed with a gradient tint, printed with a swirl"), 'high': S("hand-painted iris detail, hand-painted limbal ring, hand-painted fibres in the iris, layered pigment under a clear dome, hand-applied glitter flecks, hand-painted glow pigment")}, S("across the whole iris, around the edge, near the pupil, in the centre, at the limbal ring, in a ring"))
SLOTS = {
 'cigcase': dict(trim=S3['brooch']['trim'], finish=S3['brooch']['finish'], interior=SL(["Inside it has {}.", "The interior has {}."], "a plain elastic band, a basic plastic divider, an open pocket, a simple spring strap", "an elastic band, a leather-lined divider, a spring-loaded holder, a felt-lined interior, a hinged flap, a satin lining, a soft cloth lining", "a hand-fitted suede interior, a silk-lined interior, a gold-plated spring, a hand-sewn leather lining, a hand-engraved inner panel, a velvet-lined compartment"), hardware=HW(["It opens with {}.", "It has {}."], "a plain snap, a basic spring flap, a simple clasp, a plain lid", "a push-button latch, a hinged lid, a spring flap, a magnetic catch, a slide-open lid, a thumb notch, a hinged front", "a hand-fitted gold hinge, a concealed catch, a hand-made hinged lid, a gold push-button, a hand-polished slide, a hidden magnetic catch")),
 'lighter': dict(trim=S3['brooch']['trim'], finish=S3['brooch']['finish'], interior=SL(["Inside it has {}.", "The mechanism has {}."], "a plain wick, a basic flint wheel, a simple gas tank, a plain striker", "a refillable fuel tank, an adjustable flame, a sparking wheel, a windproof chimney, a flint wheel, a cotton wick, a piezo igniter, a sealed sealed fuel reservoir", "a hand-fitted gold mechanism, a hand-polished chimney, a hand-engraved inner case, a hand-tuned striker, a gold-plated chimney"), hardware=HW(["It opens with {}.", "It has {}."], "a plain flip lid, a basic thumb wheel, a simple push button, a plain cap", "a flip-top lid, a spring hinge, a snap-shut cap, a roller wheel, a thumb flint wheel, a windproof hood, a click-open lid, a swivel cap", "a hand-fitted hinged lid, a gold thumb wheel, a hand-made hinge, a satin-smooth flip lid, a gold flint wheel, a hand-polished hood")),
 'contact': dict(trim=SL(["The iris shows {}.", "It is patterned with {}.", "It has {}."], "a flat colour ring, a simple dot pattern, a plain tint, a basic radial line, a flat painted ring", "a layered iris pattern, a defined limbal ring, a soft gradient from centre to edge, a radial fibre pattern, a swirl of two shades, a glowing ring, a starburst, a speckled iris, a ring of tiny flecks", "hand-painted fibres in several shades, a hand-painted limbal ring, a luminous starburst, layered pigment under a clear dome, a swirl of hand-mixed colours, flecks of metallic pigment, hand-painted flames, hand-painted tiny constellations"),
  finish=SL(["It has {}.", "The lens shows {}."], "a clear edge, a plain gloss, a thin tint layer, a flat shine", "a soft matte tint, a clear glossy dome, a mirror-sheen ring, a satin edge, a glow-in-the-dark layer, a pearl sheen", "a mirror-polished dome, a luminous pearl sheen, an opalescent shift of colour, a hand-polished edge, a prismatic shimmer"),
  interior=SL(["The lens is {}.", "It has {}."], "a clear centre, a basic pupil opening, a plain clear pupil", "a clear pupil opening, a tinted outer ring, a transparent centre, a sheer tint over the pupil, a light-reactive layer", "a custom pupil opening, a hand-painted pupil, a colour-shifting layer, a light-reactive layer that changes colour in the sun, a hand-fitted clear centre"),
  hardware=HW(["It is {}.", "It fits {}."], "a plain thin edge, a daily-wear disposable, a basic soft lens, a one-day lens", "a thin comfortable edge, a one-day disposable, a two-week lens, a monthly lens, a soft comfortable fit, a shaded-edge fit, a rounded edge", "a custom-fitted lens, a hand-finished edge, a lens moulded to the wearer's eye, a scleral fitting, a hand-polished edge")),
}
PRACT = {
 'cigcase': S("a slim flat profile, a spring-loaded holder, a magnetic catch, an elastic band, a hidden mirror, a scratch-resistant finish, a hard shell, a water-resistant seal, a snug fit, a pocket-friendly shape"),
 'lighter': S("an adjustable flame, a windproof build, a refillable tank, a safety catch, a safety lock, a snug lid, a flint spare, a flat pocket-friendly shape, a long-lasting wick, a visible fuel gauge"),
 'contact': S("UV protection, a moisture-lock layer, a comfortable thin edge, a tint that does not reduce vision, a clear pupil opening, an easy-handling tint, a daily-disposable build, a breathable material, a fit that stays centred"),
}
PLACE = {'cigcase': S("on the lid, on the front, on the back, on the hinge, on the edge, on the inside"), 'lighter': S("on the lid, on the body, on the wheel, on the base, on the front, on the side"), 'contact': S("on the iris, near the pupil, at the edge, around the limbal ring, across the lens, in the centre")}
TYPES = {
 'cigcase': P("""slim flip-top cigarette case|It is a flat metal case with a hinged lid.
engine-turned silver cigarette case|It is a case with an all-over machined pattern.
enamelled cigarette case|It is a case with a painted enamel lid.
leather-covered cigarette case|It is a case wrapped in stitched leather.
Art Deco cigarette case|It is a case with a stepped geometric lid.
Victorian silver cigarette case|It is a case with a chased border and a gilt interior.
Russian niello cigarette case|It is a silver case with black-inlay scenes.
Persian lacquer cigarette case|It is a case painted with tiny scenes in lacquer.
Japanese lacquer cigarette case|It is a black case with a gold design.
mother-of-pearl cigarette case|It is a case inlaid with iridescent shell.
tortoiseshell-look cigarette case|It is a case in amber-toned laminated shell.
wooden cigarette case|It is a case turned from fine wood.
carved bone cigarette case|It is a case with a carved bone lid.
compact slide cigarette case|It slides open on one side.
double-sided cigarette case|It opens at both ends.
spring-loaded cigarette case|It has a spring that presents the contents.
case-and-lighter combination|It is a case with a built-in lighter.
case with built-in mirror|It has a small mirror inside the lid.
pocket cigarette tin|It is a flat tin with a hinged lid.
beaded cigarette pouch|It is a small beaded case.
jewelled evening cigarette case|It is a flat case set with stones.
guilloché cigarette case|It is a case with fine engraved lines under enamel.
fabric-covered cigarette case|It is a case covered in embroidered silk.
aluminium cigarette case|It is a light, simple case.
hard-shell cigarette case|It is a hard plastic case.
leather wallet-style cigarette holder|It is a folding leather holder.
brass cigarette case|It is a brass case with a worn patina.
gold cigarette case|It is a smooth case in yellow gold.
vintage military cigarette case|It is a plain tough metal case.
novelty printed cigarette case|It is a case with a playful printed lid."""),
 'lighter': P("""flip-top lighter|It has a hinged lid that clicks shut.
wheel lighter|It has a thumb wheel that strikes a flint.
windproof lighter|It has a metal hood around the flame.
Zippo-style lighter|It is a hinged metal lighter with a chimney.
pocket gas lighter|It is a slim refillable gas lighter.
disposable lighter|It is a light plastic lighter.
Dunhill-style lighter|It is a slim rectangular lighter.
Art Deco table lighter|It is a heavy lighter for a table.
table lighter|It is a large decorative lighter.
pipe lighter|It has an angled flame.
torch lighter|It has a strong narrow flame.
jet-flame lighter|It has a blue jet flame.
electric arc lighter|It uses a small spark and has no flame.
plasma lighter|It makes a spark from a rechargeable battery.
candle lighter|It is a long, slim lighter.
fireplace lighter|It is a long lighter with a trigger.
match case lighter|It holds matches and a striker.
engraved brass lighter|It is a brass lighter with a hand-engraved lid.
enamelled lighter|It has a painted enamel body.
lacquered lighter|It has a glossy lacquered body.
leather-wrapped lighter|It has a stitched leather covering.
gold-plated lighter|It has a golden finish.
silver lighter|It has a smooth silver case.
chrome lighter|It has a bright mirror finish.
novelty figure lighter|It is shaped like a small figure.
skull-shaped lighter|It is shaped like a skull.
bullet-style lighter|It is shaped like a brass cartridge.
animal-shaped lighter|It is shaped like a small animal.
lantern-style lighter|It is shaped like a little lantern.
vintage trench lighter|It is a plain, tough lighter from wartime."""),
 'contact': P("""colour-changing contact lenses|They shift colour in the light or with the wearer's mood.
natural-tint contact lenses|They give a subtle natural change of colour.
enhancement-tint contact lenses|They deepen the natural colour.
opaque-tint contact lenses|They fully cover the natural colour with a new one.
gradient-tint contact lenses|They shade from one colour at the pupil to another at the edge.
circle contact lenses|They are slightly larger and give a wide-eyed look.
anime-style big-iris contact lenses|They give a large, doll-like iris.
cat-eye contact lenses|They have a slit pupil like a cat.
dragon-eye contact lenses|They have a slit pupil and scales across the iris.
snake-eye contact lenses|They have a vertical slit and patterned scales.
wolf-eye contact lenses|They have an amber iris with dark flecks.
vampire contact lenses|They are red or amber with a dark ring.
zombie contact lenses|They are clouded white with a thin dark ring.
blind-look white-out contact lenses|They cover the iris and pupil with a milky white.
sclera-look full-eye contact lenses|They cover the whole visible eye with a single colour.
black-out contact lenses|They cover the whole visible eye in black.
mirror-finish contact lenses|They have a metallic reflective surface.
UV-reactive contact lenses|They glow under black light.
glow-in-the-dark contact lenses|They glow softly in the dark.
starburst contact lenses|They have lines radiating from the pupil.
spiral contact lenses|They show a hypnotic spiral around the pupil.
checkerboard contact lenses|They show a tiny checker pattern.
flame contact lenses|They show a ring of flames.
galaxy contact lenses|They show a swirl of stars and nebulae.
cracked-glass contact lenses|They show fine cracks across the iris.
heart-pupil contact lenses|They have a heart-shaped pupil.
star-pupil contact lenses|They have a star-shaped pupil.
cross-pupil contact lenses|They have a cross-shaped pupil.
spiderweb contact lenses|They show a web across the iris.
clock-face contact lenses|They show a small clock dial across the iris.
mosaic contact lenses|They show a pattern of tiny coloured tiles.
rainbow contact lenses|They show bands of every colour.
emoji-style contact lenses|They show a small emoji face on the iris.
scleral costume lenses|They are large lenses that rest on the white of the eye.
prosthetic-style painted lenses|They are custom hand-painted to look like a real iris.
duo-colour split contact lenses|They have two halves in different colours.
eclipse contact lenses|They show a dark disc with a glowing ring.
rimmed limbal contact lenses|They have a bold dark ring at the edge of the iris.
ombre contact lenses|They fade softly from one colour to another.
sparkle-fleck contact lenses|They are dusted with metallic flecks."""),
}
WEAR = {'cigcase': ['holding {}', 'taking {} from a pocket', 'with {} in one hand', 'opening {}'],
        'lighter': ['holding {}', 'with {} in one hand', 'flicking {}', 'with {} resting on a table'],
        'contact': ['wearing {}', 'with eyes showing {}', 'looking straight ahead wearing {}', 'with a close view of the eyes wearing {}']}
