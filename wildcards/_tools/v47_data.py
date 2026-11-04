"""v47 data: furniture, household and office objects, bottles and closures, perfume, liquids. Items only, fully described, no brands."""
from v40_data_a import E
FURN = {
'tables': E("""
dining table|a rectangular table with four sturdy legs and a flat top large enough for six people|oak; pine; walnut
round pedestal table|a round table with a single central column on a wide base|wood; marble
coffee table|a low rectangular table with a lower shelf, set in front of a sofa|wood; glass; metal
side table|a small square table with slim legs, about the height of a sofa arm|wood; metal
console table|a long narrow table with slim legs, made to stand against a wall|wood; steel
drop-leaf table|a small table with hinged flaps that fold down at the sides|oak; beech
folding card table|a square light table with folding legs and a felt top|wood and felt
picnic table|a long outdoor table with attached bench seats on both sides|treated wood
kitchen island|a freestanding counter unit with a worktop, drawers below and an overhang|wood and stone
bedside table|a small table with one drawer and an open shelf beneath|wood
glass-top table|a table with a clear glass top on a steel frame|glass and steel
low Japanese table|a very low table with short legs for sitting on the floor|lacquered wood
""".replace('\n\n','\n')),
'storage': E("""
credenza|a long low sideboard with sliding doors on the front and a flat top|walnut; teak
sideboard|a wide cupboard with drawers and two doors, standing on short legs|oak; mahogany
bookcase|a tall frame with five open shelves|pine; oak
chest of drawers|a tall cabinet with four deep drawers and round knobs|pine; walnut
wardrobe|a tall two-door cupboard with a hanging rail inside|oak; pine
tallboy|a very tall chest with six narrow drawers|wood
display cabinet|a tall cabinet with glass doors and glass shelves|wood and glass
shoe rack|a narrow stand with slanted shelves for shoes|metal; bamboo
blanket chest|a long wooden box with a hinged lid, at the foot of a bed|cedar
wall shelf|a single board fixed to a wall on two brackets|wood
filing cabinet|a metal cabinet with three deep drawers and a label holder|steel
TV stand|a low wide unit with an open shelf and two cupboards|wood
chest trunk|a travel trunk with leather straps and brass corners|wood and leather
storage ottoman|a padded cube with a lift-off lid for storage|fabric; vinyl
""".replace('\n\n','\n')),
'beds': E("""
double bed|a wide bed on a wooden frame with a headboard, a mattress, sheets and pillows|oak; pine
single bed|a narrow bed on a plain frame with a mattress and a folded blanket|pine; steel
bunk bed|two single beds stacked on one frame with a ladder at the end|wood; steel
four-poster bed|a wide bed with four tall posts at the corners and a rail across the top|oak; mahogany
canopy bed|a bed with a frame that carries a draped fabric canopy|wood; fabric
sofa bed|a sofa that unfolds into a bed with a thin mattress|fabric
futon|a thin folding mattress on a low slatted frame|cotton; wood
platform bed|a low bed on a solid base with no headboard|wood
daybed with trundle|a single bed with a back and arms and a second bed that rolls out beneath|wood; fabric
hammock bed|a swinging bed of canvas hung from a frame|canvas
camp cot|a narrow folding bed of canvas on a metal frame|canvas and steel
waterbed|a wide bed with a soft sloshing water-filled mattress in a wooden frame|vinyl and wood
""".replace('\n\n','\n')),
'bathroom': E("""
toilet|a white ceramic bowl on a pedestal, with a hinged seat and lid and a cistern behind|ceramic
wall-hung toilet|a ceramic bowl fixed to the wall with a hidden cistern|ceramic
bidet|a low oval ceramic basin with taps, beside the toilet|ceramic
pedestal washbasin|a basin on a tall column with two taps|ceramic
vanity unit|a basin set into a cabinet with doors below|wood and ceramic
bathtub|a long deep tub with a sloped back and a mixer tap|acrylic; cast iron
freestanding claw-foot bathtub|an oval roll-top tub standing on four curved feet|cast iron
shower cubicle|a glass-walled space with a fixed rain shower head and a mixer|glass and steel
towel rail|a heated rail with several bars for towels|chrome
bathroom mirror cabinet|a wall cupboard with a mirrored door|glass and wood
""".replace('\n\n','\n')),
'kitchen': E("""
kitchen sink|a deep double basin sink with a swan-neck tap|stainless steel
range cooker|a wide cooker with a flat hob and two ovens|steel
gas hob|a flat surface with four burners and iron grids|steel
refrigerator|a tall box with two doors and a handle|steel
dishwasher|a front-loading box with a door that folds down and racks inside|steel
kitchen cabinet|a wall cupboard with a door and a shelf|wood
breakfast bar|a long raised counter with high stools|wood
pantry shelving|a wall of open shelves for jars and tins|wood
""".replace('\n\n','\n')),
'office': E("""
writing desk|a flat desk with a drawer under the top and four tapered legs|oak; walnut
standing desk|a desk with an adjustable height column and a wide flat top|steel and laminate
L-shaped desk|a corner desk with two long arms and a cable hole|laminate
roll-top desk|a desk with a curved slatted lid that slides back|oak
drafting table|a tilted drawing board on an adjustable steel stand|steel; wood
conference table|a very long table seating twelve, with a central cable box|laminate; wood
reception desk|a tall front counter with a lower writing ledge|wood
office chair with arms|a swivel chair with arms, a mesh back and a padded seat|mesh and plastic
bookshelf with ladder|a tall bookcase with a sliding ladder|oak
""".replace('\n\n','\n')),
'lighting': E("""
floor lamp|a tall slim pole with a round fabric shade at the top|metal; fabric
table lamp|a ceramic base with a pleated shade|ceramic; fabric
desk lamp with a swing arm|a metal lamp with a jointed arm and a conical head|steel
pendant light|a bowl-shaped shade hanging from a long cord|metal; glass
chandelier|a tiered frame with curved arms and candle-shaped bulbs|brass; crystal
paper lantern|a round lantern of folded paper over a wire frame|paper
wall sconce|a small shaded lamp fixed to the wall|brass
candlestick|a tall holder with a round base and a drip tray|brass; ceramic
""".replace('\n\n','\n')),
'decor': E("""
floor mirror|a tall rectangular mirror in a wooden frame leaning against a wall|glass and wood
round wall mirror|a circular mirror in a thin gold frame|glass and metal
area rug|a large rectangular woven rug with a pattern|wool; jute
curtains|a pair of long floor-length curtains hanging from a rod|cotton; linen
roller blind|a window blind rolled on a tube|fabric
picture frame|a rectangular frame around an empty mount|wood; metal
potted floor plant stand|a tripod stand holding a large pot|metal; ceramic
clock on the wall|a round wall clock with plain hands|wood; metal
vase|a tall narrow vase with a curved neck|glass; ceramic
room divider screen|a folding screen of three panels|wood; paper
""".replace('\n\n','\n')),
}
HOME = {
'cookware': E("""
frying pan|a round shallow pan with a long handle and sloped sides|cast iron; stainless steel; non-stick coated steel
saucepan|a deep round pan with a long handle and a lid|stainless steel; aluminium
stock pot|a tall wide pot with two side handles and a lid|stainless steel
wok|a deep bowl-shaped pan with a long handle and two small loops|carbon steel
casserole dish|a heavy lidded pot with two side handles|enamelled cast iron; ceramic
baking tray|a flat rectangular sheet with a rolled edge|aluminium; steel
roasting tin|a deep rectangular tin with two handles|steel
kettle|a spouted pot with a handle and a lid, for boiling water|steel; copper
teapot|a rounded pot with a spout, a handle and a lid|ceramic; cast iron
cast-iron skillet|a heavy round pan with a short helper handle|cast iron
pressure cooker|a heavy lidded pot with a locking lid and a steam valve|aluminium
colander|a bowl with holes and two handles|steel; plastic
""".replace('\n\n','\n')),
'tableware': E("""
dinner plate|a flat round plate with a raised rim|ceramic; porcelain
soup bowl|a deep round bowl with a wide rim|ceramic
mug|a cylinder with a handle|ceramic; enamel
drinking glass|a plain cylinder glass with a heavy base|glass
wine glass|a glass with a stem, a round bowl and a flat foot|glass
teacup and saucer|a small cup with a handle and a matching dish|bone china
cutlery set|a knife, fork and spoon with plain handles|stainless steel
serving platter|a large oval flat dish|ceramic
salad bowl|a very wide shallow bowl|wood; glass
butter dish|a small lidded dish|ceramic
""".replace('\n\n','\n')),
'textiles': E("""
wool blanket|a thick woven blanket in a plain weave with a stitched edge|wool
patchwork quilt|a bed cover sewn from squares of different fabric with thick stitching|cotton
fleece throw|a soft light blanket with a fuzzy surface|polyester fleece
knitted blanket|a chunky knitted blanket in a rope-stitch pattern|wool; acrylic
weighted blanket|a heavy blanket quilted into small squares filled with beads|cotton
electric blanket|a thin blanket with a cord and a small controller|polyester
bed sheet set|a fitted sheet, a flat sheet and two pillowcases|cotton; linen
pillow|a plump rectangular pillow in a plain cover|cotton
bath towel|a large thick rectangle of towelling|cotton
tea towel|a thin printed cloth, square|linen
tablecloth|a large square of cloth for a table|cotton; linen
cushion|a square cushion with a zip cover|velvet; cotton
""".replace('\n\n','\n')),
'cleaning': E("""
broom|a long handle with a head of stiff bristles|wood and plastic
mop and bucket|a long handle with a head of cotton strings, beside a plastic bucket|cotton; plastic
dustpan and brush|a small flat scoop with a short brush|plastic
vacuum cleaner|an upright machine with a handle, a body and a floor head|plastic
feather duster|a short handle with a plume of feathers|feather
sponge|a small rectangular block of soft cellulose with a rough side|cellulose
spray bottle|a hand-held bottle with a trigger sprayer|plastic
laundry basket|a tall oval basket with two cutout handles|plastic; wicker
iron|a flat metal base with a handle and a steam button|steel; plastic
ironing board|a long folding board with a padded cover|steel and cotton
""".replace('\n\n','\n')),
'electronics': E("""
table radio|a rectangular box with a round dial and a speaker grille|wood; plastic
television|a flat rectangular screen on a stand|plastic
laptop|a folding computer with a screen and a keyboard|aluminium
desktop monitor|a flat screen on an adjustable stand|plastic
mechanical keyboard|a rectangular board of raised keys|plastic
computer mouse|a small curved device with two buttons and a wheel|plastic
smart speaker|a small cylinder with a mesh cover and glowing ring|fabric and plastic
alarm clock|a round clock with two bells and a hammer on top|metal
desk fan|a small fan with a round cage and a stand|plastic
table heater|a small box with a grille and a dial|metal
""".replace('\n\n','\n')),
'office_supplies': E("""
stapler|a small hinged metal tool with a spring that pushes a staple through paper|steel
hole punch|a lever tool with two round blades|steel
desk tidy|an open box with sections for pens|wood; plastic
ring binder|a thick folder with two rings and a spine label|cardboard
paper clips in a dish|a small dish of bent wire clips|steel
fountain pen|a slim pen with a metal nib and a cap|resin
ballpoint pen|a plastic tube with a pocket clip and a click top|plastic
notebook|a bound book with a plain cover and ruled pages|paper
desk calendar|a standing block of numbered pages|paper
scissors|two blades with handles that open and close|steel
tape dispenser|a heavy base with a roll of clear tape|plastic
whiteboard|a flat white board with a pen tray|melamine
""".replace('\n\n','\n')),
}
BOTTLE = E("""
round glass bottle|a bottle with a round body, a narrow neck and a flat base|clear glass
square bottle|a bottle with four flat sides and a short neck|clear glass
flask|a flat bottle with a rounded shape that fits a pocket|stainless steel
carafe|a wide-bellied jug with a flared lip|glass
amphora|a tall two-handled bottle with a pointed base|clay
hip flask|a flat curved metal bottle with a hinged cap|stainless steel
wine bottle|a tall bottle with sloping shoulders, a long neck and a punt in the base|green glass
beer bottle|a bottle with narrow neck, a short body and a lip for a cap|brown glass
spirit bottle|a heavy square-shouldered bottle with a thick base|clear glass
medicine bottle|a small cylindrical bottle with a wide mouth|amber glass; brown plastic
soda bottle|a clear plastic bottle with a ribbed base|plastic
jug|a large bottle with a handle at the neck|glass; plastic
growler|a wide-mouthed bottle with a handle|brown glass
squeeze bottle|a soft bottle with a narrow nozzle|plastic
spray bottle|a bottle with a trigger sprayer|plastic
dropper bottle|a small bottle with a rubber squeeze dropper|amber glass
pump bottle|a tall bottle with a pump on top|plastic
swing-top bottle|a thick bottle with a wire swing-top stopper|glass
milk bottle|a short wide-mouthed bottle with a narrow base|glass
novelty skull bottle|a bottle moulded as a skull|glass
novelty fish bottle|a bottle moulded as a fish|glass
tall pilsner bottle|a tall slim bottle|green glass
""")
CLOSURE = E("""
screw cap|a ribbed metal cap that screws onto the neck|aluminium
crown cap|a small metal cap crimped onto the lip with a ruffled edge|steel
natural cork|a short cylinder of cork pressed into the neck|cork
synthetic cork|a smooth cylinder of plastic that looks like cork|plastic
swing-top stopper|a ceramic stopper held by a wire lever|porcelain and wire
wax seal|a dipped coat of wax over the cap|wax
flip-top cap|a hinged cap with a spout that snaps up|plastic
pump dispenser|a pump head on a tube|plastic
child-resistant cap|a plastic cap that has to be pushed down while turned|plastic
tamper-evident band|a ring of thin plastic that breaks when the cap is turned|plastic
glass stopper|a ground-glass ball stopper|glass
wooden stopper|a round wooden knob with a cork underside|wood and cork
""")
PERFUME = E("""
atomiser spray bottle|a small bottle with a fine-mist pump nozzle and a snap-on cap|glass
splash bottle|a bottle with a narrow neck and a plain stopper|glass
stoppered flacon|a faceted glass bottle with a tall decorative stopper|crystal
rollerball|a slim bottle with a roll-on ball at the top|glass
solid perfume compact|a small round tin with a hinged lid|metal
perfume decanter|a tall bottle with a bulb and a tube|glass
antique perfume bottle|a small bottle with silver filigree on the neck|glass; silver
art-deco perfume bottle|a stepped, geometric bottle with a frosted stopper|moulded glass
novelty perfume bottle|a bottle shaped like a heart or a swan|glass
perfume sample vial|a tiny glass vial with a screw cap|glass
sample card|a small card with a dab of scent|card
spray pen|a slim pen-shaped sprayer|metal
miniature perfume bottle|a very small bottle of a standard shape|glass
tester strip|a thin paper blotter strip|paper
discovery set|a small box of five tiny bottles|glass; card
""")
LIQ = {
'liquor': ['a clear colourless spirit with a thin oily sheen', 'a pale straw-yellow white wine with fine bubbles at the edge', 'a deep ruby red wine with a purple rim', 'a dark amber spirit with a gold glow', 'a golden lager with a white foam head', 'a dark brown stout with a creamy tan head', 'a rose-pink sparkling wine with rising bubbles', 'a bright orange cocktail layered with red syrup at the base', 'a clear blue cocktail with a slice of citrus at the rim', 'a cloudy white liqueur with swirls of cream', 'a layered shot in red, yellow and green bands', 'a dark red cocktail with ice and a cherry', 'a pale green cocktail with crushed mint', 'a coppery red ale with light foam'],
'medical': ['a dark brown herbal tincture, slightly cloudy, with sediment at the bottom', 'a thick golden syrup that coats the glass', 'a clear, watery saline solution', 'a pale yellow tonic with fine bubbles', 'a cloudy white suspension that settles in layers', 'a bright red elixir, syrupy and sticky', 'a thick clear gel in a squeezed ribbon', 'a deep green herbal liquid with floating specks', 'an amber oil with a thin shine', 'a lab solution in pale violet, perfectly clear', 'a milky pink liquid with a fine froth', 'a dark blue solution, transparent and thin'],
'strange': ['a clear broth with floating carrot rounds and green leaves', 'a pale soup with floating dumplings', 'water with floating slices of citrus and sprigs of mint', 'a glass of clear liquid with a glitter swirl rising in it', 'a jelly set with whole berries suspended inside', 'a drink with ice cubes shaped like stars', 'a glass of clear liquid with a tiny toy boat floating in it', 'a layered drink with bands of blue, white and red', 'a swirled mixture of pink and orange liquids that has not blended', 'a glass of cloudy lemonade with a floating paper umbrella', 'a clear jar of liquid with a single paper crane suspended in it', 'a bowl of soup with a tiny floating rubber duck', 'a drink with dry ice smoke curling off the top', 'a vial of liquid with floating gold flakes', 'a tall glass holding bright green liquid with a spoon standing upright in it', 'a jar of cloudy water with tiny floating beads', 'a drink filled with floating basil seeds', 'a bowl of milky liquid with floating petals'],
}
LIQLOOK = {'colour': ['clear', 'pale yellow', 'amber', 'deep red', 'rose pink', 'bright orange', 'green', 'blue', 'violet', 'milky white', 'brown', 'golden'],
           'transparency': ['perfectly clear', 'slightly translucent', 'cloudy', 'completely opaque'],
           'viscosity': ['thin and watery', 'slightly thick', 'syrupy', 'thick and gel-like'],
           'extras': ['with a sheen on the surface', 'with a few small bubbles', 'with fine sediment at the bottom', 'with two distinct layers', 'with slow swirls of a second colour', 'with floating specks', 'with a head of foam on top']}
