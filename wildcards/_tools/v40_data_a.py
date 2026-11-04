"""v40 data A: purses (true purses only) and haute couture oddities. Each entry: (name, description, materials)."""
def S(x): return [i.strip() for i in x.split(';') if i.strip()]
def E(rows):
    out = []
    for r in rows.strip().split('\n'):
        if not r.strip(): continue
        n, d, m = [p.strip() for p in r.split('|')]
        out.append((n, d, S(m)))
    return out
PURSE = E("""
coin purse|a small, closed pouch about the size of a palm that holds loose coins, with a short zip across the top|soft leather; vinyl; canvas; felt; silicone
change purse with a squeeze clasp|a small pouch whose top has two metal arms that squeeze together to open and spring shut|leather; velvet; patent leather; tapestry fabric
kiss-lock frame purse|a small purse with a rigid metal frame along the top, the two halves closing with a pair of round knobs that click together|leather; velvet; brocade; embroidered silk
double-frame purse|a small purse with two separate compartments, each with its own metal frame, hinged at the middle|leather; velvet; faux crocodile; patent leather
zip-around coin purse|a flat, rounded pouch whose zip runs round three sides so the front flips open like a book|leather; nylon; canvas; vinyl
drawstring money purse|a soft, gathered pouch with a cord threaded through the top that pulls tight and knots|suede; velvet; silk; linen
beaded purse|a small purse covered in rows of tiny glass beads forming a pattern, with a frame at the top and a short beaded chain|glass beads on silk; seed beads on cotton; bugle beads on satin
crochet metal-mesh purse|a purse woven from tiny linked rings of metal like fine chain mail, with a frame top and a short chain|silver-toned mesh; gold-toned mesh; enamelled mesh
miser's stocking purse|a long, narrow knitted tube closed at both ends with a slit in the middle, and two sliding rings that keep the coins at either end|knitted silk; knitted cotton; knitted wool
sporran|a purse worn hanging at the front of a kilt from a chain or strap round the hips, with a flap and decorative tassels or fur|leather and fur; leather with metal cantles; horsehair
coin pouch with a belt loop|a small flat pouch with a strap on the back to thread onto a belt, closed with a snap|leather; waxed canvas; nylon
card purse|a flat, wallet-size purse with several slits for cards and a small zipped coin pocket|leather; vinyl; saffiano-textured leather
tin coin purse|a small hinged metal box with a rounded lid that snaps closed, used to hold coins|enamelled tin; brass; nickel-plated steel
shell-shaped coin purse|a purse moulded into a scallop-shell shape that opens like a clam along one edge|leather; velvet; patent leather
knitted coin purse|a small purse in knitted wool with a zip across the top|wool; cotton yarn; acrylic yarn
patchwork coin purse|a small purse sewn from many little cloth patches in different prints, lined, with a zip|printed cotton; silk scraps; denim scraps
tapestry change purse|a small purse covered in woven pictorial tapestry cloth, with a metal frame and a loop on the clasp|jacquard tapestry; embroidered wool; needlepoint
embroidered silk purse|a small purse covered in fine silk embroidery with a drawstring and two tassels|silk; satin; brocade
japanese drawstring purse|a small round-bottomed purse in patterned cloth with a cord that pulls the top shut, worn at the wrist|silk; cotton; brocade
clasp purse with a chain|a small rectangular purse with a hinged metal top and a thin chain loop to hold it by|leather; velvet; satin
wristlet coin purse|a small zip purse with a short strap that slides round the wrist|leather; nylon; vinyl
cork coin purse|a small zip pouch made of thin sheets of tree bark, soft and light|cork fabric; cork with leather trim
enamel-cloisonne coin purse|a small hinged purse decorated with fine wire-and-enamel patterns on the lid|enamelled metal; enamelled brass
kidskin leather purse|a small, rounded, thin purse in very soft leather with a fold-over flap held by a snap|kidskin; lambskin; calfskin
oilcloth coin purse|a small glossy-coated cloth purse with a zip, wipe-clean|coated cotton; waxed cotton; vinyl-coated fabric
""")
COUTURE = E("""
sculptural cage skirt gown|a bodice that flares into a huge skirt of rigid hoops and steel wire, with the framework left visible and fabric only in panels|steel hoops with tulle; boned wire with silk organza; cane with taffeta
swan-neck gown|a long white gown with a tall tubular neck of stiffened feathers that rises and curves forward over the head like a swan|white feathers on wire; satin over a wire frame; tulle over foam
giant puff-ball skirt|a skirt gathered into a huge sphere that hangs from the waist and reaches past the elbows on every side|stiffened tulle; taffeta; foam-lined organza
six-metre train gown|a gown with a train that trails six metres behind, held out by a hidden wire so that it floats above the floor|silk satin; organza; velvet
dress made of living plants|a dress whose fabric is covered with real moss, grass and tiny flowers growing from it|moss on mesh; grass turf on cloth; live flowers on a wire frame
fire-and-smoke dress|a dress with a thin vapour piped out through the hem, which wreathes the lower half of the gown in a cloud|silk with hidden tubes; chiffon with a fogging unit
dress with a bird cage skirt|a gown whose skirt is shaped like an enormous bird cage, with live-looking painted birds perched in it|painted metal; wire with silk; resin birds
room-sized hoop skirt|an enormous skirt like a small tent that spreads three metres wide, so the wearer cannot pass through a door|steel boning with silk; wire with organza; cane with taffeta
dress made of mirrors|a stiff gown assembled from hundreds of small mirror tiles that catch and throw light in every direction|glass tiles on a frame; polished steel plates on leather; mirrored acrylic
dress made of balloons|a gown made of long balloons twisted into tubes and spheres, with the strapless top held by a bound ribbon|latex balloons; clear PVC balloons; foil balloons
giant flower dress|a gown whose skirt is a huge flower with layered petals stiffened with wire, so the wearer stands at the centre like a stamen|silk petals on wire; tulle petals; satin petals
jellyfish-bell dress|a dress with a transparent dome-shaped skirt and long trailing ribbons like tentacles, which sways in a floating way|clear plastic; organza; silk ribbon
pleated-paper wings gown|a dress with huge stiff wings of folded paper-like pleats that spread out sideways and up above the head|treated paper; heat-set polyester; metal-coated fabric
dress of a thousand zips|a close-fitting dress covered in hundreds of working zips that can be opened to show skin-coloured lining|metal zips on leather; coloured zips on cotton; plastic zips on denim
dress made of lace-up shoes|a gown made of dozens of leather shoes stitched toe-to-heel into a skirt and bodice|leather shoes; patent shoes; canvas shoes
spiral staircase dress|a gown whose skirt winds upward in a tall spiral shape like a staircase, supported by an internal wire frame|stiffened silk; tulle on wire; metal-coated cloth
dress with a rolling hem|a gown whose skirt is rolled on a pair of wheels at the hem, so that it moves like a trolley behind the wearer|silk on a wheeled frame; velvet on a frame
oversized bow gown|a gown with a bow the size of a person on the chest or back, with wide stiff loops and long ribbon tails|taffeta; duchess satin; stiffened organza
dress made of ruffled petticoats stacked to the ceiling|a skirt built from thirty or more layers of frilled petticoats stacked in a tower above the head|tulle; organza; layered cotton
dress with sculpted gold torso|a pale gown with a gold-plated shape of a muscled torso fixed on the front, like armour|gold-plated resin; brass; gilded fibreglass
dress with a lobster painted across the front|a long white gown with a big painted lobster on the skirt, in red and orange|silk organza; satin; crepe
shoe-shaped hat|a tall hat shaped like an upturned high-heeled shoe, with the heel rising from the top of the head|felt; velvet; stiffened silk
telephone hat|a hat built from a stiff base with a dial and receiver on top, in the shape of an old telephone|felt; moulded fibre; lacquered straw
dress made of lampshade fabric|a dress cut from pleated lampshade cloth, with a wide skirt that holds its shape like a bell-shaped shade|pleated silk; paper-backed fabric; silk with wire hoops
flat-packed dress|a dress that is entirely flat and two-dimensional from the front, with the sides made as thin as paper|stiff felt; layered card; cut foam sheet
bubble wrap gown|a ballgown made entirely of sheets of air-filled plastic, glossy and puffy|clear plastic bubble sheet; pink plastic bubble sheet; silver-coated bubble sheet
inflated suit with a huge puffed silhouette|a jacket and trousers filled with air to appear many times larger, with round puffed limbs|nylon airbag fabric; vinyl; PVC
armour of safety pins|a tight garment made from thousands of safety pins linked together into a chain-like fabric|steel pins; gold-plated pins; enamelled pins
dress made of paper money-like printed sheets|a gown made of overlapping sheets of printed paper that rustle when the wearer moves|printed paper; coated paper; foil paper
dress with a tree growing through it|a dress that has a bare branch rising from the waist, with silk leaves and blossoms scattered along it|silk and wood; paper and wire; felt and wire
dress made of hair|a gown made entirely of long strands of hair braided and knotted into panels|dyed human-hair-look synthetic fibre; horsehair; wool roving
headdress shaped like a sailing ship|a tall headdress with a miniature ship with masts and sails, standing on a base of curled waves, set on a padded cap|wire, silk and wood; stiffened gauze; gilded resin
tower hairpiece|a headdress that rises more than a metre above the head in a tall tower of curled and pinned hair-like material, decorated with ribbons|white powdered wig fibre; wool and wire; dyed horsehair
gigantic ruff|a huge round collar of pleated fabric that is wider than the shoulders, standing out round the head like a plate|starched linen; organza; paper-like pleated cloth
hat of fruit and vegetables|a wide-brimmed hat piled with imitation fruit and vegetables in bright colours|wax fruit on straw; felt fruit; resin fruit
dress with wearable sofa|a dress whose rear is built out into a padded sofa shape, with arms and cushions, for the wearer to sit on|velvet; plush; upholstery fabric
trousers with a hundred legs|trousers that branch at the hips into many pairs of legs hanging down in a fan|wool; cotton; silk
suit with a pocket the size of a door|a suit jacket with one gigantic patch pocket, wide enough to hold a person, sewn to the front|wool; tweed; linen
cape with a six-metre spread|a cape which, when the arms are raised, spreads out into a semicircle six metres wide|silk; organza; velvet
cape of feathers|a long cape made of overlapping feathers in graduated colours that ripples like a bird's wing|ostrich feathers; peacock feathers; dyed goose feathers
armour-like dress of glass shards|a stiff dress built from flat pieces of clear plastic and glass cut to look like shattered glass|acrylic shards; glass shards on mesh; resin shards
gown with a clock face|a gown whose bodice has a large working clock face as its centrepiece, with hands that move|silk with a mechanical clock; satin with a battery clock
gown with an antler headpiece|a dress paired with huge branching antlers that rise from the head, decorated with ribbons and bells|resin antlers; real shed antlers; gilded antlers
dress made of seashells|a gown made of hundreds of seashells sewn in overlapping scales, heavy and clattering|shells on cloth; shells on wire; mother-of-pearl discs
dress covered in tassels|a dress completely covered in long hanging tassels in graded colours, swishing at every step|silk tassels; wool tassels; leather tassels
ice-like transparent gown|a gown moulded from clear plastic with the surface carved to look like ice crystals|clear resin; acrylic; PVC
dress made of umbrellas|a skirt formed from many small open umbrellas attached edge-to-edge, spinning around the hips|nylon and metal; lace parasols; paper parasols
extra-long glove gown|a gown with sleeves about three metres long that drag on the floor and have to be carried|silk; velvet; chiffon
stilted gown|a gown worn over tall stilts hidden under the skirt, so the wearer towers two metres above the floor|silk over stilts; satin over wooden stilts
gown with a built-in chandelier|a skirt with a hanging chandelier-like frame of crystals, which lights up|crystal beads; glass drops; LED strands
corset with a bell cage|a stiff corset leading down into a bell-shaped skirt cage and tiny round shoulders|boned satin; leather; steel and cloth
frilled-collar clown-style gown|a gown with an enormous layered frill round the neck and cuffs, with exaggerated polka-dots|organza; taffeta; cotton
topiary dress|a dress clipped into the shape of a hedge sculpture, with a neat green surface of tiny leaves on a frame|artificial leaves; felt; real clipped boxwood on a frame
dress shaped like a cake|a many-tiered gown like a wedding cake, with sugar-like ruffles and a candle-like headdress|tulle; satin; foam and cloth
chocolate-coloured liquid-effect gown|a gown whose smooth, glossy folds look as if poured, like liquid chocolate flowing to the floor|stiff satin; moulded latex; resin-coated cloth
faceless hood|a stretch hood that covers the entire head and face with a smooth surface and no openings, apart from a thin mesh patch|stretch jersey; stretch knit; satin
dress made of rope|a dress knotted and coiled from thick sailing rope, heavy with a rough surface|cotton rope; hemp rope; coloured nylon rope
dress made of cutlery|a stiff gown assembled from hundreds of forks and spoons linked into scales|stainless steel; silver-plated metal; brass
hat shaped like a lobster|a hat in the form of a large crustacean with claws sticking out over the ears|felt; resin; stiffened silk
sheep-fleece gown|a gown covered in thick curly fleece that bulges out around the body in a cloud|sheepskin; wool curls; faux fur
gown with a flock of moving birds|a gown with small mechanical birds that flap their wings on the shoulders|painted metal; felt birds; resin birds
""")
CUT_DET = S("a high stiff collar; a very long train; a deep slit; a nipped waist; a slim sleeve; asymmetric hem; a boned bodice; tiny covered buttons; a hand-rolled hem; hand-stitched embroidery")
COUT_COL = S("ivory; black; scarlet; midnight blue; emerald; gold; silver; blush pink; sky blue; saffron yellow; plum; lime green; white; copper; teal; graphite grey")
FUNNY = E("""
trousers worn pulled up over the chest|a pair of trousers pulled up to the armpits with the legs hanging empty or tied, held at the chest by a belt|denim; wool; corduroy; cotton twill
several pairs of jeans worn at once|three or four pairs of jeans layered over each other, each waistband visible above the next, with stacked cuffs at the ankles|denim; stretch denim; black denim
suit covered in buttons|a jacket and trousers whose entire surface is sewn with hundreds of buttons of every size and colour|wool; cotton; felt
cowboy hat with udder-like bulges|a wide-brimmed hat with pink rubbery bumps hanging from the brim like udders|felt; leather; moulded latex
boots with flip-flop soles|ankle boots whose soles end in a sandal-style thong strap between the toes, so they are half boot and half beach shoe|leather; rubber; faux suede
shirt printed with a photograph of itself|a shirt with a large photographic print of a person wearing the same shirt, repeating inward|jersey cotton; polyester; poplin
trouser-shorts hybrid|a garment with one leg cut off at the thigh and the other long to the ankle, joined at a single waistband|cotton twill; denim; linen
gloves with very long extra fingers|gloves whose fingers extend twenty centimetres past the fingertips, hanging down and flopping|knit wool; cotton; fleece
backpack with leg-shaped straps|a backpack whose straps are shaped like legs in trousers and shoes, hanging down the front|nylon; canvas; vinyl
jeans with sneaker-shaped lower legs|jeans that end at the knee in a pair of built-in trainers, so there is no ankle gap|denim and rubber; denim and canvas
jeans with boot-shaped lower legs|jeans that continue below the knee as tall boots in the same denim, with heels|denim and leather; denim and faux leather
dress that looks like a pile of noodles|a dress covered in hundreds of thick, tangled, cream-coloured cords falling in loops|cotton cord; yarn; satin tubing
suit cut from upholstery fabric|a matching jacket and trousers made from heavy sofa-style fabric with a floral or striped woven pattern|jacquard upholstery fabric; velvet; brocade
shirt with a circuit-board print|a shirt entirely covered with a printed pattern of green circuit traces and chips|polyester jersey; cotton; poplin
toe-separated ballet shoes|soft lace-up slippers with five separate toe compartments sewn like a glove for the foot|leather; satin; canvas
puffy fuzzy suit|a suit made from long bright synthetic pile like a puppet's fur, with the fibre standing out all over|synthetic pile; faux fur; fleece
bridal-style dress with a brown ribbon train|a white wedding-style gown with a very long brown ribbon trailing from the waist across the floor|satin; tulle; lace
dress with sleeves like frog legs|a bright green dress with wide hanging sleeves and a flat collar shaped like a frog's body|felt; fleece; velvet
oversized gold shoelaces|a pair of shoes whose laces are thick golden tubes the size of ropes, tied in huge loops|nylon tubing; satin cord; leather
rubber clogs with a wallet chain at the ankle|chunky foam clogs with a metal chain across the ankle|foam; rubber
duck-print raincoat|a yellow raincoat covered with the face and bill of a duck on the hood|waterproof nylon; PVC; coated cotton
jacket with a bear face|a jacket with a hood in the shape of a bear head, with ears and a snout, and paw-shaped pockets|fleece; plush; felt
socks with a printed graphic of skeleton hands|socks printed from heel to cuff with a detailed pattern of grey hands reaching up the leg|cotton; nylon blend
pants with the pockets in odd places|trousers with the pockets placed on the thighs, knees and seat in clumps, and a high seam crossing the crotch|cotton; denim
a garment with very little fabric|a garment made of only a few strips and straps, leaving most of the body bare apart from fitted bands|elastic; leather; cord
oversized heart-shaped sunglasses worn as a hat|a pair of giant sunglasses perched on top of the head as a hat|plastic; foam
bat-wing gloves|gloves that extend into webbed black wings from the little finger to the elbow|stretch knit; velvet
dress shaped like a tower of letters|a dress printed and padded with big three-dimensional block letters stacked up the front|foam; felt; cotton
tights printed with a distorted face|tights with a stretched, smudged face print that twists as the legs move|nylon; cotton blend
sweatpants cut and printed to look like jeans|loose sweatpants printed with denim texture, seams and pockets, with an elastic waist|printed cotton fleece
boots that make loud clicking sounds|shoes with hard heel plates that clack on the floor|leather and metal
""")
