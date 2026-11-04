"""v74 stage C - vehicle interiors (item 73): cockpits, cabins, dashboards, bridges, gondolas. 18 interior classes with shared era, wear, light and view pools.
Genre builds (v75 onward) swap in their own control, material and view pools; this stage keeps wording genre-neutral and brand-free."""
from famlib import P, slug

ERA = P("an early 1920s; a 1930s; a 1950s; a 1960s; a 1970s; a 1980s; a 1990s; a 2000s; a present-day; a 2030s")
WEAR = P("showroom fresh with no marks; lightly used with a few scuffs; heavily worn with cracked and shiny surfaces; sun-bleached with a faded dash; grubby with crumbs and grit in the corners; neglected with dust on every surface; carefully restored with polished metal; stained and sagging; patched with tape and cable ties; cluttered with personal belongings; damp with condensation on the glass; freshly cleaned with a sharp smell of polish")
LIGHT = P("harsh midday sun streaming through the windscreen; soft early morning light; warm low sun at the end of the day; dim blue light before dawn; a wash of dashboard glow in the dark; rain streaking the glass with grey light; bright overcast light; the glow of overhead lamps at night; red and amber instrument lights in the dark; golden hour light from the side window; the flicker of passing lights at night")
VIEW = P("a straight empty road; a wet city street at night; a mountain pass with hairpin bends; a long coastal highway; a rural lane between hedges; a motorway full of traffic; a desert road shimmering in heat; a forest track; a snow-covered road; a harbour wall and a grey sea; a bright runway ahead; clouds filling the glass; a town square seen through a side window; a railway line curving into the distance; a quiet suburban street")
PERSON = P("a driver with both hands on the wheel; a passenger with their feet on the dashboard; a pilot reaching for a switch; a captain gazing out ahead; a driver looking in the mirror; no one, the seats empty; a sleeping passenger in the back; a child looking out of the window; a conductor leaning on a rail; a navigator holding a folded map; a driver with one arm out of the window; a crew member checking a gauge")

