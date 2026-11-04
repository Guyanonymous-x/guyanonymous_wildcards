"""v74 stage A - books, periodicals and reading accessories (item 70).
Invented titles, authors and mastheads only (no real works, people or brands). Text meant to appear in the image is in double quotes.
Every family has a prompt (full wording), a _short (brief wording) and a fill-in version where the text is a placeholder to edit."""
import random, itertools
from famlib import P, slug

def pool(seed, n, gen):
    r = random.Random(seed); out = []; seen = set()
    for _ in range(n * 20):
        t = gen(r)
        if t not in seen: seen.add(t); out.append(t)
        if len(out) >= n: break
    return out

# ---------------------------------------------------------------- invented name and word pools
FIRST = P("Alder; Amara; Anselm; Beatrix; Bram; Calla; Cedric; Clemence; Dara; Desmond; Edda; Elias; Fenna; Gideon; Greta; Hale; Ilse; Ines; Jasper; Junia; Kiran; Lenora; Linus; Magda; Marcus; Nell; Odette; Orson; Pria; Quentin; Rosalind; Silas; Tamsin; Thea; Ulrich; Vera; Wilhelmina; Yusuf; Zora; Abel; Bianca; Caspian; Dorothea; Emeric; Farah; Gus; Hettie; Isidore; Jun; Koa; Leopold; Mina; Nadia; Osric; Petra; Rufus; Sunita; Teodor; Una; Viktor; Wren; Xavier; Yara; Zeno; Agnes; Boris; Cora; Dmitri; Esme; Felix; Gwen; Henrik; Iris; Jonah; Kemal; Lucia; Milo; Noor; Olga; Pavel; Rhea; Sven; Tilda; Uma; Valentin; Willa")
SUR_A = P("Ash; Brom; Cald; Dun; Elm; Fair; Gren; Har; Iron; Kest; Lind; Marl; North; Oak; Pen; Rav; Stan; Thorn; Under; Wex; Yar; Bright; Cobb; Dray; Flint; Hollow; Lark; Mor; Nether; Rook; Sedge; Tarn; Wild")
SUR_B = P("ford; ley; wick; ton; mere; combe; worth; gate; shaw; dale; by; field; haven; stead; well; moor; brook; hurst; ridge; wood; croft; vale")
INIT = P("A.; B.; C.; D.; E.; F.; G.; H.; J.; K.; L.; M.; N.; P.; R.; S.; T.; V.; W.")
def author(r):
    k = r.random()
    if k < 0.6: return '%s %s%s' % (r.choice(FIRST), r.choice(SUR_A), r.choice(SUR_B))
    if k < 0.85: return '%s %s %s%s' % (r.choice(INIT), r.choice(INIT), r.choice(SUR_A), r.choice(SUR_B))
    return '%s %s %s%s' % (r.choice(FIRST), r.choice(INIT), r.choice(SUR_A), r.choice(SUR_B))
ADJ = P("Quiet; Last; Hollow; Silver; Burning; Distant; Forgotten; Paper; Salt; Winter; Midnight; Crooked; Golden; Hidden; Restless; Pale; Wandering; Broken; Gentle; Iron; Long; Secret; Borrowed; Faded; Wild; Lonely; Velvet; Narrow; Glass; Slow; Amber; Scarlet; Hungry; Patient; Fallen; Bitter; Open; Third; Seventh; Northern; Southern")
NOUN = P("Orchard; Harbour; Letter; Garden; Lantern; River; Mirror; Staircase; Season; Inheritance; Promise; Compass; Window; Province; Bridge; Clockmaker; Cartographer; Lighthouse; Summer; Reckoning; Meadow; Voyage; Tenant; Stranger; Archive; Kingdom; Island; Orchestra; Apprentice; Companion; Heron; Fox; Thief; Widow; Daughter; Cousin; Hour; Shore; Engine; Chorus; Ferry; Station; Vineyard; Almanac")
PLACE = P("Marlow; Penhallow; Thornbury; Kestrel Bay; Dunmere; Ravensgate; Alderbrook; Stanwick; Greywater; Lindhurst; the Salt Coast; Old Harrow; Wexcombe; Northmoor; Saint Aldric; Fairhaven; Cobbleford; Hollowshaw")
def novel_title(r):
    k = r.randrange(7)
    if k == 0: return 'The %s %s' % (r.choice(ADJ), r.choice(NOUN))
    if k == 1: return 'The %s of %s' % (r.choice(NOUN), r.choice(PLACE))
    if k == 2: return '%s %s' % (r.choice(ADJ), r.choice(NOUN) + 's')
    if k == 3: return 'A %s in %s' % (r.choice(NOUN), r.choice(PLACE))
    if k == 4: return 'The %s and the %s' % (r.choice(NOUN), r.choice(NOUN))
    if k == 5: return 'What the %s Kept' % r.choice(NOUN)
    return 'Letters from %s' % r.choice(PLACE)
