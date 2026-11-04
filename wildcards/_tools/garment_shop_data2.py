"""Extra broad garment bases per section (original wording).  Row: name|front|back|covered|uncovered|cut and fit"""
def P(s): return [tuple(x.strip() for x in l.split('|')) for l in s.strip().split('\n') if l.strip()]
B = {}
B['ultra'] = P("""
open-tip embroidered mesh teddy|underwire cups of embroidered mesh with the tips cut open, a plunging centre and a snap-free open crotch|strappy crisscross back straps above a thong-cut seat|the sides of the breasts and the torso through mesh|the nipples, the genital area and most of the seat|snug, high-cut leg, adjustable straps
cupless embroidered cami set|a mesh cami with no cups, a keyhole neckline and narrow straps, with a matching G-string|a short mesh back ending at the ribs|the ribs and midriff through mesh|the breasts through the open mesh|loose empire cut above the waist
slit-cup velvet bustier|a boned velvet bustier whose cups have a vertical slit down each centre|a zip or hook-and-eye closure over a smooth back, detachable suspenders|the ribs, waist and outer breasts|the nipples through the slits|fitted, cinched waist
two-piece teddy set with sheer stockings|a satin-and-lace teddy with slit cups and a crotchless gusset, sheer stockings included|a thong back with a bow|the torso and hips|the nipples and genital area|snug, high-cut
open-back halter bodysuit with snaps|a halter neck and plunging front in stretch mesh|a bare back to the waist and a snap crotch|the front torso|the back|snug, high-cut
strapless open-bust corselette|a boned corselette that ends under the bust with a lace-up front|a hook-and-eye back panel and thong seat with garters|the ribs, waist and hips|the breasts and the buttocks|cinched, boned
cupless satin babydoll|a satin babydoll with a cupless empire bodice and sheer skirt|a low scoop back with a bow|the ribs and the hips|the breasts|flared, thigh-length
rhinestone halter teddy with open back|a halter teddy with a crystal-studded neckline and mesh midriff|a completely open back to the waist|the breasts and the hips|the back|snug, high-cut
sheer pleated gown|a floor-length sheer pleated gown with embroidered neckline and satin bow at the cleavage|a sheer open back, side slit|nothing opaque: the embroidered neckline only|the whole body shows through|fluid, floor length
dragon beaded gown over sheer mesh|beaded appliqué dragon over sheer mesh with a halter neck and a front slit|an open halter back with a tie|the beaded panels|the skin through the sheer mesh and the slit|fitted floor length
embroidered silk boudoir gown with bra-style back|silk cups and waist over sheer georgette|a bra-style open back and a side slit|the cups and waistband|the skin through georgette|bias drape
rhinestone velvet bustier with zip front|a boned velvet bustier with a rhinestone zipper|a smooth back with detachable garters|the breasts and ribs|the hips and thighs|boned, cinched
crotchless mesh bodystocking in six styles|a sheer all-in-one with a halter or long-sleeved neck, in animal print, metallic, floral or plain mesh|a deep low back|none|all skin shows through, the crotch is open|stretches to fit
open-crotch fishnet pantyhose|a wide fishnet pantyhose with a comfortable waistband|a back seam|the legs through net|the genital area|stretchy, waist-high
suspender pantyhose|sheer pantyhose with a lace top and attached suspender straps, open at the crotch|a back seam|the legs through sheer nylon|the genital area and hips|stretchy
rip-effect pirate set with corset top|a corset top with a hook-and-eye front, rip-effect pants and an eye patch|a lace-up back|the torso and legs|the midriff gaps in the rips|boned, relaxed pants
devil corset dress with tail|an underwire corset dress with a short flared skirt, tail and horned headband|a lace-up back|the torso and hips|the legs|boned, short
cat jumpsuit with marabou trim|a velvet jumpsuit with marabou cuffs, a removable tail and collar, and a deep zipper|a plain back with a tail loop|the whole body|the zipper-open chest|snug, full length
showgirl teddy with feather back|a sequined teddy with a plunging neckline|a fan of tulle and feathers springing from the seat|the torso|the legs and sides of the hips|snug, high-cut
harem set with veil|a foam-shaped bra with a metal chain trim, sheer harem trousers and a veil|a tie back|the bra only|the midriff and legs through sheer|loose trousers, tight bra
french maid set with crinoline skirt|an underwire-cup minidress with a ruffled apron and crinoline skirt|a zip back and ruffle-back panty|the torso and hips|the legs|short, flared
police-style dress with belt and cap|a button-front mini dress with a wide belt and a badge cap|a back zip|the torso and hips|the legs|short, fitted
waitress set with mesh apron|a satin dress with a collar and a sheer mesh apron|a zip back|the torso|the legs|short, fitted
matador set with bolero and cape|a bolero jacket, cropped trousers, sash and cape|a closed back|the torso and legs|the midriff|cropped, tailored
lace-up grommet minidress|a minidress with a collar and metal grommets laced up the front|a plain back with a zip|the torso and hips|the lace-up chest gap|short, fitted
open-back buckle dress|a mock-neck dress with a strappy buckle back|an open strap back|the front torso|the back|fitted
sarong with built-in thong|a side-tie wrap skirt in sheer fabric with an attached thong|a side tie|the pubic area|the hips and thighs through sheer|adjustable wrap
chain-draped body harness with garter|chains swagged across the chest and hips|a clasp back|the chains only|the entire body|adjustable
fur-trim brocade corset|painted brocade with a removable faux fur neckline|a lace-up back with removable garters|the torso|the legs|boned
""")
B['lingerie'] = P("""
parisian lace merry widow|a satin base with a ribbon-trimmed lace overlay and underwire cups|a hook-and-eye back with removable garters|the breasts, ribs and waist|the hips|boned, fitted
embroidered mesh balconette bra set|underwire balconette cups of embroidered mesh|a hook-and-eye back and a thong or brief|the breasts through mesh|the skin through the mesh|underwire
quilted satin corset|quilted satin with a side hook-and-eye|a lace-up back, adjustable straps|the torso|the hips|boned
jacquard dream corset|satin and lace with jacquard panels|a bi-directional lace-up back and detachable garters|the torso|the legs|boned
cracked-ice velvet and glitter corset|velvet and glitter insets|a lace-up back|the torso|the legs|all-round boning
zig-zag satin corset with contrast stitching|a satin corset with underwire cups|a lace-up back, detachable garters|the torso|the legs|boned
open mesh corselette|a mesh corselette with underwire cups|a lace-up back and removable garters|the torso through mesh|skin through the mesh|fitted
satin and lace bustier|a bustier with all-round boning|a mesh back with adjustable closure|the breasts and ribs|the hips|boned
lace overlay bustier with mesh back|a bustier of lace over satin|a mesh back|the torso|the hips|boned
stretch satin halter chemise|a halter chemise with a georgette flounce hem and zigzag stitching|removable garters at the back|the torso|the legs|short
satin and mesh chemise with floral appliqué|underwire cups, mesh body|adjustable straps|the torso through mesh|the legs|short, flowing
mandarin-collar mini chemise|a keyhole opening, frog closure and satin piping|a plain back, a matching G-string|the torso|the legs|short
velvet halter chemise with iridescent ruffle|a velvet halter bodice and an iridescent mesh ruffle|a tie neck, open back|the torso|the back and legs|short
beaded silk chemise with lace insets|silk with contrast lace insets|adjustable straps|the torso|the legs|flowing
satin shaper slip|a smooth fitted slip|a low back|the torso and hips|the legs|snug
lace-trim velvet cami|a velvet cami with a built-in bra|adjustable straps|the torso|the midriff|fitted
fringe cami set|a short cami with fringe trim and a hook-and-eye front|a plain back|the bust|the midriff|cropped
charmeuse chemise with eyelash lace|lace cups, side slit, two-tone eyelash lace|an X-back|the torso|the leg through the slit|flowing
babydoll teddy with mesh thong back|a sheer babydoll over a teddy with underwired cups|a mesh thong back|the torso|the legs|short
pleated-lace babydoll with lace G-string|all-round pleating|a lace G-string|the torso|the legs|short, flowing
ribbon-trim babydoll with open cups|sheer mesh with a cupless bodice|a ribbon-tie back|the ribs|the breasts|short
marabou-neck velvet babydoll|a velvet babydoll with pom-pom ties and a marabou neckline|a string bikini|the torso|the legs|short
holiday babydoll with faux-fur cap and bells|a velvet bra with fur trim, sheer skirting, bikini bottoms|a plain back|the torso|the midriff through sheer|short
ostrich-feather peignoir set|a full-length robe edged in feathers over a matching gown|a plain back with a sash|the whole body|nothing|floor length
charmeuse robe with inseam pockets|a full-length robe with a self belt|a plain back|the body when belted|the front when open|loose
long mesh robe with satin trim|a surplice tie front|a sheer back|the body lightly|the skin through mesh|floor length
short mesh and satin robe|piped, side-tie|a plain back|the body|the legs|short
embroidered georgette robe|floral appliqués over sheer georgette with a ribbon tie|a sheer back|the appliqués|the skin through georgette|long
silk nightshirt|an oversize button-front shirt with a chest pocket|a longer back|the torso|the legs|loose
satin and lace sleepshirt|contrast lace trim and a tie front|a shirt-tail hem|the torso|the legs|loose
ruffle-neck sleepshirt|ruffled neckline and lettuce hem|a plain back|the torso|the legs|loose
velvet teddy with lace-up front|underwire cups, sequins and pearls|a snap crotch|the torso|the legs|snug
embroidered teddy with double front straps|moldable mesh, underwire cups|a thong back and snap crotch|the torso|the legs|snug
menswear-style pinstripe teddy|underwire cups, lace trim|a strappy thong back with a bow|the torso|the legs|snug
""")
B['bras'] = P("""
three-way push-up bra|premolded foam cups with a front hook|convertible straps worn regular, crisscross or halter|the breasts|nothing|underwire
water-filled T-shirt bra|a smooth seamless cup with liquid-filled pockets|a hook-and-eye band|the whole breast|nothing|underwire
demi-cup liquid bra|half cups with liquid-filled pockets|convertible straps|the lower breast|the upper breast|underwire
tank bra with boy-short|a tank-shaped soft cup bra|a racer back, boy-short bottoms|the whole breast|nothing|stretchy
mesh underwire bra with contrast embroidery|mesh cups|a hook-and-eye band|the breasts|skin through mesh|underwire
beaded silk bra|underwire silk cups with beading|a hook-and-eye band|the breasts|nothing|underwire
rhinestone halter bra with neck clasp|a halter style bra|a back clasp|the breasts|the shoulders|wire-free
velvet bra with rhinestone trim|velvet underwire cups|a hook-and-eye band|the breasts|nothing|underwire
ruffled bralette|soft cups with ruffles|adjustable straps|the breasts|nothing|wire-free
adhesive backless combination bra|backless strapless cups with adhesive strips|none|the breasts|the back and shoulders|adhesive
four-way convertible satin bra|underwire cups|straps that cross, halter, one-shoulder or regular|the breasts|nothing|underwire
longline convertible bra|a longline band with a low back|a hook-and-eye band|the breasts and ribs|nothing|underwire
pinstripe bra with rose appliqué|underwire cups|a hook-and-eye band|the breasts|nothing|underwire
feather-embroidered mesh bra|padded cups covered in embroidered mesh|adjustable straps|the breasts|skin through mesh|underwire
deep-plunge strapless bra|fibre-filled underwire cups with a low centre|a strapless band|the breasts|the shoulders|underwire
juliette keyhole bra|a lace and satin cup with a keyhole in the centre|adjustable straps|the breasts|the skin through the keyhole|underwire
total fulfilment bra with push-up pads|deep plunge cups with removable pads|built-up straps|the breasts|nothing|underwire
open-tipped fibre-filled shelf bra|lace shelf with open tips|a hook band|the lower breasts|the nipples|underwire
power slimmer bra|underwire cups with removable pads|adjustable straps|the breasts and ribs|nothing|firm
enhancer bra with silicone inserts|a pocketed cup holding silicone shells|a hook band|the breasts|nothing|padded
coquette lace bra|fibre-filled cups, push-up|a hook band|the breasts|nothing|underwire
balconette shelf bra with demi-cup top|underwire lightly padded cups|a hook band|the lower breasts|the top edge|underwire
animal-trim mesh bra|fibre-filled, mesh-covered cups with leopard satin trim|a hook band|the breasts|nothing|underwire
rib-knit bralette|a fitted ribbed bralette|a racerback|the breasts|nothing|wire-free
cut-out front-hook bra|front hook with circular cut-outs|a racerback|the breasts|skin through cut-outs|wire-free
""")
B['panties'] = P("""
rio thong with smooth back fit|a high-waisted rio thong|a smooth narrow back|the front and hips|most of the buttocks|stretchy
string thong with bow|a minimal front with a bow|a string back|the pubic area|the buttocks|string-thin
scoop-front bikini|a low-dipping scoop front|a full back|the hips|nothing|low-rise
tap pant with lace|a loose lace-trimmed tap pant|a full back|the hips and buttocks|the legs|loose
ruffle-back boy-leg panty|a plain front|a ruffled back|the hips and buttocks|nothing|boy-leg
control brief with tummy panel|a high-rise slimming panel|a full back|the belly, hips and buttocks|nothing|firm
invisible control panty with removable pads|a front tummy panel|a back with removable pads|the belly and buttocks|nothing|firm
panty girdle with silicone leg grip|a flattening front|a full back, leg grippers|the belly, hips and thighs|nothing|firm
waist cincher brief|a high-waist brief with a hook-and-eye front|a high-cut seat|the waist and hips|the legs|boned
four-pad girdle|a girdle with removable hip pads|a lifted seat|the hips and buttocks|nothing|padded
invisible fanny panty|a lace front|foam-padded seat|the hips and buttocks|nothing|padded
power half slip|a smoothing slip|a webbed elastic waist|the hips and thighs|nothing|firm
keyhole-back thong|a minimal front|a keyhole opening|the pubic area|the buttocks|low-rise
lace-up back thong|a front triangle|a lace-up back|the pubic area|the buttocks|string-thin
crotchless panty|a lace panty with an open crotch|a full back|the hips|the genital area|stretchy
lace boy-leg panty|full coverage|a full back|the hips|nothing|boy-leg
seamless body liner|a full-length smooth liner|a smooth back|the whole torso|nothing|form-fitting
high-cut brief with satin trim|a high-cut brief|a full back|the hips|nothing|high-cut
tanga with strappy satin sides|a small front|a half-coverage back|the front|the hips|low-rise
G-string with metallic glimmer|a small front|a string back|the pubic area|the buttocks|string-thin
rib-knit boy-short|a rib-knit boy-short|a full back|the hips and buttocks|nothing|snug
stretch cotton boy-leg shorts|snug leg-lengthening shorts|a full back|the hips and thighs|nothing|snug
cotton scoop bikini|a low-cut front|a full back|the hips|nothing|low-rise
thong with sheer back|a satin strap front|a sheer back|the pubic area|the buttocks through sheer|string-thin
""")
B['clothing_sleep'] = P("""
fleece top and shorts set|a relaxed fleece top and shorts with contrast turn-back edges|a plain back|the torso and thighs|the legs|relaxed
fleece zip hoodie|a zip-front hooded jacket with front pockets|a hooded back|the torso|nothing|relaxed
fleece drawstring pants|a drawstring elastic waist|a plain back|the legs|nothing|relaxed
rib-knit lounger|a fit-and-flare dress with three-quarter sleeves and hook-and-eye details|a plain back|the torso and thighs|the lower legs|fitted
french terry top with push-up sleeves|a bateau neckline|a plain back|the torso|nothing|relaxed
stretch ankle leggings|a snug waist|a plain back|the legs|nothing|fitted
tape-trim cami|an empire cami with tape trim|adjustable straps|the torso|the midriff|fitted
rib-knit skirt|a fitted elastic waist skirt|a plain back|the hips|the legs|fitted
rhinestone lounger|a form-fitting top with a side slit|a plain back|the torso|the thighs|fitted
microfibre chemise|an empire waist|a plain back|the torso|the legs|form-following
built-in bra camisole set|a silky shaped cami with a built-in bra and a G-string|a plain back|the torso|the midriff|fitted
velvet cami set|a stretch velvet cami with shelf bra and princess seams, G-string|a plain back|the torso|the midriff|fitted
charmeuse cami set with tie slits|princess seams, tie-through buttonhole slits, tap shorts|a plain back|the torso|the midriff|relaxed
corset-inspired lace-up top|a lace-up front with a silk medallion inset|a plain back|the torso|the midriff|fitted
velvet slim-leg pants|a slim hugging pant|a plain back|the legs|nothing|slim
handkerchief top|a navel-kissing top with a dragon motif|a tie back|the bust|the midriff and back|short, flowing
cross-dyed lace blouse|a button-front lace blouse|a plain back|the arms|skin through lace|fitted
faux-fur trimmed cardigan|a button-front low V cardigan|a plain back|the torso|nothing|relaxed
leopard chiffon duster|a long flowing duster with faux fur trim|a flowing back|the body when closed|the front when open|long, loose
double-breasted pleather jacket|a structured jacket|a plain back|the torso|nothing|structured
pinstripe separates|a notched jacket, slim tapered pants and a tank dress|a back zip|the body|nothing|tailored
stretch jacket and skirt|a zip-front jacket and slim skirt|a back slit|the body|nothing|fitted
tube dress|a form-fitting tube|a plain back|the bust to the knee|the shoulders|form-fitting
short draped dress|crisscross draped sides|a low draped back|the torso|the back|short
foil velvet evening dress|a long slim-fitting dress|a plain back|the body|nothing|long
T-chain-back evening dress|a halter-style form-fitting dress|a back of chains|the front|the back|long
double-chain-back slinky evening dress|a scoop halter|a back of two bead chains|the front|the back|long
velvet jumpsuit with floral pattern|a close-fitting jumpsuit|a plain back|the body|nothing|fitted
""")
B['accessories'] = P("""
backseam stockings with shaded heel|sheer stockings|a seam up the back|the legs|nothing|sheer
Cuban heel two-tone stockings|a reinforced heel|a seam|the legs|nothing|sheer
metallic pantyhose|a sheer metallic sheen|a back seam|the legs|nothing|stretchy
floral net pantyhose|printed net with French-cut legs|a plain back|the legs through net|skin through net|stretchy
fishnet pantyhose in wide, backseam and crisscross nets|a wide net|a seam|the legs through net|skin|stretchy
control-top pantyhose|shaping sheer|a smooth back|the legs|nothing|firm
sure-grip lace-top thigh-highs|a lace welt|a plain back|the legs|nothing|stay-up
lace garter belt with removable garters|a wide lace belt|a hook back|the waist|the hips|adjustable
detachable garters for corset|elastic garters|a clip|the thigh|nothing|adjustable
brocade underwire corset with garters|brocade underwire cups|a laced back|the torso|the legs|boned
rhinestone box-chain bra straps|chain straps|a clip|the straps|nothing|adjustable
sequined pasties with fringe|fringe-tasseled adhesive covers|an adhesive back|the nipples|the rest|adhesive
heart-shaped pasties|small heart adhesive covers|an adhesive back|the nipples|the rest|adhesive
body glitter chain belt|a waist chain|a clasp|the chain|the waist|adjustable
leg chain|a thigh chain|a clasp|the chain|the leg|adjustable
feather fan|a marabou fan|plain|nothing|nothing|handheld
gloves in satin|a wrist-length glove|a button|the hands|the fingertips|stretchy
collar choker|a satin choker|a hook|the neck|nothing|adjustable
horned headband|a headband with horns|plain|nothing|nothing|adjustable
eye patch|a satin patch|an elastic strap|one eye|the other|adjustable
removable tail|a tail with a clip|a clip|nothing|nothing|clip
animal ears headband|ears on a band|plain|nothing|nothing|adjustable
mask with feathers|a feathered mask|ribbon|the eyes|nothing|adjustable
nurse-style cap|a satin cap|a pin|the head|nothing|adjustable
rhinestone ankle chain|a delicate anklet|a clasp|the ankle|nothing|adjustable
""")
B['sale'] = P("""
foil velvet bra and panty|lightly padded underwire cups with a goldtone foil rose print|a thong back|the breasts|nothing|underwire
foil velvet bustier set|a bustier with adjustable straps and detachable garters|a smooth back|the torso|the legs|boned
sequin gown with mesh flounce|a scoop low-cut front|an open back|the torso|the back|long
holiday faux-fur four-piece set|a satin bra with a ruffle and fur cuffs, G-string|a plain back|the torso|the midriff|set
chain halter teddy|a halter teddy with a chain neck|an open back|the torso|the back|snug
iced satin push-up bra and panty|deep-plunge padded cups|a thong back|the breasts|nothing|underwire
mesh bra and G-string|mesh cups|a thong back|the breasts through mesh|skin|underwire
sheer metallic bra and thong|sheer cups with a metallic glimmer|a thong back|the breasts|skin|underwire
animal-trim stretch-mesh chemise|molded cups with animal print trim|a keyhole back|the torso|the legs|short
plunging V-neck leopard chemise|a low-cut back|a V back|the torso|the legs|short
rib-knit cami|fitted ribbed cami|adjustable straps|the torso|nothing|fitted
tank bra and boy-short in lycra mesh|a tank bra|a racerback|the torso|nothing|stretchy
rhinestone tee|a form-fitting stretch tee with crystals|a plain back|the torso|nothing|fitted
stretch wet-look velvet dress|V necklines|a deep V back|the body|the V|fitted
sparkling ombre dress|a draped front on spaghetti straps|an open back|the body|the back|fitted
star-burst crystal evening dress|a fitted crystal-star dress|a plain back|the body|nothing|long
butterfly mesh and velvet dress|a deep scoop neckline|a sparkled back|the torso|the arms|fitted
chinese-style silky dress with high slit|a fitted dress|a plain back|the body|the leg through slit|fitted
dragon velvet dress|a fitted velvet dress|a plain back|the body|nothing|fitted
bias-cut nylon boudoir gown|a bias-cut gown|a plain back|the body|nothing|long
brocade underwire corset|brocade cups|a laced back|the torso|nothing|boned
ultimate corset with inner cincher|an inner cincher band, zip front|a bi-directional back cinch|the torso|nothing|boned
renaissance corset|bust-lifting, boned|a back that cinches with garters|the torso|nothing|boned
satin underwire corset with lace front|boned lace front|a hook-and-eye back|the torso|nothing|boned
power lace corset slip|a boned slimming slip|a front hook-and-eye|the torso|nothing|firm
strapless shimmer-lace corset|fibre-filled underwire cups|a powernet back|the torso|nothing|firm
""")
B['swim'] = P("""
underwire V-cup thong one-piece with chain-link shoulder straps|a one-piece with moulded underwire cups forming a gentle V at the bust, a gathered centre, thin shoulder straps of small metal chain links and a smooth satin-finish fabric down to a high-cut leg|the straps run straight down the back to a low scoop and the seat is a thong cut|the chest, the stomach and the front of the hips|the back above the scoop, the sides of the hips and the buttocks|snug, high-cut leg, adjustable chain straps
plunge-to-navel leopard thong one-piece with centre ring|a one-piece in a leopard print with a deep plunge down to the navel, a large round metal ring at the centre of the neckline and wide shoulder straps|a low scoop back and a thong seat|the sides of the chest, the stomach sides and the hips|the centre of the chest to the navel, the back and the buttocks|snug, high-cut leg, deep plunge
crop bikini top with wide straps|a short band-style top ending just below the bust with a scooped neckline and wide shoulder straps|a hook or pull-on band with wide straps at the back|the whole bust|the midriff and the shoulders|fitted, sporty, lightly lined
triangle bikini top with sliding ties|two triangle cups on a string that slides along the ties to adjust the coverage|a tie at the neck and a tie across the back|the nipple area and part of the breasts|the sides of the chest and the back|adjustable, minimal
bandeau bikini top with ruched centre|a straight strapless band across the chest with a gathered twist at the centre|a hook or pull-on band with a clear silicone grip|the whole bust|the shoulders and the back|strapless, lightly padded
halter triangle bikini top with neck tie|triangle cups pulled up to a halter tie behind the neck|a tied strap across the back|the nipple area and part of the breasts|the shoulders, the sides of the chest and the back|adjustable halter
underwire bikini top with cut-out|moulded underwire cups with a small open cut-out between them|a hook band with thin straps|the bust|the cut-out gap|supportive, lined
Brazilian bikini bottom|a low-rise front with narrow sides and a scooped seat that covers part of the buttocks|a rear that is cut high and narrow, leaving the lower part of the buttocks bare|the pubic area and the top of the buttocks|the lower buttocks and the hips|snug, narrow sides
cheeky bikini bottom|a low-rise front with a rear that is scooped to leave the lower curve of the buttocks bare|a rear cut in a curve below the buttocks|the pubic area and part of the seat|the lower buttocks|snug, scooped
high-cut bikini bottom|a bottom with leg openings cut high over the hips and a mid-rise waist|full coverage across the seat with a high leg line|the pubic area and the seat|the hips|high leg line, mid-rise
scrunch-back bikini bottom|a low-rise front with a gathered, ruched seat that is stitched with elastic|a ruched rear that bunches the fabric|the pubic area and the seat|the hips|ruched, lifted seat
tie-side bikini bottom|a triangle front joined to a thin tie at each hip|a triangle rear with the ties knotted at the hip|the pubic area and the seat|the hips|adjustable, string sides
thong bikini bottom with side rings|a small front triangle with a metal ring on each hip|a thong back with a narrow strap|the pubic area|the hips and the buttocks|string-thin, ring hardware
short-cut swim short|a short swim short with a wide waistband, ending high on the thigh|a full seat|the hips and the seat|the thighs|short, stretchy
sailor-stripe bikini set|a bikini top and bottom with bold horizontal stripes and a contrast trim|a tie back and a ruched bottom|the bust and the hips|the midriff|fitted, retro
chain-trim bikini set|a triangle bikini with small metal chain links on the straps and the hips|a tie at the neck and back, chain links at the hips|the nipple area and the pubic area|the sides of the chest and the hips|adjustable, minimal
sling swim brief with shoulder straps|a small pouch front with two straps that rise from the hips, run up the sides of the chest and over both shoulders, joining behind the neck|the straps join at the nape and run down the middle of the back into a thong|the pouch and the pubic area|the chest, the sides of the torso, the back and the buttocks|one-piece, thong-cut, adjustable straps
suspender thong swim brief|a narrow V-shaped front pouch held by two straps that rise from the hip edges over the shoulders|a single strap down the spine and a thong seat|the pouch only|the chest, torso sides and buttocks|strap-held, minimal, stretchy
classic monokini|a high-waisted bikini bottom linked to two wide straps that rise to a halter neck and leave the chest uncovered|a low open back with a tie at the neck and waist|the hips and the stomach|the chest and the back|halter-held, one-piece
plunging monokini|a one-piece with cut-away sides and a deep plunge to the navel|a bare back with a tie|the hips and a strip down the centre of the chest|the sides of the chest and the back|plunging, snug
sling bikini|a single front panel whose side straps run up over the chest and across both shoulders, joining behind the neck|the straps meet at the nape and run down the centre of the back as a thong to the waist|the nipple area and the pubic area|the sides of the torso, the back and most of the buttocks|one-piece, strap-based, adjustable at the neck
suspender thong bikini|a small bottom triangle linked by two straps that rise over the shoulders|a thin strap running down the spine into a thong back|the nipple area and the pubic area|the torso sides and the back|stretchy and snug
pretzel bikini|a small chest panel with a strap looped around the neck and a second set of straps encircling the midriff|an open back with the midriff straps tied at the spine|the nipples and the pubic area|the rest of the torso|ultra-minimal strap design
monokini with halter straps|a one-piece bottom hung from two halter straps that rise between the breasts and pass around the neck|a small back strap and a thong or full back|the lower body|the chest is left bare|halter-style, low-slung
monokini with mesh link|a bikini-style bottom joined to a top by a sheer mesh panel down the centre|a plain back with a tie|the chest and hips|the sides of the torso|sheer centre, plunging
chain-linked monokini|a bikini top and brief joined by gold-tone chains at the sides|a tie back and a thong seat|the chest and hips|the midriff|adjustable, fine chains
ring-linked one-piece|metal rings joining a top panel to the bottom at each hip|an open back with a tie|the chest and hips|the sides of the torso|adjustable
micro bikini with thin strings|tiny triangles on ultra-thin side strings|a thong back|the nipples and the pubic area|almost everything else|extremely small
G-string micro bikini|a tiny front piece on a thin string|a string back|a tiny triangle at the front|the sides and buttocks|string-thin
crochet micro bikini|open-weave triangles with a tie-sides bottom|a tie back|the nipple area and the pubic area partly|the skin through the weave|handmade look
invisible-look micro bikini|a minimal panel in near-clear stretch fabric|an almost invisible strap|a thin panel|nearly everything|ultra-stretch
sheer seekini|a see-through bikini in sheer mesh|a sheer back with a tie|nothing opaque|the whole body shows through the mesh|sheer, snug
hip-ring string bikini|a small triangle bottom with a ring at each hip|a thong back|the pubic area|the hips and buttocks|string-sided
multi-strap harness bikini|criss-cross straps over the torso forming a harness|crossed straps on the back|the straps only|the skin between the straps|adjustable
X-front string bikini|two triangles linked by straps crossing in an X at the chest|an open back with a tie|the nipples|the sides of the chest|adjustable
ladder-strap bikini|stacked horizontal straps across the chest and hips|a thong back|the straps|the skin between them|stretchy
bandage-wrap bikini|narrow strips wound around the torso like bandages|a tie at the back|the strips|the gaps between strips|wrap fit
O-ring cut-out one-piece|a one-piece with large round windows at the stomach and sides|a low open back|the chest and hips|the cut-out windows|snug
gladiator strap one-piece|a one-piece with crossing straps across the stomach and hips|a deep open back|the chest and hips|the strap gaps|fitted
backless halter one-piece|a plunging halter front with a deep V|a completely open back to the waist|the chest and hips|the back and the midriff in the V|snug
demikini|a backless, strapless top held on with skin-safe gel|no straps, bare back|the front of the chest|the back and the shoulders|gel-grip
tan-through swimsuit|a swimsuit of micro-perforated fabric|a full-coverage back with tiny holes|the body, with tiny holes that let light through|the skin through the perforations|snug
inflatable push-up bikini|a bikini top with air-filled pads|a hook-and-eye back|the chest|nothing|padded
metal bandeau bikini|a rigid polished metal chest piece|a hinge back|the chest|the shoulders|rigid
crystal-covered bikini|triangles and a brief studded with thousands of rhinestones|a tie back|the chest and the pubic area|the hips|sparkle
shell-and-bead bikini|a top of real-looking shell cups on beaded strings|a beaded tie back|the chest|the midriff|beach style
fringe bikini|a bikini edged with long swinging fringe|a tie back|the chest and hips|the midriff|loose fringe
LED-trim bikini|a bikini with light-up trim lines|a tie back|the chest and hips|the midriff|adjustable
printed artwork bikini|a bikini printed with a full scene|a tie back|the chest and hips|the midriff|snug
reversible two-in-one bikini|a bikini that flips to a second print|a tie back|the chest and hips|the midriff|reversible
swimsuit with detachable skirt|a one-piece with a clip-on skirt|a low scoop back|the body and thighs|the legs|modest
""")
FAB = {
 'swim': "stretch lycra|matt lycra|crochet|sheer mesh|metallic spandex|neoprene|ribbed knit|elastic cord|satin-finish spandex|digitally printed nylon",
 'ultra': "embroidered tulle|stretch lace|sheer mesh|liquid satin|stretch velvet|diamond-weave fishnet|wet-look stretch fabric|sequined mesh|marabou-trimmed satin|metallic mesh|leopard-print lace|sheer chiffon",
 'lingerie': "stretch lace|satin|charmeuse|silk|sheer georgette|velvet|iridescent mesh|brocade|eyelash lace|embroidered mesh|pleated chiffon|jacquard",
 'bras': "microfibre|stretch lace|satin|mesh|cotton jersey|velvet|ribbed knit|silk|moulded foam covered in lace|seamless nylon|liquid satin",
 'panties': "stretch lace|satin|cotton knit|microfibre|mesh|powernet|liquid satin|fishnet|jersey|chiffon",
 'clothing_sleep': "fleece|rib-knit cotton|stretch velvet|matte jersey|charmeuse|microfibre|french terry|polyester crepe|lace|satin|faux fur|pleather",
 'accessories': "satin|lace|sheer nylon|metallic nylon|fishnet|rhinestones and chain|velvet|feathers|faux leather|patent|crystal-set metal",
 'sale': "foil velvet|sequined fabric|brocade|satin|lace|jersey|stretch mesh|charmeuse|crushed velvet|pleather"}
TRIM = "a satin bow|rhinestone accents|scalloped lace edging|contrast piping|ribbon ties|a row of small pearls|marabou edging|metal O-rings|a ruffled edge|a hook-and-eye placket|adjustable slider straps|tonal embroidery|a small charm at the centre|a lace-up panel|beaded appliqué|a deep lettuce-edge hem|contrast stitching|silver hardware|gold-tone chain|ruched side panels|a fringe|crisscross straps"
COL = "black|ivory|crimson|midnight blue|burgundy|champagne|blush pink|emerald|silver|gold|leopard print|zebra print|lavender|white|nude|hot pink|royal purple|teal|bronze|red and black|black and gold|cream and rose|turquoise|plum|jade"
