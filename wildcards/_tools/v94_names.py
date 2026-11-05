"""v94 - fake name system: parts -> name builders -> sign/label/packaging prompts with defined quoted text."""
import os, sys, re, random, itertools
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
R = random.Random(9400)
def uniq(l): return list(dict.fromkeys(x for x in l if x))
def pick(l, n):
    l = list(l); R.shuffle(l); return l[:n]
# ---------- parts ----------
ONS = 'B D F G K L M N P R S T V Z Br Dr Fl Gr Kl Pr Tr St Sh Ch Cl Fr Gl Pl Sk Sp Th Qu Hal Mar'.split()
ONS = [o for o in ONS if len(o) < 3]
ONS_PLAIN = 'B D F G K L M N P R S T V Z H J'.split()
VOW = 'a e i o u a e i o'.split()
ENDS_LAT = 'ova ora ana ica ella ino ato ero ia ium ara ula ona ela iro uno ado'.split()
ENDS_NOR = 'vik by gard sund heim stad lund fjord holm ness vang'.split()
ENDS_GER = 'burg stein werk haus feld berg bach mann dorf tal'.split()
ENDS_TECH = 'ix ex ify ly on yx eon io ia ox ar el ent'.split()
ENDS_JAP = 'ro ki mi ta ko ma na ru sa no'.split()
def syl(n=1):
    return ''.join(R.choice(ONS) + R.choice(VOW) for _ in range(n))
BLOCK = re.compile(r'(?i)(fuck|shit|cunt|dick|cock|piss|rape|nazi|kill|dead|anal|ass|tit|sex|porn|hell|damn|cum|fag|kike|spic|coon|nig|pedo|hitler|isis)')
def clean_brand(w): return w if 5 <= len(w) <= 10 and not re.search(r'[bcdfghjklmnpqrstvwxz]{4}', w.lower()) and not re.search(r'(.)\1', w.lower()) and not BLOCK.search(w) and not re.search(r'(.)\1\1', w) else None
PRE = 'Al Ar Av Bel Cal Cor Dal Del Den Dor El Em Fal Fen Gal Hal Ian Jor Kal Kel Lan Lor Lum Mal Mar Mel Mir Nal Nor Ol Or Pal Pen Quin Ral Ren Sal Sel Sol Tal Tar Tel Tor Ul Val Var Vel Ver Vor Wen Zan Zel Zen Zor Ast Bran Cass Dex Fex Gran Hex Jax Kor Lex Max Nex Pax Rex Sax Tex Vax Zex Bol Cam Dar Fin Gem Hob Kin Lev Mon Nev Ody Pol Rob Sab Tam Vin'.split()
def make(endings, nsyl=(1, 1), n=400):
    out = []
    for _ in range(n * 6):
        w = R.choice(PRE)
        w = w + R.choice(endings)
        w = clean_brand(w)
        if w: out.append(w)
    return uniq(out)[:n]
SURN_A = 'Ash Brook Cald Dun Elm Fair Glen Hart Kirk Lang Marl North Oak Pen Quar Ridge Stan Thorn Wex Yar Bram Cross Dray Eld Fen Gar Hol Ings Jar Lyn Mor Nor Orm Pres Rad Sed Tan Ulb Vane Wend Alder Bar Cob Den Fos Gre Hav Ket Lud Mer Nel Pol Rav Sal Tar Wil'.split()
SURN_B = 'by ton ford wick ham worth dale mere combe field well stead den ley bury shaw hurst thorpe wood ridge land more'.split()
def surnames(n):
    out = []
    for a in SURN_A:
        for b in SURN_B: out.append(a + b)
    R.shuffle(out); return out[:n]
FIRST = ('Aaron Abigail Adrian Alma Amara Andre Anika Antonio Arlo Beatrix Benedict Bianca Bram Calla Carmen Cassidy Cedric Celia Clara Cormac Dagny Dara Darius Delphine Desmond Dominic Edith Elias Elena Emeka Esme '
 'Fabian Farah Felix Fiona Gideon Greta Gus Hana Harriet Hector Helena Idris Imogen Ingrid Isidore Jonah Josefina Kai Kamala Karl Leandro Lena Lorenzo Lucia Magnus Mara Marcus Mei Milo Mirela Nadia Naveen Nell Nico '
 'Odette Olga Omar Orla Otto Pablo Petra Priya Quentin Rafael Ravi Renata Rhys Rosa Salma Sasha Silas Soren Tamsin Teodor Thea Tobias Uma Valentina Viktor Wanda Wilhelm Xavier Yusuf Zara Zoltan').split()
