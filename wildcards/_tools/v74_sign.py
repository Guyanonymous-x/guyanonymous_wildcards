"""v74 stage B - shared lettering/label engine, signage (71), advertising signs (51), tins and labelled containers (52).
All business names, brands, slogans and wording are invented. Text meant to appear in the image is in double quotes."""
import random
from famlib import P, slug
from v74_books import pool, FIRST, SUR_A, SUR_B, ADJ, NOUN, PLACE

def q(lst): return ['"%s"' % x for x in lst]
SYL1 = P("Bren; Tav; Mor; Kel; Dov; Ferr; Lun; Sol; Han; Wil; Ros; Gar; Pel; Cor; Vin; Arn; Bel; Dar; Ful; Hol; Jar; Mar; Nor; Ped; Quil; Rav; Sal; Tor; Ulm; Var")
SYL2 = P("ola; ava; endo; ixa; aro; uma; ento; ora; ila; ex; ine; ado; oma; ura; ita; ova; elo; ico; ara; ium")
def brand(r):
    k = r.randrange(5)
    if k == 0: return r.choice(SYL1) + r.choice(SYL2)
    if k == 1: return r.choice(SYL1).upper() + r.choice(SYL2).upper()
    if k == 2: return '%s%s %s' % (r.choice(SYL1), r.choice(SYL2), r.choice(['Brand', 'Best', 'Select', 'Gold Label', 'Finest', 'Reserve', 'Original']))
    if k == 3: return '%s & %s' % (r.choice(SUR_A) + r.choice(SUR_B), r.choice(SUR_A) + r.choice(SUR_B))
    return "%s's" % (r.choice(FIRST))
BRANDS = pool(71, 400, brand)

TRADES = P("Bakery; Butcher; Pharmacy; Hardware; Bookshop; Barber; Tailor; Cafe; Fishmonger; Greengrocer; Dairy; Florist; Watchmaker; Cobbler; Chemist; Tea Rooms; Draper; Ironmonger; Laundry; Post Office; Toy Shop; Tobacconist; Confectioner; Pawnbroker; Optician; Photographer; Garage; Record Shop; Hat Maker; Wine Merchant")
PUB = P("The Crown and Anchor; The Red Lion; The Old Mill; The Fox and Hounds; The Three Tuns; The Plough; The Hare and Heron; The Ship Inn; The Lamplighter; The Golden Fleece; The King's Arms; The Wheatsheaf; The Salt Cellar; The Black Swan; The Lantern; The Bell and Bucket")
def shop_name(r):
    k = r.randrange(5); t = r.choice(TRADES)
    if k == 0: return "%s%s's %s" % (r.choice(SUR_A), r.choice(SUR_B), t)
    if k == 1: return 'The %s %s' % (r.choice(ADJ), t)
    if k == 2: return '%s %s' % (r.choice(PLACE), t)
    if k == 3: return '%s & Sons %s' % (r.choice(SUR_A) + r.choice(SUR_B), t)
    return '%s %s' % (r.choice(FIRST), t)
