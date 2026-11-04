"""Shoe vocabulary part 2: materials, colours, patterns, toes, details, hardware, soles, linings, finishes, extras, designers, photo styles.  Merged with the sample vocab in shoe_build.py."""
from shoe_data import L
MATERIAL = {
 'T1': L("""printed canvas
recycled nylon
smooth rubber
plastic-coated fabric
foam-backed jersey
polyester satin
glossy vinyl
split leather with a plastic coating
cotton twill
terry cloth
polyurethane-coated fabric
bonded leather
burlap
felted acrylic
nylon ripstop
perforated synthetic leather
quilted polyester
flocked fabric
jelly PVC
woven plastic straw
thin corduroy
fleece
microfiber
rope-wrapped cotton
bamboo-fibre knit
paper-thin pleather
clear vinyl
knitted acrylic
mesh and synthetic overlays
neoprene"""),
 'T2': L("""cotton drill
split suede
coated canvas
grained leather
vegan leather
recycled-polyester canvas
brushed cotton twill
natural rubber
nubuck-look microfiber
jute weave
hemp canvas
cork leather
ballistic nylon
leather-look polyurethane
softshell fabric
thick felt
raw denim
rubberized cotton
cotton corduroy
suede-look microfiber
pigskin split
tumbled leather
coated split leather
heavy duck canvas
woven raffia blend
quilted nylon
washed linen blend
sheepskin-look fleece"""),
 'T3': L("""full-grain oil-tanned leather
calf suede
reverse calf
waxed suede
grained calfskin
heavy tweed
herringbone wool
buffalo leather
horsehide
kangaroo leather
washed linen
hand-woven straw
braided leather
elk hide
pigskin
Tyrolean loden
shearling-lined suede
saddle leather
chrome-tanned kip
Italian pebble-grain leather
canvas with a leather toe cap
waxed twill
smooth veg-tan calf
brushed suede
oil-pull-up leather
glazed kid
deerskin
water-buffalo hide
oiled bridle leather
rustic split-grain leather"""),
 'T4': L("""Italian calf burnished by hand
box calf
patent calf
nubuck calf
deerskin
peccary leather
washed silk twill
silk jacquard
mohair
cashmere
kid leather
crocodile-embossed calf
bison leather
Venetian leather
hand-woven raffia
brushed alpaca felt
crushed velvet
brocade
satin-faced duchess silk
lizard-embossed leather
carbon-tanned leather
hand-antiqued calf
hand-dyed suede
mirror-polished leather
two-tone burnished calf
silk grosgrain
Harris-style tweed
stitched Chinese silk
Florentine leather
vintage-finish horsehide"""),
 'T5': L("""python skin
eel skin
crocodile leather
lizard skin
karung snake
hand-painted silk
cut velvet
embroidered tulle
beaded silk
gold-leaf calf
enamelled leather
feathered silk
mother-of-pearl-flecked lambskin
Venetian silk lampas
lace over silk
cashmere velvet
a mosaic of exotic leathers
sharkskin
hand-carved leather
silk faille embroidered with metallic thread
bespoke satin
marquetry of coloured leathers
fur-free faux shearling woven by hand
hand-pleated organza
hand-loomed silk damask
silk embroidered with pearls
anaconda leather
fine kid dyed in a custom colour
pearlized stingray
suede dyed in nine layers"""),
 'T6': L("""woven platinum wire
hammered gold sheet
solid silver filigree
carved jade plaques
rock-crystal panels
gem-set gold mesh
lapis lazuli mosaic
malachite inlay
enamelled gold plates
cloth of gold
an iridescent feather mosaic
gold-embroidered brocade
velvet embroidered with gold and seed pearls
pearl-encrusted satin
silk woven with spun silver
opal-inlaid kid leather
carved amber panels
hand-painted porcelain plaques
diamond-dusted silk
rose-gold chain mail
sapphire-studded velvet
cloisonné enamel on silver
a patchwork of gold-leafed lizard
Damascus-style layered steel
a lattice of gold wire and pearls
mosaic of tiny polished garnets
ruby-red lacquered snakeskin
carved ivory-coloured coral resin
spun glass thread
platinum-threaded Venetian lace"""),
}
COLOUR_SINGLE = L("""black
white
off-white
cream
ivory
bone
beige
sand
tan
camel
caramel
chestnut
cognac
saddle brown
dark brown
chocolate
mahogany
oxblood
burgundy
wine
crimson
scarlet
cherry red
brick red
terracotta
rust
burnt orange
tangerine
amber
mustard
marigold
sunflower yellow
lemon yellow
butter yellow
lime green
olive green
moss green
forest green
emerald
jade
sage
mint
teal
turquoise
aqua
sky blue
powder blue
cornflower blue
cobalt
royal blue
navy
midnight blue
indigo
denim blue
periwinkle
lavender
lilac
violet
plum
aubergine
magenta
fuchsia
hot pink
blush pink
dusty rose
salmon
coral
peach
nude
taupe
stone
slate
charcoal
gunmetal
silver
pewter
steel grey
pearl grey
gold
antique gold
bronze
copper
rose gold
champagne
platinum
iridescent green
holographic silver
glow-in-the-dark green
neon pink
neon yellow
neon orange
matte black
patent black
tortoiseshell pattern
oyster
ecru
khaki
army green
dusty blue
dove grey
raspberry
pistachio
apricot
burnt sienna
ochre
smoke
ink blue
petrol blue""")
COLOUR_SPECIAL = {
 'T1': L("""neon green and black
two-tone red and white
primary blue with yellow soles
pastel pink and mint
black with white racing stripes
camouflage green
tie-dye in purple and blue
bright orange with grey"""),
 'T2': L("""khaki with brown trim
navy with white piping
grey marl with orange accents
black with a red heel tab
olive drab with tan overlays
brick red with cream laces"""),
 'T3': L("""walnut brown with cream stitching
burgundy with a tan welt
bottle green with brass hardware
two-tone navy and tan
dark chocolate with a rust-coloured edge
cognac with contrast black laces"""),
 'T4': L("""hand-painted burgundy fading to black
patina in layers of cognac and espresso
ink blue with silver burnishing
two-tone grey and cream, hand-antiqued
oxblood fading to near-black at the toe
deep green with gold edge paint"""),
 'T5': L("""peacock blue shot with gold
hand-dyed ombré from blush to crimson
midnight silk with silver star embroidery
champagne with pearl-white overlays
emerald and gold
sapphire fading to turquoise"""),
 'T6': L("""solid gold with ruby accents
platinum white with diamond-white inlays
imperial purple and gold
lapis blue veined with gold
jade green carved with gold leaf
pearl, silver and moonstone white
lacquer red and gold maki-e
black onyx with gold filigree"""),
}
PATTERN = L("""houndstooth check
tartan plaid
gingham check
herringbone weave
argyle diamonds
pinstripes
chevron stripes
polka dots in several sizes
tiny scattered stars
paisley
damask scrolls
ikat zigzags
batik waves
block-printed leaves
Fair Isle bands
Nordic snowflakes
Navajo-inspired stepped diamonds
kilim-style geometric bands
greek-key border
Moroccan zellige tiles
arabesques
trellis lattice
fish-scale scallops
leopard spots
zebra stripes
snakeskin scales
giraffe patches
tiger stripes
peacock feathers
camouflage patches
marbled swirls
tie-dye spirals
watercolour washes
ombre gradient
colour-blocked triangles
checkerboard squares
harlequin diamonds
op-art concentric circles
rainbow stripes
scattered cherry blossoms
sunflower print
rose garland embroidery
tropical palm leaves
koi and waves
dragon scales
seigaiha waves
asanoha hemp-leaf pattern
sashiko stitching in white
Celtic knotwork
Viking interlace
Art Deco sunbursts
Art Nouveau whiplash curves
Memphis squiggles and confetti
pixelated hearts
tiny skulls
playing-card suits
musical notes
constellation map
topographic contour lines
map of an old city
newspaper print
handwritten script
Morse-code dashes
barcode stripes
circuit-board traces
mosaic of broken tiles
brickwork bonds
woven basketry
cable-knit ribs
quilted diamonds
basketweave
crocodile-scale emboss
lizard-skin emboss
perforated medallions
broguing in floral rosettes
stamped dots and dashes
embroidered mandalas
beaded fringe rows
tassel clusters
patchwork of leathers
sailor stripes
nautical rope knots
anchor motifs
seashell motifs
feather plumes
butterfly wings
dragonfly wings
moth wings
ladybird spots
bee and honeycomb hexagons
mushroom clusters
fern fronds
wheat sheaves
oak leaves and acorns
holly and berries
pumpkins and bats
snowmen and pines
fruit-salad prints
strawberries
lemons and leaves
avocado halves
pizza slices
sushi motifs
coffee cups
rubber ducks
cats and paws
dogs and bones
tiny elephants in a parade
folk-art birds
Dutch tulips
Delft-blue windmills
Provençal sprigs
toile de Jouy scenes
Persian garden medallions
Chinese cloud scrolls
Japanese crane motifs
Indian paisley boteh
block-printed elephants
Ethiopian cross patterns
kente stripes
mudcloth symbols
Adinkra symbols
Andean woven bands
Oaxacan folk flowers
Ottoman tulip motifs
Byzantine mosaic medallions
Venetian carnival masks
Gothic tracery
Baroque cartouches
Rococo shell scrolls
Egyptian lotus friezes
Mayan glyph bands
Aboriginal-inspired dot painting
pointillist dots
Cubist fragments
Bauhaus primary shapes
Mondrian-style colour grid
Pop-art comic dots
graffiti tags
bold abstract brush strokes
splatter paint
tiger-lily watercolours
crackle glaze
rust patina
oil-slick iridescence
metallic foil flecks
holographic scales
glitter speckles
terrazzo flecks
granite speckles
wood-grain lines
bark texture
snow-leopard rosettes
hand-drawn doodles
plain, with no pattern at all
quiet tone-on-tone stitching
subtle self-colour embossing""")
TOE = L("""a pointed toe
a rounded toe
a square toe
an almond toe
a chiseled toe
a peep toe
a domed toe
a capped round toe
a broad round toe
a gently pointed toe
a sleek tapered toe
a sleek elongated toe
a squared-off toe
a soft rounded toe
a low, rounded toe
a slim almond toe
a rounded open toe
a squared open toe
an upturned toe
a curled toe
a split toe
an apron toe
a wingtip toe cap
a plain toe
a medallion toe cap
a bulbous toe
a wide anatomic toe box
a spatulate toe
a bullet-nosed toe
a hooded toe
a duckbill toe
a bulbous platform toe
an open round toe
a closed pointed toe
a pointy toe with a long tapered end
a gently curled-up toe
a rubber-capped toe
a reinforced steel toe
a beak-like pointed toe
a squarish oval toe
an elongated chisel toe
a stubby round toe
a moc toe with a visible seam
a cap toe stitched in a straight line
a rolled-edge toe
a cut-out toe
a toe loop
a flat-fronted toe
a high-rise toe box
a tapered squared toe""")
AESTHETIC = L("""a sculpted futuristic sole
tessellated panels
a sculptural silhouette
honest construction
unembellished panels
unpolished patina
outlined color blocks
squares and triangles set flush into the upper
exposed construction seams
an upturned toe
a curled toe
even saddle stitching
a monolithic block silhouette
a pared-back minimal profile
softly collapsing folds
a razor-sharp geometric profile
layered translucent panels
a playful exaggerated proportion
an armoured segmented build
a dramatic asymmetrical cut
a vintage silhouette with modern proportions
a rounded, pillowy volume
a low-slung racing profile
a sleek continuous line from heel to toe
chunky stacked layers
a lace-trimmed romantic profile
a raw, deconstructed finish
a hand-made, slightly irregular charm""")
TECHNIQUE_EXTRA = {
 'T1': L("""stamped on by machine
sprayed on through a stencil
glued on as a flat decal
printed in a single colour
sewn on with a few quick stitches
sublimation-printed
bonded on with heat
extruded in one piece with the sole"""),
 'T2': L("""stitched on in two colours
embossed in the leather
sewn in with decorative top-stitching
woven in on a power loom
machine-quilted
punched out by a die
heat-welded in place
riveted on by machine"""),
 'T3': L("""hand-stitched with waxed thread
hand-burnished at the edges
tooled in shallow relief
hand-painted with a brush
laser-etched then hand-finished
hand-braided
hand-punched
stained and hand-rubbed"""),
 'T4': L("""hand-stitched in contrasting silk thread
burnished by hand to a patina
hand-painted in layers
hand-tooled in deep relief
inlaid in contrasting leather
applied by hand in tiny pieces
braided by hand from narrow strips
embroidered with fine silk thread"""),
 'T5': L("""embroidered by hand in gold thread
inlaid by hand with exotic leather
hand-painted with a single-hair brush
hand-carved in low relief
enamelled by hand
set by hand in tiny pieces
beaded by hand
gilded by hand with real leaf"""),
 'T6': L("""carved from a single block by a master
set with hundreds of hand-cut stones
cast in precious metal and chased by hand
engraved by a master engraver
enamelled in many fired layers
inlaid with mother-of-pearl and gems
woven from real gold wire
assembled by hand from gold and gem plaques"""),
}
DETAIL_EXTRA = L("""contrast top-stitching
decorative perforations
a quilted collar
a scalloped topline
a padded collar and tongue
an elasticated gusset
rows of rivets
a braided welt
a moulded heel counter
decorative eyelets in contrasting metal
a double row of piping
whipstitched edges
embossed initials on the quarters
a woven label stitched at the heel
cutwork along the quarters
a bound topline
a cross-stitch motif
cord piping along the seams
reflective tape trim
neon-coloured laces
mismatched left and right laces
grommets around the ankle
fold-over cuffs
a perforated toe cap
scalloped broguing
leather fringe
double buckles
stitched stars
heart-shaped cutouts
bold zigzag stitching
tiny bells on the ties
pointed collar flaps
inset gussets of contrast colour
contrasting heel stripes
a printed sole sock
a metal toe cap
decorative studs along the seams
a stitched tongue label
an embroidered crest
a single bold stripe
a stack of coloured heel layers
woven rope trim
hand-knotted fringe
a chunky heel tab
patchwork overlays
distressed edges
pinked seam allowances
pleated side panels
a ruched ankle
a draped overlay
asymmetrical lacing
cross-over straps
a ribbed knit cuff
a faux-fur collar
an exposed foam tongue
a translucent window in the heel
a glow strip along the sole
a floral appliqué
embossed crocodile scales on the toe
lace-up side panels
a keyhole cutout on the vamp
a fringe tongue
a lined tassel
horse-bit hardware
a hammered metal buckle
tiny mirrors set into the upper
a zipper-pull charm
studded straps
stacked leather rings on the heel
a contrasting piping around the sole
laser-cut lace-effect panels
engraved metal tips""")
CONSTRUCTION_EXTRA = {
 'T1': L("""pressed from a single sheet of material
fused at the seams with heat tape
glued and clamped in a single factory run
stapled and cemented to the sole
slip-lasted with a simple glued bottom
moulded around the foot shape in one shot
cut-and-sew with one row of machine stitching
bonded with hot-melt adhesive
glued together in one flat piece
cemented in a single machine pass
injection-molded in one piece
stuck to the sole with strong adhesive
cemented, with a few quick machine stitches
stamped from a single sheet and bonded"""),
 'T2': L("""strobel-stitched to the upper
sewn with double rows of machine stitching
cemented, then wrapped in a rubber foxing strip
stitched through the midsole for durability
reinforced with bar-tacks at every stress point
heat-sealed and taped at the seams
stitched with a bonded nylon thread
direct-attach moulded to the sole
cemented and double-stitched at the stress points
box-stitched at the heel
machine-stitched with reinforced seams
Littleway-stitched
vulcanized at high heat
sewn to a molded unit sole"""),
 'T3': L("""hand-finished with a sewn-in leather welt
built over a traditional last with a leather midsole
sewn with a double row of waxed thread
cork-filled and resoleable
Goodyear-welted with a leather storm welt
hand-trimmed and burnished at the sole edge
stitched by experienced operators on a Blake machine
fitted with hand-attached heel and toe stiffeners
Norwegian-welted for water resistance
stitched with a storm welt
Blake-stitched with a hand-finished edge
hand-lasted over a fitted last
stitched with a hand-finished edge and a leather midsole
Goodyear-welted with a cork filler"""),
 'T4': L("""hand-lasted and left to rest for several days before welting
finished with a hand-cut and hand-stitched welt
Blake-stitched with a hand-sewn heel seat
hand-turned and hand-sewn in the traditional manner
made with a hand-lasted bespoke-grade toe puff
completed with a hand-bevelled waist and a hand-burnished sole edge
assembled in a small workshop by a single team
double-stitched by hand with waxed linen thread
hand-welted with a chain-stitch
hand-lasted over a wooden last
finished in more than two hundred hand operations
Blake-rapid stitched with hand-painted edges
Norwegian-welted by hand
hand-sewn with a waxed linen thread and a hand-cut welt"""),
 'T5': L("""stitched entirely by hand over a period of weeks
built over a last shaped with the client's measurements and a plaster cast
hand-sewn, hand-welted and hand-polished
made by one master from the first cut to the final polish
hand-turned from supple leather and finished by candlelight
built with hand-forged tacks and hand-pegged heels
hand-shaped on the last over many days
fitted with hand-cut hidden support structures
made over a last carved to the client's own foot
hand-sewn from first stitch to last
bench-made in an atelier over many weeks
built over a custom last with a hand-sewn Goodyear welt
hand-lasted and hand-welted in a master's atelier
made in a single piece by one artisan using traditional tools"""),
 'T6': L("""built over a last carved from a single piece of rare wood
shaped by hand through hundreds of fittings
assembled by a team of cobblers, goldsmiths and lapidaries
hand-sewn at fifty stitches per inch with a thread spun from real silver
built so that every part is a hand-made miniature sculpture
made over a full year and signed on the sole by every artisan
constructed like a reliquary around the foot
hammered, chased and stitched into a single heirloom object
carved from a single piece of precious material
hand-built over many months by a team of master jewelers and cobblers
assembled in a private workshop over a year
sewn with gold thread on a last carved from a single piece of rare wood
fitted with a gold-wire welt hammered into place
built as a work of art rather than a pair of shoes"""),
}
HW = {  # tier hardware
 'buckle': {'T1': L("plastic buckle\ncheap metal-look buckle\nnickel-plated buckle"), 'T2': L("nickel roller buckle\nbrushed metal buckle\nenamelled metal buckle"), 'T3': L("brass buckle\nantique-brass buckle\nstainless buckle"),
            'T4': L("hand-polished brass buckle\nsolid brass buckle with a matte finish\npalladium-plated buckle"), 'T5': L("hand-engraved silver buckle\nhand-chased silver buckle\nrhodium-plated buckle set with crystals"),
            'T6': L("white-gold buckle set with sapphires\nsolid gold buckle set with diamonds\nplatinum buckle set with rubies")},
 'button': {'T1': L("plastic buttons\nmetal-look snap buttons"), 'T2': L("domed metal buttons\nplain resin buttons"), 'T3': L("leather-covered buttons\nbrass buttons"), 'T4': L("horn buttons\ncovered silk buttons"),
            'T5': L("mother-of-pearl buttons\ncarved bone-coloured buttons"), 'T6': L("diamond-set gold buttons\nbuttons carved from jade")},
 'lace': {'T1': L("flat polyester laces\nthin cotton laces"), 'T2': L("round cotton laces\nflat cotton laces"), 'T3': L("waxed cotton laces\nleather laces"), 'T4': L("waxed linen laces\nhand-rolled leather laces"),
          'T5': L("hand-rolled silk laces\nhand-braided silk cords"), 'T6': L("braided gold-thread laces\nsilk laces tipped in gold")},
 'zip': {'T1': L("nylon coil zipper"), 'T2': L("metal zipper"), 'T3': L("brass zipper"), 'T4': L("antique-brass zipper with a leather pull"), 'T5': L("gunmetal zipper with a leather pull"), 'T6': L("18-karat gold zipper with a diamond-set pull")},
 'ribbon': {'T1': L("polyester ribbons\nsatin ribbons"), 'T2': L("grosgrain ribbons\ncotton ribbons"), 'T3': L("silk-blend ribbons\nsatin ribbons"), 'T4': L("silk ribbons\nvelvet ribbons"),
            'T5': L("hand-dyed silk ribbons\nribbons of silk embroidered with metallic thread"), 'T6': L("gold-thread ribbons\nribbons of silk woven with pearls")},
 'strap': {'T1': L("synthetic strap"), 'T2': L("cotton webbing strap\nstitched synthetic strap"), 'T3': L("leather strap"), 'T4': L("hand-stitched leather strap\nsuede strap"), 'T5': L("hand-dyed kid strap\nexotic leather strap"), 'T6': L("gold-chain strap\nstrap of woven gold thread")},
 'eyelet': {'T1': L("punched metal eyelets"), 'T2': L("riveted metal eyelets"), 'T3': L("brass eyelets"), 'T4': L("hand-finished eyelets\nblind eyelets"), 'T5': L("hand-set silver eyelets"), 'T6': L("gold-rimmed eyelets set with tiny gems")},
}
LININGS = {
 'T1': L("""Inside is a thin foam insole covered in terry cloth
The interior is unlined, with a printed fabric-covered foam insole
A simple mesh lining and removable foam insole complete it
The lining is thin polyester with a plain foam footbed
Inside it is bare synthetic with a glued-in insole
A cheap fabric lining sits above a flat molded insole
The inside is lined in printed jersey"""),
 'T2': L("""A padded synthetic lining and contoured insole keep it comfortable
It is lined in breathable textile over a cushioned insole
A brushed cotton lining wraps a molded insole
Inside is a moisture-wicking mesh lining with an antibacterial insole
The interior is lined in soft fleece with a foam footbed
A smooth textile lining sits over a removable insole
It is lined in cotton drill with a shock-absorbing footbed"""),
 'T3': L("""A full calfskin lining and memory-foam footbed complete it
It is lined in glove leather with a cushioned leather footbed
A cork-filled footbed sits under a soft pigskin lining
Inside, a breathable leather lining and a removable cork insole
The lining is soft pigskin and the footbed is stamped with a maker's mark
It is lined in unbleached cotton with a leather-covered insole
The interior is lined in sheepskin with a padded insole"""),
 'T4': L("""It is fully lined in supple calfskin with a hand-stamped insole
A kidskin lining and leather-wrapped cork footbed sit inside
The interior is lined in natural vegetable-tanned leather
Inside, a lining of fine calf leather and a hand-stamped gold-foil insole
The lining is buttery kid with a padded insole
It is lined in silk-soft goatskin over a cushioned insole
The interior is lined in hand-dyed leather with a padded heel"""),
 'T5': L("""It is lined in suede-soft kidskin with a padded silk insole
Inside, a silk-lined footbed is embossed with a gilded maker's mark
The lining is butter-soft lambskin, and the insole is hand-painted
The interior is lined in hand-quilted silk with a leather footbed
Inside, a lining of silk charmeuse and an insole stamped in gold leaf
It is lined in finest kid leather with the client's initials stamped in the insole
The interior is lined in silk velvet with a monogrammed insole"""),
 'T6': L("""The interior is lined in hand-painted silk with an insole inlaid in mother-of-pearl
Inside, the lining is silk velvet and the insole is embroidered in gold thread
The footbed is lined in ermine-soft shearling with a gilt-stamped signature
The interior is lined in gold-leafed kidskin with a jewelled insole
Inside, the lining is cloth of gold with an insole inlaid with tiny gems
The footbed is hand-engraved with the client's name in gold
The interior is lined in silk woven with real silver and a rose-gold insole plate"""),
}
FOOTBED = {  # open shoes: no lining
 'T1': L("""A thin foam footbed with a printed top sheet sits underneath
The footbed is a flat molded EVA pad
The footbed is a simple synthetic insole glued in place"""),
 'T2': L("""A contoured footbed with a textured top sheet gives mild arch support
The footbed is cushioned foam with a nonslip top
The footbed is a molded cork-and-latex pad"""),
 'T3': L("""A moulded cork footbed topped in soft suede cradles the foot
The footbed is leather-covered and shaped to the arch
The footbed is stamped with a maker's mark"""),
 'T4': L("""A hand-shaped footbed of cork and latex is wrapped in kidskin
The footbed is contoured to the foot and covered in hand-stamped calf
The footbed is wrapped in soft nappa leather"""),
 'T5': L("""The footbed is hand-shaped and covered in silk-soft kid with a gilded maker's mark
The footbed is lined in embroidered silk over cork
The footbed is padded in lambskin and signed by the maker"""),
 'T6': L("""The footbed is inlaid with mother-of-pearl and lined with silk velvet
The footbed is covered in cloth of gold with an engraved gold plate
The footbed is hand-painted with the client's emblem and lined in ermine-soft shearling"""),
}
FINISH = {
 'T3': L("""a hand-stamped maker's mark on the heel
a burnished edge in a darker shade
a band of hand-painted edge paint
a discreet brass tag on the tongue"""),
 'T4': L("""hand-applied edge paint in a contrasting colour
a subtly embossed monogram on the instep
a hand-burnished patina at the toe
a tiny engraved metal plaque on the heel"""),
 'T5': L("""a hand-embroidered silk monogram cartouche
hand-applied gold-leaf edging
silver filigree caps on the heel
hand-set crystal trimming the topline
fine enamel plaques at the throat
hand-set rose-cut diamonds along the welt
hand-carved mother-of-pearl buttons
a gilt-embossed maker's seal on the instep
hand-painted miniatures on the heel
hand-applied platinum leaf on the toe
a trim of hand-braided silk cord
a fringe of tiny hand-strung pearls
a border of hand-cut cabochon moonstones
silver-gilt toe tips engraved by hand"""),
 'T6': L("""cabochon rubies set into each fastening
dense rows of hand-sewn natural pearls
brilliant-cut diamonds pavé-set along the heel
a single emerald set into each toe tip
a band of hand-enameled gold plaques around the collar
a scattering of sapphires across the vamp
a cluster of Burmese rubies on each tongue
a ring of brilliant diamonds round each ankle
a carved jade tassel at the heel
a heel set with a single enormous pearl
a vamp paved with tiny yellow diamonds
a scattering of black opals along the topline
a pair of carved sapphire flowers at the toe
heel plates of engraved gold set with garnets
a border of emeralds and diamonds around the topline
emerald-cut aquamarines set in each buckle"""),
}
PRACTICAL_EXTRA = L("""a padded tongue that relieves lace pressure
a hidden steel shank for midfoot support
a rubber toe bumper
a slip-resistant siped tread
a waterproof membrane sealed into the seams
a gusseted tongue that keeps out debris
a removable cushioned arch-support footbed
a moisture-wicking lining
breathable perforations along the quarters
a contoured heel cup that locks the foot in place
retroreflective details for visibility
an antimicrobial insole
heel pull loops for easy entry
a roomy toe box that lets the toes spread naturally
a flexible forefoot groove for a natural stride
a shock-absorbing heel cushion
a reinforced toe cap for durability
a padded heel collar for comfort
a nonslip heel grip
a replaceable heel tip
an easy-clean wipe-down surface
a wide fitting for swollen feet
a hook-and-loop extension panel for adjustable width
a removable insole that makes room for custom orthotics
a hidden zipper pocket in the tongue for a key
a built-in toe spring that rocks the foot forward
a stain-resistant treatment
a rolled collar that does not rub the ankle
a soft padded ankle cuff
stretchy gores that flex with the foot
a rocker sole to ease the stride
quick-drying fabric
vents that drain water
a seamless interior to prevent blisters
a cushioned insole with a metatarsal pad
heel counters stiffened for stability
a split-sole design for flexibility
laces that stay tied
a salt-resistant leather finish
oil-resistant outsole compounds
metatarsal guards for protection
a breathable cork-latex footbed
gel pads under the ball of the foot
a tough kick guard along the toe
a flexible shank for walking comfort
a low-profile sole for pedal feel
a Velcro-secured tongue keeper
a pull tab at the heel
an elastic gore at the instep""")
WHIMSY_EXTRA = L("""a tiny hidden pocket in the heel
laces that glow in the dark
mismatched colours on the left and right shoes
a heel shaped like a tiny teapot
embroidered ladybirds crawling up the vamp
a small bell hidden inside each shoe
secret messages stitched inside the tongue
miniature clock faces on the sides
tassels shaped like pine cones
a trail of embroidered stars across the toe
real dried flower petals sealed in a transparent heel
a set of tiny working zippers used purely as decoration
pom-poms in rainbow colours
a mushroom-shaped heel tab
cat-ear shaped heel counters
a rooster feather tucked into the ankle strap
a little compass set into the instep
a tiny keyhole opening on the toe
a sole that stamps a four-leaf clover in wet sand
a heel that looks like a stack of books
tiny frogs embroidered on the instep
a ribbon of stitched musical notes
buttons shaped like tiny moons
a dragonfly clip on each strap
clusters of sequins shaped like fish scales
ruffles like a ballerina's tutu at the ankle
a stitched map of a made-up island
eyelets arranged to look like a constellation
a hidden polka-dot lining
a curl of lace at the collar
a miniature weathervane on the heel
an embroidered fox peeking from the tongue
a heel that tapers into a little fish tail
bobbles that look like berries
tiny charms of acorns and keys
a painted rainbow along the welt
a flip-up toe cap with a tiny doll's mirror
a spiral heel shaped like a corkscrew
a puff of faux fur at the heel
laces made of ribbon in a different colour for each eyelet
a stitched border of tiny flames
a hand-painted moth on each tongue
dangling beads that click when walking""")
DESIGNER_EXTRA = L("""Art Deco jeweller
Bauhaus weaver
Brutalist architect-turned-cobbler
Byzantine icon painter
Danish furniture designer
De Stijl purist
Dutch Golden Age painter-cobbler
Egyptian Revival goldsmith
Fauvist colourist
Florentine leatherworker
Futurist sculptor
Georgian-era shoemaker
Glasgow School designer
Gothic cathedral stonemason turned shoemaker
Ming dynasty lacquer artisan
Italian master of the last
Edwardian dandy tailor
English country bespoke bootmaker
Hungarian folk embroiderer
Inuit sealskin sewer
Japanese geta carver
Kyoto kimono weaver
Lisbon azulejo tile painter
Mughal miniature painter
Navajo silversmith
Neoclassical sculptor
Nigerian adire dyer
Parisian haute-couture atelier
Pop-art maximalist
Portuguese cork craftsman
Prague puppet-maker
Renaissance goldsmith
Roman-sandal historian
Scottish tweed mill designer
Seattle skate-shop designer
Shanghai Art Deco tailor
Sicilian puppet painter
Swiss watchmaker
Tibetan boot-maker
Tokyo street-fashion designer
Turkish carpet weaver
Tuscan saddler
Venetian glass artist
Viennese Secession designer
Viking-age leatherworker
Welsh clog carver
West African beadwork master
Zen minimalist
Appalachian folk maker
Basque espadrille weaver
Cajun swamp-boot maker
Sardinian shepherd-shoe maker
cowboy-boot maker from Texas
vegan sustainable-materials engineer
orthopaedic shoe technician
military boot specialist
rocket-scientist turned sneaker engineer
retro-futurist industrial designer
children's-book illustrator
medieval cordwainer
Tudor court shoemaker
Elizabethan costume maker
flamenco shoemaker from Seville
Parisian Belle Époque bootmaker
Hollywood costume shoemaker
jazz-age tap-shoe maker
New England boat-shoe maker
Peruvian highlands weaver
Hungarian bootmaker
Saharan sandal maker
Siberian felt-boot maker
Mongolian felt-boot craftsman
Indonesian batik artist
Moroccan slipper embroiderer
hand-loom weaver from Oaxaca""")
PHOTO = L("""Studio product photograph on a seamless white background, soft diffused light, three-quarter view.
Studio product photograph on a pale grey sweep, crisp even lighting, side profile view.
Overhead flat-lay product photograph on a neutral linen backdrop, soft window light.
Catalogue shot on a seamless white background, both shoes shown, one slightly angled.
Glossy e-commerce photograph with a subtle reflection beneath the shoes, bright even light.
Editorial still life on a plinth, a single spotlight, deep shadows, shallow depth of field.
Macro close-up of the toe and vamp, razor-sharp detail, softly blurred background.
Moody product shot on dark slate, dramatic side light, fine surface detail.
Heel-and-sole detail shot, the pair shown side by side, soft studio light.
Hero shot at a low angle, the shoes tilted slightly toward the camera, clean background.
Museum display photograph, the shoes on a glass pedestal with a soft museum spotlight.
Pair shown on a mannequin foot form, plain pastel backdrop, soft shadows.
Lifestyle flat-lay with a few props beside the shoes: a folded scarf, a key, a cup of coffee.
Boutique window display, the shoes on a mirrored shelf, warm lighting.
Auction-house catalogue photograph on a velvet cloth, with a ruler for scale.""")