WORDS = ('Anchor Amber Arbor Atlas Aurora Badger Beacon Birch Bluebell Bramble Brook Cedar Cinder Clover Cobalt Compass Copper Coral Crane Crest Cypress Daisy Dawn Dune Eagle Ember Falcon Fern Finch Flint Fox Garnet Gull Harbor '
 'Hawthorn Heron Hollow Indigo Iron Ivory Jasper Juniper Kestrel Lantern Larch Laurel Linden Lotus Magnolia Maple Marigold Meadow Mill Mistral Moss Oak Olive Orchard Otter Pebble Pine Plover Poppy Quill Raven Reed Ridge Robin Rowan Saffron '
 'Sage Salt Sable Sparrow Spruce Summit Swallow Sycamore Thistle Timber Tulip Valley Violet Walnut Willow Wren Yarrow Zephyr Harvest Lighthouse Meridian Pioneer Northstar Silverline Goldleaf Redwood Stonebridge Brightwater').split()
TRADE_SHOP = ('Hardware|Bakery|Pharmacy|Bookshop|Butcher|Grocer|Florist|Tailor|Tyres|Cycles|Electrical|Furniture|Shoes|Toys|Stationers|Jewellers|Opticians|Barbers|Laundry|Fishmonger|Greengrocer|Delicatessen|Cafe|Tea Rooms|Music|Camera Shop|Pet Supplies|Garden Centre|Paint and Decorating|Cheesemonger|Sweets|Haberdashery|Watch Repair|Records|Antiques|Outfitters|Pawnbroker|Post Office|Hat Shop|Print Shop').split('|')
TRADE_FOOD = ('Diner|Bistro|Trattoria|Cantina|Noodle House|Grill|Kitchen|Taproom|Brasserie|Tavern|Pizzeria|Steakhouse|Ramen Bar|Dumpling House|Smokehouse|Coffee House|Tea House|Chippy|Creamery|Cocktail Bar|Wine Bar|Oyster Bar|Curry House|Tapas Bar|Burger Joint').split('|')
TRADE_CORP = ('Industries|Logistics|Systems|Dynamics|Holdings|Partners|Labs|Foods|Motors|Electronics|Textiles|Chemicals|Shipping|Freight|Energy|Insurance|Capital|Pharmaceuticals|Brewing|Steelworks|Aerospace|Paper|Telecom|Media|Foundry|Instruments|Provisions|Packaging|Plastics|Optics|Robotics|Software|Appliances|Cosmetics|Tobacco|Distillers|Mills|Engineering|Aviation').split('|')
CORP_SUF = ['Inc.', 'Ltd.', 'Co.', 'Corp.', 'LLC', 'Group', 'PLC', 'GmbH', '& Sons', '& Co.', 'and Partners', 'International', 'Worldwide', 'Limited', 'S.A.', 'AB', 'Pty Ltd', 'Holdings']
SHOP_SUF = ['Store', 'Shop', 'Market', 'Emporium', 'Outlet', 'Mart', 'Depot', 'Supply', 'Exchange', 'Warehouse', 'Trading Post', 'General Store', 'Superstore', 'Boutique', 'Centre']
PGROUPS = {
 'soft': ('Cola|Lemonade|Ginger Beer|Sparkling Water|Iced Tea|Energy Drink|Sports Drink|Orange Soda', ['330 ml', '500 ml', '1 litre', '12 fl oz', '6 pack', '2 litres'], ['Original', 'Zero', 'Light', 'Classic', 'Extra Cold', 'Family Size'], 1),
 'sweet': ('Cereal|Granola Bars|Chocolate Bar|Biscuits|Jam|Ice Cream|Yoghurt|Cookies|Popcorn|Mints|Chewing Gum|Syrup|Pancake Mix', ['Net Wt 100 g', 'Net Wt 250 g', 'Net Wt 500 g', 'Net Wt 12 oz', 'Net 340 g', '24 count'], ['Original', 'Classic', 'Family Size', 'Mini', 'Deluxe', 'Value Pack'], 1),
 'savoury': ('Crisps|Soup|Baked Beans|Pasta Sauce|Instant Noodles|Ketchup|Mustard|Salsa|Hot Sauce|Crackers|Pretzels|Canned Tuna|Sardines|Frozen Peas|Fish Fingers|Rice|Flour|Peanut Butter|Olive Oil|Pickles', ['Net Wt 250 g', 'Net Wt 500 g', 'Net Wt 1 kg', 'Net Wt 16 oz', 'Net 340 g', '500 ml'], ['Original', 'Classic', 'Family Size', 'Organic', 'Traditional', 'Mild', 'Spiced', 'Smoked', 'Value Pack'], 0),
 'spirit': ('Beer|Lager|Cider|Whisky|Gin|Vodka|Ale|Stout|Rum', ['330 ml', '500 ml', '750 ml', '700 ml', '1 litre', '6 pack'], ['Reserve', 'Select', 'Gold', 'Premium', 'Limited Batch', 'Classic', 'Export', 'Special'], 0),
 'household': ('Laundry Detergent|Dish Soap|Shampoo|Toothpaste|Hand Cream|Soap Bar|Glass Cleaner|Bleach|Deodorant|Sunscreen|Insect Repellent|Face Powder|Perfume', ['500 ml', '1 litre', '250 ml', '100 ml', 'Net Wt 100 g', '50 tablets'], ['Fresh', 'Sensitive', 'Ultra', 'Family Size', 'Extra Strong', 'Mild', 'Value Pack'], 1),
 'other': ('Motor Oil|Paint|Glue|Batteries|Light Bulbs|Matches|Candles|Writing Paper|Ink|Pencils|Crayons|Fertiliser|Tea Bags|Coffee|Hot Cocoa|Bandages|Vitamins|Cough Syrup', ['6 pack', '24 count', '100 sheets', '1 litre', '250 ml', '50 tablets'], ['Original', 'Classic', 'Extra Strong', 'Premium', 'Value Pack', 'Heavy Duty'], 0)}
