"""Cufflinks, belts, brooches, watches, neckties and hair accessories."""
from vocab_lib import S
from vocab_acc_wardrobe2 import SL, P
NEW = ['cufflink', 'belt', 'brooch', 'watch', 'necktie', 'hairpiece']
CLS = {'cufflink': 'ear', 'belt': 'bag', 'brooch': 'ear', 'watch': 'ear', 'necktie': 'scarf', 'hairpiece': 'ear'}
TECHC = {'cufflink': 'metal', 'belt': 'bag', 'brooch': 'metal', 'watch': 'metal', 'necktie': 'knit', 'hairpiece': 'metal'}
PAIR = {'cufflink'}
def G(trim, finish, interior, hw, fr=("It is set with {}.", "It is accented with {}.", "It features {}.")):
    t = lambda k: list(k)
    return dict(trim=SL(list(fr), *t(trim)), finish=SL(["It has {}.", "The surface shows {}."], *t(finish)),
                interior=SL(["The reverse has {}.", "Inside it has {}.", "It is backed with {}."], *t(interior)), hardware=[SL(["It fastens with {}.", "It is secured by {}.", "It has {}."], *t(hw))])
SLOTS = {
 'cufflink': G(("a plain enamel dot, a glued-on gem, a printed pattern, a bright plating, a plastic stone, a simple stripe",
   "a hand-set coloured stone, a tiny enamelled motif, a mother-of-pearl face, a row of small crystals, an engraved initial-free pattern, a woven-silk knot, a hand-engraved border, a carved stone face",
   "a pavé of tiny diamonds, a hand-set sapphire, a hand-engraved border, a hand-painted miniature, a frieze of rubies, carved jade, a slice of meteorite, a guilloché enamel face"),
  ("a glossy shine, a matte coat, a plated surface, a smooth polish, a painted finish, a brushed look",
   "a satin finish, a hand-polished sheen, an oxidised patina, a brushed finish, a hammered texture, a high-gloss enamel, a lightly antiqued look",
   "a mirror polish, a deep enamel glow, a hand-chased texture, a luminous patina, a flawless polish, a velvety satin that glows"),
  ("a plain flat back, a basic swivel bar, a plain post, a simple chain link, a plain stamped back",
   "a swivel bar, a whale-back toggle, a bullet-back, a chain link, a fixed post, a hinged bar, a stud and clasp, a flexible link",
   "a hand-fitted gold swivel bar, a hand-hinged platinum toggle, a gold chain link, an engraved gold back, a secret compartment in the back"),
  ("a basic swivel, a plain post, a bullet-back, a fixed bar, a simple chain",
   "a whale-back, a swivel bar, a toggle, a stud, a chain link, a hinged closure, a bullet back",
   "a hand-fitted swivel in gold, a platinum toggle, a hand-made hinge, a gold chain link, a hidden catch")),
 'belt': G(("a plain buckle, a stitched edge, a printed stripe, a plastic keeper, a simple metal tip, a single row of eyelets, a rubber tip",
   "brass studs, a row of eyelets, a contrast stitched edge, a hand-tooled border, a braided panel, a patterned weave, an embossed pattern, a leather keeper, a metal end tip, a beaded strip",
   "hand-tooled floral carving, silver conchos, a hand-braided inlay, a gold buckle plate, a row of hand-set stones, a hand-stitched edge in silk thread, a hand-painted border, exotic inlay, gold-plated studs"),
  ("a matte coat, a glossy shine, a smooth surface, a plain dye, a wipe-clean coat, a lightly worn look",
   "a waxed finish, a burnished edge, a hand-rubbed sheen, a brushed nap, a polished grain, a patina that deepens with age, a satin shine",
   "a buttery hand, a mirror shine, a hand-burnished edge, a hand-polished glow, a deeply saturated dye, a silken nap"),
  ("a plain backing, a thin lining, no lining, a fabric lining, a plain flesh side",
   "a suede lining, a cotton lining, a smooth leather lining, a stitched-in lining, a soft felt lining, a canvas backing, a woven lining",
   "a silk lining, a hand-stitched leather lining, a lining of fine calfskin, a hand-sewn silk backing, a lining in suede with a hand-painted border"),
  ("a plain pin buckle, a basic slide buckle, a simple metal clip, a plastic clip, a snap, a velcro tab",
   "a pin buckle, a roller buckle, a plate buckle, a hook-and-bar clasp, a D-ring, a magnetic clasp, a solid brass buckle, a belt loop, a double-ring buckle, a sliding bar",
   "a hand-cast silver buckle, a hand-engraved gold buckle, a gem-set buckle, a hand-made plate buckle, a hand-carved horn buckle, a hand-forged buckle, a hidden clasp"),
  ("It is set with {}.", "It is finished with {}.", "It features {}.")),
 'brooch': G(("a few rhinestones, a bright enamel dot, a plain bead, a printed motif, a glued-on gem, a plated finish",
   "a cluster of seed pearls, a hand-set coloured stone, a row of small beads, a leaf of hammered metal, a dangling charm, a tiny enamelled flower, a wrapped wire coil, a carved bone charm, a feather accent",
   "a pavé of tiny diamonds, a cascade of pearls, a hand-set emerald, a hand-engraved border, a frieze of rubies, a granulated gold bead, a cluster of sapphires, a drop of carved jade, enamelled gold feathers"),
  ("a glossy shine, a matte coat, a bright plating, a painted finish, a smooth polish, a lightly textured surface",
   "a hand-polished sheen, an oxidised patina, a satin finish, a hammered texture, a high-gloss enamel, a lightly antiqued look",
   "a mirror polish, a hand-engraved shimmer, a deep enamel glow, a luminous patina, a hand-chased texture, a flawless polish"),
  ("a plain pin back, a basic safety catch, a plain bar pin, a simple clasp, a plain stamped back",
   "a sturdy pin and catch, a safety clasp, a locking pin back, a double-pin back, a swivel bail, a rolling catch, a hinged pin",
   "a hand-fitted gold pin and catch, a hand-hinged gold bail, a hand-engraved reverse, a platinum safety catch, a secret compartment in the back, a locket-style back"),
  ("a plain pin, a basic safety clasp, a simple bar pin, a plain catch",
   "a sturdy pin stem, a locking clasp, a rolling catch, a double pin, a swivel bail, a safety chain",
   "a hand-forged pin stem, a hand-fitted gold catch, a platinum clasp, a gold safety chain, a hidden catch")),
 'watch': G(("a plain bezel, a printed dial, a basic stitched strap, a plastic case, a simple crown, a painted marker",
   "a polished bezel, a coloured dial, applied markers, a sapphire-look crystal, a decorated case back, a domed crystal, a ribbed crown, a date window, a second hand with a counterweight, a coloured strap",
   "a diamond-set bezel, a hand-guilloché dial, a hand-enamelled dial, a hand-painted miniature dial, a moon-phase window, a visible skeleton movement, a gold case, a mother-of-pearl dial, a tourbillon window"),
  ("a glossy shine, a matte coat, a brushed finish, a smooth polish, a plated case, a plain coat",
   "a satin finish, a mixed brushed and polished case, a sunburst dial, an oxidised patina, a hammered texture, a hand-polished sheen",
   "a mirror polish, a deep enamel glow, a hand-chased case, a flawless polish, a luminous dial, a lacquer glow"),
  ("a plain case back, a basic quartz movement, a snap-on case back, a plain back, a thin battery",
   "a screw-down case back, a transparent case back, an automatic movement, a manual-wind movement, an engraved case back, a solar movement, a hacking movement",
   "a hand-wound movement with a hand-finished bridge, a skeleton movement, a hand-engraved case back, a tourbillon movement, a hand-decorated rotor, a hand-polished movement with blued screws"),
  ("a plain buckle, a basic pin buckle, a snap-on strap, a velcro strap, a plain clasp, a rubber strap",
   "a pin buckle, a deployant clasp, a quick-release strap, a fold-over clasp, a mesh strap, a leather strap, a nylon strap, a bracelet clasp, a butterfly clasp",
   "a hand-made gold buckle, a hand-sewn strap in fine leather, a gold butterfly clasp, a hand-finished bracelet, a platinum deployant, a hand-stitched strap in exotic leather")),
 'necktie': G(("a plain stripe, a printed dot, a simple label-free tip, a plain tipping, a bar tack",
   "a woven stripe, a hand-rolled edge, a woven pattern, a contrasting tipping, a repeat motif, a bar tack in contrast thread, a printed pattern, a knitted edge, a hand-turned tip",
   "a hand-rolled edge in silk, a hand-painted pattern, a hand-sewn tipping, a jacquard-woven motif, a gold-thread stripe, a hand-stitched bar tack, a hand-embroidered motif, a mother-of-pearl tack"),
  ("a matte look, a slight sheen, a stiff finish, a plain finish, a crisp finish",
   "a silky sheen, a textured weave, a soft hand, a grenadine texture, a matte linen look, a satin sheen, a washed texture, a brushed softness",
   "a hand that feels like air, a luminous silk sheen, a deep silken glow, a velvety depth, a hand-finished glow, a shimmer like water"),
  ("a plain polyester lining, a basic interlining, no lining, a thin lining",
   "a wool interlining, a silk lining, a cotton lining, a hand-set interlining, a tipping in matching fabric, a self-tipped lining, a traditional three-fold construction",
   "a hand-set wool interlining, a silk tipping, a six-fold construction, a hand-sewn silk lining, a hand-turned silk lining, a hand-finished slip stitch"),
  ("a plain loop, a basic keeper, a simple label, a plain tag",
   "a fabric keeper loop, a hand-sewn loop, a slip-stitch keeper, a narrow neck loop, a hook-and-eye tab, a hand-turned tip",
   "a hand-made silk keeper loop, a gold tie bar, a mother-of-pearl tie tack, a hand-sewn keeper, a gold chain keeper, a hand-turned silk tip"),
  ("It is finished with {}.", "It has {}.", "It features {}.")),
 'hairpiece': G(("a few rhinestones, a bright enamel dot, a plain bead, a printed pattern, a glued-on gem, a plastic flower",
   "a cluster of seed pearls, a hand-set coloured stone, a row of small beads, a leaf of hammered metal, a silk flower, a carved bone charm, a dangling charm, a feather, a small bow",
   "a pavé of tiny diamonds, a cascade of pearls, a hand-set emerald, a hand-engraved border, enamelled gold flowers, a granulated gold bead, a cluster of sapphires, hand-carved jade flowers, a hand-sewn silk blossom"),
  ("a glossy shine, a matte coat, a bright plating, a painted finish, a smooth polish, a lightly textured surface",
   "a hand-polished sheen, an oxidised patina, a satin finish, a hammered texture, a high-gloss enamel, a lightly antiqued look, a lacquer finish",
   "a mirror polish, a hand-engraved shimmer, a deep enamel glow, a luminous patina, a flawless polish, a velvety satin that glows"),
  ("a plain clip back, a basic spring, a plain comb, a simple elastic, a plain bobby-pin base",
   "a gripping clip, a spring clasp, a comb with teeth, a hair-friendly elastic, a snap clip, a French barrette back, a stick pin, a no-snag back, a double prong",
   "a hand-fitted gold barrette back, a hand-carved comb, a smooth horn comb, a hidden grip, a hand-sewn silk lining, a cushioned grip, a gold hair-stick shaft"),
  ("a plain clip, a basic elastic, a plain comb, a bobby-pin base, a simple spring",
   "a spring clasp, a snap clip, a French barrette clasp, a comb, a stick pin, a prong, a hair-friendly elastic, an alligator clip",
   "a hand-made barrette clasp, a hand-carved comb, a gold hair-stick, a hand-fitted spring, a silk-wrapped elastic")),
}
PRACT = {
 'cufflink': S("a secure back that will not slip, a flat low profile, a swivel for easy fastening, a tarnish-resistant coating, a hypoallergenic metal, a safety chain, a hidden engraved message, a wide base that sits flat, a scratch-resistant finish, a travel pouch, a spare back"),
 'belt': S("an adjustable fit, extra holes, a quick-release buckle, a hidden zipped pocket, a reversible strap, a reinforced edge, a wide support, a non-scratch buckle, a wipe-clean finish, a magnetic buckle, a stretch panel, a hidden key loop, a flat low profile"),
 'brooch': S("a secure locking back, a safety catch, a lightweight build, a tarnish-resistant coating, a hypoallergenic pin, a spare clutch, a wide base that sits flat, a hidden engraved message, a safety chain, a scratch-resistant finish, a hollow build to keep it light"),
 'watch': S("water resistance, a luminous dial, a scratch-resistant crystal, a date display, an alarm, a stopwatch, a second time zone, a tool-free strap change, a solar charge, a rotating bezel, a power-reserve indicator, shock resistance, an anti-magnetic movement, a hidden engraved message"),
 'necktie': S("a wrinkle-resistant weave, a stain-resistant finish, a hidden keeper loop, a clip-on option, a pre-tied knot, a reversible weave, a lightweight build, a washable fabric, a breathable weave, a snag-free finish, an anti-fray edge"),
 'hairpiece': S("a no-slip grip, a hair-friendly elastic, a snag-free edge, a lightweight build, a secure clip, a hidden spring, a strong hold, a flat low profile, a comfortable fit, a hypoallergenic metal, a no-crease finish, a washable fabric"),
}
PLACE = {
 'cufflink': S("on the face, on the front, on the back, on the link, on the edge, on the toggle"),
 'belt': S("at the buckle, at the tip, along the edge, on the keeper, at the centre, on the strap, on the inside"),
 'brooch': S("at the centre, on the front, on the border, on the back, on the pin, at the top, on the edge"),
 'watch': S("on the dial, on the case back, on the strap, on the bezel, on the crown, on the clasp"),
 'necktie': S("at the tip, at the back, at the centre, along the edge, on the keeper, on the blade"),
 'hairpiece': S("at the front, on the clip, on the back, on the edge, on the centre, on the comb"),
}
TYPES = {
 'cufflink': P("""whale-back cufflinks|They have a flat face and a swivelling bar that flips flat to pass through the cuff.
chain-link cufflinks|They join two faces with a short chain.
stud-and-post cufflinks|They have a fixed post and a pressed-on back.
silk-knot cufflinks|They are small knots of woven silk, joined by a thin elastic cord.
bullet-back cufflinks|They have a short bar that tips to a bullet shape to fasten.
mother-of-pearl cufflinks|They have round faces in iridescent shell.
enamel cufflinks|They have faces painted in glossy enamel.
guilloché cufflinks|They have faces engraved in fine repeating lines under translucent enamel.
gemstone cufflinks|They have a polished stone set in each face.
carved cameo cufflinks|They have small carved relief faces.
coin cufflinks|They are made from old coins, mounted on a bar.
button-style cufflinks|They are round and domed, like small buttons.
square cufflinks|They have crisp square faces.
oval cufflinks|They have smooth oval faces.
bar cufflinks|They have slim rectangular faces.
puzzle cufflinks|They hide a small moving puzzle in the face.
tiny working-dial cufflinks|They hold a small moving dial in each face.
dice cufflinks|They are tiny cubes with pips.
cog-and-gear cufflinks|They are made from small brass gears.
Japanese lacquer cufflinks|They have faces in black lacquer with a gold design.
Indian meenakari cufflinks|They have faces painted in coloured enamel in a floral design.
Persian turquoise cufflinks|They have faces of polished turquoise set in silver.
Maori greenstone cufflinks|They have small carved greenstone faces.
Navajo silver cufflinks|They have hand-stamped silver faces.
Celtic knot cufflinks|They have faces of interlaced knotwork.
Victorian gold cufflinks|They are oval gold cufflinks with a chased border.
Art Deco geometric cufflinks|They are sharp-lined cufflinks in stepped shapes.
shirt-stud and link sets|They are a set of cufflinks with matching shirt studs.
fabric button cufflinks|They are covered buttons joined with thread.
feather cufflinks|They have faces of tiny feathers under clear resin."""),
 'belt': P("""dress belt|It is a slim belt with a small polished buckle.
casual belt|It is a wider belt with a sturdy buckle.
braided belt|It is woven from several plaited strands.
woven stretch belt|It is a flexible woven belt with no holes.
web belt|It is a flat cotton web belt with a metal tip and a sliding buckle.
rope belt|It is a twisted cord belt tied at the front.
chain belt|It is a belt of metal links that hangs at the hip.
statement belt|It is a wide belt with a large decorative buckle.
corset belt|It is a wide, structured belt that cinches the waist.
obi-style belt|It is a broad soft sash tied at the back or the front.
cummerbund|It is a wide pleated sash worn at the waist.
sash belt|It is a long fabric sash that wraps around the waist.
tooled leather belt|It is carved with a hand-tooled pattern along its length.
western belt|It is a tooled belt with a big oval buckle and silver tips.
concho belt|It is a belt set with large round silver discs.
beaded belt|It is a belt woven from rows of tiny beads.
quilted belt|It is a belt of padded and stitched panels.
reversible belt|It is a belt with a different colour on each side.
tool belt|It is a wide belt with loops and pouches for work.
utility belt|It is a belt with several pockets and clips.
money belt|It is a flat belt with a hidden zipped pouch inside.
climbing harness belt|It is a strong woven belt with a locking buckle.
martial arts belt|It is a long cloth belt tied in a flat knot.
kilt belt|It is a wide leather belt with a heavy buckle.
tartan sash|It is a plaid sash worn across the body.
lace-up belt|It is a belt that closes with a laced front.
elastic waist belt|It is a wide stretchy belt for cinching a dress.
snake-chain belt|It is a smooth interlocked-link belt.
bolo-clasp belt|It is a belt that closes with a sliding clasp.
Maasai beaded belt|It is a wide beaded belt in bold colour bands.
Kente cloth sash|It is a woven strip sash in bright bands.
Mexican charro belt|It is an embroidered belt with ornate silver."""),
 'brooch': P("""floral brooch|It is a pin shaped like a flower.
bar brooch|It is a slim straight pin with a decorative front.
cameo brooch|It is an oval pin with a carved relief portrait.
circle brooch|It is a round pin with an open or filled centre.
animal brooch|It is a pin in the shape of a small creature.
insect brooch|It is a pin shaped like a beetle, bee or dragonfly.
bird brooch|It is a pin shaped like a bird.
star brooch|It is a star-shaped pin.
bow brooch|It is a pin shaped like a ribbon bow.
leaf-spray brooch|It is a pin made of a spray of leaves.
feather brooch|It is a pin shaped like a feather.
lapel pin|It is a small pin worn on a jacket collar.
tie tack|It is a short pin with a decorative head.
stick pin|It is a long pin with a decorative head.
hat pin|It is a long pin used to secure a hat.
shawl pin|It is a long pin used to fasten a wrap.
penannular brooch|It is an open ring brooch with a long pin, in the old Celtic style.
fibula brooch|It is an ancient safety-pin-style brooch, used to clasp a cloak.
Viking tortoise brooch|It is an oval dome brooch with a pierced openwork top.
Scottish kilt pin|It is a large pin with a decorative head, worn on a kilt.
luckenbooth brooch|It is a heart-shaped brooch topped with a crown.
Claddagh brooch|It is a brooch of two hands holding a crowned heart.
sweetheart brooch|It is a brooch shaped like a heart, in the old style.
mourning brooch|It is a dark brooch holding a lock of woven hair.
cluster brooch|It is a pin set with a cluster of stones.
enamel pin badge|It is a small hard-enamel pin with a clasp.
button badge|It is a round pin with a printed design.
patch pin|It is a woven patch with a pin back.
sculptural brooch|It is a large, art-like pin in mixed metals.
Mexican silver brooch|It is a hand-chased silver pin.
Georgian paste brooch|It is a brooch set with foil-backed paste stones.
Art Nouveau brooch|It is a flowing-line brooch with a woman's profile or a dragonfly.
Indian peacock brooch|It is a pin shaped like a peacock with enamelled feathers.
Russian enamel brooch|It is a brooch painted in bright shaded enamel."""),
 'watch': P("""dress watch|It is a slim round watch with a plain face.
field watch|It is a sturdy watch with a clear dial and a canvas strap.
diver's watch|It is a watch with a rotating bezel and a screw-down crown.
chronograph|It is a watch with sub-dials that time short intervals.
pilot's watch|It is a large watch with a clear dial and big numerals.
digital watch|It has a screen showing numbers.
smartwatch|It has a small touchscreen that shows information.
fitness watch|It tracks steps and heart rate with a rubber strap.
skeleton watch|It has an open dial showing the moving parts.
moon-phase watch|It shows the moon's phases in a small window.
tourbillon watch|It shows a rotating cage above the balance wheel.
pocket watch|It is a round watch that sits in a pocket, on a chain.
fob watch|It is a small watch pinned to the chest.
pendant watch|It is a small watch hung on a chain around the neck.
ring watch|It is a tiny watch set into a ring.
cuff watch|It is a watch set into a wide bracelet.
bangle watch|It has a rigid bangle band and a small dial.
chain-bracelet watch|It has a fine chain band and a small dial.
nurse's fob watch|It is a small watch with a big second hand, pinned to a uniform.
railway watch|It is a pocket watch with a very legible dial.
Art Deco watch|It is a rectangular watch with a stepped case.
tank watch|It is a long rectangular watch with a plain dial.
square watch|It has a square case.
tonneau watch|It has a barrel-shaped case.
oval watch|It has an oval case.
mechanical dive watch|It is a watch with a heavy case and a luminous dial.
ancient sundial pendant|It is a small portable sundial on a chain.
astronomical watch|It shows stars and the planets.
world-time watch|It shows the time in many cities at once.
chess-clock style watch|It is a bold square watch in a retro style.
cartoon-dial watch|It has a playful animated face.
wooden watch|It has a case and strap made of wood.
leather wrap watch|It wraps several times around the wrist.
enamel dial watch|It has a dial painted in glossy enamel.
Japanese quartz watch|It is a slim, precise watch with a clean dial."""),
 'necktie': P("""classic necktie|It is a long silk tie with a pointed end.
skinny tie|It is a very slim tie.
wide tie|It is a broad tie, in a retro style.
bow tie|It is a small tied bow worn at the collar.
pre-tied bow tie|It is a bow with an adjustable band at the back.
butterfly bow tie|It is a wide shaped bow.
clip-on tie|It is a tie with a clip in place of a knot.
knit tie|It is a flat-ended tie in a knitted weave.
wool tie|It is a textured tie woven from wool.
linen tie|It is a light tie in loosely woven linen.
bolo tie|It is a cord tie with a slide clasp.
string tie|It is a thin cord tie with a small knot.
ascot tie|It is a wide silk neckpiece tucked into an open collar.
cravat tie|It is a folded silk cloth tied loosely at the neck.
ribbon tie|It is a narrow ribbon tied at the throat.
pussy-bow tie|It is a soft bow attached to a blouse collar.
Kente cloth tie|It is a tie woven in strips of bright cloth.
tartan tie|It is a tie in a woven plaid.
paisley tie|It is a tie covered in teardrop swirls.
striped regimental tie|It is a tie with diagonal stripes.
polka-dot tie|It is a tie with a field of dots.
novelty tie|It is a tie printed with a playful design.
printed floral tie|It is a tie in a flower print.
bandana-print tie|It is a tie in a bandana pattern.
batik tie|It is a tie painted with wax-resist designs.
ikat tie|It is a tie with soft blurred patterns.
shibori tie|It is a tie folded and dyed in crisp patterns.
embroidered tie|It is a tie with embroidery along its length.
beaded bolo tie|It is a cord tie with a beaded slide.
tie with built-in tie bar|It has a bar sewn in.
Japanese silk tie|It is a tie in fine silk with a small woven pattern.
Indian silk tie|It is a tie in rich silk with woven motifs."""),
 'hairpiece': P("""hair clip|It is a spring clip that holds a section of hair.
claw clip|It is a large toothed clip that gathers the hair.
barrette|It is a metal bar fastener for the hair.
French barrette|It is a long hinged clasp that holds a twist.
bobby pins|They are small pins slid into the hair.
decorative hairpins|They are fine pins with ornamental tops.
hair sticks|They are long sticks slid through a bun.
hair fork|It is a two-pronged pin pushed through a bun.
hair comb|It is a decorative comb slid into the hair.
tiara comb|It is a small crown-shaped comb.
tiara|It is a jewelled band worn on the head.
circlet|It is a plain band worn on the brow.
flower crown|It is a ring of fresh or silk flowers.
laurel wreath|It is a wreath of leaves, worn on the head.
headband|It is a narrow band that follows the curve of the head.
padded headband|It is a thick padded band.
knotted headband|It is a wide cloth band with a twist at the front.
hairband|It is a thin plastic or metal band.
scrunchie|It is a gathered fabric band for a ponytail.
ribbon|It is a long ribbon tied around a ponytail or braid.
hair bow|It is a large bow clipped to the hair.
hair wrap|It is a long cloth wound round a braid or bun.
hair cuff|It is a metal tube slid onto a braid.
hair rings|They are small beaded rings threaded into locs or braids.
beaded braid clips|They are strings of beads on a clip.
tikka|It is a jewel hung from a chain on the forehead.
maang tikka|It is a forehead jewel worn at the hair parting.
matha patti|It is a decorative chain along the hair parting.
jooda pin|It is a decorated pin for a bun.
kanzashi|It is a traditional Japanese hairpin with a flower or tassel.
hair net|It is a fine net that holds hair in place.
snood|It is a bag-like net worn at the back of the head.
feather fascinator|It is a small decorated piece worn on a clip.
bridal veil comb|It is a comb that holds a veil.
hair chain|It is a fine chain draped through the hair.
pearl hairpins|They are pins topped with pearls."""),
}
WEAR = {'cufflink': ['wearing {} at the cuffs', 'with {} fastened at the wrists', 'showing {} at the shirt cuffs', 'adjusting {} on one cuff'],
 'belt': ['wearing {} at the waist', 'with {} cinched at the waist', 'wearing {} slung low on the hips', 'with {} over a long top'],
 'brooch': ['wearing {} pinned to the lapel', 'with {} pinned at the collar', 'wearing {} on the shoulder', 'with {} pinned at the chest'],
 'watch': ['wearing {} on the wrist', 'checking {} on one wrist', 'with {} showing beneath a cuff', 'wearing {} on the left wrist'],
 'necktie': ['wearing {} knotted at the collar', 'with {} loosened at the neck', 'wearing {} neatly knotted', 'adjusting {} at the collar'],
 'hairpiece': ['wearing {} in the hair', 'with {} pinned above the ear', 'wearing {} at the crown', 'with {} holding up the hair']}
