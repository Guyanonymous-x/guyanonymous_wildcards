"""v40 data C: trades tools and related equipment. trade -> rows 'name|description|materials|hand/power/gear'."""
def S(x): return [i.strip() for i in x.split(';') if i.strip()]
def T(rows):
    out = []
    for r in rows.strip().split('\n'):
        if not r.strip(): continue
        n, d, m, k = [p.strip() for p in r.split('|')]
        out.append((n, d, S(m), k))
    return out
TRADES = {}
TRADES['carpentry'] = T("""
claw hammer|a hand hammer with a flat striking face on one side of the head and a curved split claw on the other for pulling nails|steel head with hickory handle; steel head with fibreglass handle|hand
hand saw|a flat, toothed steel blade with a wooden or plastic grip at one end that cuts wood with pushing strokes|steel blade with beech handle; steel blade with plastic handle|hand
tenon saw|a rectangular blade stiffened with a brass or steel spine along the top edge, for fine joints|steel with brass back and beech handle|hand
coping saw|a thin removable blade held tight in a deep U-shaped frame, for cutting curves|steel blade with a spring-steel frame|hand
wood chisel|a flat steel blade with a bevelled edge and a handle, struck or pushed to pare wood|chrome-vanadium steel with boxwood handle; steel with plastic handle|hand
block plane|a small metal-bodied plane with a low-angled blade held in the palm for smoothing end-grain|cast iron body with steel blade|hand
jack plane|a long wooden or iron plane with a flat sole and a single blade that shaves wood flat|beech body with steel blade; iron body with steel blade|hand
spirit level|a long, straight bar with glass vials of liquid and a bubble that shows true horizontal and vertical|aluminium with acrylic vials|hand
combination square|a ruled steel blade that slides along a cast head set at 90 and 45 degrees|steel blade with a cast-iron head|hand
tape measure|a coiled strip of flexible steel with markings, retracting into a handheld case|steel tape in plastic case|hand
carpenter's pencil|a flat, oval pencil with a thick lead that does not roll away|graphite and wood|hand
mallet|a wooden or rubber-headed hammer with a broad face, for striking chisels without damage|beech; rubber with wooden handle|hand
circular saw|a handheld saw with a round toothed blade spinning in a guard, with a handle and trigger|steel blade with plastic housing|power
jigsaw|a handheld power saw with a thin vertical blade moving up and down, for cutting curves|steel blade with plastic body|power
cordless drill|a pistol-shaped drill with a chuck at the front, a trigger and a battery pack at the base|plastic body with steel chuck|power
router|a motor in a base with a bit that spins to cut grooves and shaped edges, held with two handles|aluminium base with plastic housing|power
belt sander|a handheld tool with a looped abrasive belt running round two rollers|plastic housing with abrasive belt|power
nail gun|a handheld tool with a long magazine of nails fired in under air pressure|aluminium and plastic|power
workbench with vice|a heavy table with a thick top and a screw vice on the front edge to clamp work|beech; maple; oak|gear
bar clamp|a long steel bar with a fixed jaw at one end and a sliding jaw at the other, tightened with a screw|steel; aluminium|gear
""")
TRADES['masonry'] = T("""
brick trowel|a flat steel blade shaped like a diamond with a cranked handle, used to scoop and spread mortar|steel blade with wooden handle|hand
pointing trowel|a small pointed trowel for packing mortar into the gaps between bricks|steel with wooden handle|hand
bolster chisel|a wide, flat-edged cold chisel for cutting bricks and stone|forged steel|hand
club hammer|a short-handled, double-faced hammer with a heavy head used with chisels|steel with hickory handle|hand
brick hammer|a hammer with a square face on one side and a chisel edge on the other for trimming bricks|steel with hickory handle|hand
plumb bob|a pointed brass weight hung from a string to mark a perfect vertical line|brass; steel|hand
mortar board|a flat square board on which mortar is stacked and mixed|plywood; steel|gear
jointing iron|a curved steel rod used to strike a groove in wet mortar joints|steel|hand
masonry line|a taut string pulled between two corner pins as a straight guide for laying a course|nylon cord|gear
stone mason's point|a pointed steel chisel that is hammered to rough-shape stone|forged steel|hand
angle grinder with diamond blade|a handheld power tool with a spinning disc used to cut brick, tile or stone|steel and diamond grit; plastic housing|power
cement mixer|a rotating drum on a stand with a motor, which tumbles sand, cement and water into mortar|steel drum; plastic drum|power
wheelbarrow|a single-wheeled tray with two handles to carry sand, bricks or mortar|steel tray; plastic tray|gear
hod|a V-shaped trough on a long pole for carrying bricks up a ladder|wood; steel|gear
scaffold tower|a tall frame of steel tubes and planks on wheels for working up high|steel tube; aluminium|gear
""")
TRADES['plumbing'] = T("""
pipe wrench|an adjustable wrench with serrated jaws that bite into round pipe, with a long handle|cast iron; forged steel|hand
adjustable spanner|a wrench with a movable jaw set by a thumbwheel|chrome steel|hand
basin wrench|a long-shafted wrench with a swivelling jaw head that reaches nuts behind a sink|steel|hand
pipe cutter|a small tool with a wheel that bites round a copper pipe as the tool is turned|steel with a brass body|hand
tube bender|a pair of handles with a grooved wheel that forms smooth bends in copper tubing|steel|hand
hacksaw|a thin toothed blade stretched across a metal frame with a pistol grip|steel blade with a metal frame|hand
plunger|a rubber cup on a wooden handle that pushes air and water through a blocked drain|rubber with wooden handle|hand
drain snake|a long coil of flexible spring steel on a hand-cranked drum, pushed into blocked drains|spring steel|hand
blowtorch|a pencil-flame torch on a small gas bottle used to heat copper joints for soldering|brass; steel|hand
solder and flux|a spool of soft metal wire and a pot of paste that bonds copper pipe joints|lead-free solder; tin|gear
PTFE tape|a roll of thin white tape wound round threads to seal pipe joints|PTFE film|gear
pipe threader|a rotating die that cuts threads on the end of a pipe|hardened steel|hand
press fitting tool|a power tool with jaws that squeeze a metal fitting onto a pipe|steel and plastic|power
drain-camera inspection reel|a long flexible cable with a camera lens at the end and a hand-held screen|plastic cable; camera head|power
jetting machine|a pressure washer pump on a trolley with a hose to blast out drains|steel and plastic|power
""")
TRADES['electrical'] = T("""
wire strippers|a pair of pliers with notched jaws that cut through insulation without cutting the wire|steel with rubber grips|hand
side-cutters|pliers with angled blades that cut wire close to a surface|steel with rubber grips|hand
insulated screwdriver|a screwdriver with a shaft coated in thick plastic to guard against shocks|chrome-vanadium steel with rubber grip|hand
multimeter|a handheld box with a dial and display that reads volts, amps and resistance through two probes|plastic case|hand
voltage tester pen|a pen-shaped tool that lights when it nears a live wire|plastic|hand
fish tape|a long flat steel ribbon on a reel for pulling cable through walls and conduit|steel; fibreglass|hand
conduit bender|a curved shoe with a long handle that bends metal tubing|steel; aluminium|hand
cable cutters|big-handled shears that cut through thick cables in one squeeze|steel with rubber grips|hand
crimping tool|a plier-type tool that squeezes metal connectors onto cable ends|steel|hand
lineman's pliers|heavy pliers with flat jaws, a side cutter and a wire grip|forged steel with rubber grips|hand
soldering iron|a pen-like tool with a heated tip used to join wires and circuit parts|plastic or wood handle with a copper tip|power
heat gun|a hand-held hot air blower used to shrink insulating sleeves|plastic body with a metal nozzle|power
hammer drill|a power drill with a pounding action for making holes in masonry|plastic body with steel chuck|power
insulated gloves|thick rubber gloves rated for high voltage with leather over-gloves|rubber with leather|gear
climbing spurs and belt|steel spikes strapped to the boots with a body belt and strap for climbing poles|steel and leather|gear
""")
TRADES['welding_metalwork'] = T("""
welding helmet|a hood with a dark glass window that darkens when an arc strikes, protecting the eyes and face|plastic shell with auto-darkening lens|gear
welding gloves|thick, long-cuffed leather gloves for heat and sparks|cowhide; split leather|gear
arc welder|a box with a cable and a clamp that feeds a high current into a rod to melt metal joints|steel casing with copper cables|power
MIG welder|a welding machine with a wire fed through a gun, shielded by gas|steel casing|power
oxy-acetylene torch|a pair of gas bottles and hoses to a torch with a hot flame for cutting and welding|brass torch with steel bottles|gear
chipping hammer|a hammer with a point and a chisel edge to knock slag from a weld|forged steel with a spring handle|hand
angle grinder|a handheld spinning disc used to cut, grind and polish metal|steel disc with plastic housing|power
anvil|a heavy block of iron with a flat top, a horn on one end and a hole for tools, used to shape hot metal|forged steel; cast iron|gear
blacksmith's hammer|a forging hammer with a wide flat face and a rounded peen on the other side|forged steel with ash handle|hand
tongs|long steel pincers that hold hot metal|wrought iron|hand
forge|a hearth with a fire pot and a bellows or fan that heats metal to red hot|brick; steel|gear
metal file|a hardened steel bar with fine ridges used to smooth and shape metal|hardened steel|hand
bench vice|a heavy clamp bolted to a bench with two flat jaws and a screw handle|cast iron|gear
bandsaw|a machine with a long, continuous toothed steel loop that cuts bars and tubes|steel|power
metal lathe|a machine that spins metal while a fixed tool shaves it into a round shape|cast iron and steel|power
sheet-metal shears|large hand snips with offset handles that cut sheet metal|forged steel|hand
rivet gun|a handheld tool that pulls or hammers rivets to join sheet metal|steel|hand
""")
TRADES['mechanics'] = T("""
socket wrench set|a ratcheting handle with a range of cup-shaped sockets that fit over bolt heads|chrome vanadium steel|hand
open-ended spanner|a flat steel wrench with a U-shaped jaw at each end of different sizes|chrome vanadium steel|hand
torque wrench|a long wrench with a dial or click mechanism that measures how tightly a bolt is turned|steel with a plastic grip|hand
feeler gauge|a fan of thin metal blades of known thickness used to check small gaps|steel|hand
creeper|a flat low board with wheels, on which a mechanic lies to roll under a vehicle|plastic; steel and padded vinyl|gear
hydraulic jack|a squat unit with a long pump handle that lifts heavy vehicles|steel|gear
axle stands|a pair of steel supports with ratcheting posts that hold a lifted vehicle|steel|gear
oil filter wrench|a strap or cup that grips and turns a round oil filter|steel; rubber|hand
impact wrench|a power tool that delivers hammering bursts of torque to loosen stuck nuts|steel and plastic|power
air compressor|a tank and motor that stores compressed air for tools|steel tank|power
diagnostic scanner|a handheld box with a cable that plugs into a vehicle's computer to read faults|plastic|hand
coverall|a one-piece work suit with long sleeves, zip front and many pockets|cotton drill; flame-retardant cotton|gear
shop rag|a square of absorbent cloth for wiping oil and grease|cotton; microfibre|gear
tyre lever|a long flat bar with a curved end to prise a tyre off a rim|steel|hand
brake bleeding kit|a hose and bottle with a one-way valve that draws old fluid from brake lines|plastic; rubber|hand
""")
TRADES['agriculture'] = T("""
spade|a flat blade on a long shaft with a step on top, used to dig and lift soil|steel blade with ash handle|hand
garden fork|a handle with four straight tines for turning and loosening soil|forged steel with ash handle|hand
hoe|a flat blade at right angles to a long handle, used to chop weeds|steel with wooden handle|hand
rake|a long handle with a bar of teeth at one end for gathering hay or smoothing soil|steel teeth with ash handle; plastic teeth|hand
scythe|a long curved blade on a bent two-handled shaft, swung low to cut grass and grain|steel blade with ash snath|hand
sickle|a short curved blade with a short handle, used for cutting by hand|steel with wooden handle|hand
pitchfork|a long wooden handle with two or three sharp tines for lifting hay|forged steel with ash handle|hand
secateurs|a pair of short hand shears with curved blades that cut small branches|steel with plastic grips|hand
billhook|a short, hooked blade on a handle for trimming hedges and small trees|forged steel with wooden handle|hand
milking stool|a three-legged wooden seat low to the ground|wood|gear
seed drill|a wheeled hopper that drops seeds in rows into the soil|steel|gear
plough|a heavy blade on a frame that turns over the soil in strips as it is pulled|cast iron|gear
tractor|a heavy four-wheeled vehicle with large rear tyres used to pull farm machinery|steel|power
combine harvester|a big machine with a wide rotating header that cuts and threshes grain|steel|power
chainsaw|a handheld saw with a chain of teeth running round a guide bar, driven by a petrol engine|steel with plastic housing|power
hay bale hook|a hand hook with a T-handle used to lift and drag bales|steel with wooden handle|hand
leather work gloves|stout gloves for fencing and handling|cowhide; goatskin|gear
tall waterproof rubber boots|tall waterproof rubber boots|rubber|gear
""")
TRADES['textiles_sewing'] = T("""
sewing machine|a machine with a needle and thread spool that stitches cloth when a motor or treadle turns it|cast iron body; plastic body|power
treadle sewing machine|an old sewing machine driven by the foot pushing a pedal and belt|cast iron and wood|gear
tailor's shears|long, heavy scissors with a bent handle and a long blade for cutting cloth on a table|forged steel|hand
pinking shears|scissors with zig-zag blades that cut cloth with a toothed edge that does not fray|steel|hand
tailor's chalk|a flat triangle of chalk for marking lines on cloth|chalk; wax|hand
tape measure|a long flexible strip of cloth marked in units, used to take body measurements|fibreglass cloth|hand
thimble|a small metal cap worn on the fingertip to push the needle|brass; silver; leather|hand
needle and thread|a slim metal needle with an eye at one end and a spool of thread|steel; cotton thread|hand
pin cushion|a small stuffed pad into which pins are stuck|cotton; felt|gear
seam ripper|a small tool with a hook and a point for cutting stitches|steel with plastic handle|hand
tailor's ham|a tight, firm cushion shaped like a ham, over which curved seams are pressed|wool and cotton|gear
steam iron|a heavy, flat iron with a steam vent in the sole for pressing cloth|steel soleplate|power
dress form|a torso-shaped mannequin on a stand, padded and covered in cloth, for fitting clothes|cotton; foam|gear
loom|a wooden frame with threads stretched on it, through which a shuttle passes to make woven cloth|wood|gear
spinning wheel|a wooden wheel with a treadle and a spindle that twists wool into yarn|wood|gear
drop spindle|a weighted stick on which wool is twisted into yarn by hand|wood|hand
knitting needles|two long thin rods used to loop yarn into rows|bamboo; steel; plastic|hand
crochet hook|a thin rod with a small hook at the tip|aluminium; bamboo|hand
embroidery hoop|two round rings that hold cloth taut for stitching|wood; plastic|gear
""")
TRADES['leatherwork_cobbling'] = T("""
round knife|a curved, semicircular blade with a handle at the centre, for cutting leather|steel with wooden handle|hand
awl|a pointed spike with a wooden handle, for making holes in leather before stitching|steel and wood|hand
leather punch|a hand-held tool with a rotating head of different-sized holes|steel|hand
stitching pony|a wooden clamp on a leg that holds leather up while it is sewn|wood|gear
edge beveller|a small tool with a notch that cuts a rounded edge on leather|steel|hand
skiving knife|a flat blade used to thin the edge of leather|steel|hand
cobbler's last|a foot-shaped block of wood or metal on which a shoe is shaped|wood; iron|gear
shoe hammer|a hammer with a flat face and a tapered head used to beat leather|steel|hand
cobbler's stand|a heavy iron foot-shaped anvil on a pole to hold shoes for nailing|cast iron|gear
waxed linen thread|a strong, waxed thread used for hand-stitching leather|linen|gear
leather mallet|a mallet with a broad face and a hardwood handle|rawhide; wood|hand
rivet setter|a small tool with a cup that spreads the end of a rivet|steel|hand
""")
TRADES['pottery_glass'] = T("""
potter's wheel|a spinning flat disc on which a lump of clay is shaped by hand while it turns|steel and cast iron; wood|power
kick wheel|a potter's wheel turned by the foot kicking a large disc below|wood and iron|gear
wire clay cutter|a thin wire with a wooden handle at each end, pulled through clay to cut it|steel wire and wood|hand
wooden modelling tool|a flat or pointed stick for shaping clay|boxwood; bamboo|hand
rib|a flat, curved paddle for smoothing the wall of a pot|wood; rubber; metal|hand
kiln|a thick-walled oven with a front door, where clay is fired at high heat|firebrick; ceramic fibre|power
glassblowing pipe|a long hollow steel tube with a mouthpiece, on which molten glass is gathered and blown|stainless steel|hand
glassblower's jacks|a pair of tongs with two flat blades that squeeze and shape hot glass|steel|hand
glory hole furnace|a gas furnace with a small opening where glass is reheated|firebrick|power
marver|a flat steel table on which hot glass is rolled|steel|gear
annealing oven|a box oven that cools glass slowly to prevent cracking|steel and brick|power
heat-proof gloves|thick gloves for handling hot ware|aramid; leather|gear
""")
TRADES['mining_quarry'] = T("""
pickaxe|a heavy tool with a long wooden handle and a pointed iron head, swung to break hard ground|forged steel with hickory handle|hand
miner's helmet with lamp|a hard hat with a head lamp and cable to a battery on the belt|plastic shell; metal and plastic lamp|gear
safety lamp|a flame lamp surrounded by wire mesh so that it does not ignite gas|brass and glass; steel and glass|gear
rock drill|a heavy pneumatic tool with a long steel bit that bores holes in rock|steel|power
hand-held jackhammer|a heavy power chisel that pounds up and down to break concrete and rock|steel|power
miner's cart|a small wheeled wagon that runs on rails to carry ore|iron; steel|gear
ore pan|a wide, shallow metal dish used to swirl gravel and water to find gold|steel; plastic|hand
sledgehammer|a long-handled hammer with a heavy double-faced head|steel with hickory handle|hand
cage hoist|a platform on a winch cable for lowering people and cargo down a shaft|steel|power
respirator|a mask with filters for dusty air|rubber; plastic|gear
rope harness|a body harness of webbing with a rope and clips|nylon webbing|gear
""")
TRADES['forestry'] = T("""
felling axe|an axe with a long handle and a sharp, heavy, wedge-shaped head, for chopping trees|forged steel with hickory handle|hand
splitting maul|a heavy axe with a wide wedge for splitting logs|forged steel with fibreglass handle|hand
crosscut saw|a long, flexible two-person saw with teeth along one edge and a handle at each end|steel with wooden handles|hand
log tongs|a pair of curved hooks used to grip and drag logs|forged steel|hand
peavey|a long pole with a metal spike and a hinged hook for rolling logs|steel with ash handle|hand
chainsaw chaps|protective leg guards with layers of fibre that jam the saw chain|nylon with ballistic fibre|gear
hard hat with ear muffs and visor|a hard hat fitted with a mesh visor and ear defenders|plastic; steel mesh|gear
log splitter|a machine with a ram that pushes logs against a wedge|steel|power
climbing spikes|boot-strapped spikes and a rope, used to climb trees|steel and leather|gear
""")
TRADES['fishing_maritime'] = T("""
fishing rod|a long, thin, flexible rod with a reel and guides along the shaft|fibreglass; carbon fibre; bamboo|hand
landing net|a mesh bag on a hoop with a handle, to lift fish|nylon mesh with aluminium|hand
fishing knife|a thin flexible blade for cleaning fish|stainless steel|hand
cast net|a round net with weights along the edge, thrown by hand to spread over the water|nylon|hand
lobster pot|a box-shaped trap of mesh or wood with an entrance funnel|wood and netting; coated wire|gear
marlinspike|a pointed steel spike used to separate strands of rope when splicing|steel|hand
deck winch|a drum with a crank that hauls ropes and nets|steel|power
sea boots|knee-high rubber boots with heavy tread soles|rubber|gear
oilskin foul-weather gear|waterproof jacket and trousers of waxed fabric|oilskin; PVC|gear
life jacket|a bright foam-filled vest for floating|nylon with foam|gear
sextant|a handheld instrument with mirrors and a scale for measuring the angle of the sun above the horizon|brass; aluminium|hand
ship's compass|a bowl of liquid holding a floating card marked with directions|brass and glass|gear
""")
TRADES['medicine_care'] = T("""
stethoscope|two earpieces on flexible tubes joining a chest piece that listens to the body|stainless steel and rubber|hand
blood pressure cuff|a cloth band with a rubber bladder and a pump and dial that measures blood pressure|nylon and rubber|hand
reflex hammer|a small rubber-headed hammer with a handle for testing nerves|rubber and steel|hand
otoscope|a handheld lamp with a funnel tip for looking in the ear|plastic and steel|hand
surgical scalpel|a small handle that holds a replaceable sharp blade|stainless steel|hand
forceps|a pair of tweezers-like arms with locking handles|stainless steel|hand
surgical scissors|small pointed or blunt-tipped scissors with ring handles|stainless steel|hand
medical gloves|thin, snug, disposable gloves|nitrile; latex|gear
surgical mask|a pleated paper mask with ear loops|non-woven fabric|gear
scrubs|loose cotton short-sleeved shirt and trousers for working in medical areas|cotton; polyester|gear
thermometer|a small probe that reads body temperature|plastic and glass|hand
syringe|a plastic barrel with a plunger and a needle at the tip|plastic and steel|hand
""")
TRADES['cooking_kitchen'] = T("""
chef's knife|a long, broad blade with a curved edge and a pointed tip, with a full handle|high-carbon steel; stainless steel|hand
paring knife|a short blade with a pointed tip, for peeling and trimming|stainless steel|hand
bread knife|a long serrated blade|stainless steel|hand
cleaver|a heavy, rectangular blade for chopping bone|carbon steel with wooden handle|hand
wooden spoon|a long spoon with an oval bowl|beech; olive wood|hand
whisk|a bundle of looped wires on a handle used to beat eggs and cream|stainless steel|hand
rolling pin|a long, smooth cylinder used to roll out dough|hardwood; marble|hand
cast-iron skillet|a heavy round frying pan with a long handle|cast iron|gear
stockpot|a tall, large, round pot with two side handles|stainless steel|gear
mandoline slicer|a flat board with an adjustable blade over which vegetables are slid|stainless steel and plastic|hand
mortar and pestle|a heavy bowl and a club-shaped tool used to crush spices|marble; granite; wood|hand
chef's whites|a double-breasted white cotton jacket and checked trousers|cotton|gear
apron|a long cotton bib apron tied at the waist|cotton; canvas|gear
tongs|spring-loaded metal pincers for lifting food|stainless steel|hand
stand mixer|a heavy countertop mixer with a bowl and a tilting head|metal|power
""")
TRADES['painting_decorating'] = T("""
paintbrush|a wooden or plastic handle holding a bundle of bristles in a metal ferrule|hog bristle; nylon|hand
paint roller|a cylindrical sleeve of fluffy fabric on a handle|foam; lambswool|hand
putty knife|a flat, thin blade used to spread filler|steel|hand
scraper|a flat blade on a handle used to strip old paint|steel|hand
masking tape|a roll of papery tape that sticks to surfaces to protect them|crepe paper|gear
drop cloth|a large sheet to cover floors|canvas; plastic|gear
step ladder|an A-shaped folding ladder|aluminium; fibreglass|gear
paint sprayer|a pump and gun that sprays paint in a fan|plastic and metal|power
wallpaper paste brush|a broad brush for applying paste|bristle|hand
decorator's overalls|white cotton overalls|cotton|gear
""")
TRADES['surveying_construction'] = T("""
theodolite|a telescope on a tripod that measures horizontal and vertical angles|brass; aluminium|gear
dumpy level|a telescope on a tripod that shows a level line of sight|aluminium|gear
surveyor's chain|a long chain of metal links used to measure distances|steel|gear
measuring wheel|a wheel on a handle that counts distance as it is rolled|plastic; steel|hand
hard hat|a rigid helmet with a brim|plastic|gear
high-visibility vest|a bright orange or yellow vest with reflective bands|polyester|gear
steel-toe boots|sturdy lace-up boots with a steel toe cap|leather and steel|gear
jackhammer|a heavy power tool that pounds up and down|steel|power
concrete vibrator|a long vibrating rod placed into wet concrete|steel and rubber|power
power trowel|a spinning set of blades that smooths concrete|steel|power
""")
