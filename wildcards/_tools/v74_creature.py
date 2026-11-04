"""v74 stage E - creature body-plan builder, hybrid builder (animal and human parts, 2 to 3 source animals) and powers/effects pieces.
Part pools are written per animal; the generator composes correlated hybrids (head of A, body of B, limbs of C ...) so a creature really has 2 to 3 sources.
Adults only for human parts. Positive visual wording only. No named creatures or franchise names (v75 adds legendary creatures on top of these builders)."""
import random, itertools
from famlib import P, slug

# name|head|body|limbs|tail|covering   (each field is a noun phrase that can follow 'with')
A = """lion|a broad head with a heavy golden mane and amber eyes|a deep muscular chest and a tucked waist|powerful forelegs with large paws and long claws|a long tail ending in a dark tuft|short tawny fur
tiger|a broad striped face with white cheek ruffs|a long muscular body with black stripes|thick forelegs with wide padded paws|a long ringed tail|orange fur with bold black stripes
wolf|a long-muzzled head with pricked ears and pale eyes|a lean deep-chested body|long sinewy legs with large paws|a bushy tail|thick grey fur with a silver ruff
bear|a heavy round head with small ears and a long snout|a huge rounded body with a shoulder hump|massive limbs with broad paws and long claws|a stubby tail|thick shaggy brown fur
horse|a long head with flared nostrils and a flowing forelock|a barrel chest and a glossy back|long slim legs ending in hard hooves|a long flowing tail|short glossy coat
stag|a head with wide branching antlers and dark liquid eyes|a slim body with a pale chest|long slender legs with split hooves|a short white tail|russet fur
bull|a thick head with wide curved horns and a ring-less nose|a massive body with a humped shoulder|thick legs with heavy hooves|a tufted tail|short coarse hide
ram|a head with great spiralling horns|a woolly stocky body|strong legs with split hooves|a small tail|thick woolly fleece
goat|a bearded head with sideways pupils and curved horns|a wiry sure-footed body|sturdy legs with split hooves|a short upright tail|rough shaggy coat
boar|a heavy head with curved tusks|a thick bristled body|short strong legs with split hooves|a thin curled tail|coarse dark bristles
elephant|a huge head with large flapping ears and a long trunk with ivory tusks|an enormous barrel body|thick pillar legs with round feet|a thin tail with a tuft|thick wrinkled grey skin
rhinoceros|a long head with a thick horn on the nose|a massive armoured body|stout legs with three-toed feet|a thin whip tail|plated grey skin
hippopotamus|a huge wide-mouthed head with tiny ears|a vast rounded body|short stocky legs|a tiny flat tail|smooth grey-brown skin
giraffe|a small head on an extremely long neck with ossicones|a tall sloping body|stilt-like legs with large hooves|a long tail with a black tuft|a patchwork coat of brown patches
camel|a long head with drooping lips and long lashes|a body with a tall hump|long legs with broad padded feet|a short tail|a shaggy tan coat
fox|a narrow face with huge ears and a white muzzle|a slim body|slender black-stockinged legs|a huge bushy tail with a white tip|russet red fur
cat|a round head with tall ears and long whiskers|a supple lithe body|soft paws with sheathed claws|a long curved tail|short sleek fur
leopard|a rounded head with a spotted face|a long sleek body|strong short legs|a long spotted tail|golden fur with dark rosettes
hyena|a heavy head with powerful jaws and rounded ears|a sloping body with a short back|long forelegs and short hind legs|a short bushy tail|coarse spotted fur
bat|a fox-like head with huge ears and a leaf-shaped nose|a small furred body|thin clawed thumbs|a thin tail membrane|soft dark fur
otter|a flat head with whiskers and small ears|a long sleek body|short webbed paws|a thick tapering tail|dense dark brown fur
rabbit|a head with very long upright ears and a twitching nose|a rounded body|powerful hind legs and small forepaws|a small white puff tail|soft grey fur
squirrel|a small head with tufted ears|a slim body|nimble paws with tiny claws|an enormous plumed tail|russet fur
mouse|a pointed head with round ears and long whiskers|a small rounded body|tiny pink hands|a long thin scaled tail|soft grey fur
monkey|a flat face with bright intelligent eyes|a slim body|long arms and gripping hands and feet|a long prehensile tail|short brown fur
gorilla|a heavy brow and a broad flat nose|a massive barrel chest|huge arms and wide hands|no tail|thick black fur
eagle|a hooked beak, a fierce golden eye and a crest of feathers|a broad feathered chest|strong yellow legs with curved talons|a fanned tail of long feathers|dense brown feathers
owl|a flat round face with huge forward-facing eyes and a tiny beak|a plump feathered body|feathered legs with sharp talons|a short rounded tail|soft barred feathers
peacock|a small head with a crown of fine feathers|a slim glossy body|thin scaly legs|a great train of eyed feathers|iridescent blue-green feathers
swan|a slender head with an orange beak|an elegant rounded body|webbed black feet|a short pointed tail|pure white feathers
crow|a sleek head with a heavy black beak|a compact black body|thin scaly legs with sharp claws|a wedge-shaped tail|oily black feathers
heron|a long head with a dagger-like beak|a slim grey body|very long thin legs|a short tail|soft grey plumage
parrot|a head with a thick curved beak and bright eyes|a bright feathered body|scaly zygodactyl feet|a long tail of coloured feathers|vivid red, blue and green feathers
snake|a smooth head with a flickering forked tongue|a long coiled muscular body|no limbs|a tapering tail|glossy patterned scales
cobra|a head with a wide spread hood and unblinking eyes|a long upright body|no limbs|a tapering coiled tail|smooth banded scales
crocodile|a long head with a toothy jaw and ridged brow|a long armoured body|short strong legs with clawed feet|a thick powerful tail|armoured scales with ridged bumps
lizard|a small triangular head with bright eyes|a long slim body|splayed legs with clawed toes|a long whiplike tail|fine scales
chameleon|a head with turret eyes and a crested casque|a laterally flattened body|gripping forked feet|a tightly curled tail|colour-shifting scales
turtle|a leathery head on a wrinkled neck|a domed shell with a patterned top|thick flippers or stumpy legs|a short stubby tail|a hard patterned shell
frog|a wide head with huge bulging eyes|a smooth squat body|long folded hind legs with webbed feet|no tail|moist smooth skin
salamander|a flat head with tiny eyes|a long soft body|stubby legs with fine toes|a long flattened tail|slick spotted skin
shark|a pointed snout with rows of triangular teeth and cold black eyes|a streamlined torpedo body|stiff pectoral fins|a tall crescent tail fin|rough grey skin
dolphin|a rounded head with a beak-like snout|a smooth streamlined body|curved flippers|a broad fluked tail|smooth grey skin
whale|an enormous head with a vast mouth|a colossal smooth body|broad paddle flippers|a huge fluked tail|smooth dark skin with barnacles
octopus|a bulbous head with intelligent horizontal pupils|a soft rounded body|eight long suckered arms|no tail|mottled colour-changing skin
squid|a streamlined head with huge eyes|a long tapering body|ten arms with two long tentacles|a pair of fins|glowing patterned skin
jellyfish|a translucent bell glowing from within|a soft dome body|long trailing stinging tentacles|no tail|clear gel-like skin
crab|a head with eyes on stalks|a broad hard flat carapace|eight jointed legs and two big claws|no tail|a spiny red shell
lobster|a head with long antennae|a segmented armoured body|large pincers and jointed legs|a flat fan tail|a hard blue-black shell
scorpion|a small head with pincers|a segmented armoured body|eight jointed legs and two large pincers|a long curved tail ending in a venomous barb|a glossy brown carapace
spider|a cluster of eight gleaming eyes and fangs|a bulbous abdomen and a small chest|eight long hairy jointed legs|no tail|a dark hairy body
beetle|a small head with strong mandibles and antennae|a domed hard wing case|six jointed legs|no tail|glossy iridescent shell
mantis|a triangular head with big compound eyes|a slim green body|folded spiked front legs|no tail|green leaf-like body
dragonfly|a head with huge compound eyes|a long slim jewelled body|six thin legs|a long thin abdomen|metallic blue body
moth|a feathery-antennaed head with soft eyes|a furry rounded body|fine jointed legs|no tail|soft dusty fur and scales
butterfly|a small head with club antennae|a slim fuzzy body|six fine legs|no tail|dusted scales
bee|a head with bulging eyes and antennae|a furry striped body|six legs with pollen baskets|a stinger|fuzzy gold and black bands
ant|a head with strong mandibles and antennae|a three-part armoured body|six slender jointed legs|no tail|glossy dark armour
centipede|a flat head with venomous fangs and antennae|a long segmented body|dozens of pairs of tiny legs|a pair of trailing legs|reddish armoured segments
snail|a head with eye stalks|a soft body under a spiral shell|a single muscular foot|no tail|a patterned spiral shell
pangolin|a small narrow head with a long snout|a rounded body|short strong legs with long claws|a long tapering tail|overlapping hard scales
armadillo|a small pointed head|a body covered in banded plates|short digging legs with big claws|a long banded tail|hard overlapping armour
hedgehog|a pointed face with bright eyes|a round body|small paws|no tail|dense sharp spines
porcupine|a blunt face with small eyes|a heavy rounded body|short legs with claws|a short tail|long banded quills
sloth|a flat face with a permanent gentle smile|a shaggy slow body|long arms with hooked claws|a stub tail|shaggy green-tinged fur
kangaroo|a long head with large ears|an upright body with a pouch|huge hind legs and small forearms|a thick strong tail|short tan fur
platypus|a flat bill and small eyes|a sleek low body|webbed feet with spurs|a flat beaver-like tail|dense brown fur
seal|a round head with large dark eyes and whiskers|a sleek blubbery body|flippers|a short tail|spotted grey fur
walrus|a wrinkled face with long tusks and bristles|a vast folded body|broad flippers|a short tail|thick wrinkled hide
penguin|a small head with a black beak|an upright oval body|stubby flippers and webbed feet|a short stiff tail|sleek black and white feathers
ostrich|a small head on a long bare neck|a round feathered body|powerful long legs with two toes|a tuft of plumes|fluffy black and white feathers
flamingo|a head with a curved beak|a slim pink body|very long thin legs|a small tail|pink feathers
pelican|a head with an enormous pouched beak|a heavy white body|short webbed legs|a short tail|white feathers
chicken|a head with a red comb and wattles|a plump feathered body|scaly legs with spurs|a high arched tail|bronze feathers
bison|a huge shaggy head with short curved horns|a massive humped body|thick legs with hooves|a tufted tail|dense dark mane and brown fur
moose|a heavy head with huge flat antlers and a drooping muzzle|a tall dark body|long legs with large hooves|a short tail|coarse dark fur
yak|a shaggy head with wide horns|a stocky long-haired body|strong legs|a bushy tail|long dark hair to the ground
koi|a broad head with whiskers and gleaming eyes|a heavy gold body|wide fins|a flowing double tail|bright red, white and gold scales
eel|a snake-like head with small eyes|a long muscular body|a continuous dorsal fin|a rounded tail|slick dark skin
seahorse|a horse-like head with a tubular snout|a curled armoured body|tiny fins|a prehensile curled tail|bony ridged skin
anglerfish|a huge mouth full of needle teeth and a glowing lure|a dark blobby body|small fins|a small tail fin|dark bumpy skin""".split('\n')
ANI = {}
for l in A:
    n, head, body, limbs, tail, cov = l.split('|'); ANI[n] = dict(head=head, body=body, limbs=limbs, tail=tail, cov=cov)

