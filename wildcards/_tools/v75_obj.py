"""v75 stage C - object builders for the commonest objects found in the Location Inventory that had no wildcard family (item 82).
Each object gets type / material / colour / wear / detail / era pools built from its class, plus _short, _full and _phrase files.
Class pools are shared; each object has hand-written types. Re-runnable: add rows to OBJ."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from famlib import P, slug
COLOUR = P("off-white; cream; matte black; charcoal grey; pale grey; navy blue; forest green; olive green; brick red; faded red; mustard yellow; sky blue; dusty pink; terracotta; brushed silver; dark brown; beige; teal; ivory; two-tone grey and white")
ERA = P("from the 1930s; from the 1950s; from the 1960s; from the 1970s; from the 1980s; from the 1990s; from the 2000s; of a current design; of an old-fashioned design; of a utilitarian wartime design")
CLASSES = {
 'metal': dict(mat="pressed steel; brushed stainless steel; cast iron; galvanised steel; brass; aluminium; chromed metal; enamelled steel; copper; powder-coated steel", wear="new and spotless; lightly scratched; dented at the corners; rusting along the edges; worn bright where hands touch it; spattered with old paint; dulled by years of dust; dripping with condensation; scuffed and fingerprinted; patched with tape", detail="a stamped maker's plate; a row of rivets; a hand-written label; a rubber foot worn flat; a coat of fresh paint over an older one; a chipped enamel edge; a small hinge that no longer lines up"),
 'wood': dict(mat="oak; pine; teak; painted softwood; plywood; laminated chipboard; beech; varnished mahogany; reclaimed boards; bentwood", wear="freshly finished; polished by years of use; stained with rings; scratched and nicked; split along the grain; flaking paint; worn pale where hands rest; warped slightly; marked with carved initials", detail="a brass hinge; a dovetailed corner; a hand-lettered label; a worn handle; a nail head showing through; a thick coat of paint"),
 'plastic': dict(mat="moulded polypropylene; hard grey plastic; translucent plastic; glossy ABS; soft rubbery plastic; laminate sheet; textured black plastic", wear="new and shiny; yellowed with age; cracked at the corner; sticky with grime; scratched and dull; sun-bleached; stained with a coloured residue", detail="a moulded recycling mark; a snapped clip; a peeling sticker; a worn button; a hairline crack; a stack of the same item nearby"),
 'paper': dict(mat="thin newsprint; glossy coated paper; thick card; pale recycled paper; thermal paper; cream laid paper; folded card; photographic paper", wear="crisp and new; creased in the middle; curling at the corners; stained with a coffee ring; torn along one edge; crumpled and flattened again; faded by sunlight; pinned with several holes; written over in pencil", detail="a hand-written note in the margin; a ring stain; a stamped date; a paper clip; a sticky-note flag; a rubber-stamped mark; a folded corner"),
 'textile': dict(mat="coarse hessian; cotton canvas; thin polyester; heavy wool; worn linen; nylon webbing; pale cotton drill; velvet", wear="clean and pressed; creased and rumpled; stained with dark patches; frayed at the edge; faded by washing; pilled with wear; patched in places", detail="a stitched seam; a frayed hem; a metal eyelet; a stitched label; a woven stripe; a repaired tear"),
 'glass': dict(mat="clear glass; green-tinted glass; frosted glass; glazed ceramic; stoneware; white porcelain; moulded glass; pressed glass", wear="sparkling clean; cloudy from washing; chipped at the rim; stained inside; finely crazed; filmed with dust; fingerprinted all over", detail="a screw lid; a paper label peeling away; a printed measuring scale; a rubber seal; a chip at the rim; a moulded pattern"),
 'appliance': dict(mat="enamelled steel and plastic; stainless steel and glass; white-painted metal; moulded plastic with chrome trim; wood-effect laminate and steel", wear="spotless and new; scuffed and fingerprinted; yellowed with age; dented on one side; covered in magnets and notes; stained and sticky; dull and well used", detail="a rubber door seal; a dial worn smooth; a hum and a faint light; a sticker with a service number; a cable looped behind; a drip tray; a magnet collection"),
 'fabricated': dict(mat="painted brick; poured concrete; carved stone; cast concrete; structural steel; dressed timber; glazed tile; plastered masonry", wear="clean and freshly finished; weathered and stained; cracked and patched; chipped at the edges; stained with damp; covered in old posters or paint", detail="a chipped corner; a joint in the surface; a plaque; a bolted fixing; a layer of old paint; a stain running downward"),
}
CMAP = {'M': 'metal', 'W': 'wood', 'P': 'plastic', 'R': 'paper', 'T': 'textile', 'G': 'glass', 'A': 'appliance', 'F': 'fabricated'}
OBJ = """can|M|a drinks can; a paint can with a pressed lid; a food can with a peel-off lid; an aerosol can; an oil can with a long spout; a watering can; a biscuit can with a hinged lid
ticket|R|a paper train ticket; a cardboard raffle ticket; a thermal-printed ticket; a punched tram ticket; a cinema ticket stub; a car park ticket; a ticket in a plastic sleeve
locker|M|a tall steel locker; a bank of half-height lockers; a gym locker with a slatted door; a coin-operated luggage locker; a school locker with a padlock hasp; a dented staff locker
signage|M|a hanging wayfinding sign; a wall-mounted directional sign; an illuminated exit sign; a floor-marking sign; a door plate sign; a freestanding A-board; a sign on a post
napkin|R|a folded paper napkin; a crumpled used napkin; a stack in a napkin dispenser; a napkin tucked under a fork; a napkin printed with a pattern; a napkin torn in half
chart|R|a wall chart pinned with tacks; a clipboard chart; a laminated eye chart; a pinned timetable chart; a flip chart sheet; a hand-ruled chart with coloured pencil lines
newspaper|R|a folded newspaper; a broadsheet spread open; a tabloid; a local free paper; a newspaper in a wooden holder; a newspaper pushed under a door
trolley|M|a shopping trolley; a hospital trolley; a luggage trolley; a tea trolley with shelves; a sack trolley; a library trolley; a cleaner's trolley
radiator|M|a cast iron column radiator; a long panel radiator; a towel rail radiator; a convector heater; a small oil-filled radiator; a radiator with a clothes drying rack
logbook|R|a hardbound logbook; a clipped logbook on a string; a ledger-style log; a visitors' book; a spiral-bound log; a logbook with a broken spine
fridge|A|a retro round-cornered fridge; a tall fridge freezer; an under-counter fridge; a catering fridge with a glass door; a small bar fridge; a fridge with a freezer drawer
jar|G|a glass jam jar; a screw-top storage jar; a ceramic jar with a lid; a pickling jar; a sweet jar with a glass stopper; a preserving jar with a clip lid
photograph|R|a framed photograph; a curled snapshot; a black and white print; an instant photograph; a group portrait photograph; a faded colour print in a frame
cooler|A|a water cooler with a bottle on top; a picnic cooler box; a drinks cooler with a glass door; a wine cooler; a mains-fed water dispenser; a cooler with cone cups
tank|M|a hot water cylinder; a header water tank; a fuel tank; a gas cylinder; a pressurised expansion tank; a storage tank with a gauge
menu|R|a laminated menu; a chalkboard menu; a printed card menu; a folded menu; a menu in a stand; a handwritten menu on a clipboard
channel|F|a drainage channel with a grate; a cable channel in the floor; a gutter channel; a slot channel along a wall; a water channel in the paving
tub|P|a plastic tub with a lid; a metal washtub; a margarine tub; a storage tub; a mop tub on wheels; a bathtub
microphone|M|a handheld microphone; a stand microphone; a lapel microphone; a studio condenser microphone; a lectern gooseneck microphone; a microphone with a foam cover
fireplace|F|a brick fireplace; a marble mantel fireplace; a log burner; a tiled Victorian fireplace; an open hearth; a gas fire in an old surround
cctv|P|a dome camera; a bullet camera on a bracket; a pan-tilt camera; a ceiling camera in a smoked dome; a camera with a cable running down the wall
receipt|R|a thermal receipt; a long till receipt; a carbon copy receipt; a card terminal receipt; a handwritten receipt; a receipt in a pile
fencing|M|chain-link fencing; wooden panel fencing; wrought iron railings; wire mesh fencing; picket fencing; a temporary site fence on stands
tissue|R|a box of tissues; a pocket pack of tissues; a crumpled tissue; a tissue dispenser on the wall; a roll of toilet tissue; a wad of kitchen tissue
sack|T|a hessian sack; a paper sack; a mail sack; a plastic refuse sack; a flour sack; a sack tied at the neck
pole|W|a flagpole; a curtain pole; a barber's pole; a telegraph pole; a scaffolding-style pole; a painted pole with a ring
barrier|M|a crowd barrier; a car park barrier arm; a retractable belt barrier; a folding barrier; a hazard barrier with stripes; a counter barrier
column|F|a stone column; a fluted column; a steel column; a boxed-in column; a round concrete column; a timber post column
clipboard|P|a hardboard clipboard with a sheet; a clipboard with a pencil on a string; a plastic clipboard with a lid; a clipboard hung from a nail; a clipboard with a checklist
charger|P|a phone charger plugged into a wall; a charging dock; a multi-way charger; a laptop charger; a charger with a tangled cable
planter|G|a terracotta planter; a concrete planter; a plastic planter; a long trough planter; a hanging planter; a glazed ceramic planter
generator|A|a portable petrol generator; a standby generator in a cage; a diesel generator on a trailer; a small inverter generator; a rusted old generator
flyer|R|a folded flyer; a stack of flyers; a leaflet stuck to a wall; a flyer for a local event; a photocopied notice; a flyer under a windscreen wiper
sticker|P|a peeling sticker; a warning sticker; a bumper-style sticker; a round price sticker; a sheet of children's stickers; a sticker over a sticker
litter|P|a crisp packet; a flattened drinks can; a plastic bag caught on a fence; a crumpled paper cup; a heap of wrappers; a lone glove
hatch|F|a serving hatch; a loft hatch; a floor hatch with a ring; a pass-through hatch with a shutter; a coal hatch; a ship's hatch with a wheel
handrail|M|a tubular handrail; a wooden handrail; a brass handrail; a wall-mounted handrail; a painted iron handrail; a polished stair handrail
noticeboard|W|a cork noticeboard crowded with papers; a glass-fronted noticeboard; a felt noticeboard; a whiteboard noticeboard; a painted noticeboard with a frame
shed|W|a garden shed; a bike shed; a tool shed; a lean-to shed; a corrugated shed; a potting shed
vent|M|a ceiling vent; an air vent in a wall; a roof vent; a louvred vent; a grille vent with dust; a kitchen extractor vent
packet|R|a crisp packet; a cigarette-style packet; a seed packet; a packet of biscuits; a sugar packet; a packet of tissues
hanger|M|a wire coat hanger; a wooden hanger; a plastic hanger; a padded hanger; a row of hangers; a hanger with clips
pallet|W|a wooden pallet; a stack of pallets; a plastic pallet; a pallet of boxes; a pallet with a broken slat; a pallet used as a shelf
flashlight|P|a torch with a rubber grip; a large lantern torch; a small keyring torch; a head torch; a wind-up torch; a torch on a hook
offering|X|a bowl of fruit; a stick of incense; a bunch of flowers; a small lit candle; a bowl of rice; a folded paper offering
netting|T|fine garden netting; a fishing net; a cargo net; a mosquito net; a safety net; a tennis court net
bracket|M|a shelf bracket; an angle bracket; a wall bracket for a pipe; a bracket holding a TV; a hanging basket bracket; a scrolled iron bracket
reader|P|a card reader on a wall; a barcode reader; a ticket reader; a handheld reader; a fingerprint reader; an e-ticket reader
luggage|T|a suitcase; a holdall; a backpack; a pile of cases; a trunk with straps; a bag on a trolley
drape|T|a heavy velvet drape; a thin voile drape; a stage drape; a hospital privacy curtain; a dust sheet draped over furniture; a drape tied back with a cord
outlet|P|a double wall socket; an outlet with a cable plugged in; an old round-pin socket; an outlet with a multi-way adapter; a cracked wall outlet; a pop-up floor outlet
freezer|A|a chest freezer; an upright freezer; a catering freezer; a small ice-box freezer; a freezer with a thick coat of ice; a freezer full of frozen packages
kiosk|F|a small ticket kiosk; a newspaper kiosk; a touchscreen self-service kiosk; a park kiosk; a market kiosk; a wooden kiosk with a shutter
lectern|W|a wooden lectern; a clear acrylic lectern; a table lectern; a brass eagle lectern; a lectern with a gooseneck lamp; a lectern with a microphone
intercom|P|a wall intercom panel; a door entry intercom with buttons; a handset intercom; a video intercom; a corded desk intercom; a speaker grille intercom
pipework|M|exposed copper pipework; lagged pipework; rusting iron pipework; neat plastic pipework; painted pipework in colour bands; a tangle of old pipework
toiletry|P|a bottle of shampoo; a tube of toothpaste; a bar of soap; a shaving brush; a comb and a razor; a small bottle of lotion
brochure|R|a glossy brochure; a folded leaflet; a stack of brochures in a rack; a spiral-bound brochure; a hand-stapled brochure; a brochure with coffee rings
notepad|R|a pad of ruled paper; a spiral notepad; a notepad with a pen; a notepad by the phone; a sticky-note pad; a notepad torn to the last sheet
projector|A|a ceiling projector; a slide projector; a portable projector on a trolley; a film projector with reels; an overhead projector; a projector with a dusty lens
printer|A|a desktop printer; a large office copier; a label printer; a receipt printer; a printer with a paper tray; a printer with a jammed sheet
ramp|F|a concrete access ramp; a wooden ramp; a portable metal ramp; a loading ramp; a ramp with a handrail; a rubber threshold ramp
wristband|P|a paper wristband; a plastic wristband; a fabric festival wristband; a hospital wristband; a rubber wristband; a cut-off wristband
extractor|A|a kitchen extractor hood; a window extractor fan; a ceiling extractor; a bathroom extractor with a pull cord; an industrial extractor; a greasy extractor
ashtray|G|a glass ashtray; a metal bucket ashtray; a ceramic ashtray; a pub ashtray with a logo-free rim; a stone ashtray; a full ashtray
cupboard|W|a painted kitchen cupboard; a tall larder cupboard; a wall cupboard; a built-in alcove cupboard; a cupboard with a latch; a locked metal cupboard
"""
def build(final=None):
    G = {}; names = []
    for cls, d in CLASSES.items():
        for k in ('mat', 'wear', 'detail'): G['ob_%s_%s' % (cls, k)] = P(d[k])
    G['ob_colour'] = COLOUR; G['ob_era'] = ERA
    for row in OBJ.strip().split('\n'):
        n, c, types = row.split('|'); cls = CMAP[c] if c in CMAP else 'metal'
        if c == 'X': cls = 'paper'
        G['ob_%s_type' % n] = P(types)
        G['ob_%s_material' % n] = ['__ob_%s_mat__' % cls]; G['ob_%s_wear' % n] = ['__ob_%s_wear__' % cls]; G['ob_%s_detail' % n] = ['__ob_%s_detail__' % cls]
        G['ob_%s_short' % n] = ['__ob_%s_type__, in __ob_colour__' % n]
        mat = cls == 'appliance'
        G['ob_%s_phrase' % n] = ['__ob_%s_type__ in __ob_colour__' % n]
        G['ob_%s_full' % n] = ['__ob_%s_type__, in __ob_colour__%s, %s, %s, with __ob_%s_detail__' % (n, ' and made of __ob_%s_material__' % n if mat else '', '__ob_%s_era__' % n, '__ob_%s_wear__' % n, n)]
        G['ob_%s_era' % n] = ERA
        names.append(n)
    G['ob_names'] = names
    for suf in ('short', 'phrase', 'full'): G['ob_any_%s' % suf] = ['__ob_%s_%s__' % (n, suf) for n in names]
    G['v75_ob_entry_points'] = ['ob_any_short', 'ob_any_phrase', 'ob_any_full']
    return G
if __name__ == '__main__': print(len(build()))
