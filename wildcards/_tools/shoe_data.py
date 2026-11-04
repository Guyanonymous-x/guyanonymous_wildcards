"""Hand-written vocabulary for the shoe wildcards (shoe_build.py merges it with data/shoe_vocab.json, which was harvested from the user's sample file).
One item per line inside each block.  No curly braces or pipe characters anywhere (they are not allowed in the wildcard files)."""
def L(s): return [x.strip() for x in s.strip().split('\n') if x.strip()]
T = ['T1', 'T2', 'T3', 'T4', 'T5', 'T6']
CLASSES = ['boot', 'heel', 'flat', 'sneaker', 'sandal', 'slipper', 'clog']
CLASS_WEIGHT = {'boot': 17, 'heel': 15, 'flat': 22, 'sneaker': 20, 'sandal': 11, 'slipper': 8, 'clog': 7}
TIER_WEIGHT = {'T1': 22, 'T2': 24, 'T3': 22, 'T4': 16, 'T5': 11, 'T6': 5}
# ------------------------------------------------------------------ price bands (euro)
PRICE_BAND = {'T1': (11.99, 56.99), 'T2': (39.99, 155), 'T3': (135, 595), 'T4': (510, 1950), 'T5': (4000, 20000), 'T6': (110000, 311000)}
TIER_NAME = {'T1': 'budget', 'T2': 'value', 'T3': 'mid-range', 'T4': 'premium', 'T5': 'luxury couture', 'T6': 'museum-grade one-of-a-kind'}
WORDS = {
 'T1': L("""inexpensive
affordable
no-frills
everyday
budget-friendly
bargain-priced
mass-produced
basic
economical
factory-made
entry-level
easy-on-the-wallet
discount-rack
starter
cheap and cheerful
humble
plain-spoken
simple
off-the-peg"""),
 'T2': L("""value-minded
sturdy
practical
well-made
reliable
hard-wearing
solid
honest
workmanlike
sensible
good-value
durable
trusty
no-nonsense
straightforward
serviceable
sound
decently made
tough"""),
 'T3': L("""well-crafted
quality
handsome
mid-priced
dependable
carefully made
classic
heritage-style
fine
resoleable
thoughtfully built
craft-minded
long-lasting
good-looking
properly made
traditional
workshop-built
enduring
trim
considered"""),
 'T4': L("""polished
refined
upscale
beautifully made
premium
elegant
high-end
exceptional
superb
boutique
finely finished
distinguished
handsomely appointed
sophisticated
gallery-worthy
carefully hand-finished
designer-label
elevated
impeccable
discerning"""),
 'T5': L("""artisanal
couture
exquisite
sumptuous
luxurious
atelier-made
bespoke
rarefied
lavish
haute-couture
heirloom-quality
masterfully crafted
extraordinary
resplendent
princely
collector-grade
virtuoso
jewel-like
splendid
sovereign"""),
 'T6': L("""one-of-a-kind
museum-grade
extravagant
opulent
astonishingly ornate
astonishingly lavish
jewel-encrusted
royal-commission
treasury-grade
unique
monumental
imperial
priceless-looking
fantastical
unrepeatable
sculptural showpiece
bejewelled
palatial
gilded
mythic"""),
}
# ------------------------------------------------------------------ shoe types per class.  name|closure kinds|sole kind
TYPES = {
 'boot': L("""Chelsea boots|elastic,pull|stack
ankle booties|zip,elastic,lace|stack
button boots|button|stack
chukka boots|lace|stack
combat boots|lace,zip|lug
cowboy boots|pull|cuban
desert boots|lace|crepe
hiking boots|lace|lug
jodhpur boots|buckle,pull|stack
knee-high riding boots|zip,pull,buckle|stack
lace-up granny boots|lace,hook|stack
motorcycle boots|buckle,zip,lace|lug
rain boots|pull|lug
shearling slipper boots|pull,slip|soft
snow boots|lace,toggle|lug
thigh-high boots|zip,lace|high
work boots|lace|lug
Western boots|pull|cuban
Wellington boots|pull|lug
Beatle boots|elastic,pull|cuban
engineer boots|buckle,pull|lug
harness boots|buckle,pull|stack
mountaineering boots|lace,hook|lug
logger boots|lace,hook|lug
paratrooper boots|lace|lug
duck boots|lace|lug
mukluks|toggle,lace|soft
go-go boots|zip|stack
over-the-knee suede boots|zip,pull|high
slouch boots|pull|stack
platform lace-up boots|lace|platform
cavalier boots|pull|cuban
gaiter boots|elastic,button|stack
roper boots|pull|stack
moto-style ankle boots|buckle,zip|lug
winter trekking boots|lace,hook|lug
side-zip dress boots|zip|stack
stacked-heel ankle boots|zip,elastic|stack
Cuban-heel boots|elastic,pull|cuban
zip-front combat boots|zip,lace|lug
fur-lined winter boots|lace,toggle|lug
calf-high lace-up boots|lace,hook|stack
hunting boots|lace|lug
wader boots|pull|lug
firefighter-style boots|pull,buckle|lug
steel-toe safety boots|lace|lug
Tyrolean mountain boots|lace,hook|lug
sheepskin pull-on boots|pull|soft
pull-on ankle boots|pull,elastic|stack"""),
 'heel': L("""Mary Jane heels|strap,buckle|high
T-strap heels|strap,buckle|high
ankle-strap heeled sandals|strap,buckle|high
cage-strap heeled sandals|strap,buckle|high
d'Orsay pumps|slip|high
lace-up heeled sandals|ribbon,lace|high
opera pumps|slip|high
platform heels|strap,slip|platform
slingback heels|strap,buckle|high
stiletto pumps|slip|high
heeled mules|slip|high
kitten-heel mules|slip|mid
kitten-heel pumps|slip|mid
block-heel pumps|slip|mid
cone-heel pumps|slip|high
peep-toe pumps|slip|high
ghillie heels|ribbon,lace|high
spectator pumps|slip|mid
Louis-heel pumps|slip|mid
cutout pumps|slip|high
sculptural-heel pumps|slip|high
wedding heels|strap,slip|high
tango shoes|strap,buckle|high
ballroom dance heels|strap,buckle|mid
platform stilettos|strap,slip|platform
T-bar court shoes|strap,buckle|mid
court shoes|slip|mid
strappy block-heel sandals|strap,buckle|mid
pointed-toe slingbacks|strap,buckle|high
embellished evening pumps|slip|high
wedge pumps|slip|wedge
velvet evening heels|slip|high
patent leather pumps|slip|high
ankle-wrap heels|ribbon,strap|high
ankle-tie heeled sandals|ribbon|high
curved-heel pumps|slip|mid
flared-heel Mary Janes|strap,buckle|mid
transparent-heel pumps|slip|high
pearl-heeled pumps|slip|high"""),
 'flat': L("""Mary Jane flats|strap,buckle|flat
ballet flats|slip,elastic|flat
boat shoes|lace|flat
brothel creepers|lace,buckle|crepe
derby shoes|lace|stack
double monk-strap shoes|buckle|stack
driving moccasins|slip|flat
jutti-style flats|slip|flat
moccasins|slip|flat
oxfords|lace|stack
penny loafers|slip|stack
pointed flat mules|slip|flat
saddle shoes|lace|flat
split-toe tabi flats|slip,strap|flat
tassel loafers|slip|stack
wholecut oxfords|lace|stack
wingtip brogues|lace|stack
winklepickers|slip,lace|stack
espadrilles|slip,ribbon|rope
barefoot-style minimalist shoes|strap,elastic|thin
orthopedic comfort shoes|strap,lace|comfort
monk-strap shoes|buckle|stack
blucher shoes|lace|stack
spectator oxfords|lace|stack
kiltie loafers|slip|stack
horsebit loafers|slip|stack
venetian loafers|slip|flat
opera flats|slip|flat
d'Orsay flats|slip|flat
ghillie shoes|ribbon,lace|flat
tap shoes|ribbon,lace|stack
character shoes|strap,buckle|mid
dance flats|slip,elastic|flat
jazz shoes|slip,elastic|flat
slingback flats|strap,buckle|flat
plimsolls|lace,elastic|flat
deck shoes|lace|flat
apron-toe derbies|lace|stack
cap-toe oxfords|lace|stack
longwing brogues|lace|stack
Norwegian-split-toe loafers|slip|stack
golf shoes|lace|lug
bowling shoes|lace|flat
velvet formal slippers|slip|flat
whole-cut dress derbies|lace|stack
gum-soled lace-ups|lace|crepe
open-sided dress flats|elastic,strap|flat
pointed Mary Jane flats|strap,buckle|flat
embroidered silk flats|slip|flat
folding travel flats|slip,elastic|flat
Chinese cloth flats|slip,strap|flat
two-tone brogues|lace|stack
buckled gentleman's shoes|buckle|stack
T-strap flats|strap,buckle|flat"""),
 'sneaker': L("""basketball sneakers|lace|sport
court sneakers|lace|sport
high-top sneakers|lace|sport
low-top sneakers|lace|sport
platform sneakers|lace|platform
running shoes|lace|sport
skate shoes|lace|sport
slip-on sneakers|elastic,slip|sport
trail running shoes|lace|lug
walking shoes|lace|sport
water shoes|elastic,slip|sport
cross-training shoes|lace|sport
tennis shoes|lace|sport
canvas plimsoll sneakers|lace|sport
retro runners|lace|sport
chunky dad sneakers|lace|platform
soccer cleats|lace|lug
climbing shoes|hookloop,lace|thin
cycling shoes|hookloop,lace|thin
lifting shoes|strap,lace|sport
volleyball shoes|lace|sport
wrestling shoes|lace|thin
fencing shoes|lace|thin
golf sneakers|lace|sport
minimalist trainers|lace,elastic|thin
knit sock-sneakers|slip|sport
hybrid hiking trainers|lace|lug
approach shoes|lace|lug
hook-and-loop strap sneakers|hookloop|sport
speed-lace running shoes|lace|sport
tabi-style sneakers|slip,hookloop|sport
leather court trainers|lace|sport
suede terrace sneakers|lace|crepe
training flats|lace|thin
platform high-tops|lace|platform
baseball cleats|lace|lug
canvas high-tops|lace|sport
bouldering shoes|hookloop|thin
chunky platform trainers|lace|platform"""),
 'sandal': L("""fisherman sandals|buckle,strap|flat
flip-flops|thong|thong
geta-inspired platform sandals|thong|wood
gladiator sandals|buckle,strap,lace|flat
hiking sandals|hookloop,strap|lug
platform sandals|buckle,strap|platform
slide sandals|slip|flat
thong sandals|thong|flat
wedge sandals|buckle,strap|wedge
huaraches|strap,slip|flat
contoured cork-footbed sandals|buckle,strap|flat
sport sandals|hookloop|lug
tire-sole sandals|strap,thong|flat
jelly sandals|buckle|flat
espadrille wedge sandals|ribbon,buckle|wedge
T-strap sandals|buckle|flat
zori|thong|flat
ankle-wrap sandals|ribbon|flat
mule sandals|slip|flat
toe-loop sandals|thong|flat
pool slides|slip|flat
strappy flat sandals|buckle,strap|flat
braided leather sandals|buckle|flat
sheepskin-lined slides|slip|soft
beach sandals|thong,strap|flat
cut-out flat sandals|buckle|flat
knotted-strap sandals|strap|flat
ankle-strap flat sandals|buckle|flat
open-toe wedge mules|slip|wedge
cross-strap slides|slip|flat
tatami-style straw sandals|thong|rope
Roman sandals|lace,buckle|flat
sports slides|slip|flat
platform flip-flops|thong|platform
woven huarache slides|slip|flat
river sandals|hookloop,strap|lug"""),
 'slipper': L("""babouche slippers|slip|soft
house slippers|slip|soft
smoking slippers|slip|soft
moccasin slippers|slip|soft
bootie slippers|slip,pull|soft
sheepskin slippers|slip|soft
velvet evening slippers|slip|soft
opera slippers|slip|soft
pointed Turkish slippers|slip|soft
ballet-style slippers|elastic,slip|soft
knitted slipper socks|slip|soft
slipper clogs|slip|soft
hotel slippers|slip|soft
spa slippers|slip|soft
felt slippers|slip|soft
tatami slippers|slip|soft
open-toe house slippers|slip|soft
memory-foam slippers|slip|soft
mule slippers|slip|soft
embroidered Chinese slippers|slip|soft
fleece-lined slippers|slip|soft
quilted slippers|slip|soft
terry-cloth bath slippers|slip|soft
moleskin slippers|slip|soft
Berber leather slippers|slip|soft
wool-felt boot slippers|slip,pull|soft
satin boudoir slippers|slip|soft
crocheted slippers|slip|soft
leather scuffs|slip|soft
pom-pom slippers|slip|soft"""),
 'clog': L("""clogs|slip,strap|wood
garden clogs|slip|rubber
nursing clogs|slip,strap|rubber
wooden-soled clogs|slip,strap|wood
Dutch klompen|slip|wood
Swedish clogs|slip,strap|wood
mule clogs|slip|wood
platform clogs|slip,strap|platform
rubber clogs|slip,strap|rubber
leather clogs|slip,strap|wood
clog boots|zip,buckle|wood
chef's clogs|slip|rubber
kitchen clogs|slip,strap|rubber
hospital clogs|slip,strap|rubber
carved-wood clogs|slip|wood
painted Dutch-style clogs|slip|wood
sabot clogs|slip|wood
closed-back clogs|slip|wood
open-back clogs|slip,strap|wood
studded clogs|slip,strap|wood
shearling-lined clogs|slip|wood
suede clogs|slip,strap|wood
cork-soled clogs|slip,strap|cork
tooled leather clogs|slip,strap|wood
foam clogs|slip,strap|rubber
wetland clogs|slip|rubber
hoof-style platform clogs|slip|platform
embroidered clogs|slip,strap|wood
buckled clogs|buckle,strap|wood
orthopedic clogs|strap,slip|comfort"""),
}
# ------------------------------------------------------------------ purposes (what the shoe is for), per class
PURPOSE = {
 'boot': L("""daily city commuting in all weather
long days on a construction site
backcountry hiking on rocky trails
winter walks through deep snow
muddy farm chores and livestock work
riding motorcycles on long highway tours
horseback riding and ranch work
cold-weather dog walking
dressy evenings in a drizzle
festival crowds and puddles
firefighting-style rescue training
trail maintenance work
fishing from slippery riverbanks
mountaineering at altitude
stage performances with a rock band
off-duty military drills
rainy-day errands
warehouse shifts on concrete floors
polar expeditions
lumber camp labour
a cowboy-themed wedding
autumn foraging in the forest
a quick costume change in the theatre
urban fashion with a rugged edge
navigating icy pavements to the office"""),
 'heel': L("""a black-tie dinner
wedding ceremonies
red-carpet appearances
long conference days that need to look sharp
ballroom dancing competitions
tango nights
opening nights at the theatre
cocktail parties
job interviews at a law firm
runway modelling
formal graduation ceremonies
photo shoots
a quinceañera or debutante ball
anniversary dinners
gala fundraisers
courtroom appearances
church services on Sunday
a stylish office day
drag performances
bridal party photographs
a first date in a nice restaurant
a museum opening
cabaret shows
a night at the opera
a rooftop party"""),
 'flat': L("""all-day wear at a busy office
walking tours of old cities
a morning commute by train
weddings where there is a lot of dancing
sailing weekends
teaching in a classroom
driving long distances
weekend errands
gallery visits
travel days in crowded airports
business meetings
church or temple visits
ballet and jazz classes
gardening in good weather
cultural festivals
all-day shifts in a shop
formal dinners
country club afternoons
bowling nights
golf on a summer course
library hours
cafe afternoons
quiet strolls in the park
tap-dancing recitals
restaurant service"""),
 'sneaker': L("""marathon training
basketball games on an outdoor court
skateboarding in a city park
gym circuits and weight training
trail running through the forest
tennis matches
casual city walking
rock climbing approaches
cycling commutes
long days on a retail floor
football practice on wet grass
volleyball tournaments
parkour sessions
soccer on artificial turf
yoga and pilates studios
hiking easy trails
street fashion
airport sprints
a walking holiday
indoor court sports
rowing and cross-training
warm-up runs in the park
long shifts on a factory floor
a charity fun run
dog-park afternoons"""),
 'sandal': L("""beach days
summer city walking
poolside lounging
river hiking and water crossings
holiday sightseeing in hot weather
garden parties
barefoot-feeling comfort in warm weather
festival camping
boat decks
summer weddings
market shopping
lazy weekend mornings
summer evenings on a terrace
fishing trips
walks along the shore
tropical resort wear
yoga retreats
kayak launches
sun-baked city commutes
street food crawls
village strolls on a hot day
a spa visit
music festivals
paddling and rafting
dinners outdoors on a warm night"""),
 'slipper': L("""relaxing at home
lazy winter mornings
hotel and spa stays
cold stone floors
reading by the fire
quick trips to the mailbox
guests who remove their shoes at the door
recovering from a long day on your feet
sleepovers
bedtime
a sauna or hammam visit
long flights
a smoking-jacket kind of evening
a cosy cabin weekend
a tea ceremony
a boudoir
pottering around the kitchen
Sunday brunch in pyjamas
a meditation retreat
a library at home
a dressing room backstage
a ryokan stay
a rainy day indoors
foot comfort after surgery
warming cold feet"""),
 'clog': L("""twelve-hour nursing shifts
kitchen work on wet floors
gardening and potting
farm chores
easy slip-on wear around the house
wet-lab work
dance and folk festivals
woodworking workshops
cleaning and cooking
fishing-village life
stage performances of folk dances
a bakery shift at dawn
a pottery studio
walking the dog in all weather
dairy farm chores
hospital rounds
standing at a market stall
Scandinavian style
craft fairs
a summer cottage
potato harvests
a wooden-shoe museum display
chefs on their feet all night
tidepool exploring
street fashion"""),
}
# ------------------------------------------------------------------ target audiences (adults only), common, per class and per tier
AUDIENCE_COMMON = L("""commuters who walk a lot
people with wide feet
people with narrow feet
tall women who want a lower heel
men with high arches
people with bunions
office workers on a budget
retirees who like to walk
students on a tight budget
people who are always on their feet
travellers who pack light
people who dislike tying laces
anyone who wants one pair to do everything
fashion-forward city dwellers
collectors of old-fashioned styles
minimalists who buy few things
people who walk dogs every morning
people with sensitive feet
anyone who values repair over replacement
people over seventy who want secure footing
athletic women with strong calves
big men with size fifteen feet
petite women who want elegant shoes in small sizes
vegan shoppers who avoid leather
eco-conscious buyers who want recycled materials
night-shift workers
bookish people who like a quiet look
theatre costume designers
performers who change footwear between acts""")
AUDIENCE = {
 'boot': L("""outdoor workers
farmers and ranchers
motorcyclists
hikers and mountaineers
punks and goths
cowboys and cowgirls
winter commuters
tradespeople
military reenactors
rock musicians
festival-goers
people who live in rainy climates
anglers
off-duty police officers
construction crews"""),
 'heel': L("""brides and bridesmaids
dancers who compete
people attending a gala
runway models
lawyers and executives
theatre performers
drag queens and kings
opera-goers
cocktail-party regulars
people who love vintage glamour
men who wear heels with confidence
nightclub regulars
stylists and fashion editors
tango partners
wedding guests"""),
 'flat': L("""teachers
sailors and boaters
office workers
golfers
dancers
people who love classic tailoring
bartenders and waiters
museum guides
finance workers
drivers who want pedal feel
travellers
older gentlemen
students of ballet
anyone with a desk job and a hectic evening
brides who dance until midnight"""),
 'sneaker': L("""marathon runners
basketball players
skaters
gym-goers
hikers on easy trails
tennis players
streetwear collectors
climbers
cyclists
retail workers
footballers
volleyball players
yoga teachers
people who walk ten thousand steps a day
sneaker collectors who chase limited editions"""),
 'sandal': L("""beachgoers
holiday travellers
river guides
kayakers
festival campers
poolside loungers
summer commuters
island residents
yoga retreat guests
anglers
people who live in hot climates
street-market shoppers
market gardeners
bohemian travellers
resort guests"""),
 'slipper': L("""people who work from home
hotel guests
spa-goers
the elderly
night owls
readers
pet owners
people with cold feet
guests in a ryokan
backstage performers
people recovering from foot surgery
cabin weekenders
pipe smokers and novel readers
dressing-gown devotees
travellers on long flights"""),
 'clog': L("""nurses and care workers
chefs and cooks
gardeners
farmers
potters
woodworkers
folk dancers
Dutch heritage enthusiasts
Scandinavian design lovers
market vendors
lab technicians
bakers
craft-fair regulars
cottage dwellers
people on their feet all day"""),
}
AUDIENCE_TIER = {
 'T1': L("""shoppers on a very tight budget
people who buy shoes in bulk
students sharing a flat
festival-goers who expect to ruin their shoes
anyone who treats shoes as disposable
newcomers who need work footwear on the first day
families buying several pairs at once
people who like a new look every month"""),
 'T2': L("""practical people who want value
workers who replace their shoes every year
careful shoppers who read reviews
first-job buyers
people who want something sturdy but cheap
renters who move often
people on a family budget
weekend hobbyists"""),
 'T3': L("""buyers who want shoes that can be resoled
office professionals who dress well
people who care about craft
enthusiasts of heritage style
people who buy one good pair every few years
discerning walkers
people who prefer repair to replacement
young professionals building a wardrobe"""),
 'T4': L("""collectors of fine shoes
executives and diplomats
people who attend many formal events
design-conscious professionals
anyone who appreciates hand finishing
boutique regulars
style editors
gift buyers marking a milestone"""),
 'T5': L("""couture clients with a personal fitting
collectors of wearable art
brides with a very large budget
guests at society balls
patrons of the fine crafts
people who commission shoes from named artisans
celebrities on a red carpet
heirloom collectors"""),
 'T6': L("""royal families and heads of state
museum curators
billionaire collectors
a single client for whom the last was carved
guests at a coronation ceremony
a palace treasury
a private gallery of masterpieces
an auction house showpiece
the owner of a legendary jewel collection"""),
}