WINGS = P("great feathered eagle wings; broad owl wings with soft edges; black leathery bat wings with clawed tips; a pair of translucent dragonfly wings; large patterned butterfly wings; small hummingbird wings blurring in motion; huge swan wings; short stubby pheasant wings; iridescent beetle wing cases that open to reveal gauzy wings; thin membrane wings stretched on long finger bones; peacock-eyed wings with eyes along the edges; heavy wings with long flight feathers; delicate lacewing wings with fine veins; vast albatross wings; long tail-feather streamers along the wings")
HUMAN = dict(
 head=P("an adult woman's face with calm eyes; an adult man's weathered face with a short beard; an elderly woman's wise lined face; an adult man's strong face with a scar across the cheek; an adult woman's face with elaborate face paint; an androgynous adult's finely drawn face with pale eyes"),
 torso=P("a strong human torso with broad shoulders; a slender human torso; a muscular athletic human chest; a soft rounded human torso; a lean human torso with prominent ribs"),
 arms=P("human arms and hands with long fingers; strong human arms with scarred knuckles; slender human arms with delicate hands; thick human forearms with rough hands"),
 legs=P("human legs with bare feet; strong human legs with calloused feet; long slender human legs; muscular human thighs and calves"),
)
BODY_PLAN = P("four-legged and low-slung; four-legged and tall at the shoulder; upright on two legs; centaur-like with a human upper body on a four-legged lower body; serpentine with no legs at all; six-legged and insectoid; eight-legged and spider-like; winged and four-legged with a long tail; winged and two-legged like a bird; aquatic with fins and a long body; many-limbed and tentacled; a coiled body with a raised head; a long body on many short legs; a bipedal body with a long balancing tail; a floating body trailing tendrils; a four-legged body with two extra arms at the shoulders")
SIZE = P("the size of a house cat; the size of a large dog; the size of a horse; the size of a bus; the size of a house; as tall as a tree; small enough to sit on a hand; vast enough to block a valley")
POSE = P("rearing up on its hind legs; crouched low and ready to spring; standing calm and watchful; coiled around a boulder; perched on a ledge; stalking forward with its head low; resting curled up with its head on its paws; roaring with its head thrown back; looking directly at the viewer; walking with a slow heavy tread; lying in the sun with its eyes half closed")
POSE_HUM = P("standing calm and watchful; striding forward with a heavy tread; crouched low and ready to spring; seated on a stone with its hands on its knees; looking directly at the viewer; arms raised and roaring; leaning on a tall staff; walking slowly with its head low")
POSE_WING = P("perched on a ledge with its wings half open; flying low over the ground with its wings spread; diving with its wings folded back; landing with its wings flaring wide; resting with its wings folded around its body; rising into the air with a downward beat of its wings")
EYES = P("amber eyes with slit pupils; glowing gold eyes; round black eyes like polished stones; pale blue eyes with an intelligent stare; many small eyes in a ring; a single large eye in the centre of the forehead; deep red eyes; large soft brown eyes; white eyes with no pupils; compound eyes like faceted jewels")
FEATURE = P("a crest of long spines along the spine; a pair of curved horns; a ruff of feathers around the neck; a mane of flowing hair; bony plates along the back; a frill that spreads around the head; long whiskers like fine wires; a row of small glowing spots along the flanks; a set of tusks curving up from the jaw; a patch of bright colour on the throat; a bony crest on the skull; a fringe of tendrils around the jaw; markings like old scars; a ring of bony spikes around the neck")
HAB = P("a misty forest clearing; a rocky mountain ledge; a dark cave mouth; a reedy marsh at dawn; a windswept moor; a coral reef shallows; a sunlit meadow; a frozen lake; a desert of red dunes; a ruined stone courtyard; a canyon at sunset; a jungle river bank; a snow-covered pine wood; a night sky above a hill")