PROD = [x for g in PGROUPS.values() for x in g[0].split('|')]
VARIANT = ['Original', 'Classic', 'Extra Strong', 'Light', 'Zero', 'Family Size', 'Double Strength', 'Reserve', 'Select', 'Gold', 'Premium', 'Mild', 'Spiced', 'Smoked', 'Fresh', 'Organic', 'Traditional', 'Deluxe', 'Winter Blend', 'Summer Edition', 'Limited Batch', 'Cask Strength', 'Sensitive', 'Ultra', 'Mini', 'Value Pack']
FLAVOUR = ['Lemon', 'Lime', 'Cherry', 'Honey', 'Mint', 'Vanilla', 'Peach', 'Blackcurrant', 'Apple', 'Ginger', 'Cinnamon', 'Mango', 'Raspberry', 'Coconut', 'Chilli', 'Maple', 'Pear', 'Plum', 'Lavender', 'Sea Salt']
STREET = 'High|Mill|Station|Church|Market|Bridge|Harbour|Park|Queen|King|Orchard|Chapel|Castle|Elm|Oak|Canal|Union|Victoria|Albert|Quarry|Meadow|Old|North|South|East|West|Water|Bank|Garden|School Lane'.split('|')
STREET = [s for s in STREET if s != 'School Lane']
STYPE = ['Street', 'Road', 'Lane', 'Avenue', 'Way', 'Row', 'Terrace', 'Square', 'Close', 'Place', 'Parade', 'Court']
HOURS = ['Open 9 to 5', 'Open 7 days', 'Open daily 8am to 8pm', 'Mon to Sat 9 to 6', 'Open late', 'Open 24 hours', 'Closed Sundays', 'Open 10 to 4', 'Open from 6am', 'Weekdays 8 to 5']
TAGS = ['Since', 'Est.', 'Established', 'Founded', 'Family run since', 'Serving you since']
SLOG = ['Quality you can trust', 'Fresh every day', 'Made with care', 'Good value always', 'The local favourite', 'Honest goods, fair prices', 'Built to last', 'Simply the best', 'Taste the difference', 'Your neighbourhood choice', 'Proudly made here', 'Pure and simple', 'Always open to you', 'Service with a smile', 'Crafted by hand', 'Just what you need', 'Better every day', 'For every home', 'Made to be shared', 'Where good things begin', 'Nothing but the best', 'From our door to yours', 'Tried and tested', 'The real thing', 'Small batch, big flavour', 'Straight from the farm', 'Ready when you are', 'Clean, bright, done', 'Warm welcome guaranteed', 'Good food, good company']
def G_parts():
    G = {}
    G['name_stem_latin'] = make(ENDS_LAT, (1, 2), 300)
    G['name_stem_nordic'] = make(ENDS_NOR, (1,), 220)
    G['name_stem_german'] = make(ENDS_GER, (1,), 220)
    G['name_stem_tech'] = make(ENDS_TECH, (1, 1, 2), 300)
    G['name_stem_japanese'] = [x for x in uniq(syl(2).capitalize() + R.choice(ENDS_JAP) if False else (R.choice('K S T N H M R Y Sh Ch'.split()) + R.choice('a i u o'.split()) + R.choice('k n r m t s'.split()) + R.choice('a i u o'.split()) + R.choice(ENDS_JAP)) for _ in range(900)) if not BLOCK.search(x)][:200]
    G['name_surname'] = surnames(240)
    G['name_first'] = FIRST
    G['name_word'] = WORDS
    G['name_trade_shop'] = TRADE_SHOP
    G['name_trade_food'] = TRADE_FOOD
    G['name_trade_corp'] = TRADE_CORP
    G['name_suffix_corp'] = CORP_SUF
    G['name_suffix_shop'] = SHOP_SUF
    for g, (types, wts, vars_, flv) in PGROUPS.items():
        G['name_type_' + g] = types.split('|'); G['name_weight_' + g] = wts; G['name_variant_' + g] = vars_
    G['name_product_type'] = ['__name_type_%s__' % g for g in PGROUPS]
    G['name_variant'] = VARIANT
    G['name_flavour'] = FLAVOUR
    G['name_street'] = STREET
    G['name_street_type'] = STYPE
    G['name_hours'] = HOURS
    G['name_tagline'] = SLOG
    G['name_year'] = [str(y) for y in range(1840, 2011, 3)]
    G['name_number_small'] = [str(n) for n in range(1, 120)]
    G['name_initials'] = uniq(''.join(R.choice('ABCDEFGHJKLMNOPRSTVWZ') for _ in range(R.choice((2, 3)))) for _ in range(200))
    G['name_weight'] = ['Net Wt 250 g', 'Net Wt 500 g', 'Net Wt 1 kg', '330 ml', '500 ml', '1 litre', '750 ml', 'Net Wt 12 oz', 'Net Wt 16 oz', '12 fl oz', 'Net 100 g', 'Net 340 g', '2 pints', '6 pack', '24 count', '100 sheets', '50 tablets']
    G['name_price'] = ['$1.49', '$2.99', '$3.49', '$4.99', '$5.75', '$7.50', '$9.99', '$12.00', '£1.20', '£2.45', '£3.99', '£6.50', '€1.80', '€3.20', '€4.95', '1.25', '2.60', '0.99', '15.00', '8.40']
    G['name_phone'] = ['Tel 555 0142', 'Tel 555 0178', 'Tel 555 0199', 'Phone 555 0121', 'Call 555 0163', 'Tel 555 0107', 'Phone 555 0186', 'Call 555 0134', 'Tel 555 0155', 'Phone 555 0192']
    G['name_batch'] = ['Batch 4821', 'Batch 0372', 'Lot 77A', 'Lot 5310', 'Batch 12', 'Lot B204', 'Batch 9906', 'Lot 31C', 'Batch 6014', 'Lot 8827']
    G['name_best_before'] = ['Best before 03/28', 'Best before 11/27', 'Best before 06/29', 'Use by 09/27', 'Best before 01/28', 'Use by 12/28']
    return G
