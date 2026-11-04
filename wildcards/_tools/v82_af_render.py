# v82 art-form data: 3D render looks, stop-motion, toys, installation, ephemeral forms.
# FORMS[key] = (noun, subjects, materials, techniques, finishes, colours, scales, wear)
# Every list is one string of items separated by semicolons.

FORMS = {
'clay_render': ('clay render',
 'a small fox sitting by a lantern; a stone cottage with a crooked chimney; a bust of a bearded old sailor; a sleeping cat on a cushion; a cluster of round mushrooms; a woman reading in an armchair; a heron standing in shallow water; a tiny lighthouse on a rock',
 'a matte white clay shader on a smooth model; plain pale grey digital plaster; a uniform off-white material with no textures; a soft chalky white surface on a sculpted mesh; a single untextured light grey shader; a bone-white matte material over a detailed model; a smooth porcelain-white matte shader; a flat powder-white material on rounded forms',
 'rendering with soft global illumination; rendering with gentle ambient occlusion in the creases; lighting with one large soft source; rendering with a single overcast-style dome light; shading with smooth contact shadows; sculpting a digital model and rendering it without textures; rendering with a shallow depth of field; baking soft shadow into every corner',
 'a perfectly even matte finish; soft shadows pooling in the creases; rounded bevels on every edge; no gloss at all; smooth gradual tonal shading; faint grey darkening where forms meet; clean unbroken curves; a velvety plaster-like softness',
 'warm white and pale grey; cool white and soft grey; bone white and light taupe; chalk white with faint blue shadows; cream and pale grey; pure white and mid grey; off-white with warm grey shade; ivory and silver grey',
 'a tiny; a small; a palm-sized; a desk-sized; a miniature; a monument-sized; a room-sized; a hand-sized',
 'freshly rendered and spotless; clean and untouched; slightly grainy from noise; perfectly smooth and new; faintly banded in the shadows; crisp and unmarked; softly lit and pristine; plain and unfinished'),

'photoreal_product_render': ('product render',
 'a glass perfume bottle with a metal cap; a pair of wireless headphones; a running shoe floating in mid-air; a wristwatch with a steel strap; a lipstick tube standing upright; a ceramic coffee cup with steam; a compact camera on a plinth; a bottle of olive oil with a dark label',
 'polished steel and clear glass; matte black plastic with a metal trim; brushed aluminium and rubber; frosted glass with a gold-tone cap; glossy ceramic with a satin base; soft-touch plastic and chrome; anodised coloured metal; smooth leather and stitched fabric',
 'rendering with physically based materials; tracing light paths for sharp reflections; lighting with large studio softboxes; rendering with an environment of bright reflections; polishing every edge with a thin highlight; rendering with a gradient studio backdrop; compositing a soft floor reflection; rendering with crisp depth of field',
 'crisp bright specular highlights; thin bevelled edges catching a rim light; spotless reflective surfaces; clean glossy reflections of softboxes; no dust or fingerprints; subtle light bloom on the brightest edges; a smooth satin metal grain; sharp clean seams between parts',
 'neutral grey and silver; black and brushed steel; white and soft gold; deep blue and chrome; warm copper and cream; pale pink and white; graphite and orange accent; clear glass and amber',
 'a small; a palm-sized; a tabletop; a life-sized; an enlarged; a tiny; a floating; a hand-held',
 'flawlessly clean; brand new; unnaturally perfect; spotless and polished; freshly rendered; pristine; box-fresh; immaculate'),

'low_poly_render': ('low-poly render',
 'a snow-capped mountain range; a stag standing on a hill; a small island with a few trees; a fox curled up asleep; a sailing boat on a calm sea; a bear walking through pines; a lone cabin by a lake; a whale surfacing near rocks',
 'a mesh of flat triangular facets; a few hundred flat-shaded polygons; a crystal-like faceted surface; a simple geometric mesh with no textures; faceted shapes in a gradient palette; angular polygons with one tone each; a coarse mesh of flat coloured planes; hard-edged triangles',
 'rendering with flat shading; building shapes from a few connected points; lighting with one simple directional light; colouring each facet by its angle; rendering with a smooth sky gradient behind; reducing a form to a minimal mesh; shading faces without smoothing; rendering with soft ambient light',
 'sharp visible facet edges; each face a single flat tone; no texture or noise; crisp angular silhouettes; a crystalline cut-gem look; slight tonal steps between neighbouring faces; hard edges with no smoothing; a clean paper-model look',
 'sunset orange and violet; teal and soft pink; mint green and cream; deep blue and coral; pale peach and lilac; forest green and gold; slate grey and sky blue; warm yellow and rose',
 'a tiny; a small; a miniature; a landscape-sized; a floating; a desk-sized; a vast; a pocket-sized',
 'freshly made; clean and sharp; unmarked; crisp and new; untouched; neat and flawless; newly rendered; perfectly tidy'),

'voxel_art': ('voxel scene',
 'a tiny cottage with a red roof; a knight standing beside a castle gate; a small dragon on a hill; a fishing boat at a pier; a row of market stalls; a lone tree beside a pond; a fox in a snowy field; a bridge over a river of blue cubes',
 'small coloured cubes stacked on a grid; blocks of solid colour; a lattice of tiny cubes; cube-shaped volume pixels; stepped blocks in a limited palette; hundreds of tiny square-faced blocks; layered slices of coloured cubes; chunky blocks with flat faces',
 'placing cubes one at a time; building up layers slice by slice; stacking blocks on a regular grid; rendering with soft shadow between blocks; colouring each cube separately; lighting with a gentle top-down sun; rendering with a slight ambient glow; arranging blocks in an angled view',
 'hard square edges on every form; stair-stepped curves; flat colour on each cube face; a slight shade difference between block faces; no smooth gradients; visible grid lines between blocks; crisp cubic silhouettes; matte block faces',
 'bright primary colours; soft pastel greens and blues; earthy browns and leaf green; sunset orange and purple; sky blue and white; muted teal and rust; candy pink and mint; night blue and yellow',
 'a tiny; a small; a miniature; a floating; a desk-sized; a vast; a chunky; a pocket-sized',
 'freshly built; neat and tidy; crisp and new; unmarked; cleanly assembled; sharp-edged; newly placed; pristine'),

'isometric_diorama': ('isometric diorama',
 'a cosy attic room with a desk and lamp; a small farm with a windmill; a tiny coffee shop interior; a floating island with a cabin; a workshop with a bench and tools; a lighthouse keeper cottage; a sleepy library corner; a tiny train station platform',
 'smooth matte surfaces on rounded blocks; a cut-away room on a floating slab; satin plastic-like surfaces; soft clay-like walls and furniture; small modelled props on a square base; painted wood-look surfaces; a miniature room in a cube; warm glowing windows set in soft walls',
 'viewing from a fixed corner angle; rendering with parallel projection; lighting with soft baked shadows; placing props on a tile grid; rendering with warm lamp glow; cutting away two walls to show the inside; using a high three-quarter camera; rendering with gentle ambient occlusion',
 'soft rounded bevels on every edge; smooth satin surfaces; gentle contact shadows; cleanly lit small props; a toy-like finish; sharp even outlines of the base; faint glow from lamps; no visible seams on the walls',
 'warm pastel peach and cream; soft teal and orange; cosy brown and yellow; mint green and pink; dusk blue and amber; sage green and white; lavender and gold; rust and cream',
 'a tiny; a small; a miniature; a floating; a toy-sized; a cube-shaped; a compact; a pocket-sized',
 'freshly made; clean and cosy; untouched; neat and bright; lightly lived in; spotless; tidy; newly furnished'),

'wireframe_render': ('wireframe render',
 'a sphere made of grid lines; a car body as a see-through skeleton; a mountain terrain as a line grid; a human head as a mesh of lines; a cube with every edge drawn; a bird with an open mesh body; a city block as outlined boxes; a spiral staircase in thin lines',
 'thin glowing lines on a dark background; edges drawn between corner points; a see-through mesh of fine lines; white lines on deep blue; green lines on black; a network of crossing edges; outlined polygons with no fill; a lattice of thin coloured lines',
 'drawing only the edges of a model; showing every polygon outline; rendering with hidden lines visible; plotting vertices joined by straight lines; displaying a mesh without surfaces; overlaying lines on a solid shape; projecting a grid over a form; rendering a skeleton of the geometry',
 'crisp thin lines with no fill; tiny bright dots where lines meet; a see-through hollow look; fine dense crossing lines; a slight glow around each line; clean sharp vertices; lines that thicken in the foreground; an empty transparent interior',
 'cyan on black; white on deep blue; green on black; orange on dark grey; magenta on navy; pale blue on charcoal; yellow on dark brown; silver on midnight blue',
 'a tiny; a small; a vast; a floating; a desk-sized; a monumental; a compact; a wide',
 'freshly generated; crisp and clean; perfectly sharp; unmarked; newly plotted; clean and exact; faintly glowing; precise'),

'toon_shaded_render': ('toon-shaded render',
 'a young woman in a long coat holding an umbrella; a cheerful fox in a scarf; a swordsman standing on a rooftop; a cat sitting on a window ledge; a sailor leaning on a ship rail; a robot gardener among flowers; a baker holding a tray of bread; a wolf howling on a cliff',
 'flat bands of colour on a 3D model; hard-edged tones with black ink contours; a model shaded in two or three steps; painted-look colour blocks; a character with cartoon-style shadows; a smooth mesh with an outline; a hand-drawn look over a solid form; solid colour areas with crisp shade edges',
 'reducing lighting to a few flat tones; drawing a black outline around the silhouette; rendering with hard shadow steps; adding a faint paper-like texture; placing a bright rim light on one side; using edge lines for interior details; keeping highlights as flat white shapes; shading in clean bands',
 'a thick black ink outline; flat colour with no gradients; hard-edged shadow shapes; small white highlight shapes; a faint printed paper grain; crisp clean colour boundaries; thin interior contour lines; a glossy highlight stamped as a flat shape',
 'bold primary colours with black outline; warm orange and teal; pastel pink and sky blue; deep red and cream; forest green and gold; purple and yellow; navy and white; sunny yellow and red',
 'a small; a life-sized; a tiny; a wide; a close-up; a large; a character-sized; a poster-sized',
 'freshly rendered; sharp and clean; bright and new; unmarked; crisp-edged; vivid; neatly inked; spotless'),

'soft_translucent_render': ('soft translucent render',
 'a plump jelly creature with round ears; a glowing wax candle shaped like a bear; a smooth rounded ghost with a soft smile; a single peach on a cloth; a cluster of pink blobs; a small seal made of soft wax; a hand holding a glowing orb; a sleeping bunny made of soft rubbery material',
 'a waxy semi-translucent material; soft jelly-like rubber; a skin-like soft shader; pale glowing silicone; translucent pastel gel; a milky soft plastic; a marshmallow-like surface; soft warm-glowing wax',
 'rendering with light scattering inside the surface; backlighting thin parts so they glow; blurring the lighting across the surface; rendering with a soft rim light; lighting from behind and above; rendering with a very soft shadow edge; adding a faint inner glow; shading with smooth gradients',
 'a soft inner glow on thin edges; thicker areas darker and denser; no hard plastic gloss; very soft shadow edges; a warm reddish tint where light passes through; a smooth velvety shine; tiny soft highlights; a dewy slightly moist look',
 'peach pink and cream; soft coral and ivory; pale mint and white; blush and warm orange; lilac and pale yellow; baby blue and white; warm red glow on cream; apricot and pearl',
 'a tiny; a small; a palm-sized; a plump; a desk-sized; a macro-sized; a hand-sized; a pocket-sized',
 'freshly made; soft and new; gently glowing; unblemished; plump and smooth; warm and fresh; pristine; newly poured'),

'glass_chrome_render': ('glass and chrome render',
 'a floating liquid-metal blob; a twisted ribbon of chrome; a cluster of glass spheres; a glass ring on a mirrored floor; a knotted tube of clear glass; a chrome torus hovering over water; a stack of translucent glass cubes; a pool of silver liquid with ripples',
 'polished chrome that mirrors the room; clear glass with strong refraction; liquid silver metal; tinted glass with bright edges; mirror metal and frosted glass; iridescent glass film; thick transparent resin; reflective metal with a rainbow tint',
 'tracing rays for true reflections; bending light through thick glass; rendering bright caustic patterns; lighting with large softbox reflections; rendering with a gradient environment; adding fringed colour at the edges; reflecting a checker floor in the shapes; using a smooth studio gradient',
 'mirror-sharp reflections of the surroundings; bright pools of focused light beneath the glass; rainbow fringing at the edges; sharp highlights on curved forms; perfectly smooth unbroken surfaces; bent distorted views through the glass; soft light bloom on bright points; glossy reflections without any dust',
 'silver and pale blue; pink and violet gradient; chrome and teal; clear glass with a warm gold edge; iridescent pastels; black chrome and white; aqua and pearl; orange glow in silver',
 'a tiny; a floating; a small; a giant; an abstract; a monumental; a hand-sized; a desk-sized',
 'flawlessly clean; spotless; freshly rendered; unmarked; pristine; flawless and shining; perfectly polished; box-fresh'),

'claymation_scene': ('claymation scene',
 'a round-faced baker kneading dough; a sheep wearing a woolly scarf; a dog in a flat cap beside a toy train; a pair of ducks on a pond; a grumpy penguin on an ice block; a fisherman with a big nose in a rowing boat; a cat chasing a ball of yarn; a tired old inventor in a workshop',
 'coloured plasticine on a wire frame; soft oil-based modelling clay; clay layered over a bendable armature; blended marbled clay colours; small clay pieces pressed together; clay with glass bead eyes; modelling clay on a painted miniature set; soft clay and fine wire',
 'shaping by thumb and moving a frame at a time; pressing clay with fingers between shots; sculpting small changes in each photograph; moving a figure a tiny amount per frame; filming with a locked camera; shooting under steady warm lamps; adding replacement mouths for each sound; smoothing with a small tool',
 'fine thumbprints and soft edges; visible fingerprint ridges; faint seams where clay pieces join; a slightly lumpy hand-made surface; small smudges and dents; a soft satin sheen on the clay; slightly wobbly outlines; tiny hairs and dust specks stuck in the clay',
 'warm earthy browns and yellows; bright primary colours; soft green and cream; marbled orange and red; muted blue and grey; pink and pale yellow; deep red and olive; sky blue and white',
 'a tiny; a hand-sized; a small; a miniature; a tabletop; a palm-sized; a finger-high; a desk-sized',
 'slightly squashed; freshly made; a little smudged; dusty at the edges; sagging under the lamps; fingerprinted all over; half melted at the edges; softly worn'),

'felt_puppet_scene': ('felt puppet scene',
 'a woolly sheep in a tiny knitted jumper; a bear in a patched coat; a fox sitting in a cardboard forest; a rabbit holding a lantern; a hedgehog beside a button-sized mushroom; an old woman with yarn hair knitting; an owl on a branch of twisted wire; a mouse in a matchbox bed',
 'felt and fabric over a wire frame; knitted wool stretched on a jointed armature; stitched cloth with bead eyes; fuzzy wool fibre on a ball-and-socket frame; patchwork scraps and thread; soft latex skin under felt clothing; fine wire and padded cloth; painted card scenery with fabric props',
 'posing by hand a little for every frame; stitching tiny seams; filming one frame at a time; bending wire joints between shots; lighting with small warm lamps; replacing faces for each expression; setting up miniature scenery; shooting at a very low angle',
 'visible woven fibres; small stitches and seams; fuzz catching the light; slightly uneven hand-sewn edges; loose threads at the cuffs; a soft matte cloth surface; tiny fibres standing up on the edge; faint creases where the wire bends',
 'earthy brown and moss green; faded red and cream; mustard yellow and grey; muted blue and ochre; warm orange and olive; soft pink and brown; dusty teal and rust; cream and charcoal',
 'a tiny; a small; a hand-sized; a miniature; a finger-high; a tabletop; a palm-sized; a fist-sized',
 'slightly fuzzy; worn at the seams; a little frayed; dusty; softly faded; well handled; freshly sewn; threadbare at the edges'),

'brick_build': ('interlocking plastic brick build',
 'a tall castle with small flags; a spaceship with a clear canopy; a red sports car; a small harbour with boats; a dinosaur skeleton; a market street with shopfronts; a windmill on a green base; a lighthouse on a rocky base',
 'interlocking plastic bricks; glossy moulded plastic blocks in many colours; hundreds of small studded bricks; smooth plastic plates and slopes; clear plastic pieces with coloured bricks; hard plastic bricks on a flat baseplate; stacked rectangular plastic blocks; small round plastic tiles and bricks',
 'stacking bricks in rows; clicking studs into hollow undersides; building up layers of blocks; staggering bricks to hide seams; placing small round tiles on top; building on a flat baseplate; mixing slopes and plates for detail; photographing against a plain background',
 'round studs on every top surface; thin visible lines between bricks; a smooth glossy plastic shine; sharp moulded edges; small scratches on the plastic; stepped blocky curves; tiny printed details on tiles; slight colour differences between bricks',
 'bright red, blue and yellow; white and grey; green and tan; black and orange; sand colour and dark brown; clear and bright blue; lime green and white; red and white',
 'a small; a palm-sized; a desk-sized; a tabletop; a room-sized; a huge; a miniature; a life-sized',
 'freshly built; a little scuffed; slightly dusty; well played with; clean and shiny; faintly yellowed on the white bricks; neat and new; loosely joined'),

'vinyl_toy': ('vinyl designer toy',
 'a chubby rabbit with long ears; a round-headed bear with stitched eyes; a skull-faced monkey in a hoodie; a sleepy cat with tiny paws; a fat little monster with three eyes; a grinning dog wearing a cape; a smooth egg-shaped creature with stubby legs; a masked wrestler with a round body',
 'smooth moulded vinyl; hard glossy plastic; soft hollow vinyl painted by hand; clear translucent vinyl; cast resin with a painted finish; vinyl with a metallic flake coat; matte vinyl with printed details; a plain blank vinyl body',
 'moulding in plastic and painting by hand; spraying flat colour in layers; adding fine painted details with a small brush; casting in a mould; assembling jointed arms and legs; printing small patterns on the surface; packaging in a window box; posing on a shelf',
 'a smooth satin sheen; tidy seams at the limbs; glossy painted eyes; small crisp painted lines; flat even paint; light paint rub on the edges; subtle mould lines; a clean glossy highlight on the head',
 'flat pastel pink and mint; bold black and white; bright orange and teal; sky blue and yellow; matte grey and red; purple and lime; cream and brown; clear with a coloured tint',
 'a small; a palm-sized; a tiny; a shelf-sized; a hand-sized; a large; a pocket-sized; a desk-sized',
 'freshly unboxed; a little dusty; slightly scuffed at the edges; shiny and new; rubbed at the nose; boxed and mint; faintly yellowed; lightly handled'),

'resin_figurine': ('resin figurine',
 'a swordswoman in flowing armour; a dragon coiled on a rock; a wizard with a long staff; a fox spirit with nine tails; a knight kneeling beside a horse; a mermaid-like sea creature on a wave; a lady in a long kimono-style robe; a warrior standing on a ruined stone base',
 'cast polyurethane resin; hard rigid resin parts glued together; hand-painted resin on a round base; smooth resin with airbrushed colour; pale resin primed in grey; resin with a clear coat; resin parts with metal-effect paint; hard resin with a wooden plinth',
 'airbrushing smooth colour gradients; gluing separate cast parts; filling and sanding the seams; painting fine details with a small brush; priming in flat grey; adding a satin clear coat; mounting on a display base; casting in a flexible mould',
 'crisp sculpted detail; hairline seams where parts join; a smooth airbrushed gradient; a matte primer-like finish on bare parts; a glossy clear coat on the armour; tiny painted highlights; a hard waxy sheen; small flecks of metal-effect paint',
 'deep blue and silver; crimson and gold; forest green and bronze; white and pale pink; black and purple; teal and pearl; copper and cream; grey and orange',
 'a small; a palm-sized; a desk-sized; a tabletop; a large; a hand-sized; a shelf-sized; a miniature',
 'freshly painted; spotless; slightly chipped at the edges; dusty on the shelf; a little yellowed at the glued seams; neat and glossy; unpainted and plain; lightly handled'),

'action_figure': ('action figure',
 'a muscular hero in a long cape; a masked soldier with a rifle; a monster with a spiked back; a robot warrior with sharp armour; a cowboy with a pair of pistols; a knight with a shield; a space explorer in a bulky suit; a martial artist in a loose robe',
 'hard moulded plastic; glossy plastic with painted details; plastic limbs on jointed pegs; soft plastic cloth-like parts; hard plastic with sprayed paint; plastic with small metal-look accents; rubbery plastic with moulded muscles; plastic with a clear display stand',
 'moulding in plastic and painting by hand; spraying paint through small masks; joining limbs with rotating joints; adding small accessories to the hands; packing in a card and bubble case; posing against a coloured backdrop; adding printed logos in simple shapes; sculpting exaggerated muscle forms',
 'visible joint seams at the elbows and knees; glossy moulded muscles; small paint overspray at the edges; sharp moulded details; a slightly waxy plastic shine; scuffed paint on the corners; tiny fine lines from the mould; matte painted costume parts',
 'bold red and blue; black and gold; olive green and tan; silver and orange; purple and green; white and red; dark grey and yellow; bright teal and black',
 'a small; a palm-sized; a hand-sized; a large; a collector-sized; a tiny; a boxed; a desk-sized',
 'freshly unboxed; a little scuffed; slightly loose at the joints; well played with; mint in the box; faintly yellowed; paint rubbed at the edges; clean and glossy'),

'neon_sign': ('neon tube sign',
 'a script word glowing on a wall; a glowing arrow pointing down; a cocktail glass outline; a heart with a lightning bolt; a palm tree and sun; a running horse in a single line; a crescent moon and star; a pair of lips outlined in pink',
 'bent glass tubes filled with glowing gas; hand-bent glass tube in one continuous line; thin glass tubing on a black backing panel; bright tubes with small metal clips; glass tube with painted black blocking; coloured glass tubes mounted on clear standoffs; looping tube with electrode caps at the ends; tubes wired to a hidden transformer',
 'bending hot glass by hand; filling tubes with low-pressure gas; running high voltage through the tube; mounting on a dark panel; tracing a drawn pattern while bending; blocking out connecting lines with black paint; switching sections on in turn; fixing the tube on small standoffs',
 'a smooth continuous glowing line; a soft halo of light bloom around the tube; a slightly brighter glow at each bend; thin wires and clips visible at the back; a faint buzzing flicker; dark unlit ends near the electrodes; a hard glassy highlight on the tube; coloured light spilling on the wall',
 'hot pink; electric blue; red-orange; warm white; green; violet; amber yellow; cyan',
 'a small; a window-sized; a wall-sized; a tiny; a large; a shop-front; a table-top; a huge',
 'freshly lit; flickering; partly dark with dead sections; dusty and faded; buzzing and bright; newly made; slightly dim at one end; weathered by rain'),

'led_installation': ('LED light installation',
 'a ceiling of hanging glowing rods; a tunnel of coloured light bars; a wall of tiny pixels that change colour; a forest of glowing poles; a curtain of hanging light strands; a floor of glowing tiles; a ring of light floating above a plaza; a grid of glowing cubes',
 'thousands of tiny LEDs; light strips behind frosted panels; glowing tubes of diffused light; hanging strands of small lights; light bars mounted in a grid; panels of soft white diffusing plastic; coloured light points on thin cables; mirrored boxes with glowing points',
 'programming slow colour changes; arranging lights in a regular grid; hiding the LEDs behind diffusers; hanging strands from the ceiling; running waves of colour along the rods; lighting a dark room with coloured points; syncing colours across the whole room; mounting rods in rows',
 'tiny bright dots of light; smooth soft colour washes; a faint haze around each light; visible thin cables; sharp edges on the light bars; coloured light on the floor; slight colour banding across the panels; a soft glow on the viewers',
 'saturated red, green and blue; slow shifting magenta and cyan; warm white and amber; deep violet and pink; cool white and pale blue; lime and teal; orange and purple; pure white',
 'a room-sized; a hall-sized; a wall-sized; a building-sized; a corridor-long; a tiny; a plaza-sized; a ceiling-sized',
 'freshly lit; shining brightly; a little uneven in colour; with a few dead pixels; dim at the edges; newly installed; slowly pulsing; dusty and dull'),

'projection_mapping': ('projection-mapped facade',
 'a stone cathedral that seems to crumble; a tall tower covered in moving patterns; a town hall with flowing water; a bridge that seems to bend; a building with windows that open and close; a palace wall full of flowers; a glass tower with rippling lines; a museum with falling gold dust',
 'light projected onto stone walls; moving images fitted to windows and cornices; bright video on a dark facade; stitched images from many projectors; patterns following the building edges; coloured beams on old masonry; mapped light on a curved dome; animated textures on a tall wall',
 'masking video to the building outline; blending many projectors into one image; aligning light to every window; animating fake cracks and shadows; making flat walls seem to move in depth; projecting at night in the dark; following the stone edges exactly; mapping colour onto the carved details',
 'sharp edges where light meets the architecture; the stone texture showing through the light; bright saturated colour on a dark building; faint seams between projectors; fake depth that looks real; a slight haze around the beams; light that stops exactly at the window frames; shimmering moving patterns',
 'electric blue and gold; deep red and white; green and violet; orange and black; cyan and magenta; warm gold and cream; silver and navy; vivid rainbow colours',
 'a building-sized; a tower-sized; a street-wide; a huge; a palace-sized; a wall-sized; a monumental; a plaza-sized',
 'freshly lit; shimmering; slightly misaligned; bright against the night; washed out at the edges; newly mapped; flickering softly; faded by street lamps'),

'infinity_mirror_room': ('infinity mirror room',
 'a field of glowing lanterns in endless space; a room full of round glowing pumpkins; a scatter of coloured lights hanging at different heights; a floor of shallow water and floating lights; a space of glowing dots that never ends; a single glowing sphere repeated forever; a woman standing on a small platform among lights; a ceiling of tiny stars',
 'mirrored glass walls on every side; many small lights hung on thin wires; mirror panels and glowing balls; a dark cube lined with mirrors; glowing spheres with a mirrored floor; polka-dotted forms in a mirrored room; shallow water on a dark floor; coloured bulbs reflected in mirrors',
 'repeating reflections in facing mirrors; hanging lights at different heights; dimming the room to near dark; placing a small platform in the centre; changing the lights in slow cycles; lining every wall with mirrors; limiting the visitors to a few at a time; adding a thin film of water on the floor',
 'sharp mirror reflections; endless repeated points of light; tiny fingerprints on the glass; soft glowing halos around each light; a dark space with no horizon; a slight blur on the far reflections; a gleam on the water; bright colour on a black background',
 'warm gold and black; pink and violet; orange and deep blue; white and black; green and yellow; red dots on black; cool blue and silver; multicoloured lights on black',
 'a room-sized; a cube-shaped; a small; a cabin-sized; a tiny; a boundless; a closet-sized; a gallery-sized',
 'freshly lit; shining; a little smudged on the mirrors; spotless; softly glowing; newly installed; dusty on the glass; flickering gently'),

'sand_mandala': ('sand mandala',
 'a circular palace pattern with four gates; a lotus flower with many petals; concentric rings of small symbols; a square temple plan inside a circle; a sun-like pattern of radiating lines; a wheel with eight spokes; a border of tiny flames; a centre star surrounded by gates',
 'fine coloured sand grains; crushed and dyed stone powder; white, yellow, red and blue sand; thousands of tiny grains placed by hand; sand poured through small metal funnels; coloured powder on a flat table; ground stone in bright dyes; layers of fine sand in sharp lines',
 'pouring sand from narrow metal funnels; scraping the funnel to release a thin trickle; drawing the outline first in chalk; working from the centre outward; filling each section with colour; using a small team around the table; tapping with a rod to shake out the sand; sweeping the design away at the end',
 'razor-sharp lines of sand; a fine matte powdery surface; perfectly even grains; tiny symmetrical details; crisp edges between colours; a faint dusting around the edges; no gloss at all; delicate raised lines',
 'bright red and yellow; deep blue and white; green and orange; black and gold; pink and purple; turquoise and red; white and saffron; five bright colours on white',
 'a table-sized; a floor-sized; a small; a large; a disc-shaped; a round; a gallery-sized; a tiny',
 'freshly finished; perfect and untouched; half swept away; partly scattered; dusty at the edges; newly laid; smudged in one corner; being swept into a heap'),

'chalk_pavement_art': ('chalk pavement illusion',
 'a deep canyon opening in the street; a giant waterfall pouring across the pavement; a floating bridge over a pit; a huge dragon rising from a crack; a ship sailing on a flooded plaza; a ring of stone steps going down into a hole; a tall cliff with a river below; a sea creature rising from a manhole',
 'coloured chalk on grey pavement; soft pastel dust pressed into stone; chalk and pastel blended by hand; powdery colour on paving slabs; blended soft chalk with sharp edges; coloured chalk over a grid of guidelines; pastel on asphalt; chalk dust rubbed into a rough floor',
 'drawing on a stretched grid; seeing the image from one fixed viewpoint; blending colours with the fingers; stretching the picture along the ground; shading deep shadows to fake depth; marking guide lines before drawing; working on hands and knees; finishing a picture over several days',
 'soft powdery colour; blended gradients with sharp edges; stone texture showing through the chalk; deep dark shadows for depth; bright highlights on the edges; a slightly smudged finish; fine chalk dust around the picture; stretched shapes that only look right from one place',
 'bright blue and turquoise; earthy brown and orange; green and gold; red and cream; grey stone and white; purple and pink; deep black and yellow; sky blue and white',
 'a street-wide; a pavement-sized; a huge; a plaza-sized; a large; a floor-sized; a house-sized; a doorway-sized',
 'freshly drawn; smudged by footprints; half washed away; faded by sun; dusty at the edges; streaked by rain; scuffed by passing feet; bright and new'),

'ice_sculpture': ('ice sculpture',
 'a swan with arched wings; a tall tower with arched windows; a bar counter carved from clear blocks; a leaping horse; a castle with tiny turrets; a pair of tall glasses; a spiral column; a lantern with a candle inside',
 'clear blocks of frozen water; cloudy white ice with trapped air; glassy ice cut from a frozen river; ice with a coloured tint; stacked blocks of ice and packed snow; ice lit by coloured gels; frozen water in carved moulds; thick slabs of clear ice',
 'carving with chisels and saws; cutting large blocks with a chainsaw; polishing the surface with a torch; lighting from below with coloured lamps; stacking blocks to make walls; freezing water slowly to keep it clear; carving fine detail with a small blade; keeping pieces cold with dry ice',
 'glass-clear smooth surfaces; sharp cut edges that catch the light; frosted white areas from cutting; beads of water running down; trapped air bubbles inside; glowing edges in coloured light; thin dripping icicles; a wet shine on every surface',
 'icy clear and pale blue; white and silver; clear with magenta light; clear with green light; frosty white and deep blue; clear with warm amber light; pale cyan and white; violet and clear',
 'a table-sized; a human-sized; a building-sized; a huge; a small; a tower-sized; a room-sized; a tiny',
 'freshly carved; dripping; softened and half melted at the edges; frosted over; melting into a puddle; clear and sharp; cracked in places; sagging in the warmth'),
'sugar_sculpture': ('sugar sculpture',
 'a swan with ruffled wings; a spray of long-stemmed roses; a basket woven from sugar strands; a tall ribbon bow; a bird perched on a branch; a delicate lace fan; a pair of leaping fish; a nest of fine spun threads',
 'pulled sugar with a high gloss; blown sugar shaped like a balloon; spun sugar threads; cast sugar poured into a mould; hard boiled sugar in thin sheets; sugar paste dried to a hard shell; coloured sugar syrup cooled to glass; thin ribbons of shiny sugar',
 'pulling and folding hot sugar until it shines; blowing air into a warm sugar bubble; shaping petals by hand under a heat lamp; spinning thin threads with a fork; pouring syrup into a mould; fanning the piece so it keeps its shape; joining parts with a touch of hot sugar; cutting ribbons with scissors while warm',
 'a lustrous pearly sheen; glassy see-through edges; thin fragile curls; tiny trapped air bubbles; smooth rounded petals; sharp bright highlights; fine wispy strands; a slightly sticky-looking gloss',
 'ruby red and clear; pale pink and ivory; amber gold and cream; deep blue and white; soft green and clear; orange and yellow; lilac and pearl; clear glass-like white',
 'a tiny; a small; a hand-sized; a table-sized; a delicate; a tall; a centrepiece-sized; a palm-sized',
 'freshly pulled and shining; sagging in the heat; cloudy with damp; cracked at the thinnest points; sticky and dull; newly made and glossy; slightly drooping; fragile and perfect'),

'fireworks_display': ('fireworks display',
 'a round burst of red stars; a drooping golden willow over a river; a palm shape with thick rising trails; a ring of green sparks; a wide chrysanthemum with streaking tails; a cross of four blue bursts; a waterfall of silver sparks; a heart shape of pink stars',
 'burning metal-salt stars in the night sky; glowing sparks and trails; coloured stars and thick white smoke; bright bursts of silver and gold; streaks of light from rising shells; hundreds of tiny glowing points; a ceiling of falling sparks; burning stars in layers',
 'launching shells high into the dark sky; timing many bursts to a steady rhythm; firing rows of bursts in a fan shape; layering colours in one burst; building up to a bright finale; choreographing bursts over a river; firing from a barge or rooftop; sending low sparks across the ground',
 'long glowing streaks that fade; round flashes of light; drifting grey smoke lit by colour; a soft glow on the water below; thin bright trails; sparks that twinkle as they fall; sharp points of white light; smoke clouds tinted red and green',
 'red and gold; green and white; deep blue and silver; purple and pink; orange and yellow; silver and white; gold and crimson; blue and green',
 'a sky-wide; a huge; a small; a tower-high; a river-wide; a rooftop; a city-wide; a low',
 'blazing at its peak; fading into smoke; just launched; dying out in the dark; hanging as drifting haze; freshly burst; thinning to faint embers; glowing brightly'),

'floral_arrangement': ('floral arrangement',
 'a tall vase of white lilies and green leaves; a low bowl of roses and trailing ivy; three branches and a single bloom in a shallow dish; a wild bunch of tall grasses and poppies; a round bouquet of pink peonies; a wreath of dried flowers; a bare twisted branch with two blossoms; a mass of sunflowers in a jug',
 'fresh cut flowers and leaves; stems held on a needle holder; blossoms in clear water; dried flowers and seed pods; twisting branches and blooms; stems packed in damp foam; flowers in a ceramic vase; leaves and grasses in a shallow dish',
 'cutting stems at an angle; placing tall line flowers first; balancing three main lines at different heights; filling gaps with small sprays; leaving open space on one side; wiring branches into shape; tying stems with raffia; arranging in a round or triangular shape',
 'soft velvety petals; glossy green leaves; wet cut stems under clear water; rough bark on the branches; fine dusty pollen; papery dried petals; crisp curled leaf edges; a delicate translucent bloom',
 'white and green; blush pink and cream; deep red and dark green; yellow and orange; lavender and white; coral and peach; purple and silver green; mixed bright wildflower colours',
 'a small; a tall; a table-sized; a low; a large; a hand-held; a tiny; a doorway-sized',
 'freshly cut; at its full bloom; starting to droop; with browning petals; wilting at the edges; dried and papery; lightly dusted with fallen pollen; fresh and dewy'),

'balloon_sculpture': ('balloon sculpture',
 'a long-necked giraffe; a poodle with round ears; a sword with a curved guard; a tall flower with leaves; a swan with a curved neck; a bright arch of clusters; a snake coiled in loops; a monkey hanging from a branch',
 'twisted latex balloons; long thin latex tubes knotted together; round latex balloons in tight clusters; stretched rubbery skins filled with air; many segments of coloured latex; glossy balloons tied to a frame; layered latex in mixed colours; twisted tubes bound with wire',
 'twisting each segment until it locks; folding bubbles into joined pairs; knotting the ends together; filling each balloon with air by pump; stacking twisted segments into layers; weaving tubes through a frame; squeaking the rubber into place; building up shapes from many small balloons',
 'a glossy stretched rubber shine; tight twisted joints between bubbles; small knots at the ends; bright light reflections on round shapes; slightly translucent thin spots; squeaky smooth curves; wrinkled rubber near the twists; a taut shiny skin',
 'red and yellow; blue and pink; bright green and orange; purple and white; pastel mint and peach; gold and silver; black and red; rainbow colours',
 'a hand-sized; a small; a human-sized; a huge; a tiny; an arch-sized; a table-sized; a tall',
 'freshly twisted; tight and shiny; sagging as the air leaks out; slightly wrinkled; half deflated; fat and full; limp at the tips; ready to burst'),

'holographic_display': ('holographic display',
 'a glowing blue head turning slowly in the air; a floating model of a city street; a spinning planet made of light; a standing figure that seems to hover on a stage; a rotating engine made of fine lines; a floating map of a coastline; a ghostly dancer in a dark room; a slowly turning glass-like bird',
 'a see-through image of light floating in air; faint glowing lines on clear glass; fine glowing points in a hollow space; a ghostly reflection on a tilted clear pane; laser light on thin haze; a shimmering plate lit by a small bright lamp; tiny glowing dots swept through a volume; a translucent picture on stretched film',
 'reflecting a bright image off an angled clear pane; sweeping a point of light through a space; recording light patterns on a glass plate; lighting a plate from one direction; projecting onto a thin film of haze; dimming the room so the image stands out; fading the image in and out; scanning laser beams through the air',
 'a see-through glow with no solid edge; faint scan lines across the image; rainbow shimmer that shifts as you move; soft blurred edges on the light; a dark background showing through the picture; a slight flicker; thin bright outlines; depth that changes with viewing angle',
 'cyan and blue; green and white; rainbow shimmer on black; pale violet and teal; soft white on dark blue; orange and cyan; pink and blue; silver and green',
 'a tiny; a table-sized; a stage-sized; a human-sized; a small; a floating; a cube-shaped; a room-sized',
 'freshly projected; flickering faintly; fading in and out; shimmering softly; glitching at the edges; steady and glowing; half transparent; slightly blurred'),

'fruit_carving': ('fruit carving',
 'a watermelon carved into a deep flower; a melon basket with a lattice handle; a swan made from a pale melon; a carrot cut into a thin rose; a bird perched on a carved fruit; a bouquet of carved radish petals; a dragon coiling around a watermelon; a pumpkin carved with fine floral patterns',
 'watermelon with its green skin cut away; the pale flesh of a melon; thin slices of carrot and radish; the red and white layers of a carved fruit; pale yellow melon flesh; crisp vegetable skins curled into petals; cut apple with the red skin left on; firm pumpkin with a thin carved surface',
 'cutting thin petals with a small sharp knife; carving through the skin to the flesh; scooping out a hollow with a curved tool; shaping layers into overlapping petals; cutting grooves with a V-shaped blade; scoring a pattern before cutting deeper; rinsing in cold water to keep it crisp; setting small pieces with toothpicks',
 'wet glistening cut flesh; sharp contrast between skin and flesh; thin crisp petals; fine tool marks in the surface; tiny beads of juice; smooth glossy skin left on the outside; layers of curled slices; clean sharp edges',
 'deep green and pink; red and white; orange and pale yellow; green and cream; bright red and green; purple and white; pale gold and green; coral and white',
 'a small; a plate-sized; a table-sized; a hand-sized; a large; a centrepiece-sized; a tiny; a basket-sized',
 'freshly carved and glistening; starting to brown at the edges; slightly dried out; sagging at the petals; shrivelled at the tips; crisp and cold; dull and limp; fresh from the fridge'),

'kinetic_sculpture': ('kinetic sculpture',
 'a hanging cluster of flat red and black shapes; a row of tall rotating rods; a wave of hanging metal droplets; a tall rotating spiral of wire; a wooden ball rolling through a winding track; a frame of thin arms that swing slowly; a ring of mirrored plates turning in the wind; a group of tall slender wings that open and close',
 'thin sheet metal on balanced wire; polished steel and thin cable; painted aluminium discs; wooden rods and strings; clear plastic and metal frames; many hanging metal pieces on thin wires; small motors hidden in a metal frame; brass arms on fine pivots',
 'balancing each arm on a single wire; driving the parts with hidden motors; letting the wind move the pieces; hanging many pieces from one beam; linking pieces with fine cables; casting moving shadows on the wall; rolling balls along a looping track; turning slowly on a central pivot',
 'smooth painted flat colour on metal; bright polished reflections; thin wires almost invisible; a slight blur where parts spin; long moving shadows; matte black rods; small joints and hinges showing; gentle glints on turning edges',
 'red, black and white; polished silver; bright yellow and blue; copper and brass; matte black and gold; white and sky blue; green and orange; grey steel and red',
 'a desk-sized; a room-sized; a hall-sized; a small; a tall; a ceiling-high; a monumental; a hand-sized',
 'turning slowly; freshly polished; rusted at the joints; dusty on the arms; frozen mid-swing; slightly bent; gleaming and new; creaking and tired'),

'land_art': ('land art earthwork',
 'a long spiral of dark rock reaching into a lake; a ring of tall standing stones on a hill; a long straight trench cut into dry ground; a huge figure cut into a chalk hillside; a circle of stacked rocks in a desert; a line of upright boulders across a field; a low grass mound shaped like a wave; a pattern of pale lines on a flat plain',
 'dark rock and packed earth; tall slabs of grey standing stone; white chalk showing through grass; heaps of gravel and sand; turf cut away from bare soil; salt crystals on a flat lake bed; piled boulders from the site; soil shaped into long ridges',
 'moving earth with heavy machines; setting stones upright in a ring; cutting lines into a hillside; stacking rocks without any mortar; raking gravel into patterns; shaping soil into mounds and trenches; marking a huge shape from above; placing stones in line with the sun',
 'rough weathered rock; patches of lichen on the stones; bare cut earth edges; short grass growing over the mounds; crusts of white salt; wind-smoothed stone; cracked dry mud; pale chalk against green grass',
 'earth brown and grey; white chalk and green; rust red and sand; dark rock and blue water; pale grey stone and golden grass; salt white and pink; black basalt and tan; green turf and bare soil',
 'a field-sized; a hillside-sized; a monumental; a vast; a kilometre-long; a small; a valley-sized; a lakeside',
 'weathered by wind and rain; half buried by water; overgrown with grass; eroded at the edges; freshly cut; covered in lichen; sunk into the soil; bleached by the sun'),
}

