"""Rounds 7-8: body-change wear, cold-weather, formal, regional dress gaps. Garment descriptions only. Files clothing_garment_bodychange*, _cold*, _formal*, _regional_more."""
import os, re, sys, random, zlib
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from paths import FINAL
def S(x): return [i.strip() for i in x.split(';') if i.strip()]
def R(*k): return random.Random(zlib.crc32('|'.join(map(str, k)).encode()))
FAB = S("soft stretch jersey; organic cotton knit; bamboo-blend rib; brushed fleece; lightweight linen; breathable modal; wool-blend knit; quilted cotton; smooth satin; textured crepe; denim with stretch panels; moisture-wicking mesh; silky viscose; velvet; boiled wool; ponte knit")
COL = S("black; navy; olive; dusty rose; cream; terracotta; sage green; charcoal; burgundy; teal; mustard; heather grey; white; camel; plum; sky blue; forest green; rust; ivory; coral")
BODY = S("a maternity dress with an elastic ruched panel over the belly that stretches as it grows; a wrap maternity dress with ties at the side; maternity jeans with a stretch panel that rises over the belly; a below-belly maternity legging; a maternity tee with side ruching; a maternity jumpsuit with adjustable straps; a maternity swimsuit with a gathered front; a belly-support band worn under clothes; a nursing top with hidden side openings; a nursing dress with a layered front flap; a nursing bra with a clip-down cup; a nursing hoodie with zip openings; post-birth recovery shorts with a high compression waist; a postpartum wrap with hook closures; an abdominal binder with hook-and-loop fastening; a compression top after chest surgery with front closures; a post-surgery camisole with drain-pocket sleeves; a surgical garment with front zip and stretch panels; a medical compression sleeve; a compression stocking in a sheer weave; a post-mastectomy bra with soft pocket inserts; a chest binder in breathable mesh; a gender-affirming tuck-friendly brief with a smooth front; a packing brief with a soft pocket; a trans-inclusive swim top; a bra extender; an adjustable-waist trouser with side buttons for fluctuating size; a stretch-waist skirt with a drawstring; an expandable-seam dress with side lacing; a gusseted tent dress with a flowing cut; a pregnancy support belt; a weight-loss compression layer; a large-size wrap top with an adjustable front; plus-size high-waisted shaping pants; a loose caftan for comfort during swelling; ostomy support underwear with a pouch pocket; a tube-feeding pocket shirt; an adaptive seated-cut trouser with a raised back; a trouser with side zips for easy dressing; an adaptive shirt with magnetic closures; a button-free pullover with wide neck; a shoe with a wide, adjustable opening; a bib-style clothing protector; a sensory-friendly shirt with tagless seams; a weighted vest with soft inner lining; a cooling vest with gel packs; a heated vest with a battery pocket; a mobility-friendly cape with a back opening")
COLD = S("a down-filled parka with a fur-trimmed hood; a long quilted puffer coat; a shearling-lined aviator jacket; a wool duffle coat with toggles; a peacoat in heavy melton wool; a waxed canvas coat with a corduroy collar; a thermal base layer top and leggings; a fleece midlayer with a high collar; a softshell jacket with taped seams; a hardshell mountaineering jacket with a helmet-compatible hood; insulated bib snow pants; a one-piece snowsuit with a belt; a ski jacket with a powder skirt; an Inuit-style anorak with a deep hood; a sealskin-trimmed mitten pair; a hand-knit Fair Isle sweater; an Aran cable-knit fisherman's sweater; a Nordic patterned yoke sweater; a heavy wool cardigan with a shawl collar; a balaclava; a knitted beanie with a pom-pom; an ushanka with ear flaps; a trapper hat with fur; a long knit scarf; a snood; a heated glove liner; down mittens; fleece-lined wellington boots; felt-lined snow boots; mukluks with beaded tops; a wool blanket cape; a reindeer-hide coat; a quilted chore coat; a lumberjack flannel with a quilted liner; an insulated overall; a heavy rain-cloak; a long wool overcoat; a fur stole; a faux-fur coat; a Mongolian deel with a thick lining; a padded Chinese winter coat; a heavy kimono-style hanten; a Kashmiri pheran with a lined body; a Tibetan chuba lined with sheepskin; a Peruvian alpaca poncho; a Scottish tweed cape; a wool-lined gauntlet glove pair")
FORMAL = S("a black-tie tuxedo with satin lapels; a white-tie tailcoat set; a morning coat with striped trousers; a dinner jacket in midnight blue; a velvet smoking jacket; a three-piece suit with a waistcoat; a double-breasted suit; a mandarin-collar formal jacket; a floor-length gown with a train; a ball gown with a fitted bodice and full skirt; an evening gown in satin with a thigh slit; a beaded cocktail dress; a sequined gown; a tulle ball skirt; a mermaid-cut evening gown; a one-shoulder gown; a jewelled bodice; formal wide-legged evening trousers with a silk top; a jumpsuit evening wear; a formal sari in silk with gold border; a lehenga set with embroidery; a sherwani with embroidered neckline; an achkan jacket; a kimono formal montsuki with crest; a hakama over kimono; a hanbok in jewel tones; a baro't saya with butterfly sleeves; a barong in sheer fabric; a Chinese qipao in brocade; a changshan; an ao dai in flowing silk; a thobe with a formal bisht cloak; a kaftan with gold embroidery; a dashiki set in formal wax print; an agbada with embroidered robe; a kente cloth wrap; a gele headwrap and wrapper; a Scottish formal kilt outfit with a sporran; a Highland jacket; a dirndl with an apron; lederhosen with embroidered braces; a Sami gákti in ceremonial colours; a Maasai beaded collar and shuka; a pareo formal wrap; a Hawaiian aloha formal set; a fur-trimmed court mantle; an academic gown with hood; a judicial robe; a clergy vestment; a ceremonial military dress uniform; a ceremonial mourning robe")
REG = S("a kaross of tanned hide worn as a cloak; a lavalava wrapped skirt in printed cloth; a gho knee-length robe with a wide belt; a kikoy striped wrap cloth; a kanga printed wrap with a saying border; a tallit prayer shawl with fringes; a kippah skullcap; a tagelmust indigo veil-turban; a kente strip-woven cloth; a bogolan mud-dyed cloth; a Maasai shuka blanket; a Zulu isicholo hat; a Xhosa beaded skirt; a Berber djellaba with pointed hood; a Moroccan kaftan; an Egyptian galabeya; a Sudanese tobe wrap; an Ethiopian habesha kemis with woven border; an Eritrean zuria; a Somali guntiino; a Bedouin burqa mask; an Omani dishdasha with tassel; a Yemeni jambiya belt; an Afghan perahan tunban; a Pashtun waistcoat; a Kurdish baggy trousers and sash; a Georgian chokha with cartridge pockets; a Russian sarafan; a Ukrainian vyshyvanka embroidered shirt; a Polish kontusz; a Hungarian bunda; a Romanian ie blouse; a Bulgarian sukman; a Croatian opanak; a Greek foustanella; a Basque beret; a Portuguese capote; a Dutch klompen; a Swiss alpine apron; a Welsh tall hat; an Irish aran shawl; a Latvian woven belt; a Mongolian gutal boot; a Kazakh saukele headdress; a Kyrgyz kalpak; an Uzbek ikat robe; a Tajik atlas dress; a Turkmen telpek hat; an Ainu attus robe; an Okinawan bingata; a Filipino terno; a Malay baju kurung; a Javanese kebaya with batik; a Balinese kamen; a Burmese longyi; a Thai chut thai; a Lao sinh; a Cambodian sampot; a Vietnamese ao ba ba; an Indian bandhgala; a Rajasthani ghagra; a Kerala kasavu saree; a Pakistani shalwar kameez; a Bengali dhuti and panjabi; a Nepali daura-suruwal; a Tibetan chuba; a Bhutanese kira; a Sri Lankan osariya; a Hawaiian holoku; a Samoan puletasi; a Tongan ta'ovala; a Fijian sulu; a Maori korowai cloak; a Māori piupiu skirt; a Native American ribbon skirt; a Plains war-bonnet-style beaded headband; a Navajo velvet blouse; an Andean pollera; a Bolivian bowler hat; a Guatemalan huipil; a Mexican rebozo; a Panamanian pollera; a Brazilian baiana dress; an Argentine gaucho bombacha; an Arctic kuspuk")
FABK = {'bodychange': S("soft stretch jersey; organic cotton knit; bamboo-blend rib; breathable modal; moisture-wicking mesh; ponte knit; brushed cotton"),
 'cold': S("heavy wool; quilted nylon; brushed fleece; boiled wool; waxed canvas; hand-knit wool; shearling-lined cotton"),
 'formal': S("satin; silk; velvet; crepe; brocade; tulle; wool suiting; sequinned mesh; taffeta"),
 'regional_more': S("hand-woven cloth; printed cotton; embroidered cloth; dyed linen; felted wool; silk; natural fibre")}

