"""Umbrellas, hand fans, aprons, body jewellery, keychains, handkerchiefs, lanyards, charms and pouches."""
from vocab_lib import S
from vocab_acc_wardrobe2 import SL, P, SLOTS as S2
from vocab_acc_wardrobe3 import SLOTS as S3
NEW = ['umbrella', 'fan', 'apron', 'bodyjewel', 'keychain', 'handkerchief', 'lanyard', 'charm', 'pouch']
CLS = {'umbrella': 'bag', 'fan': 'scarf', 'apron': 'bag', 'bodyjewel': 'ear', 'keychain': 'ear', 'handkerchief': 'scarf', 'lanyard': 'bag', 'charm': 'ear', 'pouch': 'bag'}
TECHC = {'umbrella': 'bag', 'fan': 'knit', 'apron': 'bag', 'bodyjewel': 'metal', 'keychain': 'metal', 'handkerchief': 'knit', 'lanyard': 'bag', 'charm': 'metal', 'pouch': 'bag'}
PAIR = set()
KIT = {'metal': S3['brooch'], 'text': S2['scarf'], 'leather': S3['belt']}
KITOF = {'umbrella': 'leather', 'fan': 'text', 'apron': 'leather', 'bodyjewel': 'metal', 'keychain': 'metal', 'handkerchief': 'text', 'lanyard': 'leather', 'charm': 'metal', 'pouch': 'leather'}
def HW(frames, low, mid, high): return [SL(frames, low, mid, high)]
HWS = {
 'umbrella': HW(["It has {}.", "The handle is {}."], "a plastic handle, a plain push button, a basic hook handle, a plain fibreglass rib, a simple strap", "a curved wooden handle, a straight handle, a push-button opener, a wind-resistant frame, a leather-wrapped handle, an auto open and close button, a metal shaft, a wrist strap", "a hand-carved handle, a hand-turned wooden shaft, a horn handle, a silver collar, a hand-stitched leather handle, a gold-plated tip, a bamboo crook, a carved bone handle"),
 'fan': HW(["It has {}.", "It is held by {}."], "plastic ribs, a plain cord, a simple paper face, plain wooden sticks, a basic rivet", "slim bamboo ribs, lacquered sticks, a silk tassel, a carved wooden guard, a brass rivet, a leather loop, a folding frame, a feather quill", "hand-carved ivory-look ribs, mother-of-pearl sticks, filigree guards, hand-painted sticks, a pearl rivet, a gold chain, a silk cord with a gem, hand-carved sandalwood sticks"),
 'apron': HW(["It ties with {}.", "It has {}."], "a plain neck strap, a simple waist tie, a plastic buckle, an elastic strap, a plain snap", "crossed back straps, an adjustable neck strap, a long waist tie, a metal buckle, brass rings, a D-ring neck, a leather strap, a quick-release clip", "hand-stitched leather straps, brass slides, hand-forged buckles, hand-braided cord ties, silk ties, a hand-sewn adjustable strap, a hand-polished brass ring"),
 'bodyjewel': HW(["It fastens with {}.", "It is closed by {}."], "a plain ring closure, a simple bar, a basic snap, a plain post, a basic ball end", "a captive bead ring, a threaded ball end, a hinged ring, a clip-on closure, a lobster clasp, a screw-on ball, a push-in post, a segment ring, a magnetic clasp", "a hand-fitted gold clasp, a threadless gold end, a hinged gold segment, a hand-set stone end, a platinum clasp, a secret hinge, a hand-turned gold screw"),
 'keychain': HW(["It has {}.", "It attaches with {}."], "a plain split ring, a simple clip, a basic lobster hook, a plastic fob, a simple loop", "a swivel clasp, a split ring, a lobster clip, a carabiner clip, a leather loop, a chain tether, a screw-lock clip, a quick-release ring", "a hand-forged gold ring, a hand-polished carabiner, a gold swivel clasp, a hand-stitched leather loop, a solid-silver clip, a hand-made brass hook"),
 'handkerchief': HW(["It has {}.", "The edge is finished with {}."], "a plain hem, a raw edge, a basic overlock, a printed border, a simple stitch", "a rolled hem, a hemstitched edge, a mitred corner, a contrast border, a scalloped edge, a lace trim, a hand-rolled edge, a woven border", "a hand-rolled silk edge, a hand-sewn drawn-thread border, a fine lace edge, a hand-embroidered border, a hand-mitred corner, a Tatted lace edge, a hand-turned silk hem"),
 'lanyard': HW(["It has {}.", "It clips with {}."], "a plastic clip, a plain bulldog clip, a simple loop, a basic lobster clip, a snap", "a swivel hook, a breakaway clasp, a lobster clip, a badge clip, a safety release, a split ring, a D-ring, a metal slider", "a hand-forged brass hook, a hand-polished silver clip, a gold swivel, a hand-stitched leather clip, a hand-made safety breakaway, a solid-silver slider"),
 'charm': HW(["It hangs from {}.", "It has {}."], "a plain jump ring, a simple loop, a basic clip, a plain eye pin, a plastic bail", "a soldered jump ring, a lobster clasp, a bail, a spring ring, a screw-in loop, an eye pin, a slide bail, a clip-on bail", "a hand-soldered gold ring, a gold lobster clasp, a hand-made bail, a hand-fitted loop, a diamond-set bail, a platinum ring"),
 'pouch': HW(["It closes with {}.", "It has {}."], "a plain drawstring, a snap, a basic zipper, a velcro tab, a simple cord", "a drawstring with toggle, a zipper, a snap button, a flap, a magnetic clasp, a leather tie, a kiss-lock clasp, a toggle closure", "a hand-braided drawstring, a gold clasp, a hand-stitched flap, a hand-forged clasp, a silk cord with a tassel, a hand-sewn lining and gold zipper"),
}
SLOTS = {c: dict(trim=KIT[k]['trim'], finish=KIT[k]['finish'], interior=KIT[k]['interior'], hardware=HWS[c]) for c, k in KITOF.items()}
PRACT = {
 'umbrella': S("a wind-resistant frame, a quick-dry canopy, a one-touch opener, a UV-blocking coat, a reflective trim, a compact fold, a double canopy, a non-slip handle, a drip-free cap, a cover sleeve, a hidden strap, a vented top"),
 'fan': S("a light folding frame, a secure rivet, a tassel loop, a stiff ribbed face, a gentle breeze, a protective sleeve, a wrist cord, a scented panel, a slim case, a smooth easy opening"),
 'apron': S("a deep front pocket, an adjustable neck strap, a tool loop, a towel loop, a wipe-clean surface, a heat-resistant panel, a waterproof coat, a crossed back, a hidden pocket, a long tie, a hammer loop, a spare strap"),
 'bodyjewel': S("a hypoallergenic metal, a nickel-free build, an easy-open clasp, an implant-grade finish, a smooth polish, a lightweight build, a secure threaded end, a rounded comfortable edge, a flexible fit, a skin-friendly coating"),
 'keychain': S("a quick-release ring, a bottle opener, a small light, a whistle, a screwdriver, a tiny knife-free multitool, a tracker pocket, a detachable ring, a loud clasp, a flat low profile, a ring for several keys"),
 'handkerchief': S("an absorbent weave, a washable fabric, a generous size, a fine soft hand, a wrinkle-resistant weave, a quick-dry fabric, an anti-fray edge, a lightweight build, a folded pocket size"),
 'lanyard': S("a breakaway safety clasp, a badge holder, a swivel hook, a detachable clip, a reflective thread, a padded neck band, a wide strap, a key ring, an anti-twist swivel, a wrist loop"),
 'charm': S("a secure ring, a hypoallergenic finish, a small engraved message, a tarnish-resistant coating, a lightweight build, a hollow build, a smooth rounded edge, a cheerful rattle"),
 'pouch': S("a zippered main compartment, a drawstring cord, a slip pocket, a card slot, a waterproof lining, a belt loop, a key clip, a padded lining, a wipe-clean surface, a lightweight build"),
}
PLACE = {
 'umbrella': S("on the canopy, on the handle, on the tip, on the ribs, on the edge, on the strap"),
 'fan': S("on the face, on the guard, on the sticks, on the tassel, on the edge, on the back"),
 'apron': S("on the bib, on the pocket, at the waist, on the strap, at the hem, on the ties"),
 'bodyjewel': S("on the ring, on the end, on the front, on the clasp, on the length, on the bar"),
 'keychain': S("on the fob, on the ring, on the tag, on the clasp, on the loop, on the front"),
 'handkerchief': S("at one corner, at the centre, along the border, in the corner, on the edge, on the hem"),
 'lanyard': S("on the strap, on the clip, on the end, along the length, on the badge, on the hook"),
 'charm': S("on the front, on the loop, on the back, on the edge, at the centre, on the ring"),
 'pouch': S("on the flap, on the front, on the drawstring, on the zipper pull, on the base, on the back"),
}
TYPES = {
 'umbrella': P("""compact folding umbrella|It is a short umbrella that folds small.
long-shaft umbrella|It is a full-length umbrella with a hooked handle.
golf umbrella|It is a large vented umbrella.
stick umbrella|It is a long umbrella with a straight shaft.
bubble umbrella|It is a clear dome umbrella.
automatic umbrella|It opens with the touch of a button.
double-canopy umbrella|It has two layers of fabric for wind.
parasol|It is a light sun umbrella.
lace parasol|It is a delicate sun umbrella with a lace canopy.
paper parasol|It is an oiled-paper umbrella on a bamboo frame.
Japanese wagasa|It is a bamboo-ribbed oiled-paper umbrella.
Chinese oiled-paper umbrella|It is a hand-painted paper umbrella on a bamboo frame.
Indian silk parasol|It is a round silk umbrella with a fringe.
Thai bo sang parasol|It is a hand-painted umbrella made of mulberry paper.
Korean paper parasol|It is a ribbed paper parasol with a painted design.
Victorian lace parasol|It is a small folding sun umbrella with a frilled edge.
ceremonial court umbrella|It is a large round silk umbrella on a long pole.
beach umbrella|It is a big tilting umbrella with a spike.
patio umbrella|It is a large garden umbrella.
travel umbrella|It is a small light umbrella with a case.
sword-stick umbrella|It is a heavy wooden umbrella with a metal tip.
transparent umbrella|It is a clear canopy umbrella.
printed-sky umbrella|It is a canopy printed with a cloud scene.
reverse-fold umbrella|It folds the wet side inwards.
vented windproof umbrella|It has a vented canopy for gales.
children-free patterned umbrella|It has a bold pattern on the canopy.
kite-style umbrella|It has a canopy shaped like a kite.
feather umbrella|It is an umbrella with a ruffled feather canopy.
tartan umbrella|It has a woven plaid canopy.
polka-dot umbrella|It has a canopy covered in dots."""),
 'fan': P("""folding hand fan|It is a fan of ribs and a pleated face that folds shut.
brisé fan|It is a fan of joined carved sticks with no fabric.
uchiwa fan|It is a flat, round fan on a handle.
sensu fan|It is a Japanese folding fan.
Chinese silk folding fan|It is a folding fan with a painted silk face.
Chinese round fan|It is a round silk fan on a short handle.
Spanish abanico|It is a large folding fan with lace and wooden ribs.
lace fan|It is a delicate fan with a lace face.
feather fan|It is a fan made of soft feathers.
ostrich-feather fan|It is a large fan of long feathers.
peacock-feather fan|It is a fan of eye-patterned feathers.
palm-leaf fan|It is a fan made of a single leaf.
bamboo fan|It is a woven bamboo fan.
paper fan|It is a simple paper fan.
Indian hand fan|It is a woven fan with a bright border.
Filipino abanico|It is a hand-woven palm fan.
Thai palm fan|It is a round fan with a decorated border.
dancer's fan|It is a large fan used for a fan dance.
war fan|It is an iron-ribbed fan.
ceremonial fan|It is a large decorative fan on a pole.
Venetian carnival fan|It is a fan with a masked face painted on.
Victorian ball fan|It is a small fan with a pearl-set guard.
ivory-look brisé fan|It is a fan of fine carved sticks.
tortoiseshell-look fan|It is a fan with amber-toned guards.
cloisonné-handled fan|It is a fan with an enamelled handle.
printed souvenir fan|It is a cheerful printed fan.
rattan fan|It is a loose-woven fan.
cooling mist fan|It is a small fan with a soft breeze.
tasselled fan|It is a fan with a long tassel.
sandalwood fan|It is a scented carved fan."""),
 'apron': P("""bib apron|It covers the chest and falls to the knees.
waist apron|It is a half apron that ties at the waist.
bistro apron|It is a long waist apron.
cross-back apron|It has straps that cross at the back.
chef's apron|It is a sturdy cotton apron with a towel loop.
butcher's apron|It is a heavy canvas apron.
barista apron|It is a short waxed canvas apron with pockets.
blacksmith's apron|It is a thick leather apron.
welder's apron|It is a heat-resistant split-leather apron.
carpenter's apron|It has loops and pockets for tools.
gardener's apron|It has a deep front pocket for tools.
potter's apron|It is a wipe-clean apron with a front pocket.
painter's apron|It is a smock-style apron with deep pockets.
cobbler's apron|It is a leather apron with a wide front.
baker's apron|It is a long white cotton apron.
vintage half apron|It is a ruffled apron with a ribbon tie.
tea-party apron|It is a decorated frilled apron.
pinafore apron|It is a sleeveless apron dress.
smock apron|It is a long-sleeved work apron.
Japanese kappogi apron|It is a long-sleeved cotton apron.
Japanese hakama apron|It is a wide pleated waist wrap.
Indian dhoti wrap|It is a long cloth worn tied round the waist.
Mexican embroidered apron|It is an apron with bright flower embroidery.
Nordic folk apron|It is an apron in bands of woven colour.
sarong apron|It is a wrap apron tied at the side.
fishing apron|It is a waterproof apron.
barbecue apron|It is a heavy cotton apron with a large pocket.
tool-roll apron|It is a canvas apron with pockets sewn in a roll.
leather bib apron|It is a bib apron in heavy leather.
pocketed denim apron|It is a sturdy denim apron."""),
 'bodyjewel': P("""nose stud|It is a tiny jewelled stud worn in the nostril.
nose ring|It is a small ring worn in the nostril.
septum ring|It is a small ring worn through the nasal septum.
septum clicker|It is a hinged ring for the septum.
eyebrow barbell|It is a short curved bar with ball ends.
lip ring|It is a small ring worn in the lip.
labret stud|It is a flat-backed stud worn below the lip.
tongue barbell|It is a straight bar with two ball ends.
navel bar|It is a curved bar with a jewel, for the navel.
belly chain|It is a fine chain worn round the waist.
body chain|It is a delicate chain worn over the torso.
harness chain|It is a web of fine chains worn on the upper body.
arm cuff|It is a wide open band worn on the upper arm.
armlet|It is a coiled band worn on the upper arm.
ankle bracelet|It is a fine chain worn at the ankle.
anklet with bells|It is a chain with tiny ringing bells.
toe ring|It is a small ring worn on a toe.
foot chain|It is a chain worn over the foot, joining an anklet to a toe ring.
head chain|It is a fine chain worn over the head and forehead.
bindi jewel|It is a small decorative jewel worn on the forehead.
face gems|They are tiny adhesive gems worn on the face.
temple chain|It is a fine chain worn across the temples.
collar chain|It is a delicate chain worn at the collarbone.
hand harness|It is a chain bracelet joined to rings.
finger chain|It is a chain linking a ring to a bracelet.
ear-to-nose chain|It is a fine chain from the ear to the nose.
thigh chain|It is a delicate chain worn round the thigh.
waist beads|They are strings of beads worn round the hips.
shoulder chain|It is a chain worn across the shoulders.
Maasai beaded collar|It is a wide flat beaded collar worn on the neck.
Berber nose jewel|It is a tiny silver stud with a coral bead.
Indian nath nose ring|It is a large ornate nose ring with a chain to the ear.
Ndebele neck rings|They are stacked coil rings worn at the neck.
Fulani hair-and-nose rings|They are gold pieces worn in the nose and hair."""),
 'keychain': P("""leather fob keychain|It has a stitched leather tab.
metal bar keychain|It has a solid metal bar.
carabiner keychain|It has a clip for easy attachment.
tassel keychain|It has a swinging tassel.
pom-pom keychain|It has a soft pom-pom.
fur-ball keychain|It has a fluffy fur ball.
acrylic charm keychain|It has a printed clear charm.
enamel keychain|It has a bright enamel tag.
woven lanyard keychain|It has a braided cord loop.
paracord keychain|It has a woven survival cord.
bottle-opener keychain|It has a built-in bottle opener.
mini flashlight keychain|It has a tiny light.
whistle keychain|It has a small whistle.
beaded keychain|It has strings of beads.
wristlet keychain|It has a stretch coil loop for the wrist.
retractable keychain|It extends on a spring cord.
snap-hook keychain|It has a sprung gate.
miniature book keychain|It has a tiny book charm.
tiny globe keychain|It has a spinning globe.
puzzle-ring keychain|It has interlocking rings.
carved wood keychain|It has a hand-carved tag.
brass-tag keychain|It has a hand-stamped brass tag.
stuffed animal keychain|It has a small soft animal.
miniature plant keychain|It has a tiny resin plant.
glow-in-the-dark keychain|It glows softly in the dark.
magnetic keychain|It has a magnetic clasp.
fabric loop keychain|It has a loop of printed ribbon.
Moroccan leather keychain|It has a leather tag with a tassel.
Japanese omamori keychain|It has a small brocade charm.
Indian mirror-work keychain|It has a small embroidered pouch with tiny mirrors."""),
 'handkerchief': P("""cotton handkerchief|It is a plain square of cotton.
linen handkerchief|It is a crisp square of linen.
silk pocket square|It is a small square of silk, folded into a pocket.
pocket square with printed border|It is a square of fine cloth with a printed border.
lace-edged handkerchief|It is a handkerchief with a lace border.
hand-embroidered handkerchief|It has a hand-embroidered flower in one corner.
hemstitched handkerchief|It has a drawn-thread border.
monogram-free initial-free handkerchief|It is a plain handkerchief with a rolled edge.
bandana|It is a large printed cotton square.
paisley bandana|It is a bandana covered in teardrop swirls.
polka-dot bandana|It is a bandana covered in dots.
Indian block-print handkerchief|It is a cotton square printed with carved blocks.
Japanese tenugui|It is a long thin cotton cloth with dyed patterns.
Japanese furoshiki handkerchief|It is a small wrapping cloth.
Irish linen handkerchief|It is a fine linen square with a hand-rolled hem.
Swiss cotton handkerchief|It is a very fine cotton square with a printed border.
tatted-edge handkerchief|It has an edge of tiny knotted lace.
crocheted-edge handkerchief|It has an edge of crocheted loops.
tartan handkerchief|It is a woven plaid square.
batik handkerchief|It is a square painted with wax-resist designs.
ikat handkerchief|It has a soft blurred woven pattern.
map-print handkerchief|It is printed with a detailed map.
floral handkerchief|It is printed with flowers.
striped handkerchief|It is printed in bold stripes.
spotted neckerchief|It is a spotted square tied at the neck.
bridal handkerchief|It is a lace handkerchief with a small ribbon.
Victorian mourning handkerchief|It is a plain square with a dark border.
travel handkerchief|It is a quick-dry square.
silk twill pocket square|It is a thick twill silk square.
cashmere pocket square|It is a soft cashmere square."""),
 'lanyard': P("""neck lanyard|It is a strap worn round the neck.
wrist lanyard|It is a short strap worn at the wrist.
breakaway lanyard|It has a clasp that releases under force.
badge lanyard|It has a clip for a badge.
braided cord lanyard|It is a plaited cord.
paracord lanyard|It is a woven cord.
leather lanyard|It is a stitched leather strap.
beaded lanyard|It is a string of beads.
ribbon lanyard|It is a satin ribbon with a clip.
woven lanyard|It is a woven strap with a pattern.
reflective lanyard|It has reflective thread.
padded lanyard|It has a soft neck pad.
retractable lanyard|It extends on a spring reel.
clip-on lanyard|It clips at the belt.
tool lanyard|It is a strap with a clip for a tool.
camera-free key lanyard|It is a strap with a swivel hook for keys.
whistle lanyard|It has a whistle on the end.
tassel lanyard|It has a tassel on the end.
silk-cord lanyard|It is a thin cord of braided silk.
hemp lanyard|It is a twisted cord of hemp.
nylon webbing lanyard|It is a flat tough strap.
elastic lanyard|It is a stretchy cord.
Mexican woven lanyard|It is a bright woven cord.
Maori carved lanyard|It is a cord with a carved bone toggle.
Sami braided lanyard|It is a leather cord with a pewter-thread braid.
Japanese kumihimo lanyard|It is a braided silk cord.
Andean woven lanyard|It is a woven band with small patterns.
Native-style quilled lanyard|It is a beaded or quilled strap.
macramé lanyard|It is a knotted cotton cord.
chain lanyard|It is a thin metal chain."""),
 'charm': P("""heart charm|It is a small heart-shaped pendant.
star charm|It is a small star-shaped pendant.
moon charm|It is a small crescent pendant.
sun charm|It is a small pendant with rays.
flower charm|It is a small flower pendant.
leaf charm|It is a small leaf pendant.
animal charm|It is a small figure of a creature.
cat charm|It is a tiny cat figure.
bird charm|It is a tiny bird figure.
fish charm|It is a tiny fish figure.
key charm|It is a tiny decorative key.
lock charm|It is a tiny padlock.
anchor charm|It is a tiny anchor.
compass charm|It is a tiny working compass.
clover charm|It is a small four-leaf clover.
evil eye charm|It is a blue eye-shaped talisman.
hamsa charm|It is a hand-shaped talisman.
lotus charm|It is a tiny lotus flower.
Celtic knot charm|It is a small piece of interlaced knotwork.
dream catcher charm|It is a tiny woven hoop with feathers.
Ganesha charm|It is a small figure of an elephant-headed deity.
Buddha charm|It is a small seated figure.
Saint-medal-style charm|It is a small round engraved medallion.
Japanese maneki-neko charm|It is a tiny beckoning cat.
Chinese coin charm|It is a coin with a square hole.
Turkish nazar charm|It is a small blue glass eye.
Mexican milagro charm|It is a tiny tin folk-art shape.
Navajo silver charm|It is a stamped silver pendant.
glass bead charm|It is a lampwork glass bead.
resin charm|It is a clear resin shape with something sealed in it.
miniature book charm|It is a tiny book with pages.
miniature instrument charm|It is a tiny violin or flute.
birthstone charm|It is a small stone in a setting.
locket charm|It is a tiny hinged keepsake that opens."""),
 'pouch': P("""drawstring pouch|It closes with a pulled cord.
zipper pouch|It closes with a zipper along the top.
coin pouch|It is a small pouch for coins.
belt pouch|It hangs from a belt.
leather pouch|It is a soft leather bag, closed with a thong.
tobacco-free leather pouch|It is a small folded leather pouch.
medicine pouch|It is a small neck pouch on a cord.
mojo hand pouch|It is a small flannel pouch.
amulet pouch|It is a small beaded pouch worn on a cord.
sporran|It is a pouch worn at the front of a kilt.
tool pouch|It has loops for small tools.
cosmetics pouch|It is a small zipped pouch.
jewellery roll|It is a rolled cloth with pockets.
dice bag|It is a small velvet pouch.
bead pouch|It is a small woven bag.
embroidered pouch|It is a pouch with bright embroidery.
suzani pouch|It is a pouch with bright Uzbek needlework.
Indian potli bag|It is a small drawstring bag with a beaded or embroidered face.
Japanese kinchaku|It is a drawstring pouch of kimono cloth.
Chinese embroidered pouch|It is a small silk pouch.
Sami reindeer-hide pouch|It is a soft hide pouch with a pewter clasp.
Mexican woven pouch|It is a bright woven pouch.
Andean woven coca pouch|It is a woven pouch, called a chuspa.
Maasai beaded pouch|It is a small beaded bag.
Native-style beaded strike-a-light pouch|It is a small beaded pouch.
velvet pouch|It is a soft velvet bag with a cord.
waxed canvas pouch|It is a tough zipped pouch.
mesh pouch|It is a see-through zipped pouch.
clear pouch|It is a transparent zipped pouch.
chain-strap pouch|It is a small pouch on a metal chain."""),
}
WEAR = {
 'umbrella': ['holding {} overhead', 'carrying {} at the side', 'with {} resting on one shoulder', 'under {}'],
 'fan': ['holding {} open near the face', 'fanning with {}', 'with {} half-open in one hand', 'holding {} closed'],
 'apron': ['wearing {}', 'with {} tied at the waist', 'wearing {} over everyday clothes', 'tying {} behind the back'],
 'bodyjewel': ['wearing {}', 'showing {}', 'with {} catching the light', 'wearing {} with a plain top'],
 'keychain': ['holding {} in one hand', 'with {} hanging from a belt loop', 'with {} clipped to a bag', 'swinging {} from a finger'],
 'handkerchief': ['holding {}', 'with {} folded in a pocket', 'wearing {} tied at the neck', 'with {} tucked in a sleeve'],
 'lanyard': ['wearing {} around the neck', 'with {} hanging at the chest', 'with {} looped over one wrist', 'holding up {}'],
 'charm': ['wearing {} on a chain', 'holding {} up to the light', 'with {} hanging from a bag', 'with {} clipped to a bracelet'],
 'pouch': ['carrying {}', 'with {} hanging from the belt', 'holding {}', 'with {} on a cord round the neck'],
}
