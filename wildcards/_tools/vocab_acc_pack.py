"""Unusual / sculptural / experimental backpacks (research: Kofta Studio sculptural bags, Issey Miyake Bao Bao, Eastpak designer editions, Orphosis/Moondarra expanding packs, Meiosis tension-assembled shell, Maharam architectural packs, bio-leathers, inflatables, modular, transparent, hard-shell, kinetic)."""
from vocab_lib import S

SHAPES_RAW = """geometric prism backpack|It is a faceted prism of rigid panels with sharp angular edges and a hinged lid.
cylinder backpack|It is a tall, perfectly round cylinder carried upright on the back with a flat circular lid.
cone backpack|It is a tapering cone that narrows to a point at the top, worn like a small tent.
cube backpack|It is a hard-edged cube with a single seam and a square flap opening.
cycloid backpack|It is a smooth, curved, wheel-like form with no corners, carried in the middle of the back.
origami-folded backpack|It is made from a single sheet that folds into a crisp pattern of pleats and can expand or collapse.
expanding accordion backpack|It has a pleated body that extends outward in stages like a bellows when opened.
inflatable backpack|It is a puffed, air-filled form with soft rounded lobes and a valve at one side.
cloud-shaped backpack|It is a soft, billowing, unstructured silhouette of puffy quilted pillows.
turtle-shell backpack|It is a domed hard shell of overlapping plates that curves over the back.
armadillo backpack|It is built from articulated overlapping bands that flex and roll like armor.
geodesic dome backpack|It is a small dome of triangular panels fixed to a harness.
spherical backpack|It is a perfect sphere with a zipper running around its equator.
hexagonal honeycomb backpack|It is a cluster of six-sided cells, each cell a separate pocket.
pyramid backpack|It is a four-sided pyramid with a narrow apex rising behind the head.
teardrop backpack|It is a long, smooth teardrop that swells at the base and tapers up.
egg-shaped backpack|It is a smooth oval shell split at the middle by a hinge.
crescent backpack|It is a crescent moon that curves around the back and shoulder.
spiral backpack|It is a coiled form that winds around itself in a smooth spiral.
asymmetrical sculptural backpack|It is an off-balance, angular form that leans to one side with no symmetrical edge.
twisted ribbon backpack|It is a long band of material twisted into a looping knot-like form.
tent-like backpack|It is a peaked, canopy-shaped pack with tensioned ridgelines and guy-line loops.
shell-ribbed backpack|It has a radiating fan of ribs like a scallop shell.
fish-scale backpack|It is covered in overlapping scale-like plates that shimmer as it moves.
creature backpack|It is a sculpted animal-like figure with a rounded head, stubby limbs and a tail, carried on the back.
animal-head backpack|It is shaped like the head of a large animal, with ears and a snout, the opening in the back of the head.
mushroom-shaped backpack|It is a wide domed cap atop a short, stout stem.
vegetable-shaped backpack|It is a sculpted giant vegetable with a leafy top and a ridged, rounded body.
house-shaped backpack|It is a miniature house with a peaked roof, a door flap and little windows.
lantern backpack|It is a ribbed paper-lantern form that collapses flat and glows from within.
birdcage backpack|It is an open frame of fine wires shaped like an ornate birdcage with a hinged door.
bellows backpack|It is a camera-bellows pack with a leather accordion body and a rigid front plate.
suitcase backpack|It is a miniature hard-sided suitcase with corner guards, harnessed to the back.
radio-shaped backpack|It is a sculpted vintage radio with a dial, a speaker grille and an antenna.
cassette-shaped backpack|It is a giant audio cassette with two visible spools and a tape window.
television-shaped backpack|It is a boxy old television set with a rounded screen and knobs.
ship-in-a-bottle backpack|It is a clear bottle-shaped pack that holds a small model ship inside the window.
globe backpack|It is a sphere printed as a world globe, spinning slightly on its mount.
hourglass backpack|It is a waisted form with two rounded bulbs joined at a narrow pinch.
tiered stacked backpack|It is a tower of three or four discs, each disc a separate zipped pocket.
modular grid backpack|It is a base harness with magnetic squares that snap together in a grid.
pocket-covered backpack|It is covered in dozens of small pockets of different sizes, some stitched shut.
patchwork backpack|It is assembled from dozens of mismatched fabric and leather patches.
braided rope backpack|It is a mesh of thick knotted rope, with a small lined pouch hung at the center.
net-bag backpack|It is a stretchy net that bulges around its contents and shows them through the mesh.
basket backpack|It is a woven basket frame with shoulder straps made of wide braided bands.
wicker backpack|It is a hand-woven wicker form with a domed lid and leather straps.
log-shaped backpack|It is a carved wood log, hollowed and fitted with a hinged lid and straps.
barrel backpack|It is a small wooden barrel with iron hoops and a lid on the top.
bucket backpack|It is a flared bucket with a cinched collar and a rope drawstring.
fire-hose backpack|It is a coil of flattened, riveted fire hose with a plain buckle closure.
frame-and-sling backpack|It is a minimal wire frame holding a loose sling of fabric.
exoskeleton backpack|It is a lattice of jointed metal-look ribs worn like a skeleton on the back.
satellite-dish backpack|It is a shallow dish with a central antenna arm.
jellyfish backpack|It is a translucent dome fringed with long hanging strands.
coral-shaped backpack|It is a branching, spiky cluster of tubular forms.
cactus backpack|It is a ribbed green column with short padded arms and a flat-topped opening.
tree-stump backpack|It is a cross-section of trunk with visible rings, hollowed for storage.
wing backpack|It has folded fabric wings that can fan out from the sides.
umbrella backpack|It has a collapsible canopy that pops out of the top like an umbrella.
transparent backpack|It is a clear shell that shows its contents and a visible internal skeleton.
hard-shell capsule backpack|It is a smooth capsule of molded shell with a seam at the middle.
backpack that doubles as a chair|It unfolds from its pack form into a small seat on legs.
backpack that doubles as a tent|It opens up into a small shelter on a collapsible frame.
transformer poncho backpack|It unzips and unfolds into a hooded rain poncho.
suspended hammock backpack|It is a hanging cradle that swings between two straps.
sculptural bag-on-back|It is an abstract object whose shape resembles a draped cloth caught in a gust.
cubist backpack|It is a collage of flat planes seen from several angles at once.
deconstructed backpack|It has exposed seams, hanging threads and cut-away panels.
recycled-object backpack|It is assembled from salvaged objects fixed together onto a frame.
bubble-wrap backpack|It is lined with huge air bubbles that pop out in clusters.
pillow backpack|It is a pair of soft, over-stuffed pillow-like cushions on a strap.
monolith backpack|It is a slim, tall slab with perfectly flat sides and a hidden zipper.
ring-shaped backpack|It is a hollow ring that hangs at the back, holding its contents in the circle.
orbital backpack|It has several small spheres that circle a central core on thin arms.
piano-shaped backpack|It is a miniature upright piano with a keyboard-pattern flap.
camera-shaped backpack|It is a giant vintage camera with a round lens flap and a viewfinder pocket.
pagoda backpack|It is a stack of tiered, upswept roofs with a small door at the base.
spine backpack|It is a long jointed ridge of vertebra-like segments down the back.
accordion-folded paper backpack|It is a stiff folded-paper bag that fans open in a starburst.""".strip().split('\n')
SHAPES = [tuple(l.split('|')) for l in SHAPES_RAW]