WINGED = ['eagle', 'owl', 'peacock', 'swan', 'crow', 'heron', 'parrot', 'bat', 'dragonfly', 'moth', 'butterfly', 'bee']
def an(w): return ('an ' if w[0] in 'aeiou' else 'a ') + w
def build(final=None):
    G = {}; r = random.Random(740); names = list(ANI)
    G['cb_body_plan'] = BODY_PLAN; G['cb_size'] = SIZE; G['cb_pose'] = POSE; G['cb_pose_winged'] = POSE_WING; G['cb_pose_human'] = POSE_HUM; G['cb_eyes'] = EYES; G['cb_feature'] = FEATURE; G['cb_habitat'] = HAB; G['cb_wings'] = WINGS
    G['cb_animal_names'] = names
    for part in ('head', 'body', 'limbs', 'tail', 'cov'):
        G['cb_%s' % ('covering' if part == 'cov' else part)] = ['%s (%s)' % (ANI[n][part], n) if False else ANI[n][part] for n in names]
    for k, v in HUMAN.items(): G['cb_human_' + k] = v
    # single-animal builder: every part from one animal (a base creature)
    for n in names:
        a = ANI[n]; s = slug(n)
        G['cb_one_%s' % s] = ['%s, %s, %s, %s, %s and %s' % (an(n), a['head'], a['body'], a['limbs'], a['tail'], a['cov'])]
    G['cb_one'] = ['__cb_one_%s__' % slug(n) for n in names]
    # correlated hybrids with 2 or 3 source animals
    two = []; three = []; human = []
    for _ in range(900):
        a, b = r.sample(names, 2)
        two.append('a hybrid creature with the head of %s (%s), set on the body of %s (%s, %s, %s)' % (an(a), ANI[a]['head'], an(b), ANI[b]['body'], ANI[b]['limbs'], ANI[b]['cov']))
    for _ in range(900):
        a, b, c = r.sample(names, 3)
        three.append('a chimera with the head of %s (%s), the body and limbs of %s (%s, %s), and the tail of %s (%s) and the covering of %s (%s)' % (an(a), ANI[a]['head'], an(b), ANI[b]['body'], ANI[b]['limbs'], an(c), ANI[c]['tail'], an(a), ANI[a]['cov']))
    for _ in range(700):
        a, b = r.sample(names, 2); hp = r.choice(['head', 'torso', 'arms', 'legs'])
        k = r.randrange(5)
        if k == 0: human.append('a creature with the human torso, arms and face of an adult rising from the four-legged body of %s, %s and %s' % (an(b), ANI[b]['body'], ANI[b]['limbs']))
        elif k == 1: human.append('an adult human body with the head of %s, %s' % (an(a), ANI[a]['head']))
        elif k == 2: human.append('an adult human figure with the lower body of %s, %s, and the human upper body above it' % (an(b), ANI[b]['limbs']))
        elif k == 3: w = r.choice(WINGED); human.append('a figure with human arms and legs, the head of %s (%s) and the wings of %s' % (an(a), ANI[a]['head'], an(w)))
        else: human.append('a creature with a human face set into the head of %s, %s and the body and covering of %s, %s' % (an(a), ANI[a]['head'], an(b), ANI[b]['cov']))
    G['cb_hybrid_two'] = list(dict.fromkeys(two)); G['cb_hybrid_three'] = list(dict.fromkeys(three)); G['cb_hybrid_human'] = list(dict.fromkeys(human))
    G['cb_hybrid_any'] = ['__cb_hybrid_two__', '__cb_hybrid_three__', '__cb_hybrid_human__']
    # fully random per-part (loose hybrid)
    G['cb_loose_hybrid'] = ['a creature, __cb_head__, __cb_body__, __cb_limbs__, __cb_tail__ and __cb_covering__']
    G['cb_with_wings'] = ['a winged creature, __cb_head__, __cb_body__, __cb_limbs__, __cb_wings__, __cb_tail__ and __cb_covering__']
    G['cb_prompt'] = ['__cb_prompt_one__', '__cb_prompt_two__', '__cb_prompt_three__', '__cb_prompt_human__', '__cb_prompt_winged__']
    G['cb_prompt_one'] = ['The subject is __cb_one__. It is __cb_size__ and it has __cb_feature__. It is __cb_pose__ in __cb_habitat__.']
    G['cb_prompt_two'] = ['The subject is __cb_hybrid_two__. It is __cb_size__, with __cb_eyes__ and __cb_feature__. It is __cb_pose__ in __cb_habitat__.']
    G['cb_prompt_three'] = ['The subject is __cb_hybrid_three__. It is __cb_size__, with __cb_eyes__ and __cb_feature__. It is __cb_pose__ in __cb_habitat__.']
    G['cb_prompt_human'] = ['The subject is __cb_hybrid_human__. It is __cb_size__, with __cb_eyes__ and __cb_feature__. It is __cb_pose_human__ in __cb_habitat__.']
    G['cb_prompt_winged'] = ['The subject is __cb_with_wings__. It is __cb_size__, with __cb_eyes__ and __cb_feature__. It is __cb_pose_winged__ in __cb_habitat__.']
    G['cb_short'] = ['__cb_hybrid_any__']
    G.update(build_powers())
    G['v74_creature_entry_points'] = ['cb_prompt', 'cb_prompt_one', 'cb_prompt_two', 'cb_prompt_three', 'cb_prompt_human', 'cb_prompt_winged', 'cb_short', 'pw_prompt', 'pw_person_prompt', 'pw_scene_prompt']
    return G