# ------------------------------------------------------------------ v18: platform, novelty and exotic-dancer footwear classes
CLASSES += ['platform', 'novelty', 'exotic']
CLASS_WEIGHT.update({'platform': 9, 'novelty': 6, 'exotic': 5})
TYPES.update({
 'platform': L("""platform sneakers|lace|platform
chunky platform sneakers|lace,hookloop|platform
platform sandals|buckle,strap|platform
flatform sandals|strap,buckle|platform
platform Mary Janes|strap,buckle|platform
platform loafers|slip|platform
platform oxfords|lace|platform
platform brogues|lace|platform
platform creepers|lace,buckle|platform
platform combat boots|lace,zip|platform
platform ankle boots|zip,elastic|platform
platform knee-high boots|zip,lace|platform
platform thigh-high boots|zip,lace|platform
platform Chelsea boots|elastic,pull|platform
platform Western boots|pull|platform
platform go-go boots|zip|platform
platform clogs|slip|platform
platform wedge sandals|strap,buckle|platform
platform espadrilles|ribbon,strap|platform
platform stilettos|strap,buckle|platform
platform pumps|slip|platform
platform lace-up heels|lace,ribbon|platform
platform slides|slip|platform
platform flip-flops|thong|platform
glam-rock platform boots|zip,lace|platform
disco platform shoes|strap,buckle|platform
1970s stacked platform shoes|strap,buckle|platform
gothic buckle platform boots|buckle,lace|platform
cyber platform boots|lace,zip|platform
kawaii platform shoes|strap,buckle|platform
Japanese geta platform sandals|thong|platform
tall wooden platform sandals|thong,strap|platform
Venetian chopine platform shoes|slip,strap|platform
Spice-era platform sneakers|lace|platform
extra-tall platform boots|zip,lace|platform
double-platform boots|buckle,zip,lace|platform
spring-heeled platform shoes|strap,buckle|platform
hidden-wedge platform boots|zip,lace|platform
cork platform clogs|slip,strap|platform
glitter platform boots|zip,lace|platform"""),
 'novelty': L("""clown shoes|slip,lace|flat
oversized clown shoes|slip|flat
jester shoes with curled toes|slip,buckle|flat
curly-toe elf shoes|slip|flat
pointed pixie boots|slip,lace|flat
giant-toe cartoon shoes|slip|flat
duck-feet shoes|slip|flat
flipper-style shoes|slip|flat
animal-paw slippers|slip|soft
dinosaur-foot slippers|slip|soft
bunny-foot slippers|slip|soft
bear-claw boots|slip,pull|soft
hoof boots|pull,zip|stack
dragon-claw boots|zip,lace|lug
monster-feet slippers|slip|soft
cartoon character sneakers|lace|sport
light-up sneakers|lace,hookloop|sport
roller sneakers with hidden wheels|lace,hookloop|sport
heeled sneakers|lace,zip|high
sneaker-heel hybrids|lace,zip|high
aquarium-heel shoes|strap,buckle|platform
shoes with tiny doll scenes in clear heels|strap,buckle|platform
mirror-heeled shoes|strap,buckle|high
sculptural architectural heels|slip,strap|high
shoes with a single sculpted heel shaped like an animal|slip,strap|high
heel-less cantilever shoes|slip,strap|high
shoes with no heel and an angled sole|slip,strap|platform
glass-slipper style pumps|slip|high
ruby-slipper style pumps|slip|high
winged shoes|lace,strap|flat
winged sandals|strap,buckle|flat
Mercury-style winged boots|lace,pull|stack
shoes with printed faces|slip,lace|flat
tapestry carpet slippers|slip|soft
cat-face slippers|slip|soft
shark-mouth slippers|slip|soft
pickle-shaped slippers|slip|soft
sushi sneakers|lace|sport
burger-shaped slippers|slip|soft
fish-shaped slippers|slip|soft
inflatable-sole sneakers|lace|sport
bouncy spring shoes|strap,buckle|sport
stilt shoes|buckle,strap|platform
sky-high stilt boots|buckle,lace|platform
wheeled skate boots|lace,buckle|sport
ice-skate style boots|lace,hook|sport
ski-boot style novelty boots|buckle,zip|platform
armoured boots for costume wear|buckle,strap|lug
medieval poulaine shoes|slip,buckle|flat
medieval pointed-toe boots|slip,lace|flat
Elizabethan buckled shoes|buckle,ribbon|dress
pirate buccaneer boots|pull|cuban
wizard boots|lace,hook|stack
space-boot costume shoes|zip,lace|platform
robot-foot covers|slip,strap|platform
hobbit-foot slippers|slip|soft
furry yeti boots|pull|soft
mukluk-style fur boots|toggle,lace|soft
mascot-feet shoe covers|slip|soft
sock-shoe hybrids|slip|soft
vegetable-shaped novelty shoes|slip|soft
flower-petal sandals|strap,buckle|flat
seashell sandals|strap,buckle|flat
LED strip boots|zip,lace|platform
glow-in-the-dark clog boots|slip|rubber
rainbow-sole sneakers|lace|sport
bubble-wrap sole shoes|slip|sport"""),
 'exotic': L("""clear acrylic platform stilettos|strap,buckle|platform
clear platform sandals with ankle straps|strap,buckle|platform
8-inch platform stilettos|strap,buckle|platform
9-inch platform stilettos|strap,buckle|platform
6-inch stiletto pumps|slip,strap|high
7-inch stiletto pumps|slip,strap|high
ankle-strap stripper heels|strap,buckle|platform
stripper platform sandals|strap,buckle|platform
dancer's lace-up platform heels|lace,ribbon|platform
dancer's thigh-high platform boots|zip,lace|platform
pole-dance boots|zip,lace|platform
pole-dance platform boots|zip,lace|platform
dancer's over-the-knee stiletto boots|zip,lace|high
dancer's ankle booties with platform soles|zip,lace|platform
dancer's cut-out platform boots|zip,lace|platform
dancer's mirror-finish stilettos|strap,buckle|platform
glitter platform stilettos|strap,buckle|platform
holographic platform stilettos|strap,buckle|platform
rhinestone platform stilettos|strap,buckle|platform
rhinestone strap stilettos|strap,buckle|high
spiked-heel platform stilettos|strap,buckle|platform
spiked-stud platform boots|zip,lace|platform
metallic gold platform heels|strap,buckle|platform
neon platform heels|strap,buckle|platform
patent leather platform heels|strap,buckle|platform
latex-look platform boots|zip,lace|platform
lace-up gladiator stilettos|lace,buckle|high
gladiator platform heels|lace,buckle|platform
peep-toe platform pumps|slip,strap|platform
d'Orsay platform pumps|slip|platform
pointed-toe platform pumps|slip|platform
mule platform slides|slip|platform
transparent-strap platform slides|slip|platform
feathered platform slides|slip|platform
marabou-trimmed platform mules|slip|platform
chain-detail platform sandals|strap,buckle|platform
chain-wrapped ankle boots|zip,buckle|platform
collar-strap platform heels|strap,buckle|platform
lace-up corset-style boots|lace,zip|platform
stiletto boots with hidden platform|zip,lace|platform
heels with a hidden platform|slip,strap|platform
tall platform wedges|strap,buckle|platform
exotic-dance wedge boots|zip,lace|platform
rubber-soled pole-grip boots|zip,lace|platform"""),
})
PURPOSE.update({
 'platform': L("""making a bold street-fashion statement
adding height to an outfit
a retro seventies disco look
gothic and alternative nights out
festival dancing
stage and costume work
adding drama to a simple outfit
clubbing for hours
visual-kei and harajuku street style
runway styling
comfortable all-day height
cosplay of a glam-rock character"""),
 'novelty': L("""a clown or circus performance
costume parties
cosplay and conventions
cheerful comic effect
fancy-dress events
stage comedy
Renaissance fairs
a surprise gift
a holiday pageant
a theatre production
amusement park costumes
a playful photo set"""),
 'exotic': L("""a professional dance performance
pole routines on stage
club performances
dance rehearsals
burlesque shows
dance fitness classes
a themed party night
photo shoots in glamorous settings
costume work
choreographed stage numbers"""),
})
AUDIENCE.update({
 'platform': L("""street-fashion fans
glam-rock fans
disco revival fans
gothic fashion fans
festival goers
stage performers
clubbers
cosplayers
vintage collectors
people who love extra height"""),
 'novelty': L("""clowns and circus performers
cosplayers
party-goers
theatre costume wearers
comic performers
fantasy fans
Renaissance fair regulars
gift givers
convention visitors
theme park performers"""),
 'exotic': L("""professional dancers
pole performers
burlesque performers
stage dancers
dance fitness enthusiasts
nightclub performers
cabaret artists
choreographers
people attending a themed party
adult costume wearers"""),
})