MAT_ODD = {
 'low': S("PVC vinyl, clear TPU film, shiny metallic film, bubble-wrap laminate, holographic nylon, inflatable PVC, neoprene, recycled bottle fabric, recycled shopping-bag plastic, faux fur with a long pile, quilted puffer nylon, translucent vinyl, bonded foam, polyester felt, pleated polyester, glitter-filled vinyl, mesh netting, coated paper, plastic sheeting, rubberized fabric, shiny lamé fabric, reflective nylon, glossy patent vinyl, gel-filled panels, silicone-coated fabric"),
 'mid': S("fused recycled plastic, mushroom leather, apple-skin leather, cork fabric, waxed linen, felted wool, boiled wool, thick woven rope, knotted macramé cord, braided leather strips, crocheted cotton cord, 3D-knit yarn, heavy sailcloth, salvaged parachute fabric, upcycled seatbelt webbing, rubber inner tube, reclaimed billboard vinyl, banner canvas, pineapple-leaf fibre, cactus leather, patched denim, hemp canvas, woven plastic strapping, birch bark veneer, laser-cut wood veneer, thermoformed polycarbonate, translucent polycarbonate, expanded foam, quilted patchwork, thick wool felt, woven wire mesh, chainmail mesh, raffia, wicker, rattan, willow weave, seaweed-based textile, algae-based textile"),
 'high': S("carbon-fibre composite, aerospace-grade titanium mesh, hand-folded Tyvek-like sheets, lab-grown mycelium leather, spider-silk-style fibre, iridescent holographic film, dichroic film, mirror-polished stainless steel scales, sheet-copper scales, hand-beaten aluminum plates, hand-blown glass panels, handmade felt sculpted over a mold, latex from the rubber tree, hand-woven fibre-optic fabric, LED-woven fabric, E-Ink panels, temperature-reactive fabric, shape-memory alloy mesh, cast resin, hand-carved wood panels, gilded wood, brass sheet with a patina, hand-knotted silk cord, silk organza over a wire frame, hand-woven bark cloth, bronze-cast fittings, laser-cut acrylic layers, lacquered paper, hand-washed paper pulp, leather tooled in relief, shagreen")}