CLASSES = {
 'saloon car': dict(layout=P("a two-row cabin with a bench front and a bench rear; a four-door cabin with bucket seats in front; a compact cabin with a short dash; a long cabin with a wide rear seat; a cabin with a column gear shifter and a bench front seat"),
    seats=P("bench seats in cracked vinyl; seats in plush velour; bucket seats in leather with contrast stitching; seats in woven cloth with a bold pattern; seats in tan leather with piping; seats with white seat covers and a folded blanket"),
    dash=P("a wide wooden dashboard with chrome trim; a flat black plastic dashboard with simple dials; a sculpted dashboard with a large central screen; a dashboard with a metal-faced radio and push buttons; a dashboard with a hooded dial pod and a glovebox"),
    controls=P("a large thin-rimmed steering wheel; a leather-wrapped steering wheel with a horn pad; a sporty three-spoke steering wheel with buttons; a column stalk with a turn signal and a light switch; a floor-mounted gear lever with a round knob"),
    instruments=P("a round speedometer with a needle and a fuel gauge; twin round dials with a clock between them; a digital cluster with glowing numbers; a strip speedometer that sweeps across; a row of small warning lights glowing amber"),
    materials=P("brushed metal and wood veneer trim; chrome edging on the vents; hard plastic with a moulded grain; leather on the door cards; cloth on the roof lining; rubber mats on the floor"),
    extras=P("a hanging air freshener; a rosary on the mirror; a pile of parking tickets on the dash; a dog blanket across the back seat; a phone mount on the vent; a box of tissues on the shelf behind the seats; a road map stuffed in the door pocket; fluffy dice")),
 'sports car': dict(layout=P("a tight two-seat cabin with a low roofline; a cockpit with the seats almost on the floor; a snug cabin with a high centre tunnel; a roadster cabin open to the sky; a two-plus-two cabin with tiny rear seats"),
    seats=P("deep racing bucket seats with side bolsters; leather seats with perforated centres; fixed-back seats with harnesses; quilted leather seats in a bold colour; thin seats with a checked cloth insert"),
    dash=P("a low driver-focused dashboard angled toward the seat; a minimal dashboard with exposed metal; a dashboard with a row of toggle switches; a swooping dashboard with a digital screen; a sculpted dashboard with a deep brow over the dials"),
    controls=P("a small thick-rimmed steering wheel with a flat bottom; a short gear lever with a metal gate; a paddle-shifter wheel with buttons; a row of pedals with drilled metal covers; a handbrake lever beside the seat"),
    instruments=P("a large central rev counter with a red line; three deep-set round gauges; a row of small oil and temperature gauges; a bright digital display with a bar tachometer; a mechanical speedometer reaching far past legal speeds"),
    materials=P("carbon fibre trim; bare aluminium panels; suede on the dash top; leather with contrast stitching; rubber-studded floor mats; stripped door cards with a pull strap"),
    extras=P("a roll bar behind the seats; a fire extinguisher bracket; a racing harness; a lap timer taped to the dash; a helmet on the passenger seat; a bundle of tools in the boot opening")),
 'truck cab': dict(layout=P("a tall cab with a bench seat for three; a sleeper cab with a bunk behind the seats; a short cab with a high seat; a wide cab with a flat floor; a cab with a fold-down table"),
    seats=P("a high suspension driver's seat in worn vinyl; a bench seat in checkered cloth; a heavy seat with air suspension; a cracked leather seat held with tape; a seat with a sheepskin cover"),
    dash=P("an upright dashboard crowded with switches; a dashboard with a metal plate and big dials; a flat plastic dashboard with a shelf on top; a dashboard with a radio and a CB microphone clipped on; a plain dashboard with a row of warning lights"),
    controls=P("a huge flat steering wheel at a flat angle; a long gear stick with a pattern on its knob; a tall air-brake lever; a pair of foot pedals with rubber covers; a row of toggle switches in a roof panel"),
    instruments=P("big round gauges for pressure and temperature; a speedometer with a tachograph; a clock and a fuel gauge; a row of illuminated warning symbols; a digital trip computer"),
    materials=P("scuffed vinyl and metal; plastic panels held with screws; rubber matting; checkered cloth; vinyl with a crackled finish; worn carpet over the transmission hump"),
    extras=P("a thermos on the dash; a pile of delivery paperwork; a small shrine of photographs; a hanging tassel; a stack of maps; a blanket on the bunk; a gear-bag; a plastic crate of snacks")),
 'bus': dict(layout=P("a long aisle between rows of paired seats; a double-decker with a staircase at the rear; a bench-lined bus with straps overhead; a school bus with long bench seats; a coach with reclining seats and overhead racks"),
    seats=P("moulded plastic seats in bright colours; seats in patterned moquette; vinyl bench seats in green; padded coach seats with headrest covers; wooden slat seats"),
    dash=P("a driver's cab behind a glass partition; a driver's area with a large fare machine; an open cab with a mirror above the windscreen; a cab with a sliding ticket window"),
    controls=P("a very large flat steering wheel; a tall gear lever on the floor; a row of door control buttons; a pull cord along the windows; a ticket machine on a stalk"),
    instruments=P("a big speedometer in a flat panel; a passenger counter; a row of switches above the windscreen; a destination blind winder; a small round clock"),
    materials=P("bright yellow handrails; wipe-clean floor with a ribbed pattern; formica panels; ribbed rubber floor; frosted windows with a slim opening vent"),
    extras=P("a coin tray; a yellow stop button on a pole; advertising cards above the windows; a route map in a frame; a sticker warning about standing; a patched seat; a folded newspaper left on a seat")),
 'train carriage': dict(layout=P("an open saloon with rows of seats; a corridor with compartments of six seats; a long carriage with seats along the walls; a sleeper with folded bunks; a dining car with tables set for two and four"),
    seats=P("wooden slat seats; faded blue moquette seats; padded seats with antimacassars; leather seats with brass fittings; reversible bench seats with leather straps"),
    dash=P("luggage racks of brass and net above the seats; a sliding corridor door with a frosted window; a wooden table under the window; mirrored panels with advertising; framed pictures of landscapes"),
    controls=P("a leather strap to lower the window; a brass emergency handle behind glass; a pull-down blind; a sliding door latch; a small heating knob under the seat"),
    instruments=P("a station clock on the wall; a notice board with route information; a ticket-checking sign; a printed seat reservation card above each seat; a destination display strip"),
    materials=P("varnished wood panelling; patterned carpet; polished brass; chrome and glass; cream laminate; woven cane luggage nets"),
    extras=P("a dropped glove under a seat; a window cracked open; a newspaper left on the table; a hat on the rack; a suitcase in the aisle; a smeared window with a sticker; a thermos of tea on the table")),
 'tram or subway car': dict(layout=P("a long open car with benches along the sides; a car with rows of paired seats; a narrow vintage tram with wooden seats; a car with large doors and a pole in the centre"),
    seats=P("moulded plastic bench seats; slatted wooden seats; seats with patterned cloth; fold-up seats near the doors"),
    dash=P("a driver's cab behind a glass screen; a simple panel with a dead-man's handle; a dash with a few lit buttons; a cab visible through a window in the front"),
    controls=P("a brass controller lever; a vertical handrail from floor to ceiling; hanging straps; a bell cord; a button panel for the doors"),
    instruments=P("a route map strip above the door; a lit stop display; a speed dial; a destination roll; a row of warning lights in the cab"),
    materials=P("steel poles and handles; ribbed rubber floor; wood-grain laminate; scratched windows with etched initials; ceiling lights in a strip"),
    extras=P("crushed ticket stubs on the floor; advertising panels above the windows; a mix of passengers' bags; a sticker about priority seats; a forgotten umbrella; a worn spot in the floor by the doors")),
 'light aircraft cockpit': dict(layout=P("a snug two-seat cockpit with a big windscreen; a four-seat cabin with a wide dash; a tandem cockpit with seats in a row; an open cockpit with a small windscreen; a high-wing cabin with window views downward"),
    seats=P("padded seats in grey cloth; tan leather seats with a lap belt; basic bucket seats with a harness; seats with sheepskin covers; thin seats with a shoulder harness"),
    dash=P("an instrument panel with six round dials in two rows; a panel with a central radio stack; a glass-cockpit screen above a column of switches; a wooden panel with a few simple dials; a panel with handwritten placards"),
    controls=P("a central control yoke with a bar for the thumbs; a joystick between the knees; a throttle knob and a mixture knob; rudder pedals with toe brakes; trim wheels beside the seat"),
    instruments=P("an airspeed indicator and an altimeter; an artificial horizon with a spinning ball; a compass floating in liquid; a rev counter and an oil pressure gauge; a small clock and a fuel gauge with a red warning line"),
    materials=P("bare aluminium and painted metal; grey plastic panels with screws; padded vinyl; scuffed fabric headliner; stitched leather on the yoke"),
    extras=P("a clipboard with a checklist; a pair of headsets hanging on hooks; a folded chart on the dash; a pen on a string; a sectional map in a pocket; a pair of sunglasses on the panel; a thermos")),
 'airliner flight deck': dict(layout=P("a two-seat flight deck with a centre pedestal; a flight deck with a jump seat behind; a crowded deck with an engineer's station; a modern flight deck with rows of screens; a narrow deck with sliding windows"),
    seats=P("heavy adjustable seats in grey fabric; seats with four-point harnesses; pilot seats with sheepskin covers; leather seats with armrests"),
    dash=P("a wall of switches overhead; a main panel with six screens; a glare shield with a mode panel; an older panel with dozens of dials; a central pedestal with throttles and radios"),
    controls=P("a pair of control yokes; side-mounted sticks; a bank of throttle levers; a flap lever with a gate; a rudder trim knob; a row of toggles and guarded switches"),
    instruments=P("crowded rows of round dials; large colour screens showing a moving map; a flat horizon display; engine gauges in a vertical column; an old analogue artificial horizon"),
    materials=P("grey and black plastic panels; padded leather; dark carpet; clear plastic switch covers; cloth sun visors"),
    extras=P("a laminated checklist; a pair of sunglasses clipped to a visor; a paper cup of coffee on the pedestal; a tablet on a mount; flight bags behind the seats; a printed route chart")),
 'airliner cabin': dict(layout=P("a long cabin with three seats on each side; a wide-body cabin with two aisles; a narrow cabin with two plus two seating; a cabin with a curtain between classes; a cabin full of rows with overhead bins"),
    seats=P("blue cloth seats with headrest covers; grey leather seats with a tray table; fully flat seats in a pod; seats with a seat-back screen; seats with striped woven fabric"),
    dash=P("overhead bins with rounded doors; a ceiling with a row of lit signs; curved sidewalls with oval windows; a galley at the back with trolleys; a curtain dividing the front"),
    controls=P("a call button above each seat; a reading light switch; a fold-down tray table; a window shade that slides; an overhead air nozzle"),
    instruments=P("a lit seatbelt sign; a screen showing a flight map; a lit exit sign; a row of lit signs reading no smoking; a lit call light"),
    materials=P("moulded plastic sidewalls; patterned carpet; textured fabric; beige and white panels; soft ceiling light in a blue tint"),
    extras=P("a blanket and a pillow in plastic; a paper cup on a tray; a magazine in a seat pocket; a headset in a pouch; a crumpled napkin; a passenger asleep with a hood up")),
 'helicopter cockpit': dict(layout=P("a bubble cockpit with side-by-side seats; a rescue helicopter with a wide cabin behind; a military cockpit with a tandem layout; a small two-seat cabin with a huge canopy"),
    seats=P("padded seats with four-point harnesses; seats with armour plating; basic seats in grey fabric; seats with sheepskin covers"),
    dash=P("a panel of round gauges; a panel with rows of lit buttons; a glass screen cluster; a compact panel with a small compass"),
    controls=P("a cyclic stick between the knees; a collective lever beside the seat; foot pedals for the tail rotor; a row of switches on the ceiling; a radio panel"),
    instruments=P("a torque gauge and a rotor speed gauge; a small artificial horizon; a vertical speed indicator; a fuel gauge and a clock"),
    materials=P("bare metal; painted aluminium; padded vinyl; grey plastic; reinforced canvas"),
    extras=P("a hoist control box; a pair of binoculars on a hook; a flight helmet on a bracket; a rolled map; a first aid kit in the corner; a headset hanging from the ceiling")),
 'yacht or boat helm': dict(layout=P("an open cockpit with a wheel at the stern; a small cabin with a helm to one side; a flybridge with a high seat; a sail cockpit with winches and lines; a pilothouse with a large window"),
    seats=P("bench seats of teak slats; white vinyl bolster seats; folding canvas seats; a bolted swivel seat; padded cushions in striped cloth"),
    dash=P("a varnished wooden panel with brass gauges; a fibreglass console with screens; a panel with toggle switches in a row; a hinged chart table below the windows; a compass on a stand"),
    controls=P("a wooden wheel with a polished rim; a single lever throttle; a chrome wheel with spokes; a tiller of polished wood; a bank of winches and cleats"),
    instruments=P("a brass compass in a gimbal; a depth sounder with a glowing number; a chart plotter screen; a wind speed dial at the mast base; a barometer on the bulkhead"),
    materials=P("teak decks and rails; brass fittings; white gelcoat; stainless steel rails; varnished mahogany"),
    extras=P("coils of rope; a life ring on a bracket; a cup of tea on a gimballed holder; a logbook and pencil; a pair of binoculars; wet-weather gear on hooks; a neat stack of charts")),
 'ship bridge': dict(layout=P("a wide bridge with windows all round; a bridge with a central chart table; a bridge wing with open sides; a quiet bridge with a single watch officer; a bridge with a raised captain's chair"),
    seats=P("a high captain's chair in leather; a row of tall stools; swivel seats bolted to the deck; a simple wooden bench by the window"),
    dash=P("a long console of radar screens and radios; a wooden console with brass handles; a console with a ship's wheel in the centre; a console under the windows lined with gauges; a bank of engine telegraph levers"),
    controls=P("a brass engine order telegraph; a large wooden wheel; small joystick controls; a pair of engine levers; a voice pipe; a ship's whistle cord"),
    instruments=P("a radar with a sweeping green line; a gyro compass repeater; a rudder angle indicator; a barometer and a clock; a speed log; a depth sounder with a paper trace"),
    materials=P("painted steel; teak decking; brass; rubber matting; varnished wood; non-slip steel plates"),
    extras=P("a mug in a holder; a logbook; a pair of binoculars; a chart pinned with weights; a handheld radio; a pencil tied on a string; a brass clock with a ship's bell")),
 'submarine control room': dict(layout=P("a cramped room with pipes overhead; a low room full of dials and valves; a compact control room with a periscope in the centre; a dim room with red lights; a room with two diving planes controls side by side"),
    seats=P("bolted bucket seats in padded vinyl; simple stools bolted to the deck; seats with lap belts at the planes; a fold-down seat against a bulkhead"),
    dash=P("walls of dials and gauges with painted labels; a console of switches and lit buttons; a grid of valve wheels; a panel of tiny lamps; a dim plot table"),
    controls=P("a pair of aircraft-style wheels for the planes; a rack of brass valve wheels; a periscope with folding handles; a depth control lever; a row of toggle switches under glass"),
    instruments=P("a depth gauge with a trembling needle; a gyro compass; a bubble inclinometer; a bank of pressure gauges; a sonar screen with a glowing sweep; a plotting table with a glass top"),
    materials=P("painted steel; thick rubber seals around hatches; grey painted pipes; riveted plating; wiring bundles in clips; wood-grain laminate panels"),
    extras=P("a hanging microphone; a damp cloth over a pipe; a mug on a hook; a faded photo pinned to a panel; a flashlight on a lanyard; handwritten notes taped to the gauges")),
 'tractor or construction cab': dict(layout=P("a small open cab with a roll bar; a glass cab with a wide door; a single-seat cab with levers at each side; a cab with an air-conditioned seat; a cab with a rear window that opens"),
    seats=P("a moulded rubber seat on a spring; a vinyl suspension seat; a worn cloth seat with a rip; a padded bucket with armrests"),
    dash=P("a plain panel with big knobs; a metal dash painted green; a dash with a few dials and warning lights; a dash with a joystick console to one side"),
    controls=P("a thin steering wheel with a knob; a long gear stick; two hydraulic levers; twin joysticks with buttons; a pair of foot pedals; a throttle hand lever"),
    instruments=P("a tractor-style hour counter; a temperature gauge; a fuel gauge with a cracked glass; a few lit warning lamps; a monitor showing a camera view"),
    materials=P("painted steel; rubber mats; dust-covered plastic; scuffed glass; greasy handles; bare metal worn bright where hands go"),
    extras=P("a thermos in a holder; a toolkit under the seat; a hanging air freshener; a radio with a wire aerial; a jumper on a hook; a wedge of mud on the floor; a grease gun clipped to the wall")),
 'motorcycle cockpit': dict(layout=P("a wide handlebar with a small fairing; a low clip-on bar over a tank; a high touring screen with a pillion behind; a bobber seat with a stripped bar; an upright dirt-bike bar with a number plate"),
    seats=P("a stitched leather saddle; a bench seat in grippy rubber; a solo seat with a tail hump; a padded touring seat with a back rest"),
    dash=P("a round speedometer on a bracket; a small digital display in a pod; a single round dial in a chrome bezel; a tidy dash with a clock and a rev counter; a bare handlebar with no dials"),
    controls=P("a twist throttle grip; a clutch lever with a perch; a front brake lever with a reservoir; a bar-end mirror; a heated grip switch; a row of switches under the thumb"),
    instruments=P("a mechanical speedometer; a rev counter with a red zone; a small fuel warning light; a neutral light glowing green; a bright digital readout"),
    materials=P("chrome and black paint; polished aluminium; rubber grips worn smooth; leather with patina; plastic fairing"),
    extras=P("a helmet hanging from a bar; a luggage strap; a phone mount; a pair of gloves on the tank; a sticker on the screen; a bag clipped to the rack")),
 'steam locomotive cab': dict(layout=P("a cramped cab with a firebox at the front; an open-sided cab with a roof; a cab with a driver's seat on the right; a cab with a fireman's seat on the left"),
    seats=P("a hinged wooden seat; a padded driver's seat bolted to the floor; folding metal seats; a leather-padded bench"),
    dash=P("a boiler face crowded with pipes, valves and gauges; a glowing firebox door; a panel with a water level glass; a rack of brass handles; a coal-dusted shelf"),
    controls=P("a long brake handle; a regulator handle pulling steam; a reversing wheel; a whistle cord overhead; a firing shovel against the wall; a row of brass taps"),
    instruments=P("a steam pressure gauge with a red mark; a water gauge glass; a vacuum brake gauge; a speed recorder; a clock in a brass case"),
    materials=P("black painted iron; brass valves rubbed bright; polished handrails; rough wooden floor with a coal dust coat; riveted plate walls"),
    extras=P("a billycan on the firebox; a coal pile in the tender behind; an oily rag; a lamp hung on a hook; a rolled sheet of timetable; a whistling kettle")),
 'airship gondola': dict(layout=P("a narrow wooden gondola slung under a huge envelope; a covered gondola with large windows; a long cabin with passenger seats; a cockpit with a ship's wheel; an open basket with ropes"),
    seats=P("wicker chairs bolted to the floor; leather bench seats; folding canvas seats; a captain's chair with a rail"),
    dash=P("a brass and wood instrument stand; a long table with charts; a row of wheels and levers; a speaking tube; a panel of dials for gas and altitude"),
    controls=P("a large wooden wheel for the rudder; a smaller wheel for the elevators; a brass lever for ballast; a gas valve handle; ropes coiled on hooks"),
    instruments=P("an altimeter in a brass case; a gas pressure gauge; a compass; a barometer; a drift indicator; a small ship's clock"),
    materials=P("varnished wood; brass fittings; woven wicker; canvas; leather straps; fine rope"),
    extras=P("sandbags hanging as ballast; a folded chart; a sextant in a case; a telescope on a bracket; a small stove; a lantern; a signal flag in a rack")),
 'horse-drawn carriage': dict(layout=P("a two-seat closed cab with a small window; a four-seat coach with facing benches; an open carriage with a folding hood; a driver's box seat high at the front; a post coach with outside seats"),
    seats=P("buttoned leather seats; velvet upholstered benches; wooden bench seats with cushions; worn horsehair seats; seats with embroidered covers"),
    dash=P("a leather-padded front panel; a brass-framed window; a small lamp on a bracket; a luggage rail; a sliding trap to speak to the driver"),
    controls=P("a leather reins hanging from a hook; a brake lever at the side; a coachman's whip in a socket; a leather strap to lower the window; a footboard with a mud scraper"),
    instruments=P("a small pocket watch hung on a hook; a brass lamp; a speaking tube; a clock in the roof; a bell cord"),
    materials=P("polished wood panels; brass handles; velvet curtains; thick leather; painted coachwork with gold pinstripe; woven rugs"),
    extras=P("a lap blanket; a hat box; a pair of gloves on the seat; a small umbrella in a holder; straw on the floor; a carpet bag; a hot brick wrapped in cloth")),
}