TOPIC = P("Bread; Soups; Preserves; Pastry; Fermentation; Smoking and Curing; Cheese; Vegetables; Sauces; Cakes; Pickles; Tea; Herbs; Grilling; Salads; Noodles; Stews; Fish; Beans and Grains; Breakfasts")
def cook_title(r):
    k = r.randrange(4); t = r.choice(TOPIC)
    if k == 0: return 'The Complete Book of %s' % t
    if k == 1: return '%s for Every Season' % t
    if k == 2: return 'A Cook\'s Guide to %s' % t
    return '%s at Home' % t
SUBJ = P("Wild Mushrooms; Garden Birds; Coastal Plants; Night Sky Objects; Freshwater Fish; Butterflies and Moths; Hedgerow Trees; Rocks and Minerals; Seashore Life; Mountain Flowers; Tracks and Signs; Wild Orchids; Insects; Ferns and Mosses; Owls; Fungi of the Woodland; Shells")
def field_title(r):
    return r.choice(['A Field Guide to %s', 'Pocket Guide to %s', 'The Illustrated Book of %s', '%s of the Region', 'Identifying %s']) % r.choice(SUBJ)
SCI = P("Algebra; Geometry; Chemistry; Physics; Biology; Geography; World History; Economics; Statistics; Calculus; Anatomy; Grammar; Latin; Navigation; Astronomy; Geology; Accounting; Electronics; Civil Law; Philosophy")
def text_title(r):
    return r.choice(['%s: A First Course', 'Principles of %s', 'Introduction to %s', '%s for Students', 'Essential %s', 'Understanding %s']).replace(': ', ' ') % r.choice(SCI)
def kid_title(r):
    a = r.choice(['Little', 'Big', 'Sleepy', 'Brave', 'Tiny', 'Clever', 'Grumpy', 'Happy', 'Lost', 'Curious', 'Muddy', 'Wobbly']); b = r.choice(['Bear', 'Fox', 'Owl', 'Hedgehog', 'Duck', 'Rabbit', 'Mouse', 'Dragon', 'Robot', 'Whale', 'Badger', 'Frog', 'Cloud', 'Snail'])
    return r.choice(['%s %s Goes Home', '%s %s and the Moon', 'The %s %s', '%s %s Finds a Friend', 'Where Is %s %s?']) % (a, b)
POEM = P("Salt; Dusk; Ash; Rain; Hunger; Lanterns; Thaw; Orchards; Tides; Embers; Thresholds; Moths; Small Hours; Weather; Bone; Linen; Chalk; Echo; Meadows; Mercury")
def poem_title(r):
    return r.choice(['Collected %s', '%s and Other Poems', 'Poems of %s', 'The Book of %s', 'Selected %s']) % r.choice(POEM)
def mystery_title(r):
    return r.choice(['The Case of the %s %s' % (r.choice(ADJ), r.choice(NOUN)), 'Murder at %s' % r.choice(PLACE), 'The %s Affair' % r.choice(NOUN), 'Death on the %s' % r.choice(NOUN), 'The %s Murders' % r.choice(PLACE), 'A Body in %s' % r.choice(PLACE)])
def manual_title(r):
    return r.choice(['Owner\'s Manual', 'Workshop Manual', 'Service Handbook', 'Repair Guide', 'Operating Instructions', 'Maintenance Manual']) + ' for the ' + r.choice(['Model %d' % r.randrange(20, 900), 'Series %s' % r.choice('ABCDEFGHJKLMNPRSTVW') + str(r.randrange(2, 9)), 'Type %d' % r.randrange(2, 99)])
