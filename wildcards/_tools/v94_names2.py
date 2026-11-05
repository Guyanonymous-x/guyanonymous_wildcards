"""v94 names part 2: business types, heroes, comics, books, authors, music, film, magazines."""
import os, sys, re, random
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
R = random.Random(9401)
def uniq(l): return list(dict.fromkeys(x for x in l if x))
NOMORE = ' No other words or letters appear.'
# slug: (trade words, extra sign line options, door/window notice)
VENUES = {
 'liquor_store': ('Liquors|Wine and Spirits|Bottle Shop|Cellars|Spirits|Wine Merchants|Off Licence|Beer and Wine|Liquor Mart|Vintners', ['OPEN', 'Beer Wine Spirits', 'Cold Beer', 'Open late'], 'a liquor store'),
 'bar': ('Bar|Tavern|Taproom|Saloon|Lounge|Alehouse|Cocktail Room|Public House', ['OPEN', 'Happy Hour 5 to 7', 'Live Music Friday', 'Cold Beer'], 'a bar'),
 'pharmacy': ('Pharmacy|Chemist|Drug Store|Apothecary|Dispensary', ['OPEN', 'Prescriptions', 'Open 9 to 6', 'Pharmacy'], 'a pharmacy'),
 'bookshop': ('Books|Bookshop|Booksellers|Book Barn|Book Exchange|Bookstore', ['OPEN', 'New and Used', 'Open daily', 'Browse Welcome'], 'a bookshop'),
 'bakery': ('Bakery|Bread Co.|Pastry Shop|Bake House|Patisserie|Boulangerie', ['OPEN', 'Fresh Bread Daily', 'Open from 6am', 'Cakes to Order'], 'a bakery'),
 'butcher': ('Butchers|Meat Market|Family Butchers|Provisions|Charcuterie', ['OPEN', 'Fresh Cuts Daily', 'Home Made Sausages', 'Open 8 to 5'], 'a butcher shop'),
 'grocery': ('Grocery|Market|Food Hall|Supermarket|Corner Store|Mini Mart|General Store', ['OPEN', 'Open 24 hours', 'Fresh Produce', 'Deli Counter'], 'a grocery store'),
 'cafe': ('Cafe|Coffee House|Espresso Bar|Tea Rooms|Roastery|Coffee Co.', ['OPEN', 'Fresh Coffee', 'Breakfast All Day', 'Free Wifi'], 'a cafe'),
 'diner': ('Diner|Grill|Kitchen|Eatery|Lunch Counter|Chippy', ['OPEN', 'Breakfast All Day', 'Open 24 hours', 'Home Cooking'], 'a diner'),
 'pizzeria': ('Pizzeria|Pizza|Pizza Kitchen|Slice House|Pizza Oven', ['OPEN', 'Hot Slices', 'Delivery', 'Open late'], 'a pizzeria'),
 'hotel': ('Hotel|Inn|Lodge|Guest House|Motel|Grand Hotel|Resort', ['VACANCY', 'NO VACANCY', 'Rooms Available', 'Reception'], 'a hotel'),
 'bank': ('Bank|Savings Bank|Trust|Building Society|Credit Union|Bank and Trust', ['Open Mon to Fri', 'ATM', 'Cash Machine', 'Savings and Loans'], 'a bank'),
 'garage': ('Garage|Motors|Auto Repair|Tyres|Service Station|Autos|Body Shop', ['OPEN', 'MOT Testing', 'Tyres Fitted', 'Open 8 to 6'], 'a garage'),
 'petrol_station': ('Fuel|Petrol|Gas|Service Station|Fuel Stop|Gas and Go', ['Open 24 hours', 'Unleaded', 'Diesel', 'Car Wash'], 'a petrol station'),
 'gym': ('Fitness|Gym|Athletic Club|Health Club|Strength Club|Training Hall', ['OPEN', 'Day Passes', 'Open 5am to 11pm', 'Classes Daily'], 'a gym'),
 'hair_salon': ('Hair|Salon|Barbers|Cuts|Hair Studio|Hair Lounge', ['OPEN', 'Walk Ins Welcome', 'Appointments', 'Open Tue to Sat'], 'a hair salon'),
 'laundromat': ('Laundromat|Laundry|Wash House|Coin Laundry|Cleaners', ['OPEN', 'Open 24 hours', 'Coin Operated', 'Dry Cleaning'], 'a laundromat'),
 'cinema': ('Cinema|Picture House|Theatre|Movie House|Odeon Hall|Palace Cinema', ['NOW SHOWING', 'Tickets', 'Box Office', 'Coming Soon'], 'a cinema'),
 'arcade': ('Arcade|Amusements|Game Room|Play Zone|Pinball Hall', ['OPEN', 'Tokens', 'Change Here', 'Open late'], 'an arcade'),
 'record_store': ('Records|Vinyl|Music|Sound Shop|Record Exchange', ['OPEN', 'New and Used Vinyl', 'We Buy Records', 'Open daily'], 'a record store'),
 'toy_shop': ('Toys|Toy Shop|Toy Emporium|Playthings|Toy Chest', ['OPEN', 'Gift Wrapping', 'Open daily', 'Toys and Games'], 'a toy shop'),
 'hardware_store': ('Hardware|Tools|Builders Supply|Hardware and Paint|Timber and Tools', ['OPEN', 'Keys Cut', 'Paint Mixing', 'Open 7 to 6'], 'a hardware store'),
 'flower_shop': ('Florist|Flowers|Blooms|Flower Stall|Garden Florist', ['OPEN', 'Fresh Flowers', 'Wedding Flowers', 'Open daily'], 'a flower shop'),
 'tattoo_studio': ('Tattoo|Ink|Tattoo Studio|Body Art|Tattoo Parlour', ['OPEN', 'Walk Ins Welcome', 'Appointments', 'Custom Designs'], 'a tattoo studio'),
 'pawn_shop': ('Pawn|Pawnbrokers|Loans and Pawn|Cash for Gold|Pawn and Jewelry', ['OPEN', 'Cash for Gold', 'We Buy and Sell', 'Loans'], 'a pawn shop'),
 'pub': ('Arms|Inn|Tavern|Head|Crown|Anchor', ['OPEN', 'Real Ale', 'Food Served', 'Live Music'], 'a pub'),
 'sex_free_dummy': None,
}
VENUES.pop('sex_free_dummy')
def venues():
    G = {}; slugs = []
    for slug, (trade, extra, desc) in VENUES.items():
        T = trade.split('|'); slugs.append(slug)
        G['name_trade_' + slug] = T
        G['name_extra_' + slug] = extra
        if slug == 'pub':
            pass
        else:
            G['name_' + slug] = ['__name_surname__\'s __name_trade_%s__' % slug, '__name_brand_invented__ __name_trade_%s__' % slug, 'The __name_word__ __name_trade_%s__' % slug, '__name_brand_wordpair__ __name_trade_%s__' % slug, '__name_first__\'s __name_trade_%s__' % slug, '__name_brand_surname__ __name_trade_%s__' % slug, '__name_word__ __name_trade_%s__' % slug, '__name_brand_invented__ __name_trade_%s__' % slug]
        N = '"__name_%s__"' % slug; X = '"__name_extra_%s__"' % slug
        G['name_%s_sign_prompt' % slug] = uniq([
            'The exterior of %s with a sign above the door reading %s.' % (desc, N) + NOMORE,
            'The front of %s with a lit sign reading %s on the first line and %s on the second line.' % (desc, N, X) + NOMORE,
            'A painted fascia on %s reading %s, and a notice in the window reading %s.' % (desc, N, X) + NOMORE,
            'A corner building that is %s, with a hanging sign showing the words %s.' % (desc, N) + NOMORE,
            'A night view of %s with a neon sign in the window reading %s and a smaller neon sign reading %s.' % (desc, N, X) + NOMORE,
            'The glass door of %s with white lettering reading %s on the first line and "__name_hours__" on the second line.' % (desc, N) + NOMORE,
            'A shop bag from %s printed with the words %s and "__name_address__" hanging on a door handle.' % (desc, N) + NOMORE][:-1])
    G['name_business'] = ['__name_%s__' % s for s in slugs]
    G['name_business_sign_prompt'] = ['__name_%s_sign_prompt__' % s for s in slugs]
    G['name_venue_prompts'] = ['__name_%s_sign_prompt__' % s for s in slugs]
    return G