SHOP = pool(72, 400, shop_name)
SLOGAN = P("Quality You Can Taste; Since 1887; Family Owned for Four Generations; Fresh Every Morning; The Finest in Town; Better by Far; Try Us Once; Satisfaction Guaranteed; Good Honest Value; Always the Best; Made the Old Way; Pure and Simple; The Choice of the Careful; Your Neighbourhood Favourite; Best Prices Round Here; Open Late Every Day; Built to Last; Straight from the Farm; Hand Made with Care; Naturally Good")
NOTICE = P("OPEN; CLOSED; BACK IN 10 MINUTES; PUSH; PULL; WET PAINT; WELCOME; PLEASE WAIT HERE; NO ENTRY; STAFF ONLY; FRESH BREAD DAILY; SALE NOW ON; EXIT; KEEP OFF THE GRASS; MIND THE STEP; BEWARE OF THE DOG; PLEASE KNOCK; TODAY'S SPECIAL; FRESH COFFEE; NO PARKING; WE ARE HIRING; ROOMS AVAILABLE; ALL WELCOME; DELIVERIES AT REAR; PLEASE CLOSE THE GATE; OUT OF ORDER; ASK INSIDE; LOST CAT; FOR SALE; TO LET")
STREET = P("High Street; Mill Lane; Station Road; Church Row; Market Place; Canal Street; Harbour Road; Quarry Lane; Orchard Way; Bridge Street; Tannery Yard; King's Parade; Willow Close; Foundry Road; Chapel Hill; Ropewalk")
MENU = P("Soup of the Day 4.50; Fried Egg Sandwich 3.20; Fish and Chips 9.80; Tea 1.50; Apple Pie 4.00; Beef Stew 8.75; Toasted Teacake 2.90; Fresh Orange Juice 3.60; Mushroom Omelette 7.40; Pancakes with Syrup 5.50; Pot of Coffee 2.80; Sausage Roll 2.40; Cheese Plate 6.90; Ginger Beer 2.20; Lemon Tart 4.20")
SHIP = P("Merry Alice; Northern Wren; Sea Fox; Bright Venture; Lady Marguerite; Grey Heron; Saltwind; Wandering Star; Good Hope; Little Tern; Sparrowhawk; Maid of Dunmere; Kittiwake; Harvest Moon; Silver Gannet; Ocean Rose; Windflower; Cormorant; Thistle; Brave Anchor")
PLATE = ["%s %s %s" % (a, b, c) for a, b, c in [("KLM", "482", "T"), ("7ZAH", "239", ""), ("BR-12", "ST", "9"), ("2FQW", "914", ""), ("HX", "07", "NRL"), ("GD 6623", "", ""), ("AB 12 CDE", "", ""), ("L 4821", "", ""), ("PRM 331", "", ""), ("W-QT 8052", "", ""), ("5TXV", "720", ""), ("N 901 BK", "", "")]]
PLATE = [p.strip().replace('  ', ' ') for p in PLATE]
PRODUCT = P("tea; biscuits; cocoa; tobacco; boot polish; soap; mustard; sweets; coffee; baking powder; cough lozenges; motor oil; axle grease; toothpowder; custard powder; sardines; shoe cream; pipe tobacco; condensed milk; cigars; liquorice; mints; golden syrup; sewing needles; razor blades; typewriter ribbon; aspirin tablets; stove polish; paint; seed packets")
LOGO = P("a lion standing on its hind legs; a crown above a banner; a ship under full sail; a sunburst with rays; a smiling cartoon cook; a pair of crossed keys; a bee on a flower; an anchor wrapped in rope; a stag in a circle; a stylised wheat sheaf; a rooster on a post; a shield with a star; a lighthouse beam; a swan; a winged wheel; a bell; a stylised mountain; a smiling sun face; a bear holding a jar; a crescent moon and star")