CONS_ODD = {
 'low': S("heat-sealed along the seams, welded plastic seams, molded in one piece, cut from a single flat pattern, glued into shape, taped at the seams, zipped together from simple panels, sewn from a few large panels, sewn with oversized visible stitches, fused with heat"),
 'mid': S("folded origami-style from a single sheet, assembled by tension rather than sewing, laser-cut and interlocked without thread, thermoformed over a mold, hand-woven into shape, hand-knotted on a frame, hand-stitched with oversized thread, held together with rivets and straps, assembled from interlocking modular blocks, clipped together with magnetic joints, wrapped and glued over a wire frame, built up in layers like papier-mâché, sculpted over a mold and fused, stitched in a single seam at the base, patchworked piece by piece"),
 'high': S("hand-sculpted over a form by a single maker, cast from a mold made by the artist, hand-woven by a master weaver into a seamless shape, hand-folded from a single sheet using a complex origami crease pattern, assembled by tension and geometric locks, shaped by shrinking the material so the parts lock themselves, hand-welded from thin metal scales, hand-knotted over many months, hand-molded and fused by an artist, hand-carved and joined with hidden dovetails, built on a handmade frame and covered with hand-cut panels, one-off, made by an artist as a wearable sculpture")}
FEATURE_ODD = S("a hidden zipper that follows the edge of the form, a closure that is a single oversized magnet, a pull cord that doubles as a decorative tassel, a flap held shut by a wooden toggle, a window in the side that shows the contents, an LED strip that glows along the seams, an air valve that adjusts its firmness, straps that look like climbing rope, straps made of woven seatbelt webbing, straps of braided cord, straps of chain, straps of sculpted leather in the shape of a ribbon, a handle shaped like a loop of rope, a carabiner clipped to the top, a detachable pouch that clips on with magnets, a pocket that appears only when a flap is turned inside out, a collar that rolls like a snail, a roll-top closure wound around a wooden dowel, buckles in the shape of animals, a decorative tail, ears that stick up, a mock zipper that opens nothing, a lens-like window on the front, a hinged lid like a treasure chest, a drawstring top pulled through brass eyelets, a snap-on cover, a shoulder cushion shaped like a pillow, shoulder straps that cross at the front like suspenders, a harness of wide webbing bands, a flexible spine of ribbed segments, a frame of bent tubes that shows through the skin, bumpy tactile panels, a pocket stuffed with colourful tassels, ornamental pompoms, a trim of long fringe, hanging strands of beads, rows of small mirrors sewn in, dangling charms and keychains, hand-painted panels, patchwork of old badges, a label-free tag, a stitched map, a printed constellation, a hand-lettered slogan, a wax-sealed flap, a lined interior with a bold pattern, a hidden compartment shaped like a heart")
STRAP_ODD = S("two wide webbing straps cross over the chest, a single braided rope strap loops across the body, straps made from sculpted leather ribbons, twin chain straps with padded cuffs, a harness of knotted rope, a harness of stretchy elastic bands, straps shaped like the curved arms of a cradle, a single padded sling, an adjustable bungee-cord harness, straps cut from the same material as the body and left unfinished at the ends, a pair of loops sewn from climbing slings, two short top handles and a hidden pair of straps")
PLACE_ODD = S("slouching softly, standing upright on its own, sitting high on the shoulders, hanging low at the hips, balanced at the center of the back, tilted slightly to one side, with its shape casting a strong shadow, with its surface catching the light, seen from the back, seen from the side, in a three-quarter view, resting on a plinth, resting on a table")
# extra design traditions: (name, palettes, motifs)
TRADS = [
 ("Dada collagist", ["black, cream and newspaper grey", "crimson, mustard and ink black", "pale blue, cream and rust"], ["cut-and-pasted print fragments", "mismatched letterforms", "torn-paper edges", "stitched collage of badges", "nonsense slogans", "photographic cut-outs"]),
 ("Bauhaus-trained designer", ["primary red, yellow and blue with black", "white, grey and black", "mustard, charcoal and cream"], ["circle, square and triangle forms", "bold geometric blocks", "grid lines", "diagonal stripes", "tubular steel hardware", "offset circles"]),
 ("deconstructivist architect", ["concrete grey, black and white", "steel blue and graphite", "raw leather brown and charcoal"], ["tilted planes", "exposed seams", "angled cut-outs", "collisions of volumes", "twisted facets", "visible inner framework"]),
 ("Arte Povera sculptor", ["raw canvas, rope brown and soot black", "earth brown, rust and chalk white", "faded blue, tarpaulin green and rope tan"], ["found-object attachments", "knotted rope", "salvaged hardware", "scrap fabric patches", "rough stitched seams", "bare-bones joinery"]),
 ("Memphis Group designer", ["pink, turquoise and yellow with black", "lilac, orange and teal", "bright red, mint and white"], ["squiggle patterns", "confetti terrazzo", "bold zigzags", "clashing checkerboards", "playful geometric appliqués", "laminate-like dots"]),
 ("kinetic sculptor", ["silver, white and signal red", "brass, black and cream", "chrome and deep blue"], ["small spinning parts", "hinged moving panels", "pendulum charms", "balanced mobiles", "rotating discs", "swaying hanging forms"]),
 ("origami engineer", ["white, pale grey and silver", "ivory and charcoal", "pale gold and cream"], ["tessellated folds", "pleated starbursts", "crisp diagonal creases", "collapsible geometric panels", "interlocking triangles", "box-pleated ridges"]),
 ("biomorphic designer", ["moss green, sand and bone white", "coral, ivory and sage", "deep teal and mushroom grey"], ["organic curves", "cell-like bubbles", "veined textures", "pod forms", "branching ribs", "bone-like struts"]),
 ("Brutalist architect", ["raw concrete grey and black", "pale stone and charcoal", "oxide red and slate"], ["board-formed ridges", "heavy slab shapes", "deep recessed pockets", "monolithic blocks", "rough textured faces", "bolted plate details"]),
 ("Surrealist painter", ["dusky pink, teal and deep violet", "sky blue, ochre and charcoal", "plum, gold and cream"], ["melting forms", "floating eyes", "impossible staircases", "dreamlike clouds", "keyholes in odd places", "hands emerging from the surface"]),
 ("Futurist", ["metallic silver, red and black", "bright orange and gunmetal", "cobalt and white"], ["speed lines", "overlapping dynamic shapes", "machine-age motifs", "slashing diagonals", "gear shapes", "fragmented motion"]),
 ("Constructivist designer", ["red, black and cream", "ochre, charcoal and white", "red and grey"], ["sharp diagonal bars", "bold sans lettering", "spiky geometric rays", "propaganda-style graphics", "pared-down blocks", "tightly arranged circles"]),
 ("solarpunk designer", ["leaf green, gold and sky blue", "terracotta, moss and cream", "sun yellow and fern green"], ["leaf-shaped panels", "built-in miniature solar cells", "woven plant fibres", "sprouting vine motifs", "recycled-material patchwork", "curving botanical lines"]),
 ("sculptural fashion house", ["jet black", "bone white and graphite", "oxblood and black"], ["architectural volumes", "a single dramatic curve", "extreme proportions", "folded planes", "gravity-defying shapes", "sleek monolithic forms"]),
 ("outsider-art maker", ["clashing brights with black outlines", "hand-mixed muddy colours", "primary colours and white"], ["naive hand-painted figures", "dense hand-drawn patterns", "uneven stitched lettering", "crowded mysterious scenes", "obsessive repeating marks", "painted faces"]),
 ("toy-maker turned bag designer", ["bright red, yellow and blue", "pink, mint and sky blue", "orange, teal and cream"], ["wind-up keys", "chunky button eyes", "pull-string tabs", "toy-block lettering", "bright clip-on figures", "friendly cartoon faces"]),
 ("naval-architect designer", ["navy, white and brass", "oyster grey and rope tan", "signal red and white"], ["rope rigging details", "porthole-like windows", "hull-like curves", "knotted sailor's lines", "brass cleats", "riveted plates"]),
 ("tactile textile artist", ["mixed natural dyes in madder, indigo and weld", "undyed wool, charcoal and cream", "rust, olive and cream"], ["dense woven relief", "thick tufted pile", "hand-knotted fringe", "felted ridges", "sculpted padding", "raised embroidered coils"]),
]

