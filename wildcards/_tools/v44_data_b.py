"""v44 data B: wearable tech, lapel pins, patches, merit badges, balls, sport gear, range-audit lists."""
from v40_data_a import E
TECH = {
'retro': E("""
portable cassette player with foam headphones|a palm-sized box with clear window on the lid, buttons on top, and a belt clip, attached by a thin cord to a headband with two orange foam ear pads|plastic and foam
portable CD player|a flat round box slightly wider than a disc, with a small display and buttons on the lid, worn on a belt clip|plastic
early digital music player|a slim rectangular player with a small screen and a round control dial, on a neck lanyard|plastic and metal
pager on a belt clip|a small black rectangle with a narrow screen and two buttons, clipped to a belt|plastic
calculator watch|a wristwatch with a rubber band and a face made of tiny number keys and a narrow display|plastic and steel
early cell phone in a holster|a large brick phone with a long stubby antenna and a number pad, in a leather holster on the belt|plastic; leather
handheld game gadget|a small grey plastic console with a tiny screen and two round buttons, with a strap loop|plastic
wired headphones with a headband|two padded ear cups joined by a curved band, with a long cord|plastic; foam
""".replace('\n\n','\n')),
'current': E("""
wireless earbuds|two small rounded buds that sit in the ears with a stem on each, stored in a small charging case|plastic
over-ear wireless headphones|two cushioned ear cups on an adjustable padded band|plastic; leather-look foam
smart watch|a square or round watch with a bright glass screen and a rubber strap|aluminium; silicone
fitness band|a slim rubber band with a small display strip that fastens with a pin|silicone
smart ring|a thick smooth metal ring with a small flat sensor underside|titanium; ceramic
smart glasses|a slim frame with a small clear lens and a tiny projector on one arm|plastic; metal
VR headset|a wide boxy visor strapped across the face with a foam seal and a strap at the back|plastic; foam
bone-conduction headset|a thin band that wraps behind the head with small pads resting in front of the ears|titanium; silicone
body-worn action camera|a small box with a lens on the front, clipped to the chest on a strap|plastic
wrist-worn terminal|a rugged wrist computer with a wide screen and a buckle strap|plastic; rubber
glowing LED jacket strip|a flexible strip of tiny lights stitched down a jacket's seams|fabric and LEDs
haptic vest|a snug vest with small padded buzzers across the chest and back|neoprene and plastic
""".replace('\n\n','\n')),
'near-future': E("""
augmented-reality contact display visor|a thin, clear band across the eyes with faint lines of light floating on it|clear polymer
neural headband|a slim band around the forehead with small round sensors, glowing softly|fabric and metal
exoskeleton arm brace|a light frame of metal bars strapped along the forearm with small motors at the joints|carbon fibre and aluminium
holographic wrist display|a wide band on the wrist that projects a small floating screen above it|polymer and metal
solar-panel shoulder cape|a short cape made of thin overlapping panels that shine blue|photovoltaic fabric
translator earpiece|a tiny, nearly invisible bud that glows a faint white|ceramic
""".replace('\n\n','\n')),
'far-future': E("""
floating halo display|a ring of light that hovers above the head and shows shifting symbols|invented energy ring
skin-surface circuit patches|thin glowing patches stuck to the temples and wrists with fine lines of light|flexible polymer
gravity belt|a wide metal belt with a ring of glowing discs that hover slightly|brushed metal
liquid-metal gauntlet|a smooth silvery glove that flows and re-forms around the hand|liquid metal
memory-crystal pendant|a clear crystal on a thin cord that lights up from within|crystal and wire
full-face data mask|a smooth, featureless mask covering the face with lines of coloured light|polymer
""".replace('\n\n','\n')),
}
PINS = E("""
hard enamel lapel pin|a small metal badge with smooth, glossy colour-filled sections separated by raised metal lines|enamel and metal
soft enamel lapel pin|a small metal badge with colour sitting below raised metal lines, giving a textured surface|enamel and metal
cloisonne lapel pin|a small domed badge with glassy fired enamel in thin metal cells|enamel; gold-plated
die-struck metal lapel pin|a flat metal pin with a raised design and no colour|brass; silver
engraved lapel pin|a small metal pin with fine lines cut into its surface|silver; gold
jewelled lapel pin|a gold-tone pin set with tiny stones in a shape such as a star or a flower|crystal and gold plate
flag-style lapel pin|a small rectangular pin showing a waving flag of an invented design|enamel
ribbon-shaped awareness pin|a loop of ribbon in a single colour, with the ends crossed|enamel
boutonniere flower pin|a single artificial flower with a green stem and a pin to hold it|silk; wire
club emblem pin|a round pin with a simple original badge of a ship wheel, tree or lion|enamel
anniversary numeral pin|a pin with a large number in gold surrounded by a laurel wreath|gold-plated
humorous slogan pin|a round button pin with a funny drawing and no words|tin; paper
animal-shaped pin|a small metal animal such as a cat, owl or fish with an enamel body|enamel and metal
food-shaped pin|a tiny pin shaped like an egg, a slice of cake or an avocado|enamel
tool-shaped pin|a miniature pin of a hammer, wrench or saw in metal|brass
instrument pin|a tiny violin, trumpet or guitar in gold-tone metal|brass
planet and star pin|a small ringed planet, moon or star with a glossy finish|enamel
rainbow pin|an arched rainbow made of bands of coloured enamel|enamel
button badge|a round pin with a safety pin back and a printed image|tin; paper
tie tack pin|a small decorated head with a pointed pin and a clutch|metal
magnetic lapel pin|a small badge that attaches with a magnet on the other side of the cloth|metal and magnet
chained pair pin|two small matching pins joined by a thin chain, worn on both lapels|brass
mourning ribbon pin|a small black loop of ribbon with a plain silver pin|silk; silver
cluster of lapel pins|several small pins of different shapes grouped on one lapel|assorted metals
""")
PATCH = E("""
embroidered sew-on patch|a patch stitched with dense thread in a design, with a raised edge|polyester thread on twill
woven patch|a flat patch woven with fine thread so that the design is smooth and detailed|woven polyester
printed patch|a flat fabric patch with a printed image and a heat-cut edge|printed fabric
chenille varsity patch|a thick, fluffy looped-thread letter or shape on a felt backing|chenille and felt
leather patch|a stitched or debossed patch cut from leather with a plain design|leather
PVC rubber patch|a raised, moulded patch with flat bright colours and a rubbery feel|soft PVC
felt patch|a cut-out felt shape with simple stitched details|wool felt
sequin patch|a patch covered in tiny sequins that flip colour when brushed|sequins on fabric
iron-on patch|a patch with a hot-melt glue back that is pressed on with heat|embroidered twill
sew-on patch with merrowed edge|a patch finished with a thick rolled thread border|embroidered twill
round patch|a circular patch with a satin-stitch border|embroidered twill
shield-shaped patch|a patch shaped like a shield, with a border|embroidered twill
die-cut patch|a patch cut to follow the outline of its design|embroidered twill
hook-and-loop backed patch|a patch with a rough fabric back that sticks to a matching panel|embroidered twill
animal icon patch|a patch showing an original animal in simple bold shapes|embroidered twill
plant and flower patch|a patch showing leaves, mushrooms or flowers|embroidered twill
space theme patch|a patch with planets, stars and rockets in bright thread|embroidered twill
food theme patch|a patch showing a loaf, taco or a slice of pie|embroidered twill
tool and craft patch|a patch with a hammer, needle or paintbrush|embroidered twill
folk motif patch|a patch with a pattern of geometric folk shapes|woven thread
mending patch|a plain square of fabric with turned-under edges, to cover a worn spot|denim; canvas; cotton
elbow patch|an oval of leather or suede for the elbow of a jacket|suede; leather
knee patch|a rounded rectangle of tough fabric sewn over the knee|canvas; denim
decorative stitched patch|a patch with a freehand pattern of coloured stitching|cotton thread on fabric
glow-in-the-dark patch|a patch whose design glows green in the dark|thread and glow ink
patch panel|a large square with several small patches sewn into rows|assorted fabric
""")
BADGE_SKILL = E("""
camping merit badge|a round embroidered patch with a small tent under a pine tree and a campfire|embroidered twill
knots merit badge|a round embroidered patch with a tied rope in a looping knot|embroidered twill
first aid merit badge|a round embroidered patch with a white cross inside a green circle|embroidered twill
cooking merit badge|a round embroidered patch with a pot with steam and a wooden spoon|embroidered twill
nature merit badge|a round embroidered patch with a leaf and a small bird|embroidered twill
crafts merit badge|a round embroidered patch with a pair of scissors and a ball of yarn|embroidered twill
navigation merit badge|a round embroidered patch with a compass rose and a map|embroidered twill
swimming merit badge|a round embroidered patch with a wave and a swimming fish|embroidered twill
fire-safety merit badge|a round embroidered patch with a small flame and a bucket|embroidered twill
gardening merit badge|a round embroidered patch with a trowel and a seedling|embroidered twill
astronomy merit badge|a round embroidered patch with a ringed planet and stars|embroidered twill
bird-watching merit badge|a round embroidered patch with a pair of binoculars and a small bird|embroidered twill
cycling merit badge|a round embroidered patch with a bicycle wheel|embroidered twill
music merit badge|a round embroidered patch with a treble clef and a drum|embroidered twill
painting merit badge|a round embroidered patch with a palette and brush|embroidered twill
volunteer merit badge|a round embroidered patch with two open hands holding a heart|embroidered twill
proficiency rank badge|a square embroidered patch with a row of three chevrons|embroidered twill
achievement bar badge|a long narrow embroidered bar with a single star|embroidered twill
sash-style display of badges|a diagonal sash covered in rows of small round patches in many colours|felt and embroidered patches
rope-and-cord award display|a thick braided cord hung over the shoulder with metal medals attached|cord and metal
award pin and ribbon|a small gold pin hanging from a short ribbon in blue and white|metal and ribbon
badge vest|a sleeveless vest with rows of small patches sewn all over the front|twill vest with patches
""")
BALLS = E("""
steel ball bearing|a small, perfectly round polished steel sphere|steel
glass marble|a small clear glass ball with a coloured swirl inside|glass
wooden bead|a small smooth round bead with a hole through the middle|wood
pearl|a small lustrous round pearl in white or cream|pearl
bouncy rubber ball|a bright solid rubber ball that rebounds high|rubber
stress ball|a soft squeezable ball that holds the print of a hand|foam; gel
juggling ball|a small beanbag-style ball, softly stuffed, in a single colour|leather; cloth
ping-pong ball|a very light hollow white or orange ball with a smooth surface|celluloid; plastic
golf ball|a white ball covered in small round dimples|rubber and plastic
tennis ball|a fuzzy yellow-green ball with a curved white seam|felt and rubber
baseball|a white leather ball with raised red stitching in a figure-eight pattern|leather
cricket ball|a hard red leather ball with a raised seam around the middle|leather
football (soccer ball)|a round ball made of black and white panels|synthetic leather
American football|an oval brown leather ball with white laces and pointed ends|leather
basketball|a large orange ball with black lines and a pebbled surface|rubber; leather
volleyball|a ball in panels of white, blue and yellow with a smooth surface|synthetic leather
rugby ball|a long oval ball with a pebbled grip and four seams|synthetic; leather
beach ball|a large inflated ball with colourful striped panels|vinyl
yoga ball|a large soft inflated exercise ball, as tall as a seated hip|PVC
medicine ball|a heavy weighted ball with a leather-look cover and a grip texture|rubber; leather
bowling ball|a heavy glossy sphere with three finger holes|polyurethane
billiard ball|a smooth coloured ball with a white circle and a number|resin
crystal ball|a clear glass sphere on a small metal stand|glass
disco ball|a sphere covered in small mirror tiles that reflect light|mirror glass
punching ball|a pear-shaped bag hanging from a swivel on a short rope|leather
ornamental garden ball|a smooth heavy stone ball on a plinth|stone
Christmas bauble|a hollow, shiny glass sphere with a hanging loop|glass
cannon-free decorative iron ball|a plain black decorative iron sphere used as a doorstop or garden ornament|iron
squash ball|a small black rubber ball with a single dot|rubber
handball|a small leather ball sized to fit the palm|leather
netball|a medium ball in pale leather with fine ridges|leather
water polo ball|a yellow ball with a rough, tacky surface|rubber
bocce ball|a heavy smooth ball in a bright colour|resin
croquet ball|a hard wooden ball with a coloured stripe|wood
cat toy ball with a bell|a light ball of woven plastic with a small bell inside|plastic
wool felt ball|a small soft ball of pressed coloured wool|wool
""")
SPORT = {
'tennis': E("""
tennis racket|an oval racket head strung with a mesh of strings and a long handle wrapped in a grip|graphite; wood
tennis white outfit|a white pleated skirt or shorts with a collared white polo shirt|cotton; polyester
tennis shoes|low white court shoes with a firm sole and a toe guard|leather; synthetic
sweatband and visor|a terry cloth band around the wrist or forehead with a short-brimmed visor|cotton
""".replace('\n\n','\n')),
'baseball': E("""
baseball bat|a long smooth rounded bat with a narrow grip and a knob|wood; aluminium
baseball glove|a large leather glove with a deep pocket and laced fingers|leather
baseball uniform|a button-up jersey with matching trousers and a belt|polyester
baseball cleats|shoes with small moulded studs under the sole|synthetic
batting helmet|a hard shell helmet with an ear flap on one side|plastic
""".replace('\n\n','\n')),
'football (soccer)': E("""
football boots|low boots with small studs under the sole and a snug lace-up front|synthetic leather
football shirt and shorts|a short-sleeved jersey with a number and matching shorts|polyester
shin guards|rounded hard plates strapped over the shins|plastic and foam
goalkeeper gloves|gloves with a grippy latex palm|latex and foam
""".replace('\n\n','\n')),
'American football': E("""
football helmet|a hard shell helmet with a face cage and chin strap|plastic; steel
shoulder pads|a wide padded frame worn under the jersey|foam and plastic
football cleats|high-top shoes with firm studs|synthetic
mouthguard|a moulded rubber guard that fits over the upper teeth|rubber
""".replace('\n\n','\n')),
'ice hockey': E("""
hockey stick|a long thin stick with a flat curved blade at the bottom|wood; composite
hockey skates|stiff boots with a long steel blade under the sole|leather; steel
hockey helmet|a hard shell helmet with a cage over the face|plastic
chest and shoulder protector|a padded vest with large plates over the shoulders|foam and plastic
""".replace('\n\n','\n')),
'cycling': E("""
road bicycle|a lightweight frame with thin tyres and a curved handlebar|aluminium; carbon
cycling helmet|a vented foam helmet with a chin strap|foam and plastic
cycling shoes|stiff shoes with a metal cleat under the sole|synthetic
padded cycling shorts|tight stretchy shorts with a padded seat panel|lycra
""".replace('\n\n','\n')),
'climbing': E("""
climbing shoes|tight, snug shoes with smooth rubber soles and a curved toe|leather; rubber
climbing harness|a set of padded loops around the waist and legs with a belay loop|nylon
climbing chalk bag|a small bag worn at the back of the waist and filled with white powder|cotton
carabiner|a metal loop with a spring gate|aluminium
""".replace('\n\n','\n')),
'gym': E("""
barbell|a long steel bar with weighted plates at the ends|steel
dumbbell|a short bar with a fixed weight on each end|iron; rubber
kettlebell|a cast iron ball with a handle on top|iron
weightlifting belt|a wide leather belt with a thick back|leather
weightlifting shoes|flat firm shoes with a raised heel|synthetic
yoga mat|a rolled rectangular mat with a grippy surface|rubber
""".replace('\n\n','\n')),
}
# range-audit lists: family -> (plastic/cheap rows, novelty rows)
AUDIT = {
'bracelet': (E("""
plastic bangle|a rigid glossy ring of coloured plastic that slips over the hand|plastic
jelly bracelet|a stretchy translucent rubber ring in bright colours|silicone
beaded elastic bracelet|a row of coloured plastic beads on a stretch cord|plastic beads
friendship string bracelet|a woven band of coloured threads with a knot closure|cotton thread
plastic charm bracelet|a chain with cheap coloured plastic charms|plastic; metal
"""), E("""
animal-charm novelty bracelet|a chain hung with tiny animals in enamel|enamelled metal
candy-bead novelty bracelet|a stretch cord strung with beads that look like wrapped sweets|plastic
watch-style novelty bracelet|a plastic wrist band with a toy dial face|plastic
light-up bracelet|a soft band with LEDs that flash|silicone and LEDs
""")),
'necklace': (E("""
plastic bead necklace|a long strand of big round coloured plastic beads|plastic
plastic pendant necklace|a thin cord with a bright plastic pendant|plastic
choker of stretch plastic|a tight band of tiny ridged plastic that stretches over the head|plastic
costume jewellery pearl necklace|a strand of glossy pearl-look plastic beads|plastic
"""), E("""
toy-charm novelty necklace|a cord with a tiny toy such as a rubber duck|plastic
glow stick necklace|a loop of glowing plastic tube|plastic
candy necklace|a stretch cord of sweet-shaped beads|plastic
miniature bottle necklace|a tiny sealed glass bottle with a cork|glass
""")),
'ring': (E("""
plastic toy ring|a bright plastic band with a large moulded gem on top|plastic
adjustable cheap metal ring|a thin split band that opens for any finger|base metal
costume gemstone ring|a large glass stone in a plain metal setting|glass and base metal
plastic stacking rings|several thin coloured rings worn together|plastic
"""), E("""
animal head novelty ring|a ring topped with a small moulded animal head|resin
mood ring|a band with a stone that changes colour|glass and metal
flower-top toy ring|a ring topped with a big plastic flower|plastic
puzzle ring|several linked bands that interlock into one ring|steel
""")),
'brooch': (E("""
plastic flower brooch|a bright flower with a pin on the back|plastic
costume rhinestone brooch|a cluster of glass stones in a plain metal setting|base metal and glass
felt animal brooch|a stitched felt animal with a safety pin|felt
acrylic brooch|a laser-cut flat shape in coloured acrylic|acrylic
"""), E("""
food-shaped novelty brooch|a tiny brooch like a croissant or an egg|enamel
bug-shaped novelty brooch|a brooch like a beetle with sparkling stones|enamel
miniature teapot brooch|a tiny teapot with a hinged lid|enamel
kitten face brooch|a round face with whiskers and ears|resin
""")),
'watch': (E("""
plastic digital watch|a light rectangular watch with a small display and a rubber strap|plastic
jelly-strap watch|an analogue watch with a see-through rubber strap|plastic
cheap quartz watch|a slim round watch with a thin strap and a plain face|base metal
plastic wind-up watch|a toy watch with a plastic dial and strap|plastic
"""), E("""
cartoon-dial novelty watch|a watch with a face showing a smiling animal whose arms are the hands|plastic
backwards-running watch|a watch with the numbers in reverse order|plastic
big-dial oversized watch|an extremely wide round watch face|plastic
cuckoo-clock wristwatch|a wrist clock with a tiny bird that pops out|metal and plastic
""")),
'belt': (E("""
plastic buckle belt|a webbing belt with a moulded plastic buckle|nylon and plastic
elastic stretch belt|a stretchy fabric belt with a plain buckle|elastic
cheap faux leather belt|a thin belt with a shiny surface and a metal buckle|vinyl
canvas web belt|a flat woven belt with a sliding metal bar|cotton
"""), E("""
oversized belt buckle|an enormous decorative buckle in the shape of a horseshoe or star|metal
chain belt of coins|a long chain hung with large gold-coloured coins|metal
light-up belt|a belt with a row of small flashing lights|fabric and LEDs
toy holster belt|a belt with a toy pistol-shaped holder|plastic
""")),
'wallet': (E("""
plastic card holder|a clear plastic sleeve that holds cards|plastic
velcro nylon wallet|a bright folding wallet fastened with hook-and-loop strip|nylon
cheap vinyl wallet|a plain folding wallet in shiny plastic leather-look|vinyl
zip coin pouch wallet|a small zipped wallet in coloured plastic|plastic
"""), E("""
animal-face novelty wallet|a small wallet shaped like a cat face|plush
food-shaped wallet|a coin purse like an avocado half|fabric
duct tape wallet|a folding wallet made of silver tape|tape
mini suitcase wallet|a tiny suitcase for cards|vinyl
""")),
'umbrella': (E("""
cheap folding umbrella|a thin umbrella with a plastic handle and light ribs|nylon and plastic
clear plastic dome umbrella|a see-through umbrella shaped like a bell|plastic
plastic poncho umbrella|a transparent shell with a stiff plastic handle|PVC
""".replace('\n\n','\n')), E("""
animal-shaped novelty umbrella|an umbrella whose canopy has ears and eyes on the top|nylon
hat umbrella|a small umbrella that fits on the head with a band|nylon
upside-down umbrella|a double-layer umbrella that opens inside out|nylon
""".replace('\n\n','\n'))),
'glove': (E("""
cheap knit stretch glove|a thin one-size knit glove|acrylic
plastic disposable glove|a thin clear loose glove|plastic
rubber washing-up glove|a long yellow glove with a flared cuff|latex
"""), E("""
animal-paw novelty gloves|soft gloves with a paw pad on the palm|plush
fingerless glove with claws|a fingerless glove with pointed claw tips|plastic
oversized foam hand|a huge foam hand with one finger raised|foam
""")),
'fan': (E("""
folding plastic fan|a fan with plastic ribs and a printed paper top|plastic and paper
paper fan on a stick|a paper rectangle on a wooden handle|paper
battery desk fan|a handheld fan with a spinning plastic blade|plastic
"""), E("""
novelty cartoon fan|a flat fan with a smiling face|paper
fan with a water mister|a fan with a small tank and a nozzle|plastic
""")),
}