ROAD_V = "a straight empty road; a wet city street at night; a mountain pass with hairpin bends; a long coastal highway; a rural lane between hedges; a desert road shimmering in heat; a forest track; a snow-covered road; a quiet suburban street"
VP = {
 'saloon car': (ROAD_V + "; a motorway full of traffic", "a driver with both hands on the wheel; a passenger with their feet on the dashboard; a driver looking in the mirror; no one, the seats empty; a sleeping passenger in the back; a child looking out of the window"),
 'sports car': (ROAD_V, "a driver with both hands on the wheel; a driver looking in the mirror; no one, the seats empty; a passenger holding a map; a driver in gloves changing gear"),
 'truck cab': (ROAD_V + "; a motorway full of traffic; a loading yard at dawn", "a driver with one arm out of the window; a driver with both hands on the wheel; no one, the seats empty; a driver pouring tea from a flask"),
 'bus': ("a wet city street at night; a town square seen through a side window; a rural lane between hedges; a motorway full of traffic", "a driver with both hands on the wheel; a conductor leaning on a rail; a child looking out of the window; a sleeping passenger in the back; no one, the seats empty"),
 'train carriage': ("a railway line curving into the distance; a town square seen through a side window; fields rushing past; a station platform with waiting people", "a conductor leaning on a rail; a sleeping passenger by the window; a child looking out of the window; a passenger reading a newspaper; no one, the seats empty"),
 'tram or subway car': ("a tunnel wall flashing past; a station platform with waiting people; a wet city street at night", "a conductor leaning on a rail; a commuter holding a strap; a sleeping passenger on a bench; no one, the seats empty"),
 'light aircraft cockpit': ("clouds filling the glass; a patchwork of fields far below; a bright runway ahead; a coastline far below", "a pilot reaching for a switch; a pilot gazing out ahead; a passenger pointing at something below; a pilot checking a gauge"),
 'airliner flight deck': ("clouds filling the glass; a bright runway ahead; a sea of cloud at sunset; city lights far below", "a captain gazing out ahead; a first officer reaching for a switch; a pilot checking a gauge; no one, the seats empty"),
 'airliner cabin': ("clouds seen through an oval window; a wing against a sunset; a sea of cloud through a window", "a sleeping passenger in the back; a child looking out of the window; a flight attendant pushing a trolley; no one, the seats empty"),
 'helicopter cockpit': ("a city skyline far below; a mountain valley; a harbour and grey sea; a bright landing pad ahead", "a pilot reaching for a switch; a pilot gazing out ahead; a crew member checking a gauge"),
 'yacht or boat helm': ("a harbour wall and a grey sea; open water with a distant headland; waves breaking over the bow; a quiet marina", "a skipper with both hands on the wheel; a crew member checking a gauge; a navigator holding a folded map; no one, the seats empty"),
 'ship bridge': ("a harbour wall and a grey sea; a line of cargo cranes; a long grey swell to the horizon; a foggy channel with a buoy", "a captain gazing out ahead; a navigator holding a folded map; a crew member checking a gauge; a helmsman at the wheel"),
 'submarine control room': ("dim red light on pipes and valves", "a navigator holding a folded map; a crew member checking a gauge; a captain gazing at a periscope; a helmsman at the wheel"),
 'tractor or construction cab': ("a ploughed field stretching ahead; a muddy building site; a farm track between hedges; a quarry floor", "a driver with one arm out of the window; a driver with both hands on the controls; no one, the seats empty"),
 'motorcycle cockpit': (ROAD_V, "a rider in gloves gripping the handlebar; no one, the seat empty; a rider glancing at the mirror"),
 'steam locomotive cab': ("a railway line curving into the distance; a signal gantry ahead; a long embankment in the smoke", "a driver with one arm out of the window; a fireman shovelling coal; a driver checking a gauge"),
 'airship gondola': ("clouds filling the glass; a patchwork of fields far below; a harbour far below", "a captain gazing out ahead; a navigator holding a folded map; a crew member checking a gauge"),
 'horse-drawn carriage': ("a rural lane between hedges; a cobbled street; a town square seen through a side window; a muddy track in the rain", "a coachman on the box; a passenger looking out of the window; a child looking out of the window; no one, the seats empty"),
}
OLD_ERA = {'steam locomotive cab': "an early 1900s; a 1920s; a 1930s; a 1940s; a 1950s", 'airship gondola': "a 1920s; a 1930s", 'horse-drawn carriage': "an 1820s; an 1850s; an 1880s; an early 1900s"}