# ---------- builders ----------
def G_names(P):
    G = {}
    flav = ['latin', 'nordic', 'german', 'tech', 'japanese']
    for f in flav: G['name_brand_' + f] = ['__name_stem_%s__' % f]
    G['name_brand_invented'] = ['__name_brand_%s__' % f for f in flav]
    G['name_brand_wordpair'] = ['__name_word__ __name_word__', '__name_word__ & __name_word__', 'The __name_word__ __name_word__', '__name_word__ __name_surname__', '__name_word__ __name_stem_tech__']
    G['name_brand_surname'] = ['__name_surname__', '__name_surname__ & __name_surname__', '__name_surname__ and __name_surname__', '__name_surname__ __name_surname__', "__name_surname__'s"]
    G['name_brand_initials'] = ['__name_initials__', '__name_initials__ __name_stem_tech__', '__name_initials__ __name_number_small__']
    G['name_brand'] = ['__name_brand_invented__'] * 5 + ['__name_brand_wordpair__'] * 2 + ['__name_brand_surname__'] * 2 + ['__name_brand_initials__']
    # --- uppercase static variant: expanded from the stems
    up = [s.upper() for s in P['name_stem_latin'][:100] + P['name_stem_nordic'][:60] + P['name_stem_german'][:60] + P['name_stem_tech'][:100] + P['name_stem_japanese'][:60]]
    G['name_brand_upper'] = uniq(up)
    G['name_company'] = ['__name_brand__ __name_suffix_corp__', '__name_brand_invented__ __name_trade_corp__', '__name_brand_invented__ __name_trade_corp__ __name_suffix_corp__', '__name_brand_surname__ __name_trade_corp__', '__name_brand_wordpair__ __name_trade_corp__ __name_suffix_corp__', '__name_brand_initials__ __name_trade_corp__', '__name_brand_invented__ Group', '__name_brand_invented__ __name_suffix_corp__', 'The __name_brand_wordpair__ Company', '__name_brand_surname__ __name_suffix_corp__']
    G['name_shop'] = ['__name_surname__\'s __name_trade_shop__', '__name_brand_surname__ __name_trade_shop__', '__name_brand_invented__ __name_suffix_shop__', '__name_brand_wordpair__ __name_trade_shop__', 'The __name_word__ __name_trade_shop__', '__name_surname__ & Sons __name_trade_shop__', '__name_brand_invented__ __name_trade_shop__', '__name_first__\'s __name_trade_shop__', '__name_brand_wordpair__ __name_suffix_shop__', '__name_surname__ __name_suffix_shop__', '__name_word__ __name_suffix_shop__', 'The __name_brand_invented__ __name_suffix_shop__']
    G['name_restaurant'] = ['__name_surname__\'s __name_trade_food__', 'The __name_word__ __name_trade_food__', '__name_brand_invented__ __name_trade_food__', '__name_brand_wordpair__ __name_trade_food__', '__name_first__\'s __name_trade_food__', '__name_word__ & __name_word__', 'Café __name_brand_latin__', '__name_brand_nordic__ __name_trade_food__', '__name_brand_japanese__ __name_trade_food__']
    G['name_pub'] = ['The __name_word__ and __name_word__', 'The __name_word__ Arms', 'The Old __name_word__', 'The __name_surname__ Arms', 'The __name_word__ Inn', 'The Golden __name_word__', 'The Royal __name_word__', 'The Three __name_word__s']
    G['name_product_brand'] = ['__name_brand_invented__', '__name_brand_wordpair__', '__name_brand_surname__', '__name_brand_invented__', '__name_brand_upper__']
    G['name_product'] = ['__name_product_%s__' % g for g in PGROUPS]
    for g, (types, wts, vars_, flv) in PGROUPS.items():
        T = '__name_type_%s__' % g; V = '__name_variant_%s__' % g
        G['name_product_' + g] = ['__name_product_brand__ ' + T, '__name_product_brand__ ' + T + ' ' + V, '__name_product_brand__ ' + V + ' ' + T] + (['__name_product_brand__ __name_flavour__ ' + T] if flv else [])
        G['name_product_line2_' + g] = [T, V + ' ' + T] + (['__name_flavour__ ' + T, '__name_flavour__'] if flv else [])
    G['name_product_line2'] = ['__name_product_line2_%s__' % g for g in PGROUPS]
    G['name_person'] = ['__name_first__ __name_surname__']
    G['name_person_title'] = ['Dr __name_surname__', 'Mr __name_surname__', 'Ms __name_surname__', 'Mrs __name_surname__', 'Professor __name_surname__', 'Captain __name_surname__', '__name_first__ __name_surname__']
    G['name_address'] = ['__name_number_small__ __name_street__ __name_street_type__', '__name_number_small__ __name_surname__ __name_street_type__', '__name_number_small__ __name_word__ __name_street_type__']
    G['name_established'] = ['Est. __name_year__', 'Since __name_year__', 'Established __name_year__', 'Founded __name_year__', 'Family run since __name_year__']
    G['name_book_title'] = ['The __name_word__ __name_word__', 'A Year at __name_surname__', 'The Last __name_word__', 'Beyond the __name_word__', 'The __name_surname__ Affair', '__name_word__ Hill', 'Letters from __name_brand_latin__', 'The Secret of __name_surname__ House', 'Songs of the __name_word__', 'Winter at __name_brand_nordic__']
    G['name_ship'] = ['__name_word__ __name_word__', 'The __name_word__', 'Spirit of __name_brand_latin__', '__name_first__ __name_surname__', 'Star of __name_brand_latin__', '__name_surname__ Queen']
    G['name_town'] = ['__name_surname__', '__name_surname__ __name_street_type__', 'New __name_surname__', 'Port __name_brand_latin__', 'Upper __name_surname__', 'Lower __name_surname__', '__name_brand_nordic__']
    return G
