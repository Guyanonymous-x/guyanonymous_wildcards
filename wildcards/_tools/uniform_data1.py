# name|where/when|upper body|lower body|headwear|footwear|carried
# categories: each key maps to rows
U = {}
U['medical'] = """surgeon in scrubs|modern hospital|a green scrub top with a surgical gown, a paper mask and gloves|matching scrub trousers|a surgical cap|washable clogs|a clipboard
hospital nurse|modern ward|a colourful scrub top with an ID badge and a stethoscope round the neck|scrub trousers|-|white trainers|a pen light
nurse in a traditional white uniform|1950s Europe and North America|a starched white dress with a belt and a breast pocket watch|a white skirt and white stockings|a starched nurse's cap|white lace-up shoes|a fob watch
Victorian nurse|Crimean War era|a grey wool dress with a white apron and a white collar|a long skirt|a white cap|black boots|a lantern
paramedic|emergency services|a dark green jacket with reflective stripes, a high-visibility vest and a radio on the shoulder|dark cargo trousers|-|black work boots|a trauma bag
dentist|clinic|a white coat over a polo shirt with a face shield and gloves|dark trousers|a surgical cap|clinic clogs|a mirror and probe
veterinarian|clinic|a patterned scrub top with a stethoscope and a cat-print lab coat|scrub trousers|-|work shoes|a small animal carrier
pharmacist|pharmacy|a white lab coat over a shirt with a name badge|dark trousers|-|black shoes|a prescription tray
lab scientist|laboratory|a white lab coat, safety goggles and blue gloves|trousers|-|closed-toe shoes|a test tube rack
radiologist|hospital|a lead apron over a scrub top|scrub trousers|-|clinical clogs|a dosimeter badge
physiotherapist|clinic|a polo shirt with a clinic logo-free badge and a tape measure round the neck|athletic trousers|-|trainers|a resistance band
midwife|maternity ward|a tunic with a pocket full of instruments and a fob watch|trousers|-|comfortable clogs|a pinard horn
plague doctor|17th-century Europe|a long waxed black coat, a leather cape and gloves|dark trousers|a wide-brimmed hat and a beaked bird-shaped mask|dark boots|a wooden cane
barber-surgeon|medieval Europe|a stained linen apron over a wool tunic with rolled sleeves|hose|a cloth cap|leather shoes|a bleeding bowl and razors
Chinese barefoot doctor|1960s China|a plain cotton jacket with a red cross medical bag|rolled trousers|a straw hat|cloth shoes|a herbal kit
Ayurvedic practitioner|South Asia|a white kurta with a shoulder cloth|a dhoti|-|leather sandals|a small pouch of herbs
Medieval apothecary|Europe|a long wool robe with a leather apron|-|a soft hood|-|jars and a mortar
Army field medic|modern military|camouflage combat shirt with a red cross patch and body armour|combat trousers|a helmet with a red cross|combat boots|a medical pack
dental hygienist|clinic|a pastel scrub top, loupes and a mask|scrub trousers|-|clogs|a suction tool
sleep technician|clinic|a polo top and a lanyard|chinos|-|soft shoes|electrodes
optician|shop|a white coat over a shirt and tie|trousers|-|polished shoes|a pair of test frames
""".strip().split('\n')
U['emergency'] = """firefighter|modern|a heavy turnout coat with reflective bands and braces|fire-resistant overtrousers|a helmet with a visor|steel-toed boots|an axe
wildland firefighter|forest fire|a yellow flame-resistant shirt and a webbing harness|green flame-resistant trousers|a hard hat|leather boots|a pulaski tool
smoke jumper|forest fire|a padded jumpsuit with a harness|-|a helmet with a face mask|boots|a parachute pack
Victorian fireman|19th century|a double-breasted tunic with brass buttons and a wide belt|dark trousers|a tall leather helmet|boots|a brass nozzle
lifeguard|beach|a red swimsuit top with a whistle and a rescue vest|red shorts|a cap|bare feet|a rescue tube
mountain rescue volunteer|mountains|an orange shell jacket with a harness|waterproof trousers|a climbing helmet|mountain boots|a rope coil
coast guard|maritime|a navy parka with reflective tape|work trousers|a baseball cap|rubber boots|a life ring
search and rescue dog handler|outdoors|a high-visibility vest with a harness|cargo trousers|a bush hat|hiking boots|a long lead
police officer|modern|a dark shirt with a badge, shoulder patches, a utility belt and a radio|dark trousers|a peaked cap|black boots|a notebook
British bobby|London, 20th century|a dark tunic with silver buttons and a whistle chain|dark trousers|a tall custodian helmet|black boots|a truncheon
mounted police|ceremonial|a scarlet tunic with gold braid|riding breeches|a peaked helmet|tall black boots|a lance
traffic officer|road|a high-visibility jacket with white gloves|dark trousers|a reflective cap|boots|a baton
detective|1940s|a rumpled suit jacket and loose tie with a shoulder holster|suit trousers|a fedora|worn shoes|a notebook
sheriff|American West|a vest with a star badge over a plaid shirt|jeans|a wide-brimmed hat|spurred boots|a lawman's rope
Texas ranger|American West|a vest with a star badge, a long coat and a string tie|pressed trousers|a cream Stetson|boots|a lasso
customs officer|port|a navy jacket with epaulettes|trousers|a peaked cap|black shoes|a torch
prison guard|modern|a pale blue shirt with a duty belt|dark trousers|-|boots|a key ring
bailiff|court|a dark robe over a suit|-|-|polished shoes|a mace
SWAT team member|modern|a tactical vest with pouches|combat trousers|a helmet and balaclava|boots|a shield
bomb disposal technician|modern|a heavy blast suit|-|a blast helmet with a visor|heavy boots|a tool kit
Mountie|Canada|a scarlet serge tunic with brass buttons and a Sam Browne belt|navy breeches with a yellow stripe|a broad-brimmed campaign hat|tall brown boots|-
carabiniere|Italy|a black tunic with a red stripe and white cross-belts|dark trousers|a bicorne hat|boots|-
gendarme|France|a dark blue tunic with a kepi|blue trousers|a kepi|black boots|-
Hong Kong colonial police|1960s|a khaki shirt with a Sam Browne belt|khaki shorts|a peaked cap|black shoes and long socks|-
sheriff's deputy|modern|a tan uniform shirt with a star|dark green trousers|a campaign hat|boots|-
crime scene investigator|modern|a white disposable coverall with gloves|-|a hood and mask|shoe covers|an evidence bag
park ranger|national park|a green shirt with a badge and a flat-brimmed hat|olive trousers|a flat-brimmed hat|hiking boots|a field guide
""".strip().split('\n')
U['military'] = """modern infantry soldier|modern army|a camouflage combat shirt, body armour and webbing|camouflage combat trousers|a helmet|combat boots|a rucksack
fighter pilot|modern air force|a green flight suit with patches and a harness|-|a flight helmet with a visor|flight boots|an oxygen mask
Navy officer in dress whites|modern navy|a white tunic with gold epaulettes and ribbons|white trousers|a white peaked cap|white shoes|a ceremonial sword
sailor in a dress uniform|navy|a navy jumper with a white-striped sailor collar and neckerchief|bell-bottom trousers|a white sailor cap|black shoes|-
Marine dress blues|modern marines|a dark blue high-collared tunic with a white belt|blue trousers with a red stripe|a white cap|black shoes|a sword
submariner|modern navy|a blue coverall with a patch|-|a ball cap|rubber-soled shoes|-
paratrooper|WWII-era|a camouflage smock, webbing and a parachute harness|baggy trousers|a helmet|jump boots|a rifle sling
tank crew|modern|a padded coverall with a headset|-|a crewman helmet|boots|-
military band musician|ceremonial|a scarlet tunic with white cross-belts, braid and aiguillettes|dark trousers with a stripe|a tall plumed hat|polished boots|a brass instrument
Grenadier guardsman|London ceremonial|a scarlet tunic with brass buttons and white cross-belts|dark trousers|a tall bearskin hat|black boots|-
Swiss Guard|Vatican|a puff-sleeved tunic in blue, red and yellow stripes and a white ruff|striped puffed breeches|a plumed morion helmet|black shoes|a halberd
Scottish Highland soldier|ceremonial|a doublet with a plaid sash|a kilt|a feather bonnet|buckled brogues|bagpipes
Evzone|Greece|a white shirt with wide sleeves and a short embroidered jacket|a white pleated kilt-skirt with white tights|a red cap with a long tassel|red clogs with black pom-poms|-
Roman legionary|ancient Rome|a red tunic with segmented plate armour and a belt|-|a crested helmet|hobnailed sandals|a shield and short sword
Greek hoplite|ancient Greece|a bronze breastplate over a short tunic|-|a crested Corinthian helmet|greaves|a round shield and spear
Viking raider|Scandinavia|a wool tunic with a mail shirt and a fur cloak|woollen trousers with leg wraps|a round iron helmet|leather shoes|a round shield and axe
medieval knight|Europe|a mail hauberk with a heraldic surcoat and plate armour|-|a great helm|armoured boots|a longsword
samurai|feudal Japan|a lacquered armour with a silk cord over a kimono|wide hakama|a kabuto helmet|straw sandals|a katana
Mongol horse archer|13th century|a lamellar armour over a quilted coat|trousers|a fur-trimmed helmet|felt boots|a composite bow
Ottoman janissary|16th century|a long blue coat with a sash|baggy trousers|a tall felt hat with a flap|boots|a musket
Napoleonic hussar|1810s|a braided jacket with a fur-trimmed pelisse|tight breeches|a shako|tall boots|a sabre
Zulu warrior|southern Africa|a leopard-skin cape and a leather harness|a skirt of animal tails|a headband with a feather|-|a cowhide shield
American Civil War infantry soldier|1860s|a wool sack coat|wool trousers|a kepi|brogans|a musket
WWI British soldier|1914-18|a khaki tunic and webbing|puttees and breeches|a brodie helmet|hobnailed boots|a rifle
WWII British Land Girl|1940s|a green jumper and a cotton shirt|breeches|a head scarf|wellington boots|a pitchfork
Cold War astronaut trainer|1960s|a pressure suit|-|a white helmet|boots|-
Zouave|19th century|a short embroidered jacket and a sash|baggy red trousers|a red fez|spats|-
Cossack|Eastern Europe|a long coat with cartridge pouches across the chest|wide trousers|a tall fur hat|high boots|a sabre
Mughal soldier|India|a quilted coat with a sash|loose trousers|a turban|curled slippers|a curved sword
Gurkha soldier|Nepal|a green shirt with a kukri belt|trousers|a slouch hat|boots|a kukri
Maasai warrior|East Africa|a red shuka draped over one shoulder with bead collars|-|a headdress|sandals|a spear
Egyptian pharaoh's guard|ancient Egypt|a linen kilt with a broad collar|-|a striped headcloth|sandals|a spear
""".strip().split('\n')
U['aviation_sea_road'] = """airline pilot|modern airline|a white shirt with epaulettes and a dark jacket with gold stripes|dark trousers|a peaked cap|black shoes|a flight bag
flight attendant|modern airline|a tailored jacket and neckerchief with a name badge|a pencil skirt|a pillbox hat|court shoes|a trolley
1960s cabin crew member|jet age|a fitted jacket with a hat|a mini skirt|a pillbox hat|go-go boots|a tray
air traffic controller|control tower|a shirt with headset and a lanyard|trousers|-|shoes|-
airport ground crew|runway|a high-visibility jacket and ear defenders|work trousers|-|safety boots|signalling wands
aviator|1920s|a leather flying jacket with a silk scarf|breeches|a leather helmet with goggles|tall boots|-
ship captain|merchant navy|a navy double-breasted jacket with four gold stripes|trousers|a peaked cap|black shoes|a telescope
sea shanty sailor|18th century|a striped shirt with a neckerchief and a short jacket|slops|a knitted cap|bare feet|a rope
pirate captain|golden age of piracy|a long embroidered coat with a sash and cross-belt|breeches|a feathered tricorn|buckled boots|a cutlass
fisherman|North Atlantic|a thick Aran sweater with an oilskin smock|waders|a sou'wester|rubber boots|a net
lighthouse keeper|19th century|a heavy wool coat with brass buttons|wool trousers|a peaked cap|boots|an oil lamp
bus driver|modern|a waistcoat shirt with a tie and a badge|dark trousers|-|black shoes|a ticket machine
London black cab driver|modern|a jumper and a flat cap|trousers|a flat cap|shoes|a map
train conductor|steam era|a double-breasted jacket with brass buttons and a watch chain|trousers|a peaked cap|black shoes|a punch and whistle
steam locomotive engineer|1900s|a denim jacket, a red neckerchief and pinstripe overalls|overalls|a striped engineer's cap|work boots|an oil can
pullman porter|1930s|a double-breasted jacket with brass buttons|trousers|a peaked cap|black shoes|a luggage cart
hotel bellhop|1930s|a short red jacket with gold braid|trousers with a stripe|a pillbox hat with a chin strap|black shoes|a luggage trolley
doorman|grand hotel|a long coat with gold braid and epaulettes|trousers|a top hat|black shoes|an umbrella
rickshaw puller|Asia|a vest and a loose shirt|short trousers|a conical straw hat|sandals|-
gondolier|Venice|a striped boat-neck shirt and a sash|dark trousers|a flat straw boater with a ribbon|rope-soled shoes|a long oar
tuk-tuk driver|South Asia|a khaki shirt|trousers|-|sandals|-
cycle courier|city|a cycling jersey with a courier bag|cycling shorts|a cycling cap|cycling shoes|a messenger bag
Formula One driver|racing|a fireproof racing suit with sponsor-free patches|-|a helmet|racing boots|-
pit crew mechanic|racing|a fireproof overall|-|a helmet|boots|an air wrench
astronaut|space station|an orange pressure suit or a blue flight suit with mission patches|-|a white helmet with a gold visor|boots|-
cosmonaut|space program|a pale blue flight suit with a ribbed collar|-|a soft flight cap|boots|-
hot-air balloon pilot|ballooning|a windbreaker|cargo trousers|a baseball cap|boots|a map
""".strip().split('\n')