# ============================== utility / camping / hauling packs
UTIL_RAW = """internal-frame trekking pack|It is a tall, slim pack that hugs the spine, with a hidden frame, a padded hip belt and a top lid.
external-frame backpack|It is a bag mounted on an exposed rectangular tube frame, with a gap of air between the frame and the back.
external-frame hauling pack with a load shelf|It has a tubular frame with a bare shelf at the bottom for strapping on bulky loads.
frameless ultralight pack|It is a soft, slim, unstructured sack with thin straps and a roll-top.
hybrid frame pack|It is a pack with a short carbon rod frame hidden in the back panel and a removable aluminum stay.
expedition mountaineering pack|It is a huge, tall pack with ice-axe loops, crampon patches and a floating lid.
backpacking pack with a sleeping-bag compartment|It has a zipped lower compartment, a floating lid and side compression straps.
panel-loading trekking pack|It opens like a suitcase down the full length of the front.
top-loading rucksack|It is a deep sack closed by a drawcord collar and a buckled flap.
canvas rucksack with leather straps|It is a simple envelope of canvas with leather shoulder straps and brass buckles.
canoe portage pack|It is a nearly square, heavy canvas pack that sits low on the back, closed with straps and roller buckles.
Duluth pack|It is a big, flat-bottomed canvas sack with a long front flap, three leather straps and riveted leather patches.
tumpline pack|It has a wide leather strap that passes over the forehead to help carry the load.
pack basket|It is a rigid woven ash-splint basket on canvas shoulder straps, with a canvas cover and a rope tie.
wooden pack frame|It is a bent-wood frame with canvas webbing and long thongs for lashing on a bundle.
bundle pack|It is a canvas sheet wrapped around the load and held in a harness of straps.
Adirondack pack|It is a large canvas pack with a big flap and several outer pockets.
bushcraft haversack|It is a waxed-canvas satchel carried on a long cross-body strap with a big flap.
military rucksack|It is a large olive-patterned pack with huge outer pockets, a metal frame and webbing straps.
MOLLE assault pack|It is covered in rows of webbing loops for clipping on pouches.
tactical sling pack|It is a single-strap pack that rotates from back to chest.
bug-out bag|It is a bulky survival pack covered in clipped-on pouches and tools.
range pack|It is a boxy bag with many padded compartments and internal dividers.
hunting pack with a meat shelf|It is a camo pack with a frame, a hinged shelf and compression straps for hauling game.
fishing backpack|It has rod tube holders, tackle trays and a net holder on the side.
foraging backpack|It is a roomy open-top pack with mesh pockets and hooks for tools.
hydration vest pack|It is a minimal vest with a water bladder, front pockets and bungee on the back.
trail-running vest|It is a snug, stretchy vest pack with soft flasks on the chest.
climbing pack|It is a narrow, tall pack with no hip belt, a rope strap and gear loops.
ski mountaineering pack|It is a slim pack with A-frame ski carry straps, a helmet net and an ice-axe sleeve.
avalanche airbag pack|It has a folded airbag cell at the back, a pull handle on the shoulder strap and a deployment cylinder.
dry-bag backpack|It is a welded roll-top sack with a hard-wearing waterproof skin and simple harness straps.
kayak dry pack|It is a tall, bright waterproof sack with a roll-top closure and a cap on a lanyard.
rolling duffel backpack|It is a long duffel with hidden backpack straps and a hip belt.
duffel backpack|It is a large cylindrical bag with a zipper along the top and backpack straps that tuck into a panel.
expedition duffel with backpack straps|It is a huge, heavy-duty haul bag with grab handles, a wide D-shaped zip and shoulder straps.
sea bag backpack|It is a tall cylindrical canvas sack with a drawstring top and shoulder straps.
kit bag backpack|It is a long barrel-shaped bag with end panels, a long zip and padded straps.
climbing haul bag|It is a tough, abrasion-resistant cylinder with a PVC skin and heavy straps.
rope bag backpack|It is a round bag that opens flat into a rope tarp.
cooler backpack|It is an insulated roll-top pack with a hard liner.
picnic backpack|It has a built-in plate set, a blanket strap and a wine holder.
camera backpack|It is a padded pack with modular dividers and a side opening.
tool backpack|It is a heavy-duty pack with a rigid plastic base and many small tool pockets.
cargo hauler pack|It is a flat plywood-like board frame with a long tie-down cargo net.
beekeeper's backpack|It is a ventilated pack for smoker and hive tools.
musician's backpack|It is a padded pack shaped to hold an instrument.
hammock camping pack|It is a pack with built-in hammock straps and a rain fly pocket.
tent-pole backpack|It has long sleeves for tent poles down the sides.
weekender travel pack|It is a large clamshell with a wide opening and a hidden harness.
anti-theft urban pack|It is a smooth body with hidden zippers and slash-resistant panels.
bike-touring pack|It is a long pack with a rack-mounting plate, reflective strips and a rain flap.
messenger-backpack hybrid|It is a big flap bag with a quick-release buckle and a cross strap.
military duffel|It is a long, olive canvas cylinder with a top zipper and web handles.
fire-crew hauler|It is a heavy-duty pack with reflective bands and a fabric lid.
rescue medical pack|It is a modular pack with a dividing internal organizer and zippered, colour-coded pouches.
survey field pack|It is a pack with a clear map pocket, a tool loop and mesh pockets.
photo-trekking pack|It is a hybrid frame pack with a padded camera cube.
all-terrain mule pack|It is a wide, low panniered double bag slung over the back.
double-pannier backpack|It is two matching sacks joined by a yoke and carried across the back.
water-carrying pack|It is a pack with a large collapsible bladder and a drinking hose.
blanket-roll pack|It is a rolled blanket and gear held in a long cylinder with end straps.
portable workshop backpack|It is an open-frame pack that unfolds into a tabletop.""".strip().split('\n')
UTIL = [tuple(l.split('|')) for l in UTIL_RAW]