CAPTION = P("A novel; A mystery; A true story; A love story; A tale of the sea; A new translation; The classic account; Illustrated edition; Revised and expanded; Book one of three; Volume two; A family saga; First edition; Large print edition; With a new foreword; Now a bestseller; The prize-winning novel; Stories; A memoir; The complete collection; A thriller; Abridged for young readers; An adventure; A history; A ghost story; A comedy of manners; Selected letters; A journey; An unauthorised life; Over one million copies sold")
BLURB = P("A haunting debut about a family and the house they cannot leave; A gripping story of loyalty and loss on the northern coast; Warm, funny and quietly devastating; The book everyone is talking about; Praised for its clear prose and sharp eye; An unforgettable portrait of a small town; A wise and tender guide for beginners; Simple recipes from a lifetime of cooking; Three hundred illustrations drawn from life; A classic of its kind, newly revised")
PRICE_TAG = P("$4.99; $12.95; $18.00; 3.50 pounds; 8.99 pounds; 6 shillings; 12 euros; 25 cents; 95 cents; 1.25 dollars; 14.99 dollars; 5 francs")

# ---------------------------------------------------------------- books
BOOK_TYPES = {
 'novel': dict(sizes=P('mass-market paperback; trade paperback; small hardcover; thick hardcover; pocket paperback'), title=novel_title),
 'cookbook': dict(sizes=P('large flat hardcover; spiral-bound; thick hardcover with a ribbon marker; slim paperback; ring-bound with plastic pockets'), title=cook_title),
 'field guide': dict(sizes=P('pocket-sized flexible cover; small weatherproof hardcover; slim paperback; thick small-format hardcover'), title=field_title),
 'textbook': dict(sizes=P('heavy oversized hardcover; large paperback; thick hardcover with a worn spine; ring-bound study edition'), title=text_title),
 'picture book': dict(sizes=P('square hardcover; large landscape hardcover; thick board book; slim paperback'), title=kid_title),
 'poetry collection': dict(sizes=P('slim paperback; small hardcover; thin saddle-stitched book; narrow hardcover'), title=poem_title),
 'detective story': dict(sizes=P('mass-market paperback; worn pocket paperback; hardcover with a dust jacket; pulp-style paperback'), title=mystery_title),
 'technical manual': dict(sizes=P('thick ring binder; stapled booklet; heavy hardcover; spiral-bound manual'), title=manual_title),
}
BIND = P("sewn pages; a glued spine; staples through the fold; spiral coil binding; ring binding; Japanese stab binding; raised bands on a leather spine; a cloth-covered rounded spine; reinforced library binding; headbands and a case binding; visible thread stitching")
MATERIAL = P("cloth; smooth leather; worn leather; glossy laminated card; matte card; linen; marbled paper boards; buckram; embossed leatherette; paper over boards; velvet; canvas; vinyl; faux crocodile skin; kraft board")
COLOUR = P("deep green; oxblood red; navy blue; mustard yellow; faded black; cream; slate grey; rust orange; dusty pink; forest brown; teal; plum; olive; pale blue; charcoal; ivory; burnt sienna; bright red; saffron; sage")
COVER_ART = P("a gold-stamped title and a simple border; a painted landscape of hills at dusk; a bold geometric pattern in two colours; a woodcut of a lone ship; a photograph of a rain-streaked window; a hand-drawn botanical illustration; a single large letter surrounded by flowers; a silhouetted figure on a hill; a cartoon animal on a plain colour; a bold block of type with no picture; a collage of torn paper shapes; a close-up photograph of a hand holding a key; an embossed crest; a minimalist drawing of a door; an Art Deco sunburst design; a repeating pattern of tiny birds; a painting of a harbour at night; a pencil sketch of a house with a lit window; a mosaic of coloured squares; a stylised map with a dotted route")
SPINE = P("the title in gold capitals; the title in white block letters on a coloured band; the title and author in a thin serif typeface; a small publisher's emblem at the foot; a library label near the foot; white creases down its length; faded lettering; five raised bands; a paper label; bold red type")
EDGES = P("untouched white page edges; yellowed page edges; gilt page edges; sprayed red page edges; deckle edges; brown foxed page edges; marbled page edges; dog-eared pages; page edges stained by damp; clean, tight page edges")
CONDITION = P("pristine; lightly handled; creased at the spine; torn at one corner; rubbed at the edges; stained by water across the lower cover; sun-faded along the spine; scribbled with pencil notes inside; broken at the hinge; ringed by a coffee stain; curled at the corners; mended with sticky tape on the spine; ripped at the cover flap; heavily thumbed; yellowed with age; freshly printed; marked with a price sticker; stamped with a library mark; shedding loose pages")
JACKET = P("a glossy dust jacket; a torn dust jacket; a protective clear plastic cover; a plain brown paper cover; a worn paper dust jacket with a chipped top edge; no jacket; a bright jacket with a cover blurb on the back; a sun-faded dust jacket; a clear library jacket with a label")
STATE = P("closed; lying open and face up; lying open and face down to hold the page; resting open under one hand; propped half open; standing upright; lying closed with a bookmark protruding; open with the pages fanned; tilted open on a stand; open with a single page being turned")
REST = P("a wooden table; a kitchen counter; the arm of a chair; a rumpled bed; a sofa cushion; a lap; a window seat; the floor beside a bed; a stack of other books; a garden bench; a picnic blanket; a train seat tray; a hospital bedside table; a desk beside a lamp; the edge of a bath; a pile of cushions; a damp towel; a car dashboard; a rock beside a stream; a rough wooden stool")
PLACEHOLDER = dict(title='"TITLE GOES HERE"', author='"AUTHOR NAME"', caption='"CAPTION GOES HERE"')

