"""Novelty / costume / historical / regional hats and funny / novelty socks (research: Wikipedia list of hat styles, novelty-sock catalogues and design articles)."""
from vocab_lib import S
NOV_HAT_RAW = """cheese-wedge hat|It is a foam wedge of cheese with holes, worn tilted on top of the head.
propeller beanie|It is a colourful panelled cap with a small spinning propeller on a stem at the top.
horned viking helmet|It is a round metal-look helmet with a nose guard and two curved horns.
jester hat|It is a floppy multi-pointed cap, each point ending in a small bell.
shark-fin hat|It is a soft cap with a tall fin on top and a toothy jaw over the forehead.
bacon-strip hat|It is a plush cap shaped like a wavy strip of bacon.
light-up LED hat|It has a band of small lights that blink in changing patterns.
drink-holder hat|It has two can holders on the sides and straws that run down to the mouth.
pizza-slice hat|It is a triangular slice of pizza with pepperoni, perched on the head.
watermelon-wedge hat|It is a half-moon wedge of watermelon with seeds, worn like a crescent.
taco hat|It is a folded taco shell stuffed with felt toppings.
pineapple hat|It is a spiky green crown of leaves on a textured golden dome.
cactus hat|It is a ribbed green column with small spines and a flower on top.
flamingo hat|It is a plush cap with a long curving neck and head on top.
unicorn hat|It is a soft hood with a spiralled horn, small ears and a flowing mane.
dinosaur hat|It is a hood with a ridge of spikes down the back and a toothed snout.
frog-eyes hat|It is a green cap with two bulging eyes on top.
cat-ears hat|It is a close cap with two pointed ears and a small face.
bunny-ears hat|It is a soft cap with two long floppy ears.
bear hat|It is a plush hood with round ears and a small snout.
fox hat|It is a hood with pointed ears and a bushy tail hanging at the back.
penguin hat|It is a knit hat with a beak, two eyes and little flipper flaps.
octopus hat|It is a bulbous cap with long dangling tentacles.
rubber-chicken hat|It is a hat with a rubber chicken lying along the top.
giant cupcake hat|It is a tall frosted cupcake with a cherry on top.
sushi hat|It is a nigiri-shaped hat with a slice of fish over a rice base.
hot-dog hat|It is a long bun with a sausage and a squiggle of mustard.
ice-cream-cone hat|It is a waffle cone upturned with three scoops stacked on top.
mullet hat|It is a baseball cap with a long wig of hair attached at the back.
wig hat|It is a hat with a tall, elaborate piled-up wig attached.
rainbow-tower hat|It is a stack of coloured rings rising high above the head.
tall striped floppy hat|It is a tall red-and-white striped stovepipe with a floppy bent top.
umbrella hat|It is an umbrella canopy on a headband.
disco-ball hat|It is a cap covered with tiny mirrored tiles that throw spots of light.
party-cone hat|It is a tall cone with a pom-pom on the top and an elastic chin strap.
foam crown|It is a squishy, oversized crown with cartoon jewels.
tinfoil hat|It is a crumpled foil cone with a pinched top.
astronaut-helmet hat|It is a clear dome with a glowing visor.
goldfish-bowl hat|It is a clear bowl with a toy fish and plastic plants.
bird's-nest hat|It is a woven nest of twigs holding a few small eggs.
tiny-house hat|It is a miniature cottage with a peaked roof and a chimney, built on a brim.
tiny-garden hat|It is a hat with a small garden of moss, flowers and a tiny watering can.
flower-pot hat|It is an upturned terracotta pot with a flower growing from it.
teacup hat|It is a floral porcelain-look cup on a saucer, worn tipped over one ear.
lampshade hat|It is a pleated fabric shade with a fringe.
stars-and-stripes top hat|It is a tall top hat with bands and stars in bold patterns.
pilgrim hat|It is a tall black hat with a buckled band and a wide brim.
pirate hat|It is a black tricorn with a skull-and-crossbones badge.
Santa hat|It is a red cap with a white fur-look trim and pom-pom.
elf hat|It is a green pointed cap with striped trim and a jingling bell.
reindeer antler hat|It has soft plush antlers hung with tiny baubles.
turkey hat|It is a plush turkey with a fan of feathers behind.
pumpkin hat|It is a round orange gourd with a stem and curling vine.
witch hat|It is a tall black cone with a crooked tip and a wide brim.
wizard hat|It is a tall pointed hat with stars and moons.
devil-horns hat|It is a cap with two red horns and a pointed tail.
angel-halo hat|It is a headband with a floating halo ring and small wings.
eyeball hat|It is a giant veined eye on top of the head.
robot-head hat|It is a boxy metal-look head with an antenna and dials.
alien-antenna hat|It is a headband with two springy antennae topped with glowing balls.
bobblehead-spring hat|It is a cap with a springy coil carrying a large toy head.
giant-bow hat|It is a huge fabric bow on a headband.
chimney hat|It is a very tall tube of red bricks with a puff of smoke.
jack-in-the-box hat|It is a box with a spring-loaded clown popping out of the top.
snow-globe hat|It is a clear dome holding a tiny winter scene with falling flakes.
volcano hat|It is a conical mountain with a crater that puffs steam.
lighthouse hat|It is a striped tower with a rotating beacon on top.
sombrero-sized party hat|It is a huge saucer brim with pom-pom fringe and a tall cone crown.
fruit-basket hat|It is a basket of plastic fruit tipped on top of the head.
cowboy-hat cooler|It is a wide hat with a built-in drink holder.
bat-wing hat|It is a dark cap with spreading leathery wings.
dragon hat|It is a scaled hood with horns, a crest and a snout.
mushroom-cap hat|It is a wide red dome with white spots.
rooster-comb hat|It is a hat with a red scalloped comb and a wattle.
moose-antler hat|It is a hat with huge branching antlers.
cow-print hat|It is a bucket hat with horns and spots.
sloth hat|It is a plush hood with a sleepy face and long arms that dangle.""".strip().split('\n')
NOV_HAT = [tuple(l.split('|')) for l in NOV_HAT_RAW]
HIST_HAT_RAW = """capotain|It is a tall, narrow-brimmed conical hat with a buckled band.
cavalier hat|It is a wide-brimmed hat with a sweeping plume.
cartwheel hat|It is a broad, flat, shallow-crowned hat tilted at an angle.
hennin|It is a tall conical headdress with a trailing veil, in medieval style.
mobcap|It is a gathered, ruffled indoor bonnet.
poke bonnet|It is a bonnet with a small crown and a deep rounded front brim.
coal-scuttle bonnet|It is a bonnet with a stiff curved brim and a flat back.
tricorne|It is a hat with the brim turned up on three sides.
bicorne|It is a large felt hat with the brim folded up at the front and back.
bycocket|It is a beaked hat with an upturned back and a feather.
smoking cap|It is a small tasselled cap embroidered with a pattern.
capirote|It is a tall, pointed, cone-shaped hat with a cloth face veil.
mortarboard|It is a flat square board on a skullcap with a tassel.
bearskin|It is a very tall cylindrical fur ceremonial cap with a chin strap.
shako|It is a tall cylindrical military cap with a plume and a badge.
toque blanche|It is a tall, white, pleated chef's hat.
Phrygian cap|It is a soft conical cap with the tip folded forward.
shtreimel-style fur hat|It is a wide, round, fur-trimmed velvet hat.
pith helmet|It is a domed, cork-like sun helmet with a puggaree band.
sou'wester|It is a brimmed oilskin rain hat, longer at the back.
peach-basket hat|It is an upturned basket shape lavishly trimmed with flowers.
sombrero|It is a tall crown on a huge saucer-shaped brim, trimmed with embroidery.
sombrero cordobés|It is a flat-crowned hat with a flat brim in Andalusian style.
montera|It is a black two-lobed cap with ears, worn by bullfighters.
chullo|It is a knit Andean hat with ear flaps and tassels.
vueltiao hat|It is a hat of woven black-and-natural palm cane braids.
ushanka|It is a fur hat with ear flaps that tie up on top.
papakha|It is a tall, shaggy sheepskin hat.
kalpak|It is a conical lambskin hat.
tubeteika|It is a small embroidered four-sided cap.
fez|It is a red felt truncated cone with a tassel.
kofia|It is a flat-topped cylindrical embroidered cap.
conical rice-straw hat|It is a wide pointed hat of woven palm leaf with a chin tie.
gat hat|It is a horsehair brimmed hat with a tall crown.
humao|It is a riding hat with fur trim and ear flaps.
jaapi|It is a woven bamboo conical hat with a decorated cloth.
Dhaka topi|It is a brimless cap in a bright geometric woven fabric.
blangkon|It is a batik-patterned cap with a knot at the back.
songkok|It is a rigid velvet cap with a flat top.
glengarry|It is a boat-shaped cap with a ribbon at the back.
Balmoral bonnet|It is a flat soft round cap with a pom-pom and ribbon.
tam o' shanter|It is a wide flat wool beret with a pom-pom.
deerstalker|It is a tweed cap with a brim at the front and back and tied ear flaps.
Tyrolean hat|It is a felt hat with a corded band and a feather brush.
barretina|It is a long floppy pull-on hat that flops over to one side.
busby|It is a tall fur cap with a coloured bag hanging at the side.
boonie hat|It is a soft cotton hat with a wide brim all around.
kepi|It is a flat-topped cap with a stiff visor.
budenovka|It is a wool cap with a pointed crown and fold-down ear flaps.
amigasa|It is a wide woven straw hat that hides the face.
jingasa|It is a flat conical lacquered hat.
tengkolok|It is a folded and tied patterned cloth headdress.
Gainsborough picture hat|It is a huge, lavishly trimmed wide-brimmed hat.
Edwardian hat|It is a large hat piled with flowers, feathers and ribbons.
cloche with feathers|It is a deep bell-shaped hat with a feather spray.
pillbox with a veil|It is a small flat-topped drum with a net veil.
fascinator|It is a small headpiece of feathers, flowers and netting on a band.
turban|It is a long cloth wound around the head in neat folds.
snood|It is a net bag that holds the hair at the back.
widow's cap|It is a plain lace-edged cap.
printer's paper hat|It is a folded newsprint hat with a point.
Robin-Hood-style cap|It is a soft pointed felt cap with a feather.
Cossack hat|It is a tall fur-trimmed hat with a cloth top.""".strip().split('\n')
HIST_HAT = [tuple(l.split('|')) for l in HIST_HAT_RAW]
GIMMICK_HAT = S("a spinning propeller on top, tiny bells that jingle with every move, a bank of blinking LED lights, a motor that makes the ears wiggle, a spring that makes the top bounce, a hidden drink straw, a squeaker that sounds when pressed, a built-in cup holder, glow-in-the-dark details, a flashing battery pack hidden inside, googly eyes that roll, a tail that swings, a detachable cape, pom-poms hanging from the edges, ears that flop, a chin strap shaped like a beard, detachable braids, hair that stands on end, a tassel that spins, long dangling tentacles, a mirrored brim, a built-in sunshade flap, smoke-effect fabric puffs, inflatable sections you can blow up, a squishy foam body, a hard shell with a printed pattern, plush fabric with a fuzzy feel, tinsel trim, glitter trim, rows of sequins that flip colour, sparkling confetti inside a clear dome, a tiny flag on a stick, a miniature windmill, a tiny trophy, a toy bird that bobs, a mini disco light, a rainbow that arcs across, a lace veil, a streaming ribbon, a long scarf attached, a built-in earmuff section, a rope strap, a feather boa trim")
NOV_SOCK_RAW = """taco socks|They show a folded taco with felt-like toppings knit along the leg.
pizza socks|They show a pizza slice with pepperoni across the ankle and cheese-pull stripes.
avocado socks|They have avocado halves with a pit at the heel.
sushi socks|They are printed with rolls and nigiri in rows.
burger socks|They stack a bun, patty, lettuce and cheese up the leg.
donut socks|They are printed with iced donuts and sprinkles.
banana socks|They are bright yellow banana peels peeling down the leg.
cactus socks|They show potted cacti with tiny pink flowers.
flamingo socks|They have long-necked flamingos standing at the ankle.
shark-fin socks|They have a raised fin at the heel and teeth at the toes.
dinosaur-spike socks|They have a row of spikes down the back of the leg.
unicorn socks|They have a horn at the toe and a flowing mane up the leg.
sloth socks|They have sleepy sloths hanging from the cuff.
cat-face toe socks|They have a cat face on the top of the foot with whiskers across the toe.
dog-ear socks|They have floppy ears on the ankle.
fox-tail socks|They have a small tail stitched at the heel.
bunny socks|They have a pair of ears at the cuff and a cotton-ball tail.
penguin socks|They have penguins sliding down snowy slopes.
bear-paw socks|They have claw-toe stitching and fuzzy pads on the sole.
animal-paw socks|They are printed to make the foot look like a furry paw.
mermaid-scale socks|They are covered in shimmering overlapping scales.
dragon-scale socks|They have rows of armored scales and a spiked cuff.
3D sculpted-food socks|They have sculpted three-dimensional food pieces knit into the surface.
3D animal-knit socks|They have raised animal faces and ears knit in relief.
mismatched crew socks|They are two socks with different designs sharing one theme.
mismatched sushi pair|They are two socks printed with two different sushi pieces.
art-inspired painting socks|They are printed with a swirling painted landscape in an expressionist style.
anatomy-illustration socks|They show labelled bones and muscles in a vintage chart style.
circuit-board socks|They are printed with green traces and tiny components.
galaxy socks|They are printed with spiral galaxies and stars.
planet socks|They are printed with the planets in a row.
rocket socks|They have rockets blasting off up the leg.
alien socks|They have green aliens and flying saucers.
retro-gaming pixel socks|They are printed with blocky pixel characters in rows.
80s fade socks|They are printed with a retro sunset gradient and grid.
holiday-lights socks|They are printed with strings of festive lights.
skeleton-bone socks|They are printed with a skeleton's foot bones, glowing in the dark.
glow-in-the-dark socks|They are printed with patterns that glow after being in the light.
light-up LED socks|They have tiny lights in the cuffs that blink.
separate-toe socks, each toe a different animal|They have five toes each knitted as a tiny animal.
pocket socks|They have a small pocket sewn at the cuff.
tassel socks|They have tassels at the cuffs.
ruffled lace-cuff socks|They have a ruffled lace cuff.
pom-pom cuff socks|They have fluffy pom-poms at the cuffs.
fishnet socks|They are open netted socks.
sheer printed socks|They are fine sheer socks with a printed pattern.
thigh-high striped socks|They rise to the upper thigh in wide stripes.
over-the-knee bow socks|They rise above the knee with a bow at each top.
knee-high socks with bows|They reach the knee with a bow at the back of each.
leg warmers|They are footless tubes of chunky knit with fold-over cuffs.
tabi split-toe socks|They have a separated big toe.
grip-paw slipper socks|They have rubber paw-pad grips on the sole.
faux-fur boot socks|They are thick, fluffy socks with a fur-look cuff.
sock-puppet-face socks|They have a mouth that opens at the toe and eyes on the top.
trompe-l'oeil shoe socks|They are printed to look like a pair of lace-up shoes.
bare-foot print socks|They are printed to look like bare feet with painted toenails.
flip-flop print socks|They are printed to look like flip-flops with tan lines.
tuxedo-shoe socks|They are printed to look like polished dress shoes with spats.
pun-without-words socks|They show a funny visual pun with no text at all.
sandwich socks|They are printed with stacked layers like a sandwich.
fruit-slice socks|They have citrus slices and berries in rows.
cow-print socks|They are printed with black patches and have pink nose-shaped toes.
leopard-print socks|They are printed with a leopard rosette pattern.
tie-dye socks|They are swirled with tie-dye.
rainbow socks|They are striped in a full spectrum.
polka-dot socks|They are printed with large polka dots.
argyle socks|They are knit in a bold argyle pattern.
camouflage socks|They are printed in a camouflage pattern.
Christmas-tree socks|They have a Christmas tree knit into the leg with decorations.
pumpkin socks|They have jack-o'-lantern faces.
Valentine-hearts socks|They are scattered with hearts of many sizes.
beach-day socks|They are printed with palm trees, shells and a sunset.
campfire socks|They are printed with a campfire, marshmallows and pine trees.
musical socks|They are printed with notes and instruments.
coffee-cup socks|They have steaming cups of coffee at the ankle.
book-lover socks|They have stacks of books and a reading cat.
gardening socks|They have watering cans, flowers and gnomes.
mushroom socks|They have toadstools in a forest floor pattern.
dice-and-cards socks|They are printed with playing cards and dice.""".strip().split('\n')
NOV_SOCK = [tuple(l.split('|')) for l in NOV_SOCK_RAW]
GIMMICK_SOCK = S("a different design on each sock, a built-in cuff that looks like a tiny cake, a raised 3D texture that you can feel, a printed hidden message on the sole, a pom-pom on each heel, fringe at the top, ears sewn onto the cuffs, a tail stitched at the back, eyes that look up from the toes, a tongue that sticks out of the toe, lenticular print that changes with the angle, glow-in-the-dark thread, reflective thread, metallic yarn, glitter yarn, heat-reactive colour change, scented fabric, a tiny zipper, buttons on the side, ribbons that tie at the ankle, fold-over cuffs showing a second pattern, a contrast heel and toe in a clashing shade, a rubberized grip pattern on the sole, a face on the sole, mini pockets for a coin, a built-in bow, sequin patches, patches of faux fur, patches of faux leather, studs along the cuff, a pearl trim, a ruffle trim, mesh panels, lace panels, ribbed bands in clashing stripes")
SOCK_THEME = S("tacos, pizza, sushi, burgers, ramen, donuts, cupcakes, ice-cream cones, popcorn, french fries, hot dogs, sandwiches, pancakes, waffles, pretzels, croissants, bananas, avocados, pineapples, strawberries, cherries, lemons, watermelons, peaches, cacti, mushrooms, sunflowers, tulips, daisies, palm trees, pine forests, mountains, waves, sunsets, rainbows, clouds, lightning, snowflakes, planets, rockets, aliens, constellations, dinosaurs, sharks, whales, octopuses, flamingos, sloths, llamas, alpacas, foxes, owls, penguins, pandas, koalas, cats, dogs, pugs, frogs, bees, butterflies, dragons, unicorns, mermaids, ghosts, skeletons, witches, robots, astronauts, pirates, ninjas, cowboys, wizards, dice, chess pieces, playing cards, video-game pixels, musical notes, guitars, vinyl records, cassette tapes, cameras, typewriters, bicycles, vintage cars, hot-air balloons, lighthouses, sailboats, anchors, compasses, maps, tea cups, coffee cups, wine glasses, cocktails, beer mugs, books, glasses, paintbrushes, scissors, keys, clocks, light bulbs, paper planes, kites, umbrellas, cupcakes with candles, presents, balloons, fireworks, hearts, stars, moons, suns, geometric shapes, stripes, checks, dots, paisley, houndstooth, camo, tie-dye, leopard spots, zebra stripes, giraffe patches, snakeskin")
