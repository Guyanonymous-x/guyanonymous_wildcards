"""v50 data: furniture broken into parts. Each part has independent options (style, design, material); some include 'none'."""
WOOD = ['oak', 'walnut', 'pine', 'teak', 'mahogany', 'ash', 'birch', 'cherry wood', 'beech', 'bamboo', 'painted softwood', 'reclaimed timber', 'ebonised wood', 'maple', 'elm']
FABRIC = ['velvet', 'linen', 'cotton canvas', 'leather', 'faux leather', 'wool tweed', 'woven boucle', 'corduroy', 'patterned tapestry fabric', 'smooth microfibre', 'woven cane', 'striped cotton']
METAL = ['brushed steel', 'black iron', 'polished brass', 'antique brass', 'chrome', 'copper', 'matt black powder-coated steel', 'aged bronze', 'pewter', 'gold-coloured metal']
PARTS = {
'bed': {
 'headboard': ['no headboard at all', 'a tall upholstered headboard in __part_fabric__ with button tufting', 'a low plain headboard of __part_wood__', 'a headboard of vertical slats in __part_wood__', 'a curved headboard padded in __part_fabric__', 'a wrought-iron headboard with curling scrolls in __part_metal__', 'a woven cane headboard in a rounded shape', 'a carved headboard of __part_wood__ with a peaked top', 'a wide panelled headboard of __part_wood__ with a raised centre', 'a headboard formed of horizontal bars in __part_metal__', 'a shelf-style headboard of __part_wood__ holding books and a lamp', 'a winged headboard that curves forward at the sides, in __part_fabric__', 'a plain padded headboard in __part_fabric__ in __comp_colour__'],
 'footboard': ['no footboard at all', 'a low footboard of __part_wood__ matching the frame', 'a footboard of vertical slats in __part_wood__', 'a footboard in curved iron bars in __part_metal__', 'a padded footboard in __part_fabric__', 'a tall footboard with turned posts at each end', 'a bench-style footboard that doubles as a seat, in __part_fabric__', 'a carved footboard of __part_wood__ with a scalloped top', 'a plain panel footboard painted in __comp_colour__'],
 'frame': ['a low platform frame of __part_wood__ with no legs', 'a divan base with a fabric-covered side in __part_fabric__', 'a frame of __part_wood__ on four tapered legs', 'a metal frame in __part_metal__ with slim rails', 'a four-poster frame of __part_wood__ with tall corner posts', 'a canopy frame with slim posts and a rail across the top, in __part_metal__', 'a sleigh-style frame of __part_wood__ with sides that curve up at both ends', 'a storage frame of __part_wood__ with deep drawers beneath', 'a frame of reclaimed timber planks with a rough finish', 'a Japanese-style low frame of pale __part_wood__ with clean joints'],
 'feet': ['short square blocks', 'tall tapered legs', 'turned legs with a round ball foot', 'metal legs with rubber caps', 'bun feet', 'castor wheels', 'no visible feet, the base sits on the floor', 'curved legs with a claw-and-ball foot'],
 'mattress': ['a thick firm mattress with a plain white cover', 'a thin futon mattress folded flat', 'a pillow-top mattress with stitched squares', 'a medium mattress with a quilted cover in __comp_colour__', 'an old mattress with a worn ticking stripe'],
 'bedding': ['a plain white cotton duvet with two pillows', 'a patchwork quilt in warm colours and a bolster', 'crisp linen sheets and a folded blanket in __comp_colour__', 'a thick wool blanket over striped sheets', 'a satin cover and several large pillows in __comp_colour__', 'a rumpled duvet in __comp_colour__ with the pillows pushed to one side', 'neatly tucked hospital-corner sheets and a single flat pillow', 'a floral print duvet cover with matching pillowcases', 'a stack of cushions and a fur-look throw'],
 'size': ['a single bed', 'a small double bed', 'a standard double bed', 'a queen-size bed', 'a king-size bed'],
},
'chair': {
 'seat': ['a flat wooden seat of __part_wood__', 'a round padded seat in __part_fabric__', 'a woven rush seat', 'a woven cane seat', 'a moulded plastic seat in __comp_colour__', 'a square upholstered seat in __part_fabric__ with piping', 'a saddle-shaped carved seat of __part_wood__', 'a thin metal seat pierced with holes, in __part_metal__', 'a deep cushioned seat in __part_fabric__'],
 'back': ['a straight back of vertical slats', 'a curved spindle back', 'a tall ladder back with five horizontal rails', 'a low rounded back', 'a high upholstered back in __part_fabric__', 'a back of woven cane in an oval frame', 'a back of a single curved plank', 'a wing back that curves forward at the sides', 'a back of thin bent metal rods in __part_metal__', 'no back at all, it is a backless chair'],
 'arms': ['no arms', 'short slim wooden arms', 'wide padded arms in __part_fabric__', 'curved open arms of __part_wood__', 'metal arms in __part_metal__ with a plastic cap'],
 'legs': ['four straight square legs', 'four tapered legs that splay outward', 'four turned legs', 'two sled-style legs in __part_metal__', 'a single central pedestal on a cross base', 'four slim metal legs with rubber feet', 'curved cabriole legs', 'four peg legs set into the seat', 'a swivel base on five wheels'],
 'extras': ['a footrest bar between the front legs', 'a rail between the legs for stability', 'a loose seat cushion tied to the back', 'no extra details', 'a small carved detail at the top of the back'],
},
'sofa': {
 'back': ['a straight, low back', 'a high rolled back', 'a back of three big soft cushions', 'a tufted back with deep buttons', 'a camelback with a gentle hump in the middle', 'a low rounded back that curves around the seat', 'a back with a tight, smooth upholstery panel'],
 'arms': ['no arms', 'low square arms', 'wide padded rolled arms', 'slim wooden arms of __part_wood__', 'high flared arms with piping', 'curved scrolled arms'],
 'cushions': ['three loose seat cushions in the same fabric', 'one long tight seat with no loose cushions', 'deep, plump feather-filled cushions', 'firm foam cushions with sharp edges', 'cushions in __comp_colour__ and a few patterned scatter cushions'],
 'base': ['short wooden legs of __part_wood__', 'tall tapered legs in __part_wood__', 'metal legs in __part_metal__', 'a skirted base that hides the legs', 'a solid plinth base', 'curved legs with a small brass cap'],
 'shape': ['a straight two-seat sofa', 'a straight three-seat sofa', 'an L-shaped corner sofa', 'a curved sofa that bends around a corner', 'a chaise sofa with a long extended seat at one end', 'a deep modular sofa made of separate blocks'],
 'cover': ['upholstered in __part_fabric__ in __comp_colour__', 'upholstered in __part_fabric__ in a muted shade', 'covered in a bold pattern woven in __comp_colour__', 'upholstered in worn __part_fabric__ with a soft shine on the arms'],
},
'table': {
 'top': ['a rectangular top', 'a round top', 'an oval top', 'a square top', 'a top with rounded corners', 'a top with a live-edge wavy side', 'a long narrow top', 'a hexagonal top', 'a top with two fold-down leaves'],
 'top_material': ['solid __part_wood__', 'planks of __part_wood__ with visible joins', 'a smooth glass sheet', 'white marble with grey veining', 'black laminate', 'a tiled top in small coloured squares', 'a stone slab', 'woven cane under glass', 'pale painted wood with a worn edge'],
 'edge': ['a plain square edge', 'a rounded edge', 'a bevelled edge', 'a thick chunky edge', 'a thin sharp edge', 'a moulded rim'],
 'legs': ['four straight square legs', 'four turned legs', 'four splayed tapered legs', 'two solid slab ends', 'a single central pedestal on a wide base', 'trestle legs joined by a long beam', 'hairpin legs in __part_metal__', 'an X-shaped base', 'a tripod base of curved legs', 'a metal frame in __part_metal__ with slim legs'],
 'extras': ['no drawers or shelves', 'a single shallow drawer in the apron', 'a lower shelf between the legs', 'two small drawers side by side', 'a hinged leaf at each end'],
 'size': ['small, seating two', 'medium, seating four', 'large, seating six', 'very long, seating ten'],
},
'desk': {
 'top': ['a plain rectangular top', 'an L-shaped top', 'a wide curved top', 'a top with a raised back ledge', 'a sloped drawing top that tilts', 'a small compact top'],
 'storage': ['a single shallow centre drawer', 'a tower of three drawers on the right', 'drawers on both sides and a knee space in the middle', 'an open shelf under the top', 'no storage at all', 'a roll-down lid that closes over the top'],
 'base': ['four slim legs in __part_wood__', 'two panel ends in __part_wood__', 'a metal frame in __part_metal__ with adjustable feet', 'a height-adjustable column on a wide foot', 'trestle legs'],
 'extras': ['a pigeonhole shelf unit on top', 'a cable hole with a grommet', 'a pen tray in the front edge', 'a built-in lamp bracket', 'no additional details'],
 'material': ['solid __part_wood__', 'laminate in __comp_colour__', 'glass on a metal frame', 'painted metal', 'veneer over board'],
},
'credenza': {
 'body': ['a long low body of __part_wood__', 'a tall narrow body of __part_wood__', 'a wide body with a stepped top', 'a body with a rounded front corner', 'a plain boxy body painted in __comp_colour__'],
 'doors': ['sliding doors in __part_wood__', 'hinged panel doors', 'doors with woven cane panels', 'glass-fronted doors', 'doors with vertical fluting', 'no doors, open compartments', 'tambour doors that roll sideways'],
 'drawers': ['no drawers', 'a row of three shallow drawers', 'two deep drawers on one side', 'four drawers in the centre', 'a single long drawer across the top'],
 'handles': ['no handles, with finger grooves', 'round wooden knobs', 'brass pull handles', 'slim black metal bars', 'ring pulls in __part_metal__', 'leather loops'],
 'base': ['four short tapered legs', 'a solid recessed plinth', 'a slim metal frame in __part_metal__', 'bracket feet', 'tall splayed legs'],
 'top': ['a plain flat top', 'a top with a marble inlay', 'a top with a raised rim', 'a glass top', 'a lightly scratched wood top'],
},
'wardrobe': {
 'doors': ['two hinged panel doors', 'three doors, the middle one with a mirror', 'sliding mirrored doors', 'a single tall door', 'sliding plain wood doors', 'louvred doors', 'curtain front on a rail'],
 'frame': ['a frame of __part_wood__ with a carved cornice', 'a plain boxy frame in __comp_colour__', 'a tall frame of reclaimed timber', 'a white painted frame with a thin moulded top', 'a metal rack with an open front'],
 'inside': ['a hanging rail only', 'a hanging rail and two shelves', 'drawers on one side and a rail on the other', 'a full set of shelves', 'a rail above a row of shoe racks'],
 'feet': ['short bun feet', 'tapered legs', 'a plain plinth', 'castor wheels', 'a drawer at the base'],
 'handles': ['ring pulls in __part_metal__', 'glass knobs', 'long metal bars', 'carved wooden handles', 'no handles with push latches'],
},
'bookcase': {
 'frame': ['a frame of __part_wood__', 'a frame of black iron tubes', 'a ladder-style frame leaning against the wall', 'a stepped frame like a staircase', 'a tall plain frame painted in __comp_colour__'],
 'shelves': ['four open shelves', 'six narrow shelves', 'five shelves of varying heights', 'three wide shelves', 'eight shelves in a tall frame'],
 'back': ['an open back', 'a solid back panel', 'a back of woven cane', 'a back with horizontal slats'],
 'doors': ['no doors', 'glass doors on the lower half', 'solid doors at the base', 'glass doors across the whole front'],
 'base': ['a solid plinth', 'short legs', 'a lower cupboard', 'bracket feet'],
},
'stool': {
 'seat': ['a round flat seat of __part_wood__', 'a padded round seat in __part_fabric__', 'a square seat of woven rope', 'a dished moulded seat in __comp_colour__', 'a saddle seat of leather'],
 'legs': ['three splayed legs', 'four straight legs', 'four tapered legs', 'hairpin legs in __part_metal__', 'a single central column on a heavy base', 'folding crossed legs'],
 'footrest': ['a ring footrest', 'a straight footrest bar', 'no footrest', 'a low bar close to the floor'],
 'height': ['a low stool at knee height', 'a counter-height stool', 'a tall bar stool'],
},
'bench': {
 'seat': ['a plain plank seat of __part_wood__', 'a long cushioned seat in __part_fabric__', 'a slatted seat', 'a seat of woven cane', 'a stone seat'],
 'legs': ['two solid slab ends', 'four straight legs', 'trestle legs', 'cast iron ends with curling scrolls', 'metal tube legs in __part_metal__'],
 'back': ['no back', 'a low back of vertical slats', 'a tall upholstered back', 'a curved back rail'],
 'arms': ['no arms', 'a slim arm at each end', 'a scrolled arm at each end'],
 'length': ['short, seating two', 'medium, seating three', 'very long, seating five'],
},
'lamp': {
 'base': ['a round ceramic base', 'a turned wooden base of __part_wood__', 'a tripod base of slim legs', 'a heavy cast brass foot', 'a glass base filled with coloured stones', 'a flat metal disc foot', 'a small woven basket base'],
 'stem': ['a short stem', 'a tall slim stem of __part_metal__', 'a twisting stem', 'a jointed arm with two hinges', 'no visible stem, the shade sits on the base'],
 'shade': ['a pleated fabric shade in __comp_colour__', 'a drum-shaped linen shade', 'a conical metal shade in __part_metal__', 'a paper globe shade', 'a stained-glass shade', 'a wide flat disc shade', 'a tasselled fringe shade'],
 'switch': ['a pull cord', 'a rotary switch on the socket', 'a switch in the cord', 'a push button on the base'],
 'type': ['a table lamp', 'a floor lamp', 'a desk lamp'],
},
}
