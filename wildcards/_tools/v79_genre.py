"""v79 stage A - film noir (nr_), pirates (pt_) and spies (sy_): same layout as the v78 genres, looks only, shared pools per genre."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from famlib import P
import v78_genre as G78

NR = dict(noun='film noir', pre='nr',
SLOC="""classic_noir|office police_station apartment library
rain_street|rain_alley tram_stop alley_stairs bridge
smoke_room|casino bar nightclub warehouse
femme_fatale|nightclub hotel_lobby mansion bar
neo_noir|diner parking_garage rooftop cinema
stairwell|alley_stairs apartment hotel_lobby mansion
docks_fog|pier warehouse bridge
penthouse|mansion rooftop library""",
STYLES="""classic_noir|classic black-and-white noir|hard shadows, venetian blind stripes, cigarette smoke and wet pavement|a single hard lamp throwing sharp slats of shadow|a ringing black telephone
rain_street|rainy city street|slick black pavement, glowing shopfronts, trench coats and a rain-soaked night|streetlight halos in the drizzle|a pair of headlights approaching through the rain
smoke_room|smoky back room|haze hanging under a bare bulb, a card table, whisky glasses and tall shadows|a swinging bare bulb in thick smoke|a full ashtray on a green table
femme_fatale|femme fatale|a long satin gown, long gloves, a cigarette holder and a hooded gaze in a dim doorway|a soft key light and a deep shadow behind|a pair of gloves on a bar top
neo_noir|colour neo-noir|saturated neon reds and greens, glass towers and wet streets after midnight|red and green neon spilling over faces|a flickering motel sign reading "VACANCY"
stairwell|stairwell and corridor|a narrow stair, patterned wallpaper, a door with frosted glass and a long shadow|a hall light casting a stripe across the floor|a name painted on frosted glass reading "M. HALE, INVESTIGATIONS"
docks_fog|foggy docks|thick fog, wet planks, crates and a single lamp at the end of a pier|a pale lamp glow in fog|a coil of rope on a post
penthouse|penthouse night|a window wall over the city, a long bar, polished floors and a lone figure|a city glow through tall windows|a decanter on a glass table""",
CLASS="""detective|private detective|a rumpled trench coat, a fedora tilted low and a loosened tie|a battered notebook and a dented lighter
femme|femme fatale|a satin dress, a fur stole, red lipstick and a pinned-up wave of hair|a slim cigarette in a long holder
cop|city cop|a heavy overcoat, a brimmed cap and a badge on the belt|a flashlight and a notepad
reporter|crime reporter|a rumpled suit, a hat with a press card tucked in the band|a folded newspaper and a pencil behind the ear
gangster|crime boss|a wide-shouldered pinstripe suit, a white scarf and a diamond tie pin|a cigar and a ring on every finger
singer|nightclub singer|a sequined evening gown, long gloves and a flower in the hair|a standing microphone
barman|barman|a white shirt, a black waistcoat and rolled sleeves|a cloth over the shoulder and a shaker
informant|informant|a threadbare coat, a turned-up collar and a nervous squint|a folded envelope in a hand
widow|widow in black|a black veil, a fitted black coat and a small handbag|a white handkerchief
doctor|night doctor|a crumpled white coat under an overcoat and a leather bag|a stethoscope around the neck
lawyer|lawyer|a sharp grey suit, a briefcase and round glasses|a thick folder tied with string
bodyguard|bodyguard|a broad dark suit, a flat nose and a wary stare|a hand held near a jacket button
cabbie|taxi driver|a flat cap, a scarf and fingerless gloves|a thermos and a folded map
photographer|press photographer|a trench coat, a hat with a card in the band and a big flash camera|a satchel of flash bulbs
fixer|fixer|a camel coat, a hat pulled low and a thin moustache|a notebook of names
hotel_clerk|hotel clerk|a buttoned jacket, a tidy parting and a bell on the desk|a key on a heavy brass tag""",
LOC="""office|detective office|a frosted glass door with painted lettering reading "M. HALE, INVESTIGATIONS", a desk, a hat stand and blinds throwing stripes
rain_alley|rain-soaked alley|dripping fire escapes, puddles, a single lamp and a dumpster
nightclub|nightclub|small round tables, a stage with a microphone, a smoky haze and a spotlight
diner|all-night diner|a long counter, a neon sign in the window reading "EAT", chrome stools and a cup of coffee
hotel_lobby|hotel lobby|a worn carpet, a brass bell on a desk, potted palms and a revolving door
rooftop|rooftop|a water tower, chimney pots, a steel railing and a city glow
train_station|train station|a vast hall of steam, a big clock, a row of benches and a hurrying crowd
pier|fog-bound pier|wet planks, bollards, a lamp in the fog and the sound of water
police_station|police station|a scuffed desk, a green lamp, a wall of notices and a line of chairs
casino|back-room casino|a roulette wheel, green felt, cigar smoke and men in dark suits
bar|corner bar|a long wooden counter, a mirror behind the bottles and a flickering sign reading "COCKTAILS"
morgue|city morgue|white tile, steel drawers, a bare bulb and a clipboard
apartment|small apartment|a sagging bed, a window with a flashing sign outside reading "HOTEL" and a rotary phone
library|private library|tall shelves, a rolling ladder, a leather chair and a dim lamp
bridge|iron bridge|riveted girders, a passing train, wet planks and a lone lamp
alley_stairs|back stairs|steep concrete steps between buildings, a rusty rail and a lamp at the bottom
parking_garage|parking garage|concrete pillars, parked cars, buzzing strip lights and echoing steps
newsroom|newsroom|rows of typewriters, a haze of smoke, ringing phones and a glass-walled editor's office
mansion|mansion hall|a sweeping staircase, a grandfather clock, a marble floor and a dead fireplace
tram_stop|tram stop|a shelter in the rain, a wet timetable and a distant bell
cinema|old cinema|a tilted marquee with glowing bulbs reading "NOW SHOWING", a ticket booth and a long red-lit foyer
warehouse|warehouse|stacked crates, a hanging bulb, a rolling door and long shadows""",
ITEM="""fedora|fedora|a grey felt hat with a dark band and a crease worn into the crown
revolver|revolver|a snub-nosed revolver with worn grips resting on a folded cloth
lighter|lighter|a dented steel lighter with a small flame and a scratched engraving
phone|black telephone|a heavy black rotary telephone with a coiled cord
typewriter|typewriter|a battered typewriter with a half-typed page and a smudged ribbon
whisky|whisky glass|a short glass of amber whisky with a bottle beside it and a ring on the wood
cigarette|cigarette|a cigarette burning in a glass ashtray, a curl of smoke rising
photo|photograph|a creased black-and-white photograph with a torn corner
key|brass key|a small brass key on a heavy tag marked "ROOM 9"
letter|letter|a folded letter with a smear of red lipstick, a few lines of handwriting and an unopened envelope
matchbook|matchbook|a matchbook from a club, with the words "THE BLUE ROOM" printed on the cover
newspaper|newspaper|a folded newspaper with a headline reading "BODY FOUND" and a coffee ring
blinds|window blinds|slatted blinds throwing stripes of light across a desk
case|briefcase|a scuffed leather case with brass catches and a heavy bulge
gloves|gloves|a pair of long black gloves lying on a bar top beside a purse
badge|badge|a dull metal badge and a leather wallet with a worn card
lamp|desk lamp|a green-shaded desk lamp with a pool of light on a blotter""",
VEH="""sedan|black sedan|a long black sedan with round fenders, whitewall tyres and a chrome grille
taxi|taxi|a checkered cab with a lit roof sign reading "TAXI", round headlamps and wet tyres
police_car|police car|a black and white patrol car with a roof light and a spotlight on the door
convertible|convertible|a long cream convertible with the top down and a spare wheel on the back
tram|tram|a green streetcar with lit windows, a pole on the roof and wet rails
train|night train|a dark steam train with lit windows and a plume of smoke
delivery|delivery van|a boxy van with the painted name "LUNN & SONS" on the side and a dented fender
motorbike|motorcycle|a heavy black motorcycle with a leather saddle and a sidecar""",
VSET="a rain-soaked city street; a dark alley with a single lamp; a foggy waterfront; a wet bridge at night; the front of a hotel with a lit sign; a deserted road under a streetlight",
POSE="standing with a cigarette; walking slowly with the collar turned up; leaning on a wall and watching; sitting with a glass in hand; looking out of a window; waiting with the hat tilted low; holding a telephone and staring; checking a watch",
SHOT="in a wide shot with the figure small in the street; in a full-length view; in a medium portrait; from a low angle; over the shoulder; in a close portrait with the shadows falling across the face",
MOOD="with a tense, hushed mood; with a lonely mood; with a weary, cynical mood; with a seductive, dangerous mood; with a cold, hopeless mood; with a nervous, watchful mood",
LIGHT="lit by one hard lamp; lit by stripes of light through blinds; lit by flickering neon; lit by a bare bulb in smoke; lit by dim warm light with deep shadows; lit by cold pale light")

PT = dict(noun='pirate', pre='pt',
SLOC="""golden_age|deck dock crows_nest bay
storm_deck|deck crows_nest hold gun_deck
tavern_night|tavern market prison
treasure_isle|beach treasure_cave jungle_path
ghost_ship|ghost_wreck bay hold
naval_battle|deck gun_deck crows_nest
cove_hideout|treasure_cave swamp bay treasure_room
port_town|market dock shipyard tavern""",
STYLES="""golden_age|golden age of piracy|tricorn hats, billowing sails, tarred rope, brass cannons and a bright sea|warm sun on white sails and blue water|a black flag snapping above
storm_deck|storm at sea|a heaving deck, towering grey waves, flying spray and straining rigging|a flash of lightning on black clouds|a sailor clinging to a mast
tavern_night|harbour tavern|low beams, barrels, candle stubs, clay mugs and rough laughter|warm candle glow with deep shadows|a map pinned to a table with a dagger
treasure_isle|treasure island|white sand, palm trees, a battered chest half buried and a turquoise lagoon|bright noon sun and sharp shadows|an old map with a red cross
ghost_ship|ghost ship|torn sails, green mist, slimy planks and a pale glow under the water|cold green moonlight on a still sea|a lantern swinging by itself
naval_battle|sea battle|clouds of cannon smoke, splintered masts, boarding ropes and shouting crews|orange flashes through grey smoke|a torn flag falling
cove_hideout|smuggler's cove|a sea cave, hanging lanterns, stacked barrels and a hidden jetty|lantern glow on wet rock|a rope ladder up the cliff
port_town|pirate port town|crooked wooden houses, crowded docks, parrots, market stalls and washing lines|hot afternoon sun with long shadows|a stall of stolen goods""",
CLASS="""captain|pirate captain|a long red coat with brass buttons, a feathered tricorn hat and tall boots|a curved cutlass and a spyglass
first_mate|first mate|a striped shirt, a sash, a short jacket and a coil of rope over the shoulder|a brass whistle on a cord
gunner|gunner|a bare-armed rough shirt, a rag round the head and soot-black hands|a linstock and a powder horn
cook|ship's cook|a stained apron, rolled sleeves and a battered pot lid|a long ladle and a sack of beans
navigator|navigator|a blue coat, a small hat and ink on the fingers|a brass sextant and a rolled chart
lookout|lookout|a faded striped shirt, bare feet and a scarf round the head|a battered spyglass
swordswoman|swordswoman|a loose white shirt, a leather vest, a red sash and tall boots|a thin rapier
quartermaster|quartermaster|a sober dark coat, a ledger and a sensible hat|a ring of keys and a ledger
parrot_keeper|sailor with a parrot|a patched shirt, an eye patch and a gold hoop earring|a green parrot on the shoulder
surgeon|ship's surgeon|a stained waistcoat, a leather bag and round spectacles|a saw and a bottle of rum
privateer|privateer|a neat blue coat with gold braid and a powdered wig|a sealed letter with a ribbon
smuggler|smuggler|a dark hooded cloak, a dripping lantern and muddy boots|a small keg on the shoulder
innkeeper|innkeeper|a stained apron, thick forearms and a cloth over the shoulder|a tray of mugs
shipwright|shipwright|a canvas apron, a leather cap and a belt of tools|an adze and a mallet
deckhand|deckhand|a ragged striped shirt, patched trousers and bare feet|a bucket and a mop
treasure_hunter|treasure hunter|a dusty coat, a wide hat, a satchel and muddy boots|a folded map and a short spade""",
LOC="""deck|ship's deck|a scrubbed wooden deck, coiled ropes, tall masts and a ship's wheel
crows_nest|crow's nest|a small barrel high on the mast, a rope ladder and a wide sea below
captains_cabin|captain's cabin|a low cabin with stern windows, a chart table, a hanging lantern and a locked chest
gun_deck|gun deck|a low deck with a row of cannons, stacked shot and swinging lamps
hold|ship's hold|stacked barrels, hanging hammocks, dripping beams and dim lanterns
tavern|harbour tavern|a smoky low room with barrels, long tables, a fireplace and a stair to rooms above
dock|crowded dock|wooden jetties, stacked crates, nets, gulls and moored ships
treasure_cave|treasure cave|a sea cave with glittering piles, an old chest and dripping stone
beach|desert island beach|white sand, a few palms, a wrecked boat and a campfire
jungle_path|jungle path|dense green leaves, hanging vines, a muddy track and a rusty gate
cliff_fort|clifftop fort|stone walls, rusty cannons facing the sea and a flag on a pole
lighthouse|lighthouse|a stone tower on a rock, a spiral stair and a great lamp
market|port market|stalls of fruit, spices and stolen goods, parrots and haggling crowds
shipyard|shipyard|a ship's hull on timber supports, stacks of planks and steaming pitch
swamp|mangrove swamp|twisting roots, still brown water, hanging moss and a hidden boat
ghost_wreck|wrecked ship|a half-sunk hull, broken masts, seaweed and a green glow
prison|harbour prison|a damp stone cell, iron bars and a high small window
treasure_room|vault of treasure|piles of coins, jewelled cups and chests in a torchlit room
bay|moonlit bay|a calm bay with a single ship at anchor and a silver path on the water
gallows_hill|windy hill|a bare hill with a lone wooden frame, wind and a cold sky""",
ITEM="""cutlass|cutlass|a curved sword with a worn leather grip and a nicked blade
flag|black flag|a tattered black flag with a white skull and crossed bones
chest|treasure chest|an iron-banded wooden chest overflowing with gold coins and a string of pearls
map|treasure map|a stained parchment map with a coast, a dotted path and a red cross
spyglass|spyglass|a brass telescope with a leather wrap and a dented cap
compass|compass|a brass compass in a worn box with a trembling needle
pistol|flintlock pistol|a long-barrelled flintlock with a carved wooden grip and brass fittings
rum|rum bottle|a dark bottle with a cork, a clay mug and a ring of drops on the table
hat|tricorn hat|a battered black hat with a feather and a worn edge
bottle|message in a bottle|a green glass bottle with a rolled note, sealed with wax, in wet sand
anchor|anchor|a rusted anchor wrapped in chain and seaweed
cannon|cannon|a black iron cannon on a wooden carriage with a pile of round shot
coins|pieces of eight|a heap of worn silver coins stamped with crowns and crosses
wheel|ship's wheel|a wooden ship's wheel with polished handles and a worn rim
lantern|ship's lantern|a brass lantern with a glass panel and a flickering flame
journal|captain's log|a leather book with water-stained pages and the words "LOG OF THE SEA WOLF" on the cover
parrot|parrot perch|a bright parrot on a wooden perch with seed scattered below
hook|iron hook|a polished iron hook on a leather cuff beside a pair of dice""",
VEH="""galleon|galleon|a tall wooden ship with three masts, carved decoration, square sails and a black flag
sloop|sloop|a fast single-masted ship with a long bowsprit and patched sails
schooner|schooner|a slim two-masted ship with fore-and-aft sails and a low hull
frigate|frigate|a war ship with two rows of gun ports and a tall mast of grey sails
rowboat|rowboat|a small wooden boat with oars, a lantern and a pile of crates
longboat|longboat|a long boat with a dozen oarsmen and a lantern in the bow
ghost_galleon|ghost galleon|a ruined tall ship with torn black sails, a green glow and weed hanging from the hull
raft|raft|a lashed log raft with a ragged sail and a single barrel""",
VSET="a bright open sea; a stormy grey ocean; a moonlit bay; a rocky coast with white surf; a calm harbour at dawn; a fog bank at dusk",
POSE="standing with a hand on the hilt; striding with a hand on the belt; pointing into the distance; leaning on a barrel with a mug; crouching over a map; swinging on a rope; staring ahead through a spyglass; laughing with a cup raised",
SHOT="in a wide shot with the figure small on the deck; in a full-length view; in a medium portrait; from a low angle; over the shoulder; in a close portrait with the sea behind",
MOOD="with a bold, swaggering mood; with a wild, stormy mood; with a tense, hushed mood; with a merry, rowdy mood; with a greedy, scheming mood; with an adventurous, restless mood",
LIGHT="lit by warm lantern light; lit by hard bright light; lit by low gold light; lit by flashes of lightning; lit by cold moonlight; lit by candles and firelight")

SY = dict(noun='spy thriller', pre='sy',
SCREEN="""the lines \"FLIGHT 217\" and \"BOARDING\"; the lines \"TARGET LOCATED\" and \"STANDBY\"; the lines \"ACCESS DENIED\" and \"TRY AGAIN\"; the lines \"COUNTDOWN\" and \"00:04:59\"; the lines \"INCOMING CALL\" and \"UNKNOWN\"; the lines \"GATE 4\" and \"DELAYED\"; the lines \"TRANSMISSION 3 OF 5\" and \"RECEIVED\"; the lines \"SECTOR NINE\" and \"ALL CLEAR\"""",
SLOC="""cold_war|dead_drop safehouse_flat border old_town
glamour_spy|casino hotel_suite yacht opera
tech_spy|lab bunker mountain_lair
safehouse|safehouse_flat radio_room cafe
border_crossing|border car_park airport
embassy_gala|embassy opera hotel_suite
chase|rooftop_chase market old_town
undercover|market cafe museum old_town""",
STYLES="""cold_war|Cold War spy|grey streets, trench coats, a dead drop in a park and a nervous meeting in the snow|flat grey winter light|a coded note in a hollow coin
glamour_spy|glamorous agent|tuxedos, evening gowns, a casino table and a sports car outside a grand hotel|bright chandelier light and warm shadows|a martini with an olive
tech_spy|gadget spy|a hidden lab, a briefcase of gadgets, screens showing __sy_screen_text__, laser lines and sleek suits|cool blue screen light|a pen that is not a pen
safehouse|safehouse|a plain flat, drawn blinds, a radio, a suitcase and a pot of cold tea|a single lamp behind drawn curtains|a map with pins on the wall
border_crossing|border crossing|a striped barrier, a guard hut, floodlights, snow and a long queue of cars|harsh white floodlights|a stamped passport
embassy_gala|embassy gala|a ballroom of chandeliers, waiters with trays and guests in tuxedos and gowns|warm gold chandelier light|a folded note beneath a glass
chase|rooftop chase|clotheslines, tiled rooftops, a crowded market below and a figure leaping a gap|bright afternoon sun and sharp shadows|a flapping sheet on a line
undercover|undercover in a market|a crowded foreign market, awnings, spices, hidden watchers and a dropped newspaper|dappled sun through awnings|a briefcase left on a bench""",
CLASS="""field_agent|field agent|a slim dark suit, a loosened tie and a watch with a thick strap|a compact pistol in a shoulder holster
femme_agent|elegant agent|an evening gown with a high slit, long gloves and an elegant clutch|a lipstick that hides a tiny lens
handler|handler|a grey overcoat, a hat and a folded newspaper|a thermos and a small notebook
analyst|analyst|a rumpled cardigan, thick glasses and a stack of files|a magnifying glass and a mug
tech|gadget master|a lab coat, goggles on the forehead and pockets full of tools|a suitcase of strange devices
double_agent|double agent|a tidy suit, a polite smile and cufflinks that do not match|two passports hidden in a coat
courier|courier|a plain raincoat, a flat cap and a battered satchel|a sealed envelope taped under a tray
assassin|hired killer|a black coat, black gloves and a calm, empty gaze|a thin wire and a silenced weapon
diplomat|diplomat|a sash and a medal on a pressed formal coat|a leather folder with a seal
bodyguard|bodyguard|a big dark suit, an earpiece and sunglasses at night|a hand held close to the jacket
safecracker|safecracker|a dark sweater, soft shoes and a tool roll|a stethoscope round the neck
forger|forger|an ink-stained apron, a jeweller's loupe and steady hands|a stack of blank passports
radio_operator|radio operator|headphones, rolled sleeves and tired eyes|a suitcase radio with a key
villain|master villain|a high-collared jacket, a white cat on the lap and a scar across one eye|a remote control with a red button
informant|informant|a threadbare coat, a turned-up collar and a nervous squint|a folded note
chauffeur|chauffeur|a peaked cap, a dark uniform and gloves|a car key on a leather fob""",
LOC="""safehouse_flat|safehouse flat|a drab room with drawn blinds, a rotary phone, a suitcase and a pot of cold tea
dead_drop|park dead drop|a bench beside a path, a hollow tree and snow under bare branches
casino|casino|a baccarat table, chandeliers, tuxedos, gowns and rows of chips
hotel_suite|hotel suite|a grand room with a balcony, a minibar, a safe behind a painting and a city view
rooftop_chase|rooftop|tiled roofs, antennas, washing lines and a long drop to a crowded street
train|night train compartment|a narrow sleeping compartment, a rattling window, a small lamp and a locked case
lab|secret lab|white benches, odd devices, a wall of screens showing __sy_screen_text__ and a locked metal door
embassy|embassy ballroom|chandeliers, a polished floor, flags and waiters weaving between guests
border|border post|a striped barrier, a guard hut, floodlights and a long queue
bunker|command bunker|a concrete room, a huge wall map, banks of phones and hard fluorescent light
cafe|street cafe|small round tables, a striped awning, a newspaper left on a chair and a watcher across the street
airport|airport hall|a vast hall, a departure board showing __sy_screen_text__, a row of plastic seats and a locked locker
mountain_lair|mountain lair|a cavern of steel, a glowing control room with screens showing __sy_screen_text__, a monorail and a vast domed ceiling
yacht|luxury yacht|a white deck, a bar with stools, a spiral stair and a blue sea
market|foreign market|awnings, crowded stalls, hanging lamps and a dropped newspaper
museum|museum gallery|cases of treasure, laser lines across the floor and a sleeping guard
car_park|underground car park|concrete pillars, buzzing lights, a parked sedan and echoing steps
opera|opera house|a plush red auditorium, a gilded balcony, a stage in light and a figure in a box
alpine|alpine chalet|a wooden chalet, a snowy slope, a cable car and a glass lounge
radio_room|radio room|a cramped room of dials, a bank of headphones, a desk lamp and a coded pad with the lines "7419" and "2836"
old_town|old town alley|narrow cobbles, a lit window, a tram bell and a figure in a doorway
pier|harbour pier|crates, cranes, a waiting boat and a pale light on the water""",
ITEM="""pistol|silenced pistol|a compact pistol with a long silencer lying on a folded handkerchief
briefcase|briefcase|a silver briefcase with two combination locks and a sheet of foam inside
passport|passport|a worn passport stamped many times, with a photograph and the name "J. MARLOW" written in blue ink
microfilm|microfilm|a tiny roll of film in a small metal case beside a magnifying glass
radio|suitcase radio|a leather suitcase opened to show dials, a key and a pair of headphones
camera|miniature camera|a tiny camera hidden in a lighter, with a roll of film beside it
cipher|code book|a notebook with the lines "KXQ 4417" and "ZVM 0922" written in a neat hand, a pencil and a strip of paper with a pattern
watch|gadget watch|a heavy wristwatch with an extra dial and a tiny blade on the strap
umbrella|umbrella|a black umbrella with a pointed tip and a strangely heavy handle
dossier|dossier|a thick folder stamped "TOP SECRET" with a photograph clipped inside
map|map|a city map with red circles, pins and the handwritten times "21:40" and "23:15"
pen|pen|a fountain pen with a tiny button and a small cap
envelope|envelope|an envelope sealed with wax and marked with the letter "K"
coin|hollow coin|a large coin split open to show a rolled slip of paper
cufflinks|cufflinks|gold cufflinks with a hidden catch and a small stone
phone|rotary phone|a black phone with a bug taped under the receiver
key|safe key|a small key on a chain with a number stamped on the head""",
VEH="""sports_car|sports car|a low silver sports car with a long bonnet and headlights hidden behind panels
sedan|black sedan|a dark long sedan with tinted windows and a plain plate
motorboat|speedboat|a sleek boat with a white wake and a hooded cockpit
helicopter|helicopter|a small dark helicopter with a bubble canopy and a long tail
train|express train|a long green train with lit windows and a plume of steam
jet|private jet|a sleek white jet on a runway with a stairway down
motorbike|motorbike|a lean black motorbike with a tall windscreen
gondola|cable car|a red cable car swinging high above a snowy valley""",
VSET="a winding mountain road; a night-time city street; a blue open sea; a snow-covered pass; a foggy runway; a glittering waterfront",
POSE="standing with a hand in a coat pocket; walking calmly; watching from behind a newspaper; leaning on a rail and scanning the room; adjusting a cufflink; crouching behind cover; looking over a shoulder; sitting with a drink",
SHOT="in a wide shot with the figure small in the scene; in a full-length view; in a medium portrait; from a low angle; over the shoulder; in a close portrait with the setting behind",
MOOD="with a cool, tense mood; with a stylish, confident mood; with a paranoid, watchful mood; with a quiet, lonely mood; with a playful, daring mood; with a hushed, secretive mood",
LIGHT="lit by a single lamp; lit by warm chandelier glow; lit by hard white light; lit by a cool screen glow; lit by dim light with deep shadows; lit by pale grey light")
for _g in (NR, PT, SY): _g['SLOC'] = dict(l.split('|') for l in _g['SLOC'].strip().split('\n'))
GENRES = [NR, PT, SY]
def build(final=None):
    G78.GENRES = GENRES
    G = {}; ep = []
    for g in GENRES:
        x = G78.one(g); ep += x.pop('%s_entry' % g['pre']); G.update(x)
    G['v79_genre_entry_points'] = ep
    return G
if __name__ == '__main__':
    b = build(); print(len(b))
