"""v77 stage C - toys and models: figures, dolls and plush (human and creature), playsets, board and card games and other toys, die-cast toys, and toy packaging
by era and condition. Invented brand names only (real ones belong in maker_ files). Text on boxes is in quotation marks."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from famlib import P
def A(l): return 'an' if l[0].lower() in 'aeio' else 'a'
COND = P("sealed and unopened; in mint condition; lightly shelf-worn; crushed at one corner; faded by sunlight; held together with old tape; stained by water; opened and resealed; yellowed with age; marked by a half-peeled price sticker; covered in dust")
LOOSE = P("lightly worn; heavily played with; dusty; repaired with glue; faded by sunlight; held together with old tape; yellowed with age; stained by water; cracked in places")
PWEAR = P("worn paint on the nose and knees; scuffed edges; a loose limb; chewed corners; faded colour; tiny cracks in the paint; a missing accessory; sticky grime in the joints; fingerprints in the dust; a dented head")
# ---------- figures
SCALE = P("a tiny finger-sized; a palm-sized; a hand-sized; a forearm-sized; a child-sized; a life-size")
FIG_KIND = """action figure|a jointed plastic action figure|plastic; vinyl; rubbery plastic; plastic with metal pins|a hero in a cape; a masked soldier; a space ranger in a white suit; a cowboy with a hat and holsters; a ninja in black; a pirate captain; a knight in plastic armour; a wrestler in trunks and boots; a robot with a chest panel; a monster with a fanged mouth; a caveman with a club; a safari explorer; a firefighter; an astronaut; a fantasy sorcerer; a rock-star in leather|swivelling shoulders and hips; ball-jointed knees and elbows; a spring-loaded punching arm; a tiny rotating waist; hands moulded to hold props|a plastic helmet; a tiny sword; a laser rifle; a small shield; a backpack; a pair of removable boots; a cape of thin cloth; a spare pair of hands
fashion doll|a fashion doll|vinyl and soft plastic; moulded plastic; glossy vinyl|in an evening gown with long glossy hair; in a sports kit with a short curly bob; in a bridal outfit; in a tiny business suit; in a travel outfit; in a vintage dress; in an astronaut suit; in a rock-band outfit|a bendable body; bendable knees; twisting waist; a swivelling head; rooted hair|a tiny handbag; high-heeled shoes; a hairbrush; a small dog; a set of spare outfits on hangers; a tiny mirror; a pair of sunglasses
porcelain doll|a porcelain doll|glazed porcelain; bisque; cloth and porcelain; painted composition|in a lace christening gown; in a velvet coat and bonnet; in a sailor suit; with ringlets and a ribbon; in a folk costume; with glass eyes and real hair; in a Victorian dress|a stiff cloth body; jointed arms on pegs; eyes that open and close; a sewn wig; fingers curled|a tiny parasol; a lace hat; a basket; a small book; a tiny pair of leather boots
rag doll|a stitched cloth doll|calico; wool; felt; linen; patchwork cotton|with button eyes; with yarn hair; in a patchwork apron; with a stitched smile; with striped stockings; in a floppy hat|a floppy cloth body; stitched hands; yarn braids; a hand-embroidered face; a soft stuffed head|a little knitted scarf; a wooden spoon; a patched pocket; a tiny cloth bag
wooden toy|a carved wooden toy figure|painted beech wood; carved pine; turned maple; lacquered birch|a soldier with a tall hat; a farmer and his cow; a nutcracker in a red coat; a jointed puppet; a toy animal on wheels; a carved sailor; a peg doll; a jack-in-the-box|painted features; a hinged jaw; wheels on the base; string-jointed limbs; a spring in the box|a small wooden drum; a tiny sword; a wooden cart; a painted hat
plush toy|a stuffed plush toy|soft short pile fleece; long shaggy fur; velvety velour; corduroy; mohair; knitted wool; minky fabric; worn fur-like fabric|a teddy bear; a floppy rabbit; a round penguin; a long-necked giraffe; a sleepy owl; a fox with a bushy tail; a smiling octopus with long arms; a hippo with a wide mouth; a sock monkey; a goofy dragon; a lamb; an elephant|a loose stuffed body; a soft embroidered nose; glass bead eyes; stitched whiskers; a crinkly ear; a squeaker inside|a ribbon bow; a tiny knitted scarf; a name tag sewn to the ear; a small heart patch; a bell on a collar
plush creature|a stuffed plush toy|soft plush; faux fur; felt; fleece; velvety velour|__cb_one__; __cb_hybrid_two__; a dragon with felt wings; a monster with many eyes; a mushroom creature; a sea creature with soft tentacles|a rounded, soft stuffed body; big stitched eyes; felt claws; soft fins; a long squashy tail|a ribbon around the neck; a tiny sewn-on badge; felt teeth; a patch on the belly
creature figure|a creature toy figure|hard plastic; rubbery vinyl; resin; cast metal|__cb_one__; __cb_hybrid_two__; __cb_hybrid_human__; a dragon with spread wings; a dinosaur; a sea monster; a giant insect|movable jaws; poseable legs; wings on hinges; a swivelling head; a movable tail|a stand base; a small egg; a tiny cave backdrop; a scattering of bones
resin collectible|a resin collectible statue|cast resin; painted resin; polystone|a warrior queen; a wizard; a dragon on a rock; a fox spirit; a robot hero; a skeleton knight|a rocky base; a base with a nameplate; fine painted details; a cape frozen mid-flutter|a certificate card; a clear display dome; a wooden plinth""".split('\n')
FIG_FACE = P("with a stern painted face; with a happy painted smile; with wide round eyes; with a heroic jaw; with a cheeky grin; with a sleepy face; with a snarling expression; with a calm, blank expression; with rosy cheeks; with a freckled nose")
FIG_ERA = P("from the 1950s; from the 1960s; from the 1970s; from the 1980s; from the 1990s; from the 2000s; from the 2010s; of a current design; from before the war")
# ---------- playsets
PLAY = """dollhouse|a wooden dollhouse|a three-storey mansion with a pitched roof and opening front|tiny furniture in every room; a miniature staircase; paper rugs; a tiny family seated at dinner; a hanging lamp; small framed pictures
fortress|a toy fortress|a plastic castle with a drawbridge, towers and a portcullis|a trap door; flags on poles; catapults; a dungeon; a tiny throne; soldiers on the walls
spaceship|a toy spaceship playset|a cockpit with moulded dials, a ramp and a hatch|a command chair; a tiny robot; a launch rail; stickers of controls; a pop-out engine
farm|a toy farm|a barn with opening doors, a silo and a fenced yard|plastic cows and sheep; a tiny tractor; a hayloft; a pond; a rooster; a fence
garage|a toy garage|a multi-level car park with a ramp and a lift|a petrol pump; a car wash; a repair bay; toy cars; a spinning turntable
stage|a toy theatre stage|a small wooden stage with painted curtains|a cut-out cast; a painted backdrop; footlights; a puppet master's bridge
workshop|a toy workshop|a bench with plastic tools, a vice and a shelf of boxes|a drill; a saw; a tiny anvil; a rack of wrenches
playmat|a cloth playmat|a printed town map with roads, a river and buildings|toy cars; wooden blocks; tiny trees; a bridge
pirate_ship|a toy pirate ship|a plastic galleon with sails, a plank and cannons|a captain; a treasure chest; a parrot; a small rowing boat
fire_station|a toy fire station|a red building with a sliding pole and an opening garage door|a fire engine; a ladder; a hose; a tiny alarm bell
treehouse|a toy treehouse|a plastic tree with a lodge, a rope ladder and a slide|a swing; a lookout; a hanging bucket; tiny birds
train_set|a toy railway|a wooden track with a bridge, a tunnel and a station|a little engine; carriages; signals; a level crossing
tin_town|a tin toy village|a street of lithographed tin buildings with tiny signs|a clock tower; a post office; a little shop; tin trees
accessory_set|an accessory set|a carry case of bits sized to fit the figures|a tiny table; chairs; cups; a map; a camp fire; a radio; a flag
dino_island|a toy dinosaur island|a moulded jungle with a volcano, a pool and a cave|a plastic dinosaur nest; a fence gate; a tiny jeep; ferns
space_base|a toy moon base|a white plastic dome with airlocks and a rover|a satellite dish; a flag; crates; a lunar buggy""".split('\n')
PLAY_FIT = P("sized for six-inch figures; sized for one-twelfth scale dolls; sized for tiny finger-sized figures; sized for plush animals; sized for sixty-millimetre soldiers; sized for twelve-inch figures; sized for one-sixth scale figures")
PLAY_COL = P("in bright primary colours; in faded pastel plastic; in warm wood and painted red; in brown and cream; in white and silver; in worn green and grey; in sun-bleached colours; in glossy new colours")
# ---------- games
GAMES = """board game|a board game|a printed folding board with a winding path of coloured spaces; a board with a map and numbered regions; a board with a grid of squares; a board in the shape of a star; a board with a spiral track|dice in a cup; wooden pawns; coloured plastic counters; a spinner; tiny cards; a stack of paper money|from the 1930s; from the 1950s; from the 1960s; from the 1970s; from the 1980s; from the 1990s; from the 2010s; of a current design
card game|a card game|a deck of cards in a cardboard sleeve; a tin of cards; a fan of illustrated cards; a deck with a bright back pattern; a card game in a tuck box|picture cards of animals; cards with numbers and colours; cards with tiny characters; cards with a bold border; special action cards|from the 1920s; from the 1950s; from the 1970s; from the 1980s; from the 1990s; from the 2010s
puzzle|a jigsaw puzzle|a boxed jigsaw puzzle with a painted scene on the lid; a round puzzle; a wooden puzzle with big pieces; a tin of puzzle pieces; a tray puzzle|pieces strewn across a table; a few pieces missing; a half-finished picture; a plastic bag of pieces; a corner piece in a hand|from the 1930s; from the 1950s; from the 1970s; from the 1990s; of a current design
dexterity toy|a small dexterity toy|a wooden ball-in-cup toy; a maze with a rolling ball; a stack of wooden rings; a tin of marbles; a spinning top; a yo-yo|string; a painted stick; coloured balls; a round tin lid; a wooden handle|from the 1930s; from the 1950s; from the 1960s; from the 1970s; from the 1990s
wind-up toy|a tin wind-up toy|a tin robot with a key; a tin monkey playing cymbals; a tin car with a driver; a tin duck on wheels; a tin drummer; a walking tin soldier|a clockwork key; lithographed details; a bent tab; rust spots on the base; painted rivets|from the 1920s; from the 1950s; from the 1960s; from the 1980s
construction toy|a building set|a tin of interlocking plastic bricks; a box of wooden blocks; a set of metal strips and bolts; a box of magnetic rods and balls; a tube of snap-together pieces|a manual with diagrams; a half-built tower; a spare pile of pieces; a tiny motor; a baseplate|from the 1950s; from the 1960s; from the 1980s; from the 2000s; of a current design
kite or ball|a simple outdoor toy|a paper kite; a rubber ball; a skipping rope; a bat and ball; a hoop and stick; a boomerang; a wooden sword and shield|a ribbon tail; faded stripes; a leather lace; chipped paint; a worn handle|from the 1930s; from the 1950s; from the 1970s; of a current design
remote toy|a toy with a remote control|a remote-controlled car; a remote robot with a cable; a radio-controlled boat; a remote helicopter; a toy tank|an antenna; a wire controller; a battery cover; a flashing light; a little rubber tyre|from the 1960s; from the 1980s; from the 2000s; of a current design""".split('\n')
BOXART = P("a painted illustration of children playing; a bold flat graphic of the contents; a photograph of a smiling family; a dramatic painted battle scene; a bright cartoon mascot; a plain colour band with a title; a collage of pictures of the pieces; a scene of the toy in action; a simple line drawing; a glossy photograph of the toy")
# ---------- packaging
PK = """blister card|a blister card|a stiff printed card with a clear plastic bubble holding the toy and a punched hanging hole
window box|a window box|a printed cardboard box with a clear plastic window showing the toy
tin|a collector's tin|a printed metal tin with a hinged lid and rounded corners
tube|a clear tube|a clear plastic tube with printed end caps
sleeve|a cardboard sleeve|a printed card sleeve that slides over the toy tray
paper wrapper|a paper wrapper|a printed paper wrapper folded around the toy and sealed with a sticker
bag|a header bag|a clear plastic bag stapled to a printed header card
display case|a display case|a clear acrylic case with a printed backing card
lidded box|a lidded box|a sturdy printed two-piece box with a separate lid and a paper liner
mailer|a mailer box|a plain brown cardboard box with a printed label and string
foil bag|a foil bag|a shiny foil bag with a crimped top and bright printing
tray|a tray with film|a moulded plastic tray covered with clear film and a printed cardboard sleeve
gift box|a gift box|a ribbon-tied printed box with tissue paper inside""".split('\n')
PK_ERA = P("in the style of the 1930s, with ornate lettering and flat painted pictures; in the style of the 1950s, with bold slab letters and bright flat colour; in the style of the 1960s, with pop colours and wide stripes; in the style of the 1970s, with orange and brown stripes and rounded fonts; in the style of the 1980s, with neon colours and starbursts; in the style of the 1990s, with jagged shapes and foil lettering; in the style of the 2000s, with glossy gradients; in a current minimalist style")
PK_TEXT = P('with the brand __text_brand__ across the top; with the words "NEW!" in a starburst; with a bold label reading "For ages 8 and up"; with a sticker reading "SALE"; with the words "Batteries not included" in small print; with a yellow flash reading "Collect them all!"; with the line "Made in the old workshop" in small print; with a banner reading "Genuine Quality"')
PK_EXTRA = P("with a small price sticker; with a hanging hole at the top; with a clear plastic window; with a hologram sticker; with an instruction sheet folded inside; with a numbered label on the back; with a paper seal across the lid; with a barcode on the side; with a tiny logo of an invented mascot")
# ---------- die-cast
DC_KIND = """car|a die-cast model car|a 1950s two-door family sedan; a 1950s tail-fin convertible; a 1960s muscle coupe; a 1960s mini hatchback; a 1960s sports roadster; a 1970s station wagon; a 1970s hot rod with big engine pipes; a 1980s boxy hatchback; a 1980s wedge-shaped supercar; a 1990s compact coupe; a 2000s sports sedan; a modern electric hatchback; a 1930s open touring car; a 1920s roadster; a taxi; a police car; a rally car with stickers; a drag racer; a classic mini van; a retro pickup truck
truck|a die-cast model truck|a tipper truck; a tanker truck; a cement mixer; a car transporter; a fire engine; a tow truck; a delivery van; a milk float; a flatbed lorry; a bulldozer; a mobile crane; an ice cream van; a camper van; a school bus; a double-decker bus; a refuse truck; an articulated lorry
aircraft|a die-cast model aircraft|a twin-propeller airliner; a jet airliner; a biplane; a jet fighter; a flying boat; a helicopter; a bomber from the old war; a small passenger plane; a space shuttle; a large cargo aircraft; a crop duster; an airship
ship|a die-cast model ship|a steam tugboat; an ocean liner; a battleship; a submarine; a lifeboat; a tall sailing ship; a fishing boat; a cargo ship; a paddle steamer; a speedboat
train|a die-cast model locomotive|a steam locomotive with a tender; a diesel engine; an electric commuter train; a bullet train; a tram; a coal wagon; a guard's van; a narrow-gauge engine
building|a die-cast model building|a tin cottage; a lighthouse; a fire station; a windmill; a small skyscraper; a church; a railway station; a barn; a castle; a gas station
figure|a die-cast figure|a toy soldier; a knight on horseback; a cowboy on a horse; a small cast robot; a farm worker; a clown; a king on a throne; a jockey on a racehorse
tool or animal|a die-cast miniature|a toy anvil; a pair of pliers; a brass hammer; a small horse; a cast dog; a lion; an elephant; a cast eagle; a heavy bulldog""".split('\n')
# per kind dc data: scale | cast | paint | wheels | baseplate
CARP = "in glossy red; in metallic blue; in cream and brown two-tone; in matte olive green; in glossy black; in bright yellow; in metallic gold; in sky blue with white stripes; in silver; in orange with black flames; in candy green; in white with a racing number; in police black and white"
DCX = {
 'car': ("at a large one-eighteenth scale; at one-forty-third scale; at a small one-sixty-fourth scale", "with a heavy metal body and plastic windows; with a metal body and a plastic base; with a fully metal body and rubber tyres; with a chunky body and a hinged bonnet; with doors that open; with a bonnet that opens to show an engine; with a chrome-plated grille; with a spring-loaded suspension", CARP, "on thin chrome wheels; on rubber tyres with white walls; on fat rubber tyres; on thin plastic wheels with red rims; on spoked wheels", 1),
 'truck': ("at one-forty-third scale; at a small one-sixty-fourth scale; at a tiny one-eighty-seventh scale", "with a metal body and a plastic base; with a tipping bed; with a hinged cab; with a working crane arm; with a rotating drum; with opening rear doors; with a chrome-plated grille", "in glossy red; in bright yellow; in white with blue lettering; in orange; in two-tone green and cream; in matte olive green; in blue with white stripes; in police black and white", "on thin plastic wheels; on rubber tyres; on fat rubber tyres; on steel wheels", 1),
 'aircraft': ("at one-seventy-second scale; at one-hundred-and-forty-fourth scale; at hand-sized scale", "with a thin metal body and plastic propellers; with a heavy metal body and swivelling wings; with a metal fuselage and a plastic stand; with folding wings; with retractable wheels; with a clear plastic cockpit", "in polished silver; in desert camouflage; in white with a blue stripe; in olive green; in sky blue; in red and cream; in glossy grey", "on a clear plastic stand; on a tiny set of wheels; on a flat display base", 1),
 'ship': ("at one-six-hundredth scale; at hand-sized scale; at finger-sized scale", "with a solid metal hull; with a thin metal hull and plastic funnels; with tiny cast lifeboats; with a plastic mast and thread rigging; with a rotating gun turret", "in black with a red funnel; in battleship grey; in white and blue; in dark green; in rust red; in cream and brown", "on a small wheeled base; on a flat display base; on a plain plastic stand", 1),
 'train': ("at one-eighty-seventh scale; at a larger hand-sized scale; at finger-sized scale", "with a heavy metal body; with a metal body and plastic wheels; with moving rods on the wheels; with a tiny funnel that smokes; with a coupling hook", "in glossy black with red wheels; in green with gold lining; in blue and cream; in red and grey; in matte olive green; in glossy brown", "on thin metal wheels; on plastic flanged wheels", 1),
 'building': ("at hand-sized scale; at palm-sized scale; at finger-sized scale", "with a solid metal body; with a thin metal shell and a plastic base; with tiny cast windows; with a painted roof; with painted brickwork; with a lit window cut-out", "in cream walls with a red roof; in grey stone with a green roof; in painted white with blue trim; in red brick with a black roof; in yellow with brown timber", "on a small green base; on a flat painted base; on a plain base", 0),
 'figure': ("at hand-sized scale; at palm-sized scale; at finger-sized scale", "with a solid metal body; with a hollow cast body; with a cast horse; with raised arms; with a movable arm; with a painted face", "in a bright painted uniform; in red and gold paint; in blue and white paint; in green and brown paint; in plain bronze", "on a round base; on a rectangular base; on a base with a painted grass edge", 0),
 'miniature': ("at hand-sized scale; at palm-sized scale; at finger-sized scale", "with a solid metal body; with a bright chrome plating; with fine cast detail; with a heavy base", "in polished brass; in bronze; in silver; in black; in gold paint; in matte grey", "on a small wooden base; on a flat base; on a plain base", 0),
}
DC_WEAR = P("with a few chips on the corners; with rubbed paint on the top; with a scratched window; with a loose part; with a bent axle; with rust on the underside; with a small dent; with a sticker half peeled; with yellowed windows; with a repainted body; with oil stains on the base")
DC_BASE = P('with "MADE IN ENGLAND" stamped on the underside; with "No. 48" cast into the underside; with a model name cast in raised letters on the underside; with a tiny copyright date on the underside; with a rivet visible in the middle of the underside; with a scale mark stamped on the underside')
GTITLE = {
 'board_game': '"Treasure Trail"; "Race to the Moon"; "Haunted Hallway"; "Lost Kingdoms"; "Market Day"; "Tiny Tycoons"; "Grand Hotel"; "Pirate Cove"',
 'card_game': '"Snap Happy"; "Midnight Heist"; "Jungle Jam"; "Captain Grumble"; "Bake-Off"; "Pocket Detectives"',
 'puzzle': '"Harbour at Dawn"; "The Old Mill"; "Garden Party"; "Mountain Lake"; "Circus Parade"; "Rocket Launch"',
 'dexterity_toy': '"Whirl-a-Top"; "Rolling Marbles"; "Steady Hands"; "Ring Toss"',
 'wind_up_toy': '"Tin Tommy"; "Drummer Boy"; "Clockwork Charlie"; "Marching Duck"',
 'construction_toy': '"Brick Builder"; "Tower Time"; "Engineer Set"; "Magna-Rods"',
 'kite_or_ball': '"Sky Dancer"; "Bouncing Joe"; "Summer Days"; "Garden Games"',
 'remote_toy': '"Rally Racer"; "Sky Hawk"; "Robo Rover"; "Speed Boat"'}
BOXED = ('board_game', 'card_game', 'puzzle', 'construction_toy', 'remote_toy')
def build(final=None):
    G = {'toy_condition': COND, 'toy_loose': LOOSE, 'toy_wear': PWEAR, 'toy_face': FIG_FACE, 'toy_era': FIG_ERA}
    ks = []
    DOLL = ('fashion_doll', 'porcelain_doll', 'rag_doll')
    SC = {'action_figure': 'finger-sized; palm-sized; hand-sized', 'fashion_doll': 'hand-sized; forearm-sized', 'porcelain_doll': 'hand-sized; forearm-sized; child-sized', 'rag_doll': 'hand-sized; forearm-sized; child-sized', 'wooden_toy': 'finger-sized; palm-sized; hand-sized', 'plush_toy': 'palm-sized; hand-sized; forearm-sized; child-sized; life-size', 'plush_creature': 'palm-sized; hand-sized; forearm-sized; child-sized', 'creature_figure': 'finger-sized; palm-sized; hand-sized; forearm-sized', 'resin_collectible': 'palm-sized; hand-sized; forearm-sized'}
    for row in FIG_KIND:
        label, noun, mats, types, arts, extras = row.split('|')
        k = label.replace(' ', '_'); nn = noun.replace('a ', '', 1)
        G['toy_%s_type' % k] = P(types); G['toy_%s_material' % k] = P(mats); G['toy_%s_artic' % k] = P(arts); G['toy_%s_extra' % k] = P(extras)
        G['toy_%s_scale' % k] = ['a ' + x for x in SC[k].split('; ')]
        con = ' ' if k in DOLL else ' depicting '
        face = ', __toy_face__' if k in ('action_figure', 'fashion_doll', 'wooden_toy') else ''
        G['toy_%s_short' % k] = ['__toy_%s_scale__ %s%s__toy_%s_type__, made of __toy_%s_material__.' % (k, nn, con, k, k)]
        G['toy_%s_look' % k] = ['__toy_%s_scale__ %s%s__toy_%s_type__, made of __toy_%s_material__%s, with __toy_%s_artic__, __toy_era__' % (k, nn, con, k, k, face, k)]
        G['toy_%s_prompt' % k] = ['The toy is __toy_%s_look__. Nearby is __toy_%s_extra__. It is __toy_loose__ and has __toy_wear__. It is shown on __toy_surface__.' % (k, k)]
        ks.append(k)
    G['toy_surface'] = P("a plain wooden table; a pale cloth; a shelf among other toys; a child's bedroom floor; a glass display shelf; a workbench; a pile of cushions; a white backdrop; a market stall table")
    for s_ in ('prompt', 'short', 'look'): G['toy_figure_' + s_] = ['__toy_%s_%s__' % (k, s_) for k in ks]
    G['toy_lineup_prompt'] = ['A line-up of figures standing side by side on a shelf. On the left is __toy_figure_short__ Next is __toy_figure_short__ In the middle is __toy_figure_short__ Next is __toy_figure_short__ On the right is __toy_figure_short__ They are all __toy_loose__.']
    pk = []
    for row in PLAY:
        k, label, look, extras = row.split('|'); l2 = label.replace('a ', '', 1) if label.startswith('a ') else label.replace('an ', '', 1)
        G['toy_play_%s_look' % k] = ['%s %s, %s' % (A(l2), l2, look)]; G['toy_play_%s_extra' % k] = P(extras)
        G['toy_play_%s_prompt' % k] = ['The playset is __toy_play_%s_look__, __toy_play_fit__, __toy_play_colour__. It includes __toy_play_%s_extra__. It is __toy_loose__ and has __toy_play_wear__, and it is on __toy_surface__.' % (k, k)]
        G['toy_play_%s_scene' % k] = ['A view of __toy_play_%s_look__, __toy_play_fit__, with figures posed in it. Posed in it are __toy_figure_look__ and __toy_figure_look__. It also includes __toy_play_%s_extra__.' % (k, k)]
        pk.append(k)
    G['toy_play_wear'] = P('scuffed edges; faded colour; a cracked piece; a missing part; fingerprints in the dust; peeling stickers; scratched paint; a bent hinge')
    G['toy_play_fit'] = PLAY_FIT; G['toy_play_colour'] = PLAY_COL
    G['toy_play_prompt'] = ['__toy_play_%s_prompt__' % k for k in pk]; G['toy_play_scene'] = ['__toy_play_%s_scene__' % k for k in pk]
    gk = []
    for row in GAMES:
        label, noun, items, bits, eras = row.split('|'); k = label.replace(' ', '_').replace('-', '_'); nn = noun.replace('a ', '', 1)
        G['toy_game_%s_item' % k] = P(items); G['toy_game_%s_bits' % k] = P(bits); G['toy_game_%s_era' % k] = P(eras); G['toy_game_%s_title' % k] = P(GTITLE[k])
        G['toy_game_%s_look' % k] = ['__toy_game_%s_item__, __toy_game_%s_era__, with __toy_game_%s_bits__' % (k, k, k)]
        if k in BOXED:
            G['toy_game_%s_prompt' % k] = ['A boxed %s, __toy_game_%s_look__. The box shows __toy_boxart__ and carries the title __toy_game_%s_title__ and the brand __text_brand__. The box is __toy_condition__, and it is on __toy_surface__.' % (nn, k, k)]
        else:
            G['toy_game_%s_prompt' % k] = ['A %s, __toy_game_%s_look__. It carries the name __toy_game_%s_title__ and the brand __text_brand__. It is __toy_loose__ and has __toy_play_wear__, and it is on __toy_surface__.' % (nn, k, k)]
        G['toy_game_%s_short' % k] = ['__toy_game_%s_item__, __toy_game_%s_era__.' % (k, k)]
        gk.append(k)
    G['toy_boxart'] = BOXART
    G['toy_game_prompt'] = ['__toy_game_%s_prompt__' % k for k in gk]; G['toy_game_short'] = ['__toy_game_%s_short__' % k for k in gk]
    tk = []
    for row in PK:
        k, noun, look = row.split('|'); k = k.replace(' ', '_')
        G['toy_pack_%s_look' % k] = ['%s, %s' % (noun, look)]
        G['toy_pack_%s_prompt' % k] = ['Toy packaging, __toy_pack_%s_look__, __toy_pack_era__, __toy_pack_text__, __toy_pack_extra__. It holds __toy_any_short__ It is __toy_condition__.' % k]
        G['toy_pack_%s_short' % k] = ['__toy_pack_%s_look__, __toy_pack_era__.' % k]
        tk.append(k)
    G['toy_pack_era'] = PK_ERA; G['toy_pack_extra'] = PK_EXTRA; G['toy_pack_text'] = PK_TEXT
    G['toy_pack_prompt'] = ['__toy_pack_%s_prompt__' % k for k in tk]; G['toy_pack_short'] = ['__toy_pack_%s_short__' % k for k in tk]
    G['toy_pack_look'] = ['__toy_pack_%s_look__' % k for k in tk]
    G['toy_any_short'] = ['__toy_figure_short__', '__dc_short__']
    G['toy_prompt'] = ['__toy_figure_prompt__', '__toy_play_prompt__', '__toy_game_prompt__', '__toy_pack_prompt__']
    dk = []
    for row in DC_KIND:
        label, noun, types = row.split('|'); k = label.replace(' ', '_').replace('tool_or_animal', 'miniature')
        sc, cast, paint, wheel, hw = DCX[k]
        G['dc_%s_type' % k] = P(types); G['dc_%s_scale' % k] = P(sc); G['dc_%s_cast' % k] = P(cast); G['dc_%s_paint' % k] = P(paint); G['dc_%s_wheel' % k] = P(wheel)
        G['dc_%s_look' % k] = ['__dc_%s_type__, __dc_%s_scale__, __dc_%s_cast__, __dc_%s_paint__, __dc_%s_wheel__' % ((k,) * 5)]
        G['dc_%s_prompt' % k] = ['A %s. It is __dc_%s_look__, __dc_base__. It is __toy_loose__, __dc_wear__. It sits on __toy_surface__.' % (noun.replace('a ', '', 1), k)]
        G['dc_%s_boxed' % k] = ['A %s still in its packaging. The model is __dc_%s_look__. The packaging is __toy_pack_look__, __toy_pack_era__, __toy_pack_text__. It is __toy_condition__.' % (noun.replace('a ', '', 1), k)]
        G['dc_%s_short' % k] = ['__dc_%s_type__, __dc_%s_paint__.' % (k, k)]
        dk.append(k)
    G['dc_wear'] = DC_WEAR; G['dc_base'] = DC_BASE
    for s_ in ('prompt', 'boxed', 'short'): G['dc_' + s_] = ['__dc_%s_%s__' % (k, s_) for k in dk]
    G['dc_collection_prompt'] = ["A collector's shelf of die-cast models. On the left is __dc_short__ Next is __dc_short__ In the middle is __dc_short__ Next is __dc_short__ On the right is __dc_short__ They are all __toy_loose__."]
    G['v77_toy_entry_points'] = ['toy_prompt', 'toy_figure_prompt', 'toy_lineup_prompt', 'toy_play_prompt', 'toy_play_scene', 'toy_game_prompt', 'toy_pack_prompt', 'dc_prompt', 'dc_boxed', 'dc_collection_prompt'] + ['toy_%s_prompt' % k for k in ks]
    return G
if __name__ == '__main__': print(len(build()))
