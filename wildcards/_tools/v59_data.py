# sector -> lines 'name|outfit;outfit|tool;tool|workplace;workplace|action;action'
RAW = {
'health': """nurse|blue scrubs with a lanyard and soft clogs; a white tunic and trousers|a stethoscope; a clipboard of patient notes|a bright hospital ward; a quiet clinic corridor|checking a patient's pulse; recording notes at a bedside
surgeon|green surgical scrubs, a cap and a mask; a sterile gown and gloves|a surgical instrument tray; a bright overhead lamp|an operating theatre; a scrub room|leaning over an operating table; washing hands before surgery
general practitioner|a pressed shirt and a long white coat; smart casual clothes with a name badge|a stethoscope; a small reflex hammer|a consulting room; a family practice surgery|listening to a patient; writing a prescription
dentist|a light tunic, a mask and gloves; a short white coat and safety glasses|a mouth mirror and probe; a dental drill|a dental surgery with a reclining chair; a clean treatment room|examining a patient's teeth; adjusting an overhead lamp
paramedic|a green jumpsuit with reflective strips; a dark uniform with a high-visibility vest|a first-aid bag; a portable defibrillator|beside an ambulance; at a roadside incident|kneeling beside a patient; lifting a stretcher
pharmacist|a white coat over smart clothes; a plain tunic with a name badge|a box of medicine; a counting tray|a pharmacy counter; shelves of labelled boxes|counting tablets; explaining a prescription
physiotherapist|a polo shirt and trainers; a fitted tunic and trousers|a resistance band; a foam roller|a bright therapy room; a gym with mats and rails|guiding a patient through a stretch; adjusting a patient's posture
veterinarian|blue scrubs and a stethoscope; a white coat with a paw-print badge|a stethoscope; a small thermometer|an animal clinic; a farm barn|examining a dog; listening to an animal's heartbeat
midwife|a soft tunic and a lanyard; comfortable scrubs|a handheld foetal monitor; clean towels|a birthing room; a home visit|reassuring a patient; preparing a birth pool
radiographer|a tunic with a lead apron; scrubs and a radiation badge|an X-ray plate; a control panel|an imaging suite; a control room with a window|positioning a patient; checking a scan on a screen""",
'trades': """electrician|a high-visibility vest, a hard hat and boots; dark work overalls|a voltage tester; a coil of cable|a building site; a switch room|connecting wires in a panel; testing a circuit
plumber|work overalls and knee pads; a polo shirt and sturdy trousers|a pipe wrench; a roll of pipe|under a kitchen sink; a bathroom with exposed pipes|tightening a joint; fitting a new tap
carpenter|a canvas apron over a work shirt; sawdust-covered overalls|a handsaw; a claw hammer and a tape measure|a workshop with a bench; a half-built timber frame|measuring a plank; planing a board
bricklayer|dusty overalls and a hard hat; work trousers and gloves|a trowel; a spirit level|a half-built wall; a scaffolded building|laying bricks in a neat course; spreading mortar
welder|a leather apron, a welding helmet and gloves; flame-resistant overalls|a welding torch; a metal clamp|a fabrication shop; an industrial yard|welding a seam with a shower of sparks; checking a weld
painter and decorator|white spattered overalls; a paint-flecked shirt|a roller and tray; a wide brush|a half-painted room; a ladder against a wall|rolling paint onto a wall; taping a skirting board
mechanic|oil-stained overalls; a work shirt with rolled sleeves|a socket set; a wrench|a garage with a car on a lift; a workshop|checking under a bonnet; tightening a wheel
roofer|a hard hat, harness and boots; a work shirt and gloves|a hammer and nails; a stack of tiles|on a pitched roof; beside a scaffold|laying tiles; checking a ridge
mason|a dusty apron and goggles; work clothes and gloves|a chisel and mallet; a block of stone|a stoneyard; a cathedral workshop|carving a block of stone; checking a measurement
glazier|work gloves and a canvas apron; a hard hat and a high-visibility vest|a large sheet of glass on a frame; a glass cutter|a building site; a workshop|carrying a pane of glass; fitting a window
miner|a hard hat with a lamp and dusty overalls; a high-visibility jacket and boots|a pickaxe; a safety lamp|a tunnel with timber supports; a mine entrance|walking along a rail line; drilling at a rock face
farmer|a checked shirt, jeans and boots; a wide-brimmed hat and overalls|a pitchfork; a bucket of feed|a field at harvest; a farmyard|feeding animals; checking a crop
fisher|oilskin trousers and a woollen hat; waterproof overalls and boots|a fishing net; a tackle box|a small wooden fishing boat; a harbour quay|hauling in a net; baiting a line
forester|a hard hat, ear defenders and chainsaw trousers; a green work jacket|a chainsaw; a measuring wheel|a managed forest; a lumber yard|marking a tree; cutting a log
chef|a white double-breasted jacket and a tall hat; a black apron and a bandana|a long knife; a copper pan|a busy commercial kitchen; a restaurant pass|plating a dish; stirring a pot
baker|a white cap and a floury apron; a short-sleeved shirt and a hairnet|a wooden peel; a rolling pin|a bakery with a brick oven; a counter of fresh loaves|shaping dough; sliding bread from an oven
butcher|a striped apron and a white hat; a white coat and rubber boots|a large cleaver; a sharpening steel|a butcher's counter; a cold room|cutting meat; wrapping an order
barista|a dark apron over a shirt; a casual shirt with rolled sleeves|a milk jug; an espresso portafilter|a coffee bar with a gleaming machine; a counter by a window|pouring latte art; tamping coffee
barber|a fitted black smock; a shirt with rolled sleeves|scissors and a comb; an open razor|a barber shop with a leather chair; a mirrored wall|trimming a beard; cutting hair
hairdresser|a black apron with pockets; a stylish casual outfit|a pair of scissors; a hairdryer|a salon with mirrors; a styling chair|combing out hair; mixing a colour
tailor|a waistcoat and a tape measure round the neck; a smart shirt with sleeves rolled|a measuring tape; a pair of shears|a fitting room; a tailor's workshop|marking cloth with chalk; pinning a hem
cobbler|a leather apron over a shirt; work clothes and glasses|a small hammer; a last and awl|a small repair shop; a bench strewn with leather|stitching a sole; polishing a shoe""",
'public': """police officer|a dark uniform with a utility belt and a badge; a high-visibility jacket over a uniform|a radio; a notebook|a city street; a police station desk|talking to a member of the public; directing traffic
firefighter|a heavy coat, helmet and boots; a fireproof suit with a breathing apparatus|a fire hose; an axe|beside a red fire engine; at a smoky building|climbing a ladder; spraying water
soldier|combat fatigues and boots; a dress uniform with a beret|a field pack; a map case|a training ground; a barracks yard|marching in step; checking equipment
lifeguard|a red swimsuit and a whistle; shorts and a bright rash vest|a rescue tube; binoculars|a high lifeguard chair on a beach; a poolside|scanning the water; blowing a whistle
postal worker|a short-sleeved uniform and a satchel; a high-visibility vest and shorts|a bundle of letters; a parcel|a residential street; a sorting office|delivering parcels; sorting letters
bus driver|a smart uniform and a cap; a work shirt with a lanyard|a large steering wheel; a ticket machine|a driver's cab; a bus stop|checking a mirror; greeting passengers
train conductor|a navy uniform with a peaked cap; a waistcoat and a lanyard|a ticket punch; a handheld whistle|a station platform; a railway carriage|checking tickets; signalling departure
pilot|a navy uniform with epaulettes and a cap; a white shirt with gold stripes on the shoulders|a flight bag; a headset|an aircraft cockpit; beside an aeroplane|running pre-flight checks; speaking into a headset
air traffic controller|a headset and a smart shirt; a lanyard and a jumper|a radar screen; a microphone|a tower with wide windows; a dark control room|scanning a radar display; speaking to pilots
judge|a black robe over a suit; a robe with a white collar|a wooden gavel; a stack of case files|a courtroom bench; a panelled chamber|reading a document; listening to a witness
lawyer|a dark suit and a briefcase; a gown over a suit|a thick file; a pen and notepad|a law office with shelves of books; a courtroom|arguing a case; reviewing a contract
politician|a tailored suit and a lapel pin; a smart dress and a scarf|a lectern and microphone; a folder of papers|a council chamber; a press podium|giving a speech; shaking hands
librarian|a cardigan and glasses on a chain; a smart casual outfit with a lanyard|a trolley of books; a scanner|a library with tall shelves; a quiet reading room|re-shelving books; helping a reader
teacher|a shirt and a lanyard; a cardigan and trousers|a whiteboard marker; a pile of exercise books|a bright classroom; a school corridor|writing on a board; reading to a class
professor|a tweed jacket with elbow patches; a smart shirt with a scarf|a stack of papers; a laser pointer|a lecture hall; a book-lined office|giving a lecture; marking an essay
social worker|a smart casual shirt and a lanyard; a cardigan and trousers|a folder of notes; a mobile phone|a community centre; a small office|listening carefully; writing a plan
coach|a tracksuit and a whistle; a polo shirt and shorts|a stopwatch; a clipboard|a sports field; a gym hall|demonstrating a drill; timing a sprint""",
'office': """accountant|a shirt and tie or a smart blouse; a cardigan and glasses|a calculator; a spreadsheet printout|an office desk with two screens; a meeting room|checking figures; tapping a calculator
software developer|a hoodie and jeans; a casual shirt with a lanyard|a laptop; a pair of headphones|a desk with two monitors; a sunlit open-plan office|typing at a keyboard; looking at code
architect|a dark shirt and round glasses; a smart jacket with a rolled plan|a roll of drawings; a scale ruler|a drawing office; a building site visit|studying a plan; sketching a building
engineer|a hard hat and a high-visibility vest over a shirt; a smart jacket and a lanyard|a tablet of drawings; a measuring tool|a construction site; a laboratory|inspecting a structure; reviewing a drawing
scientist|a white lab coat and safety glasses; a lab coat and gloves|a pipette; a microscope|a bright laboratory; a bench lined with glassware|pipetting a sample; reading a result
journalist|a creased jacket with a notebook in the pocket; a casual shirt with a press lanyard|a reporter's notebook; a recording device|a busy newsroom; a street scene|taking notes; interviewing a person
photographer|a vest with many pockets; casual dark clothes|a camera with a long lens; a tripod|a studio with a backdrop; outdoors on location|looking through a viewfinder; adjusting a light
graphic designer|a creative layered outfit; a plain shirt and glasses|a graphics tablet and stylus; a colour swatch book|a bright studio desk; a wall of pinned sketches|drawing on a tablet; comparing colour swatches
receptionist|a smart blouse or shirt with a name badge; a blazer and a headset|a desk phone; an appointment book|a welcoming front desk; a lobby|greeting a visitor; answering a call
bank teller|a smart uniform and a lanyard; a shirt and a branded-free tie|a cash drawer; a stamp|a bank counter behind glass; a branch lobby|counting notes; processing a form
secretary|a smart cardigan and glasses; a neat shirt and skirt|a typewriter or keyboard; a diary|an office anteroom; a desk with trays|typing a letter; organising a diary
travel agent|a smart blazer and a scarf; a patterned shirt with a lanyard|a globe; a folder of brochures|a travel office with maps; a counter with a computer|pointing at a map; printing a ticket
call centre agent|a polo shirt and a headset; a plain shirt and a lanyard|a headset; a computer screen|a row of desks; a quiet open-plan floor|speaking into a headset; typing notes
real estate agent|a smart suit; a blazer and trousers with a key lanyard|a bunch of keys; a folder of listings|outside a house for sale; inside an empty room|showing a house; unlocking a door
interpreter|a dark suit and a lanyard; a smart jacket and a headset|a headset; a notebook|a conference booth; a meeting table|listening intently; speaking into a microphone""",
'creative': """painter|a paint-stained smock; an old shirt with rolled sleeves|a palette and brushes; an easel|a bright studio; an outdoor field|mixing colours; stepping back from a canvas
sculptor|a dusty apron and goggles; overalls covered in clay|a chisel and mallet; a block of clay|a workshop with half-finished figures; a stone studio|shaping clay; chipping stone
potter|a clay-spattered apron; a loose shirt with rolled sleeves|a potter's wheel; a wooden shaping tool|a pottery studio; a kiln room|throwing a vase; trimming a bowl
musician|a performance outfit; a casual jacket and boots|a guitar; a violin|a small stage; a rehearsal room|playing a melody; tuning an instrument
singer|a stage outfit; a sparkling jacket|a microphone; a microphone stand|a concert stage; a recording booth|singing into a microphone; closing eyes on a note
dancer|a leotard and wrap skirt; a loose practice outfit|a barre; soft slippers|a mirrored dance studio; a theatre stage|stretching at a barre; leaping across a floor
actor|a period costume; a plain rehearsal outfit|a script; a prop|a theatre stage; a backstage mirror|delivering a line; reading a script
magician|a dark suit with a cape; a waistcoat and a top hat|a deck of cards; a wand|a small stage with a curtain; a street corner|fanning out cards; pulling a scarf from a sleeve
circus performer|a sequinned bodysuit; a striped costume|juggling clubs; a hoop|a circus ring; a big top tent|juggling; balancing on a ball
film director|a casual jacket and a scarf; a dark shirt and a cap|a megaphone; a clapperboard|a film set with lights; a location shoot|calling for action; looking at a monitor
writer|a jumper with sleeves pulled over the hands; a casual shirt and glasses|a notebook and pen; a typewriter|a cluttered desk by a window; a cafe table|writing in a notebook; staring thoughtfully out of a window
fashion designer|a stylish black outfit with a measuring tape; a creative layered outfit|a mannequin; a pair of shears|a design studio with fabric rolls; a fitting room|pinning fabric on a mannequin; sketching a garment
jeweller|an apron and magnifying glasses; a plain shirt with a headlamp|a small file; a loupe|a jeweller's bench; a showroom|setting a stone; polishing a ring
florist|an apron and gardening gloves; a casual shirt with rolled sleeves|secateurs; a bucket of flowers|a flower shop; a market stall|arranging a bouquet; trimming stems
tattoo artist|a black shirt and gloves; a casual vest|a tattoo machine; a stencil|a tattoo studio; a clean treatment chair|drawing a stencil; tattooing a design
chocolatier|a white jacket and a cap; an apron and gloves|a piping bag; a tray of truffles|a clean confectionery kitchen; a shop counter|tempering chocolate; decorating truffles""",
'service': """taxi driver|a casual shirt and a cap; a jacket and a lanyard|a steering wheel; a navigation screen|a car at the roadside; a city rank|opening a car door; checking a mirror
waiter|a white shirt, black trousers and an apron; a waistcoat and a bow tie|a tray of glasses; a notepad|a busy restaurant; a table by a window|serving a dish; pouring wine
hotel concierge|a smart uniform with gold keys on the lapel; a dark jacket and tie|a brass bell; a city map|a hotel lobby desk; a marble foyer|giving directions; handing over a key
flight attendant|a neat uniform and a scarf; a fitted jacket and a hat|a service trolley; a safety card|an aircraft cabin aisle; beside the boarding door|serving a drink; demonstrating a safety device
cleaner|a tunic and rubber gloves; a work apron|a mop and bucket; a trolley of supplies|a bright corridor; a hotel room|mopping a floor; wiping a surface
security guard|a dark uniform and a radio; a high-visibility jacket and a cap|a torch; a bunch of keys|a building entrance; a corridor at night|patrolling a corridor; checking a pass
shop assistant|a casual shirt and a name badge; an apron and a lanyard|a barcode scanner; a price gun|a bright shop floor; a till|folding clothes; helping a customer
market trader|a flat cap and a woollen jumper; a bright apron|a set of scales; a crate of produce|a busy outdoor market stall; a covered market|calling out a price; weighing fruit
street musician|a worn jacket and a hat; a colourful scarf and fingerless gloves|an accordion; a violin|a busy pavement; a city square|playing for passers-by; tipping a hat
delivery rider|a helmet and a bright jacket; a cycling jacket and a bag on the back|a large delivery bag; a bicycle|a city street; a rainy pavement|checking a phone; handing over a parcel
dog walker|a practical jacket and boots; a fleece and a cap|several dog leads; a bag of treats|a park path; a woodland trail|walking several dogs; throwing a ball
tour guide|a bright jacket and a lanyard; a hat and a flag on a stick|a raised flag; a megaphone|a historic square; a museum entrance|pointing out a landmark; leading a group
gardener|a wide-brimmed hat and gloves; a work apron and boots|a pair of secateurs; a wheelbarrow|a walled garden; a greenhouse|pruning a rose; planting seedlings
childminder|a casual top and an apron; a cardigan|a basket of toys; a picture book|a bright playroom; a kitchen table|reading aloud; tying a shoelace
carer|a tunic and a lanyard; scrubs and trainers|a blood pressure monitor; a tray of tea|a comfortable living room; a care home lounge|helping someone stand; pouring tea""",
'spiritual': """rabbi|a dark suit, a tallit prayer shawl and a skullcap; a black coat and hat|an open prayer book; a Torah scroll with a pointer|a synagogue sanctuary; a study hall of books|reading from a scroll; teaching a class
cantor|a robe and a prayer shawl; a dark suit and a skullcap|an open prayer book; a lectern|a synagogue bimah; a sanctuary|singing a prayer; leading a congregation
Anglican priest|a black cassock and a white clerical collar; a white surplice over a black cassock|an open book of prayer; a silver chalice|a stone parish church; behind an altar|reading a blessing; raising a chalice
Catholic priest|a black cassock and a white collar; a green chasuble over a white alb|a censer; a chalice and paten|a cathedral nave; behind an altar|blessing with raised hand; swinging a censer
Orthodox priest|a black robe and a tall cylindrical hat; richly embroidered vestments|a hand cross; a censer|a church with a painted screen of icons; a candlelit nave|making a blessing; chanting a prayer
Protestant minister|a black robe with a white collar; a suit and a clerical collar|a large open Bible; a lectern|a plain white chapel; a pulpit|preaching from a pulpit; greeting people at the door
Methodist preacher|a dark suit and a clerical collar; a plain black robe|a large open Bible; a hymn book|a village chapel; a pulpit|preaching; leading a hymn
imam|a long robe and a white cap; a thobe and a turban|a copy of the Quran on a stand; a string of prayer beads|the prayer hall of a mosque; a courtyard of a mosque|leading a prayer; reciting from a book
muezzin|a long robe and a white cap; a plain white thobe|a handheld microphone; a loudspeaker|the balcony of a minaret; a courtyard|calling a prayer; standing with raised hands
Buddhist monk|a saffron robe with a bare shoulder; a maroon robe and a shaved head|a wooden alms bowl; a string of prayer beads|a mountain monastery; a temple hall|walking with a bowl; meditating in silence
Zen priest|a black robe with a wide sleeve; a grey robe and a rakusu bib|a wooden bell; a wooden stick|a quiet zendo; a rock garden|sitting in meditation; striking a bell
Tibetan lama|a maroon robe and a yellow hat; a layered robe and a sash|a ritual bell and a small drum; a prayer wheel|a high monastery with prayer flags; a candlelit shrine|turning a prayer wheel; chanting in a low voice
Hindu priest|a white dhoti and a saffron shawl; a sacred thread and a forehead mark|a brass lamp; a bell and a tray of flowers|a temple with a carved tower; a shrine with garlands|ringing a bell; waving a lamp in circles
Sikh granthi|a white robe and an orange turban; a plain robe and a blue turban|a chauri whisk; a large holy book on a throne|a temple with a golden dome; a prayer hall with a carpet|waving a whisk over a book; reading aloud
Shinto priest|a white robe and a tall black hat; a white kimono and a wide pale-blue skirt|a wand with paper streamers; a branch with white strips|a shrine under a red gate; a forest shrine|waving a streamered wand; bowing before a shrine
Taoist priest|a long blue robe and a hair knot; a yellow robe with symbols|a ritual sword; a small bell|a mountain temple; a courtyard with incense|making a gesture; burning incense
druid|a long hooded robe in green or white; a plain robe with a leaf crown|a wooden staff; a sickle|a stone circle at dawn; a forest clearing|raising a staff; speaking to the trees
shaman|a robe decorated with feathers and bones; a fur cloak and a painted face|a hand drum; a bundle of herbs|a campfire clearing; a tent of animal hides|beating a drum; waving smoke from a bundle
nun|a long habit and a veil; a plain grey dress and a headscarf|a string of beads; a prayer book|a convent garden; a cloister|walking slowly; reading in silence
pagan priestess|a flowing robe and a flower crown; a hooded cloak and silver jewellery|a chalice; a wand|a candlelit grove; a stone altar outdoors|raising a chalice; drawing a circle on the ground
vodou priest|a white outfit and a headscarf; a bright shirt and many beaded necklaces|a rattle; a flag with sequins|a temple courtyard with drums; a candlelit altar|shaking a rattle; pouring a libation
Sufi mystic|a white robe and a tall felt hat; a wide skirt|a reed flute; a string of prayer beads|a round hall with a wooden floor; a courtyard|turning in slow circles; playing a flute
yogi|a white wrap and a long beard; simple robes|a string of beads; a mat|a riverbank at dawn; a cave|sitting in a lotus position; chanting
pilgrim|a plain cloak and a walking staff; a hooded shirt and a backpack|a walking staff; a scallop shell|a long dusty road; a mountain path|walking with a staff; resting at a shrine
church organist|a black dress and a cardigan; a dark suit|an organ keyboard; sheet music|a gallery of a church; behind an organ|playing a hymn; turning a page""",
}
SECTORS = list(RAW)
def parse():
    out = {}
    for sec, txt in RAW.items():
        for ln in txt.strip().split('\n'):
            parts = ln.split('|')
            assert len(parts) == 5, ln[:60]
            n, o, t, w, a = parts
            out[n] = (sec, [x.strip() for x in o.split(';')], [x.strip() for x in t.split(';')], [x.strip() for x in w.split(';')], [x.strip() for x in a.split(';')])
    return out