DESC = {
 "kaross": "a cloak made from a soft tanned animal hide, worn over the shoulders and fastened at the front",
 "lavalava": "a rectangle of printed cotton cloth wrapped around the waist and hanging to the calves",
 "gho": "a knee-length robe folded over at the front and held at the waist by a long woven belt, with wide white cuffs",
 "kikoy": "a lightweight striped cotton cloth with fringed ends, wrapped around the waist",
 "kanga": "a printed cotton wrap with a border and a printed saying, worn around the body or the waist",
 "tallit": "a rectangular prayer shawl with knotted fringes at each corner",
 "kippah": "a small round cap that covers the crown of the head",
 "tagelmust": "a long indigo-dyed cloth wound into a turban with a part that covers the face",
 "kente": "a cloth woven in narrow bright strips sewn side by side into geometric patterns",
 "bogolan": "a hand-woven cloth painted with fermented mud in dark geometric patterns on a pale ground",
 "shuka": "a checked or striped blanket, usually red, wrapped over the shoulders and around the body",
 "isicholo": "a wide, flat-topped hat of woven material covered with red-ochre-coloured cloth",
 "Xhosa beaded skirt": "a wraparound skirt decorated with bands of white and coloured beads",
 "djellaba": "a long, loose hooded robe with full sleeves that reaches the ankles",
 "Moroccan kaftan": "a long, loose robe with wide sleeves, closed down the front with decorative braid",
 "galabeya": "a long, loose, ankle-length cotton robe with wide sleeves",
 "tobe": "a long cloth wrapped around the body and over one shoulder, often of thin printed fabric",
 "habesha kemis": "a long white cotton dress with a coloured woven border at the hem, cuffs and chest",
 "zuria": "a long white cotton dress with a wide, brightly coloured woven border and a matching shawl",
 "guntiino": "a length of cloth knotted over one shoulder and tied around the waist",
 "burqa mask": "a stiff, shaped fabric mask that covers the upper face with narrow openings for the eyes",
 "dishdasha": "a long, plain white robe with long sleeves and a small tassel hanging from the collar",
 "jambiya": "a curved dagger in a decorated sheath, worn at the front of a wide belt",
 "perahan tunban": "a long loose shirt reaching the knees worn over wide drawstring trousers",
 "Pashtun waistcoat": "a sleeveless embroidered waistcoat worn over a long shirt",
 "Kurdish baggy trousers": "very wide trousers gathered at the ankle, worn with a sash wound around the waist",
 "chokha": "a long fitted wool coat with a flared skirt and rows of cartridge pockets across the chest",
 "sarafan": "a long, sleeveless dress with a high waist, worn over a white blouse",
 "vyshyvanka": "a white linen shirt with embroidery in red and black across the collar, chest and sleeves",
 "kontusz": "a long outer coat with slit sleeves that are thrown back, tied with a wide sash",
 "bunda": "a heavy sheepskin coat embroidered with flowers on the front and back",
 "ie blouse": "a loose white blouse with dense embroidered patterns on the sleeves and chest",
 "sukman": "a sleeveless dress of heavy wool, often dark, with embroidered trim",
 "opanak": "a soft leather shoe with a curled-up toe and a sole made from a single piece of leather",
 "foustanella": "a short, pleated white kilt with many folds, worn with white tights",
 "beret": "a soft, round, flat-crowned cap of wool",
 "capote": "a long hooded cape worn over the shoulders",
 "klompen": "carved wooden clogs with a rounded toe",
 "alpine apron": "a broad apron of printed or plain cloth tied at the waist and worn over a dress",
 "Welsh tall hat": "a tall black hat with a high crown and a wide brim",
 "aran shawl": "a heavy knitted shawl in a pattern of ropes and braids",
 "woven belt": "a narrow, patterned belt woven in repeating geometric designs",
 "gutal": "a leather boot with a turned-up, pointed toe and a thick sole",
 "saukele": "a tall, cone-shaped bridal headdress decorated with beads, coins and feathers",
 "kalpak": "a tall, white felt hat with a black band and a curved brim",
 "ikat": "a robe woven in blurred, bold stripes and diamonds from pre-dyed threads",
 "atlas": "a dress cut from a bright silk with a blurred pattern of bold shapes",
 "telpek": "a tall, round fur hat with a wide cylindrical shape",
 "attus": "a robe woven from tree bark fibre with bold appliqué patterns at the back and cuffs",
 "bingata": "a cloth printed with brightly coloured patterns of flowers and birds using stencils and resist paste",
 "terno": "a dress with stiff, upright butterfly-shaped sleeves, usually of sheer, stiff fabric",
 "baju kurung": "a long, loose tunic reaching the knees worn over a matching ankle-length skirt",
 "kebaya": "a fitted, sheer lace blouse with long sleeves worn with a wrapped batik skirt",
 "kamen": "a length of cloth wrapped around the hips and tied with a sash",
 "longyi": "a tube of cloth worn around the waist, tied at the front and reaching the ankles",
 "chut thai": "a set of a wrapped skirt, fitted blouse and a draped sash",
 "sinh": "a tube skirt with a woven decorated band at the hem",
 "sampot": "a rectangular cloth wrapped around the waist and pulled between the legs, tucked at the back",
 "ao ba ba": "a pyjama-style outfit of a loose, long-sleeved buttoned top and wide trousers",
 "bandhgala": "a fitted jacket with a stand collar closed with buttons all the way up",
 "ghagra": "a very full, ankle-length skirt with bright mirror-work and a matching short blouse",
 "kasavu": "a cream saree with a gold border woven along the edge",
 "shalwar kameez": "a long, loose tunic worn over wide, gathered trousers",
 "dhuti": "a long, white cloth wrapped around the waist and legs and tucked at the back, worn with a loose long shirt",
 "daura-suruwal": "a long wrapped shirt tied at the side with strings, worn with fitted trousers",
 "chuba": "a long-sleeved, ankle-length wraparound robe held with a belt, often lined with sheepskin",
 "kira": "a rectangle of woven cloth wrapped around the body and pinned at the shoulders, with a belt",
 "osariya": "a saree draped with pleats at the waist and a decorated loose end over the shoulder",
 "holoku": "a long dress with a train and a high neck, loose from the shoulders",
 "puletasi": "a matching fitted top and ankle-length wrapped skirt",
 "ta'ovala": "a woven mat wrapped around the waist and held with a cord",
 "sulu": "a rectangle of cloth wrapped around the waist like a skirt, hemmed with zigzag edges",
 "korowai": "a cloak covered in woven tassels or feathers, hung from the shoulders",
 "piupiu": "a skirt made of rolled flax strips that swing and rattle when walking",
 "ribbon skirt": "a skirt with horizontal rows of coloured ribbon sewn along the lower half",
 "beaded headband": "a band of tightly sewn glass beads in patterns, worn around the forehead",
 "velvet blouse": "a long-sleeved, loose velvet top decorated with silver buttons",
 "pollera": "a very wide, layered skirt with bright embroidered or appliquéd bands",
 "bowler hat": "a small, round, stiff hat with a narrow brim worn on top of the head",
 "huipil": "a loose rectangular tunic woven from two or three panels with embroidered patterns",
 "rebozo": "a long rectangular shawl, with fringed ends, wrapped over the shoulders and arms",
 "baiana dress": "a wide, ruffled white skirt with a lace blouse, strings of beads and a head wrap",
 "bombacha": "loose gathered trousers with buttoned cuffs that fit around the ankles",
 "kuspuk": "a hooded pullover smock with a frill around the hem",
 "sherwani": "a long coat with a stand collar and buttons down the front, reaching the knees",
 "achkan": "a tailored, knee-length coat with a high collar closed with buttons",
 "hakama": "wide pleated trousers that are tied at the waist and worn over a kimono",
 "montsuki": "a black formal kimono with five small family crests on the back, sleeves and chest",
 "hanbok": "a short jacket with a long wide skirt, tied at the chest with a bow",
 "baro't saya": "a blouse with wide, stiff, butterfly sleeves worn with a long wrapped skirt",
 "barong": "a long, loose, translucent embroidered shirt worn untucked over an undershirt",
 "qipao": "a close-fitting, high-collared dress with a side slit and cloth knot buttons",
 "changshan": "a long, loose gown with a stand collar and knot buttons down the side",
 "ao dai": "a long, fitted tunic split to the waist at both sides, worn over wide trousers",
 "bisht": "a loose, open cloak with gold-embroidered edges, worn over a thobe",
 "dashiki": "a loose, colourful pullover shirt with a V-shaped neckline and embroidered edges",
 "agbada": "a very wide, flowing robe with large embroidered sleeves, worn over a matching shirt and trousers",
 "gele": "a very large, stiff head wrap folded into a fan or a bow",
 "gákti": "a knee-length tunic of wool or cotton trimmed with coloured bands and silver",
 "pareo": "a rectangular piece of cloth wrapped around the body or the waist",
}
def describe(item):
    best = None
    for k, v in DESC.items():
        if k.lower() in item.lower() and (best is None or len(k) > len(best[0])): best = (k, v)
    if not best or 'worn as' in item: return item
    return f"{item}, which is {best[1]}"
