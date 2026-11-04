"""v78 stage A - cyberpunk (cy_), steampunk (sp_) and western (we_): styles, characters, places, objects and vehicles, by looks only, with shared pools per genre."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from famlib import P
def A(l): return 'an' if l[0].lower() in 'aeio' or (l[0].lower() == 'u' and not l.lower().startswith(('uni', 'use'))) else 'a'
def rows(t): return [r.split('|') for r in t.strip().split('\n')]

CY = dict(noun='cyberpunk', pre='cy',
STYLES="""neon_noir|neon noir|wet streets, pink and cyan neon, deep black shadows and cigarette smoke|rain-slick reflections of neon signs|a flickering holographic ad overhead
corporate_dystopia|corporate dystopia|glass towers, clean white lobbies, drones and identical uniformed workers under a grey sky|cold white light with a hazy sky|a huge corporate logo glowing on a tower
street_grit|street grit|cluttered alleys, hand-painted signs, tangled cables, steam vents and patched clothing|dirty orange sodium light|a pile of discarded machine parts
retro_cyberpunk|retro cyberpunk|chunky screens, green text, big shoulder pads, grids and visible cables|purple and teal glow from old monitors|a heap of old cassette tapes
rain_megacity|rain megacity|endless towers, flying traffic lanes, rain streaks and umbrellas below|blue-grey light with glowing windows|a crowd of umbrellas on a walkway
biohack|biohacker|glass tanks, glowing implants, grafted limbs and clinical green light|green and white lab light|a tray of tiny implants
hacker_den|hacker den|a cramped room of stacked screens, cables, energy drink cans and dim glow|blue-white screen light in a dark room|a coffee-stained keyboard
night_market|night market|dense hanging signs, steaming food stalls, bargain tech and crowds in the rain|warm lantern light with neon edges|a stall of glowing gadgets""",
CLASS="""netrunner|netrunner|a long hooded coat with glowing seams, a visor and cables from the neck|a worn cyberdeck on the forearm
street_samurai|street samurai|an armoured coat, a cyber arm with exposed pistons and a mirrored visor|a glowing blade at the hip
fixer|fixer|a sharp long coat, tinted glasses and rings that glow|a tablet of contacts and a pocket of data chips
exec|corporate executive|a pressed silver suit, a slim glowing earpiece and polished boots|a thin glass tablet
ripperdoc|ripperdoc|a stained surgical apron, magnifying goggles and a tool belt|a tray of chrome limbs and eyes
courier|courier|a padded jacket, a rain mask and a bag strapped across the chest|a stack of sealed parcels
gang_member|gang member|a studded jacket with painted shoulders, dyed spikes of hair and glowing tattoos|a chain and a baseball bat with lights
android|android|smooth synthetic skin with visible seams at the wrists and neck, calm eyes and plain clothes|a faint blue glow in the eyes
detective|detective|a worn trench coat, a hat and a cybernetic eye that glows amber|a flickering lighter
street_vendor|street vendor|an apron over a padded coat, a head scarf and steaming bowls|a cart of noodles with a hanging neon sign
streamer|streamer|a bright jacket, a floating camera drone and glowing face paint|a ring light on a stick
smuggler|smuggler|a patched jacket, a respirator and many pockets|a duffel bag with a glowing lock
bartender|bartender|a waistcoat, a chrome hand and a neon-trimmed apron|a tall glowing cocktail
scavenger|tech scavenger|a canvas coat, a headlamp and a backpack of spare parts|a magnet on a stick
security|corporate security|black armour with a visor, a stun baton and a shoulder light|a shield with a company mark
rebel|rebel|a ragged hooded jacket, a face covering and spray-paint stained gloves|a spray can and a sticker roll
pilot|hover pilot|a flight jacket, goggles on the forehead and gloves|a helmet under the arm
dancer|club performer|a glittering jacket, light-up boots and glowing body paint|a handheld light baton""",
LOC="""noodle_stall|neon noodle stall|a narrow steaming stall under a buzzing neon sign with stools in the rain
neon_alley|neon alley|a narrow alley of stacked signs, dripping pipes and puddles that glow
tower_lobby|megatower lobby|a vast white lobby with a hovering logo, drones and a polished floor
rooftop|rooftop|a wet rooftop with antennas, a water tank and a view of endless lit towers
data_den|data den|a cramped room of mismatched screens, cables on the floor and a hammock
clinic|back-alley clinic|a glowing green room with a reclining chair, tools and jars of parts
night_market|night market|crowded lanes under tangled cables, food smoke, hanging screens and signs
arcade|arcade|rows of glowing machines in the dark, carpet with stains and flickering lights
subway|underground platform|a tiled platform with graffiti, a digital board and a humming train
hab_corridor|hab block corridor|a low corridor of stacked metal doors, cables, laundry and a flickering strip light
hacker_lab|hacker lab|workbenches covered in open machines, a server rack and a soldering iron
nightclub|nightclub|a packed floor of bodies, laser beams, a raised booth and haze
harbour|container harbour|towering cranes, stacked containers with painted marks and wet concrete
server_farm|server farm|endless rows of humming racks, blue lights and cold fog on the floor
micro_flat|micro apartment|a tiny room with a fold-down bed, a wall screen and a rain-streaked window
under_highway|street under the highway|concrete pillars, tents, burning barrels and a rumble overhead
boardroom|corporate boardroom|a long glass table, a skyline wall and a hovering projection
scrapyard|scrapyard|mountains of broken machines, a crane and a glowing fire
taxi_rank|hover taxi rank|a rooftop pad of parked flying cabs, puddles and a ticket booth
garden|rooftop garden|rows of grow lights, hydroponic tubes and a view of the city
bar|dive bar|a dim bar with a chrome counter, a flickering sign and mismatched stools
vending_alley|vending alley|a wall of glowing vending machines and a puddle full of cans
bridge|rain-soaked bridge|a long steel bridge between towers, lit with red warning lights
cargo_dock|cargo dock|loading drones, conveyor belts and a hanging crane at night""",
ITEM="""cyberdeck|cyberdeck|a chunky portable computer with a keyboard, a tiny screen, ports and stickers
implant|neural implant|a tiny silver chip with glowing gold traces on a velvet pad
cyberarm|cybernetic arm|a chrome arm with exposed pistons, plated fingers and blue light under the plates
hologram|hologram projector|a small disc projecting a rotating blue figure in the air
smart_pistol|smart pistol|a boxy pistol with a glowing sight, a small screen and a worn grip
datachip|data chip|a tiny black chip with gold contacts and a handwritten label
visor|visor|a sleek curved visor with a glowing amber display
jacket|neon jacket|a black jacket with light-up piping and a large glowing back panel
drone|drone|a small four-rotor drone with a camera eye and a blinking light
sign|neon sign|a crooked neon sign with some letters burnt out
can|energy drink can|a dented can with a bright label and condensation
chit|credit chit|a thin card with a glowing strip and scratched corners
mask|rain mask|a sealed face mask with glowing filter rings
boots|light-up boots|chunky boots with glowing soles and metal buckles
eye|cyber eye|a loose mechanical eye with a glowing iris on a tray
umbrella|neon umbrella|an umbrella with glowing ribs and a transparent canopy
phone|handset|a thin flexible handset with a cracked, glowing screen
deck_case|equipment case|a battered hard case with stickers and a glowing lock""",
VEH="""hovercar|hover car|a low sleek car floating on glowing thrusters with tinted glass and neon underlights
bike|motorcycle|a wide-tyred motorcycle with glowing rims, a low seat and a bright headlamp
cab|hover cab|a boxy yellow flying cab with a roof light and scratched panels
drone_truck|cargo drone|a huge flat drone carrying a stack of crates with four big rotors
tram|tram|a narrow elevated tram with lit windows gliding between towers
scooter|scooter|a small scooter with a delivery box on the back and a blinking tail light
van|armoured van|a grey armoured van with a roof camera and thick tyres
walker|police walker|a two-legged police machine with a spotlight and a loudspeaker""",
VSET="a rain-soaked street between towers; an elevated highway at night; a crowded neon avenue; a cargo dock at night; a rooftop landing pad; a tunnel of glowing signs",
POSE="standing under a flickering sign; walking quickly with the head down; leaning on a wall and watching the street; hunched over a glowing device; looking up at the towers; sitting on a crate with a drink; running through the rain; talking quietly with a hand over the mouth; holding a glowing object up to the light; waiting under an awning",
SHOT="in a wide shot with the figure small in the street; in a full-length view; in a medium portrait; from a low angle; over the shoulder; in a close portrait with the street glowing behind",
MOOD="with a tense mood; with a lonely mood; with a restless, busy mood; with a cool, hopeless mood; with a stylish, confident mood; with a hushed, uneasy mood",
LIGHT="lit by pink and cyan neon; lit by a flickering sign; lit by cold screen glow; lit by amber street lamps; lit by rain-blurred headlights; lit by red warning lights")

SP = dict(noun='steampunk', pre='sp',
STYLES="""brass_gaslamp|brass and gaslamp|brass fittings, leather, gas lamps, riveted panels and polished wood|warm gold gaslight with soft smoke|a coiled pipe along the wall
airship_age|airship age|great balloons, rope rigging, propellers, canvas and brass gondolas in bright clouds|bright cloudy daylight with sun glints|a flag snapping in the wind
clockwork|clockwork|visible gears, springs, tiny cogs, brass dials and wind-up figures|warm lamplight on copper|a drawer full of spare cogs
industrial_smog|industrial smog|tall chimneys, smoke, iron bridges, soot-stained brick and heavy machinery|grey-brown light through smoke|a belching chimney stack
victorian_explorer|Victorian explorer|pith helmets, maps, specimen jars, steam wagons and a faraway jungle edge|hot yellow light through green leaves|a tent with brass lamps
aether_lab|aether laboratory|glass tubes of glowing liquid, coils, sparks, copper dials and handwritten formulas|green and amber glow with white sparks|a crackling coil
gentleman_adventurer|gentleman adventurer|waistcoats, top hats, canes, brass gadgets and cosy club rooms|golden light from a fireplace|a map pinned to a wall
steam_city|steam city|brick towers, pipe networks, elevated rails, steam jets and gas-lit streets|warm lamps in a misty evening|a train crossing a high viaduct""",
CLASS="""inventor|inventor|a stained leather apron, goggles pushed up on the head and rolled sleeves|a wrench and a half-built gadget
captain|airship captain|a long coat with brass buttons, a peaked cap and a brass telescope|a ship's wheel under one hand
aeronaut|aeronaut|a leather flying helmet, goggles, a scarf and a harness with many buckles|a brass compass on a chain
mechanic|mechanic|oil-stained overalls, thick gloves and a belt of tools|a heavy spanner
scientist|lady scientist|a high-collared dress with a utility belt, magnifying goggles and gloves|a glass flask of glowing liquid
detective|detective|a long coat, a deerstalker-style cap and a magnifying glass|a brass pipe
automaton|automaton|a polished brass body with visible gears, a faceplate with painted eyes and a keyhole in the back|a small winding key
adventurer|gentleman adventurer|a tweed waistcoat, a top hat with goggles and polished boots|a cane with a brass knob
mad_scientist|eccentric professor|wild hair, a stained lab coat, thick goggles and sparking gloves|a bubbling flask
tinker|tinker|a patched coat hung with tools, a pack of parts and a battered hat|a tiny clockwork bird
engineer|train engineer|a soot-streaked cap, a leather vest and goggles round the neck|a long oil can
spy|spy|a dark cloak, a half mask and a coat with hidden pockets|a brass pocket device
pirate|sky pirate|a patched captain's coat, a feathered hat, a brass eye piece and a cutlass|a clockwork parrot
nurse|field nurse|a white apron, a pinned cap and a brass mechanical arm|a leather medical bag
clockmaker|clockmaker|a waistcoat, rolled sleeves, a jeweller's loupe and fine tools|a pocket watch with open gears
conductor|conductor|a dark uniform with brass buttons, a peaked cap and a whistle|a punch and a lantern
duellist|duellist|a fitted coat, a lace cravat and a long rapier with a gear guard|a brass pistol
courier|courier|a short cloak, a flat cap and a satchel of letters|a rolled scroll tube""",
LOC="""airship_dock|airship dock|a high wooden dock where huge airships are moored, with crates, ropes and cranes
workshop|inventor's workshop|a cluttered workshop of half-built machines, a forge, hanging tools and a high window
observatory|observatory|a round room with a huge brass telescope, star charts and a rolling ladder
train_station|steam train station|an iron-framed hall with a hissing locomotive, a big clock and travellers
factory_floor|factory floor|rows of pistons, belts, gears and workers beneath smoky skylights
library|library|tall shelves, rolling ladders, a globe and green-shaded lamps
clock_tower|clock tower interior|giant gears turning slowly behind a vast glass clock face
salon|salon|a plush room with velvet chairs, a brass gramophone and a tea tray
laboratory|laboratory|glass tubes, coils, sparks, shelves of jars and a bubbling vat
cobbled_street|cobbled street|gas lamps, brick buildings, a steam cab and drifting fog
market|market|a noisy covered market of brass gadgets, spice stalls and clockwork toys
mine|mine|timber supports, rails, a steam drill and hanging lamps
balloon_deck|airship deck|a wooden deck with rigging, a spinning propeller and a view of clouds
ironworks|ironworks|a glowing forge, molten metal, hammers and a huge steam hammer
greenhouse|glass greenhouse|an iron-framed glass hall of exotic plants, brass watering tools and mist
ballroom|ballroom|a polished floor, crystal lamps, a clockwork orchestra and dancers
canal|canal wharf|narrow boats, a steam crane, brick warehouses and gas lamps on the water
bridge|iron bridge|riveted iron arches over a smoky river with a train crossing
rooftops|rooftops|chimney pots, pipes, an airship overhead and the lights of the city
museum|museum hall|glass cases of brass curiosities, a skeleton of a beast and marble floors
dock|submarine dock|a wet dock with a riveted brass submarine, chains and lamps
cafe|coffee house|a wood-panelled room with copper urns, newspapers and round tables
tunnel|tunnel|a brick tunnel with steam pipes along the wall and a distant lamp
courtyard|palace courtyard|a stone courtyard with a brass fountain, mechanical birds and gas lamps""",
ITEM="""goggles|brass goggles|round goggles with tinted lenses, leather straps and tiny dials
watch|gear pocket watch|a pocket watch with an open back showing turning gears and a gold chain
arm|mechanical arm|a brass arm with visible gears, pistons and articulated fingers
raygun|brass ray gun|a chunky brass pistol with coils, a glass chamber and a glowing tip
engine|small steam engine|a tiny brass steam engine with a flywheel, a pressure gauge and a chimney
bird|clockwork bird|a small brass bird with feather plates, a key in its back and tiny glass eyes
telescope|telescope|a long brass telescope on a wooden tripod with engraved scales
gauntlet|gauntlet|a leather and brass glove with small gears across the knuckles
compass|compass|a heavy brass compass with a glass dome and strange extra dials
jetpack|steam jetpack|a metal backpack with twin pipes, a pressure dial and leather straps
lantern|brass lantern|a glass-fronted lantern with a gear-driven shutter
gramophone|gramophone|a wooden gramophone with a huge brass horn
key|winding key|a large brass key with a decorative bow and tiny cogs
hat|top hat|a tall top hat with goggles, a gear badge and a feather
umbrella|brass umbrella|an umbrella with a brass handle and a hidden spyglass
typewriter|brass typewriter|a typewriter with exposed gears, brass keys and a glass-covered mechanism
cane|gadget cane|a wooden cane with a brass head that opens to show tiny tools
box|puzzle box|a wooden box with brass inlay, small dials and hidden drawers""",
VEH="""airship|airship|a huge cigar-shaped balloon with a wooden gondola, fins, propellers and a rope ladder
steam_car|steam car|a high-wheeled brass and wood car with a boiler, a tall funnel and a bench seat
locomotive|locomotive|a black and brass locomotive with a tall funnel, big wheels and a bright headlamp
walker|steam walker|a big four-legged machine with a boiler, hissing pistons and a canopy
submarine|submarine|a riveted brass submarine with round portholes, a periscope and a screw at the back
ornithopter|ornithopter|a wooden flying machine with flapping canvas wings, gears and a pilot seat
penny_farthing|high-wheeled bicycle|a tall bicycle with a huge front wheel, a tiny rear wheel and brass lamps
tram|steam tram|a long tram with brass fittings, a bell and a chimney on a rail
riverboat|paddle steamer|a wide paddle steamer with two tall chimneys, paddles and a lit deck
crawler|crawler tractor|a heavy tracked machine with a brass boiler and a plough blade""",
VSET="a smoky industrial riverside; a cobbled street in fog; a busy airship dock; a green valley with a river; a bank of low cloud; a brick railway cutting",
POSE="holding up a brass device to the light; adjusting a dial with a small tool; looking through a telescope; leaning over a workbench; walking along a deck with a hand on a rail; checking a pocket watch; pouring tea from a brass pot; reading a map unrolled on a table; tightening a bolt with a wrench; standing with arms folded and a thoughtful look",
SHOT="in a wide shot with the figure small in the machinery; in a full-length view; in a medium portrait; from a low angle; over the shoulder; in a close portrait with the workshop softly behind",
MOOD="with a curious mood; with a proud, inventive mood; with an adventurous mood; with a cosy mood; with a busy mood; with a dramatic mood",
LIGHT="lit by warm gaslight; lit by the glow of a furnace; lit by sunlight through smoky glass; lit by green laboratory glow; lit by lamplight on brass; lit by cold morning light")

WE = dict(noun='western', pre='we',
STYLES="""classic|classic western|wide skies, red rock buttes, plain wooden buildings and heroic riders|clear hard sun with long shadows|a lone rider far away
sunbaked|sun-baked desperado|squinting faces, dust, flies, tight close-ups and hot bleached colour|blinding midday sun with deep hat shadow|a vulture circling high
frontier_real|frontier realism|mud, plain clothes, simple farms, weathered faces and a muted palette|soft overcast light|a pair of muddy boots by a door
ghost_town|ghost town|empty streets, sagging porches, swinging signs, drifting dust and broken windows|low gold evening light|a tumbleweed rolling past
gold_rush|gold rush|stream-side camps, panning pans, tents, shovels and mud-spattered prospectors|bright light on water and mud|a sluice box in a creek
ranch_life|ranch life|corrals, cattle, hay bales, campfires and horse tack|warm morning light with dust haze|a windmill turning slowly
sunset_epic|sunset epic|huge red-orange skies, silhouettes on a ridge and a long line of riders|saturated sunset glow|a wagon train in silhouette
revisionist|gritty revisionist|rain-soaked streets, tired faces, shabby saloons and muted brown tones|grey rain light|a lantern swinging in the wind""",
CLASS="""sheriff|sheriff|a dusty vest with a star badge, a wide hat and a gun belt|a lever-action rifle
outlaw|outlaw|a bandana over the face, a long duster coat and spurs|a pair of revolvers
gunslinger|gunslinger|a black hat, a leather vest, a bolo tie and a low-slung holster|a silver revolver
saloon_owner|saloon owner|a fine waistcoat, a pocket watch chain and sleeve garters|a bottle and a glass
rancher|rancher|a sun-faded hat, a work shirt, chaps and a kerchief|a coiled rope
cowhand|cowhand|a battered hat, leather chaps, spurs and a kerchief|a lasso
bounty_hunter|bounty hunter|a long coat, a low hat and a rifle across the back|a folded wanted poster
prospector|prospector|a floppy hat, a ragged beard and a pack of tools|a mining pan and a pick
preacher|preacher|a black coat, a wide-brimmed black hat and a white collar|a worn book
doctor|town doctor|a dark suit, a vest and a leather bag|a stethoscope and a bottle
teacher|schoolteacher|a high-necked dress, a bonnet and a small bag of books|a bell
blacksmith|blacksmith|a leather apron, bare muscled forearms and a soot-streaked face|a hammer and tongs
driver|stagecoach driver|a dusty coat, a goggle-like pair of glasses and long reins|a whip
gambler|gambler|a neat waistcoat, a string tie and a flat hat|a fan of cards
railroad|railroad worker|a striped cap, work clothes and a lantern|a heavy mallet
rider|horse rider|a hat, a bandana, a poncho and a saddle with bedroll|a rifle in a saddle scabbard
singer|saloon singer|a bright satin dress with feathers and gloves|a feather fan
farmer|homesteader|a plain work shirt, suspenders and a straw hat|a pitchfork""",
LOC="""main_street|main street|a wide dirt street lined with plank buildings, hitching rails and a water trough
saloon|saloon|a long bar, swinging doors, a piano, spittoons and a smoky haze
jail|jailhouse|a small plank office with a cell, a desk, a rifle rack and a lantern
general_store|general store|shelves of tins and sacks, a pot-bellied stove and a counter
canyon|canyon|red rock walls, a dry riverbed and a narrow trail
desert_trail|desert trail|scrub, a cactus, cracked earth and a far line of mesas
station|railway station|a plank platform, a water tower and a steam train waiting
mine_entrance|mine entrance|a timber frame in a rock face, ore carts and a rail track
ranch|ranch yard|a wooden house, a barn, a corral and a windmill
church|frontier church|a small white wooden church with a bell tower and plain benches
homestead|homestead|a sod cabin, a plough, a well and a vegetable patch
river_crossing|river crossing|a shallow river with a wooden ferry and wagons waiting
ghost_town|ghost town street|leaning buildings, broken signs, drifting dust and a creaking door
camp|night camp|a campfire, bedrolls, a coffee pot and horses tied nearby
rodeo|rodeo ring|a dusty arena, a wooden chute and watching crowds
coach_stop|stagecoach stop|a station house, a corral of horses and a hitched coach
cattle_drive|cattle drive|a long herd on open grassland with riders at each side
bank|bank|a plank building with barred windows, a heavy vault door and a brass counter
barber|barber shop|a leather chair, a mirror, bottles and a striped pole
livery|livery stable|stalls, hay, tack on the walls and a farrier's bench
hotel|frontier hotel|a creaking staircase, a plain lobby and a bell on the desk
cemetery|hill cemetery|wooden crosses on a windy rise and a lone tree
bridge|rope bridge|a rope and plank bridge over a deep gorge
water_tower|water tower|a wooden tower beside the tracks with a long spout""",
ITEM="""revolver|revolver|a long-barrelled revolver with a wooden grip and a worn finish
hat|cowboy hat|a sweat-stained wide-brimmed hat with a leather band
saddle|saddle|a worn leather saddle with silver studs and a rolled blanket
lasso|lasso|a coiled rope with a neat loop and a frayed end
poster|wanted poster|a creased paper poster with a sketched face, the word "WANTED" and a reward
badge|star badge|a tarnished silver star pinned to a vest
spurs|spurs|a pair of worn spurs with big rowels and leather straps
coffee|camp coffee pot|a blackened tin pot with a bent handle over embers
lantern|lantern|a rusty oil lantern with a bent handle
rifle|rifle|a lever-action rifle with a scratched wooden stock
bedroll|bedroll|a rolled blanket tied with rope and a tin cup
boots|boots|dusty boots with worn heels and a stitched pattern
holster|gun belt|a worn leather belt with a holster and loops of cartridges
pan|gold pan|a dented metal pan holding gravel and a few flecks of gold
cards|card hand|five worn playing cards fanned on a wooden table
telegram|telegram|a folded slip of paper with typed words and a stamped mark
whiskey|whiskey bottle|a dusty bottle with a faded label and a cork
sign|saloon sign|a hanging wooden sign with painted letters reading "SALOON" """,
VEH="""stagecoach|stagecoach|a painted wooden coach with big wheels, leather straps and a team of horses
wagon|covered wagon|a canvas-topped wagon with wooden wheels, a bucket on the side and oxen
locomotive|locomotive|a black steam locomotive with a diamond stack, a cowcatcher and a bell
buckboard|buckboard|a small open wagon with a bench seat, drawn by a single horse
horse|saddled horse|a dusty horse with a worn saddle, a bedroll and a rifle scabbard
handcar|rail handcar|a small hand-pumped rail cart with two men
steamboat|riverboat|a white paddle steamer with two tall chimneys and a red paddle wheel
herd|cattle herd|a wide herd of longhorn cattle moving over open ground""",
VSET="a dusty main street; a wide desert plain; a shallow river crossing; a canyon trail; open grassland; the edge of a town at dusk",
POSE="standing tall with the weight on one leg; walking slowly down the street; leaning on a post with the hat tilted; riding at a steady walk; squatting by a small fire; staring across the empty street; sitting on a porch with a cup; looking up at the sun; tying a horse to a rail; checking the ground for tracks",
SHOT="in a wide shot with the figure small in the landscape; in a full-length view; in a medium portrait; from a low angle; over the shoulder; in an extreme close-up of the eyes under a hat",
MOOD="with a tense, quiet mood; with a lonely mood; with a hot, weary mood; with a proud mood; with a dusty, calm mood; with a grim mood",
LIGHT="lit by a hard noon sun; lit by low gold evening sun; lit by campfire glow; lit by a swinging lantern; lit by grey rain light; lit by red sunset")
GENRES = [CY, SP, WE]
def one(g):
    pre = g['pre']; n = g['noun']; G = {}
    for k in ('POSE', 'SHOT', 'MOOD', 'LIGHT'): G['%s_%s' % (pre, k.lower())] = P(g[k])
    sk = []; ck = []; lk = []; ik = []; vk = []
    for k, label, look, light, detail in rows(g['STYLES']):
        G['%s_style_%s_prompt' % (pre, k)] = ['A %s scene in the %s manner, with %s. The place is __%s_loc_look__. In it is __%s_class_look__, __%s_pose__. The scene has %s. Also in view is %s. It is shown __%s_shot__, __%s_mood__.' % (n, label, look, pre, pre, pre, light, detail, pre, pre)]
        G['%s_style_%s_scene' % (pre, k)] = ['A %s scene in the %s manner, with %s. The place is __%s_loc_look__. The scene has %s. Also in view is %s. It is shown __%s_shot__, __%s_mood__.' % (n, label, look, pre, light, detail, pre, pre)]
        sk.append(k)
    for k, label, outfit, gear in rows(g['CLASS']):
        G['%s_class_%s_look' % (pre, k)] = ['%s %s in %s, with %s' % (A(label), label, outfit, gear)]
        G['%s_class_%s_prompt' % (pre, k)] = ['The subject is __%s_class_%s_look__. They are __%s_pose__. The place is __%s_loc_look__. It is shown __%s_shot__, __%s_light__, __%s_mood__.' % (pre, k, pre, pre, pre, pre, pre)]
        G['%s_class_%s_short' % (pre, k)] = ['__%s_class_%s_look__.' % (pre, k)]
        ck.append(k)
    for k, label, look in rows(g['LOC']):
        G['%s_loc_%s_look' % (pre, k)] = ['%s %s, %s' % (A(label), label, look)]
        G['%s_loc_%s_prompt' % (pre, k)] = ['A %s scene set in __%s_loc_%s_look__. In the foreground is __%s_class_look__, __%s_pose__. It is shown __%s_shot__, __%s_light__, __%s_mood__.' % (n, pre, k, pre, pre, pre, pre, pre)]
        G['%s_loc_%s_empty' % (pre, k)] = ['A %s scene with no people in it, set in __%s_loc_%s_look__. It is shown __%s_shot__, __%s_light__, __%s_mood__.' % (n, pre, k, pre, pre, pre)]
        G['%s_loc_%s_short' % (pre, k)] = ['__%s_loc_%s_look__.' % (pre, k)]
        lk.append(k)
    for k, label, look in rows(g['ITEM']):
        G['%s_item_%s_look' % (pre, k)] = ['%s %s, %s' % (A(label), label, look)]
        G['%s_item_%s_prompt' % (pre, k)] = ['A close view of __%s_item_%s_look__, resting on __%s_rest__ and %s.' % (pre, k, pre, '__%s_light__' % pre)]
        G['%s_item_%s_short' % (pre, k)] = ['__%s_item_%s_look__.' % (pre, k)]
        ik.append(k)
    for k, label, look in rows(g['VEH']):
        G['%s_veh_%s_look' % (pre, k)] = ['%s %s, %s' % (A(label), label, look)]
        G['%s_veh_%s_prompt' % (pre, k)] = ['The subject is __%s_veh_%s_look__. Its surroundings are __%s_vset__. It is shown __%s_shot__, __%s_light__, __%s_mood__.' % (pre, k, pre, pre, pre, pre)]
        G['%s_veh_%s_short' % (pre, k)] = ['__%s_veh_%s_look__.' % (pre, k)]
        vk.append(k)
    G['%s_vset' % pre] = P(g['VSET'])
    G['%s_rest' % pre] = P("a worn wooden table; a dark workbench; a pale cloth; a crate; a metal tray; a stone ledge; a folded coat; a stack of papers")
    for p, ks in (('style', sk), ('class', ck), ('loc', lk), ('item', ik), ('veh', vk)):
        for suf in ('look', 'prompt', 'short', 'scene', 'empty'):
            names = [x for x in ('%s_%s_%s_%s' % (pre, p, k, suf) for k in ks) if x in G]
            if names: G['%s_%s_%s' % (pre, p, suf)] = ['__%s__' % x for x in names]
    G['%s_prompt' % pre] = ['__%s_style_prompt__' % pre, '__%s_class_prompt__' % pre, '__%s_loc_prompt__' % pre, '__%s_item_prompt__' % pre, '__%s_veh_prompt__' % pre]
    G['%s_pair_prompt' % pre] = ['Two characters face each other. On the left is __%s_class_look__. On the right is __%s_class_look__. The place is __%s_loc_look__. It is shown __%s_light__, __%s_mood__.' % ((pre,) * 5)]
    G['%s_group_prompt' % pre] = ['A small group stands together. On the left is __%s_class_look__. Next is __%s_class_look__. In the middle is __%s_class_look__. Then __%s_class_look__. On the right is __%s_class_look__. The place is __%s_loc_look__. It is shown __%s_shot__, __%s_mood__.' % ((pre,) * 8)]
    G['%s_entry' % pre] = ['%s_prompt' % pre, '%s_style_prompt' % pre, '%s_class_prompt' % pre, '%s_loc_prompt' % pre, '%s_loc_empty' % pre, '%s_item_prompt' % pre, '%s_veh_prompt' % pre, '%s_pair_prompt' % pre, '%s_group_prompt' % pre]
    return G
def build(final=None):
    G = {}; ep = []
    for g in GENRES:
        x = one(g); ep += x.pop('%s_entry' % g['pre']); G.update(x)
    G['v78_genre_entry_points'] = ep
    return G
if __name__ == '__main__': print(len(build()))
