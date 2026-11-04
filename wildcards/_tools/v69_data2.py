# vehicle classes: car, motorbike, bicycle, skate, rail, boat, air, space, imagined
CLASS_OF = {}
for k in "city_car hatchback saloon estate coupe convertible suv pickup van sports_car supercar muscle_car hot_rod rally_car race_car classic_car limousine microcar offroader kit_car lowrider art_car taxi police_car camper caravan rv".split(): CLASS_OF[k] = 'car'
for k in "golf_cart tuk_tuk rickshaw horse_carriage wagon sleigh".split(): CLASS_OF[k] = 'cart'
for k in "box_truck flatbed dump_truck tanker semi tow_truck fire_engine ambulance refuse_truck cement_mixer food_truck monster_truck tractor_farm combine forklift bus_city bus_coach school_bus jeepney".split(): CLASS_OF[k] = 'truck'
for k in "cruiser_bike sport_bike naked_bike touring_bike adventure_bike scrambler cafe_racer chopper moped scooter_motor dirt_bike".split(): CLASS_OF[k] = 'motorbike'
for k in "road_bicycle mountain_bike gravel_bike city_bike folding_bike cargo_bike bmx recumbent tandem ebike trike".split(): CLASS_OF[k] = 'bicycle'
for k in "kick_scooter electric_scooter unicycle skateboard longboard roller_skates inline_skates hoverboard_self".split(): CLASS_OF[k] = 'skate'
for k in "steam_loco diesel_loco electric_train bullet_train tram subway monorail funicular cable_car handcar".split(): CLASS_OF[k] = 'rail'
for k in "sailing_dinghy yacht_sail speedboat canoe kayak rowing_shell gondola dhow raft jet_ski".split(): CLASS_OF[k] = 'boat'
for k in "motor_yacht fishing_boat ferry cargo_ship tanker_ship tugboat junk longship galleon steamship paddle_steamer hovercraft lifeboat submarine houseboat hydrofoil".split(): CLASS_OF[k] = 'ship'
for k in "airliner prop_plane biplane seaplane bush_plane glider helicopter balloon airship hang_glider paraglider drone supersonic cargo_plane crop_duster autogyro".split(): CLASS_OF[k] = 'air'
for k in "rocket capsule spaceplane rover space_station satellite probe lander".split(): CLASS_OF[k] = 'space'
for k in "flying_car hoverbike steam_airship mech sky_galleon sandcrawler starship cyber_bike retro_future_car wasteland_buggy magic_carpet clockwork_carriage hover_train submarine_city balloon_house".split(): CLASS_OF[k] = 'imagined'
def L(s): return [i.strip() for i in s.split(';') if i.strip()]
STATE = {
'cart': L("parked with the wheels or runners pointing straight ahead; parked with the front wheels turned to one side; moving along at an easy pace; stopped with the lamps lit at dusk; loaded high with goods and tied down; empty with the seat folded forward; covered with a canvas sheet; standing in rain with a hood or canopy raised; standing in snow or mud with a heavy coating; with a wheel off and propped on a block"),
'truck': L("parked with the cab lights on and the front wheels turned; driving with the headlights on; reversing with the reversing light and amber beacon on; parked loaded with the cargo secured by straps; parked empty with the load area open; with the cab door open and the step down; with the cab tilted forward to show the engine; stopped at a depot with the engine running; driving in rain with the wipers on; parked at night with the marker lights glowing; covered in dust after a long job; with a rear door open"),
'ship': L("moored at a quay with ropes tied and fenders out; underway with a bow wave and white wake; at anchor in a calm bay; at a mooring at dusk with the cabin lights glowing; moving slowly through fog with lights on; docking with a tug beside it; being launched down a slipway; sailing in heavy swell with spray over the bow; with the wheelhouse lit at night"),
'car': L("parked with the front wheels turned sharply to the left; parked with the front wheels pointing straight ahead; parked on a hill with the front wheels turned in to the kerb; driving fast along a road with the headlights on; driving slowly with the indicator flashing; stopped at a junction with the brake lights glowing; cornering hard with the body leaning and the outer wheels loaded; drifting round a bend with a trail of tyre smoke; parked at dusk with the tail lights glowing and the cabin lit; parked at night with all lights off; with the hazard lights flashing at the roadside; with the driver door open; with all doors open; with the bonnet raised; with the boot lid raised; with the bonnet and boot both open; with a front wheel off the ground on a jack; being washed, covered in soap suds; covered with a fitted cloth cover; covered in a layer of fresh snow; splashing through a deep puddle; with its windows wound down; with the roof removed or folded away"),
'motorbike': L("leaning over at a steep angle through a bend; parked on its side stand with the handlebars turned to the left; parked on its centre stand with the front wheel straight; riding fast with the headlight on; stopped with one foot down and the engine idling; wheelie with the front wheel raised; with the rear wheel throwing up dirt; parked at dusk with the tail light glowing; with the seat lifted to show the compartment below; with the fuel cap open; with the front wheel removed on a stand; with its engine exposed on a workshop stand"),
'bicycle': L("leaning against a wall with the front wheel turned; on its kickstand with the handlebars straight; being ridden fast with the wheels blurred at the spokes; climbing a hill out of the saddle; locked to a railing with a heavy chain; upside down on its saddle and handlebars with a wheel off; with the front wheel removed and the fork resting on the ground; with a flat rear tyre; with its lights on at dusk; with a basket loaded with shopping; with panniers bulging with luggage; on a workshop stand with the chain exposed"),
'skate': L("rolling fast with the wheels blurring; stopped flat on the ground; upside down with the wheels in the air; mid-jump in the air; tilted on two wheels during a turn; sliding sideways to stop; leaning against a wall; stacked with others in a rack"),
'rail': L("standing at a platform with the doors open; running fast with a blur of motion; arriving with steam rolling along the platform; stopped at a signal with lit headlamps; waiting in a depot with the lights off; crossing a bridge in a curve; passing through a tunnel mouth; being coupled to a line of wagons; covered in snow with ice on the roof; with the pantograph raised under wires"),
'boat': L("moored at a quay with ropes tied; heeled over under full sail; underway with a bow wave and white wake; at anchor in a still bay; at a mooring at dusk with the cabin lights on; being launched down a slipway; lifted out of the water on a hoist; hauled out on a cradle for repairs; surfing down a wave; stopped with the engine off and drifting; moving slowly through fog with lights on; tied to a pier with fenders out"),
'air': L("taxiing on the runway with the landing lights on; taking off with the nose raised; in a steep bank turn; in a level cruise above clouds; landing with the wheels just touching down; parked on the apron with the engine covers on; parked in a hangar with the cowling open; flying low over water; descending with the flaps and wheels out; parked at night with the navigation lights glowing; with the passenger door open and a stair attached; in a loop with a smoke trail"),
'space': L("lifting off with a blaze of exhaust; in orbit above the curve of the Earth; docked with another vehicle; with solar panels fully extended; descending under parachutes; landing on a dusty surface kicking up dust; sitting on the pad before launch with vapour venting; drifting alone in the dark; with its hatch open and an astronaut at the opening; being rolled out on a transporter"),
'imagined': L("hovering above the ground with a glow beneath; flying fast with a streak of light behind; docked or parked at night with the lights glowing; with its main panels open to show glowing machinery; leaving a trail of steam or sparks; landing with its engines kicking up dust; with its doors open and a staircase down; in a dramatic banking turn"),
}
CAMERA = {
'cart': L("a front three-quarter view; a rear three-quarter view; a straight side profile; a low angle from the front; a high angle looking down"),
'truck': L("a front three-quarter view; a rear three-quarter view; a straight side profile; a straight front view; a low angle close to the ground; a high angle looking down; a close detail of the cab"),
'ship': L("a bow three-quarter view; a stern three-quarter view; a straight side profile; a head-on view; a low view from the water; a high view from the quay"),
'car': L("a front three-quarter view; a rear three-quarter view; a straight side profile; a straight front view; a straight rear view; a low angle close to the ground; a high angle looking down; a close detail of one wheel; a close detail of the headlights"),
'motorbike': L("a front three-quarter view; a rear three-quarter view; a straight side profile; a low angle from the front; a view from above and behind the rider; a close detail of the engine"),
'bicycle': L("a front three-quarter view; a rear three-quarter view; a straight side profile; a low angle from the front; a close detail of the drivetrain"),
'skate': L("a three-quarter view from the front; a straight side view; a view from directly above; a low angle from the ground; a close detail of the wheels"),
'rail': L("a front three-quarter view; a straight side profile; a head-on view along the tracks; a view from a platform edge; a high view from a bridge"),
'boat': L("a bow three-quarter view; a stern three-quarter view; a straight side profile; a head-on view; a low view from the water; a view from above looking down at the deck"),
'air': L("a front three-quarter view; a straight side profile; a view from below as it passes overhead; a head-on view; a rear three-quarter view; a view from beside it in the air"),
'space': L("a distant wide view; a close view of the front; a side profile; a view from below; a view from above"),
'imagined': L("a front three-quarter view; a rear three-quarter view; a straight side profile; a low dramatic angle; a high angle looking down"),
}
PERSON = {
'cart': L("sitting on the driver's seat holding the reins or handlebar; walking beside it with a hand on the side; pulling it by the shafts or handles; loading goods onto the back; climbing aboard by the step; sitting in the passenger seat looking out; checking a wheel; resting against it with arms folded"),
'truck': L("standing on the step by the cab door; climbing into the cab; sitting at the wheel looking ahead; checking a tyre with a hand on the wheel; leaning from the cab window talking; strapping down the load; walking round the vehicle on an inspection; directing the vehicle with hand signals; checking a clipboard beside the cab; standing at the open rear door"),
'ship': L("standing at the rail looking out; steering at the helm in the wheelhouse; coiling a rope on the deck; waving from the bow; stepping aboard by a gangway; tying the vessel to a bollard; leaning over the side; standing on the bridge wing with binoculars; working a winch on the deck"),
'car': L("sitting in the driver's seat with both hands on the steering wheel; leaning an elbow on the open window; leaning against the closed door with arms folded; kneeling to check a front tyre; polishing the bonnet with a cloth; sitting on the bonnet with feet on the bumper; standing at the open boot loading a bag; looking into the engine bay under the raised bonnet; changing a wheel with a wrench; pushing the car from behind with both hands; waving from the passenger window; sitting in the back seat looking out; walking away from the parked car with keys in hand; sheltering under an umbrella beside the car; filling the petrol tank at the side"),
'motorbike': L("riding with both hands on the grips and the body leaning forward; sitting on the parked bike with both feet on the ground; standing beside it with a helmet under the arm; kneeling to adjust the chain; putting on a helmet; checking the engine with a spanner; riding with a passenger behind; lifting a leg over the seat to mount; leaning on the seat with arms crossed"),
'bicycle': L("pedalling hard with the body low over the handlebars; sitting upright and riding slowly; standing beside it holding the handlebars; pushing it uphill; carrying it on one shoulder; fixing a flat tyre with the wheel off; locking it to a railing; riding with a child on a rear seat; stopped at a crossing with one foot down; lifting it over a gate"),
'skate': L("riding with knees bent and arms out for balance; mid-jump with the board spinning; sitting on the ground lacing up skates; carrying the board under one arm; pushing off with one foot; stopped with a foot on the tail; crouching low in a downhill tuck; gliding on one foot; landing a jump with arms out"),
'rail': L("standing in the open doorway of the carriage; looking out of a carriage window; waving from the platform; driving from the cab with a hand on the controls; leaning from the footplate; waiting on the platform with a suitcase; walking along the side of the train carrying a lantern; sitting on a bench on the platform; hanging from a strap in a crowded carriage"),
'boat': L("steering at the helm with both hands on the wheel; hauling on a rope; sitting at the stern holding the tiller; standing at the bow looking ahead; rowing with both oars; paddling with a double paddle; tying the boat to a bollard; coiling a rope on the deck; stepping aboard from a pier; leaning over the rail; casting a net over the side; mending a sail on the deck"),
'air': L("sitting at the controls in the cockpit; climbing into the cockpit by a ladder; walking round the aircraft doing a pre-flight check; standing on the wing with a hand on the cockpit; waving from the open door; refuelling from a hose; loading luggage into the hold; standing in front of the nose with arms folded; wearing a headset and holding a clipboard; running towards it with a helmet"),
'space': L("floating at the hatch in a pressure suit; standing beside it in a pressure suit; working on the surface with a tool; walking toward it across dusty ground; looking up at it from the ground; checking a panel on its side; being strapped into a seat inside the cabin; waving through a window"),
'imagined': L("sitting at the controls with a glowing display; standing on top with the wind in the hair; leaning against it with a confident posture; kneeling to adjust a glowing panel; climbing aboard by a ladder; looking up at it in wonder; holding on to a rail as it moves"),
}
GROUP = {
'cart': L("a family riding together; a team loading goods; a crowd of onlookers around it; two drivers talking beside two vehicles"),
'truck': L("a crew loading cargo onto the back; a team of workers unloading pallets; a mechanic and a driver looking under the cab; passengers boarding at the door; a crowd gathered round a food counter"),
'ship': L("a crew working on deck; a crowd on the quay waving it off; passengers standing at the rail; dockworkers securing ropes"),
'car': L("a family loading luggage into the boot; a pit crew changing all four wheels; a crowd gathered around admiring the car; two people pushing a broken-down car; a group of friends squeezed into the seats; a mechanic and a customer looking under the bonnet; a bride and groom stepping into the back seat; a line of people waiting beside a bus"),
'motorbike': L("a group of riders parked side by side; a mechanic and a rider looking at the engine; two riders on a country road; a crowd of onlookers at a bike meet"),
'bicycle': L("a group of cyclists riding in a tight line; a family cycling together with a child seat; a mechanic and a customer at a repair stand; a row of parked cycles with people chatting"),
'skate': L("a group of skaters at a skatepark taking turns; two friends rolling side by side; a crowd watching a trick; a group sitting on the edge of a bowl"),
'rail': L("a crowd boarding at a platform; a family waving goodbye; a group of workers by the track; a line of passengers at a window"),
'boat': L("a crew working together on deck; a family on a picnic aboard; a rowing crew pulling in time; a harbour crowd waving a boat off; fishermen hauling nets"),
'air': L("a ground crew fuelling and checking the aircraft; a line of passengers walking to the stairs; a family waving from the apron; a group of pilots looking at a map by the nose"),
'space': L("a ground crew watching a launch; a crew of astronauts standing in front of the vehicle; engineers checking panels beside it"),
'imagined': L("a crew of travellers climbing aboard; a crowd of townspeople looking up at it; a group of mechanics working on it"),
}
SPECIAL = {
'dump_truck': L("with the bed tipped up and gravel pouring out; with the bed lowered and loaded high; reversing with the amber lights flashing"),
'fire_engine': L("with the ladder extended to full height; with the hoses unrolled and lights flashing; parked at the station with the doors open"),
'tow_truck': L("winching a car onto its flat bed; towing a car with its hook; parked at the roadside with amber lights flashing"),
'ambulance': L("with the rear doors open and a stretcher at the back; racing with blue lights flashing; parked at a hospital entrance"),
'refuse_truck': L("lifting a bin into the rear hopper; compacting waste with the hopper open; driving slowly along a street"),
'cement_mixer': L("pouring concrete down the chute; turning its drum while driving; washing out the chute"),
'food_truck': L("with the serving hatch open and awning out; with strings of lights glowing and a queue; parked with the shutter closed"),
'monster_truck': L("flying over a row of crushed cars; spinning donuts in the mud; with its huge wheels hanging in the air"),
'tractor_farm': L("pulling a plough across a field; towing a trailer of hay bales; parked in a barn with the engine cover open"),
'combine': L("cutting a field of wheat with the header spinning; unloading grain into a trailer; parked in a shed during winter"),
'forklift': L("lifting a pallet high on the forks; carrying a pallet through a warehouse; parked with the forks lowered"),
'horse_carriage': L("with the horses pulling at a trot; with the horses stopped and the driver holding the reins; parked with the horses unhitched"),
'sleigh': L("gliding over fresh snow pulled by a horse; parked in the snow with the lamps lit; sliding fast down a hill"),
'camper': L("with the pop-up roof raised and an awning out; parked at a campsite with the side door open and chairs outside; driving on a mountain road"),
'bus_city': L("at a stop with its doors open and people boarding; driving through traffic with the destination blind lit; parked empty in a depot"),
'school_bus': L("stopped with the stop sign out and red lights flashing; parked in a row at a depot; driving on a country road"),
'sailing_dinghy': L("capsized and being righted; heeled over with the crew leaning out; becalmed with the sail slack"),
'yacht_sail': L("heeled over with the sails full; under power with the sails furled; at a mooring with the sails covered"),
'ferry': L("with the bow door open and cars driving off; crossing with a wake behind it; docked with the ramp down"),
'cargo_ship': L("being loaded by cranes at a port; sailing with a bow wave; in dock with the hull above the waterline"),
'tugboat': L("pulling a large ship with a taut towline; working in a harbour with a spray of water; moored with fenders out"),
'rowing_shell': L("racing with the oars all in the water; resting with the oars flat on the surface; carried on shoulders by the crew"),
'submarine': L("diving with a stream of bubbles; surfacing with water streaming off the hull; docked in a harbour with the hatch open"),
'hovercraft': L("riding on its cushion of air over water with a cloud of spray; resting on the beach with the skirt deflated; coming ashore over mud"),
'jet_ski': L("jumping a wave with spray flying; turning sharply throwing a sheet of water; parked on a beach"),
'airliner': L("at the gate with the stairs attached and lights on; rotating for take-off with the nose up; on final approach with the wheels and flaps down"),
'helicopter': L("with the rotors spinning on a helipad; hovering low above a field with grass flattened; with the door open and a winch lowered"),
'balloon': L("being inflated with the burner roaring and the envelope half full; floating at altitude above a valley; landing with the basket tilting"),
'airship': L("moored to a tall mast; floating over a city; being walked into a hangar by ground crew"),
'glider': L("being towed up by a rope; soaring along a ridge; landing on a grass strip"),
'biplane': L("doing a loop with a smoke trail; parked on grass with the propeller still; taking off from grass"),
'seaplane': L("taking off from water with spray; moored at a dock; landing on a calm lake"),
'drone': L("hovering with the propellers blurred; landed on the ground with the lights on; carrying a package"),
'rocket': L("lifting off with a long blaze of flame; standing on the pad in floodlights; separating from its first stage"),
'capsule': L("descending under parachutes; floating in the sea after splashdown; docked with a station"),
'rover': L("tracking across a dusty plain with its robotic arm extended; parked on a ridge with solar panels out; casting a long shadow at sunset"),
'space_station': L("in orbit with the Earth below; with a docked capsule; passing in front of the sun"),
'spaceplane': L("gliding down towards a runway; sitting on a launch stack; rolling to a stop on a runway"),
'lander': L("touching down in a cloud of dust; standing alone on the surface with an astronaut beside it; with the ladder extended"),
'cable_car': L("rising over a valley between pylons; arriving at a station; swaying in strong wind"),
'funicular': L("rising up a steep slope with the other car coming down; stopped at the top station; at the bottom station with the doors open"),
'steam_loco': L("pulling out of a station in clouds of steam; standing with the fire door open and glowing; crossing a stone viaduct"),
'tram': L("curving round a city corner with the bell ringing; stopped with the doors open; passing in a street at night with lit windows"),
'bullet_train': L("rushing past at speed with a blur; waiting in a station; emerging from a tunnel"),
'mech': L("striding forward with one foot lifted; kneeling for repairs with panels open; standing in a ruined street"),
'sky_galleon': L("sailing through clouds with full sails; docking at a floating island; firing a flare into a stormy sky"),
'starship': L("departing a space dock with engines glowing; passing a planet; docked at a station"),
'flying_car': L("hovering above a city street with the wheels tucked up; taking off from a rooftop pad; landing in a car park"),
'magic_carpet': L("flying over a desert at dusk; hovering with a person sitting cross-legged; gliding among minarets"),
}
PAINT_COLOUR = L("signal red; deep burgundy; candy-apple red; coral orange; sunflower yellow; mustard gold; lime green; British racing green; forest green; sage green; mint green; teal; turquoise; powder blue; sky blue; royal blue; midnight blue; navy blue; lavender; deep purple; magenta pink; dusty rose; cream; ivory white; pearl white; light grey; gunmetal grey; charcoal; jet black; copper brown; chocolate brown; sand beige; olive drab; military khaki; silver; gold; bronze; two colours split along the beltline; a fade from orange to purple; a fade from blue to green")
PAINT_FINISH = L("a high-gloss solid colour; a metallic flake that sparkles in the sun; a pearlescent finish that shifts between two tones; a matt finish with no shine; a satin finish with a soft sheen; a colour-shifting finish that changes with the angle; a candy finish with deep translucent colour over a metallic base; a polished mirror chrome wrap; a brushed bare metal finish; a flat primer grey; a hand-painted finish with visible brush strokes; a faded patina with worn paint and bare metal showing through; a weathered finish with chalky oxidised paint; a vinyl wrap with a slight texture; a carbon fibre weave; a wood-grain panel finish; a rough-textured utility coating")
PAINT_EFFECT = L("twin racing stripes running the length of the body; a pinstripe line along the side; painted flames licking back from the front; a number in a white circle on the door; a chequered flag band; a dazzle camouflage pattern; a woodland camouflage pattern; a pattern of small stars; gold leaf lettering on the doors; an airbrushed mural of a landscape on the side; a pattern of fine scallops in a contrasting colour; a faded sunburst on the bonnet; a pattern of bold geometric shapes; a hand-lettered sign-writing panel; a set of small decals and badges from travels; large diagonal hazard stripes; a mirror-finish pinstripe; a swirling paisley pattern; a splatter of paint drips; a plain finish with no markings")
DMG = {
'car': ("a few fine scratches along the door and a small dent in the wing; a stone chip pattern on the bonnet and a scuffed bumper corner", "a long deep scratch down one side, a dented door and a cracked headlight; a crumpled wing, a hanging bumper and a missing wing mirror", "a crumpled front end with the bonnet folded, a shattered windscreen, flat tyres and torn panels"),
'motorbike': ("light scratches on the tank and a scuffed footpeg", "a dented tank, a cracked fairing and a bent handlebar", "a bent frame, a broken fairing, a missing mirror and a twisted front wheel"),
'bicycle': ("light scratches on the top tube and a scuffed saddle", "a bent wheel, a loose chain and a cracked mudguard", "a buckled frame, a collapsed wheel and a snapped chain"),
'boat': ("light scuffs on the hull and some chipped varnish", "a long gouge along the hull, a torn sail and a cracked window", "a hole in the hull, a broken mast and water in the cabin"),
'air': ("light scratches on the paint and a stained nose cone", "a dented wing edge, a cracked cockpit window and a missing panel", "a torn wing, a collapsed landing gear and a broken propeller"),
'rail': ("light scratches along the carriage side and some stains", "dented panels, a broken window and flaking paint", "a derailed carriage, torn roof panels and shattered windows"),
}
VSTRENGTH = ('light', 'moderate', 'heavy')
VINT = {
'car': {
 'dashboard': L("the dashboard with round analogue dials, a thin steering wheel and a chrome-edged radio; a wide modern dashboard with a large touch screen and a flat-bottomed steering wheel; a plain dashboard of moulded plastic with a few switches and a simple speedometer; a wooden dashboard with brass-ringed gauges and a large thin steering wheel"),
 'seats': L("front bucket seats in black leather with red stitching; a wide bench seat in cracked brown vinyl; rear seats in grey cloth with seat belts and a fold-down armrest; sports seats with high side bolsters and a harness"),
 'trunk': L("an open boot holding a suitcase, a spare wheel and a folded blanket; an empty boot with carpeted floor and the spare wheel under a panel; a boot packed with shopping bags and a toolbox; a pickup bed with straps, a toolbox and a bundle of timber"),
 'engine': L("an open bonnet showing a large engine block with a chrome air filter and coloured hoses; an engine bay of a modern car covered by a plastic engine cover with a battery to one side; a tidy engine bay with polished metal parts and braided hoses; a messy engine bay with oil stains and loose wires"),
 'detail': L("a close view of the gear lever and the centre console; a close view of the pedals and the driver's footwell; a close view of the steering wheel and instrument cluster; a close view of the door panel with window winder; a close view of the wheel, brake disc and caliper; a close view of the headlight and grille; a close view of the exhaust pipes at the rear; a view of the underside of the car on a workshop lift"),
 'trim': L("black leather; tan leather; red leather; grey cloth; striped cloth; cracked vinyl; wood veneer panels; carbon fibre panels; brushed aluminium; quilted leather; sheepskin seat covers; plain rubber mats"),
},
'motorbike': {
 'dashboard': L("the handlebars with a single round speedometer and a chrome mirror; the cockpit with a digital display and switch gear on both grips; the handlebars with two analogue dials and a rubber-gripped throttle"),
 'engine': L("a close view of an air-cooled twin engine with cooling fins and chrome pipes; a close view of a compact water-cooled engine with hoses and a radiator; the exposed engine with the side cover removed"),
 'detail': L("the tank with a painted badge and the saddle; the chain, sprocket and rear wheel; the exhaust pipe and silencer; the front fork and brake disc; the rear suspension and swing arm; the headlight and mirrors"),
 'trim': L("black leather seat; worn tan leather seat; ribbed seat in grey; chrome-plated parts; brushed aluminium parts; matt black parts"),
},
'bicycle': {
 'detail': L("the chain, rear sprockets and rear derailleur; the front wheel, fork and brake; the saddle and seat post; the handlebars, grips and brake levers; the crank, pedals and chainring; the frame head tube with the badge; a wicker basket on the front rack; a leather saddlebag"),
 'trim': L("a brown leather saddle; a black gel saddle; wrapped tape on the handlebars; cork grips; chrome mudguards; a bell; a basket of woven cane"),
},
'skate': {
 'detail': L("the underside of the deck with the metal trucks and the wheels; the grip tape top with scuffs; a close view of the wheels and bearings; the front wheels and toe stop of the skate; the laces and boot of the skate; the brake pad and wheel frame of the inline skate; the folding hinge of the kick scooter"),
 'trim': L("black grip tape with scratches; a printed deck graphic; bright urethane wheels; white leather boots; pompoms on the laces; scuffed toe caps"),
},
'rail': {
 'cab': L("the driver's cab with a regulator handle, brake valve and a window onto the track; the footplate of a steam engine with a glowing firebox, pressure gauges and levers; a modern cab with a desk of screens and a single control lever"),
 'saloon': L("a passenger carriage with rows of cushioned seats, luggage racks overhead and wide windows; a commuter carriage with bench seating and grab poles; a first-class compartment with plush seats and a small table; a sleeping compartment with a folded bunk and a washbasin"),
 'detail': L("the wheels and rods of a steam engine; the bogies and axles under the carriage; the coupling between two carriages; the pantograph on the roof; the front lamp and number plate"),
 'trim': L("green patterned moquette; red leather; polished wood panels; brass fittings; plain grey plastic panels; embroidered antimacassars"),
},
'boat': {
 'cabin': L("a wooden cabin with a bunk, a small table and a lantern; a modern cabin with a double berth and white panels; a galley with a small stove and hanging pans; a wheelhouse with a large wheel, a compass and a radar screen; an engine room with a large engine, pipes and gauges"),
 'deck': L("the deck with coils of rope and a winch; a teak deck with a bench and cushions; the bow with an anchor and chain; the stern with a tiller and fishing gear"),
 'detail': L("the hull seen from the waterline; the propeller and rudder; the sails and rigging; a close view of the helm and compass"),
 'trim': L("polished teak; white painted wood; brass fittings; faded cotton cushions; stainless steel rails; worn rope"),
},
'air': {
 'cockpit': L("a light aircraft cockpit with round gauges, a control yoke and two seats; an airliner flight deck with rows of screens, a central pedestal and two seats; an open biplane cockpit with a leather helmet hanging on the stick; a helicopter cockpit with a collective lever and a windscreen; a glider cockpit with a reclined seat and a single yoke"),
 'cabin': L("an airliner cabin with rows of seats, overhead lockers and oval windows; a small plane cabin with four leather seats and a narrow aisle; a cargo hold with strapped crates and a rail floor; a private jet cabin with wide leather seats and a table"),
 'detail': L("a close view of the propeller and spinner; a close view of the engine under the cowling; the landing gear and tyre; the wing tip with a navigation light; the tail fin with a number; the nose with an instrument probe"),
 'trim': L("worn grey leather; blue cloth seats; polished metal; painted instrument panels; leather straps; a cream-painted panel"),
},
'space': {
 'cabin': L("a capsule interior with three couches, a panel of switches and small round windows; a station module with handrails, cables and floating items; an airlock with suits hanging on the walls; a flight deck with screens and a joystick"),
 'detail': L("a close view of the heat shield tiles; the engine nozzles; the docking port; the solar panel hinge; the landing legs; the wheel and suspension of a rover"),
 'trim': L("gold insulation foil; white painted panels; blue cloth lining; metal handrails; thick cable looms"),
},
'imagined': {
 'cabin': L("a cockpit with glowing curved panels and a single seat; a brass-fitted bridge with a large wooden wheel and dials; a plush cabin with floating displays and soft light; a cramped cabin with patched wires and tape; a bright white cabin with a transparent floor"),
 'detail': L("glowing engine coils behind a glass panel; a close view of the hover thrusters; the steering wheel made of brass and leather; a close view of the controls with mismatched switches"),
 'trim': L("polished brass; glowing blue light strips; patched leather; white moulded panels; woven carpet"),
}}

VINT['ship'] = VINT['boat']
DMG['truck'] = DMG['car']; DMG['ship'] = DMG['boat']

DMG['cart'] = ('light scratches and chipped paint on the side panels', 'a cracked wheel rim, a split board and a torn cover', 'a broken axle, a collapsed side and a wheel missing')