def build(final=None):
    G = {}; refs = []
    G['vint2_era'] = ERA; G['vint2_wear'] = WEAR; G['vint2_light'] = LIGHT; G['vint2_view'] = VIEW; G['vint2_person'] = PERSON
    G['vint2_types'] = list(CLASSES)
    for t, d in CLASSES.items():
        s = slug(t)
        for k, v in d.items(): G['vint2_%s_%s' % (s, k)] = v
        G['vint2_%s_view' % s] = P(VP[t][0]); G['vint2_%s_person' % s] = P(VP[t][1])
        if t in OLD_ERA: G['vint2_%s_era' % s] = P(OLD_ERA[t])
        G['vint2_%s_short' % s] = ['The inside of %s %s: %s, with %s.' % ('an' if t[0] in 'aeiou' else 'a', t, '__vint2_%s_layout__' % s, '__vint2_%s_dash__' % s)]
        G['vint2_%s_prompt' % s] = ['The inside of %s %s, from %s era. The layout is __vint2_%s_layout__. The seats are __vint2_%s_seats__. The dashboard is __vint2_%s_dash__, with __vint2_%s_controls__. The instruments show __vint2_%s_instruments__. The materials are __vint2_%s_materials__. Nearby there is __vint2_%s_extras__. The interior is __vint2_era_wear__.' % ('an' if t[0] in 'aeiou' else 'a', t, '__vint2_%s_era__' % s if t in OLD_ERA else '', s, s, s, s, s, s, s)]
        G['vint2_%s_scene_prompt' % s] = ['__vint2_%s_prompt__ Through the glass is __vint2_%s_view__. The light is __vint2_light__. In view is __vint2_%s_person__.' % (s, s, s)]
        refs.append(s)
    # fix the era/wear join sentence
    for s in refs:
        G['vint2_%s_prompt' % s] = [l.replace(', from  era.', '.').replace('from __vint2_%s_era__ era' % s, 'from __vint2_%s_era__ vehicle' % s).replace('__vint2_era_wear__', '__vint2_wear__') for l in G['vint2_%s_prompt' % s]]
    G['vint2_prompt'] = ['__vint2_%s_prompt__' % s for s in refs]
    G['vint2_scene_prompt'] = ['__vint2_%s_scene_prompt__' % s for s in refs]
    G['vint2_short'] = ['__vint2_%s_short__' % s for s in refs]
    groups = {'road': ['saloon car', 'sports car', 'truck cab', 'bus', 'motorcycle cockpit', 'tractor or construction cab'],
              'rail': ['train carriage', 'tram or subway car', 'steam locomotive cab'],
              'air': ['light aircraft cockpit', 'airliner flight deck', 'airliner cabin', 'helicopter cockpit', 'airship gondola'],
              'sea': ['yacht or boat helm', 'ship bridge', 'submarine control room'], 'old': ['horse-drawn carriage', 'steam locomotive cab', 'airship gondola']}
    for g, ts in groups.items():
        G['vint2_%s_prompt' % g] = ['__vint2_%s_prompt__' % slug(t) for t in ts]
        G['vint2_%s_scene_prompt' % g] = ['__vint2_%s_scene_prompt__' % slug(t) for t in ts]
    G['v74_vint2_entry_points'] = ['vint2_prompt', 'vint2_scene_prompt', 'vint2_road_prompt', 'vint2_rail_prompt', 'vint2_air_prompt', 'vint2_sea_prompt', 'vint2_old_prompt']
    return G
