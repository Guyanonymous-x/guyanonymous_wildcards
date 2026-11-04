"""v46 data: seats, lying surfaces, leaning supports, poses by support, interactions."""
from v40_data_a import E
SEAT = E("""
low wooden stool|a round-topped three-legged stool about knee height with plain turned legs|pine; oak; beech
tall bar stool|a tall stool with a round padded seat, a ring footrest and four slim legs|steel and leather-look vinyl; wood
dining chair|a four-legged chair with a straight back, a flat seat and square-cut legs|oak; pine; beech
cushioned armchair|a deep chair with padded arms, a high back and a thick seat cushion|woven fabric; leather
wooden bench|a long plank seat on two sturdy trestle legs, seating two or three people|oak; pine; teak
park bench|a long bench with a slatted seat, a slatted back and cast metal ends|iron and wood
three-seat sofa|a long upholstered seat with a padded back, two rolled arms and three loose cushions|fabric; leather; velvet
loveseat|a small two-person sofa with a tall back and two arms|fabric; velvet
floor cushion|a large square flat cushion for sitting on the floor with a zip cover|cotton; wool
bean bag|a large soft bag filled with beads that moulds to the sitter|canvas; faux leather
rattan chair|a round-backed chair woven from cane with a flat woven seat|rattan; cane
folding camp chair|a light folding chair with a fabric seat and back on a foldable metal frame|nylon and steel
rocking chair|a wooden chair with curved runners under the legs, a high back and slim arms|walnut; oak
swing seat|a flat wooden board hanging on two ropes from a branch or a frame|wood and rope
porch swing|a bench hung by chains from a porch beam, with a slatted seat and back|painted wood
hammock chair|a seat of woven rope hung from a single ring|cotton rope
wicker garden chair|a chair with a curved woven back, woven arms and a soft cushion|wicker
metal café chair|a light chair with a thin round seat, a curved back and four thin legs|painted steel
wooden crate seat|an upturned wooden crate with open slats|pine
rock slab|a flat grey stone slab, waist height, with a smooth worn top|stone
tree stump|a short cut tree trunk with a flat top and visible growth rings|wood
tatami cushion seat|a flat square cushion on a woven straw mat|cotton; straw
office chair|a swivel chair with a padded seat, a mesh back, arms and a five-star base on wheels|mesh and plastic
wheelchair|a seat on two large wheels with handrims and two small front wheels, a back and arm rests|steel and fabric
""")
LIE = E("""
double bed|a wide bed with a fitted sheet, a duvet and two pillows on a wooden frame|cotton; linen
single mattress on the floor|a thin mattress with a plain fitted sheet laid flat on the floor|cotton
yoga mat|a thin rolled-out rectangular mat with a grippy surface|rubber; foam
beach towel|a large flat towel laid on sand, in bold stripes|cotton
picnic blanket|a large square blanket spread on grass, in a check pattern|wool; cotton
hammock|a long woven cloth hung between two trees or posts, sagging in the middle|cotton; nylon
daybed|a single bed with a back and arms, used as a sofa, with a thick cushion|wood and fabric
chaise longue|a long reclining seat with a raised head end and a curved back|velvet; leather
sun lounger|a long adjustable reclining seat with a slatted frame and a padded cushion|wood; plastic
sofa (lying)|a long upholstered sofa with a flat cushion for lying along|fabric
grass lawn|a short, even green lawn|grass
rug|a woven rectangular rug on a floor|wool; jute
massage table|a padded narrow table with a face hole and a clean sheet|vinyl and cotton
""")
LEAN = E("""
brick wall|a tall wall of red bricks with pale mortar lines|brick
painted plaster wall|a smooth wall painted in a flat colour|plaster
wooden railing|a waist-high railing with a flat top bar and vertical posts|wood
metal railing|a thin round metal rail on short posts|steel
tree trunk|a thick rough-barked tree trunk|wood
door frame|the wooden frame of an open doorway|wood
wooden fence|a fence of tall upright boards|wood
rock face|a tall rough natural stone face|stone
kitchen counter edge|the rounded edge of a waist-height counter|laminate; stone
stone pillar|a thick round pillar, floor to ceiling|stone
ship's rail|a metal rail along the edge of a deck|steel
window sill|the wide ledge of a window with a view|wood; stone
lamp post|a tall metal pole with a lamp at the top|cast iron
bar counter|a long polished counter, chest height|wood
""")
# pose by support: base forms
SIT_GROUND = ['sitting cross-legged on the floor', 'sitting on the ground with knees drawn up and arms around them', 'sitting on the ground with legs stretched out in front', 'sitting on the ground with legs folded to one side', 'kneeling and sitting back on the heels', 'sitting on the ground leaning back on both hands', 'squatting low on the heels', 'sitting on the ground with one knee up and an arm resting on it', 'sitting in a straight, upright posture on the floor with a long spine', 'sitting on the ground with the legs crossed at the ankles']
SIT_SEAT = ['sitting upright on {S}, hands resting on the thighs', 'sitting on {S} with legs crossed at the knee', 'sitting on {S}, leaning forward with elbows on the knees', 'sitting on {S}, leaning back relaxed', 'sitting on {S} with feet flat on the floor and hands in the lap', 'sitting sideways on {S} with one arm over the back', 'sitting on {S} with one ankle resting on the opposite knee', 'sitting on the edge of {S} with the weight forward', 'sitting on {S} with legs stretched out in front', 'sitting on {S} with the chin resting on one hand']
LIE_GROUND = ['lying flat on the back on the ground with arms by the sides', 'lying on the side on the ground with the head propped on a hand', 'lying face down on the ground with arms folded under the chin', 'lying on the back on the floor with knees bent', 'lying curled on one side on the ground', 'lying on the back on the ground with arms stretched above the head']
LIE_SURF = ['lying flat on the back on {S}', 'lying on the side on {S} with the head propped on a hand', 'lying face down on {S} with arms folded under the chin', 'lying on the back on {S} with knees bent', 'lying curled on one side on {S}', 'lying on {S} propped up on both elbows', 'lying on the back on {S} with one arm behind the head']
LEAN_FREE = ['leaning slightly forward with weight on the front foot', 'leaning back with the weight on the heels', 'leaning to one side with a hand on the hip', 'leaning into a stride with the torso tilted', 'leaning forward with hands on the knees']
LEAN_SUP = ['leaning back against {S} with arms crossed', 'leaning with one shoulder against {S} and hands in pockets', 'leaning with both elbows on {S}', 'leaning against {S} with one foot up behind', 'leaning on {S} with one hand resting on it', 'leaning against {S} with the head tilted back']
FLOAT = ['floating on the back in calm water with arms spread', 'floating upright in water with arms drifting', 'swimming forward with outstretched arms', 'floating weightless with limbs loosely curled', 'diving headfirst with arms pointed ahead', 'floating face-up weightless with hair drifting', 'mid-jump with the knees tucked high', 'mid-leap with arms flung wide']
TWO = ['the person on the left and the person on the right are hugging', 'the person on the left hands an object to the person on the right', 'the person on the left whispers into the ear of the person on the right', 'the person on the left and the person on the right are walking side by side, talking', 'the person on the left and the person on the right are laughing together', 'the person on the left leans their head on the shoulder of the person on the right', 'the person on the left and the person on the right stand back to back with arms folded', 'the person on the left and the person on the right hold hands', 'the person on the left helps the person on the right to stand up', 'the person on the left and the person on the right face each other in conversation', 'the person on the left points toward something while the person on the right looks', 'the person on the left tucks a stray lock of hair behind the ear of the person on the right', 'the person on the left and the person on the right shake hands', 'the person on the left carries the person on the right on their back', 'the person on the left and the person on the right dance close together', 'the person on the left and the person on the right toast with raised cups']
TWO_SEAT = ['the person on the left and the person on the right sit side by side on {S}', 'the person on the left sits on {S} while the person on the right stands beside them', 'the person on the left and the person on the right sit across from each other, each on {S}, talking']
THREE = ['the person on the left, the person in the middle and the person on the right stand shoulder to shoulder with arms around each other', 'the person on the left and the person on the right look at the person in the middle, who is speaking', 'the three people walk in a line, the person in the middle slightly ahead', 'the person in the middle sits low while the person on the left and the person on the right stand behind', 'the three people stand in a loose triangle, laughing', 'the person on the left and the person on the right hold the hands of the person in the middle', 'the three people lean in together over something held by the person in the middle', 'the three people stand in a row, each looking in a different direction', 'the person in the middle raises both arms while the others applaud', 'the three people bow together toward the front']
THREE_SEAT = ['the three people sit in a row on {S}, shoulder to shoulder', 'the person in the middle sits on {S} while the person on the left and the person on the right stand on either side']
OBJ = ['the person holds an object up with both hands and studies it', 'the person carries an object under one arm', 'the person passes an object from one hand to the other', 'the person holds an object out, offering it to the front', 'the person examines an object held close to the face', 'the person balances an object on one open palm', 'the person hugs an object to the chest with both arms', 'the person carries an object over one shoulder', 'the person sets an object down carefully', 'the person swings an object lightly at one side']