MAT_UTIL = {
 'low': S("polyester 600D fabric, polyester oxford cloth, nylon taffeta, cotton duck, coated polyester canvas, tarp-weight polyethylene, woven polypropylene, nylon pack cloth, plain canvas, vinyl-coated nylon, PU-coated polyester, light ripstop nylon"),
 'mid': S("500D Cordura nylon, 1000D Cordura nylon, ballistic nylon, ripstop nylon with silicone coating, PU-coated nylon, TPU-coated nylon, X-Pac laminate, waxed cotton canvas, 18-ounce heavy canvas, rubber-coated canvas, military-spec nylon, hemp canvas, oilcloth, tarpaulin vinyl, 840D ballistic nylon, gridstop nylon, Hypalon-trimmed pack cloth, heavy sailcloth, felted wool, cotton-nylon blend, bonded polyester"),
 'high': S("Dyneema composite fabric, ultra-high-molecular-weight polyethylene grid, 1680D ballistic nylon, hand-waxed heavy Scottish canvas, bonded Cordura with a full-grain leather bottom, titanium-reinforced pack cloth, vegetable-tanned harness leather, aerospace-grade carbon composite, laminated sailcloth, military-spec Kevlar-reinforced fabric, welded TPU, ash-splint basket weave, hand-bent hickory, hand-forged steel buckles on heavy canvas")}
