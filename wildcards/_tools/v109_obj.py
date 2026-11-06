"""v109 - object builders for the commonest objects in the full Location Inventory conversion that had no object wildcard (same scheme as v75_obj:
type / material / wear / detail / era pools from the object's class, plus _short, _phrase and _full). The ob_any_* mix files now cover v75 and v109 objects.
Types describe plain, unlettered objects; nothing printed is named (text rules)."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from famlib import P
import v75_obj
OBJ = """mug|G|a tall ceramic mug; a chunky stoneware mug; an enamel camping mug with a rolled rim; a squat tea mug with a chipped handle; a tall travel mug with a lid; a mug with a tea-stained inside
flask|M|a tall steel vacuum flask with a cup lid; a slim insulated flask; a tartan-covered vintage flask; a dented hip flask; a wide-mouthed food flask; a battered flask with a pouring stopper
stove|A|a small camping stove with one burner; a cast-iron wood-burning stove with a glass door; a two-ring gas stove; a pot-bellied stove; a paraffin stove; a squat multi-fuel stove on a hearth
curtain|T|a pair of heavy velvet curtains; thin unlined cotton curtains; a net curtain; a blackout curtain on a track; a shower curtain on rings; a privacy curtain on a ceiling rail
key|M|a long iron mortice key; a small brass door key; a bunch of keys on a ring; a car key fob; a flat steel locker key; a key on a loop of string
pen|P|a clicky ballpoint pen; a chewed ballpoint pen with its cap missing; a fountain pen with a steel nib; a thick marker pen; a pen on a chain; a cheap pen with a see-through barrel
dispenser|P|a wall-mounted soap dispenser; a paper towel dispenser; a hand sanitiser pump on a stand; a water cooler with a stack of cups; a cereal dispenser; a tape dispenser
jug|G|a white enamel water jug; a glass jug with a lip; a stoneware milk jug; a plastic measuring jug; a tall pitcher with ice; a copper jug
pump|M|a cast-iron hand water pump with a long handle; a bicycle track pump; a small electric water pump; a foot pump; a hand-cranked fuel pump; a garden sprayer with a pump handle
piano|W|an upright piano against a wall; a baby grand piano with its lid propped; a battered pub piano; a digital piano on a stand; a small spinet piano; a piano with a fringed shawl over the top
hose|P|a green garden hose on a reel; a coiled fire hose; a canvas hose laid flat; a black rubber hose; a pressure-washer hose; a short hose on a tap
padlock|M|a heavy brass padlock; a steel combination padlock; a small luggage padlock; a rusty padlock on a hasp; a long-shackle padlock; a padlock and chain
handset|P|a corded telephone handset on its cradle; a cordless handset in a charging dock; a two-way radio handset; a wall-mounted intercom handset; a chunky old mobile phone; a payphone handset on a steel cord
couch|T|a sagging three-seater couch; a leather chesterfield couch; a corner couch with cushions; a velvet couch on short legs; a futon couch; a worn couch with a throw over it
tarpaulin|T|a blue plastic tarpaulin with eyelets; a green canvas tarpaulin; a tarpaulin weighed down with bricks; a clear plastic sheet; a tarpaulin stretched as a shelter; a folded grey tarpaulin
whiteboard|P|a plain wall-mounted whiteboard with a pen tray; a whiteboard on a wheeled easel; a small blank whiteboard; a smeared whiteboard wiped clean; a glass board; a portable flip easel
meter|A|an electricity meter with a spinning disc; a gas meter in a cupboard; a water meter under a hatch; a small round dial gauge; a digital meter box; a coin-operated meter
soap|R|a bar of white soap on a dish; a cracked bar of coal tar soap; a liquid soap pump bottle; a sliver of soap; a block of laundry soap; a soap on a rope
dish|G|a shallow ceramic dish; a pie dish; a white serving dish; an enamel baking dish; a small dish of nuts; a glass dish with a lid
broom|W|a stiff yard broom; a soft indoor broom; a besom broom of twigs; a push broom with a wide head; a dustpan and brush; a broom leaning in a corner
urn|M|a tall steel tea urn with a tap; a brass samovar; a stone garden urn; a ceramic urn on a plinth; a coffee urn on a counter; a polished hot-water urn
trough|F|a stone water trough; a galvanised feeding trough; a long washing trough with taps; a concrete planter trough; a wooden hay trough; a horse trough by a gate
dehumidifier|A|a white dehumidifier with a water tank; a small desiccant dehumidifier; an industrial dehumidifier on wheels; a dehumidifier humming in a corner; a dehumidifier with a hose to the drain; a compact dehumidifier on a shelf
hairbrush|P|a paddle hairbrush; a round hairbrush; a bristle hairbrush with a wooden back; a cheap plastic hairbrush clogged with hair; a folding travel hairbrush; a wide-toothed comb and brush
rucksack|T|a large hiking rucksack; a small daypack; a canvas rucksack with leather straps; a battered school-style rucksack; a waterproof roll-top rucksack; a rucksack with a sleeping mat strapped on
shovel|M|a long-handled shovel; a short coal shovel; a snow shovel; a folding army shovel; a garden spade; a rusty shovel stuck in a heap
mop|T|a string mop in a bucket; a flat microfibre mop; a sponge mop; a wringer bucket on wheels; a dry mop; a mop leaning against a wall
hairgrip|M|a few black hairgrips; a bronze bobby pin; a pearl-topped hairgrip; a hair claw clip; a pile of hairgrips in a saucer; a single hairgrip on the floor
extinguisher|M|a red fire extinguisher on a wall bracket; a black-banded foam extinguisher; a fire blanket in a red case; a small car extinguisher; a water extinguisher on the floor; a pair of extinguishers on a stand
detector|P|a round white smoke detector on the ceiling; a carbon monoxide alarm; a motion sensor in a corner; a heat detector; a smoke alarm with a blinking light; a sensor with its cover off
barrel|W|an oak barrel with iron hoops; a blue plastic drum; a steel oil drum; a small rum cask; a rain barrel; a barrel used as a table
bollard|F|a cast-iron bollard; a concrete bollard; a steel post bollard; a retractable bollard; a mooring bollard on a quay; a striped plastic bollard
shutter|M|a roller shutter pulled down; painted wooden window shutters; louvred shutters; a steel security shutter; shutters folded back against the wall; a hatch shutter over a counter
hairband|T|a stretchy hairband; a velvet headband; a scrunchie; a sports headband; a plastic Alice band; a hairband looped around a wrist
comb|P|a black pocket comb; a wide-toothed comb; a tortoiseshell-pattern comb; a metal comb; a barber's comb in a jar of blue liquid; a comb missing several teeth
boiler|A|a white wall-mounted boiler; an old floor-standing boiler; a copper hot-water cylinder in a cupboard; a steam boiler with gauges; a combination boiler with a pressure dial; a boiler with a flue pipe
headphones|P|a pair of over-ear headphones; earbuds with a tangled cable; a headset with a microphone; studio headphones on a hook; wireless earbuds in a case; headphones around a neck
parcel|R|a parcel in plain brown paper tied with string; a cardboard box sealed with brown tape; a padded envelope; a parcel wrapped in plastic; a battered box with dented corners; a stack of parcels
brazier|M|a steel brazier with a fire inside; a perforated drum brazier; a charcoal brazier; a brazier on legs; a glowing brazier at dusk; a cold brazier full of ash
pillow|T|a plump white pillow; a flattened pillow; a pillow in a striped case; a memory-foam pillow; a pillow folded in half; a pair of pillows propped up
decanter|G|a cut-glass decanter with a stopper; a square whisky decanter; a wine decanter with a wide base; a ship's decanter; a decanter on a silver tray; a half-empty decanter
sandwich|R|a sandwich in cling film; a half-eaten sandwich on a plate; a toasted sandwich cut in triangles; a baguette sandwich; a sandwich in a paper bag; a stack of sandwiches on a platter
timer|P|a wind-up kitchen timer; a sand timer; a digital timer with a clip; a plug-in timer switch; a stopwatch on a lanyard; an egg timer
scuttle|M|a coal scuttle with a handle; a copper coal scuttle; a log basket; a brass fire set with poker and tongs; a black iron scuttle; a scuttle full of coal
straw|R|a bale of straw; loose straw on a floor; a paper drinking straw; a bundle of thatching straw; straw bedding; a straw hat on a nail
tent|T|a small dome tent; a canvas bell tent; a large family tent; a frame tent with a porch; a bivouac shelter; a tent pitched in the wind
alarm|A|a round wind-up alarm clock with two bells; a digital alarm clock; a travel alarm clock; an alarm clock knocked on its side; a radio alarm clock; an alarm bell on a wall
controller|P|a game controller; a TV remote; a set of remote controls; a wired controller with a long cable; a pair of controllers on a sofa; a joystick
carrier|P|a plastic pet carrier; a wicker pet basket; a canvas tote; a bike carrier rack; a roof box carrier; a cool box
trap|M|a wooden mouse trap; a humane trap cage; a lobster pot; a sticky fly paper strip; a wasp trap jar; a rat trap in a corner
coil|M|a coil of rope; a coil of electric cable; a coil of wire; a hose coil; a reel of extension cable; a loose coil of chain"""
def build(final=None):
    G = {}; names = []
    base = v75_obj.build()
    for row in OBJ.strip().split('\n'):
        n, c, types = row.split('|'); cls = v75_obj.CMAP[c]
        G['ob_%s_type' % n] = P(types)
        G['ob_%s_material' % n] = ['__ob_%s_mat__' % cls]; G['ob_%s_wear' % n] = ['__ob_%s_wear__' % cls]; G['ob_%s_detail' % n] = ['__ob_%s_detail__' % cls]
        G['ob_%s_short' % n] = ['__ob_%s_type__, in __ob_colour__' % n]
        G['ob_%s_phrase' % n] = ['__ob_%s_type__ in __ob_colour__' % n]
        G['ob_%s_full' % n] = ['__ob_%s_type__, in __ob_colour__%s, %s, %s, with __ob_%s_detail__' % (n, ' and made of __ob_%s_material__' % n if cls == 'appliance' else '', '__ob_%s_era__' % n, '__ob_%s_wear__' % n, n)]
        G['ob_%s_era' % n] = v75_obj.ERA
        names.append(n)
    allnames = base['ob_names'] + names
    G['ob_names'] = allnames
    for suf in ('short', 'phrase', 'full'): G['ob_any_%s' % suf] = ['__ob_%s_%s__' % (n, suf) for n in allnames]
    G['ob_v109_names'] = names
    return G
if __name__ == '__main__':
    G = build(); print(len(G), 'files', len(G['ob_v109_names']), 'new objects')