# ---------------------------------------------------------------- lettering engine
LETTER_STYLE = P("tall condensed block capitals; ornate Victorian serif lettering with shadows; flowing hand-painted script; rounded 1950s diner script; clean modern sans-serif capitals; chunky slab serif; gothic blackletter; stencil capitals; Art Deco geometric capitals; neat brush-pen lettering; sign-painter's gold leaf lettering with a black drop shadow; elegant thin serif capitals; playful hand-cut lettering; bold bubble letters; typewriter lettering; engraved capitals; condensed railway-style lettering; 1970s rounded lettering; narrow all-capitals in wide spacing")
MATS = {
 'paint': P("white enamel paint on a dark ground; black paint on a pale ground; stencilled black paint; hand-painted gold with a black shadow; cream paint on a dark ground; red paint outlined in white"),
 'wallpaint': P("black paint on whitewashed brick; faded white letters painted straight onto rough brick; red and cream paint on weathered brick"),
 'glass': P("gold leaf on glass; white enamel lettering on glass; gilded glass lettering with a black shadow"),
 'neon': P("neon tube glowing pink; neon tube glowing blue; red neon tube; green neon tube; warm white neon tube; backlit coloured plastic letters"),
 'chalk': P("coloured chalk on a blackboard; white chalk on a slate; chalk and paint pen on a black board"),
 'metal': P("raised cast metal letters; pressed aluminium letters; stamped metal characters; painted steel letters"),
 'brass': P("individually mounted brass letters; engraved and filled brass; raised cast brass letters"),
 'plate': P("embossed enamel on steel; white enamel on a blue steel plate; black letters on a white enamel plate"),
 'paper': P("black ink on cream paper; marker pen on card; typed ink on a pale sheet; cut-out paper letters; printed paper pasted on a board; handwritten pen on a notepad page"),
 'wood': P("routed letters in painted wood; carved and gilded wood; gold-painted cut letters on a dark board"),
 'stone': P("carved stone letters; incised letters filled with black paint"),
 'cloth': P("painted letters on stretched cloth; stitched letters on a banner; printed vinyl banner letters"),
}
LETTER_MAT = [m for v in MATS.values() for m in v]
LETTER_COND = P("freshly painted and bright; faded by the sun; flaking in patches; partly peeled away; streaked with dirt running down from the top; missing some of its letters; dark where a bulb has failed in the middle; stained by rust bleeding from the bolts; covered in a thin layer of grime; overpainted in places; scratched and scuffed; newly installed and spotless; wet from the rain with bright reflections; yellowed with age; hung with one letter crooked; sprayed over by graffiti")
LETTER_LAYOUT = P("in one line across the top; stacked in two lines; arched in a curve above a small picture; set inside a bordered panel; with a swirling underline; centred under an emblem; on a diagonal; with a smaller line of text beneath it; framed by a thin double line; with a small star at each end")
SIGN_COLOUR = P("red letters on cream; white on dark green; gold on black; black on yellow; cream on navy blue; white on red; deep blue on pale yellow; black on white; orange on brown; pale pink on maroon; white on teal; black on orange")
SIGN_STRUCT = {
 'shop fascia': ('a long painted wooden board above a shop window', 'SHOP', ['paint', 'wood']),
 'hanging pub sign': ('a painted hanging pub sign swinging from an iron bracket', 'PUB', ['paint', 'wood']),
 'neon sign': ('a neon sign mounted in a window', 'SHOP', ['neon']),
 'billboard': ('a large roadside billboard on a steel frame', 'SLOGAN', ['paint', 'paper']),
 'chalkboard menu': ('a chalkboard menu stand on the pavement', 'MENU', ['chalk']),
 'painted wall sign': ('a large painted sign on a brick wall', 'SHOP', ['wallpaint']),
 'enamel plate': ('an enamel plate sign bolted to a wall', 'NOTICE', ['plate']),
 'street name plate': ('a street name plate on a corner wall', 'STREET', ['plate']),
 'notice on a door': ('a handwritten notice taped inside a glass door', 'NOTICE', ['paper']),
 'box sign': ('a lit box sign over a doorway', 'SHOP', ['neon']),
 'ship name board': ('a painted name board on the stern of a boat', 'SHIP', ['paint', 'wood']),
 'licence plate': ('a licence plate on the rear of a vehicle', 'PLATE', ['plate']),
 'banner': ('a cloth banner stretched across a street', 'SLOGAN', ['cloth']),
 'shop window lettering': ('lettering applied to a shop window glass', 'SHOP', ['glass']),
 'brass nameplate': ('a polished brass nameplate beside a door', 'SHOP', ['brass']),
 'roadside sign': ('a hand-painted sign on a wooden post at the edge of a road', 'NOTICE', ['paint', 'wood']),
}
WORD = {'SHOP': q(SHOP), 'PUB': q(PUB), 'SLOGAN': q(SLOGAN), 'MENU': q(MENU), 'NOTICE': q(NOTICE), 'STREET': q(STREET), 'SHIP': q(SHIP), 'PLATE': q(PLATE)}
FILL = {'SHOP': '"SHOP NAME"', 'PUB': '"PUB NAME"', 'SLOGAN': '"YOUR SLOGAN HERE"', 'MENU': '"DISH NAME 0.00"', 'NOTICE': '"YOUR NOTICE HERE"', 'STREET': '"STREET NAME"', 'SHIP': '"BOAT NAME"', 'PLATE': '"PLATE NUMBER"'}

