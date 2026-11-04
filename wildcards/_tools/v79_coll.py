"""v79 stage B - money (mo_) and metalware (mt_) collections. Invented marks only; no real currency names or people."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from famlib import P
def A(l): return 'an' if l[0].lower() in 'aeio' or (l[0].lower() == 'u' and not l.lower().startswith(('uni', 'use'))) else 'a'

COND = P("in mint condition; lightly handled with a soft patina; worn smooth on every raised edge; scratched and dull; toned dark with age; missing a small part; bent and straightened; freshly cleaned to a high shine; dusty from years in a drawer; heavily used and dented; covered in tiny marks of use")
DISPLAY = P("on a velvet tray; in a glass-topped display case; on a wooden table beside a lamp; in a collector's album; on a shop counter; on a folded cloth; in a shallow dish; under a magnifying lamp; on a market stall table; in an open drawer")
SERVICE = P("a handwritten price label; a paper tag tied on with string; scratched owner's initials; a faded paper label; a dated inscription; a small stamp; a chip on one edge; a tiny hole drilled near the edge")
# name|types|materials|features|eras|mark place
MO = {
 'coin': ('coin', "a small round coin with a ridged edge; a large heavy coin the size of a biscuit; a thin square-holed coin; a six-sided coin with a raised rim; a tiny thin coin the size of a fingernail; a holed round coin on a string; a chunky roughly hammered coin; a two-metal coin with a bright centre and a darker ring; a scalloped-edge coin; a very worn coin with a faint head in profile",
  "silver; copper; brass; bronze; nickel; gold; steel; aluminium", "a crowned head in profile; a ship in full sail on one face; a wreath of leaves round the edge; a number in the centre; a tiny star above the date; a smooth blank reverse; a deep scratch across the face; an old bend in the rim",
  "from the 1600s; from the 1700s; from the 1800s; from the 1900s; from the 1950s; from the 1970s; of a current design", "face"),
 'note': ('banknote', "a long rectangular banknote with a decorated border; a small square note with a printed portrait panel; a crisp folded note; a very large old note with a wide margin; a thin plastic note with a clear window; a pale note with a watermark; a note with a red serial number; a worn soft note with a split fold; a stack of rolled notes held by a rubber band; a torn note taped back together",
  "thick cotton paper; linen paper; thin polymer; coloured card; pale tissue paper; waxed paper", "a swirling border of fine lines; a large printed number in each corner; a watermark seen against the light; a circle of tiny repeated letters; a faded purple stamp; two signatures at the bottom; a small hole punched in the corner; a folded crease down the centre",
  "from the 1900s; from the 1920s; from the 1940s; from the 1960s; from the 1980s; of a current design", "corner"),
 'purse': ('purse or wallet', "a small clasp coin purse; a long leather wallet; a folded billfold with card slots; a drawstring pouch; a snap-top purse with a chain; a beaded evening purse; a money belt; a tin coin holder with a hinged lid; a leather pouch with a long flap; a clip for notes",
  "soft leather; woven cloth; embroidered velvet; stiff canvas; snakeskin; plastic; brass and leather", "a stitched edge; a metal clasp that snaps; a faded gold stamped pattern; a zip across the top; a tiny mirror inside; a worn corner; a hidden pocket; a loop for a chain",
  "from the 1900s; from the 1920s; from the 1950s; from the 1970s; from the 1990s; of a current design", "inside"),
 'box': ('money box', "a round china pig with a slot in its back; a tall tin money box shaped like a house; a cast iron bank shaped like a bulldog; a glass jar with a slot cut in the lid; a wooden chest with a tiny padlock; a cardboard savings tube; a metal bank shaped like a post box; a clay pot with a thin slit; a clear plastic ball bank",
  "glazed china; painted tin; cast iron; glass; wood; clay; moulded plastic", "a thin coin slot in the top; a rubber plug underneath; a key in the side; a painted smile; a chipped ear; a worn painted pattern; a flat base with a small hole; a lid that lifts off",
  "from the 1890s; from the 1920s; from the 1950s; from the 1960s; from the 1980s; of a current design", "base"),
 'cheque': ('cheque or bond', "a long rectangular cheque with a printed bank name; a stock certificate with an ornate border; a folded savings bond; a small paying-in slip; a wide old share certificate with a seal; a book of tear-out cheques with a stub; a banker's draft with a punched date; a ration-style coupon with a perforated edge; a pay envelope with a window",
  "heavy printed paper; thin pale blue paper; cream card; green safety paper; stiff coloured card", "a looping handwritten amount; a scrollwork border; a raised red seal; a faded signature; a cancelled stamp across the face; a torn perforated edge; a printed picture of a ship; a faint ink stain",
  "from the 1880s; from the 1910s; from the 1930s; from the 1950s; from the 1970s; of a current design", "top"),
 'chip': ('gaming chip or token', "a round casino chip with coloured edge stripes; a stack of casino chips in different colours; a square brass gaming plaque; a transport token with a hole in the middle; a heavy brass arcade token; a plastic laundry token; a wooden market token; a bone gaming counter; a metal beer token; a pair of dice and a stack of chips",
  "clay composite; brass; plastic; wood; bone; nickel; steel", "a coloured stripe round the edge; a centre disc with a number; a hole stamped through the middle; a printed picture of a club; a worn painted edge; a tiny crest; a smooth blank face; a rim notched like a coin",
  "from the 1880s; from the 1920s; from the 1950s; from the 1970s; from the 1990s; of a current design", "face"),
 'ledger': ('account book', "a wide ledger with a cloth spine and ruled columns; a small pocket cash book with a pencil loop; a thin passbook with stamped entries; a thick bound account book with marbled edges; a roll of till receipts; a stack of invoices on a spike; a wooden tally stick split in two; a punched card of figures; a bank statement folded in thirds",
  "cloth and board; leather; thin card; thick paper; wood; stiff card", "neat columns of handwritten figures; a blotted ink stain; red ink totals underlined twice; a faded stamp on the page; a ribbon marker; a loose receipt tucked in; a corner worn soft; rubber-stamped dates in purple",
  "from the 1850s; from the 1900s; from the 1930s; from the 1950s; from the 1980s; of a current design", "cover"),
 'till': ('counting equipment', "a heavy brass cash register with raised number keys and a pop-up flag; a hand-cranked adding machine with a paper roll; a wooden abacus with coloured beads; a balance scale with a pair of brass pans and a set of weights; a coin counting tray with round recesses; a wooden cash drawer with a bell; a coin sorting machine with a tilted chute; a pocket calculator with large grey keys",
  "polished brass; painted steel; wood; chrome; cast iron; plastic", "a bell that rings when the drawer opens; a row of round numbered keys; a paper tape curling out; a worn wooden handle; a coin tray with five slots; a cracked glass display; a hand-painted price sign; a small brass plate with the maker's name",
  "from the 1880s; from the 1910s; from the 1940s; from the 1960s; from the 1980s; of a current design", "plate"),
 'bar': ('bullion or ingot', "a heavy rectangular ingot with rounded edges; a small thin bar like a chocolate tablet; a stack of three gold-coloured bars; a flat disc of metal the size of a saucer; a rough nugget the size of a walnut; a small bar in a sealed plastic case; a long thin rod of metal; a twisted ribbon of metal",
  "gold; silver; copper; platinum; brass; lead", "a stamped weight and purity mark; a row of small serial digits; a stamped hallmark; a dull brushed top; a worn dent; a slightly rough poured surface; a mark from the mould; a tiny maker's stamp",
  "from the 1850s; from the 1900s; from the 1930s; from the 1960s; from the 1990s; of a current design", "top"),
}
MT = {
 'brass': ('brassware', "a tall candlestick with a round base; a bulbous hand bell with a wooden handle; a shallow bowl with a rolled edge; a pair of vases with flared tops; a trumpet-shaped jug with a loop handle; a squat kettle with a swan-neck spout; a decorative wall plate with a raised pattern; a long-handled warming pan; a set of three graduated weights; a small ship's lamp with a glass chimney",
  "polished brass; dark brass; lacquered brass; cast brass; brass over a copper core", "engraved scrollwork; a hammered surface; a green patina in the creases; a bright polished rim; a pair of loop handles; a worn maker's mark underneath; a smooth domed lid; a row of tiny beads round the edge",
  "from the 1700s; from the 1850s; from the 1900s; from the 1930s; from the 1960s; of a current design", "base"),
 'copper': ('copperware', "a round-bellied saucepan with a long iron handle; a tall coffee pot with a long beak; a shallow oval fish kettle with a lid; a jelly mould shaped like a fluted crown; a big stockpot with two side handles; a hammered mixing bowl; a ladle with a long curved handle; a pair of graduated measuring jugs; a copper kettle with a hinged lid; a bed warmer with a perforated lid",
  "hammered copper; tinned copper; polished copper; copper with a brass handle; copper with an iron handle", "dents from long use; a tinned inner lining worn through in places; copper rivets; a dark tarnished outside; a rim rolled over a wire; a heavy base with a ring of marks; a stamped maker's name; a green stain at the handle",
  "from the 1700s; from the 1800s; from the 1900s; from the 1930s; from the 1960s; of a current design", "base"),
 'pewter': ('pewterware', "a lidded tankard with a thumb rest and a glass base; a shallow plate with a wide rim; a squat teapot with a wooden handle; a footed goblet; a set of measuring tots in graduated sizes; a plain jug with a pinched spout; a candlestick with a drip tray; a pair of salt cellars; a hip flask with a screw cap; a communion plate with an engraved edge",
  "soft grey pewter; polished pewter; dark oxidised pewter; pewter with a wooden handle; pewter with a glass base", "a dull blue-grey sheen; a row of touchmarks under the base; a hinged lid with a thumb rest; a soft scratched surface; fine turned rings round the body; a dented rim; a small engraved crest; a lid with a flat knob",
  "from the 1600s; from the 1700s; from the 1800s; from the 1900s; from the 1930s; of a current design", "base"),
 'silver': ('silverware', "a heavy table spoon with a rounded bowl; a set of six small teaspoons; a table knife with a pointed handle; a long serving fork with four tines; a footed bowl with a pierced rim; a teapot with an ivory handle; a sugar bowl with a hinged lid; a cake slice with an engraved blade; a pair of candlesticks with fluted columns; a napkin ring with a monogram",
  "sterling silver; silver plate; plated nickel silver; silver with a bone handle; silver with a wooden handle", "an engraved monogram; a bright cast handle with a floral pattern; a row of tiny hallmarks on the back; rubbed bright edges; dark tarnish in the grooves; a smooth mirror finish; a worn plating showing brass underneath; a beaded rim",
  "from the 1700s; from the 1800s; from the 1900s; from the 1920s; from the 1950s; of a current design", "back"),
 'iron': ('castironware', "a heavy round skillet with a short handle and a pouring lip; a deep pot with a lid and a wire handle; a flat griddle with a ridged surface; a flat iron with a curved wooden handle; a cast iron kettle with a rounded spout; a small doorstop shaped like an animal; a pair of fire tongs; a waffle iron with two hinged plates; a long-handled shovel for ashes; a boot scraper with a scrolled end",
  "cast iron; black enamelled iron; wrought iron; rusted iron; iron with a wooden handle", "a rough sand-cast surface; a raised maker's name on the base; a rust pitted rim; a seasoned black shine inside; a loop handle; a ring of small feet underneath; a number cast into the handle; a flaking enamel edge",
  "from the 1800s; from the 1880s; from the 1900s; from the 1930s; from the 1950s; of a current design", "base"),
 'tin': ('tinware', "a rectangular biscuit tin with a hinged lid; a round lunch box with a wire handle; a dented watering can with a long spout; a cylinder money tin with a slot; a pierced lantern with a candle inside; a set of nesting baking tins; a bucket with a loop handle; a square cake tin with a loose base; a small dustpan; a tin toy car with a key",
  "tinplate; painted tinplate; galvanised steel; enamelled tin; embossed tin", "a printed picture on the lid; faded red and gold paint; a rusty seam along the side; a pressed pattern of tiny dots; a sharp folded edge; a bent handle; a worn paint patch down to bare metal; a lithographed street scene",
  "from the 1880s; from the 1910s; from the 1930s; from the 1950s; from the 1970s; of a current design", "lid"),
 'lock': ('locks and keys', "a large iron padlock with a curved shackle; a ring of five old keys; a small brass padlock with a tiny key; a heavy door lock with a decorated keyhole plate; a long skeleton key with a ring-shaped head; a safe key with a flat bit; a combination padlock with a ring of numbers; a heavy iron hasp and staple; a chest lock with a hinged cover; a pair of handcuffs on a chain",
  "forged iron; solid brass; steel; blackened iron; chrome-plated steel", "a plain round keyhole; a barrel-shaped body; a rust stained shackle; a worn brass finish; a decorative scrollwork plate; a tiny maker's name on the front; a bright new key beside a dull old one; a thick chain of linked rings",
  "from the 1700s; from the 1800s; from the 1900s; from the 1930s; from the 1960s; of a current design", "face"),
 'tool': ('hand tools', "a claw hammer with a long wooden handle; a pair of heavy pliers; a hand plane with a curved wooden grip; a brace and bit with a wooden handle; a set of chisels in a roll; a long hand saw with a wooden handle; an adjustable spanner; a pair of garden shears with red handles; a hand drill with a crank; a spirit level with a wooden frame",
  "forged steel; carbon steel; cast iron and wood; chrome vanadium steel; steel with a plastic handle", "a worn wooden handle; a rust speckled blade; a sharp bright edge; a stamped maker's mark; a brass fitting that glints; a handle rubbed dark with use; a bright new part on an old tool; a painted number on the head",
  "from the 1850s; from the 1900s; from the 1930s; from the 1950s; from the 1980s; of a current design", "head"),
 'bronze': ('bronzeware', "a small statuette of a standing animal on a base; a heavy bell with a rope; a ceremonial dish with a raised pattern; a round mirror with a decorated back; a pair of bookends shaped like horses; a small bust on a square plinth; a door knocker shaped like a lion's head; a plaque with raised letters; a tall incense burner with a pierced lid; a pair of chopsticks with ringed ends",
  "dark bronze; green bronze; polished bronze; bronze with a dark patina; cast bronze", "a deep green patina in the hollows; a rubbed bright high point; a fine chased surface; a mark of the founder on the base; a heavy solid weight; a dark brown wash; raised lettering; a worn smooth face",
  "from the 1700s; from the 1850s; from the 1900s; from the 1930s; from the 1960s; of a current design", "base"),
}
FINISH = P("a bright polished shine; a dull matte grey; a warm brown patina; a mottled green and brown; a frosted silvery grey; a dark blackened look; a soft golden glow; a crackled dull surface; a speckled bronze colour")
def build(final=None):
    G = {}
    ep = []
    for pre, C, what in (('mo', MO, 'money'), ('mt', MT, 'metalware')):
        G['%s_condition' % pre] = COND; G['%s_display' % pre] = DISPLAY; G['%s_service' % pre] = SERVICE
        if pre == 'mt': G['mt_finish'] = FINISH
        allp = []
        for k, (noun, types, mats, feats, eras, mk) in C.items():
            G['%s_%s_type' % (pre, k)] = P(types); G['%s_%s_material' % (pre, k)] = P(mats); G['%s_%s_feature' % (pre, k)] = P(feats); G['%s_%s_era' % (pre, k)] = P(eras)
            G['%s_%s_marks' % (pre, k)] = ['with the maker name __text_brand__ stamped on the %s' % mk, 'with a small mark of __text_logo_emblem__ on the %s' % mk, 'with a paper label on it reading __text_brand__', 'with no marks at all']
            fin = ', with __mt_finish__' if pre == 'mt' else ''
            G['%s_%s_look' % (pre, k)] = ['__%s_%s_type__, __%s_%s_era__, made of __%s_%s_material__%s, with __%s_%s_feature__, __%s_%s_marks__' % (pre, k, pre, k, pre, k, fin, pre, k, pre, k)]
            G['%s_%s_prompt' % (pre, k)] = ['A collectable %s piece, shown as __%s_%s_look__. It is __%s_condition__, with __%s_service__, and it is __%s_display__.' % (what, pre, k, pre, pre, pre)]
            G['%s_%s_short' % (pre, k)] = ['__%s_%s_type__, __%s_%s_era__, made of __%s_%s_material__.' % ((pre, k) * 3)]
            G['%s_%s_group_prompt' % (pre, k)] = ['Three pieces of %s are shown together. The first is __%s_%s_short__ The second is __%s_%s_short__ The third is __%s_%s_short__ They are all __%s_condition__, and they are __%s_display__.' % (noun, pre, k, pre, k, pre, k, pre, pre)]
            allp.append(k)
        for s_ in ('prompt', 'group_prompt', 'short'): G['%s_%s' % (pre, s_)] = ['__%s_%s_%s__' % (pre, k, s_) for k in allp]
        ep += ['%s_prompt' % pre, '%s_group_prompt' % pre, '%s_short' % pre] + ['%s_%s_prompt' % (pre, k) for k in allp]
    G['v79_coll_entry_points'] = ep
    return G
if __name__ == '__main__': print(len(build()))