SHARED = {
'display': 'on a plain grey studio floor; on a white seamless backdrop; on a dark reflective surface; on a wooden table; on a small plinth; inside a glass case; in a bare white gallery; on a shelf against a plain wall; on a black stage; hung from the ceiling; in an open outdoor space; on a pedestal in a dim room',
'light': 'soft studio light; warm lamp light; cold blue light; harsh side light; dim moody light; bright even daylight; a single spotlight; glowing coloured light; soft overcast light; strong rim light from behind; flickering light; low evening light',
'shot': 'a three-quarter view; a straight front view; a high overhead view; a low hero angle; a close-up macro view; a wide establishing view; a tilt-shift miniature view; an eye-level view; an isometric corner view; a symmetrical centred view; a view from slightly above; a distant long view',
'marks': 'with a small caption in the corner that reads "Scene 07"; with a tiny label card that reads "Study 12"; with a small sign beside it that reads "Do not touch"; with a hand-lettered tag that reads "No. 4"; with a small plaque that reads "Untitled"; with a corner caption that reads "Frame 031"; with no text at all; with no text at all and a clean frame; with a small title card that reads "Night Shift"; with a neat numbered tag that reads "A-09"',
}

DISPLAY = {
'clay_render': 'shown on a monitor with a thin dark frame; on a plain pale grey studio floor; on a white seamless backdrop; printed on matte paper and pinned to a wall; on a plain light backdrop with a soft floor shadow; centred on an empty off-white page; on a bare grey turntable base',
'photoreal_product_render': 'on a seamless white sweep; on a dark glossy studio floor; on a gradient grey backdrop; on a polished reflective surface; floating above a soft floor shadow; shown on a bright monitor in a clean frame; on a plain pale plinth',
'low_poly_render': 'shown on a monitor with a thin frame; on a soft gradient backdrop; centred on a plain pastel background; printed as a flat poster on a wall; on a plain pale studio floor; on an empty sky-coloured backdrop',
'voxel_art': 'shown on a monitor with a thin dark frame; on a plain flat-coloured backdrop; on a simple square base against a pale background; printed as a flat poster on a wall; on a soft sky gradient; centred on an empty dark screen',
'isometric_diorama': 'floating on a plain pastel background; shown on a monitor in a thin frame; on a soft gradient backdrop; centred on an empty off-white page; on a flat dark backdrop; printed as a flat poster on a wall',
'wireframe_render': 'on a dark monitor screen; against a deep blue backdrop; on a plain black background; on a pale grid-lined blueprint page; floating in an empty dark space; printed in thin lines on white paper',
'toon_shaded_render': 'shown on a monitor with a thin frame; on a flat painted-style backdrop; on a plain pastel background; printed as a flat poster on a wall; centred on an empty light page; on a simple sky gradient',
'soft_translucent_render': 'on a plain soft pastel backdrop; on a pale studio floor with a soft shadow; shown on a monitor in a thin frame; against a warm gradient backdrop; on a seamless white sweep; printed on matte paper and pinned to a wall',
'glass_chrome_render': 'on a mirrored studio floor; floating above a soft gradient backdrop; on a checkered floor; shown on a bright monitor in a thin frame; against an empty pale gradient; on a dark glossy surface',
'claymation_scene': 'on a miniature set under warm lamps; on a small tabletop stage; in front of a painted paper backdrop; on a plain wooden tabletop; in a still from a film with a shallow depth of field; on a small set with a painted sky',
'felt_puppet_scene': 'on a miniature set under warm lamps; on a small tabletop stage; in front of a painted paper backdrop; on a plain wooden tabletop; in a still from a film with a shallow depth of field; on a small set with cardboard scenery',
'brick_build': 'on a flat baseplate on a shelf; on a plain white table; on a bright shelf against a plain wall; on a wooden table; on a plain white photo set; on a pale plinth',
'vinyl_toy': 'on a glass shelf; on a plain white shelf; on a small plinth; inside a clear window box; on a plain desk; on a collector shelf against a plain wall',
'resin_figurine': 'on a round display base; inside a lit glass case; on a small plinth; on a dark shelf with a spotlight; on a plain wooden desk; on a white shelf against a plain wall',
'action_figure': 'on a clear display stand; on a plain shelf; inside a card and bubble pack; on a collector shelf against a plain wall; on a plain desk; on a small plinth',
'neon_sign': 'on a dark wall; on a black panel in a dim room; in a shop window at night; on a plain brick wall in the dark; hanging in a dim gallery; on a dark painted board',
'led_installation': 'in a dark room; in a bare white gallery; in an open plaza at night; in a long dim corridor; in a large dark hall; in an empty warehouse',
'projection_mapping': 'on a building at night; on a stone wall in the dark; on a tall facade over a plaza; on a curved wall in a dark space; on a bridge at night; on a wide front of an old building',
'infinity_mirror_room': 'in a dark mirrored room; in a small gallery chamber; in a dim room with a low platform; in a black mirrored cube; in a bare gallery space; in a dark room with a shallow floor of water',
'sand_mandala': 'on a low table in a quiet hall; on a flat floor in a bare gallery; on a wide table under soft light; on a platform in a temple room; on a plain dark floor; on a low round platform',
'chalk_pavement_art': 'on a paved street; on a stone plaza; on a wide pavement beside a wall; on a grey asphalt road; in a busy square; on paving slabs outside a building',
'ice_sculpture': 'on a table with a white cloth; on a plain dark base; in a cold hall with lights beneath; on a block of ice; on a metal tray; in an open frozen courtyard',
'sugar_sculpture': 'on a banquet table; on a plain white plate; on a small plinth; under a glass dome; on a dark tray; on a mirrored board',
'fireworks_display': 'over a dark river; across a night sky; above a city skyline; over a dark field; above a calm lake; over a crowd at night',
'floral_arrangement': 'on a wooden table; on a low plinth; in a quiet alcove; on a plain white shelf; on a stone ledge; on a dark table by a window',
'balloon_sculpture': 'on a party table; on a plain floor; in a bright hall; against a plain wall; in a shop entrance; on a plain white backdrop',
'holographic_display': 'in a dark room; on a small black stage; above a dark table; behind a clear pane; in a dim hall; against a black backdrop',
'fruit_carving': 'on a banquet table; on a plain white plate; on a bed of ice; on a dark tray; at the centre of a table; on a wooden board',
'kinetic_sculpture': 'in a bare white gallery; in a tall hall; in an open courtyard; on a plain plinth; in a bright atrium; against a plain pale wall',
'land_art': 'in an open landscape; on a wide empty plain; on a hillside; beside a lake; in a dry desert; in a grassy field',
}