# ---------- text-bearing prompts (quoted, one line each, no other text) ----------
Q = lambda x: '"' + x + '"'
def G_prompts():
    G = {}
    NOMORE = ' No other words or letters appear.'
    def add(n, lines): G[n] = uniq(lines)
    N = '"__name_shop__"'
    add('name_sign_shopfront_prompt', [
        'A shopfront with a painted fascia sign carrying the words ' + N + ' on the first line and "__name_established__" on the second line.' + NOMORE,
        'A shop fascia in __letter_style__ lettering reading ' + N + ', with a small line beneath it reading "__name_hours__".' + NOMORE,
        'A shop window with gold lettering on the glass reading ' + N + ' on the first line and "__name_address__" on the second line.' + NOMORE,
        'A hanging shop sign on an iron bracket showing the words ' + N + ' and a simple painted emblem.' + NOMORE,
        'A shop front with a lit box sign above the door reading ' + N + ', and an open sign on the door reading "OPEN".' + NOMORE])
    add('name_sign_company_prompt', [
        'A tall office building with large metal letters on its facade reading "__name_company__".' + NOMORE,
        'A brushed steel plaque beside a glass door with the words "__name_company__" on the first line and "__name_address__" on the second line.' + NOMORE,
        'A factory gate with a painted sign reading "__name_company__" on the first line and "__name_tagline__" on the second line.' + NOMORE,
        'A roadside billboard showing "__name_company__" in large letters and "__name_tagline__" beneath it.' + NOMORE,
        'A warehouse wall with big painted letters reading "__name_company__" and a smaller line reading "__name_phone__".' + NOMORE])
    add('name_sign_restaurant_prompt', [
        'A neon sign in a restaurant window reading "__name_restaurant__".' + NOMORE,
        'A chalkboard by the entrance with the words "__name_restaurant__" on the first line and "__name_hours__" on the second line.' + NOMORE,
        'A hanging pub sign painted with a simple emblem and the words "__name_pub__".' + NOMORE,
        'A restaurant awning with lettering reading "__name_restaurant__" and a menu board beside the door headed "__name_restaurant__".' + NOMORE,
        'A cafe window with the words "__name_restaurant__" in curved gold letters on the glass and "__name_established__" beneath.' + NOMORE])
    for g in PGROUPS:
        W = '__name_weight_%s__' % g
        add('name_label_product_%s_prompt' % g, [
            'A product label with the words "__name_product_brand__" on the first line, "__name_type_%s__" on the second line, and "%s" on the third line.' % (g, W) + NOMORE,
            'A package with a wrap-around label reading "__name_product_%s__" on the first line and "%s" on the second line.' % (g, W) + NOMORE,
            'A package front printed with "__name_product_brand__" in large letters, "__name_product_line2_%s__" below it, and "%s" at the bottom.' % (g, W) + NOMORE,
            'A cardboard box front printed with "__name_product_brand__" on the first line, "__name_product_line2_%s__" on the second line, and "__name_tagline__" on the third line.' % g + NOMORE,
            'A shelf of three identical packages, each labelled "__name_product_%s__" and nothing else.' % g])
    add('name_label_product_prompt', ['__name_label_product_%s_prompt__' % g for g in PGROUPS] + [
        'A shipping carton with a stencilled line reading "__name_company__" and a second line reading "__name_batch__".' + NOMORE,
        'A jar with a round lid label reading "__name_product_brand__" on the first line and "__name_flavour__" on the second line, and a small paper tag reading "__name_batch__".' + NOMORE])
    add('name_label_price_prompt', [
        'A small paper price tag tied to the item, with the words "__name_product_type__" on the first line and "__name_price__" on the second line.' + NOMORE,
        'A shelf edge label with the words "__name_product__" on the first line and "__name_price__" on the second line.' + NOMORE,
        'A hand-written card in a market stall reading "__name_product_type__" and "__name_price__".' + NOMORE,
        'A date sticker on the pack reading "__name_best_before__" and nothing else.'])
    add('name_tag_person_prompt', [
        'A name badge pinned to a jacket, with the words "__name_person__" on the first line and "__name_company__" on the second line.' + NOMORE,
        'A brass door plate reading "__name_person_title__" on the first line and "__name_address__" on the second line.' + NOMORE,
        'A business card with the words "__name_person__" on the first line, "__name_company__" on the second line and "__name_phone__" on the third line.' + NOMORE,
        'A luggage tag with the words "__name_person__" on the first line and "__name_town__" on the second line.' + NOMORE,
        'A desk nameplate reading "__name_person_title__".' + NOMORE])
    add('name_tag_clothing_prompt', [
        'A small woven label sewn inside the garment, with the words "__name_brand_invented__" on the first line and "__name_town__" on the second line.' + NOMORE,
        'A leather patch stitched on the garment with the words "__name_brand_invented__" burned into it.' + NOMORE,
        'A hang tag on a string with the words "__name_brand_invented__" on the first line and "__name_price__" on the second line.' + NOMORE,
        'A metal button engraved with the words "__name_brand_invented__".' + NOMORE])
    add('name_vehicle_livery_prompt', [
        'A delivery van with the words "__name_company__" painted on its side and "__name_phone__" painted beneath.' + NOMORE,
        'A lorry with a painted side panel reading "__name_company__" on the first line and "__name_tagline__" on the second line.' + NOMORE,
        'A bus with a side advertisement reading "__name_shop__" on the first line and "__name_address__" on the second line.' + NOMORE,
        'A cargo ship with white letters on the hull reading "__name_company__" and its name "__name_ship__" at the bow.' + NOMORE,
        'A shipping container with the words "__name_company__" in large letters on its side.' + NOMORE])
    add('name_poster_prompt', [
        'A poster on a wall with the words "__name_product__" in large letters at the top and "__name_tagline__" below.' + NOMORE,
        'A poster in a shop window reading "__name_shop__" on the first line and "__name_hours__" on the second line.' + NOMORE,
        'A book on a table with the title "__name_book_title__" on its cover and nothing else.' + NOMORE,
        'A street map board headed "__name_town__" with no other readable text.',
        'A wooden road sign pointing the way, reading "__name_town__" on the first line and "__name_number_small__ miles" on the second line.' + NOMORE])
    add('name_receipt_prompt', [
        'A paper receipt on a counter with the words "__name_shop__" on the first line, "__name_address__" on the second line and "__name_price__" on the third line.' + NOMORE,
        'A letterhead on a desk with the words "__name_company__" on the first line and "__name_address__" on the second line.' + NOMORE,
        'A shop bag with the words "__name_shop__" printed on the front.' + NOMORE,
        'A matchbox with the words "__name_restaurant__" on the first line and "__name_town__" on the second line.' + NOMORE,
        'A coffee cup with the words "__name_restaurant__" printed on the sleeve.' + NOMORE])
    add('name_blank_text_prompt', [
        'A shop sign, label or packaging with plain shapes and patterns only, and no readable words or letters anywhere.',
        'A product package decorated with colours and simple pictures only, and no readable words or letters anywhere.',
        'A storefront with an unlettered painted sign showing only a simple emblem and no readable words or letters.'])
    return G