def build_sign():
    G = {}
    G['letter_style'] = LETTER_STYLE; G['letter_material'] = LETTER_MAT; G['letter_condition'] = LETTER_COND; G['letter_layout'] = LETTER_LAYOUT
    G['letter_colour'] = SIGN_COLOUR
    G['text_shop_name'] = q(SHOP); G['text_pub_name'] = q(PUB); G['text_slogan'] = q(SLOGAN); G['text_notice'] = q(NOTICE); G['text_street'] = q(STREET)
    G['text_menu_item'] = q(MENU); G['text_ship_name'] = q(SHIP); G['text_plate'] = q(PLATE); G['text_brand'] = q(BRANDS); G['text_logo_emblem'] = LOGO
    G['text_product'] = PRODUCT; G['text_product_label'] = q(PRODUCT)
    G['sign_types'] = list(SIGN_STRUCT); refs = []
    for t, (struct, kind, mk) in SIGN_STRUCT.items():
        s = slug(t); G['sign_%s_material' % s] = [m for k in mk for m in MATS[k]]
        G['sign_%s_look' % s] = ['%s%s reading __text_%s__ in __letter_style__, in __sign_%s_material__, __letter_layout__.' % (struct[0].upper(), struct[1:], {'SHOP': 'shop_name', 'PUB': 'pub_name', 'SLOGAN': 'slogan', 'MENU': 'menu_item', 'NOTICE': 'notice', 'STREET': 'street', 'SHIP': 'ship_name', 'PLATE': 'plate'}[kind], s)]
        G['sign_%s_look_fill' % s] = ['%s%s reading %s in __letter_style__, in __sign_%s_material__, __letter_layout__.' % (struct[0].upper(), struct[1:], FILL[kind], s)]
        G['sign_%s_prompt' % s] = ['__sign_%s_look__ The colour scheme is __letter_colour__. The sign is __letter_condition__.' % s]
        G['sign_%s_prompt_fill' % s] = ['__sign_%s_look_fill__ The colour scheme is __letter_colour__. The sign is __letter_condition__.' % s]
        refs.append(s)
    G['signage_prompt'] = ['__sign_%s_prompt__' % s for s in refs]; G['signage_prompt_fill'] = ['__sign_%s_prompt_fill__' % s for s in refs]
    G['signage_look'] = ['__sign_%s_look__' % s for s in refs]
    G['sign_shopfront_prompt'] = ['A shop front for __text_shop_name__. The fascia board above the window has the name in __letter_style__, in __letter_material__, and the window glass has __text_slogan__ in smaller lettering. A hand-written card in the door says __text_notice__. The colour scheme is __letter_colour__. The whole front is __letter_condition__.']
    G['sign_street_scene_prompt'] = ['A short run of shops on __text_street__. The first has a sign reading __text_shop_name__, the second has a sign reading __text_shop_name__, and the third has a sign reading __text_shop_name__, each in a different lettering style. The signs are __letter_condition__.']
    G['v74_sign_entry_points'] = []
    return G

