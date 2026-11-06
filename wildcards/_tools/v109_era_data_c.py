# Era descriptions, batch C: furniture, kitchenware and bathroom fittings.
# Each line names the period and then the look: shape, material, colour, finish.
ERA = {
 'chair': {
  'before_1800': ['a 1600s oak chair with a tall carved panel back and thick turned legs', 'a 1700s mahogany dining chair with a pierced vase-shaped back splat and curved legs ending in carved feet'],
  '1800s': ['an 1860s walnut dining chair with a rounded hoop back and a stuffed seat in dark red fabric', 'an 1880s bentwood café chair of steam-bent dark beech with a looped back and a round cane seat'],
  '1900_1945': ['a 1930s dining chair in glossy walnut veneer with a curved fan-shaped back', 'a 1930s chair of bent chrome steel tube with a black leather seat and back'],
  '1946_1979': ['a 1950s moulded plastic shell chair in pale yellow on thin black wire legs', 'a 1970s orange moulded plastic stacking chair with a single curved seat and back'],
  '1980_1999': ['a 1980s black-stained ash dining chair with a padded grey seat and a slatted back', 'a 1990s beech chair with a curved plywood seat and back on slim steel legs'],
  '2000_present': ['a 2000s chair of clear see-through acrylic with a rounded back', 'a 2010s pale oak chair with a curved back rail and thin spindle legs']},
 'armchair': {
  'before_1800': ['a 1700s wing armchair with tall side wings, curved wooden legs and pale green damask upholstery', 'a 1700s carved and gilded armchair with an oval back in cream silk'],
  '1800s': ['an 1870s deep-buttoned armchair in dark green velvet on brass castors', 'an 1890s leather wingback armchair with brass studs along the edges'],
  '1900_1945': ['a 1930s club armchair in tan leather with thick rounded arms and a low back', 'a 1940s armchair in brown moquette with wooden arm pads'],
  '1946_1979': ['a 1950s armchair with slim wooden arms on splayed tapered legs and a mustard wool seat', 'a 1970s low armchair in brown corduroy with deep ribbed cushions'],
  '1980_1999': ['a 1980s black leather armchair with chrome feet', 'a 1990s squashy armchair in a large floral print with a pleated skirt'],
  '2000_present': ['a 2000s cube armchair in cream faux leather', 'a 2010s armchair in grey boucle wool on thin wooden legs']},
 'sofa': {
  'before_1800': ['a 1700s settee with a carved wooden frame, curved legs and striped silk upholstery'],
  '1800s': ['an 1860s deep-buttoned sofa in red velvet with a high scrolled arm and carved walnut feet', 'an 1890s leather sofa with deep buttoning and rolled arms the same height as the back'],
  '1900_1945': ['a 1930s three-seater sofa in mohair with thick rounded arms and wooden feet', 'a 1940s sofa in patterned moquette with plain wooden arm caps'],
  '1946_1979': ['a 1960s low sofa on tapered wooden legs in grey-blue tweed', 'a 1970s brown velour sofa with chunky square cushions'],
  '1980_1999': ['a 1980s black leather sofa with puffy padded arms', 'a 1990s sofa in a large floral print with loose scatter cushions'],
  '2000_present': ['a 2000s L-shaped corner sofa in charcoal fabric', 'a 2010s velvet sofa in emerald green on slim brass legs']},
 'couch': {
  '1800s': ['an 1870s couch in dark velvet with one raised scrolled end and a carved walnut frame', 'an 1890s leather couch with deep buttoning'],
  '1946_1979': ['a 1960s low couch in burnt orange wool on tapered legs', 'a 1970s brown corduroy couch with thick ribbed cushions'],
  '1980_1999': ['a 1980s grey fabric couch with wide padded arms', 'a 1990s overstuffed couch in navy fabric with a pleated skirt'],
  '2000_present': ['a 2000s brown leather couch with low square arms', 'a 2010s grey modular couch in separate square sections']},
 'settee': {
  'before_1800': ['a 1700s settee with a carved double-hoop back and curved legs in yellow silk'],
  '1800s': ['an 1860s buttoned settee in dark blue velvet with a curved back'],
  '1946_1979': ['a 1960s two-seater settee in teak with loose orange wool cushions'],
  '2000_present': ['a 2010s compact settee in mustard fabric on black legs']},
 'table': {
  'before_1800': ['a 1600s long oak refectory table on thick turned legs joined by low stretchers', 'a 1700s mahogany drop-leaf table with hinged side flaps and slim curved legs'],
  '1800s': ['an 1860s round walnut table on a single carved pedestal with three splayed feet', 'an 1880s oak table with thick bulbous legs and a heavy apron'],
  '1900_1945': ['a 1930s oak table on spiral-turned legs', 'a 1940s plain painted kitchen table with a scrubbed wooden top'],
  '1946_1979': ['a 1950s kitchen table with a red patterned plastic laminate top on chrome legs', 'a 1960s teak extending table on tapered legs'],
  '1980_1999': ['a 1980s glass-topped table with a smoky grey top on a chrome base', 'a 1990s chunky pine farmhouse table with a honey-coloured varnish'],
  '2000_present': ['a 2000s glossy white table on a single central leg', 'a 2010s table with a thick live-edge wooden slab on black steel legs']},
 'desk': {
  'before_1800': ['a 1700s mahogany writing desk with a slanted fall front and brass handles', 'a 1700s walnut bureau with pigeonholes behind a hinged lid'],
  '1800s': ['an 1880s oak roll-top desk with a slatted tambour cover and many small drawers', 'an 1860s mahogany pedestal desk with a green leather top'],
  '1900_1945': ['a 1930s oak office desk with drawers in both pedestals and brass handles', 'a 1940s steel office desk painted olive green'],
  '1946_1979': ['a 1960s teak desk on tapered legs with a single slim drawer', 'a 1970s grey steel office desk with a wood-effect top'],
  '1980_1999': ['a 1990s computer desk in beech-effect laminate with a pull-out keyboard shelf', 'a 1980s black ash desk with a drawer unit'],
  '2000_present': ['a 2000s glass desk on chrome trestle legs', 'a 2010s white standing desk on a height-adjustable steel frame']},
 'bed': {
  'before_1800': ['a 1600s carved oak four-poster bed with a wooden canopy and heavy woollen drapes', 'a 1700s mahogany tester bed with fluted posts and silk curtains'],
  '1800s': ['an 1880s brass and black iron bed with curly scrollwork and round brass knobs', 'an 1860s mahogany sleigh bed with curved ends'],
  '1900_1945': ['a 1930s walnut veneer bed with a curved fan-shaped headboard', 'a 1940s painted iron bed with a plain rail headboard'],
  '1946_1979': ['a 1960s low teak bed with a slatted headboard', 'a 1970s bed with a tall buttoned velvet headboard in brown'],
  '1980_1999': ['a 1980s black lacquered bed with a low headboard', 'a 1990s honey pine bed with chunky turned posts'],
  '2000_present': ['a 2000s low platform bed in dark wood', 'a 2010s bed with a tall upholstered headboard in grey fabric']},
 'bedstead': {
  '1800s': ['an 1880s black iron bedstead with brass knobs and a curved brass rail', 'an 1860s mahogany bedstead with a carved headboard'],
  '1900_1945': ['a 1920s oak bedstead with a plain panelled headboard', 'a 1930s white painted iron bedstead']},
 'wardrobe': {
  'before_1800': ['a 1700s oak press cupboard with panelled doors and drawers below'],
  '1800s': ['an 1870s tall mahogany wardrobe with a full-length mirrored door and a carved cornice', 'an 1890s pine wardrobe painted dark brown'],
  '1900_1945': ['a 1930s walnut wardrobe with curved front doors and a stepped top', 'a 1940s plain oak wardrobe'],
  '1946_1979': ['a 1960s teak wardrobe with slim wooden handles on tapered legs', 'a 1970s white wardrobe with ornate gold-coloured plastic handles'],
  '1980_1999': ['a 1980s fitted wardrobe with mirrored sliding doors', 'a 1990s honey pine wardrobe with round wooden knobs'],
  '2000_present': ['a 2000s flat-pack wardrobe in white with tall sliding mirror doors', 'a 2010s wardrobe in oak with slim black handles']},
 'dresser': {
  'before_1800': ['a 1700s oak dresser with open plate racks above and cupboards below'],
  '1800s': ['an 1870s pine kitchen dresser with plates lined up on open shelves', 'an 1880s mahogany dresser with a carved mirror back'],
  '1946_1979': ['a 1950s kitchen dresser painted cream with glass-fronted upper doors', 'a 1970s dark oak dresser'],
  '2000_present': ['a 2010s farmhouse dresser painted sage green with open shelves']},
 'sideboard': {
  '1800s': ['an 1860s mahogany sideboard with a tall carved mirrored back', 'an 1890s oak sideboard with carved doors'],
  '1900_1945': ['a 1930s walnut sideboard with curved ends and stepped edges', 'a 1940s plain oak sideboard on short legs'],
  '1946_1979': ['a 1960s long low teak sideboard with sliding doors on tapered legs', 'a 1970s dark wood sideboard with smoked glass doors'],
  '2000_present': ['a 2010s oak sideboard with slatted doors on thin black legs']},
 'bookcase': {
  '1800s': ['an 1870s mahogany bookcase with glazed doors and a carved cornice', 'an 1890s oak bookcase with open shelves'],
  '1900_1945': ['a 1930s oak bookcase with stacked glass-fronted sections that lift up', 'a 1940s plain painted bookcase'],
  '1946_1979': ['a 1960s teak bookcase with open shelves on tapered legs', 'a 1970s wall-hung shelving system on metal uprights'],
  '2000_present': ['a 2000s square-grid bookcase in white', 'a 2010s ladder bookcase leaning against the wall']},
 'cabinet': {
  '1800s': ['an 1870s mahogany display cabinet with glazed doors', 'an 1880s ebonised cabinet with painted panels'],
  '1900_1945': ['a 1930s walnut cocktail cabinet with a mirrored inside', 'a 1940s plain oak cabinet with small brass knobs'],
  '1946_1979': ['a 1950s kitchen cabinet in pale blue enamel', 'a 1970s cabinet with wood-effect doors'],
  '2000_present': ['a 2000s glossy white cabinet with handleless doors', 'a 2010s matt green cabinet with brass knobs']},
 'stool': {
  'before_1800': ['a three-legged wooden milking stool with a round seat', 'a 1700s joint stool in oak with turned legs'],
  '1946_1979': ['a 1950s chrome bar stool with a round red vinyl seat', 'a 1970s wooden kitchen stool'],
  '2000_present': ['a 2010s black metal bar stool with a low back', 'a 2010s wooden stool with a round seat']},
 'bench': {
  'before_1800': ['a plain oak bench with splayed legs'],
  '1800s': ['an 1880s cast-iron park bench with curly ends and wooden slats', 'an 1870s pew-like oak bench'],
  '1946_1979': ['a 1960s slatted wooden park bench on concrete ends'],
  '2000_present': ['a 2010s concrete bench with a wooden seat', 'a 2010s bench of perforated steel sheet']},
 'cot': {
  '1800s': ['an 1880s wicker cot on a stand with a fabric hood'],
  '1946_1979': ['a 1960s painted wooden cot with rounded bars', 'a 1970s cot in pine'],
  '2000_present': ['a 2010s white wooden cot with a drop side', 'a 2010s cot painted soft grey with straight bars']},
 'cradle': {
  'before_1800': ['a carved oak rocking cradle with a hooded end'],
  '1800s': ['an 1870s wicker cradle on a stand with a frilled cover', 'an 1880s swinging wooden cradle'],
  '2000_present': ['a 2010s wooden cradle on curved rockers']},
 'mirror': {
  'before_1800': ['a 1700s mirror in a carved and gilded frame', 'a 1700s walnut-framed mirror'],
  '1800s': ['an 1870s large mirror in an arched gilded frame over a mantelpiece', 'an 1880s oval mirror in a dark wood frame'],
  '1900_1945': ['a 1930s frameless mirror with bevelled edges and stepped corners', 'a 1940s round mirror on a chain'],
  '1946_1979': ['a 1960s round mirror surrounded by gilded metal rays', 'a 1970s mirror in a wicker frame'],
  '2000_present': ['a 2010s round mirror in a thin brass frame', 'a 2010s tall arched mirror in a black metal frame']},
 'teapot': {
  'before_1800': ['a 1700s silver teapot with a curved spout and a wooden handle', 'a 1700s small porcelain teapot with blue painted flowers'],
  '1800s': ['an 1870s round brown glazed earthenware teapot', 'an 1880s silver-plated teapot with engraved patterns'],
  '1900_1945': ['a 1930s geometric teapot with a stepped lid in cream and orange', 'a 1940s plain brown teapot under a knitted cosy'],
  '1946_1979': ['a 1960s tall coffee-pot-shaped teapot with a bold flower print', 'a 1970s brown stoneware teapot'],
  '2000_present': ['a 2010s clear glass teapot with a steel infuser', 'a 2010s matt white teapot']},
 'mug': {
  '1900_1945': ['a white enamel tin mug with a blue rim', 'a 1940s thick white pottery mug'],
  '1946_1979': ['a 1970s brown speckled stoneware mug', 'a 1960s orange flower-patterned mug'],
  '1980_1999': ['a 1980s white mug with a printed cartoon pattern', 'a 1990s tall dark blue mug'],
  '2000_present': ['a 2000s stainless steel travel mug with a lid', 'a 2010s handmade speckled ceramic mug in matt glaze']},
 'cup': {
  'before_1800': ['a 1700s small handleless porcelain tea bowl with blue painted decoration'],
  '1800s': ['an 1870s bone china teacup with gilded edges and painted roses on a matching saucer'],
  '1946_1979': ['a 1960s plastic melamine cup in pastel colours', 'a 1970s brown glazed cup'],
  '2000_present': ['a 2010s paper takeaway cup with a plastic lid', 'a 2010s reusable cup in glass with a cork band']},
 'bottle': {
  'before_1800': ['a 1700s dark green hand-blown glass bottle with a squat round body and a short neck'],
  '1800s': ['an 1880s aqua glass bottle with a marble trapped in its neck', 'an 1870s brown stoneware ink bottle'],
  '1900_1945': ['a 1930s glass milk bottle with a foil cap', 'a 1920s ribbed blue glass bottle'],
  '1946_1979': ['a 1960s curvy clear glass soda bottle with a metal cap', 'a 1970s brown glass beer bottle'],
  '2000_present': ['a 2010s clear plastic water bottle with a ribbed body', 'a 2010s reusable steel water bottle']},
 'tin': {
  '1800s': ['an 1880s biscuit tin with a printed lid of scenes and gilt edging', 'an 1870s plain tinplate canister'],
  '1900_1945': ['a 1930s tea tin printed with bright patterns', 'a 1940s tin with rusted edges'],
  '1946_1979': ['a 1960s round cake tin with a flowery printed lid', 'a 1970s tin in orange and brown'],
  '2000_present': ['a 2010s matt tin with a simple printed design', 'a 2010s round tin with a hinged lid']},
 'jar': {
  'before_1800': ['a salt-glazed brown stoneware jar with a narrow mouth', 'a 1700s glazed earthenware jar'],
  '1800s': ['an 1880s apothecary jar of clear glass with a ground glass stopper', 'an 1870s stoneware storage jar'],
  '1946_1979': ['a 1970s glass storage jar with an orange plastic lid'],
  '2000_present': ['a 2010s glass jar with a hinged lid and rubber seal', 'a 2010s jar with a bamboo lid']},
 'bucket': {
  'before_1800': ['a wooden bucket of staves bound with iron hoops and a rope handle'],
  '1900_1945': ['a galvanised steel bucket with a wire handle', 'a 1930s enamel bucket'],
  '1946_1979': ['a 1960s red plastic bucket'],
  '2000_present': ['a 2010s plastic bucket with a pouring lip', 'a 2010s rubber bucket in black']},
 'broom': {
  'before_1800': ['a besom broom of bound birch twigs on a long stick'],
  '1900_1945': ['a 1930s straw broom with a wooden handle'],
  '1946_1979': ['a 1960s broom with a wooden head and stiff bristles'],
  '2000_present': ['a 2010s plastic broom with coloured bristles']},
 'mangle': {
  '1800s': ['an 1880s cast-iron mangle on a stand with two large wooden rollers and a crank wheel'],
  '1900_1945': ['a 1930s mangle with rubber rollers on a metal frame']},
 'washboard': {
  '1800s': ['an 1880s wooden washboard with a ribbed zinc front'],
  '1900_1945': ['a 1930s washboard with a ridged glass panel']},
 'radiator': {
  '1800s': ['an 1880s cast-iron column radiator with ornate patterns'],
  '1900_1945': ['a 1930s plain cast-iron radiator'],
  '1946_1979': ['a 1960s steel panel radiator painted cream'],
  '2000_present': ['a 2010s tall vertical radiator in anthracite grey', 'a 2010s chrome towel radiator']},
 'fireplace': {
  'before_1800': ['a wide stone inglenook fireplace with a heavy oak beam above'],
  '1800s': ['an 1880s cast-iron fireplace with patterned tile panels on each side', 'an 1860s marble fireplace with a carved mantelpiece'],
  '1900_1945': ['a 1930s tiled fireplace in beige with a stepped top'],
  '1946_1979': ['a 1970s fireplace clad in rough stone with a gas fire'],
  '2000_present': ['a 2010s hole-in-the-wall gas fire with a pebble bed', 'a 2010s wood-burner set in a plain chimney breast']},
 'bath': {
  '1800s': ['an 1880s cast-iron roll-top bath on four claw feet'],
  '1946_1979': ['a 1970s bath in avocado green with matching panels'],
  '2000_present': ['a 2010s freestanding white bath shaped like an egg']},
 'bathtub': {
  '1800s': ['an 1880s cast-iron roll-top bathtub painted dark green outside'],
  '1946_1979': ['a 1970s bathtub in harvest gold'],
  '2000_present': ['a 2010s freestanding stone bathtub']},
 'toilet': {
  '1800s': ['an 1880s toilet with a high wall cistern and a pull chain'],
  '1946_1979': ['a 1970s toilet in pastel pink'],
  '2000_present': ['a 2010s white wall-hung toilet with a hidden cistern']},
 'sink': {
  '1800s': ['an 1880s shallow stone sink'],
  '1900_1945': ['a 1930s deep white ceramic sink with a wooden draining board'],
  '1946_1979': ['a 1960s steel sink with a ridged drainer'],
  '2000_present': ['a 2010s undermounted steel sink', 'a 2010s white farmhouse sink']},
 'basin': {
  '1800s': ['an 1880s washbasin and jug on a marble-topped stand'],
  '1946_1979': ['a 1970s pedestal basin in avocado green'],
  '2000_present': ['a 2010s round white countertop basin']},
 'shower': {
  '1900_1945': ['a 1930s shower with a large round chrome head and exposed pipes'],
  '1946_1979': ['a 1970s shower with a coloured plastic curtain and a hose head'],
  '2000_present': ['a 2010s walk-in shower with a large square rainfall head and glass screen']},
}
