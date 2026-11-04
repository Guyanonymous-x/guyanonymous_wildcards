"""Helmets, suits of armour, body armour, gauntlets, codpieces, capes and cloaks, greaves and shields from cultures across time. Garment/object descriptions only."""
import os, re, sys, random, zlib
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from paths import FINAL
def rg(*k): return random.Random(zlib.crc32('|'.join(map(str, k)).encode()))
def S(x): return [i.strip() for i in x.split(';') if i.strip()]
A = {}
def cat(k, rows): A[k] = [tuple(x.strip() for x in l.split('|')) for l in rows.strip().split('\n') if l.strip()]
cat('helmet', """
corinthian helmet|ancient Greece|a bronze helm covering the whole head with narrow eye and nose slits
Attic helmet|ancient Greece|an open-faced bronze helm with cheek guards
Roman legionary helmet|Rome|an iron bowl with a neck guard, cheek plates and a brow ridge
centurion crested helmet|Rome|a polished helm topped with a transverse horsehair crest
gladiator helmet|Rome|a heavy visored helm with a broad brim and a decorative crest
Viking spectacle helmet|Scandinavia|an iron cap with a nose guard and eye-ring brow bands
Norman nasal helmet|medieval Europe|a conical steel cap with a long nose bar
great helm|medieval Europe|a flat-topped cylindrical steel helm with eye slits and breathing holes
bascinet|medieval Europe|a pointed steel helm with a movable visor and mail aventail
sallet|medieval Europe|a rounded helm with a tail for the neck and a slit visor
armet|Renaissance Europe|a close helmet with hinged cheek plates and a visor
burgonet|Renaissance Europe|an open helm with a peak and cheek pieces
morion|Spain|a crescent-shaped open helmet with a high comb
kabuto|Japan|a lacquered iron bowl with flared neck plates and a sweeping crest
Mongol lamellar helmet|steppe Asia|a rounded iron cap with a plume and a lamellar neck curtain
Persian turban helmet|Persia|a spiked steel helm with a mail neck cover
Ottoman helm|Ottoman Empire|a steel bowl with a tall spike and a nose guard
Chinese Tang helmet|China|a steel bowl with ear flaps and a tall decorative plume
Indian chilah helmet|India|a bowl helm with a nasal bar and a mail skirt
Ethiopian horn helmet|Africa|a leather and brass helm decorated with horns
Aztec jaguar helmet|Mesoamerica|a wooden or leather helmet carved as an open jaguar mouth
Aztec eagle helmet|Mesoamerica|a feathered helm shaped as an eagle head
Maori warrior helmet|Pacific|a woven fibre helm with carved ornaments
Kiribati coconut-fibre helmet|Pacific|a woven helm covered with a spiky puffer-fish skin
Hawaiian mahiole|Hawaii|a feathered helmet with a high crest
Celtic horned helmet|Iron Age Europe|a bronze helm decorated with sculpted horns
Samurai menpo mask|Japan|a fierce iron face guard with a moustache
Greek Boeotian helmet|ancient Greece|a broad-brimmed bronze hat helm
pickelhaube-style spiked helmet|Europe|a leather-and-steel helm topped with a spike
winged helm|myth|a polished helm with large feathered wings
dragon helm|fantasy|a scaled helm with a crest of spines
""")
cat('armor', """
full plate armour|late medieval Europe|a complete suit of articulated polished steel plates
Gothic plate harness|Germany|a fluted steel suit with pointed details
Maximilian armour|Renaissance Germany|a fluted suit with sharply decorative ridges
chainmail hauberk|medieval Europe|a long shirt of riveted iron rings reaching the knees
scale armour|steppe Asia|a coat of overlapping small metal plates sewn onto cloth
lamellar armour|Asia|a cuirass of laced metal plates in rows
O-yoroi|Japan|a boxy suit of laced plates with large shoulder guards
do-maru|Japan|a lighter wrap-around suit of laced plates
tosei gusoku|Japan|a fitted suit of plates with a front plate and a curved shoulder guard
brigandine|medieval Europe|a coat with small plates riveted under cloth, studded on the outside
muscle cuirass|ancient Greece|a bronze breastplate sculpted with a muscled chest
lorica segmentata|Rome|a suit of overlapping steel strips and plates around the torso
lorica squamata|Rome|a coat of overlapping bronze scales
linothorax|ancient Greece|a layered linen cuirass stiffened with glue
Viking mail shirt|Scandinavia|a short riveted mail coat
Samurai tatami armour|Japan|a folding suit of small plates for travel
Mongol leather lamellar|steppe Asia|a coat of lacquered leather lamellae
Persian four-mirror armour|Persia|four polished steel plates on a mail coat
Indian kavacha|India|a quilted coat with a metal plate
Chinese mountain-pattern armour|China|a suit of overlapping metal scales in a mountain pattern
Aztec ichcahuipilli|Mesoamerica|a quilted cotton armour padded with salt
Hawaiian woven armour|Hawaii|a suit of woven fibre
Polynesian coconut armour|Pacific|woven coconut-fibre armour in layers
boiled leather cuirass|world|a moulded and hardened leather breastplate
Zulu hide shield and kilt|southern Africa|a cowhide shield and a kilt of animal tails
Spartan hoplite panoply|ancient Greece|a bronze cuirass, helmet and greaves
Mamluk armour|Egypt|a lamellar and mail suit
Ottoman cavalry plates|Ottoman Empire|a mail-and-plate suit
fantasy elven armour|fantasy|a slim suit of leaf-shaped plates
fantasy dwarven armour|fantasy|a heavy suit of rune-engraved plates
""")
cat('gauntlet', """
plate gauntlets|medieval Europe|steel finger plates articulated over leather
mitten gauntlets|medieval Europe|steel mitten-shaped hand guards
Japanese kote|Japan|armoured sleeves with plated hand guards
mail mittens|medieval Europe|gloves of riveted rings
leather bracers|world|laced forearm guards
vambraces|world|plated forearm guards
Roman manica|Rome|segmented arm guard
Mongol lamellar gloves|steppe Asia|a leather glove with small metal plates
Persian hand guards|Persia|embossed steel
spiked gauntlets|fantasy|steel gloves with spikes on the knuckles
""")
cat('codpiece', """
Renaissance codpiece|Europe|a padded and decorated pouch at the front of the hose
steel codpiece|Europe|a metal armoured guard shaped over the crotch
slashed fabric codpiece|Europe|a showy pouch of slashed and puffed velvet
leather codpiece|Europe|a sculpted leather pouch with studs
jewelled codpiece|Europe|an ostentatious pouch with gems and gold braid
fantasy plate codpiece|fantasy|a polished curved metal shield for armour
Roman subligaculum|Rome|a wrapped loincloth
fundoshi|Japan|a cloth loincloth wrapped and knotted
loincloth|world|a simple strip of cloth
""")
cat('cape', """
heroic cape|fantasy|a long flowing cape in a bold colour with a high collar
fur-trimmed cloak|medieval Europe|a heavy cloak with a thick fur border
hooded cloak|medieval Europe|a long woollen cloak with a deep hood
Roman paludamentum|Rome|a purple military cloak fastened at the shoulder
sagum|Rome|a rough woollen soldier's cloak
Greek chlamys|ancient Greece|a short cloak pinned at the shoulder
Viking cloak|Scandinavia|a heavy wool cloak with a round brooch
Highland plaid|Scotland|a long length of tartan wool wrapped and belted
Ottoman kaftan cape|Ottoman Empire|a long embroidered cape
Mongol deel cape|Mongolia|a heavy fur-lined wrap
Hawaiian feather cloak|Hawaii|a cape covered in thousands of red and yellow feathers
Maori feather cloak|New Zealand|a cloak of woven flax with feathers
Zulu leopard-skin cape|southern Africa|a cloak of leopard hide
cardinal cape|Europe|a long scarlet silk cape with an ermine collar
vampire cape|fantasy|a high-collared black cape with a red lining
superhero cape|fantasy|a bright cape clasped at the neck
wizard robe cloak|fantasy|a star-embroidered cloak
Roman scarlet sagum cape|Rome|a short rectangular cloak in red wool
ceremonial feathered mantle|Pacific|a mantle of woven feather panels
""")
cat('shield', """
round shield|Viking Scandinavia|a painted wooden boss shield
kite shield|Norman Europe|a long teardrop-shaped shield
heater shield|medieval Europe|a triangular shield with a flat top
Roman scutum|Rome|a rectangular curved shield
hoplon|ancient Greece|a large round bronze-faced shield
buckler|Europe|a small round hand shield
targe|Scotland|a round leather-covered shield with studs
Zulu isihlangu|southern Africa|a large ox-hide shield
Aztec chimalli|Mesoamerica|a round shield with feather mosaic
Maasai shield|East Africa|an oval hide shield painted in clan patterns
Mongolian leather shield|steppe Asia|a lacquered round shield
Japanese pavise|Japan|a large wooden standing shield
dhal|India|a small round shield of hide
Persian sipar|Persia|an embossed round shield
Hawaiian mat shield|Hawaii|a woven mat
fantasy tower shield|fantasy|a full-length shield with an emblem
""")
cat('greave', """
plate greaves|medieval Europe|steel plates over the shins
Greek bronze greaves|ancient Greece|moulded shin guards clipped around the calf
Samurai sune-ate|Japan|splint shin guards
mail chausses|medieval Europe|leggings of riveted rings
sabatons|medieval Europe|armoured shoes of overlapping plates
leather leg wraps|world|wrapped lacings
""")
MAT = S("polished steel; blackened steel; bronze; brass; gilded metal; hardened leather; lacquered leather; layered linen; silk cord lacing; iron rings; embossed copper; rawhide; wool; velvet; fur; silk; feathers; woven fibre; carved wood; enamelled plates")
DEC = S("engraved scrollwork; gold inlay; a coloured plume; a horsehair crest; rivets along the edges; etched geometric bands; a heraldic emblem; fine filigree; lacquered colour; red cord lacing; a studded border; a painted crest; a leather lining; a fur trim; tassels; a polished edge; hammered dents; battle scratches")
MATC = {'helmet': S('polished steel; blackened steel; bronze; brass; hardened leather; lacquered iron; embossed copper; gilded metal; woven fibre; carved wood; enamelled plates'), 'armor': S('polished steel; blackened steel; bronze; hardened leather; lacquered leather and silk cord; riveted iron rings; layered linen; enamelled plates; quilted cotton; woven fibre'), 'gauntlet': S('polished steel; hardened leather; riveted iron rings; embossed copper; lacquered leather; bronze'), 'codpiece': S('steel; hardened leather; velvet; padded silk; brass; slashed satin; gilded metal'), 'cape': S('wool; velvet; fur; silk; satin; feathers; woven flax; hide; heavy linen; brocade'), 'shield': S('painted wood; bronze; hide over wood; hardened leather; steel; woven fibre; lacquered wood; embossed copper'), 'greave': S('polished steel; bronze; hardened leather; riveted iron rings; lacquered plates; laced hide')}
COND = S("shining new; battle-worn; ceremonial; weathered; ornate; plain and practical; ancient and tarnished; lovingly restored; museum-grade")
def build():
    G = {}; allx = []
    for k, rows in A.items():
        out = []
        for name, culture, desc in rows:
            for i in range(6):
                R = rg('ar', name, i)
                out.append(f"{R.choice(COND).capitalize()} {name} from {culture}: {desc}; made of {R.choice(MATC[k])}, with {R.choice(DEC)} and {R.choice(DEC)}.")
        G[f'armor_{k}'] = sorted(set(out)); G[f'armor_{k}_name'] = [f'{n} ({c})' for n, c, d in rows]; allx += out
    G['armor'] = sorted(set(allx)); G['armor_material'] = MAT; G['armor_decoration'] = DEC
    G['armor_prompt'] = ['__armor_helmet__', '__armor_armor__', '__armor_gauntlet__', '__armor_codpiece__', '__armor_cape__', '__armor_shield__', '__armor_greave__', '__armor_armor__ with __armor_helmet__ and __armor_cape__', '__armor_helmet__ with __armor_gauntlet__']
    return G
def run(final):
    G = build()
    for n, l in G.items(): open(os.path.join(final, n + '.txt'), 'w', encoding='utf8', newline='\n').write('\n'.join(l) + '\n')
    print('armor:', len(G), 'files;', len(G['armor']), 'descriptions'); return G
def export_aoo(out, prefix='aoo_'):
    G = build(); names_ = set(G); ref = re.compile(r'__([A-Za-z0-9_\-/]+)__'); n = 0
    for name, lines in G.items():
        keep = list(dict.fromkeys(ref.sub(lambda m: '__' + prefix + m.group(1) + '__' if m.group(1) in names_ else m.group(0), l) for l in lines))
        if not name.startswith('armor_prompt'): random.Random(zlib.crc32(name.encode())).shuffle(keep)
        open(os.path.join(out, prefix + name + '.txt'), 'w', encoding='utf8', newline='\n').write('\n'.join(keep) + '\n'); n += 1
    return n
if __name__ == '__main__':
    a = [x for x in sys.argv[1:] if os.path.isdir(x)]; run(os.path.abspath(a[0]) if a else FINAL)
