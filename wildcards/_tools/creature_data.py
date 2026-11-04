"""Creature onesie vocabulary: name|colourways|hood and face|body features|hands and feet.  Adult-sized costume onesies; real and imaginary creatures."""
def P(s): return [tuple(x.strip() for x in l.split('|')) for l in s.strip().split('\n') if l.strip()]
C = {}
C['pet_farm'] = P("""
cat|grey tabby, ginger, black, white, calico, tuxedo|pointed ears, whiskers, a pink nose, big sewn eyes|a long curved tail with stripes|paw-pad mitts and paw-pad feet
dog|golden brown, black and tan, white with spots, grey|floppy ears, a snout with a black nose, a pink tongue|a wagging tail|paw mitts and paw feet
corgi|fawn and white, red and white, tricolour|large upright ears, a fox-like snout, a white blaze on the face|a tiny stub tail and a fluffy white chest|short paw feet
husky|grey and white, black and white, red and white|pointed ears, a mask-like face pattern, blue eyes|a thick curled tail|big paw mitts and feet
pug|fawn with a black mask, black, apricot|folded ears, a wrinkled brow, a flat snout|a curly tail|paw mitts and feet
poodle|white, apricot, black, pink|fluffy pom-pom ears, a topknot|a pom-pom tail|pom-pom cuffs and ankles
bunny|white, grey, cream, brown, pink|tall floppy or upright ears, a pink nose, buck teeth|a fluffy round cotton tail|paw mitts with pink pads and big bunny feet
hamster|golden, white, cream and grey|small round ears, puffed cheeks, tiny whiskers|a tiny tail and a round belly|small paw mitts and feet
guinea pig|tricolour, orange and white, black|small rounded ears, a blunt nose, a rosette fur swirl|a rounded rump|tiny paw mitts and feet
hedgehog|brown, grey, cream|a pointed snout, small round ears, a quilled fringe at the hood|a back covered in spikes of fabric quills|small paw feet
pig|pink, black and white, spotted|a round snout with nostrils, flopped ears|a curly tail|hoof mitts and hoof feet
cow|black and white, brown and white, highland tan|ears, short horns, a pink muzzle|a tail with a tufted tip and spots on the body|hoof mitts and hoof feet
sheep|white fluffy, black, cream|curled horns or soft ears, a fluffy wool face|a short woolly tail and a wool-textured body|hoof mitts and feet
goat|white, brown, grey|small horns, a beard, rectangular ears|a short upright tail|hoof mitts and feet
horse|chestnut, black, white, palomino, dapple grey|upright ears, a long snout, a mane down the hood|a long swishing tail|hoof mitts and hoof feet
donkey|grey, brown, white|very long ears, a pale muzzle, a short mane|a tufted tail|hoof mitts and feet
llama|cream, brown, white|tall banana ears, a woolly topknot|a short fluffy tail|woolly cuffs and feet
chicken|white, brown, speckled|a red comb on the hood, a beak, wattles|a feathered tail fan|feathered wings at the sides and clawed feet
duck|yellow, white, mallard green|a flat orange bill, round eyes|a small tail of feathers|webbed duck feet
""")
C['wild_mammal'] = P("""
fox|red-orange, arctic white, silver, grey|pointed ears with dark tips, a white muzzle, whisker marks|a big bushy tail with a white tip|dark paw mitts and feet
wolf|grey, black, white, brown|pointed ears, a long muzzle, a mane of fur around the hood|a thick bushy tail|claw mitts and paw feet
bear|brown, black, cinnamon, honey|small round ears, a rounded snout|a short round tail|big paw mitts with claws
panda|black and white|round black ears, black eye patches, a small nose|a short white tail|black paw mitts and feet
polar bear|white, cream|small round ears, a black nose|a short fluffy tail|big white paw mitts and feet
koala|ash grey, light grey|big fluffy round ears, a large black nose|a round tailless rump|clinging paw mitts
raccoon|grey and black, brown|a black face mask, small round ears|a ringed striped tail|dark paw mitts and feet
red panda|rusty red, cream|a white-marked face, rounded ears with white tufts|a long ringed bushy tail|dark paw mitts and feet
tiger|orange with black stripes, white tiger, golden|round ears with white spots, a striped face|a long striped tail|paw mitts with claws
lion|golden tan, tawny, white|a big golden mane around the hood, small round ears|a tail with a tufted tip|paw mitts with claws
leopard|golden with black rosettes, black panther|round ears, a spotted face|a long spotted tail|paw mitts and feet
cheetah|golden with black spots, king cheetah|small ears, black tear-marks on the face|a long spotted tail|spotted paw feet
snow leopard|pale grey with rosettes|small rounded ears, thick fur ruff|a very long thick tail|big furred paw feet
elephant|grey, pink, blue|huge floppy ears, a long trunk hanging from the hood, tusks|a small tail with a tuft|round foot pads
giraffe|yellow with brown patches|short ossicone horns on the hood, long ears, a patterned face|a thin tail with a tuft and a patchwork body|hoof mitts and feet
zebra|black and white stripes|upright striped ears, a striped mane|a tail with a tuft|hoof mitts and feet
hippo|grey, pink, lilac|small round ears on top, a wide snout|a stubby tail|round foot pads
rhino|grey, silver|a horn on the nose of the hood, small ears|a thin tail|round foot pads
kangaroo|sandy red, grey|tall ears, a pointed nose|a thick tail and a belly pouch pocket|large kangaroo feet
wombat|brown, grey|small round ears, a blunt nose|a stubby rump|short paw mitts
sloth|light brown, grey, green-tinged|a pale face with dark eye patches, tiny ears|a stubby tail|long curved claw mitts
monkey|brown, golden, grey|round ears, a pale face mask|a long curling tail|long hand mitts and foot mitts
gorilla|black, silverback grey|a heavy brow, a broad face|a rounded back|big hand mitts
orangutan|orange-red|a shaggy orange hood, a flat face|long shaggy arms|big hand mitts
lemur|grey with a ringed tail, white|big round eyes, pointed ears, a face mask|a long black-and-white ringed tail|small hand mitts and feet
bat|black, brown, purple|big pointed ears, small fangs, a snub nose|bat wings stretching from the sleeves to the sides|clawed feet
squirrel|red, grey, brown|tufted ears, big front teeth|a big fluffy curled tail|small paw mitts and feet
chipmunk|brown with stripes|round ears, stripes on the face and back, puffed cheeks|a striped tail|small paw mitts
beaver|brown|round ears, big front teeth|a flat paddle tail|webbed feet
otter|brown, cream|small round ears, whiskers, a pale muzzle|a thick tapering tail|webbed paw feet
deer|tan with white spots, brown|antlers on the hood, large ears|a short white tail|hoof mitts and feet
moose|dark brown|broad palmate antlers, a long droopy nose|a short tail|hoof mitts and feet
reindeer|brown and white, red nose|branching antlers, a red nose|a short white tail|hoof mitts and feet
bison|dark brown, shaggy|short curved horns, a shaggy beard and mane|a tufted tail|hoof mitts and feet
camel|sand, tan|small round ears, a long face, a hump on the back|a thin tail|large padded feet
meerkat|sandy, brown with dark eye patches|small round ears, dark eye patches|a thin tail|small claw mitts
skunk|black and white|small ears, a white stripe down the hood and back|a huge bushy striped tail|small paw mitts
badger|black and white, grey|a white stripe on the face|a short tail|digging claw mitts
mouse|grey, white, brown|big round ears, a pink nose, long whiskers|a long thin pink tail|small paw mitts
rat|grey, white, brown|round ears, a pointed nose|a long tail|small paw mitts
capybara|brown|small round ears, a blunt nose|no tail, a barrel-shaped body|webbed feet
armadillo|grey, pink, tan|small pointed ears, a pointed snout|banded armour plates across the back|claw mitts
anteater|grey, black and white striped|a long thin snout, small ears|a big bushy tail|long claw mitts
pangolin|brown, grey|a pointed snout, tiny ears|overlapping scale plates across the back and tail|claw mitts
tapir|black and white, brown|a short trunk-like snout, rounded ears|a short tail|round foot pads
hyena|tan with dark spots|round ears, a spotted face|a short bushy tail|paw mitts and feet
""")
C['bird'] = P("""
owl|brown, snowy white, grey, barn owl|round facial discs, big eyes, ear tufts, a beak|feathered wings and a short tail fan|talon feet
penguin|black and white, emperor with yellow neck|a beak and a white face patch|flipper wings and a small tail|orange webbed feet
flamingo|pink, coral|a curved beak, a long neck loop at the hood|feathered wings and a tail fan|long stilt-leg feet
peacock|iridescent blue and green|a crest of feathers, a beak|a huge fan of eyed tail feathers|clawed feet
parrot|red, blue and gold, green, rainbow|a curved beak, a crest|long tail feathers and wings|clawed feet
toucan|black with an orange beak|a huge colourful beak|a short tail and wings|clawed feet
eagle|brown with a white head, golden|a hooked beak, a fierce brow|large wings and a tail fan|talon feet
hawk|brown, red-tailed|a hooked beak, a streaked face|wings and a rust-red tail fan|talon feet
swan|white, black|a long neck arc and a beak at the hood|folded wings and a tail|webbed feet
chick|yellow, fluffy|a small beak, tufted fluff on the hood|small fluffy wings|orange feet
crow|black|a black beak, a glossy hood|wings and a tail fan|clawed feet
raven|black, glossy|a heavy beak, a shaggy neck ruff|wings and a wedge tail|clawed feet
hummingbird|green, iridescent|a long needle bill|small wings and a forked tail|tiny clawed feet
pelican|white, grey|a huge pouched beak|wings and a short tail|webbed feet
puffin|black and white, with an orange beak|a colourful striped beak|short wings and a tail|orange webbed feet
ostrich|grey, black and white|a small head, long eyelashes, a beak|fluffy plume wings and tail|long two-toed feet
kiwi|brown, fuzzy|a long thin beak|a round fluffy body, no tail|strong claw feet
dodo|grey, blue-grey|a large hooked beak|tiny wings and a tuft tail|stubby feet
cardinal|red|a crest, a black face mask, an orange beak|wings and a tail fan|clawed feet
rooster|red, gold, rainbow|a red comb, wattles, a beak|a sweeping tail plume|clawed feet
""")
C['reptile_amphibian'] = P("""
crocodile|green, olive, dark green|a long snout with teeth, eye bumps|a long scaly tail and back ridges|clawed feet
alligator|dark green, grey|a broad snout with teeth|a thick tail and back ridges|clawed feet
turtle|green, brown|a rounded head, a domed shell on the back|a small tail|flipper-like feet
tortoise|brown, olive|a wrinkled head, a high domed shell|a short tail|stumpy feet
frog|green, red, blue, spotted|big bulging eyes on top of the hood, a wide mouth|a plump body|webbed hand mitts and feet
toad|brown, warty green|bulging eyes, a wide mouth|a bumpy textured back|webbed feet
gecko|green, orange, blue|big eyes, a ridged brow|a long tapering tail|toe-pad feet
chameleon|rainbow, green, orange|a crest, rotating bulging eyes|a spiral curled tail|gripping feet
iguana|green, orange|a ridge of spines, a dewlap|a long spiked tail|clawed feet
snake|green, red and yellow, purple, python pattern|a snake head hood with fangs, slit eyes|a long coiled tail|a pointed tail end
axolotl|pink, wild brown, golden, blue|feathery pink gills on the hood, a smiling face|a flat finned tail|small hand and foot mitts
salamander|orange with spots, black and yellow|a wide head, bright spots|a long tail|small mitts and feet
komodo dragon|grey, brown|a forked tongue at the hood, a long snout|a thick tail|clawed feet
""")
C['sea'] = P("""
shark|grey, blue, white|a shark fin on the hood, rows of teeth|a tall back fin and a tail fin|fin feet
dolphin|grey, blue|a rounded beak snout|a dorsal fin and a fluked tail|flipper mitts
whale|blue, grey, white|a rounded head, a spout on the hood|a fluke tail|flipper mitts
orca|black and white|white eye patches|a tall dorsal fin and a fluke tail|flipper mitts
seal|grey, white, silver|big dark eyes, whiskers|a flipper tail|flipper mitts and feet
walrus|brown, tan|big tusks, a bristled muzzle|a flipper tail|flipper mitts
octopus|purple, red, pink, blue|a big bulbous hood, big eyes|eight tentacles hanging from the back and legs|sucker-dotted tentacle feet
jellyfish|pink, blue, translucent glow|a dome hood with a frilled edge|long ribbon tentacles trailing behind|ribbon feet
crab|red, orange|eye stalks, claws at the hood|big pincer claws at the hands|pincer mitts
lobster|red, blue|eye stalks, long antennae|a segmented tail fan and pincers|pincer mitts
seahorse|yellow, orange, pink|a curled snout, a crown of spikes|a curled tail|small fin mitts
starfish|orange, pink, red|five-point star shape on the hood|textured star arms|star-shaped mitts
manta ray|black and white, grey|wide wing fins, cephalic horns|a long thin tail|wing sleeves
pufferfish|yellow, brown, blue|big eyes, puffed round cheeks, small spikes|a round puffed body with spines|fin mitts
goldfish|orange, gold, white|big eyes, a gentle round mouth|a flowing split tail fin|fin mitts
clownfish|orange with white stripes|big eyes, a fish mouth|stripes and a tail fin|fin mitts
narwhal|grey, blue, white|a long spiral tusk on the hood|a fluke tail|flipper mitts
manatee|grey, brown|a round whiskered snout|a flat paddle tail|flipper mitts
sea turtle|green, brown|a rounded head, a patterned shell on the back|a small tail|flipper mitts and feet
""")
C['insect_bug'] = P("""
ladybug|red with black spots|antennae, black spotted dome shell on the hood|a spotted shell on the back|black feet
bee|yellow and black stripes|antennae, big eyes|translucent wings and a striped abdomen with a stinger|striped feet
butterfly|orange monarch, blue morpho, pink, rainbow|antennae with tips|large patterned wings on the back|slender feet
moth|brown, white, cream, grey|feathery antennae, soft furry face|dusty patterned wings|soft furry feet
dragonfly|blue, green, iridescent|huge compound eyes, antennae|four long see-through wings and a long tail|slender feet
caterpillar|green, rainbow|antennae, a rounded face|a segmented body in sections with small round feet|rounded foot pads
spider|black, red, purple|many eyes on the hood, fangs|extra arm legs at the sides|clawed feet
scorpion|brown, black, sand|claw pincers, small eyes|an upward curved stinging tail|pincer mitts
ant|black, red|antennae, round eyes|a segmented body and tail|slim feet
snail|brown, orange, pink|eye stalks on the hood|a spiral shell on the back|round foot
firefly|dark with a yellow glow|antennae, a smiling face|a glowing tail end and wings|slim feet
praying mantis|green|a triangular head, big eyes|folded spiked arms and slim wings|slim feet
beetle|black, blue, green|horns on the hood, antennae|a glossy shell and wings|clawed feet
""")
C['prehistoric'] = P("""
T. rex|green, brown, red-orange|a big toothy snout, small eyes|a heavy tail and a ridge of spikes|three-claw feet and small arms
triceratops|olive, grey, blue|three horns and a bony frill on the hood|a thick tail|big stumpy feet
stegosaurus|green, purple, orange|small head, a row of back plates|a spiked tail|stumpy feet
velociraptor|green and brown stripes, teal|a long snout, feathered crest|a long stiff tail and sickle claws|clawed feet
brachiosaurus|grey, green, blue|a very long neck drape on the hood, small head|a long tail|big round feet
pterodactyl|brown, orange, teal|a long crested beak|leathery wings spanning the arms|clawed feet
ankylosaurus|brown, green|armoured head with spikes|a clubbed tail and armour plates|stumpy feet
spinosaurus|green, blue|a long crocodile snout, a tall sail on the back|a long tail|clawed feet
woolly mammoth|brown, shaggy|long curved tusks, a long trunk, shaggy fur|a shaggy tail|furry round feet
sabre-toothed cat|tan, spotted|long sabre fangs, round ears|a short tail|big paw mitts
""")
C['mythical'] = P("""
dragon|red, green, blue, purple, gold, black|horns, a ridged snout, sewn-on spines down the hood|wings, a spiked tail and back ridges|clawed mitts and feet
unicorn|white, pastel rainbow, pink, silver|a spiral horn, a flowing mane, pointed ears|a flowing tail|hoof mitts and hoof feet
pegasus|white, silver, black|pointed ears, a flowing mane|large feathered wings and a flowing tail|hoof mitts and feet
griffin|golden, brown|an eagle head with a beak and ear tufts|feathered wings and a lion tail with a tuft|eagle talon front mitts and lion paw feet
phoenix|red, orange and gold, blue flame|a crest of flame feathers, a beak|large flame wings and long flame tail feathers|talon feet
kraken|deep teal, purple|a huge dome head, glowing eyes|long tentacles and suckers|tentacle feet
wyvern|green, brown, grey|a horned head and snout|bat-like wings on the arms and a barbed tail|two-clawed feet
sphinx|golden, sand|a headdress-like hood, a calm face|lion body, wings and a tail|big paw feet
werewolf|grey, brown, black|wolf ears, a snout with fangs, a furry mane|a bushy tail, claws and shaggy fur|claw mitts and feet
yeti|white, blue-white|a big shaggy hood, a brow ridge, tusk fangs|shaggy fur all over|huge furry feet
nine-tailed fox|orange, white, silver|fox ears, face markings|nine fluffy tails|paw mitts and feet
kitsune|white, orange|fox ears, red face markings|multiple bushy tails|paw mitts and feet
tanuki|brown, grey|round ears, a raccoon-dog face mask, a leaf on the hood|a round belly and a bushy tail|paw mitts and feet
qilin|green, gold, red|antlers, a dragon-like face, a mane|a lion tail and scale patches|hoof mitts and feet
Chinese dragon|red, gold, green|a long whiskered face, antlers, a mane|a long serpentine tail and scales|clawed mitts and feet
thunderbird|blue, gold, white|a beak, lightning feather crest|huge wings and a tail fan|talon feet
jackalope|tan with antlers|rabbit ears with antlers between them|a fluffy tail|paw mitts and feet
mermaid|teal, purple, rainbow shells|a shell crown, ear fins|a full fish tail with scales in place of legs|fin mitts and a tail fin
centaur|brown, black, palomino|a mane, pointed ears|a horse hindquarters and tail attached at the back|hoof mitts and hoof feet
cerberus|black, charcoal|three dog heads on the hood|a spiked tail and fiery mane|claw mitts and feet
basilisk|green, yellow|a crested head, a snake face|a long tail and scaled body|clawed feet
chimera|golden, red, green|a lion head with goat horns|a snake-headed tail and small wings|paw mitts and feet
hippogriff|grey, chestnut, white|an eagle head and beak|feathered wings and a horse tail|talon front mitts and hoof feet
manticore|red, orange|a lion mane, a human-like face, fangs|bat wings and a scorpion tail|paw mitts and feet
selkie|grey, silver|a seal-like face, round ears, whiskers|a flipper tail and a sleek coat|flipper mitts
kappa|green|a water dish on the hood, a beak, big eyes|a shell on the back|webbed hands and feet
naga|green, gold|a hooded cobra crest on the hood|a long snake tail|scaled mitts
garuda|red, gold|a beak, a feathered crest|large golden wings|talon feet
bigfoot|brown|a shaggy hood, a brow ridge|shaggy fur all over|huge furry feet
mothman|dark grey, black|glowing red eyes on the hood, antennae|large moth wings on the back|furry feet
chupacabra|grey-green|spined ridges on the hood, fangs, red eyes|a back of spikes and a long tail|clawed feet
Nessie|green, grey|a long neck loop and a small head on the hood|humps on the back and a long tail|flipper feet
""")
C['fantasy_original'] = P("""
fluffy horned monster|purple, blue, orange, green|two horns, big round eyes, a toothy grin|a fuzzy body and a stubby tail|big furry foot mitts
one-eyed monster|green, blue, lilac|a single big eye on the hood, tiny horns|a fuzzy round body and a tail|round furry feet
tentacled monster|purple, teal|many soft tentacles around the face, big eyes|trailing tentacles at the back|tentacle feet
cute alien|green, grey, lilac|large almond eyes, antennae|a smooth body with a small antenna tail|three-toed feet
mushroom creature|red with white dots, brown|a big spotted mushroom cap hood|a stem-like body|round foot pads
cloud creature|white, grey, pastel|a puffy cloud hood, a sleepy face|a fluffy cloud tail|puffy foot pads
cactus creature|green|a small flower on the hood, a smiling face|spiked arms and a ribbed body|round foot pads
ghost creature|white, pastel|a sheet-like hood with a wavy hem and round eyes|a wavy hem tail|floating wavy feet
slime monster|green, pink, blue|a dripping dome hood, big eyes|a puddle-like hem|round foot pads
robot critter|silver, orange, blue|antennae, round ears, a screen face|a spring tail and bolts|bolt-studded feet
imp|red, purple|small horns, pointed ears, a sly smile|a spaded tail|clawed feet
gargoyle|stone grey|horns, pointed ears, fangs|stone wings and a thick tail|clawed feet
""")
