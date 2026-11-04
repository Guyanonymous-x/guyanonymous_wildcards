"""v77 stage A - fantasy (fa_) and horror (ho_): styles, folk or entities, characters, locations, objects, each by looks only, plus shared pools."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from famlib import P
def A(l): return 'an' if l[0].lower() in 'aeio' or (l[0].lower() == 'u' and not l.lower().startswith(('uni', 'use'))) else 'a'

FA_STYLES = """high_fantasy|high fantasy|soaring white towers, banners in the wind, heroic poses and clean bright colour|golden hour light with a crisp sky|a sweeping vista behind
dark_fantasy|dark fantasy|blackened armour, ruined stone, thin cold mist and a worn, grim mood|low grey light with deep shadow|bones and crows at the edges
fairy_tale|fairy tale|a picture-book look with soft rounded shapes, small cottages and glowing windows|warm lantern light on a deep blue evening|tiny animals watching from the grass
sword_and_sorcery|sword and sorcery|lean fighters, smoky torches, sweating stone halls and bright blades|torchlight with orange glow and black shadow|a heap of old treasure in a corner
mythic_epic|mythic epic|towering figures, great pillars, gleaming bronze and wide dramatic skies|bright hard sun with long shadows|a wide plain far below
gaslamp_fantasy|gaslamp fantasy|cobbled streets, brass lamps, long coats, top hats and quiet magic in a foggy city|yellow gaslight in blue fog|a hansom cab waiting at the kerb
whimsical_fantasy|whimsical fantasy|crooked towers, bright patchwork colours, chubby creatures and playful props|soft pastel daylight|floating bubbles and paper lanterns
urban_fantasy|urban fantasy|neon signs and wet pavement with a hidden magical door, spell marks chalked on walls|night city light with coloured reflections|a stray cat with glowing eyes
grimdark|grimdark|mud, rust, torn banners, tired soldiers and heavy overcast sky|flat overcast light|smoke on the horizon
pastoral_fantasy|pastoral fantasy|rolling green hills, thatched cottages, hedgerows and a gentle old magic in the air|soft morning light with long mist|sheep and a stone wall
desert_sorcery|desert sorcery|wind-carved dunes, painted tents, brass lamps and shimmering heat over ancient ruins|harsh noon sun with warm sand tones|a caravan far away
frozen_north|frozen north saga|snowy fjords, longhouses, fur cloaks, runestones and the glow of a green sky|cold blue light with a pale aurora|a long ship beached on ice""".split('\n')
FA_FOLK = """elf|elf|a tall slender person with pointed ears, high cheekbones and long straight hair|a moss-hung forest glade
dwarf|dwarf|a short, broad, powerful person with a thick braided beard and strong hands|a lamplit mine hall with stone arches
halfling|halfling|a small cheerful person with bare furred feet, curly hair and round cheeks|a round-doored hillside home with a flower garden
gnome|gnome|a tiny wiry person with a pointed hat, bright eyes and big ears|a workshop full of tiny gears and glass jars
orc|orc|a heavy green-grey skinned person with tusks, a broad jaw and scarred shoulders|a ridge camp with hide tents and fires
goblin|goblin|a wiry, long-nosed, big-eared green person with sharp teeth and nimble fingers|a junk-filled tunnel lit by candle stubs
troll|troll|a huge, lumpy, stone-skinned person with mossy patches and a heavy brow|a stone bridge over a fast river
ogre|ogre|a very large, thick-limbed person with a wide face, small eyes and a belly|the mouth of a cave with a smoking camp
fae|fae|a slight, luminous person with thin wings, leaf-like hair and a sharp, curious face|a ring of mushrooms in twilight
giant|giant|an enormous person as tall as the trees, with a rough cloak and slow movements|a valley with tiny huts at their feet
centaur|centaur|a person with a human torso on the body of a horse, a braided mane and a strong bow|a wide meadow with tall grass
satyr|satyr|a person with curled horns, goat legs, hairy thighs and a pipe in their hand|a sunlit vineyard on a hillside
mermaid|mermaid|a person with a scaled fish tail, fin-like ears and wet shining hair|a rock pool at the edge of the sea
dragonborn|dragonkin|a person with fine scales, a dragon-like snout, small horns and a thick tail|a rocky ledge above a canyon
tiefling|hornkin|a person with swept-back horns, a long tail and deep red skin|a candlelit tavern at night
undead_knight|undead knight|a gaunt armoured figure with hollow eyes, rusted plate and a torn cloak|a fog-covered battlefield
treefolk|living tree|a tall person made of living bark and branches, with a leaf crown and slow deep eyes|the middle of an ancient wood
stone_folk|living statue|a heavy person carved from grey rock, with glowing crystals in the chest and moss on the shoulders|a mountain pass with scattered boulders
beastfolk_fox|foxkin|a person with fox ears, a bushy tail, russet fur on the face and sharp amber eyes|a lantern-lit lane between wooden houses
beastfolk_wolf|wolfkin|a person with wolf ears, thick grey fur, a muzzle and a fur-trimmed coat|a snowy ridge beside a pine forest
beastfolk_cat|catkin|a person with cat ears, a long tail, slit pupils and sleek short fur|a rooftop under the moon
winged_folk|wingkin|a person with large feathered wings folded behind them and pale clothes|a cliff-top village of rope bridges
ratfolk|ratkin|a hunched person with a pink nose, whiskers, round ears and a patched coat|a cluttered cellar market
salamander_folk|lizardkin|a lean person with smooth patterned skin, a flat head and a long tail|a steaming swamp with stilted huts""".split('\n')
FA_CLASS = """knight|knight|a polished steel breastplate, a surcoat with a painted crest and a long sword|a kite shield
wizard|wizard|a long robe with star patterns, a tall pointed hat and a gnarled staff|a heavy book and a glowing orb
rogue|rogue|a dark hooded leather jerkin, soft boots and a belt of tools|a thin knife and a ring of keys
ranger|ranger|a green cloak, a long bow and sturdy walking boots|a quiver and a hunting horn
cleric|healer in white|a plain white robe, a shining pendant and bandaged hands|a small bell and a staff with a lantern
bard|bard|a bright patched coat, a feathered cap and a lute on a strap|a rolled songbook
alchemist|alchemist|a stained apron, thick gloves and goggles pushed up on the head|a rack of bubbling flasks
witch|witch|a patched shawl, a wide hat, jars on a belt and a bundle of herbs|a broom and a black cat
paladin|paladin|gleaming plate armour with a white tabard and a golden sun emblem|a mace and a glowing shield
barbarian|barbarian|a fur cloak, bare scarred arms, leather straps and a huge axe|a horned drinking cup
druid|druid|a leaf-green robe, antler headband and a staff wrapped in vines|a crow on the shoulder
sorceress|sorcerer|a flowing coat with embroidered runes, rings on every finger and sparks around the hands|a floating ring of light
blacksmith|blacksmith|a leather apron, soot-black forearms and a heavy hammer|an anvil and tongs
innkeeper|innkeeper|a rolled-sleeve shirt, a stained apron and a tray of tankards|a ring of cellar keys
merchant|travelling merchant|a wide coat with a hundred pockets and a pack-laden mule|a set of brass scales
bounty_hunter|monster hunter|a battered leather coat, a crossbow and rows of vials on a bandolier|a silver sword on the back
battle_mage|battle mage|half-plate armour under a mage's coat with a glowing staff|crackling lightning on the fingertips
jester|court jester|a diamond-patterned costume, a belled hat and a painted face|a rattle on a stick
royal_guard|royal guard|a plumed helm, polished armour in red and gold and a tall spear|a tower shield with a lion emblem
queen|ruler|a heavy crown, a long velvet mantle and rings of office|a carved sceptre
pilgrim|pilgrim|a rough brown cloak, a scallop shell and a wooden staff|a worn leather satchel""".split('\n')
FA_LOC = """castle_hall|castle great hall|a long hall with high beams, banners, a roaring hearth and a long banquet table
wizard_tower|wizard's tower study|a round room with crowded shelves, a brass telescope, floating candles and a stuffed owl
tavern|fantasy tavern|a low timbered room with a big fireplace, mismatched tables and a bard in the corner
dragon_lair|dragon's lair|a vast cavern with a mountain of gold coins, broken swords and glowing embers
forest_glade|enchanted glade|a clearing ringed with old trees, mushrooms, drifting motes of light and a mossy altar
elven_city|elf city in the trees|rope bridges and curved wooden halls among giant tree trunks hung with lanterns
dwarf_hall|dwarf hall|huge carved stone pillars, rivers of molten gold in channels and forge fires
market|fantasy market square|colourful stalls, a fountain, banners, odd potions and creatures for sale
ruins|overgrown ruins|toppled columns under thick vines, a broken statue and a hidden stair
bridge|ancient stone bridge|a mossy single arch over a deep gorge with mist rising
harbour|fantasy harbour|tall-masted ships, crooked warehouses, hanging lamps and gulls
mountain_pass|mountain pass|a narrow snowy path between sheer cliffs with a distant fortress
swamp|witch's swamp|black water, hanging moss, a leaning stilt hut and green marsh lights
floating_isle|floating islands|rocky islands in the sky joined by chains, waterfalls dropping into cloud
crypt|crypt|rows of carved stone tombs, dripping candles and a sealed iron door
library|wizard's library|endless tall shelves, ladders, glowing books and a sleeping dragon-cat
throne_room|throne room|a long red carpet, tall windows, a high stone throne and a ring of guards
village|thatched village|crooked cottages, a well, hens in the road and smoke from chimneys
temple|mountain temple|stepped white stone, bells, prayer flags and mist in the valley
battlefield|battlefield at dawn|broken spears, trampled banners, pale mist and distant horns
alchemy_lab|alchemy laboratory|copper stills, glass tubing, bubbling vats and shelves of coloured bottles
cave_market|underground market|lantern-lit tunnels, hanging cloth stalls and traders in hooded cloaks
crystal_cavern|crystal cavern|enormous glowing crystals, a still blue lake and dripping echoes
witch_cottage|witch's cottage|a crooked hut with herbs hanging from the beams, a cauldron and a black cat
sky_ship|sky ship deck|a wooden ship deck with great canvas sails, hanging in clouds
frozen_keep|frozen fortress|a castle of blue ice with icicle spires and a white wolf at the gate
desert_oasis|desert oasis|palms, a clear pool, painted tents and warm lamp light
sunken_city|sunken city|pale columns and arches under green water, shoals of fish and drifting light
giant_tree|giant tree house|a vast hollow tree with stairs winding inside and lit windows in the bark
road_inn|roadside inn|a stone and timber inn with a swinging sign, a stable and a night of rain""".split('\n')
FA_ITEM = """sword|enchanted sword|a long blade with runes along the fuller and a softly glowing edge
staff|wizard's staff|a gnarled wooden staff topped with a floating crystal
amulet|amulet|a heavy silver pendant on a chain set with a single dark stone
grimoire|spellbook|a thick book bound in cracked leather with a metal clasp and glowing pages
crown|crown|a tarnished gold crown set with uneven gems and a cracked band
chalice|chalice|a plain silver cup that glimmers from inside
ring|ring of power|a thick gold band with tiny engraved letters and a faint heat haze
potion|potion bottle|a stoppered glass bottle of swirling coloured liquid with a wax seal
map|treasure map|a stained parchment map with inked mountains, a red cross and curled edges
shield|dragon shield|a round shield covered in overlapping scales with a polished boss
bow|elven bow|a slender curved bow of pale wood with silver inlays and a glowing string
orb|scrying orb|a clear glass ball on a carved stand with clouds moving inside
lantern|ghost lantern|an old iron lantern with a cold blue flame and cracked glass
horn|war horn|a large curved horn banded in brass and hung from a leather strap
key|ancient key|a long iron key with an ornate bow and teeth like a tiny castle
boots|travelling boots|worn leather boots with faint winged marks on the heels
cloak|travelling cloak|a heavy green cloak with a silver clasp and a hood that casts deep shadow
mirror|magic mirror|a tall oval mirror in a black carved frame whose surface ripples
egg|dragon egg|a large egg with iridescent scales and a faint glow in the cracks
hammer|forge hammer|a thick-headed war hammer with a runed haft and a leather wrist loop""".split('\n')
FA_POSE = P("standing tall with one hand on a weapon; walking forward through the scene; crouching to look at something on the ground; looking out over the view; sitting by a fire with a hot drink; turned half away with a glance back; raising an arm to cast a spell; resting against a wall with crossed arms; leading a horse by the reins; reading from an old scroll; sharpening a blade; laughing with head thrown back")
FA_SHOT = P("in a wide shot with the figure small in the scene; in a full-length view; in a medium portrait; from a low angle; over the shoulder; in a close portrait with the setting soft behind")
FA_PERSON = P("a woman; a man; a non-binary person; an older woman; an older man; a young woman; a young man")
FA_MOOD = P("with an adventurous mood; with a calm, hushed mood; with a heroic mood; with a tense mood; with a warm, homely mood; with a lonely, quiet mood; with a mysterious mood")

HO_STYLES = """gothic|gothic horror|pointed arches, black iron, candle smoke, cobwebs and dark velvet|cold moonlight through narrow windows|a raven on a stone ledge
folk_horror|folk horror|straw crowns, a standing stone, a silent crowd in masks and a bright, wrong, sunlit field|flat pale daylight with long shadows|woven straw figures along a path
cosmic_horror|cosmic horror|a sky with the wrong colours, enormous shapes in the distance, tiny humans and a sense of vast scale|dim green-grey light|tentacle shapes against the clouds
haunted_house|haunted house|peeling wallpaper, a staircase with a dark landing, sheets over furniture and cold lamplight|a single weak lamp and deep shadow|a door left slightly open
ghost_story|ghost story|a pale transparent figure, drifting mist, an old lamp and a damp, quiet room|blue-white moonlight and low candle glow|a chair rocking slowly
creature_feature|creature feature|a huge lurking shape, wet floors, flashlights cutting the dark and shocked faces|harsh torch beam in black air|claw marks on a metal wall
psychological|psychological horror|an empty corridor, a flickering tube light, too many doors and a figure at the far end|sickly fluorescent light|a mirror reflecting something slightly off
abandoned|abandoned place|collapsed ceilings, peeling paint, rusted beds, weeds through the floor and stale light|dust-filled shafts of daylight|a child's toy in the dust
carnival|carnival horror|a rusted fairground, painted clown faces, broken rides and flickering bulbs|strings of dim coloured bulbs in fog|a carousel horse with a cracked grin
rural_gothic|rural gothic|a leaning farmhouse, a dead tree, a cold wind in the corn and a single lit window|low orange dusk light|a scarecrow in the field
ocean_horror|ocean horror|a creaking wooden ship in a fog bank, black water and a pale shape beneath the surface|grey dawn light|a ship's bell ringing alone
snow_horror|snow horror|a white wilderness, a lone cabin, tracks in the snow that stop and a whiteout wind|blue dusk light|a figure standing far out on the ice""".split('\n')
HO_ENT = """pale_bride|pale bride ghost|a transparent woman in a torn wedding dress with long wet black hair over her face|a cold hallway
faceless_man|faceless man|a very tall thin man in a black suit with a smooth blank face|the edge of a dark wood
scarecrow|living scarecrow|a stitched burlap figure on a pole with straw poking out and button eyes|a field of dry corn
plague_doctor|beaked doctor|a figure in a long waxed coat with a bird-beak mask, round glass eyes and a cane|a foggy cobbled street
drowned_woman|drowned woman|a woman with pale blue skin, dripping hair and seaweed tangled on her dress|the shore of a still lake
antlered_figure|antlered stalker|a gaunt figure with a deer skull for a head, long arms and a tattered cloak|a misty forest
wall_thing|thing in the walls|a long pale arm and a thin pale face pressing out of cracked plaster|an old bedroom
puppet|living puppet|a wooden marionette with a painted smile, cracked cheeks and strings that go up into the dark|a dusty theatre
clown|sinister clown|a tall figure in a faded costume with a chalk-white face, a wide painted smile and a drooping flower|an empty fairground
mirror_twin|mirror twin|a figure in a mirror that smiles after the real person stops|a dim bathroom
lantern_man|lantern bearer|a hooded figure holding a lantern with a green flame, its face hidden|a marsh path
crow_woman|crow woman|a stooped woman in a cloak of black feathers with a long beak-like nose and shining eyes|a ruined chapel
hollow_knight|hollow knight|an empty suit of armour with a glowing red pinprick in each eye slit|a stone crypt
long_limbed|long-limbed crawler|a pale humanoid on all fours with too many joints and a bowed head|a dim attic
shadow_figure|shadow figure|a tall man-shaped shadow with no source, standing against a wall|a bedroom at night
spider_nest|spider nest|a huge mass of grey webbing with many glinting eyes in the dark|an old cellar
melting_figure|melting figure|a figure in a coat whose face and hands sag and drip like warm wax|a dim motel room
wendigo|antlered giant|a starved giant with sunken eyes, grey skin stretched on ribs and tall antlers|a snowfield at dusk
swarm|bird swarm|hundreds of black birds on the roof, wires, and ground, all facing the same way|a quiet suburban street
sleepwalker|sleepwalker|a person in a nightgown with open blank eyes, standing at the top of stairs|a dim landing
mask_crowd|masked crowd|a crowd in identical white masks standing silent in a field|an open field at dusk
doll_woman|porcelain doll woman|a life-size porcelain doll with a cracked face and glass eyes sitting very still|a nursery with dust sheets
pale_hands|many hands|dozens of pale hands pressing against the inside of a window|a dark farmhouse window
bog_thing|bog creature|a lumpy figure of mud, roots and wet leaves with two glowing eyes|a black peat bog
lighthouse_keeper|ghost keeper|a faint bearded figure in an oilskin coat with a lamp, soaked and sad|a storm-struck lighthouse""".split('\n')
HO_CLASS = """survivor|survivor|a torn jacket, a scraped face, a flashlight and wide watchful eyes|a battered flashlight
investigator|investigator|a long coat, a camera on a strap and tired eyes|a notebook and pencil
priest|priest|a black cassock, a white collar, a wooden cross and a worn book|a small flask and a candle
medium|medium|a shawl, many rings, kohl-dark eyes and a hand resting on a table|a candle in a saucer
caretaker|old caretaker|worn overalls, a heavy ring of keys and a dim lantern|a lantern with a cracked glass
traveller|lost traveller|a rain-soaked coat, a rucksack and a map held in one hand|a dead phone
widow|widow in black|a veiled hat, a long black dress and gloves holding a small photograph|a framed portrait
doctor|night doctor|a rumpled white coat, a stethoscope and a clipboard under a flickering lamp|a pocket torch
hunter|hunter|a thick wool coat, a rifle on a sling and a woollen cap|a lantern and rope
photographer|photographer|a vest of pockets, a camera on each hip and a tripod|a camera with a long lens
teenage_adult|young adult|a hoodie, torn jeans and scuffed trainers|a phone with a lit screen
farmer|farmer|a worn coat, a flat cap, muddy boots and a pitchfork|a pitchfork
scholar|scholar|a tweed jacket, round glasses and an armful of old books|a leather book with a clasp
sailor|old sailor|an oilskin coat, a beard and a pipe, with a rope in one hand|a ship's lantern
nurse|night nurse|a pale uniform, a cardigan and a small torch|a ring of keys
occultist|occultist|a dark hooded coat, chalk-white hands and a dagger in the belt|a book of symbols""".split('\n')
HO_LOC = """mansion_hall|mansion hall|a vast hall with a dust-sheeted piano, a sweeping stair, cracked portraits and a chandelier hanging by one chain
attic|attic|a low sloping roof, trunks, a dress form, a mirror under a sheet and a single dusty window
cellar|cellar|damp stone walls, a bare bulb, shelves of jars and a door in the floor
asylum|abandoned asylum ward|a long corridor of rusted bed frames, peeling green paint and flickering light
forest_path|forest path at night|tall dark trunks, a thin fog and a faint lantern far ahead
graveyard|graveyard|leaning stones, a rusted gate, ground mist and a broken angel statue
chapel|ruined chapel|a roofless nave with broken pews, wet leaves and a cracked altar
cabin|woodland cabin|a small timber cabin, one lit window, a woodpile and a thin path of footprints
motel|empty motel|a flickering sign, a row of closed doors, a dry pool and a single parked car
hospital|night hospital corridor|long green corridor, a gurney, flickering fluorescent tubes and a door ajar
school|empty school|rows of small desks, a cracked blackboard with faded writing and a coat hook row
theatre|abandoned theatre|a velvet curtain, red seats under dust and a single ghost light on a stage
fairground|closed fairground|a rusted wheel, a boarded stall, scattered tickets and a turning carousel
lighthouse|storm lighthouse|a spiral stair, a huge cold lens and the sea crashing below
farmhouse|farmhouse kitchen|a long table, a cold stove, faded floral wallpaper and a rocking chair
subway|empty subway platform|tiled walls, a flickering board, a dead train and a long dark tunnel
nursery|dusty nursery|a wooden cot, a stack of old toys, a music box and faded wallpaper
swamp|swamp|black pools, hanging moss, rotted boats and low mist
mine|mine tunnel|timber supports, rusted rails, a hanging lamp and an echoing drip
mirror_room|hall of mirrors|endless reflected corridors, a cracked mirror and a figure in the glass
station|empty railway station|an old clock stopped, a long bench, rain on the roof and one lit window
hotel|empty hotel corridor|a long patterned carpet, identical doors, wall lamps and a cart left in the hall
library|dark library|tall shelves, a green reading lamp, a ladder and one book left open
church_bell|bell tower|a cracked bell, thick ropes, dusty beams and pigeons
bunker|sealed bunker|a steel door, bare concrete, a red lamp and cabinets of files
bog|moor in fog|bare heath, a lone stone wall, low fog and a distant light
shipwreck|derelict ship|rusted decks, hanging rope, tilted doors and green water in the hold
cornfield|cornfield|tall dry corn, a gap in the stalks and a lit scarecrow
cottage|village cottage|a low-ceilinged room, a dying fire, drawn curtains and a locked chest
cave|cave|wet limestone, black pools, bones and a narrow gap leading down""".split('\n')
HO_ITEM = """doll|cracked doll|a porcelain doll with a cracked cheek, glass eyes and a faded lace dress
music_box|music box|a small wooden box with a tiny ballerina frozen mid-turn and a bent key
mirror|old mirror|a tall tarnished mirror in a carved frame with a long crack
diary|diary|a water-stained leather diary with a broken lock and torn pages
photograph|photograph|a faded group photograph in which one face has been scratched out
lantern|lantern|an old oil lantern with a bent handle and a dull red glow
ouija|spirit board|a worn wooden board with letters and a heart-shaped pointer
rocking_chair|rocking chair|an old wooden rocking chair moving slowly by itself
tape_recorder|tape recorder|a heavy reel recorder with its spools turning and a handwritten label
key|rusted key|a large rusted key on a frayed ribbon
candle|candle|a thick candle burning with a green flame and dripping black wax
puppet|puppet|a worn ventriloquist dummy with a wooden jaw and painted red cheeks
telephone|ringing telephone|a black rotary telephone on a dusty table, its cord cut
book|forbidden book|a thick book bound in dark skin-like leather with a lock and faint symbols
mask|mask|a plain white mask with narrow eye holes and a single painted tear
clock|stopped clock|a tall clock with a cracked glass front and hands stopped at midnight
bed|iron bed|an iron bed frame with a stained mattress and a broken restraint strap
lamp|flickering lamp|a green-shaded lamp with a buzzing bulb that flickers
toy|toy clown|a small wind-up clown with chipped paint and a hand raised
crow|crow|a single large crow sitting on a headstone with a ring in its beak""".split('\n')
HO_POSE = P("standing perfectly still and facing the viewer; looking over a shoulder with wide eyes; holding a light up toward the dark; walking slowly down a corridor; crouching and listening; backing away with a hand out; sitting frozen on the floor; pressed against a wall; reaching toward a door handle; staring at something out of frame; running with a light swinging")
HO_SHOT = P("in a wide view with deep shadows; in a tight close-up; from low on the floor; through a doorway; through a half-open door; in a long corridor view with the figure small at the end; through a dusty window")
HO_MOOD = P("with a tense, quiet mood; with a creeping dread; with a cold, lonely mood; with a sense of being watched; with a sad, haunted mood; with an uneasy stillness")
HO_LIGHT = P("lit by a single weak lamp; lit by cold moonlight; lit by a flashlight beam; lit by flickering fluorescent tubes; lit by guttering candles; lit by a dim green glow; lit by a low red lamp; in thick fog with muted colour")
HO_HERE = P("a faint shape in the background; a door standing slightly open; a pair of wet footprints; handprints on the glass; a light flickering; a shadow that does not match anything; a chair pulled out from a table; a heavy silence")

def rows(L): return [r.split('|') for r in L]
def build(final=None):
    G = {}
    # ---- fantasy
    for k, v in (('pose', FA_POSE), ('shot', FA_SHOT), ('person', FA_PERSON), ('mood', FA_MOOD)): G['fa_' + k] = v
    sk = []; fk = []; ck = []; lk = []; ik = []
    for k, label, look, light, detail in rows(FA_STYLES):
        G['fa_style_%s_look' % k] = ['%s manner of %s, with %s' % ('the', label, look)]
        G['fa_style_%s_light' % k] = [light]; G['fa_style_%s_detail' % k] = [detail]
        G['fa_style_%s_prompt' % k] = ['A fantasy scene in the %s manner, with %s. The place is __fa_loc_look__. In it is __fa_class_look__. They are __fa_pose__. The scene has %s. Also in view is %s. It is shown __fa_shot__, __fa_mood__.' % (label, look, light, detail)]
        G['fa_style_%s_scene' % k] = ['A fantasy scene in the %s manner, with %s. The place is __fa_loc_look__. The scene has %s. Also in view is %s.' % (label, look, light, detail)]
        sk.append(k)
    for k, label, look, hab in rows(FA_FOLK):
        G['fa_folk_%s_look' % k] = ['%s %s, %s' % (A(label), label, look)]
        G['fa_folk_%s_prompt' % k] = ['The subject is __fa_folk_%s_look__, dressed as __fa_class_look__. They are __fa_pose__. Their surroundings are %s. It is shown __fa_shot__, __fa_mood__.' % (k, hab)]
        G['fa_folk_%s_portrait' % k] = ['A portrait of __fa_folk_%s_look__, in the clothes of __fa_class_look__. Behind them is %s, softly out of focus.' % (k, hab)]
        G['fa_folk_%s_short' % k] = ['__fa_folk_%s_look__.' % k]
        fk.append(k)
    for k, label, outfit, gear in rows(FA_CLASS):
        G['fa_class_%s_look' % k] = ['%s %s in %s, with %s' % (A(label), label, outfit, gear)]
        G['fa_class_%s_prompt' % k] = ['The subject is __fa_class_%s_look__. They are __fa_pose__. The place is __fa_loc_look__. It is shown __fa_shot__, __fa_mood__.' % k]
        G['fa_class_%s_short' % k] = ['__fa_class_%s_look__.' % k]
        ck.append(k)
    for k, label, look in rows(FA_LOC):
        G['fa_loc_%s_look' % k] = ['%s %s, %s' % (A(label), label, look)]
        G['fa_loc_%s_prompt' % k] = ['A fantasy scene set in __fa_loc_%s_look__. In the foreground is __fa_class_look__, __fa_pose__. It is shown __fa_shot__, __fa_mood__.' % k]
        G['fa_loc_%s_empty' % k] = ['A fantasy scene with no people in it, set in __fa_loc_%s_look__. It is shown __fa_shot__, __fa_mood__.' % k]
        G['fa_loc_%s_short' % k] = ['__fa_loc_%s_look__.' % k]
        lk.append(k)
    for k, label, look in rows(FA_ITEM):
        G['fa_item_%s_look' % k] = ['%s %s, %s' % (A(label), label, look)]
        G['fa_item_%s_prompt' % k] = ['A close view of __fa_item_%s_look__, resting on __fa_item_rest__. The scene also has __fa_item_around__.' % k]
        G['fa_item_%s_short' % k] = ['__fa_item_%s_look__.' % k]
        ik.append(k)
    G['fa_item_rest'] = P("a stone altar; a worn wooden table; a velvet cushion; a bed of moss; an iron-bound chest; a bare flagstone floor; folded dark cloth; a cracked map; a mound of coins")
    G['fa_item_around'] = P("scattered candles and wax; drifting motes of light; thick dust and cobwebs; fresh snow; a few fallen leaves; dark smoke curling upward; spilled coins; a soft blue glow")
    for p, ks in (('fa_style', sk), ('fa_folk', fk), ('fa_class', ck), ('fa_loc', lk), ('fa_item', ik)):
        for suf in ('look', 'prompt', 'short', 'scene', 'portrait', 'empty'):
            names = ['%s_%s_%s' % (p, k, suf) for k in (sk if p == 'fa_style' else fk if p == 'fa_folk' else ck if p == 'fa_class' else lk if p == 'fa_loc' else ik)]
            names = [n for n in names if n in G]
            if names: G['%s_%s' % (p, suf)] = ['__%s__' % n for n in names]
    G['fa_prompt'] = ['__fa_style_prompt__', '__fa_folk_prompt__', '__fa_class_prompt__', '__fa_loc_prompt__', '__fa_item_prompt__']
    G['fa_party_prompt'] = ['A band of adventurers stands together. On the left is __fa_class_look__. Next to them is __fa_folk_look__. Then __fa_class_look__. On the right is __fa_folk_look__. The place is __fa_loc_look__. It is shown __fa_shot__, __fa_mood__.']
    G['fa_duel_prompt'] = ['Two fighters face each other. On the left is __fa_class_look__. On the right is __fa_folk_look__. The place is __fa_loc_look__. The light is dramatic, __fa_mood__.']
    # ---- horror
    for k, v in (('pose', HO_POSE), ('shot', HO_SHOT), ('mood', HO_MOOD), ('light', HO_LIGHT), ('here', HO_HERE)): G['ho_' + k] = v
    sk = []; ek = []; ck = []; lk = []; ik = []
    for k, label, look, light, detail in rows(HO_STYLES):
        G['ho_style_%s_prompt' % k] = ['A horror scene in the %s manner, with %s. The place is __ho_loc_look__. In it is __ho_class_look__, __ho_pose__. The scene has %s. Also in view is %s. It is shown __ho_shot__, __ho_mood__.' % (label, look, light, detail)]
        G['ho_style_%s_scene' % k] = ['A horror scene in the %s manner, with %s. The place is __ho_loc_look__. The scene has %s. Also in view is %s. Nothing else moves. It is shown __ho_shot__, __ho_mood__.' % (label, look, light, detail)]
        sk.append(k)
    for k, label, look, hab in rows(HO_ENT):
        G['ho_ent_%s_look' % k] = ['%s %s, %s' % (A(label), label, look)]
        G['ho_ent_%s_prompt' % k] = ['The subject is __ho_ent_%s_look__. Its setting is %s. Far from it, small in the frame, is __ho_class_look__, who has not yet seen it. It is shown __ho_shot__, __ho_light__, __ho_mood__.' % (k, hab)]
        G['ho_ent_%s_alone' % k] = ['The subject is __ho_ent_%s_look__. Its setting is %s. Nothing else is in the frame except __ho_here__. It is shown __ho_shot__, __ho_light__, __ho_mood__.' % (k, hab)]
        G['ho_ent_%s_short' % k] = ['__ho_ent_%s_look__.' % k]
        ek.append(k)
    for k, label, outfit, gear in rows(HO_CLASS):
        G['ho_class_%s_look' % k] = ['%s %s in %s, with %s' % (A(label), label, outfit, gear)]
        G['ho_class_%s_prompt' % k] = ['The subject is __ho_class_%s_look__. They are __ho_pose__. The place is __ho_loc_look__. In the background is __ho_here__. It is shown __ho_shot__, __ho_light__, __ho_mood__.' % k]
        G['ho_class_%s_short' % k] = ['__ho_class_%s_look__.' % k]
        ck.append(k)
    for k, label, look in rows(HO_LOC):
        G['ho_loc_%s_look' % k] = ['%s %s, %s' % (A(label), label, look)]
        G['ho_loc_%s_prompt' % k] = ['A horror scene in __ho_loc_%s_look__. Present are __ho_here__ and __ho_class_look__, who is __ho_pose__. It is shown __ho_shot__, __ho_light__, __ho_mood__.' % k]
        G['ho_loc_%s_empty' % k] = ['A horror scene with no people in it, in __ho_loc_%s_look__. There is __ho_here__. It is shown __ho_shot__, __ho_light__, __ho_mood__.' % k]
        G['ho_loc_%s_short' % k] = ['__ho_loc_%s_look__.' % k]
        lk.append(k)
    for k, label, look in rows(HO_ITEM):
        G['ho_item_%s_look' % k] = ['%s %s, %s' % (A(label), label, look)]
        G['ho_item_%s_prompt' % k] = ['A close view of __ho_item_%s_look__, set in __ho_loc_look__. It is %s. There is a faint sense that something is nearby.' % (k, '__ho_light__')]
        G['ho_item_%s_short' % k] = ['__ho_item_%s_look__.' % k]
        ik.append(k)
    for p, ks in (('ho_style', sk), ('ho_ent', ek), ('ho_class', ck), ('ho_loc', lk), ('ho_item', ik)):
        for suf in ('look', 'prompt', 'short', 'scene', 'alone', 'empty'):
            names = [n for n in ('%s_%s_%s' % (p, k, suf) for k in ks) if n in G]
            if names: G['%s_%s' % (p, suf)] = ['__%s__' % n for n in names]
    G['ho_prompt'] = ['__ho_style_prompt__', '__ho_ent_prompt__', '__ho_class_prompt__', '__ho_loc_prompt__', '__ho_item_prompt__']
    G['v77_genre_entry_points'] = ['fa_prompt', 'fa_style_prompt', 'fa_folk_prompt', 'fa_class_prompt', 'fa_loc_prompt', 'fa_loc_empty', 'fa_item_prompt', 'fa_party_prompt', 'fa_duel_prompt', 'ho_prompt', 'ho_style_prompt', 'ho_ent_prompt', 'ho_ent_alone', 'ho_class_prompt', 'ho_loc_prompt', 'ho_loc_empty', 'ho_item_prompt']
    return G
if __name__ == '__main__': print(len(build()))