def mk():
    G = {}
    for k, items in [('bodychange', BODY), ('cold', COLD), ('formal', FORMAL), ('regional_more', REG)]:
        n = f'clothing_garment_{k}'
        items = [describe(x) for x in items]; G[n + '_item'] = items; G[n + '_fabric'] = FABK[k]; G[n + '_colour'] = COL
        G[n] = sorted({f"{it}, in {R(k, it, c).choice(FABK[k])}, coloured {c}" for it in items for c in COL if R('w', k, it, c).random() < .30})
    G['clothing_garment_more_prompt'] = [f"__clothing_garment_{k}__." for k in ('bodychange', 'cold', 'formal', 'regional_more')]
    return G
def build(): return mk()
def run(final):
    G = build()
    for n, l in G.items():
        assert l and all(l) and not any(c in x for x in l for c in '{}|'), n
        open(os.path.join(final, n + '.txt'), 'w', encoding='utf8', newline='\n').write('\n'.join(dict.fromkeys(l)) + '\n')
    print('wear more:', len(G), 'files'); return G
def export_aoo(out, prefix='aoo_'):
    G = build(); nm = set(G); ref = re.compile(r'__([A-Za-z0-9_\-/]+)__'); n = 0
    for name, lines in G.items():
        keep = list(dict.fromkeys(ref.sub(lambda m: '__' + prefix + m.group(1) + '__' if m.group(1) in nm else m.group(0), l) for l in lines))
        if not name.endswith('prompt'): random.Random(zlib.crc32(name.encode())).shuffle(keep)
        open(os.path.join(out, prefix + name + '.txt'), 'w', encoding='utf8', newline='\n').write('\n'.join(keep) + '\n'); n += 1
    return n
if __name__ == '__main__':
    a = [x for x in sys.argv[1:] if os.path.isdir(x)]; run(os.path.abspath(a[0]) if a else FINAL)