CONS_UTIL = {
 'low': S("machine-stitched with single seams, sewn with a bartack at each stress point, glued and stitched, sewn with taped inside seams, machine-sewn from a few big panels, ultrasonically welded, sewn in a single envelope"),
 'mid': S("double-stitched and bar-tacked at every stress point, box-stitched at the strap anchors, seam-taped inside, riveted at the corners, stitched with bonded nylon thread, reinforced with triple stitching, welded at the seams and stitched at the straps, hand-finished with bartacks, rivet-reinforced at the straps"),
 'high': S("hand-finished with leather reinforcements at every wear point, made by a pack-maker in a small shop, stitched with heavy waxed thread, hand-riveted with copper rivets, hand-cut and hand-stitched in a single envelope, built on a hand-welded frame, sewn by a saddler, expedition-tested and built to the maker's own pattern")}
FRAME_ITEMS = S("a contoured aluminum perimeter frame, a rectangular welded aluminum tube frame, a pair of flexible carbon rods, a single curved aluminum stay, a sheet of high-density plastic framesheet, a bent-hickory pack frame, a hoop of titanium wire, a riveted aluminum frame, a molded plastic frame, a lightweight tubular alloy frame, a ladder-style steel frame with canvas webbing, an X-shaped crossed stay, a removable foam pad, a cantilevered carbon frame, a bent ash-wood frame with leather lacing")
FRAME_SUSP = S("with a padded hip belt, with a mesh back panel, with a taut mesh trampoline back, with a wide sternum strap, with load lifters, with a nylon back band, with a hinged shoulder yoke, with ventilated foam pads, with a foam back pad, with a leather-padded yoke, with an adjustable torso length, with a wide wool-padded shoulder strap, with sliding clevis pins, with a swing-away hip belt, with air channels behind the back, with a floating shelf, with webbing straps tied on, with a rolled-leather shoulder pad")
GEAR = S("a rolled sleeping pad, a sleeping bag in a stuff sack, a tent bundle, a pair of trekking poles, a camp stove, a dangling tin cooking pot, a coil of climbing rope, an ice axe, a pair of crampons, a folding saw, a hatchet in a leather sheath, a bedroll, a canvas tarp, a rolled foam mat, a water bottle, a pair of snowshoes, a folding camp chair, an enamel camp mug, a rain jacket, a lantern, a bear canister, a bundle of firewood, a fishing rod tube, a pair of skis, a helmet, a carabiner full of keys, a coiled hammock, a tent pole bundle, a camp shovel, a billy can, a folded map case, a bundle of rolled blankets, a first-aid kit, a thermos, a fuel canister, a headlamp, a tripod, a climbing harness, a bag of kindling, a wooden walking stick, a coil of paracord, a sealed dry bag, a hand axe, a folded canoe paddle, a roll of canvas, a lashed bedroll with a rope tie")
UTILFEAT = S("a floating lid with a zippered pocket, side compression straps with buckles, a front shove-it pocket, lash points along the front, daisy-chain webbing down the face, stretch mesh side pockets, ice-axe loops, a hipbelt with zippered pockets, load-lifter straps at the shoulders, a rain cover pocket in the base, a haul loop at the top, reflective tabs on the shoulder straps, a removable lid that converts to a hip pack, a zippered sleeping-bag compartment, a hydration sleeve and hose port, a wide sternum strap, a padded back panel with channels, a leather bottom that resists wear, riveted leather patches at the strap anchors, a long front flap with three leather straps, brass roller buckles, a rope handle at the top, a heavy-duty zip with a pull cord, a web grab handle at each end, a reinforced base plate, a wide D-shaped main zipper, tie-downs along the sides, a cargo net across the front, tool loops, a gear sling, slots for tent poles, a sternum whistle, MOLLE webbing across the front, drain eyelets in the base")