def build_books():
    G = {}
    G['book_binding'] = BIND; G['book_cover_material'] = MATERIAL; G['book_cover_colour'] = COLOUR
    G['book_cover_art'] = COVER_ART; G['book_spine'] = SPINE; G['book_edges'] = EDGES; G['book_condition'] = CONDITION
    G['book_jacket'] = JACKET; G['book_state'] = STATE; G['book_rest'] = REST
    G['book_author'] = ['"%s"' % a for a in pool(11, 400, author)]
    G['book_caption'] = ['"%s"' % c for c in CAPTION]; G['book_blurb'] = ['"%s"' % b for b in BLURB]
    G['book_price'] = ['"%s"' % p for p in PRICE_TAG]
    G['book_types'] = list(BOOK_TYPES)
    allsizes = []; refs = []
    for t, d in BOOK_TYPES.items():
        s = slug(t); G['book_%s_size' % s] = d['sizes']; allsizes += d['sizes']
        G['book_%s_title' % s] = ['"%s"' % x for x in pool(len(t) * 7, 350 if t != 'technical manual' else 200, d['title'])]
        tpl = 'A %s, a %s, with a __book_cover_colour__ __book_cover_material__ cover showing __book_cover_art__. The title "TITLE" is printed on the cover and the spine has __book_spine__.' % (t, '__book_%s_size__' % s)
        G['book_%s_look' % s] = ['A %s, which is a __book_%s_size__ with __book_binding__. The cover is __book_cover_colour__ __book_cover_material__ with __book_cover_art__. The cover title is __book_%s_title__ and the author is __book_author__. The spine has __book_spine__ and the book has __book_edges__.' % (t, s, s)]
        G['book_%s_look_fill' % s] = ['A %s, which is a __book_%s_size__ with __book_binding__. The cover is __book_cover_colour__ __book_cover_material__ with __book_cover_art__. The cover title is %s and the author is %s. The spine has __book_spine__ and the book has __book_edges__.' % (t, s, PLACEHOLDER['title'], PLACEHOLDER['author'])]
        G['book_%s_short' % s] = ['A %s, __book_%s_size__, __book_cover_colour__ __book_cover_material__ cover, titled __book_%s_title__.' % (t, s, s)]
        G['book_%s_phrase' % s] = ['a %s, __book_%s_size__, with a __book_cover_colour__ __book_cover_material__ cover, titled __book_%s_title__' % (t, s, s)]
        G['book_%s_prompt' % s] = ['__book_%s_look__ The book is __book_condition__. It has __book_jacket__. It is __book_state__ on __book_rest__.' % s]
        G['book_%s_prompt_fill' % s] = ['__book_%s_look_fill__ The book is __book_condition__. It has __book_jacket__. It is __book_state__ on __book_rest__.' % s]
        refs.append(s)
    G['book_prompt'] = ['__book_%s_prompt__' % s for s in refs]
    G['book_prompt_fill'] = ['__book_%s_prompt_fill__' % s for s in refs]
    G['book_short'] = ['__book_%s_short__' % s for s in refs]
    G['book_phrase'] = ['__book_%s_phrase__' % s for s in refs]
    G['book_look'] = ['__book_%s_look__' % s for s in refs]
    G['book_stack_prompt'] = ['A stack of three books on __book_rest__. The top one is __book_phrase__. The middle one is __book_phrase__. The bottom one is __book_phrase__.']
    G['book_row_prompt'] = ['A row of books standing on a shelf, their spines showing __book_spine__ and __book_spine__. One is __book_phrase__. A gap shows where a book has been taken out.']
    return G