# ---- heroes
HADJ = 'Crimson Silver Midnight Scarlet Iron Storm Phantom Radiant Shadow Golden Emerald Amber Cobalt Static Silent Savage Thunder Frost Solar Lunar Rapid Velvet Neon Sable Ivory Ashen Jade Violet Copper Ruby Onyx Opal Titan Cinder Ember Gale Vortex Zenith Apex Nova'.split()
HNOUN = 'Falcon Heron Wolf Fox Raven Comet Lantern Tiger Viper Mantis Hornet Condor Panther Cobra Badger Lynx Owl Stag Eagle Shark Jaguar Phoenix Sparrow Hawk Dragonfly Scorpion Orchid Thistle Blade Shield Arrow Hammer Spark Pulse Echo Prism Specter Sentinel Guardian Avenger Ranger Knight Warden Striker Courier Whisper Torch Anvil Tempest'.split()
HTITLE = ['Captain', 'Doctor', 'Major', 'Lady', 'Lord', 'Professor', 'Agent', 'Commander', 'Sergeant', 'Baroness', 'Colonel', 'Mister', 'Miss']
KNOWN = {'batman', 'superman', 'spider', 'wonder woman', 'aquaman', 'green lantern', 'black panther', 'captain america', 'iron man', 'ghost rider', 'silver surfer', 'black widow', 'green arrow', 'dark knight', 'iron fist', 'doctor strange', 'doctor doom', 'captain marvel', 'storm', 'scarlet witch', 'crimson dynamo', 'silver sable', 'shadow cat', 'phantom lady', 'golden eagle', 'iron wolf', 'hawk', 'cobalt man', 'captain atom', 'dr. fate', 'doctor fate', 'iron spider', 'black cat', 'moon knight', 'night owl', 'nova', 'red hood', 'scarlet spider', 'crimson fox', 'silver fox', 'black hornet', 'green hornet', 'jade spider', 'amber alert', 'sparrow', 'frost giant'}
def heroes():
    G = {}
    plain = []
    for a in HADJ:
        for n in HNOUN:
            nm = a + ' ' + n
            if nm.lower() in KNOWN or n.lower() in ('arrow',) and a.lower() == 'green' or ('hornet' in nm.lower() and a.lower() in ('green', 'black')): continue
            plain.append(nm)
    R.shuffle(plain); plain = plain[:260]
    titled = []
    for _ in range(140):
        t = R.choice(HTITLE); n = R.choice(HNOUN)
        w = ('%s %s' % (t, n)); a = R.choice(HADJ)
        w = R.choice([w, '%s %s %s' % (t, a, n), 'The %s %s' % (a, n), 'The %s' % n, '%s %s' % (n, R.choice(['Man', 'Woman', 'Girl', 'Boy']))])
        if re.search(r'(Girl|Boy)$', w): w = w.replace('Girl', 'Woman').replace('Boy', 'Man')
        if w.lower() in KNOWN or w.lower().startswith('captain america'): continue
        titled.append(w)
    G['name_hero'] = uniq(plain + titled)
    G['name_hero_team'] = ['The __name_word__ __name_hero_group__', 'The __name_hero_adj__ __name_hero_group__', '__name_hero_group__ of __name_word__', 'The __name_hero_adj__ __name_hero_noun__ __name_hero_group__']
    G['name_hero_group'] = ['League', 'Guard', 'Order', 'Syndicate', 'Brigade', 'Alliance', 'Vanguard', 'Society', 'Corps', 'Legion', 'Circle', 'Watch', 'Patrol', 'Union', 'Council']
    G['name_hero_adj'] = HADJ; G['name_hero_noun'] = HNOUN
    G['name_villain'] = ['Doctor __name_surname__', 'The __name_hero_adj__ __name_hero_villain_noun__', 'Baron __name_surname__', 'Lord __name_hero_villain_noun__', 'Madame __name_surname__', '__name_hero_villain_noun__ King', 'The __name_hero_villain_noun__']
    G['name_hero_villain_noun'] = ['Mirage', 'Hex', 'Plague', 'Gloom', 'Rust', 'Venom', 'Maelstrom', 'Eclipse', 'Obsidian', 'Havoc', 'Wraith', 'Cobweb', 'Jackal', 'Scarab', 'Specter', 'Doom Moth', 'Overlord', 'Puppeteer', 'Gravedigger', 'Harrier']
    G['name_hero_power_tag'] = ['Strength', 'Flight', 'Speed', 'Invisibility', 'Lightning', 'Frost', 'Fire', 'Shadow', 'Sonic', 'Gravity', 'Light', 'Magnetism']
    G['name_hero_catchphrase'] = ['Justice never sleeps', 'Not on my watch', 'Stand together', 'Here to help', 'The night is mine', 'Hold the line', 'Rise up', 'Never give in', 'Face the storm', 'Light the way']
    G['name_hero_prompt'] = uniq([
        'A costumed adult hero with a chest emblem showing a single bold letter "__name_hero_letter__" and no other words or letters.',
        'A comic hero standing on a rooftop with a cape, with a belt buckle bearing the letter "__name_hero_letter__" and no other words or letters.',
        'A wall poster showing a costumed hero with the words "__name_hero__" in bold letters at the top and "__name_hero_catchphrase__" at the bottom.' + NOMORE,
        'A hero team gathered in a row, with a banner behind them reading "__name_hero_team__".' + NOMORE,
        'A villain in a dark cloak under a street light, with a newspaper headline on the ground reading "__name_villain__ STRIKES AGAIN".' + NOMORE,
        'A costumed hero action figure in its blister pack, with the packaging reading "__name_hero__" on the first line and "__name_hero_power_tag__" on the second line.' + NOMORE,
        'A lunchbox decorated with a costumed hero and the words "__name_hero__" printed above the picture.' + NOMORE])
    G['name_hero_letter'] = list('ABCDEFGHJKLMNPRSTVWXZ')
    return G
