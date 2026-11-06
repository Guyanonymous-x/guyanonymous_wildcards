"""v109 - architectural fixtures and fittings (user 2026-11-06): the built-in parts of rooms and buildings that had no object builder yet.
Each fixture gets the same set as other objects: ob_<k>_type (forms), _material, _wear, _detail, _era, _short, _phrase, _full, and _text where
text belongs on it (house numbers, floor numbers). The era-sensitive ones also get period descriptions (v109_era_data_g.py) so v109_era makes
their _full era-matched. Wear pools are per group so a staircase never gets a fabric's wear."""

WEAR = {
 'door': ['freshly painted', 'scuffed along the bottom edge', 'with paint worn thin around the handle', 'slightly warped and sticking in its frame', 'polished smooth by years of hands', 'weathered and faded by sun', 'with flaking paint at the corners', 'in good condition'],
 'window': ['freshly painted', 'with flaking paint on the frame', 'with streaky glass', 'sparkling clean', 'with condensation along the bottom of the glass', 'with old putty cracking round the panes', 'weathered and grey', 'in good condition'],
 'surface': ['clean and freshly finished', 'scuffed in places', 'faded by sunlight', 'stained in places', 'patched in one area', 'chipped at the edges', 'with a hairline crack', 'in good condition'],
 'floor': ['freshly polished', 'worn smooth along the busiest path', 'scuffed by chair legs', 'faded by sunlight near the window', 'stained in places', 'with a few cracked pieces', 'freshly swept', 'in good condition'],
 'structure': ['solid and freshly painted', 'darkened with age', 'cracked along one face', 'chipped at the edges', 'weathered', 'newly restored', 'stained in places', 'in good condition'],
 'stair': ['worn into shallow dips at the centre of each tread', 'freshly varnished', 'scuffed along the nosings', 'creaky and well used', 'polished by years of feet', 'newly carpeted', 'chipped on the edges of the steps', 'in good condition'],
 'roof': ['weathered and mossy', 'newly fitted', 'streaked with rainwater stains', 'with a few slipped pieces', 'sagging slightly', 'freshly painted', 'with lichen in patches', 'in good condition'],
 'machine': ['spotless and gleaming', 'scuffed by heavy use', 'with fingerprints on the steel', 'dusty', 'newly serviced', 'slightly dented', 'well kept', 'in good condition'],
}
ERA_WORDS = ['from the 1880s', 'from the 1920s', 'from the 1930s', 'from the 1950s', 'from the 1960s', 'from the 1970s', 'from the 1990s', 'recently fitted']