# ---------------------------------------------------------------- item 51 advertising signs
ERA = P("1890s; 1900s; 1910s; 1920s; 1930s; 1940s; 1950s; 1960s; 1970s; 1980s; 1990s; 2000s; 2010s; 2020s")
AD_KIND = {
 'enamel advertising sign': 'a heavy enamel sign with a rolled rim and four mounting holes',
 'tin advertising sign': 'a lithographed tin sign with embossed edges',
 'painted wall advertisement': 'a large faded advertisement painted directly on a brick wall',
 'neon advertising sign': 'a neon advertising sign with bent glass tubes on a metal backing',
 'light box sign': 'an illuminated light box sign with a plastic face',
 'roadside billboard': 'a large roadside billboard with a hand-painted face',
 'cardboard shop display': 'a freestanding cardboard shop display with a folding easel back',
 'mirror advertisement': 'a bar mirror with a printed advertisement and a bevelled edge',
 'delivery truck lettering': 'hand-painted lettering and a small picture on the side of a delivery van',
 'tram or bus advertisement': 'a long advertisement panel above the windows of a tram',
 'cinema poster': 'a large printed poster for a film behind a glass case',
 'trade calendar': 'a printed wall calendar from a local business with a picture above the dates',
 'wooden fence hoarding': 'a row of pasted paper posters on a wooden hoarding',
 'clock advertisement': 'a clock with an advertisement printed around its face',
 'thermometer sign': 'a tall thermometer sign with an advertisement printed above and below the scale',
 'flag or pennant': 'a string of triangular flags printed with a logo',
 'inflatable figure': 'a tall inflatable figure advertising a business',
 'window decal': 'a peeling sticker advertisement on a shop window',
}
AD_PRINT = {'enamel advertising sign': 'fired porcelain enamel', 'tin advertising sign': 'bright lithographed inks on tin', 'painted wall advertisement': 'hand-painted sign-writer paint on brick', 'neon advertising sign': 'glowing bent neon tubes', 'light box sign': 'backlit printed plastic', 'roadside billboard': 'large hand-painted panels', 'cardboard shop display': 'glossy printed card', 'mirror advertisement': 'enamel lettering fired onto mirrored glass', 'delivery truck lettering': 'hand-painted signwriting with gold shadow lettering', 'tram or bus advertisement': 'printed vinyl panels', 'cinema poster': 'printed paper with a bold illustration', 'trade calendar': 'colour-printed paper', 'wooden fence hoarding': 'layers of pasted printed paper', 'clock advertisement': 'printed face lettering around the dial', 'thermometer sign': 'enamelled metal with a painted scale', 'flag or pennant': 'printed cloth', 'inflatable figure': 'printed vinyl', 'window decal': 'printed adhesive vinyl'}
AD_COND = P("pristine and glossy; chipped around the bolt holes; faded to pale colours; heavily rusted with only part of the picture visible; scratched and sun-bleached; torn and re-pasted in places; dented and bent; ghostly and half-washed by weather; spotless and newly installed; stained by water streaks; peeling at one corner; covered in lichen and moss")
AD_SCENE = P("a smiling child holding the product; a family at a table with the product in the centre; a hand-drawn picture of the product with sunbeams behind it; a bold close-up of the product and a price; a farmer in a field; a glamorous woman beside a car; a smiling cook in a tall hat; a cartoon mascot waving; a mountain landscape behind a large product name; a steam engine pulling into a station; a ship leaving a harbour; a row of lined-up products on a shelf; an athlete with a large product; an animal holding the product")
def build_ads():
    G = {}
    G['ad_era'] = ERA; G['ad_condition'] = AD_COND; G['ad_scene'] = AD_SCENE
    G['ad_kinds'] = list(AD_KIND); G['ad_slogan'] = q(SLOGAN)
    G['ad_text'] = ['__text_brand__ and __text_slogan__']
    refs = []
    for t, d in AD_KIND.items():
        s = slug(t)
        G['ad_%s_look' % s] = ['An advertisement, %s, from the __ad_era__, for __text_product__ with the brand name __text_brand__ in __letter_style__, made of %s, with the line __text_slogan__ and a picture of __ad_scene__, with a logo of __text_logo_emblem__.' % (d, AD_PRINT[t])]
        G['ad_%s_look_fill' % s] = ['An advertisement, %s, from the __ad_era__, for "PRODUCT" with the brand name "BRAND NAME" in __letter_style__, made of %s, with the line "YOUR SLOGAN HERE" and a picture of __ad_scene__, with a logo of __text_logo_emblem__.' % (d, AD_PRINT[t])]
        G['ad_%s_prompt' % s] = ['__ad_%s_look__ The advertisement is __ad_condition__.' % s]
        G['ad_%s_prompt_fill' % s] = ['__ad_%s_look_fill__ The advertisement is __ad_condition__.' % s]
        refs.append(s)
    G['ad_prompt'] = ['__ad_%s_prompt__' % s for s in refs]; G['ad_prompt_fill'] = ['__ad_%s_prompt_fill__' % s for s in refs]
    G['ad_wall_scene_prompt'] = ['A brick wall on __text_street__ with two layers of old painted advertisements, one for __text_brand__ and one for __text_brand__, each showing __ad_scene__. Both are __ad_condition__.']
    return G