# ---------------------------------------------------------------- periodicals
def mag_name(r):
    a = r.choice(P("Modern; Weekly; Country; Home; Garden; Motor; Radio; Screen; Sport; Style; Science; Travel; Youth; Family; Popular; Evening; Illustrated; Practical; Cinema; Adventure; Gentleman's; Ladies'; Farm; Boating; Camera; Trade"))
    b = r.choice(P("Life; Digest; Review; Monthly; Magazine; Companion; Journal; Gazette; Illustrated; World; Digest; Quarterly; Weekly; Mirror; Post; Times; Courier; Echo; Herald"))
    return '%s %s' % (a, b)
def comic_title(r):
    a = r.choice(P("Captain; Doctor; Shadow; Iron; Mighty; Star; Night; Rocket; Thunder; Crimson; Silver; Phantom; Atomic; Jungle; Secret; Cosmic; Steel; Savage; Ghost; Lightning"))
    b = r.choice(P("Comet; Falcon; Wasp; Ranger; Hawk; Avenger; Knight; Marvel; Wolf; Pilot; Raven; Defender; Sentinel; Titan; Fox; Panther; Crusader; Scout; Viper; Hunter"))
    return '%s %s' % (a, b)
def paper_name(r):
    a = r.choice(P("Daily; Evening; Morning; Sunday; Weekly; National; County; City; Harbour; Valley; Border; Northern; Metropolitan; Borough; Coastal; Mountain; Prairie; Capital; Provincial; Midland"))
    b = r.choice(P("Chronicle; Courier; Herald; Gazette; Tribune; Sentinel; Standard; Mercury; Record; Clarion; Observer; Dispatch; Examiner; Messenger; Telegraph; Bulletin; Ledger; Advertiser; Star; Beacon"))
    return 'The %s %s' % (a, b)
def zine_title(r):
    return r.choice(P("Basement Noise; Cut and Paste; Static; Soft Rot; Loose Leaf; Bad Tooth; Paper Cuts; Late Bloomer; Spare Change; Tin Can; Kitchen Floor; Fuzz; Dial Tone; Overgrown; Sticky Notes; Stray Dogs; Pocket Lint; Snail Mail; Dead Air; Tape Hiss"))