def wiring(final):
    G = {}
    old = []
    try:
        old = [l.rstrip('\n') for l in open(os.path.join(final, 'text_slogan.txt'), encoding='utf8') if l.strip() and '__name' not in l]
    except Exception: pass
    G['text_slogan'] = old + ['"__name_tagline__"', '"__name_established__"', '"__name_hours__"']
    G['text_brand'] = ['"__name_product_brand__"', '"__name_company__"', '"__name_brand_upper__"', '"__name_product__"', '"__name_brand_invented__"']
    G['text_shop_name'] = ['"__name_shop__"', '"__name_business__"', '"__name_restaurant__"']
    G['text_pub_name'] = ['"__name_pub__"']
    G['text_ship_name'] = ['"__name_ship__"']
    G['text_card_name'] = ['"__name_person__"', '"__name_hero__"']
    G['text_map_name'] = ['"__name_town__"']
    return G
LIGHT_OUT = ['soft overcast daylight', 'warm low evening light', 'bright midday sun with crisp shadows', 'blue dusk with the sign lit', 'early morning light', 'gentle light after rain']
LIGHT_IN = ['soft even window light', 'warm indoor lamp light', 'bright shop lighting', 'cool daylight from a skylight', 'a single warm overhead light with soft falloff', 'soft diffused light with a plain background']
import re as _re
_PAT = [(r' No other words or letters appear( on the card)?\.', ''), (r',? and (nothing else|no other (readable )?words( or letters)?)(?=[.,])', ''), (r' and nothing else(?=[.,])', ''), (r' with no other readable text', ''),
 (r'(,| with| and) no words( or letters)?(?=[,.]| and the)', ' as a purely pictorial mark'), (r' among small paper notes with no readable text', ' among small blank paper notes'),
 (r' Nothing else is printed on the front\.', ' The rest of the front is plain and empty.')]
