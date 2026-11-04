"""Sock lengths/styles (many ankle-height), and odd, translucent and unusual materials for socks."""
from vocab_lib import S
def P(t): return [tuple(x.split('|')) for x in t.strip().split('\n') if x.strip()]
ANKLE = P("""anklet socks|They are short socks that stop just above the ankle bone.
ankle socks|They end at the ankle with a small folded cuff.
no-show socks|They are cut so low that they hide inside a shoe, with a silicone heel grip.
low-cut socks|They have a low line that sits below the ankle bone.
quarter-height socks|They rise a quarter of the way up the calf from the ankle.
footie socks|They are the shortest socks, covering only the foot with a low scooped edge.
lace-trimmed anklet socks|They are short socks with a lace frill at the ankle.
ruffled anklet socks|They are short socks with a gathered ruffle at the cuff.
frilly cuffed anklet socks|They are short socks with a deep double frill around the ankle.
turn-down ankle socks|They end at the ankle with a wide cuff that folds over.
ballet-flat liner socks|They are scooped very low so that they do not show above a flat shoe.
sneaker liner socks|They are cut very low with a gripping heel and a thin sole.
tabi ankle socks|They are short split-toe socks with a separate big toe.
toe-spring anklet socks|They have five separate toes and end at the ankle.
pom-pom anklet socks|They are short socks with a tiny pom-pom at each heel.
bobby socks|They are short folded-cuff socks that end just above the ankle.
mary-jane lace anklets|They are fine anklets with a scalloped lace top.
airy anklet socks|They are short, almost transparent socks with a faint seam at the toe.
open-weave anklet socks|They are short open-net socks that end at the ankle.
ankle-strap sock sandals|They are short socks with a strap that crosses the ankle.
mesh sport anklets|They are short, breathable socks with a vented mesh top.
cushioned ankle socks|They are short socks with a thick padded sole.""")
LONG = P("""crew socks|They rise to the middle of the calf with a ribbed cuff.
knee-high socks|They rise to just below the knee with an elastic cuff.
over-the-knee socks|They rise above the knee with a stay-up silicone top.
thigh-high stockings|They reach the upper thigh with a deep lace band.
tube socks|They are long, straight-sided socks with no heel shaping.
toe socks|They have five separate toes and a cushioned sole.
leg warmers with a foot opening|They are long tubes that stretch from the ankle to the knee with an open heel.
slouch socks|They are loose and bunched around the ankle and calf.
stirrup socks|They have a strap that passes under the arch and leave the heel open.
garter-style hold-ups|They stay up by themselves with a silicone band at the top.
compression socks|They are graduated-compression socks that rise to the calf.
ski socks|They are tall, thick, cushioned socks that rise to the knee.
hiking socks|They are padded socks with a cushioned heel and arch band.
slipper socks|They are chunky lounge socks with a gripper sole.
boot socks|They are heavy cushioned socks with a rolled cuff.
rain-boot liner socks|They are long soft socks for wearing inside tall boots.
tights with footed ends|They are opaque or sheer tights that cover the whole leg and the foot.
patterned stockings|They are long stockings with a repeating pattern.
seamed stockings|They have a dark line up the back of the leg.
pop socks|They are sheer, knee-length socks that gather at the top.""")
THIGH = P("""thigh-high socks|They reach all the way to the top of the thigh with a snug band that grips the leg.
thigh-high stockings|They reach the upper thigh with a deep lace band.
stay-up thigh-highs|They stay up by themselves with a wide silicone grip at the top of the thigh.
lace-topped thigh-highs|They reach the top of the thigh with a wide scalloped lace edge.
very fine thigh-high stockings|They are almost transparent and run the whole length of the leg to the top of the thigh.
open-weave thigh-highs|They are open-net stockings that reach the top of the thigh.
ribbed thigh-high socks|They are chunky ribbed socks that reach the top of the thigh.
cable-knit thigh-high socks|They are thick cable-knit socks that climb to the top of the thigh.
striped thigh-high socks|They are striped from the ankle to the top of the thigh.
ruffle-topped thigh-highs|They reach the top of the thigh with a gathered ruffle.
bow-topped thigh-highs|They reach the top of the thigh with a small ribbon bow on the outside.
garter-belt stockings|They reach the top of the thigh and clip to a garter belt with metal clasps.
back-seam thigh-high stockings|They have a dark seam line running up the back of the leg to the top of the thigh.
glossy fitted thigh-high socks|They are fitted, stretchy and glossy, reaching the top of the thigh.
plush-banded thigh-high socks|They reach the top of the thigh with a soft, deep band of pile.
thigh-high leg warmers|They are long soft tubes that cover the leg from the ankle to the top of the thigh.
thigh-high compression stockings|They are graduated-compression stockings that reach the top of the thigh.
thigh-high boot socks|They are tall, cushioned socks made to go inside high boots, reaching the top of the thigh.
thigh-high toe socks|They have five separate toes and reach the top of the thigh.
thigh-high stirrup stockings|They have a strap under the arch and reach the top of the thigh.""")
STYLES = ANKLE + LONG + THIGH
# odd, translucent and unusual materials, by price band.  Each is an item phrase (no commas).
ODD = {
 'low': S("clear PVC film, translucent vinyl, sheer nylon net, nylon mesh, fishnet nylon, cheap polyester tulle, thin organza-look polyester, clear plastic sheeting, frosted plastic wrap, shiny metallic polyester, aluminium-look foil fabric, faux fur, long-pile faux fur, short-pile plush faux fur, fleece, teddy-bear plush, faux leather, patent-look vinyl, rubberised cotton, neoprene, foam rubber, jelly-look silicone, rubber bands wound into stripes, plastic bag yarn, paper yarn, raffia-look plastic, cellophane, mesh with sequins glued on, glitter netting, stretch lace, sheer lace-print polyester, faux suede, faux shearling, towelling, felt, terry loops, cotton string knit, packing-twine knit, plastic cord knit, transparent mesh with a printed pattern"),
 'mid': S("real sheer silk, fine nylon gauze, soft tulle, silk organza, silk chiffon, open-work fishnet, lace in cotton thread, nylon lace, hand-knotted net, fine metallic lamé, glossy lamé, iridescent film fabric, holographic foil fabric, sheer iridescent polyester, genuine suede, soft lambskin leather, grained leather, patent leather, nubuck, shearling, sheepskin, rabbit-style fur, long-haired goat fur, soft rex-style pile, mohair, angora, rubber latex, thin silicone, wetsuit neoprene, clear vinyl with embroidered details, leather-look knit, hand-crocheted rope, hemp rope, jute twine, waxed cotton cord, knitted copper wire, hand-knitted fine wire, woven paper ribbon, raffia, woven grass, wool felt, boiled wool, velvet, velour, chenille, sequined mesh, bead-embroidered mesh, rhinestone mesh"),
 'high': S("hand-knotted silk net, gossamer silk gauze, Chantilly lace, Alençon lace, hand-made bobbin lace, silk tulle with hand-sewn pearls, cloth of silver, cloth of gold, fine gold-thread mesh, silver-thread mesh, spun-gold lamé, hand-beaded glass bead net, woven glass-bead fabric, crystal-beaded mesh, fine chainmail of sterling silver rings, fine chainmail of gilded rings, knitted fine silver wire, knitted gold wire, fine kid leather, buttery lambskin, nappa leather, crocodile-embossed leather, python-skin leather, stingray leather, hand-pierced leather lace, soft deerskin, fine mink-style fur, sable-style fur, chinchilla-style fur, silver fox-style fur, long silky fur trimmed with satin, fur-lined sheer silk, ostrich feather, marabou feather trim, swan-down trim, peacock feather mosaic, silk velvet devoré, burnout velvet, iridescent silk taffeta, fibre-optic fabric, thermochromic fabric that changes colour, glow-in-the-dark knit, hand-poured clear resin film, mother-of-pearl paillettes"),
}
ODDCON = {
 'low': S("machine-knit with a plain top, knit in one piece with a flat toe seam, stitched with a visible seam up the back, glued at the toe, printed with a simple pattern, gathered with a rubber band at the top, trimmed with a plain elastic cuff, finished with an overlocked edge, heat-sealed at the toe, sewn with a basic heel patch"),
 'mid': S("hand-finished at the toe, fully lined at the foot, lined at the sole only, with a reinforced heel and toe, lace-trimmed at the cuff, edged with satin ribbon, bound with silk tape, finished with a ruffled cuff, with a double-layer foot over a sheer leg, with a seam running down the back, stitched with contrast thread, with a tailored gusset at the heel"),
 'high': S("hand-sewn on a fine foot form, fully hand-finished with a silk-lined sole, with hand-applied beading at the ankle, edged with hand-rolled picot, embroidered by hand up the leg, set with tiny jewels at the cuff, finished with a gilt-thread top band, lined with scented silk, tailored to the foot by a couturier, with a hand-linked toe and a hidden seam"),
}
ODDFORM = S("They are see-through, so the foot shows through, They are see-through with a bold seam at the heel, They are fully translucent with a darker toe and heel, They are lightly sheer at the leg and opaque at the foot, They have a mixed look with a transparent leg and a solid foot, They look almost like a second skin, They catch the light in a metallic sheen, They have a rubbery sheen, They are fuzzy and plush all over, They are soft and thick with a long pile, They are stiff and shaped like leather, They are glossy and wet-look, They shimmer when they move, They are lightly cushioned and bouncy, They are clearly handmade and a little irregular, They are bold and strange in texture, They are pale and delicate, They look as if made for a theatre costume, They are made to be seen above the shoe, They are made to be worn with open sandals")