MAG_KIND = {
 'fashion magazine': ('glossy', 'a close portrait of a model in a bold outfit', ['Spring Looks Under Budget', 'Ten Coats for the Cold Months', 'The Return of Long Skirts', 'Shoes You Can Walk In']),
 'news magazine': ('glossy', 'a dramatic photograph of a crowd in a city square', ['The Year Ahead', 'Inside the Election Race', 'A Nation at the Crossroads', 'Why Prices Keep Rising']),
 'home and garden magazine': ('glossy', 'a sunlit kitchen with potted herbs', ['Small Gardens, Big Ideas', 'Paint Your Hallway in a Weekend', 'Houseplants That Survive Anything', 'The Cottage Border']),
 'science magazine': ('glossy', 'a colourful illustration of a distant galaxy', ['How the Brain Stores a Memory', 'New Light on Old Stars', 'The Deep Sea Revealed', 'Can We Grow Food on Mars?']),
 'motoring magazine': ('glossy', 'a low sports car on a mountain road', ['Six Roadsters Tested', 'The Last Great Coupes', 'Winter Tyres Explained', 'Restoring a Barn Find']),
 'cooking magazine': ('glossy', 'a golden pie on a wooden table', ['Pies for Every Table', 'One-Pan Suppers', 'Bake the Perfect Loaf', 'Spices of the Coast']),
 'film magazine': ('glossy', 'a smouldering portrait of a film star in a spotlight', ['Stars of the New Season', 'Behind the Scenes on Location', 'The Great Costume Dramas', 'Premiere Night in Pictures']),
 'sports magazine': ('glossy', 'an athlete leaping with arms raised', ['Season Preview', 'The Greatest Comebacks', 'Training Secrets of the Champions', 'Your Weekend Match Guide']),
 'travel magazine': ('glossy', 'a harbour town at sunrise', ['Slow Trains Through the Alps', 'Ten Islands Off the Map', 'A Week in the Highlands', 'Markets of the Old City']),
 'pulp magazine': ('rough pulp', 'a lurid painted scene of a hero with a ray gun', ['The Thing in the Cellar', 'Rocket to the Red Moon', 'Death Rides the Night Train', 'Terror from the Deep']),
 'radio and television listings magazine': ('thin newsprint', 'a smiling presenter beside a television set', ['This Week\'s Programmes', 'Your Guide to the Evening', 'Stars at Home', 'Win a Holiday']),
 'women\'s weekly': ('soft glossy', 'a smiling woman with a tray of baking', ['Dinners on a Budget', 'Knitting for Winter', 'The Secrets of a Happy Marriage', 'Hats for the Races']),
}
KW = {'fashion magazine': 'Style; Elegance; Chic; Mode; Glamour; Silhouette; Couture', 'news magazine': 'World; National; Weekly; Dispatch; Chronicle; Review; Report; Courier', 'home and garden magazine': 'Home; Garden; Cottage; Hearth; Country; Practical; Gardener; Household', 'science magazine': 'Science; Discovery; Popular; Modern; Cosmos; Inquiry; Nature; Future', 'motoring magazine': 'Motor; Road; Auto; Motoring; Speed; Drive; Wheels; Engine', 'cooking magazine': 'Kitchen; Cook; Good Table; Recipe; Taste; Pantry; Table; Baker', 'film magazine': 'Screen; Cinema; Picture; Film; Star; Movie; Matinee; Studio', 'sports magazine': 'Sport; Athlete; Champion; Field; Arena; Game; Stadium; Team', 'travel magazine': 'Voyage; Travel; Journey; Passport; Horizon; Explorer; Atlas; Wanderer', 'pulp magazine': 'Amazing; Thrilling; Astounding; Weird; Fantastic; Startling; Dime; Pulp', "women's weekly": "Woman's; Ladies'; Family; Home; Weekly; Fireside; Companion; Household", 'radio and television listings magazine': 'Radio; Television; Listener; Viewer; Airwaves; Broadcast; Tuner; Dial'}
SUF = 'Monthly; Magazine; Review; Digest; Illustrated; Quarterly; Weekly; Journal; Gazette; World; News; Companion'
def kind_name(t):
    def f(r):
        a = r.choice([x.strip() for x in KW[t].split(';') if 'like' not in x]); b = r.choice([x.strip() for x in SUF.split(';')])
        return '%s %s' % (a, b)
    return f