# ---------------------------------------------------------------- powers and effects (positive visual descriptions)
SRC = P("from an open palm; from the tip of a raised staff; from both hands pressed together; from the eyes; from the chest through the clothing; from the barrel of a handheld device; from the point of a drawn sword; from a clenched fist swung forward; from the mouth in a long exhale; from the fingertips as they trace a pattern in the air; from the ground at the feet; from a wand held steady; from the forehead; from the back where wings of light unfold")
POW = {
 'fire magic': dict(form=P("a rolling ball of flame; a spiralling jet of fire; a fan of burning feathers; a wall of fire rising from the ground; a stream of sparks and embers; a sphere of white-hot flame; a coil of flame like a snake"), colour=P("orange and yellow with white cores; deep red with black smoke; blue-white; molten gold; crimson with violet edges"), motion=P("leaping and licking upward; sweeping across in a wide arc; bursting outward in a ring; pulling in on itself and then exploding"), env=P("the air above shimmering with heat; scorched ground in a ring; sparks drifting upward; the walls lit orange; shadows leaping wildly; leaves curling and glowing at the edges")),
 'ice magic': dict(form=P("a spray of icy shards; a spiralling blast of frost; a growing lattice of crystals; a wall of jagged ice; a swirl of snow and cold mist; a spear of ice; a ring of frozen petals"), colour=P("pale blue and white; glassy teal; silver-blue with sparkles; deep indigo with white frost"), motion=P("spreading outward across the surface; shooting in a straight line; spinning slowly in the air; freezing everything it touches in a creeping wave"), env=P("frost forming on every surface; breath turning to white clouds; a fine dust of snow in the air; icicles growing downward; a layer of ice across the ground")),
 'lightning magic': dict(form=P("a branching bolt of lightning; a crackling sphere of electricity; a web of arcs between two hands; a chain of bright sparks; a storm of forked lightning above; a coil of electricity around the arm"), colour=P("electric blue-white; violet with white cores; yellow-white; neon cyan with magenta fringes"), motion=P("snapping across the gap in an instant; jittering and branching wildly; looping and crackling around the body; striking down from above in a flash"), env=P("hair lifting with static; a bright flash lighting the whole scene; ground scorched in branching patterns; small sparks jumping between metal objects; a faint smell-of-ozone haze in the air")),
 'light and holy magic': dict(form=P("a radiant beam of golden light; a halo of rays behind the head; a dome of soft white light; a shower of glowing petals; a shining circle of runes; a column of light from the sky; wings of pure light"), colour=P("warm gold and white; soft pearl and pink; bright sunlit white; pale gold with rainbow edges"), motion=P("rising slowly and gently; expanding outward in a slow ring; pouring down in a steady stream; shimmering and pulsing like a heartbeat"), env=P("everything bathed in a soft glow; shadows lifting away; dust motes glittering in the beams; flowers opening nearby; a clear bell-like stillness")),
 'shadow magic': dict(form=P("tendrils of darkness reaching outward; a swirling cloak of shadow; a sphere of absolute black; a pool of darkness spreading on the ground; claws of shadow rising from the floor; a veil of smoke-like darkness"), colour=P("deep black with violet edges; ink-black with faint blue glints; charcoal with sickly green flecks; shadow with crimson eyes inside"), motion=P("creeping slowly and silently; whipping out suddenly; swirling around the figure in a spiral; swallowing the light as it expands"), env=P("nearby lights dimming; candle flames bending toward it; the air cold and still; shadows lengthening in impossible directions; a faint violet glow at the edges")),
 'nature magic': dict(form=P("vines bursting from the ground; a blooming ring of flowers; roots rising to form a wall; a swirl of green leaves; a stream of glowing seeds; branches growing from the arms; a tree sprouting at speed"), colour=P("fresh spring greens and gold; deep forest green with pink blossoms; autumn red and amber; glowing green with white light"), motion=P("growing upward at visible speed; unfurling slowly like a time-lapse flower; twisting around an object; sweeping across the ground in a wave"), env=P("grass springing up where it passes; petals drifting through the air; moss spreading over stones; birds and insects gathering; a warm smell of rain on earth")),
 'water magic': dict(form=P("a ribbon of water spiralling in the air; a wave rising from nothing; a ring of floating droplets; a whip of water; a sphere of swirling water; a rain cloud forming above the hand; a bubble shield"), colour=P("clear blue-green with white foam; deep sea blue with silver highlights; crystalline turquoise; dark stormy teal"), motion=P("flowing in a smooth curve; rising in a graceful arch; crashing forward in a rush; spinning in slow circles"), env=P("mist drifting across the ground; puddles forming on the floor; droplets glittering in the light; ripples spreading in the air; fine rain falling nearby")),
 'wind magic': dict(form=P("a spiral of howling wind; a ring of whirling leaves; a gust that bends everything outward; a tornado forming from the palm; a flowing ribbon of cloud; blades of cutting air"), colour=P("pale silver-white; faint grey-blue; translucent grey-white with swirling leaves and dust; sky blue with white streaks"), motion=P("spinning in a tight spiral; blasting outward in a wide gust; swirling upward in a column; sweeping low across the ground"), env=P("clothes and hair whipped sideways; leaves, paper and dust caught in the flow; trees bowing; a cloud of dust racing outward; flags snapping taut")),
 'earth magic': dict(form=P("a rising wall of stone; a fist of rock lifting from the ground; a ring of floating boulders; a crack opening in the earth; crystals thrusting from the ground; a wave of rising soil; a stone armour forming over the body"), colour=P("brown and grey with amber glints; dark stone with glowing orange veins; green moss over grey rock; sandy gold with sparkling crystal"), motion=P("rising slowly and heavily; thrusting up in a sudden burst; rolling forward as a wave of ground; shattering and re-forming"), env=P("dust and pebbles rising from the ground; the floor cracking; a low rumble; shaking dust from the rafters; small stones dancing in the air")),
 'arcane magic': dict(form=P("a ring of glowing runes in the air; a floating sigil of interlocking lines; a spinning circle of symbols; a thread of light drawing a pattern; a sphere of crackling coloured energy; a book of floating pages; a lattice of glowing lines"), colour=P("violet with silver lines; electric blue and magenta; glowing teal and gold; rainbow shifting colours"), motion=P("rotating slowly in layers; drawing itself in a rush of lines; pulsing in time with a hum; unfolding like a flower"), env=P("floating particles of light; the air humming faintly; objects lifting a little from tables; the glow reflected on every surface; ghostly letters in the air")),
 'energy beam': dict(form=P("a thick beam of bright energy; a narrow piercing ray; a twisting double beam; a pulsing stream of energy; a wide sweeping beam; a cone of radiant energy; a bolt of plasma"), colour=P("hot cyan with a white centre; red with a bright white core; vivid green; magenta-pink; yellow-orange; deep violet"), motion=P("firing in a straight line to the target; sweeping across in a wide arc; pulsing in rapid bursts; widening as it travels"), env=P("a bright glow lighting the faces; the target glowing white where it strikes; sparks flying from the impact; a ring of heated air; lens flares at the source")),
 'ray gun fire': dict(form=P("a bolt of coloured light leaving a retro ray pistol; a burst of rapid laser fire from a rifle; a glowing plasma bolt trailing sparks; a blue beam from a heavy cannon; a ring of red pulses from a handheld device; a spread of bright darts"), colour=P("bright red pulses; electric blue lines; lime green bolts; magenta and white; orange plasma"), motion=P("streaking toward the target in a straight line; fired in rapid sequence; arcing in a slow curve; spreading in a fan"), env=P("glowing muzzle with a cloud of vapour; the walls flickering in colour; bright impact sparks on the target; tiny bits of molten metal flying; scorch marks on the wall")),
 'force field': dict(form=P("a shimmering dome of light around the figure; a flat glowing shield with a hexagon pattern; a ring of soft light; a translucent wall; a sphere with ripples spreading from an impact; a barrier of glowing lines"), colour=P("pale blue with white ripples; clear gold; translucent green with hexagon cells; rose pink with sparkles"), motion=P("rippling outward from the point of impact; humming gently with soft pulses; flickering as it takes a hit; expanding to full size in an instant"), env=P("sparks sliding off the surface; objects deflected and falling; the air shimmering faintly; reflections curving across it; dust swirling at its edge")),
 'aura': dict(form=P("a glowing outline around the whole body; a wavering flame-like aura; a halo of floating sparks; a swirling cloud of coloured mist; a rising column of light; ethereal wings of energy"), colour=P("gold and white; blazing red; electric blue; green with white sparks; violet with silver; pure white"), motion=P("flickering and rising like flame; pulsing slowly with each breath; whipping upward in strong waves; surging outward in bursts"), env=P("hair and clothing floating upward; the ground trembling; small stones rising; a ring of dust racing out; light shining on every nearby surface")),
 'transformation': dict(form=P("a body mid-change with fur spreading across the skin; limbs lengthening into claws; skin turning to scales in rippling waves; wings unfolding from the back; the face shifting between human and beast; bones rising under skin as horns; the body glowing as it reshapes; feathers sprouting along the arms"), colour=P("warm gold light from within; white mist; silver patterns across the skin; cool blue light; bright flashing flickers of colour"), motion=P("in the middle of the change, caught between two forms; changing slowly with strain; collapsing and reforming in an instant; rippling from the head down"), env=P("clothing straining and tearing; a swirling cloud of light around the body; the surroundings darkening; leaves and dust spinning upward; a faint low tone in the air")),
 'telekinesis': dict(form=P("objects floating in a slow orbit around a figure; a heavy boulder lifted with an outstretched hand; a rain of small items hanging in the air; a stream of books flying through the room; a car held off the ground; a ring of rippling air in front of the hand"), colour=P("faint blue-white distortion; pale gold glow at the fingertips; soft violet halos; a clear ripple in the air"), motion=P("rising in perfect stillness; spinning slowly in place; flung outward all at once; suspended in a frozen instant"), env=P("dust hanging motionless; hair floating; papers lifting and fluttering; shadows stretching; shattered glass hanging in the air")),
 'portal and teleport': dict(form=P("a circular gateway of swirling light; a tear in the air with glowing edges; a doorway of sparks in mid-air; a spiral vortex opening in the ground; a pillar of light with a figure fading in it; a mirror-like surface standing in the air; a ring of runes with a glowing centre"), colour=P("violet and white with a black centre; electric blue; gold with orange edges; rainbow shimmer; emerald with a bright core"), motion=P("opening slowly like an eye; swirling quickly; closing with a flash; pulsing at the edges as something steps through"), env=P("loose papers and leaves pulled toward it; hair blown toward the opening; scattered sparks; a glowing reflection on the floor; a faint view of another place inside")),
 'healing and restoration': dict(form=P("soft green light flowing from the hands into a wound; a ring of floating petals around a figure; a gentle golden glow spreading over a body; sparkles drifting from a staff; a pool of warm light on the ground; a luminous mist around a sleeping figure"), colour=P("soft green and gold; warm pearl-white; pale pink and white; light aqua"), motion=P("flowing gently like water; pulsing slowly; rising like warm steam; drifting in a spiral"), env=P("a calm stillness in the air; flowers blooming at the feet; a soft warm glow on the faces; bruises fading; dust glittering in the light")),
 'illusion and invisibility': dict(form=P("a figure fading to a faint shimmer in the air; a double image that separates from the body; a distortion like heat haze in the shape of a person; a mirage of a grand hall over an empty field; a hall of mirrors with different versions; a cloak of shifting colours blending with the wall"), colour=P("transparent ripple with a thin blue edge; ghostly white outline; shifting pattern copying the background; faint silvery edges"), motion=P("flickering between visible and invisible; drifting apart from the body; dissolving from the edges inward; shimmering as it moves"), env=P("a faint distortion of the background behind it; footprints appearing in dust with no one visible; a ripple in the puddles; blurred and doubled reflections")),
 'time and gravity distortion': dict(form=P("water drops frozen in the air around a figure; a ring of warped space with stretched light; a clock face of light spinning backwards; a field where objects drift upward; a ripple of stretched lines; a figure leaving trails of afterimages"), colour=P("pale blue and silver; stretched rainbow edges; sepia and gold ghost images; deep purple with white lines"), motion=P("slowed to a crawl; spinning backward; stretching and pulling toward a point; floating gently upward"), env=P("dust hanging in the air; debris drifting slowly; light bending around the effect; clocks and gears hanging in the air; hair floating upward")),
 'summoning': dict(form=P("a glowing circle on the floor with a shape rising from it; a pillar of fire from which a figure steps; a swirling mist forming a creature; a tear in the ground with hands reaching up; a spiral of light drawing a spirit down; a flock of spectral birds rising from a book"), colour=P("violet with silver circle lines; red with black smoke; ghostly white-blue; bright gold with white feathers"), motion=P("slowly materialising from the centre; bursting upward in a flash; spiralling inward then outward; emerging through the circle step by step"), env=P("candle flames leaning toward the circle; chalk lines glowing; a cold wind from the centre; floating sparks; shadows pointing the wrong way")),
 'curse and dark energy': dict(form=P("a veil of black threads crawling over a figure; glowing sickly green runes burning on the skin; a spiralling cloud of dark smoke; tendrils of dark purple reaching from a hand; a black flame that gives off no heat; creeping cracks of dark light across the floor"), colour=P("sickly green and black; violet-black with red sparks; deep crimson on black; ash grey with green glints"), motion=P("creeping slowly along the ground; coiling around the target; pulsing like a heartbeat; spreading in an ever-widening ring"), env=P("flowers wilting nearby; frost on the walls; candle flames shrinking to blue; shadows moving on their own; a thin mist clinging to the floor")),
}
def build_powers():
    G = {}; keys = []
    G['pw_source'] = SRC
    for k, d in POW.items():
        s = slug(k); keys.append(s)
        for part, v in d.items(): G['pw_%s_%s' % (s, part)] = v
        G['pw_%s_prompt' % s] = ['%s %s' % (k.capitalize() if False else 'The effect is ' + k + ', showing', '__pw_%s_form__, coming __pw_source__. Its colour is __pw_%s_colour__. It is __pw_%s_motion__. Around it, __pw_%s_env__.' % (s, s, s, s))]
        G['pw_%s_short' % s] = ['__pw_%s_form__, in __pw_%s_colour__.' % (s, s)]
    G['pw_names'] = list(POW)
    G['pw_prompt'] = ['__pw_%s_prompt__' % s for s in keys]
    G['pw_short'] = ['__pw_%s_short__' % s for s in keys]
    G['pw_person_prompt'] = ['__pw_person_who__ The person is using a power in __cb_habitat__. __pw_prompt__']
    G['pw_person_who'] = ['__f_create_random_woman_w_clothes_short__', '__m_create_random_man_w_clothes_short__', '__any_create_random_androgynous_person_w_clothes_short__']
    G['pw_scene_prompt'] = ['A dramatic scene in __cb_habitat__. __pw_prompt__ A creature, __cb_hybrid_any__, faces it.']
    G['pw_magic_prompt'] = ['__pw_%s_prompt__' % s for s in keys if s.endswith('_magic')]
    G['pw_tech_prompt'] = ['__pw_%s_prompt__' % s for s in ('energy_beam', 'ray_gun_fire', 'force_field')]
    return G