# ============================== colours (backpack only)
BASE = S("ultramarine, vermilion, chartreuse, mauve, oxblood, ochre, teal, cerulean, saffron, aubergine, sage, terracotta, cobalt, magenta, olive, burgundy, tangerine, periwinkle, emerald, coral, indigo, mustard, lilac, maroon, turquoise, rust, fuchsia, khaki, navy, peach, crimson, jade, amber, plum, slate, scarlet, sand, cyan, rose, lime, charcoal, ivory, bronze, copper, gold, silver, pewter, gunmetal, chrome, pearl, cream, bone, ecru, taupe, mocha, chestnut, russet, sienna, umber, sepia, caramel, honey, butter yellow, lemon, canary, marigold, pumpkin, apricot, salmon, blush, dusty rose, raspberry, cherry red, brick red, wine, mulberry, orchid, violet, lavender, amethyst, grape, midnight blue, royal blue, sky blue, powder blue, denim blue, steel blue, petrol blue, peacock blue, aqua, seafoam, mint, pistachio, moss green, forest green, fern green, hunter green, bottle green, army green, khaki green, lichen, celadon, verdigris, pine, kelly green, avocado, wheat, flax, linen, oatmeal, stone, ash grey, dove grey, cement grey, graphite, soot black, jet black, matte black, off-white, chalk white, snow white, fluorescent orange, hot pink, electric blue, acid yellow, neon green, neon pink, signal red, safety orange, hi-vis yellow, holographic silver, iridescent teal, oil-slick purple, mirrored chrome, opal white, rose gold, brass, tarnished copper, patinated bronze, camouflage green, desert tan, coyote brown, multicam olive, ranger green, foliage grey, sunset orange, dusk purple, glacier blue, lagoon green, lava red, sunflower yellow, cornflower blue, bubblegum pink, tomato red, paprika, cinnamon, cocoa, espresso, walnut brown, tan, buff, fawn, biscuit, almond, parchment, mushroom, driftwood grey, fog, mist, storm grey, thunder, ink, onyx, obsidian, ebony, raven, coal, cadet blue, prussian blue, lapis, sapphire, azure, turquoise blue, cyan blue, ice blue, baby blue, blueberry, lilac grey, heather, thistle, wisteria, mauve pink, rosewood, garnet, ruby, carmine, cardinal red, poppy red, flame orange, ember, rust orange, copper orange, honey gold, mustard gold, olive gold, lime green, apple green, spring green, jungle green, malachite, spruce, juniper, eucalyptus, artichoke, matcha, wasabi, cactus green, algae green, kelp, deep sea blue, abyss, tidal teal, coastal blue, seaglass, pebble, sandstone, clay, adobe, paprika red, ox-blood leather brown, saddle tan, bridle brown, cognac, whisky, tobacco, chestnut brown")
MODC = S("pale, deep, dusty, neon, muted, burnt, faded, electric, acid, smoky, washed, inky, bright, soft, rich, vivid, dark, light, warm, cool, milky, glossy, matte, sun-bleached, weathered, saturated")
PATC = ["{a}", "{a} and {b}", "{a}, {b} and {c}", "{a} with {b} accents", "{a} with {b} piping", "{a} fading into {b}", "{a} on {b}", "{a} colour-blocked with {b}", "speckled {a} over {b}", "{a} with {b} stripes", "{a} marbled with {b}", "mottled {a} and {b}", "{a} dip-dyed to {b}", "{a} with a {b} lining and {c} hardware", "{a} panels trimmed in {b}", "{a} with {b} stitching", "{a} and {b} in a patchwork", "{a} with {b} polka dots", "{a} with {b} zippers", "{a}, with {b} straps and {c} buckles", "{a} base with a {b} flap", "{a} with a {b} ombré", "tie-dyed {a} and {b}", "{a} with {b} and {c} stripes", "{a} with {b} webbing", "{a} checked with {b}", "gradient from {a} to {b}", "{a} with {b} reflective trim"]