def build_periodicals():
    G = {}
    G['mag_masthead'] = ['"%s"' % x for x in pool(31, 300, mag_name)]
    G['mag_issue'] = ['"Issue %d"' % n for n in (3, 7, 12, 19, 24, 31, 48, 62, 77, 103, 118, 142)] + ['"%s"' % m for m in P("January; February; March; April; May; June; July; August; September; October; November; December")] + ['"Spring Number"', '"Summer Special"', '"Christmas Number"', '"Annual Edition"', '"Vol. 9, No. 4"', '"Vol. 22, No. 11"']
    G['mag_price'] = ['"%s"' % p for p in PRICE_TAG]
    G['mag_condition'] = P("crisp and new; creased down the middle; torn across the cover; missing a corner; yellowed; marked by a coffee ring; curled at the edges; stuck with a mailing label on the cover; folded back on itself; sun-faded; stamped with a subscriber's address sticker; thumbed soft; water-damaged with rippled pages; half-filled with pencilled crossword answers; coming apart at the centre pages")
    G['mag_state'] = P("lying face up; lying open to a double-page spread; rolled into a tube; held open under a thumb; fanned out in a pile; lying face down and open; stacked in a tall pile")
    G['mag_rest'] = P("a coffee table; a waiting-room chair; a train seat; a barber's shelf; a magazine rack; a hospital bedside table; a floor beside a sofa; a café table; a bathroom shelf; a doctor's reception desk; a newsstand shelf; a kitchen table")
    G['mag_kinds'] = list(MAG_KIND)
    refs = []
    for t, (paper, cover, heads) in MAG_KIND.items():
        s = slug(t)
        G['mag_%s_headline' % s] = ['"%s"' % h for h in heads]
        G['mag_%s_masthead' % s] = ['"%s"' % x for x in pool(31 + len(s), 60, kind_name(t))]
        G['mag_%s_look' % s] = ['A %s with __mag_%s_masthead__ printed across the top in large letters and __mag_issue__ beneath. The cover shows %s, printed on %s paper. Cover lines read __mag_%s_headline__ and __mag_%s_headline__. The price is __mag_price__.' % (t, s, cover, paper, s, s)]
        G['mag_%s_look_fill' % s] = ['A %s with "MAGAZINE NAME" printed across the top in large letters and "ISSUE" beneath. The cover shows %s, printed on %s paper. Cover lines read "HEADLINE ONE" and "HEADLINE TWO". The price is "PRICE".' % (t, cover, paper)]
        G['mag_%s_prompt' % s] = ['__mag_%s_look__ The magazine is __mag_condition__, __mag_state__ on __mag_rest__.' % s]
        G['mag_%s_prompt_fill' % s] = ['__mag_%s_look_fill__ The magazine is __mag_condition__, __mag_state__ on __mag_rest__.' % s]
        G['mag_%s_short' % s] = ['A %s titled __mag_%s_masthead__, with %s on the cover.' % (t, s, cover)]
        refs.append(s)
    G['mag_prompt'] = ['__mag_%s_prompt__' % s for s in refs]
    G['mag_prompt_fill'] = ['__mag_%s_prompt_fill__' % s for s in refs]
    G['mag_short'] = ['__mag_%s_short__' % s for s in refs]
    # comics and graphic novels
    G['comic_title'] = ['"%s"' % x for x in pool(41, 300, comic_title)]
    G['comic_cover'] = P("a hero bursting through a wall with a clenched fist; a masked figure crouched on a rooftop at night; a rocket ship streaking past a ringed planet; a cowboy facing a gunslinger on a dusty street; two rivals locked in a fight under a cracked moon; a giant monster looming over a small town; a detective in a trench coat under a street lamp; a girl with a sword standing on a ruined tower; a robot reaching toward a child; a pirate captain at the helm in a storm; a ghost floating in a hallway; a crowd of animals in a cartoon marketplace; a team of heroes in a dramatic line-up")
    G['comic_era'] = P("a golden age comic of the 1940s with bold flat colours and a cover price of ten cents; a 1960s comic with a halftone dot cover and a corner box; a 1970s comic with a warning stamp and a grainy cover; an 1980s comic with a glossy cover and a barcode; a modern comic with a clean digital cover; a hand-stapled independent comic with a black-and-white cover")
    G['comic_condition'] = P("mint in a clear bag with a backing board; creased along the spine and sun-faded on the cover; torn across the cover and missing a corner; cut where a coupon was removed; marked with a name on the cover; yellowed at the edge with a rusty staple; heavily read with a rolled spine; marked by a price sticker; stained on the back; slipped into a plastic sleeve")
    G['comic_look'] = ['A comic book titled __comic_title__ in jagged lettering above a cover of __comic_cover__. It is __comic_era__, and it is __comic_condition__.']
    G['comic_look_fill'] = ['A comic book titled "COMIC TITLE" in jagged lettering above a cover of __comic_cover__. It is __comic_era__, and it is __comic_condition__.']
    G['graphic_novel_look'] = ['A graphic novel titled __comic_title__ and "VOLUME TWO", a thick __book_binding__ with a cover of __comic_cover__. The author is __book_author__ and the book is __book_condition__.']
    G['comic_prompt'] = ['__comic_look__ It is __mag_state__ on __mag_rest__.']
    G['comic_prompt_fill'] = ['__comic_look_fill__ It is __mag_state__ on __mag_rest__.']
    # newspapers
    G['paper_masthead'] = ['"%s"' % x for x in pool(51, 250, paper_name)]
    G['paper_headline'] = ['"%s"' % h for h in P("Storm Closes the Coast Road; Council Votes to Save the Library; Local Team Wins the Cup; Prices Rise Again at the Market; Bridge to Reopen in Spring; Fire at the Old Mill; Record Harvest Expected; New Station Opens Downtown; Mayor Defends Budget; Heatwave Grips the Region; Flood Waters Recede; Lost Dog Found After Three Days; Strike Ends After Long Talks; Rare Bird Spotted at the Marsh; Festival Draws Thousands; Schools Reopen Early; Ferry Service Resumes; Traffic Chaos at the Junction")]
    G['paper_edition'] = ['"%s"' % e for e in P("Late Edition; Morning Edition; Sunday Edition; Final Edition; Evening Edition; Special Edition; Weekend Edition; Extra")]
    G['paper_size'] = P("broadsheet; tabloid; thick Sunday; thin local weekly; single-sheet extra")
    G['paper_fold'] = P("folded in half; rolled and held by a rubber band; crumpled; folded with the crossword half done; tied with string; cut with a hole where an article was removed; left damp on a doorstep; spread open on the page with the headline")
    G['paper_look'] = ['A __paper_size__ newspaper titled __paper_masthead__ with __paper_edition__ beneath. The front page has the headline __paper_headline__ above a large photograph, in closely set columns of small print. It is __paper_fold__.']
    G['paper_look_fill'] = ['A __paper_size__ newspaper titled "NEWSPAPER NAME" with "EDITION" beneath. The front page has the headline "HEADLINE" above a large photograph, in closely set columns of small print. It is __paper_fold__.']
    G['paper_prompt'] = ['__paper_look__ It is __mag_condition__, lying on __mag_rest__.']
    G['paper_prompt_fill'] = ['__paper_look_fill__ It is __mag_condition__, lying on __mag_rest__.']
    # zines and pamphlets
    G['zine_title'] = ['"%s"' % x for x in P("Basement Noise; Cut and Paste; Static; Soft Rot; Loose Leaf; Bad Tooth; Paper Cuts; Late Bloomer; Spare Change; Tin Can; Kitchen Floor; Fuzz; Dial Tone; Overgrown; Sticky Notes; Stray Dogs; Pocket Lint; Snail Mail; Dead Air; Tape Hiss")]
    G['zine_look'] = ['A hand-made zine titled __zine_title__ in cut-out letters, a photocopied booklet folded and stapled, with a cover of __comic_cover__ in grainy black and white. It is __mag_condition__, lying on __mag_rest__.']
    G['zine_look_fill'] = ['A hand-made zine titled "ZINE TITLE" in cut-out letters, a photocopied booklet folded and stapled, with a cover of __comic_cover__ in grainy black and white. It is __mag_condition__, lying on __mag_rest__.']
    G['pamphlet_kind'] = P('a tri-fold tourist leaflet; a church service sheet; a concert programme; a museum guide; a political leaflet; a seed catalogue; a mail-order catalogue; a railway timetable booklet; a theatre programme; a street map folded in panels; a school prospectus; a cinema flyer')
    G['pamphlet_look'] = ['A pamphlet, %s, with the title "PAMPHLET TITLE" on the front, printed in __book_cover_colour__ ink on cream paper. It is __mag_condition__.' % '__pamphlet_kind__']
    # reading accessories
    G['bookmark_type'] = P("a silk ribbon sewn into the spine; a leather corner bookmark; a laminated paper bookmark with a tassel; a pressed flower between pages; a brass clip bookmark; a magnetic page marker; a cardboard bookmark with a printed quote; a folded ticket stub; a postcard used as a marker; a woven cord with a charm; a wooden thumb-shaped bookmark; a metal page clip shaped like a cat; a strip of torn newspaper; a feather; a receipt; a dried leaf")
    G['book_holder'] = P("a folding wooden book stand; a brass reading stand with a lip; a cushioned lap cradle; a pair of page-holding weights on a chain; a clear plastic page holder; a bean-filled book support; a carved wooden lectern; a spring clip holding a paperback open; a metal music-style stand; a thumb ring page holder; a wall-mounted swing arm book holder; a bedside tray with a page rest; an acrylic tablet stand; an old library reading desk with a sloped top")
    G['book_light'] = P("a clip-on reading light; a brass desk lamp with a green shade; a candle in a holder; a head-mounted reading torch; a bedside lamp with a fabric shade; a lantern on a ledge; a glowing screen; a small reading light with a flexible neck")
    G['reading_scene_prompt'] = ['A person reading, holding __book_phrase__. They sit on __book_rest__ with __bookmark_type__ tucked in and __book_light__ shining on the pages. Nearby is __book_holder__.']
    G['reading_prompt'] = ['__book_prompt__', '__mag_prompt__', '__comic_prompt__', '__paper_prompt__', '__zine_look__', '__graphic_novel_look__', '__reading_scene_prompt__']
    G['reading_prompt_fill'] = ['__book_prompt_fill__', '__mag_prompt_fill__', '__comic_prompt_fill__', '__paper_prompt_fill__', '__zine_look_fill__']
    return G

def build(final=None):
    G = build_books(); G.update(build_periodicals())
    G['v74_reading_entry_points'] = ['reading_prompt', 'reading_prompt_fill', 'book_prompt', 'book_prompt_fill', 'mag_prompt', 'comic_prompt', 'paper_prompt']
    return G