# ---- books, comics, authors
def media():
    G = {}
    G['name_author'] = ['__name_first__ __name_surname__', '__name_first__ __name_surname__', '__name_first__ __name_surname__', '__name_initial__. __name_initial__. __name_surname__', '__name_first__ __name_initial__. __name_surname__', '__name_first__ __name_surname__ Jr.']
    G['name_initial'] = list('ABCDEGHJKLMNPRSTVW')
    G['name_book_title_thriller'] = ['The __name_word__ Protocol', 'Dead of __name_word__', 'The __name_surname__ File', 'Last Train to __name_town__', 'Nine Days in __name_town__', 'The Quiet __name_word__', 'Cold __name_word__', 'The Night Before __name_town__', 'Red __name_word__', 'The Informant']
    G['name_book_title_romance'] = ['A Summer in __name_town__', 'The __name_word__ Letters', 'Love at __name_surname__ House', 'Hearts of __name_word__', 'Under the __name_word__ Moon', 'The Last Dance at __name_town__', 'Meet Me at __name_word__ Lane', 'Where the __name_word__ Blooms']
    G['name_book_title_fantasy'] = ['The __name_word__ Crown', 'Heir of __name_brand_latin__', 'The Last __name_hero_noun__', 'A Throne of __name_word__', 'The Sword of __name_brand_nordic__', 'Shadows over __name_brand_nordic__', 'The Wizard of __name_town__', 'Kingdom of __name_word__ and __name_word__']
    G['name_book_title_scifi'] = ['Orbit of __name_brand_tech__', 'The __name_brand_tech__ Signal', 'Beyond __name_brand_latin__', 'Station __name_brand_tech__', 'The Long Road to __name_brand_latin__', 'Colony __name_number_small__', 'Echoes of __name_brand_tech__', 'The Last Ship from __name_brand_tech__']
    G['name_book_title_cookbook'] = ['The __name_word__ Kitchen', 'Simple Suppers', '__name_first__\'s Family Recipes', 'The Bread Book', 'A Year of Soups', 'Cooking with __name_flavour__', 'The Weeknight Table', 'Food from __name_town__']
    G['name_book_title_history'] = ['The Rise of __name_town__', 'A History of __name_town__', 'The __name_surname__ Dynasty', 'Empire of __name_word__', 'The Fall of __name_brand_latin__', 'Voices of the __name_word__ Coast', 'Rivers and Roads: A History of __name_town__']
    G['name_book_title_literary'] = ['The Weight of __name_word__', 'What the __name_word__ Knew', 'Small Hours', 'An Ordinary House', 'The Year of __name_word__', 'Ashes and __name_word__', 'The Distance Between Us', 'A Quiet Inheritance']
    G['name_book_title_any'] = ['__name_book_title_%s__' % g for g in ('thriller', 'romance', 'fantasy', 'scifi', 'cookbook', 'history', 'literary')]
    G['name_series'] = ['The __name_word__ Chronicles', 'The __name_surname__ Mysteries', '__name_brand_latin__ Saga', 'The __name_word__ Trilogy', 'A __name_surname__ Novel']
    G['name_publisher'] = ['__name_surname__ & __name_surname__', '__name_word__ Press', '__name_brand_invented__ Books', 'The __name_word__ Press', '__name_surname__ House', '__name_word__ Publishing']
    G['name_book_cover_prompt'] = uniq([
        'A hardback book standing upright, its cover printed with the title "__name_book_title_any__" and the author "__name_author__" and no other words or letters.',
        'A paperback novel on a table, the cover reading "__name_book_title_thriller__" on the first line and "__name_author__" on the second line.' + NOMORE,
        'A cookbook lying open beside a bowl, its cover reading "__name_book_title_cookbook__" and "__name_author__".' + NOMORE,
        'A fantasy novel with a painted cover, the title "__name_book_title_fantasy__" in gold letters and the author "__name_author__" at the bottom.' + NOMORE,
        'A shelf of three books whose spines read "__name_book_title_any__", "__name_book_title_any__" and "__name_book_title_any__", with author names omitted.',
        'A book with a plain cloth cover, spine reading "__name_book_title_literary__" and "__name_publisher__" at the foot.' + NOMORE,
        'A paperback with a cover reading "__name_series__" at the top, "__name_book_title_scifi__" in the middle and "__name_author__" at the bottom.' + NOMORE])
    # comics
    G['name_comic_title'] = ['__name_hero__', '__name_hero__ & __name_hero__', 'The Adventures of __name_hero__', '__name_hero_team__', 'Tales of the __name_word__', '__name_hero__ Versus __name_villain__', 'Secret Files of __name_surname__', 'The Amazing __name_hero__', '__name_hero__: Origins', '__name_brand_tech__ Force', 'Space Patrol __name_number_small__', 'Strange Tales of __name_town__']
    G['name_comic_issue'] = ['Issue __name_number_small__', 'No. __name_number_small__', '#__name_number_small__', 'Vol. __name_number_small__']
    G['name_comic_publisher'] = ['__name_word__ Comics', '__name_surname__ Comics', '__name_brand_invented__ Comics', '__name_word__ Studios', '__name_brand_invented__ Press']
    G['name_comic_cover_prompt'] = uniq([
        'A comic book cover with the title "__name_comic_title__" across the top, "__name_comic_issue__" in a corner, and a price of "__name_price__" in a small box.' + NOMORE,
        'A comic book cover showing a costumed hero leaping across the page, with the title "__name_hero__" at the top and "__name_comic_publisher__" in a small banner.' + NOMORE,
        'A comic cover with the title "__name_comic_title__" and the tagline "__name_hero_catchphrase__" beneath it, and no other words or letters.',
        'A wall of comic books on a spinner rack, each cover with a title in large letters reading "__name_comic_title__" and "__name_comic_title__".' + NOMORE,
        'A comic book open to a single splash page with a speech balloon reading "__name_hero_catchphrase__" and no other words or letters.'])
    # music
    G['name_band'] = ['The __name_word__s', 'The __name_hero_adj__ __name_hero_noun__s', '__name_brand_invented__', 'The __name_surname__ Brothers', '__name_word__ Road', '__name_first__ and the __name_word__s', 'The __name_surname__ Set', '__name_brand_tech__']
    G['name_album'] = ['__name_word__ Hours', 'Songs for __name_town__', 'The __name_word__ Sessions', 'Live at the __name_word__', 'Blue __name_word__', 'Midnight in __name_town__', 'Long Way Home', 'Static and __name_word__']
    G['name_record_prompt'] = uniq([
        'A vinyl record sleeve with the band name "__name_band__" on the first line and the album title "__name_album__" on the second line.' + NOMORE,
        'A gig poster pinned to a wall, reading "__name_band__" in large letters, "__name_pub__" on the second line and "__name_price__" at the bottom.' + NOMORE,
        'A concert ticket stub reading "__name_band__" on the first line and "__name_town__" on the second line.' + NOMORE,
        'A cassette tape with a hand-written label reading "__name_album__" and nothing else.',
        'A guitar case covered in stickers, one reading "__name_band__" and no other readable words.'])
    # film / tv / magazine / newspaper / games
    G['name_movie'] = ['The __name_word__ Job', 'Night of the __name_hero_noun__', '__name_surname__', 'Escape from __name_town__', 'The Last __name_word__', 'A Man Called __name_surname__', 'Operation __name_word__', '__name_brand_tech__ Rising', 'The __name_surname__ Inheritance', 'Return to __name_town__']
    G['name_movie_prompt'] = uniq([
        'A cinema marquee reading "NOW SHOWING" on the first line and "__name_movie__" on the second line.' + NOMORE,
        'A film poster with the title "__name_movie__" in large letters and "__name_tagline__" beneath it.' + NOMORE,
        'A cinema ticket reading "__name_movie__" on the first line and "__name_price__" on the second line.' + NOMORE,
        'A video cassette box with the title "__name_movie__" on the spine.' + NOMORE,
        'A television screen showing a title card that reads "__name_movie__" and nothing else.'])
    G['name_magazine'] = ['__name_word__ Weekly', 'The __name_brand_invented__ Review', '__name_word__ Monthly', 'Modern __name_trade_corp__', '__name_brand_tech__ Today', 'The __name_town__ Gazette', 'Home and __name_word__', '__name_surname__\'s Magazine']
    G['name_newspaper'] = ['The __name_town__ Times', 'The __name_town__ Herald', 'The Daily __name_word__', 'The __name_town__ Courier', 'The Evening __name_word__', 'The __name_town__ Post']
    G['name_headline'] = ['STORM HITS __name_town__', 'MAYOR OPENS NEW BRIDGE', 'LOCAL BAKERY WINS PRIZE', 'FLOODS CLOSE ROADS', 'TOWN CELEBRATES FESTIVAL', 'RAIL STRIKE ENDS', 'HARVEST BEATS RECORD', 'NEW LIBRARY OPENS']
    G['name_print_prompt'] = uniq([
        'A magazine on a table with the title "__name_magazine__" across the top and "__name_headline__" as the cover line.' + NOMORE,
        'A newspaper folded on a bench, the masthead reading "__name_newspaper__" and a headline reading "__name_headline__".' + NOMORE,
        'A newsstand with magazines whose covers read "__name_magazine__", "__name_magazine__" and "__name_magazine__", and a sign reading "__name_newspaper__".' + NOMORE])
    G['name_players'] = ['2 to 4 players', '2 to 6 players', '1 to 5 players', 'For 2 players', '3 to 8 players', '2 to 5 players']
    G['name_game_title'] = ['__name_brand_tech__ Quest', 'Super __name_word__', '__name_hero_adj__ __name_word__', 'Dungeons of __name_brand_nordic__', '__name_word__ Racer', 'Galaxy __name_brand_tech__', 'Farm of __name_town__', 'Battle for __name_brand_latin__']
    G['name_game_prompt'] = uniq([
        'A video game box with the title "__name_game_title__" in large letters and "__name_company__" in small print.' + NOMORE,
        'A board game box with the title "__name_game_title__" on the lid and "__name_players__" beneath.' + NOMORE,
        'An arcade cabinet with a marquee reading "__name_game_title__" and a screen showing only a title card with the same words.' + NOMORE])
    G['name_media_prompt'] = ['__name_book_cover_prompt__', '__name_comic_cover_prompt__', '__name_record_prompt__', '__name_movie_prompt__', '__name_print_prompt__', '__name_game_prompt__', '__name_hero_prompt__']
    return G
def build(final=None):
    G = {}; G.update(venues()); G.update(heroes()); G.update(media())
    G['v94n2_entry_points'] = [k for k in G if k.endswith('_prompt')] + ['name_hero', 'name_villain', 'name_author', 'name_book_title_any', 'name_comic_title', 'name_band', 'name_movie', 'name_business']
    return G