# ---------------------------------------------------------------- item 52 tins and labelled containers
TIN = {
 'biscuit tin': 'a rectangular biscuit tin with a hinged lid',
 'tea caddy': 'a tall tea caddy with a slip-on lid',
 'sweet tin': 'a round sweet tin with a screw lid',
 'cocoa tin': 'a cylindrical cocoa tin with a pressed-in lid',
 'tobacco tin': 'a flat pocket tobacco tin with a hinged lid',
 'sardine tin': 'a small flat sardine tin with a pull-off key lid',
 'paint can': 'a metal paint can with a wire handle and a press-fit lid',
 'oil can': 'a tall oil can with a spout',
 'spice tin': 'a small screw-top spice tin',
 'mint tin': 'a tiny hinged mint tin',
 'cigar box': 'a wooden cigar box with a printed lid',
 'matchbox': 'a cardboard matchbox with a striking strip',
 'glass jar': 'a glass jar with a metal lid and a paper label',
 'glass bottle': 'a glass bottle with a cork stopper and a paper label',
 'bottle with embossed glass': 'a bottle with raised lettering in the glass and a paper label',
 'cardboard carton': 'a printed cardboard carton with folded flaps',
 'cylinder canister': 'a cardboard canister with a metal base and a pull-off lid',
 'squeezable tube': 'a metal squeezable tube with a crimped end',
 'pill bottle': 'a small brown pill bottle with a child-proof lid and a typed label',
 'food can': 'a modern steel food can with a wrapped paper label',
 'drinks can': 'an aluminium drinks can with printed graphics',
 'milk bottle': 'a glass milk bottle with a foil top',
 'enamel storage tin': 'an enamel storage tin with a stencilled word on the side',
 'plastic tub': 'a plastic tub with a snap-on lid and a printed wrap-around label',
 'cardboard box with window': 'a cardboard box with a clear window and printed lid',
 'wooden crate': 'a wooden crate with stencilled markings on the end',
 'burlap sack': 'a burlap sack with stencilled lettering',
 'paper bag': 'a printed paper bag with a folded top',
}
LABEL_B = P("a net weight line near the bottom; a short line of directions in small print; an ingredients panel in small type; a small \"Established\" line with a year; a row of stars; a rectangle for a price; a picture of the factory; a small royal-style crest; a gold medal printed beside the name")
LABEL_ELEMENT = P("a large brand name across the top; a circular emblem in the centre; a banner reading the product name; a decorative border of leaves; an illustration of the product on the front; a stripe in a contrasting colour across the middle; a wide ribbon across the front")
LABEL_PRINT = P("lithographed in rich colours; letterpress printed in two colours; embossed in the metal; printed in flat bright inks; screen printed in bold colours; transfer printed; hand-applied paper label in a single ink; foil-stamped in gold; photographed and printed in glossy full colour; stencilled in black paint; printed with a halftone picture; debossed into the surface")
CONT_COND = P("shiny and unmarked; dented along one side; rusted around the lid; scratched and rubbed at the edges; faded by the sun; peeling at the label; chipped to bare metal in places; stained and sticky; opened and half-empty; sealed and unopened; dented with a rust bloom; marked with a price sticker; missing its lid; polished and well kept; crushed at one corner; scuffed with the lettering half rubbed away")
CONT_NET = P("Net Weight 4 oz; Net Weight 500 g; Contents 1 lb; Contents 250 g; 12 fl oz; 350 ml; Packed in the City; Best Before See Lid; Keep in a Cool Dry Place; Shake Well; Product of the Region; Fresh Packed; Genuine Article; Use Within 3 Days of Opening; Handle with Care")
def build_tins():
    G = {}
    G['container_label_element'] = LABEL_ELEMENT; G['container_label_element_b'] = LABEL_B; G['container_print'] = LABEL_PRINT; G['container_condition'] = CONT_COND; G['container_net'] = q(CONT_NET)
    G['container_kinds'] = list(TIN); refs = []
    for t, d in TIN.items():
        s = slug(t)
        G['container_%s_look' % s] = ['%s%s from the __ad_era__, labelled with the brand __text_brand__ for __text_product__, with the line __text_slogan__ and the small print __container_net__. The label has __container_label_element__ and __container_label_element_b__, with a picture of __text_logo_emblem__, %s.' % (d[0].upper(), d[1:], '__container_print__')]
        G['container_%s_look_fill' % s] = ['%s%s from the __ad_era__, labelled with the brand "BRAND NAME" for "PRODUCT", with the line "YOUR SLOGAN HERE" and the small print "NET WEIGHT". The label has __container_label_element__ and __container_label_element_b__, with a picture of __text_logo_emblem__, %s.' % (d[0].upper(), d[1:], '__container_print__')]
        G['container_%s_phrase' % s] = [G['container_%s_look' % s][0][0].lower() + G['container_%s_look' % s][0][1:].rstrip('.')]
        G['container_%s_prompt' % s] = ['__container_%s_look__ It is __container_condition__.' % s]
        G['container_%s_prompt_fill' % s] = ['__container_%s_look_fill__ It is __container_condition__.' % s]
        refs.append(s)
    G['container_prompt'] = ['__container_%s_prompt__' % s for s in refs]; G['container_prompt_fill'] = ['__container_%s_prompt_fill__' % s for s in refs]
    G['container_shelf_prompt'] = ['A shelf of old labelled containers. The first is __container_biscuit_tin_phrase__. The second is __container_glass_jar_phrase__. The third is __container_sardine_tin_phrase__. They are __container_condition__.']
    G['container_pantry_prompt'] = ['A pantry shelf with a row of mixed tins and bottles. One tin is labelled __text_brand__ and another is labelled __text_brand__, and a jar has a handwritten label reading __text_product_label__. The containers are __container_condition__.']
    return G

def build(final=None):
    G = build_sign(); G.update(build_ads()); G.update(build_tins())
    G['v74_sign_entry_points'] = ['signage_prompt', 'signage_prompt_fill', 'sign_shopfront_prompt', 'sign_street_scene_prompt', 'ad_prompt', 'ad_prompt_fill', 'ad_wall_scene_prompt', 'container_prompt', 'container_prompt_fill', 'container_shelf_prompt', 'container_pantry_prompt']
    return G