def positive(line):
    for a, b in _PAT: line = _re.sub(a, b, line)
    return line
def build(final=None):
    import v94_names2
    P = G_parts(); G = dict(P); N = G_names(P); G.update(N); G.update(G_prompts())
    import v94_cards, v94_merch; G.update(v94_cards.build(P)); G.update(v94_merch.build(final)); G.update(v94_names2.build(final)); G.update(wiring(final or '/home/claude/w/wildcards'))
    G['name_light_night'] = ['night light with the sign glowing and a wet street reflecting it', 'night light with the sign glowing against a dark sky', 'night light with warm window glow and the sign lit']; G['name_light_outdoor'] = LIGHT_OUT; G['name_light_indoor'] = LIGHT_IN
    top = ['name_sign_shopfront_prompt', 'name_sign_company_prompt', 'name_sign_restaurant_prompt', 'name_label_product_prompt', 'name_label_price_prompt', 'name_tag_person_prompt', 'name_tag_clothing_prompt', 'name_vehicle_livery_prompt', 'name_poster_prompt', 'name_receipt_prompt', 'name_blank_text_prompt', 'name_business_sign_prompt', 'name_media_prompt', 'name_business_card_prompt', 'name_logo_prompt', 'name_merch_prompt']
    G['name_any_prompt'] = ['__%s__' % k for k in top]
    G['name_blank_text_prompt'] = ['A shop sign, label or package with plain unmarked surfaces, decorated only with simple shapes and patterns.', 'A product package with plain unmarked surfaces, decorated only with colours and simple pictures.', 'A storefront with a painted sign showing only a simple emblem on a plain ground.']
    for k in list(G):
        if not k.endswith('_entry_points'): G[k] = list(dict.fromkeys(positive(l) for l in G[k]))
    G['v94n_entry_points'] = [k for k in G if k.endswith('_prompt') and not k.startswith('text_')] + ['name_company', 'name_shop', 'name_restaurant', 'name_pub', 'name_product', 'name_person', 'name_address', 'name_brand']
    return G
if __name__ == '__main__':
    G = build(); print(len(G), 'files')
    import re as _re
    ref = _re.compile(r'__([a-z0-9_]+)__'); bad = set()
    for k, v in G.items():
        for l in v:
            for m in ref.findall(l):
                if m not in G and not os.path.exists('/home/claude/w/wildcards/%s.txt' % m): bad.add((k, m))
    print('missing refs', sorted(bad)[:10])
    for k in ('name_stem_latin', 'name_stem_nordic', 'name_stem_german', 'name_stem_tech', 'name_stem_japanese', 'name_surname'): print(k, len(G[k]), G[k][:8])
