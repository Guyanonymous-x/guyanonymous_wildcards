"""Slots, practical features, placements, item types, traditions, motifs and wearing verbs for earrings, gloves, scarves and tights."""
from vocab_lib import S
def P(t): return [tuple(x.split('|')) for x in t.strip().split('\n') if x.strip()]
def SL(frames, low, mid, high): return dict(frames=frames, low=S(low), mid=S(mid), high=S(high), tails=None)
SLOTS = {
 'earring': dict(
  trim=SL(["It is set with {}.", "It is accented with {}.", "It features {}."],
    "a few rhinestones, a bright enamel dot, a plain bead, a small plastic charm, a printed pattern, a glued-on gem, a tiny painted flower, a shiny metal ball, a simple tassel, a coloured resin bead",
    "a cluster of seed pearls, a hand-set coloured stone, a row of small beads, a leaf of hammered metal, a dangling charm, a tiny enamelled flower, a wrapped wire coil, a feather drop, a bead fringe, a tassel of silk thread, a carved bone charm, an engraved disc",
    "a pavé of tiny diamonds, a cascade of pearls, a hand-set emerald, a hand-engraved border, a frieze of rubies, a granulated gold bead, a cluster of sapphires, a drop of carved jade, a feather of enamelled gold, a tassel of hand-knotted silk and gold, a hanging pearl on a gold chain"),
  finish=SL(["It has {}.", "The surface shows {}."],
    "a glossy shine, a matte coat, a bright plating, a painted finish, a smooth polish, a lightly textured surface, a uniform colour coat, a brushed look",
    "a hand-polished sheen, an oxidised patina, a satin finish, a hammered texture, a brushed finish, a high-gloss enamel, a lightly antiqued look, a hand-burnished edge, a soft rose-gold wash",
    "a mirror polish, a hand-engraved shimmer, a deep enamel glow, a luminous patina, a hand-chased texture, a flawless polish, a lustre like candlelight, a velvety satin that glows"),
  interior=SL(["It has {}.", "The back has {}."],
    "a plain post, a butterfly back, a basic hook wire, a plain clutch, a plain clip, a simple hoop wire, a lever back, a push-back",
    "a hypoallergenic post, a secure screw-back, a comfortable clip pad, a safety back, a hinged hoop, a soft silicone pad, a fish-hook wire, a latch back, a French wire, an invisible clip",
    "a gold screw-back with a hidden catch, a platinum post, a hand-fitted lever back, a hinged snap with a gold safety, a hand-formed ear wire, a cushion of soft leather behind the lobe, an invisible hand-set clip"),
  hardware=[SL(["It hangs from {}.", "{} holds it in place.", "It fastens with {}."],
    "a plain hook wire, a plain post, a basic clip-on, a simple hoop, a ring clasp, a stud with a butterfly back",
    "a French hook, a lever back, a sturdy post, a latch closure, a screw back, a hinged hoop, a sleeper hoop, a threader chain, a comfortable clip-on",
    "a hand-formed gold ear wire, a hand-engraved lever back, a platinum post, a hand-fitted hinged hoop, a gold clip mounted to the wearer's ear, a jewelled sleeper hoop")]),
 'glove': dict(
  trim=SL(["They are trimmed with {}.", "They have {}.", "{}."],
    "a plain cuff, a ribbed wrist, a contrast stitch line, a bow at the wrist, a printed band, a simple button, an elastic wrist, a faux-fur edge",
    "a fur cuff, a knitted cuff, a pearl button at the wrist, a lace edge, a leather strap and buckle, a contrast welt, a bow, a decorative stitch line, a rolled cuff, an embroidered cuff, a row of tiny buttons, a patterned band",
    "a mink-style cuff, a band of hand-sewn pearls, a hand-embroidered wrist, a hand-beaded cuff, a hand-sewn silk bow, a rim of crystals, a row of mother-of-pearl buttons, a gold-thread cuff, a feather edge, a hand-cut lace trim"),
  finish=SL(["They have {}.", "The surface shows {}."],
    "a matte coat, a glossy shine, a smooth finish, a plain dye, a wipe-clean coat, a slight sheen, a dull finish, a printed finish",
    "a soft suede nap, a burnished edge, a waxed finish, a satin shine, a brushed nap, a hand-rubbed sheen, a polished grain, a hand-felted fuzz, a water-repellent coat, a washed softness",
    "a buttery hand, a mirror shine, a hand-burnished surface, a silken nap, a deeply saturated dye, a hand-polished glow, a velvety touch, a pearl-like lustre"),
  interior=SL(["They are lined with {}.", "The inside is {}.", "Inside they have {}."],
    "a thin polyester lining, no lining, a basic fleece lining, a plain jersey lining, a thin acrylic lining, a cotton lining",
    "a silk lining, a cashmere lining, a lambswool lining, a fleece lining, a rabbit-fur lining, a fine jersey lining, a Thinsulate-style insulation, a quilted lining, a wool-blend lining, a rayon lining",
    "a silk lining embroidered with a monogram, a cashmere lining, a mink-style lining, a hand-sewn silk lining, a rabbit-fur lining, a sable-style lining, a gold-lamé lining, a lining of Persian lamb"),
  hardware=[SL(["They close with {}.", "They have {}.", "At the wrist they have {}."],
    "an elastic wrist, a plain cuff, a velcro strap, a snap closure, a plain button, a drawstring cord, a stretch cuff",
    "a snap closure, a buckled wrist strap, a zipper at the wrist, a press stud, a leather lace, a hook and loop tab, a drawstring toggle, a touchscreen fingertip patch, a pull tab, a magnetic closure, a wrist cord",
    "a pearl button, a gold press stud, a hand-sewn hook and eye, a tiny gold buckle, a silk ribbon tie, a row of mother-of-pearl buttons, a hand-laced wrist, a concealed magnetic closure")]),
 'scarf': dict(
  trim=SL(["It is edged with {}.", "It has {}.", "{} finishes the ends."],
    "a plain hem, a short fringe, a printed border, a raw edge, simple tassels, an overlocked edge, a plain stripe at each end, pom-poms",
    "a knotted fringe, a hand-rolled hem, hand-tied tassels, a contrast border, a tassel at each corner, a fine stripe, a lace edge, a patchwork border, a twisted fringe, a pom-pom edge, a woven border of geometric shapes, a block-printed border",
    "a long hand-knotted silk fringe, a hand-rolled hem, a gold-thread border, a border of hand-sewn pearls, a fringe of crystal beads, a hand-embroidered edge, a hem of chinchilla-style fur, a border of fine lace, silk tassels with gold wrapping, a feather trim"),
  finish=SL(["It has {}.", "The cloth has {}."],
    "a soft hand, a light sheen, a matte surface, a slightly stiff finish, a light brushed feel, a shiny coat, a plain wash",
    "a brushed softness, a crinkled finish, a silky sheen, a washed linen look, a lightly felted surface, a gauzy softness, a mercerised glow, an airy drape, a woven texture, a pleated finish",
    "a hand that feels like air, a luminous sheen, a cloud-like softness, a gossamer drape, a hand-pleated finish, a shimmer like water, a silky glow, a velvet depth, a hand-finished glow"),
  interior=SL(["The reverse is {}.", "It is {} on the back.", "On the back it has {}."],
    "the same print, a plain solid colour, a plain white back, a simple contrast colour, the same colour, a fleece back",
    "a contrasting colour, a fine stripe, a softly brushed fleece, a satin back, a contrasting print, a matching print, a velvet back, a woven check, a quilted back",
    "a plain silk back in a contrasting colour, a hand-painted reverse, a different pattern on each side, a double-faced weave in two colours, a silk lining, a cashmere reverse, a contrast of velvet and silk"),
  hardware=[SL(["It has {}.", "It is held by {}.", "It fastens with {}."],
    "a plain loop, no fastening, a simple knot, a snap, a plain button, a ring, a basic pin",
    "a decorative brooch, a shawl pin, a scarf ring, a button closure, a toggle, a hidden snap, a clip, a leather tab, a wooden ring, a metal ring, a hidden clasp, a loop and toggle",
    "a hand-made brooch, a jewelled shawl pin, a gold scarf ring, a pearl brooch, a hand-carved bone toggle, a silver pin, a hand-engraved clasp, a diamond-set pin, a jewelled slide")]),
 'tights': dict(
  trim=SL(["They have {}.", "{}."],
    "a plain waistband, a printed band, a contrast waist, a simple stripe, a plain toe, a plain gusset, an elastic waist",
    "a comfort waistband, a contrast toe, a reinforced toe, a seam up the back, a patterned panel, a ribbed cuff at the ankle, a lace panel, a flat-seam toe, a bow at the ankle, a contrast heel",
    "a hand-embroidered motif at the ankle, a row of hand-sewn crystals at the back, a hand-finished seam, a hand-beaded edge, a lace top, a seam in silk thread, a hand-linked toe, a gold-thread waistband, a pearl at each ankle"),
  finish=SL(["They have {}.", "The knit has {}."],
    "a matte look, a slight sheen, a smooth surface, a stretch fit, a plain finish, a soft hand, a shiny look",
    "a sheer silky look, a soft brushed interior, a velvety opaque finish, a satin sheen, a fine ribbed texture, a lightly textured surface, a smooth second-skin look, a glossy look",
    "a second-skin silk look, a luminous sheen, a gossamer sheerness, a velvety depth, a hand that feels like air, a shimmer like moonlight, a pearlescent sheen"),
  interior=SL(["They have {}.", "{}."],
    "a plain gusset, a basic elastic waist, a thin cotton crotch, a simple flat seam, a plain toe",
    "a cotton gusset, a fleece lining, a comfortable waistband, a seamless toe, a reinforced heel and toe, a control panel, a graduated-compression panel, a soft inner lining, a smooth flat-seam finish",
    "a hand-finished silk gusset, a cashmere lining, a hand-linked toe, a hidden silicone grip at the waist, a hand-shaped heel, a silk-lined waistband, a gusset in fine silk"),
  hardware=[SL(["They {}.", "They have {}."],
    "have a plain elastic waist, have a flat toe seam, have a basic gusset, have a straight cut, have a plain waistband",
    "have a wide comfortable waistband, are footless with a stirrup, have a convertible foot, have a seam up the back, have a reinforced toe, have a non-slip grip at the waist, are full-length with a foot, are cut to the ankle",
    "have a hand-finished waistband, have a hand-linked toe, have a hand-sewn seam up the back, have a hidden silicone grip, have a hand-shaped gusset, are made to the wearer's measurements")]),
}
PRACT = {
 'earring': S("a hypoallergenic post, a lightweight build that is comfortable all day, a secure locking back, a soft silicone pad, a tarnish-resistant coating, a nickel-free metal, a lever back that will not open, a safety chain, a hidden engraved message, a wide base that sits flat, a gentle clip with a cushion, a sleep-safe low profile, a waterproof coating, a scratch-resistant finish, a hollow build to keep it light, a posts-and-backs spare set"),
 'glove': S("touchscreen fingertips, a grip palm, a reinforced thumb, a padded palm, a waterproof membrane, a wind-blocking layer, reflective piping, a wrist cord, a hook and loop wrist strap, a pull tab, a zipped pocket for a key, a nose-wipe patch, a pre-curved fit, insulated fingers, an anti-slip print, a cut-resistant lining, a heated panel"),
 'scarf': S("a hidden zipped pocket, a magnetic closure, a hood that folds out, a hidden thumbhole, a water-repellent finish, a packable build, a reversible weave, a UPF 50 weave, a built-in snap, a fleece-lined section, a reflective thread, a hidden phone pocket, an anti-fray edge, a breathable weave, a lightweight build, a wrinkle-resistant weave"),
 'tights': S("a comfortable waistband, a cotton gusset, reinforced toes, a non-roll waist, a graduated-compression panel, moisture-wicking fibres, a laddering-resistant knit, an anti-static finish, a seamless toe, a control panel, thermal fleece lining, a non-slip grip, a run-resistant weave, UV protection, a firm flat seam, a stretch that recovers"),
}
PLACE = {
 'earring': S("on the lobe, on the hook wire, on the post, on the back, on the dangling charm, on the front face, on the hoop, on the bottom drop"),
 'glove': S("on the cuff, on the back of the hand, on the thumb, on the fingertips, on the wrist, on the palm, on the first finger, at the side seam"),
 'scarf': S("at one end, at a corner, on the fringe, along the edge, at the centre, on the reverse, on a tassel, on the border"),
 'tights': S("at the ankle, on the thigh, up the back of the leg, on the waistband, on the toe, at the knee, on the calf, along the side"),
}
TYPES = {
 'earring': P("""stud earrings|They are small fixed earrings that sit flat against the lobe on a post.
hoop earrings|They are round rings of metal that pass through the lobe.
huggie hoops|They are small snug hoops that hug the lobe.
drop earrings|They hang straight down from the lobe on a short post.
dangle earrings|They swing freely on a long drop.
chandelier earrings|They fan out into tiers of hanging pieces.
threader earrings|They are fine chains that thread through the lobe and hang on both sides.
ear climbers|They curve upward along the edge of the ear.
ear cuffs|They clasp to the rim of the ear with no piercing needed.
clip-on earrings|They clip to the lobe with a padded clip and need no piercing.
jhumka earrings|They are bell-shaped domes that hang from a stud, with small beads or pearls along the lower edge.
chandbali earrings|They are crescent-shaped earrings with a decorated moon-shaped lower edge.
kundan earrings|They are broad earrings set with polished stones in gold foil, often with a pearl drop.
Maasai beaded disc earrings|They are flat circular beaded discs in bold colour bands that hang from a stretched lobe.
Fulani gold crescent earrings|They are large, sweeping crescents of gold, thin and light at the tips.
Berber silver earrings|They are heavy silver earrings with enamel inlay and coral or glass beads.
Tibetan turquoise and coral earrings|They are large drop earrings set with turquoise and coral in silver.
Mexican silver filigree earrings|They are delicate, open filigree earrings with fine wire swirls.
penannular earrings|They are open rings with a gap, in the ancient Southeast Asian style.
mizuhiki paper-cord earrings|They are light earrings knotted from coloured paper cord.
Navajo silver and turquoise earrings|They are hand-stamped silver earrings set with turquoise stones.
Haida carved earrings|They are carved earrings with formline animal designs.
Ethiopian gold drop earrings|They are fine hanging earrings with filigree work in gold.
Bedouin coin earrings|They are earrings hung with small coins that chime softly.
Persian enamel earrings|They are enamelled earrings painted with tiny floral scenes.
Thai gold dangle earrings|They are long, tiered gold earrings set with small stones.
Balinese silver granulation earrings|They are silver earrings covered in tiny silver grains and spirals.
Nordic silver sølje earrings|They are pierced silver discs that shimmer and hang on rings.
girandole earrings|They have a central stone with three pendant drops below.
Victorian jet drop earrings|They are black polished drops in a carved style.
Art Deco geometric earrings|They are sharp-lined earrings in stepped and angled shapes.
mod enamel flower earrings|They are bold, flat enamelled flowers in bright colours.
ear spools|They are broad flat discs worn in a stretched lobe, in the ancient Andean style.
flesh tunnel plugs|They are hollow rings worn in a stretched lobe.
lobe stretcher plugs|They are solid carved plugs in wood, bone, stone or glass for stretched lobes.
helix cuffs|They wrap around the upper rim of the ear.
conch hoops|They are broad hoops worn in the inner ear.
ear jackets|They sit behind the lobe and show a second piece in front.
front-and-back earrings|They show a post at the front and a second piece peeking out from behind.
mismatched earrings|They are a deliberately different pair, one in each ear.
asymmetrical pair earrings|They are a pair in which one drop is longer than the other.
beaded fringe earrings|They hang in a wide fan of beaded strands.
feather earrings|They are light drops of feathers on a hook.
tassel earrings|They hang in a soft cascade of thread.
shell earrings|They are carved or whole shell pieces on a hook.
sculptural earrings|They are miniature sculptures in metal, glass or clay.
gemstone cluster earrings|They are clusters of mixed gemstones, set close together."""),
 'glove': P("""dress gloves|They are slim gloves in thin leather or fabric, sitting snug at the wrist.
opera gloves|They are long, elegant gloves that reach above the elbow.
evening gloves|They are slim gloves, often in satin or lace, ending at the wrist or the forearm.
wrist-length gloves|They end neatly at the wrist.
driving gloves|They are slim, snug gloves with open knuckles and a grippy palm.
riding gloves|They are close-fitting gloves with reinforced fingers for holding reins.
cycling gloves|They are padded, half-finger gloves with a ventilated back.
fingerless gloves|They leave the fingertips bare.
convertible mitten gloves|They have a flip-over mitten cap that folds back from the fingers.
gauntlets|They have a long flared cuff that covers the wrist and part of the forearm.
falconry gauntlets|They are thick, long-cuffed leather gloves for the forearm.
welding gloves|They are heavy, heat-resistant gloves with a long split-leather cuff.
work gloves|They are tough canvas or leather gloves with reinforced palms.
gardening gloves|They are flexible, dirt-resistant gloves with a grippy palm.
waterproof rubber gloves|They are long rubber gloves for wet work.
winter mittens|They are thick mittens with a single cover for the four fingers.
lobster mittens|They are mittens with a split between two fingers and the other two.
trigger-finger mittens|They have a separate index finger for tasks needing a pointing finger.
ski gloves|They are insulated, waterproof gloves with a long cuff.
touchscreen gloves|They have conductive fingertips that work on a phone screen.
lace gloves|They are fine open-work gloves with a scalloped edge.
mesh gloves|They are stretchy open-weave gloves, snug on the hand.
latex gloves|They are glossy, skin-tight gloves.
leather biker gloves|They are tough gloves with armoured knuckles and a wrist strap.
batting gloves|They are snug sports gloves with a grippy palm.
goalkeeper gloves|They are thick-palmed sports gloves with a padded back.
fishing gloves|They are quick-dry gloves with open fingertips.
heated gloves|They have thin heating elements running through the fingers.
arm warmers with thumbholes|They are long fingerless tubes that cover the hand and forearm.
Sami reindeer-hide mittens|They are warm mittens with embroidered cuffs in bright wool.
Nordic patterned mittens|They are hand-knit mittens in a repeating star and snowflake pattern.
Andean alpaca mitts|They are fingerless mitts knitted in bold stripes.
Kashmiri embroidered gloves|They are soft wool gloves covered with chain-stitch flowers.
Persian felted mittens|They are thick felted mittens with decorative cut-outs.
Tibetan wool-lined gloves|They are heavy gloves with a thick woolly lining and a decorated cuff.
Afghan sheepskin mitts|They are warm, wool-lined mitts with embroidered cuffs.
Chinese silk sun gloves|They are thin silk gloves with a long cuff for sun protection.
Indian embroidered gloves|They are gloves with zari embroidery across the back of the hand.
Japanese tekko hand covers|They are cloth hand covers worn over the back of the hand, tied at the wrist.
chainmail gloves|They are made of tiny interlocking metal rings.
butcher's gloves|They are tough cut-resistant gloves in woven steel mesh.
historical gauntlets|They are articulated plates for reenactment, with leather backing.
steampunk gauntlets|They are brass and leather gauntlets with decorative gears.
glovelettes|They are very short gloves that cover only the palm and half the fingers.
bridal gloves|They are soft gloves in lace or satin with a pearl button.
spooky costume gloves|They are long gloves with claws or stitched seams for costumes.
fur-trimmed gloves|They are leather gloves with a soft fur rim.
shearling mittens|They are warm mittens lined with thick wool.
knitted wrist warmers|They are short knitted tubes covering the wrist and the back of the hand.
puppet gloves|They are gloves with a sewn-on animal face on the back.
embroidered garden gloves|They are light gloves with a painted flower on the back."""),
 'scarf': P("""infinity scarf|It is a long looped scarf that wraps twice around the neck.
long rectangular scarf|It is a plain long scarf with two open ends.
square silk scarf|It is a square of silk that can be folded and knotted in many ways.
pashmina wrap|It is a large soft rectangular wrap that can be worn as a scarf or shawl.
stole|It is a broad, long wrap that drapes over the shoulders.
bandana neckerchief|It is a square of cotton tied loosely around the neck.
checked keffiyeh|It is a large square of cotton in a woven check, folded and wrapped around the neck or head.
shemagh|It is a large cotton square in a woven check, wrapped for sun and dust.
dupatta|It is a long, light scarf worn draped over the shoulders or head.
kente stole|It is a stole woven in narrow bright strips of cloth.
mud-cloth scarf|It is a scarf of hand-woven cotton painted in earth-toned geometric symbols.
kanga wrap|It is a printed cotton cloth with a bold border and a saying along one side.
Tuareg indigo cheche|It is a long indigo-dyed cotton cloth, wrapped around the head and neck.
Sami shawl|It is a square shawl with a wide bright fringe.
tartan scarf|It is a woolen scarf in a woven plaid.
Fair Isle scarf|It is a knitted scarf in bands of small repeating patterns.
rib-knit scarf|It is a stretchy knitted scarf with vertical ribs.
chunky cable-knit scarf|It is a thick scarf with raised twisted cables.
blanket scarf|It is a very large, soft scarf that doubles as a wrap.
neck gaiter|It is a seamless tube worn around the neck.
snood|It is a thick looped scarf that sits close to the neck.
hooded scarf|It has an attached hood and a long end that wraps around the neck.
ascot|It is a wide silk tie that tucks into an open collar.
cravat|It is a folded silk cloth tied loosely at the neck.
twilly|It is a narrow silk scarf, tied on a bag handle or the neck.
head scarf|It is a square of cloth tied over the hair.
turban wrap|It is a long cloth wound around the head.
furoshiki wrap|It is a square cloth in the Japanese tradition, worn knotted at the neck.
obi-style sash scarf|It is a broad, stiff sash that wraps around the neck or waist.
feather boa|It is a long fluffy tube of feathers.
fur stole|It is a soft wrap of fur that drapes over the shoulders.
mohair scarf|It is a fluffy, brushed scarf with a soft halo.
linen summer scarf|It is a light, airy scarf in loosely woven linen.
gauze summer scarf|It is a very light, crinkled scarf in fine cotton.
lace mantilla|It is a fine lace scarf draped over the head and shoulders.
sheer organza scarf|It is a light see-through scarf with a crisp drape.
beaded scarf|It is a scarf covered with rows of tiny beads.
chain scarf|It is a long scarf made of metal chain links.
reflective running scarf|It is a light scarf with reflective thread, worn for night runs.
heated scarf|It is a thick scarf with a thin heating layer.
pocket scarf|It is a long scarf with a hidden pocket at each end.
tassel scarf|It is a scarf with large tassels at each end.
poncho scarf|It is a large wrap with openings for the arms.
map-print silk scarf|It is a silk square printed with a detailed map.
printed floral scarf|It is a light scarf with a bold flower pattern.
patchwork scarf|It is a scarf pieced together from many fabrics.
tie-dye scarf|It is a scarf in swirling dyed colours.
batik scarf|It is a scarf painted with wax-resist designs.
ikat scarf|It is a scarf woven from yarn dyed before weaving, with soft blurred edges.
shibori scarf|It is a scarf folded and dyed to make crisp patterns.
sequined scarf|It is a scarf covered in tiny sequins.
braided scarf|It is a long scarf made of braided strands."""),
 'tights': P("""sheer tights|They are fine, nearly transparent tights.
opaque tights|They are solid, thick tights that fully cover the skin.
fleece-lined tights|They have a warm brushed lining and a sheer-looking outer.
fishnet tights|They are open-net tights with diamond holes.
patterned tights|They are tights in a repeating pattern.
footless tights|They end at the ankle with no foot.
stirrup tights|They have a loop that passes under the arch and leave the heel and toe bare.
convertible tights|They have a foot that can be rolled up out of the way.
seamed tights|They have a dark line running up the back of each leg.
compression tights|They are firm tights with graduated pressure up the leg.
ribbed tights|They are tights with fine vertical ribs.
cable-knit tights|They are chunky tights with raised twisted cables.
lace tights|They are tights in a delicate flower lace.
glitter tights|They are tights with a shimmer of glitter.
metallic tights|They are tights with a shiny metallic finish.
striped tights|They are tights in bold horizontal stripes.
argyle tights|They are tights in a diamond argyle pattern.
polka-dot tights|They are tights in a field of dots.
colour-block tights|They are tights in two or three solid colour blocks.
leg-print tights|They are printed with a design that wraps up the leg.
mesh tights|They are tights in a soft, stretchy mesh.
high-waist control tights|They have a wide high waistband that smooths the body.
thermal tights|They are heavy insulating tights for cold weather.
wool tights|They are thick tights knit from wool.
silk tights|They are fine, light tights in silk.
cotton tights|They are soft, breathable tights in cotton.
pantyhose|They are sheer stockings joined to a panty.
dancer's tights|They are smooth tights with a convertible foot for dance.
rainbow-gradient tights|They shade from one colour to another up the leg.
lace-up tights|They have a row of ribbon lacing up the back.
cut-out tights|They are tights with shaped holes at the knee or the thigh.
diamond-net tights|They are wide-net tights with large diamond holes.
velvet tights|They are tights with a velvety surface.
faux-leather tights|They are glossy leather-look tights.
latex tights|They are glossy, skin-tight rubber tights.
sock-footed knit tights|They are knitted tights with a thick cosy foot.
toeless tights|They have an open toe.
embroidered tights|They are tights with delicate embroidery at the ankle.
bow-back tights|They have a ribbon bow at the back of the ankle.
tattoo-print sheer tights|They are sheer tights printed with a flowing tattoo design.
star-print tights|They are tights scattered with small stars.
crystal-studded tights|They are sheer tights with hand-set crystals.
fluffy sherpa-lined tights|They have a thick sherpa lining."""),
}
# traditions (global) and motifs used by the *_design files
TRAD = S("Navajo silversmith, Yoruba aso-oke weaver, Ashanti kente weaver, Maasai beadworker, Fulani goldsmith, Berber silversmith, Ethiopian weaver, Tuareg leatherworker, Kashmiri shawl weaver, Rajasthani bandhani dyer, Banarasi silk weaver, Indian chikankari embroiderer, Persian enameller, Ottoman court embroiderer, Uzbek suzani embroiderer, Tibetan jeweller, Japanese shibori dyer, Japanese kimono weaver, Korean hanbok seamstress, Chinese Suzhou embroiderer, Thai silk weaver, Balinese silver granulator, Filipino piña weaver, Javanese batik artist, Maori weaver, Polynesian tapa maker, Andean alpaca weaver, Quechua backstrap weaver, Mexican Oaxacan embroiderer, Guatemalan Maya weaver, Haida carver, Sami duodji craftsperson, Scottish tartan weaver, Irish lace maker, Italian Venetian glassmaker, French Parisian couturier, Dutch Delft painter, Baroque court goldsmith, Art Nouveau jeweller, Art Deco designer, 1960s mod designer, Victorian mourning jeweller, Georgian court tailor, Edwardian milliner, Georgian paste jeweller, Scandinavian silver smith, Celtic knotwork artisan, Russian enamel artist")
MOTIF = S("woven chevrons, a border of small triangles, a running band of waves, a field of tiny stars, a repeat of paisley teardrops, a pattern of interlocking diamonds, a border of leaves and vines, a sunburst, a row of small birds, a field of flowers, a lattice of diamonds, dotted rows, a stepped fret, a spiral border, stripes in graduated colours, a checkerboard, a medallion at the centre, crescent moons and stars, interlaced knots, a scatter of tiny shells, a pattern of feathers, concentric circles, an all-over scale pattern, a repeat of tiny mirrors, a block of colour bands, a meander border, a pattern of lotus flowers, a pattern of tiny geometric animals, a pattern of cloud scrolls")
TECHPOS = {'earring': S("on the front, on the lobe, at the drop, on the back, on the face of each piece"), 'glove': S("across the back of the hand, at the cuff, on the fingers, at the wrist, along the side"), 'scarf': S("at both ends, along the borders, at the centre, in a repeat, on one side"), 'tights': S("up the leg, at the ankle, at the thigh, on the waistband, up the back")}
WEAR = {'earring': ['wearing {}', 'with {} on the ears', 'wearing {} that swing as the head turns', 'with {} catching the light', 'showing {} beneath tucked-back hair', 'wearing {} in both ears'],
        'glove': ['wearing {}', 'with hands in {}', 'pulling on {}', 'holding one hand up in {}', 'wearing {} with the cuffs turned back', 'with {} on both hands'],
        'scarf': ['wearing {} around the neck', 'with {} wrapped twice around the neck', 'wearing {} draped loosely over the shoulders', 'with {} knotted at the throat', 'wearing {} over the head', 'with {} trailing behind'],
        'tights': ['wearing {}', 'with legs in {}', 'wearing {} under a skirt', 'wearing {} with ankle boots', 'with {} showing at the ankle']}