def _check():
    keys = ('subjects', 'materials', 'techniques', 'finishes', 'colours', 'scales', 'wear')
    bad = 0
    for k, v in FORMS.items():
        assert len(v) == 8, k
        for name, s in zip(keys, v[1:]):
            items = [x.strip() for x in s.split(';')]
            if not 8 <= len(items) <= 10:
                print('count', k, name, len(items)); bad += 1
            for it in items:
                if not it or any(c in it for c in '{}|') or ': ' in it:
                    print('badchar', k, name, it); bad += 1
    for n in ('display', 'light', 'shot'):
        c = len(SHARED[n].split(';'))
        if not 10 <= c <= 12:
            print('shared count', n, c); bad += 1
    assert set(DISPLAY) == set(FORMS), set(FORMS) ^ set(DISPLAY)
    for k, v in DISPLAY.items():
        items = v.split(';')
        if not 6 <= len(items) <= 8 or any(not x.strip() or any(c in x for c in '{}|') or ': ' in x for x in items):
            print('display bad', k, len(items)); bad += 1
    m = SHARED['marks'].split(';')
    if not 8 <= len(m) <= 10 or any(not x.strip().startswith('with ') for x in m):
        print('marks bad'); bad += 1
    return bad

if __name__ == '__main__':
    print('forms', len(FORMS))
    for k, v in FORMS.items():
        print(k, [len(s.split(';')) for s in v[1:]])
    print('shared', {k: len(v.split(';')) for k, v in SHARED.items()})
    print('problems', _check())