# key: (group, types, materials, details, text lines or None)
FIX = {
 'door': ('door', ['a front door', 'a panelled interior door', 'a flush door', 'a stable door split across the middle', 'a ledged and braced plank door', 'a half-glazed door', 'a double door', 'an arched door'],
   ['painted timber', 'solid oak', 'pine', 'steel', 'aluminium and glass', 'painted plywood', 'weathered teak', 'green-painted timber'],
   ['a brass knocker', 'a round brass knob', 'a lever handle', 'a small glass panel', 'a letter flap', 'iron studs', 'a fanlight above it', 'a spyhole at eye height'],
   ['with the house number "__name_number_small__" in brass numerals on the upper panel', 'with the number "__name_number_small__" painted in white beside the knocker']),
 'doorframe': ('door', ['a doorframe', 'a wide doorframe with deep reveals', 'an arched door opening'], ['painted timber', 'oak', 'steel', 'stone'], ['a carved architrave', 'pencil height marks', 'a hinge plate', 'a draught strip'], None),
 'door_handle': ('machine', ['a door handle', 'a lever handle on a backplate', 'a round door knob', 'a long pull bar'], ['polished brass', 'brushed steel', 'black iron', 'porcelain', 'chrome'], ['a matching keyhole plate', 'a rose backplate', 'a thumb latch'], None),
 'knocker': ('machine', ['a door knocker', 'a ring-shaped knocker', 'a lion-head knocker', 'a plain bar knocker'], ['brass', 'black iron', 'bronze'], ['a striking plate', 'a worn shine where it is gripped'], None),
 'keyhole': ('machine', ['a keyhole plate', 'a keyhole with a swinging cover'], ['brass', 'iron', 'chrome'], ['a tiny pivoting cover', 'a key left in it'], None),
 'fire_door': ('door', ['a fire door', 'a pair of fire doors with push bars'], ['heavy painted timber', 'steel'], ['a small wired-glass window', 'an overhead closer arm', 'a push bar across the middle'], None),
 'revolving_door': ('machine', ['a revolving door', 'a four-winged revolving door in a glass drum'], ['bronze and glass', 'steel and glass', 'polished brass and glass'], ['brush strips on each wing', 'a polished floor plate', 'a curved glass canopy'], None),
 'sliding_door': ('door', ['a sliding door', 'a patio door', 'a barn-style sliding door on a top rail'], ['aluminium and glass', 'painted timber', 'steel and glass'], ['a long recessed pull', 'a top track', 'a floor guide'], None),
 'french_door': ('door', ['a pair of french doors', 'glazed double doors opening onto a garden'], ['painted timber and glass', 'white uPVC and glass', 'steel-framed glass'], ['small square panes', 'long brass bolts', 'sheer curtains'], None),
 'window': ('window', ['a window', 'a sash window', 'a casement window', 'a bay window', 'a picture window', 'a round window', 'a tall arched window', 'a small square window'],
   ['painted timber', 'white uPVC', 'slim steel', 'aluminium', 'weathered oak', 'black-painted steel'],
   ['a deep sill', 'small leaded panes', 'a brass catch', 'a window box of flowers', 'net curtains', 'a stained-glass top light', 'a roller blind', 'a crack in one corner pane'], None),
 'sash_window': ('window', ['a sash window', 'a tall sash window with six panes over six', 'a sash window with two large panes'], ['painted timber', 'white-painted pine'], ['brass sash lifts', 'a sash cord showing at the side', 'a wide sill'], None),
 'casement': ('window', ['a casement window', 'a pair of side-hung casements'], ['painted timber', 'steel', 'uPVC'], ['a stay arm', 'a lever handle', 'small square panes'], None),
 'bay_window': ('window', ['a bay window', 'a curved bow window', 'a three-sided bay window'], ['painted timber', 'stone and timber', 'uPVC'], ['a cushioned window seat', 'plants along the sill', 'long curtains'], None),
 'dormer': ('roof', ['a dormer window', 'a pitched dormer', 'a flat-roofed dormer'], ['tile-hung timber', 'slate-clad timber', 'lead-clad timber'], ['a small gable', 'a lead apron below it'], None),
 'skylight': ('window', ['a skylight', 'a roof window', 'a lantern roof light', 'a round dome skylight'], ['aluminium and glass', 'timber and glass', 'clear acrylic'], ['rain streaks', 'a blind pulled halfway', 'a view of sky'], None),
 'fanlight': ('window', ['a fanlight', 'a half-moon fanlight above a door', 'a rectangular transom light'], ['painted timber and glass', 'iron tracery and glass', 'coloured stained glass'], ['radiating glazing bars', 'a pattern of coloured glass'], ['with the number "__name_number_small__" painted in gold on the glass']),
 'porthole': ('window', ['a porthole', 'a round porthole window', 'a porthole with a thick rim'], ['brass and thick glass', 'steel and glass'], ['wing nuts round the rim', 'a hinged deadlight cover'], None),
 'wall': ('surface', ['a wall', 'a tall wall', 'a long wall', 'a curved wall', 'a wall with a window', 'a wall with a doorway', 'a feature wall', 'a gable end wall'],
   ['painted plaster', 'red brick', 'rough stone', 'bare concrete', 'painted brick', 'oak panelling', 'white tiles', 'cedar boards'],
   ['a picture rail', 'a framed print', 'a hairline crack', 'a light switch', 'a row of hooks', 'a patch of fresh paint', 'a dado rail', 'an old fixing hole'], None),
 'floor': ('floor', ['a floor', 'a wide open floor', 'a hallway floor', 'a kitchen floor', 'a landing floor', 'a stepped floor', 'a sunlit floor', 'a narrow corridor floor'],
   ['oak boards', 'pine boards', 'terracotta tiles', 'polished concrete', 'grey carpet', 'stone flags', 'herringbone parquet', 'speckled vinyl'],
   ['a rug', 'a worn path', 'a gap between boards', 'a floor vent', 'a scatter of dust', 'a chair scrape mark'], None),
 'floorboard': ('floor', ['floorboards', 'wide plank floorboards', 'narrow tongue-and-groove floorboards'], ['pine', 'oak', 'reclaimed elm'], ['nail heads in rows', 'gaps between boards', 'a lifted board'], None),
 'parquet': ('floor', ['a parquet floor', 'a herringbone parquet floor', 'a chevron parquet floor'], ['oak', 'walnut', 'teak'], ['a border band', 'a waxed sheen', 'a few loose blocks'], None),
 'linoleum': ('floor', ['a linoleum floor', 'a patterned lino floor', 'a sheet vinyl floor'], ['marbled linoleum', 'checked linoleum', 'speckled vinyl'], ['a curled edge at the doorway', 'a worn patch by the sink'], None),
 'terrazzo': ('floor', ['a terrazzo floor', 'a terrazzo staircase landing'], ['grey terrazzo with marble chips', 'pink terrazzo', 'white terrazzo with black chips'], ['brass dividing strips', 'a polished shine'], None),
 'ceiling': ('surface', ['a ceiling', 'a high ceiling', 'a low ceiling', 'a vaulted ceiling', 'a coffered ceiling', 'a sloping attic ceiling', 'a flat ceiling'],
   ['painted plaster', 'exposed timber beams', 'square mineral-fibre tiles', 'tongue-and-groove pine', 'pressed tin', 'bare concrete'],
   ['a ceiling rose', 'a cornice', 'a hanging pendant light', 'a water stain', 'a smoke detector', 'a ceiling fan'], None),
 'ceiling_rose': ('surface', ['a ceiling rose', 'a round plaster ceiling rose', 'a leafy plaster medallion'], ['moulded plaster', 'painted plaster'], ['a pendant light hanging from the centre', 'layers of old paint softening the detail'], None),
 'cornice': ('surface', ['a cornice', 'a deep moulded cornice', 'a plain coving'], ['moulded plaster', 'painted plaster', 'timber'], ['egg-and-dart moulding', 'a crack along one join'], None),
 'skirting': ('surface', ['a skirting board', 'a tall moulded skirting board', 'a plain low skirting board'], ['painted timber', 'oak', 'MDF painted white'], ['scuffs from a vacuum', 'a cable clipped along the top'], None),
 'architrave': ('surface', ['an architrave', 'a moulded architrave around a door'], ['painted timber', 'oak'], ['a plinth block at the base', 'layers of paint'], None),
 'dado': ('surface', ['a dado rail', 'a dado rail with panelling below'], ['painted timber', 'oak'], ['paint in two colours above and below'], None),
 'picture_rail': ('surface', ['a picture rail', 'a picture rail with brass hooks'], ['painted timber'], ['picture wires hanging from hooks'], None),
 'panelling': ('surface', ['wall panelling', 'tall raised-and-fielded panelling', 'tongue-and-groove panelling'], ['dark oak', 'painted pine', 'walnut'], ['a carved frieze', 'a hidden door in the panels'], None),
 'wallpaper': ('surface', ['wallpaper', 'patterned wallpaper', 'flocked wallpaper', 'striped wallpaper', 'woodchip wallpaper'], ['printed paper', 'flocked velvet paper', 'vinyl wallpaper'], ['a peeling corner', 'a matching border', 'a seam lifting'], None),
 'tiling': ('surface', ['wall tiling', 'tiling around a bath', 'floor-to-ceiling tiling', 'a band of decorative tiling'], ['white glazed tiles', 'brick-shaped metro tiles', 'patterned encaustic tiles', 'small mosaic tiles'], ['grey grout lines', 'a cracked tile', 'a border of coloured tiles'], None),
 'mosaic': ('floor', ['a mosaic', 'a mosaic floor', 'a mosaic wall panel'], ['small glass tesserae', 'small stone tesserae', 'ceramic tesserae'], ['a geometric border', 'a pattern of birds and leaves'], None),
 'splashback': ('surface', ['a splashback', 'a splashback behind a hob', 'a splashback behind a sink'], ['toughened glass', 'stainless steel', 'glazed tiles'], ['a row of hanging utensils', 'a few splashes'], None),
 'worktop': ('surface', ['a kitchen worktop', 'a long run of worktop', 'a breakfast bar'], ['laminate', 'solid oak', 'granite', 'white quartz', 'stainless steel', 'tiled'], ['a chopping board', 'a kettle', 'a fruit bowl', 'a knife block', 'a ring mark from a hot pan'], None),
 'kitchen_island': ('surface', ['a kitchen island', 'a kitchen island with stools', 'a wheeled kitchen island'], ['painted timber and quartz', 'oak', 'steel'], ['a hanging rack of pans above', 'a small sink set in', 'tall stools tucked under'], None),
 'partition': ('surface', ['a partition wall', 'an office partition', 'a folding room divider', 'a cubicle partition'], ['frosted glass', 'painted plasterboard', 'laminate panels', 'slatted timber'], ['a glass door', 'a narrow gap at the top', 'a pinned photograph'], None),
 'staircase': ('stair', ['a straight staircase', 'a spiral staircase', 'a sweeping curved staircase', 'a dog-leg staircase with a half landing', 'a steep cottage staircase', 'a floating staircase'],
   ['oak', 'painted pine', 'stone', 'cast iron', 'concrete', 'steel and glass', 'carpeted timber'],
   ['a carved newel post', 'a long handrail', 'a stair runner held by brass rods', 'turned spindles', 'a window on the landing', 'a glass balustrade'], None),
 'banister': ('stair', ['a banister', 'a curved banister', 'a banister with turned spindles'], ['polished mahogany', 'painted pine', 'wrought iron'], ['a carved newel cap', 'a worn shiny top'], None),
 'balustrade': ('stair', ['a balustrade', 'a curved balustrade', 'a balustrade along a landing', 'a balustrade on a terrace'], ['carved stone', 'toughened glass', 'wrought iron', 'painted timber'], ['bottle-shaped balusters', 'a flat top rail', 'scrolled ironwork'], None),
 'newel': ('stair', ['a newel post', 'a carved newel post', 'a square newel post with a ball cap'], ['oak', 'painted pine', 'mahogany'], ['a carved acorn cap', 'a scuffed base'], None),
 'landing': ('stair', ['a landing', 'a wide half landing', 'a top-floor landing'], ['carpeted timber', 'stone', 'polished boards'], ['a window', 'a small table with a lamp', 'a row of doors'], None),
 'escalator': ('machine', ['an escalator', 'a pair of escalators running up and down', 'a long escalator into an underground station'], ['steel and glass', 'stainless steel', 'wood-panelled steel'], ['black rubber handrails', 'grooved metal steps', 'yellow edge lines on each step', 'lit side panels'], None),
 'lift': ('machine', ['a lift', 'a passenger lift', 'an open-cage lift', 'a goods lift', 'a glass panoramic lift'], ['brushed steel', 'mirrored panels', 'polished brass', 'wrought iron and glass'], ['a panel of round buttons', 'a folding gate', 'a handrail', 'a small round lamp above the door'], ['with the floor number "__name_number_small__" lit above the doors']),
 'fire_escape': ('structure', ['a fire escape', 'a zigzag fire escape', 'an external staircase'], ['black-painted iron', 'galvanised steel'], ['a drop ladder', 'grated steps', 'a landing at each floor'], None),
 'beam': ('structure', ['a beam', 'an exposed ceiling beam', 'a girder', 'a tie beam'], ['adzed oak', 'painted steel', 'pine', 'concrete'], ['old peg holes', 'rivets', 'adze marks'], None),
 'rafter': ('structure', ['rafters', 'exposed roof rafters', 'a row of rafters under the slates'], ['rough pine', 'oak', 'painted timber'], ['cobwebs between them', 'old nails'], None),
 'truss': ('structure', ['a roof truss', 'a king post truss', 'a lattice truss'], ['oak', 'pine', 'steel'], ['iron straps at the joints', 'bolted plates'], None),
 'pillar': ('structure', ['a pillar', 'a round pillar', 'a square pillar', 'a fluted pillar'], ['stone', 'painted cast iron', 'concrete', 'marble'], ['a carved capital', 'a square base', 'a fire extinguisher beside it'], None),
 'pilaster': ('structure', ['a pilaster', 'a fluted pilaster', 'a pair of pilasters framing a doorway'], ['stone', 'painted plaster', 'timber'], ['a carved capital', 'a plain base'], None),
 'archway': ('structure', ['an archway', 'a round archway', 'a pointed archway', 'a wide arch'], ['brick', 'stone', 'painted plaster'], ['a keystone at the top', 'worn steps beneath', 'ivy round the edge'], None),
 'alcove': ('structure', ['an alcove', 'an arched alcove', 'a shelved alcove beside a chimney breast'], ['painted plaster', 'stone'], ['built-in shelves', 'a lamp on a shelf', 'a curved top'], None),
 'niche': ('structure', ['a niche', 'a small arched wall niche', 'a recessed display niche'], ['plaster', 'stone'], ['a small statue', 'a candle', 'a vase of flowers'], None),
 'lintel': ('structure', ['a lintel', 'a lintel over a door', 'a lintel over a window'], ['stone', 'oak', 'concrete'], ['a carved rosette', 'cracks at one end'], ['with "__name_established__" carved into the stone']),
 'sill': ('window', ['a windowsill', 'a deep windowsill', 'a narrow windowsill'], ['stone', 'painted timber', 'tiled'], ['a row of potted plants', 'a cat asleep on it', 'a jar of pens'], None),
 'threshold': ('floor', ['a threshold', 'a doorstep', 'a threshold strip'], ['worn stone', 'brass', 'oak'], ['a doormat', 'a dip worn in the middle'], None),
 'porch': ('roof', ['a porch', 'an open porch', 'an enclosed porch', 'a columned porch'], ['painted timber', 'brick and tile', 'stone'], ['a bench', 'boots by the door', 'a hanging lantern'], None),
 'veranda': ('roof', ['a veranda', 'a wide covered veranda', 'a wraparound veranda'], ['painted timber', 'cast iron lacework', 'bamboo'], ['rocking chairs', 'hanging plants', 'a ceiling fan'], None),
 'balcony': ('structure', ['a balcony', 'a juliet balcony', 'a long balcony', 'a corner balcony', 'a small balcony'], ['wrought iron', 'concrete', 'glass and steel', 'timber'], ['potted plants', 'washing hung on a rail', 'a small table and chairs'], None),
 'parapet': ('structure', ['a parapet', 'a low parapet along a roof', 'a parapet on a bridge'], ['stone', 'brick', 'concrete'], ['coping stones along the top', 'a stone urn at the corner'], None),
 'roof': ('roof', ['a roof', 'a pitched roof', 'a flat roof', 'a steep roof', 'a hipped roof', 'a mansard roof', 'a low curved roof'],
   ['clay tiles', 'slate', 'thatch', 'corrugated iron', 'green copper', 'roofing felt', 'cedar shingles'], ['a chimney stack', 'a ridge of crested tiles', 'a skylight', 'a weathervane', 'solar panels'], None),
 'gutter': ('roof', ['a gutter', 'a half-round gutter', 'an ogee gutter'], ['cast iron', 'black plastic', 'zinc', 'copper'], ['a leaf-blocked corner', 'a downpipe joint', 'brackets every metre'], None),
 'chimney': ('roof', ['a chimney', 'a chimney stack with pots', 'a tall factory chimney', 'a squat chimney'], ['red brick', 'stone', 'rendered brick'], ['clay chimney pots', 'a cowl', 'a TV aerial strapped to it'], None),
 'chimney_breast': ('surface', ['a chimney breast', 'a painted chimney breast with alcoves either side'], ['painted plaster', 'bare brick'], ['a mirror above the mantel', 'a picture'], None),
 'mantelpiece': ('surface', ['a mantelpiece', 'a carved mantelpiece', 'a plain mantel shelf'], ['marble', 'painted timber', 'oak', 'slate'], ['a clock', 'a row of cards', 'candlesticks', 'a pair of china dogs'], None),
 'hearth': ('surface', ['a hearth', 'a raised hearth', 'a wide hearth'], ['slate', 'tiles', 'stone'], ['a fire guard', 'a log basket', 'a brass fender'], None),
 'window_seat': ('surface', ['a window seat', 'a cushioned window seat in a bay', 'a built-in window bench'], ['painted timber', 'oak'], ['cushions', 'a folded blanket', 'a book left open'], None),
 'shower_screen': ('surface', ['a shower screen', 'a fixed shower screen', 'a folding bath screen'], ['clear glass', 'frosted glass', 'patterned glass'], ['chrome hinges', 'water droplets', 'limescale streaks'], None),
 'ceiling_fan': ('machine', ['a ceiling fan', 'a ceiling fan with a light', 'a five-blade ceiling fan'], ['wood and brass', 'white metal', 'black steel'], ['a pull chain', 'a glass light bowl'], None),
 'fuse_box': ('machine', ['a fuse box', 'a consumer unit', 'an old fuse board on a wooden panel'], ['white plastic', 'grey steel', 'bakelite on wood'], ['a row of switches', 'a hinged clear cover'], None),
 'light_switch': ('machine', ['a light switch', 'a double light switch', 'a dimmer switch', 'a toggle switch'], ['white plastic', 'brushed steel', 'brass', 'brown bakelite'], ['a smudge of fingerprints around it', 'a round dial'], None),
 'dome': ('roof', ['a dome', 'a shallow dome', 'a tall ribbed dome', 'a dome ceiling'], ['green copper', 'glass and iron', 'painted plaster', 'stone'], ['a lantern at the top', 'ribs radiating from the centre'], None),
 'vault': ('structure', ['a vaulted ceiling', 'a ribbed vault', 'a barrel vault'], ['stone', 'brick', 'painted plaster'], ['carved bosses where ribs meet', 'old soot marks'], None),
 'conservatory': ('roof', ['a conservatory', 'a lean-to glasshouse', 'a tall glass conservatory with an ornate iron ridge'], ['white-painted timber and glass', 'white uPVC and glass', 'cast iron and glass'], ['potted palms', 'wicker chairs', 'blinds under the roof'], None),
 'pergola': ('roof', ['a pergola', 'a long pergola', 'a pergola covered in vines'], ['oak', 'pine', 'black steel'], ['climbing roses', 'string lights', 'a hanging basket'], None),
 'cladding': ('surface', ['wall cladding', 'vertical cladding', 'horizontal board cladding'], ['cedar boards', 'corrugated steel', 'slate', 'charred timber'], ['weathered silver patches', 'rain streaks'], None),
 'gatepost': ('structure', ['a gatepost', 'a pair of gateposts', 'a square gate pier with a ball on top'], ['stone', 'brick', 'oak'], ['a carved ball finial', 'iron hinge pins'], ['with the house name "__name_town__" carved into the stone']),
}

def build(final=None):
    G = {}
    for g, v in WEAR.items(): G['ob_fixture_wear_%s' % g] = v
    names = []
    for k, (grp, types, mats, dets, text) in FIX.items():
        b = 'ob_%s' % k
        G[b + '_type'] = types; G[b + '_material'] = mats; G[b + '_detail'] = dets
        G[b + '_wear'] = ['__ob_fixture_wear_%s__' % grp]; G[b + '_era'] = ERA_WORDS
        t = ''
        if text: G[b + '_text'] = text; t = ', __%s_text__' % b
        G[b + '_short'] = ['__%s_type__ in __%s_material__' % (b, b)]
        G[b + '_phrase'] = ['__%s_type__ in __%s_material__, __%s_wear__' % (b, b, b)]
        G[b + '_full'] = ['__%s_type__ in __%s_material__, __%s_wear__, with __%s_detail__%s' % (b, b, b, b, t)]  # era-sensitive fixtures get period lines from v109_era
        names.append(k)
    G['ob_fixture_names'] = names
    for suf in ('short', 'phrase', 'full'): G['ob_fixture_any_%s' % suf] = ['__ob_%s_%s__' % (n, suf) for n in names]
    return G
