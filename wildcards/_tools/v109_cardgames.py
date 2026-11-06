"""v109 - card game generator (user 2026-11-06): generic, unbranded versions of family card games, built like the trading cards.
Every game is described by how it looks and works rather than by a trademarked name, and every word or number on a card is quoted.
Games: a trick-taking game with four coloured suits numbered 1 to 14 and a bird card; a road-race game of distance, hazard, remedy
and safety cards; a picture-matching fishing game; a stats-comparison game of themed cards with quoted numbers; a colour-matching
shedding game with number and action cards; a happy-families game of illustrated family members; a snap game of paired pictures;
and an ordinary deck of playing cards. Each can be shown as one card, a hand of cards, a game in play on a table, the box, or a
spread of worn cards, in the look of its decade.

Files: cg_<game>_card (one card), cg_<game>_hand_prompt, cg_<game>_play_prompt, cg_<game>_box_prompt, cg_<game>_card_prompt,
       cg_decade_<d>_look, cg_condition, cg_table, cg_photo, cg_title, cg_any_prompt."""
import random
DECADES = ['1910s', '1930s', '1950s', '1970s', '1990s', '2020s']
LOOK = {
 '1910s': 'printed by stone lithography in soft muted colours on thin buff card with ornate scrolled borders and fine engraved-style drawings',
 '1930s': 'printed in two or three flat colours on thick cream card with a fine linen texture, with small neat lettering and simple line drawings',
 '1950s': 'printed in cheerful bright colours on glossy white card with rounded corners and painted illustrations',
 '1970s': 'printed in bold orange, brown and mustard tones with chunky rounded lettering and stylised drawings',
 '1990s': 'printed in bright saturated colours on plastic-coated card with bold outlined cartoon art',
 '2020s': 'printed in clean modern colours on smooth matte card with flat graphic illustrations and neat sans-serif lettering',
}
CONDITION = ['The cards are crisp and new, with sharp corners and bright colours.', 'The cards are well used, softened and slightly curled, with rounded corners.',
             'The cards are old and dog-eared, the corners bent over and the backs rubbed pale.', 'The cards are faded and yellowed, with a few creases and a coffee ring on one.',
             'The cards are grubby and darkened along the edges from years of family games.', 'The cards are almost new, with one bent corner.']
TABLE = ['a wooden kitchen table', 'a green felt card table', 'a tartan picnic blanket on grass', 'a pub table with beer mats', 'a train table by a window', 'a caravan table under a lamp', 'a living room rug']
PHOTO = ['Natural light photograph with true colours, every card clearly readable.', 'Photograph from directly above, every card in sharp focus.', 'Warm photograph at table height with a shallow depth of field.']
TITLE = ['__name_hero_adj__ __name_hero_noun__', '__name_town__ Rally', 'Grand __name_hero_noun__', 'The Great __name_word__ Game', '__name_word__ and __name_word__']

COLOURS = ['red', 'yellow', 'green', 'black']
def trick():
    # the full deck: every number 1 to 14 in each of the four colours, plus the bird card (57 cards)
    cards = ['a %s card with a large number "%d" in the centre and in two corners, on a plain white face with a %s border' % (c, n, c) for c in COLOURS for n in range(1, 15)]
    cards += ['the special bird card, showing a black crow with spread wings and the word "CROW" across the top']
    return cards
# Road-race games with the same rules go back over a century under many themes: the deck always has distance cards, hazards,
# the remedy for each hazard and a safety card for each hazard. Pictures and wording change with the theme.
RACE = {
 'motorcar': ('KM', 'a small car speeding along a road', [('a car with a burst tyre', 'FLAT TYRE', 'a spare wheel', 'SPARE TYRE', 'a tyre with a shield over it', 'PUNCTURE PROOF'),
              ('two crashed cars', 'ACCIDENT', 'a spanner and a jack', 'REPAIRS', 'a driver in goggles waving', 'ACE DRIVER'), ('a car beside an empty fuel can', 'OUT OF FUEL', 'a fuel pump', 'FUEL', 'an extra fuel tank', 'EXTRA TANK'),
              ('a red traffic light', 'STOP', 'a green traffic light', 'GO', 'a car passing every light', 'RIGHT OF WAY'), ('a round speed sign', 'SPEED LIMIT', 'a crossed-out speed sign', 'END OF LIMIT', None, None)]),
 'cyclist': ('MILES', 'a racing cyclist pedalling hard along a country road', [('a bicycle with a flat tyre', 'PUNCTURE', 'a pump and a patch kit', 'MENDED', 'a tyre wrapped in a shield', 'SOLID TYRES'),
              ('a rider tumbled off on the road', 'FALL', 'a bandaged rider remounting', 'BACK IN THE SADDLE', 'a rider with a laurel wreath', 'CHAMPION RIDER'), ('a rider slumped with exhaustion', 'EXHAUSTED', 'a rider drinking from a bottle', 'REFRESHED', 'a rider with a basket of food', 'FULL BASKET'),
              ('a closed level crossing gate', 'STOP', 'an open level crossing gate', 'GO', 'a rider waved through by a policeman', 'RIGHT OF WAY'), ('a steep hill sign', 'STEEP HILL', 'a downhill sign', 'END OF HILL', None, None)]),
 'aeroplane': ('MILES', 'a biplane flying over fields', [('a plane in a thunderstorm', 'STORM', 'clearing skies', 'CLEAR SKIES', 'a plane above the clouds', 'ALL WEATHER'),
              ('a plane with a smoking engine', 'ENGINE FAILURE', 'a mechanic with a spanner', 'REPAIRED', 'a pilot with a medal', 'ACE PILOT'), ('a plane with an empty tank gauge', 'NO FUEL', 'a fuel tanker on the runway', 'REFUELLED', 'a plane with extra wing tanks', 'LONG RANGE'),
              ('a red runway light', 'GROUNDED', 'a green runway light', 'CLEARED TO FLY', 'a plane with a priority flag', 'PRIORITY'), ('a thick fog bank', 'FOG', 'the sun breaking through', 'FOG LIFTS', None, None)]),
 'coach': ('MILES', 'a horse-drawn coach racing along a lane', [('a coach with a broken wheel', 'BROKEN WHEEL', 'a wheelwright with a new wheel', 'NEW WHEEL', 'an iron-rimmed wheel', 'IRON WHEELS'),
              ('a lame horse', 'LAME HORSE', 'a fresh horse led out', 'FRESH HORSE', 'a coachman with a whip held high', 'MASTER COACHMAN'), ('an empty hay sack', 'NO FODDER', 'a bale of hay', 'FODDER', 'a heaped feed cart', 'FULL STORES'),
              ('a closed toll gate', 'TOLL GATE', 'an open toll gate', 'PAID', 'a royal crest on a coach door', 'ROYAL WARRANT'), ('a muddy flooded road', 'MUD', 'a dry road', 'DRY ROAD', None, None)]),
 'motorbike': ('KM', 'a motorbike racing along a winding road', [('a motorbike with a flat tyre', 'FLAT TYRE', 'a spare tube', 'SPARE TUBE', 'a solid tyre with a shield', 'PUNCTURE PROOF'),
              ('a bike lying on its side', 'SPILL', 'a mechanic at work', 'REPAIRS', 'a rider standing on the footpegs', 'ACE RIDER'), ('an empty petrol can', 'OUT OF PETROL', 'a petrol can being poured', 'PETROL', 'a big long-range tank', 'EXTRA TANK'),
              ('a red light', 'STOP', 'a green light', 'GO', 'a police escort on bikes', 'RIGHT OF WAY'), ('a speed sign', 'SPEED LIMIT', 'an end of limit sign', 'END OF LIMIT', None, None)]),
}
DIST = ['25', '50', '75', '100', '200']
def race_theme(t):
    unit, pic, rows = RACE[t]; out = []
    out += ['a white distance card with "%s %s" in big letters across the top, a picture of %s in the middle, and "MOVE AHEAD %s %s" in small letters in a box at the bottom' % (d, unit, pic, d, unit) for d in DIST]
    for hp, hw, rp, rw, sp, sw in rows:
        out.append('a red-bordered hazard card with "%s" across the top, a picture of %s in the middle, and "PLAY ON AN OPPONENT TO STOP THEM" in small letters in a box at the bottom' % (hw, hp))
        out.append('a green-bordered remedy card with "%s" across the top, a picture of %s in the middle, and "CURES %s" in small letters in a box at the bottom' % (rw, rp, hw))
        if sp: out.append('a blue-bordered safety card with "%s" across the top, a picture of %s in the middle, and "SAFE FROM %s FOR THE WHOLE GAME" in small letters in a box at the bottom' % (sw, sp, hw))
    return out
def race(): return [c for t in RACE for c in race_theme(t)]
FISH = [('CLOWN FISH', 'an orange fish with white stripes'), ('BLUE TANG', 'a bright blue fish with a yellow tail'), ('PUFFER FISH', 'a round spiky yellow fish puffed up'), ('OCTOPUS', 'a purple octopus with curly arms'),
        ('CRAB', 'a red crab waving its claws'), ('SEAHORSE', 'a curled yellow seahorse'), ('STARFISH', 'an orange starfish'), ('WHALE', 'a big friendly blue whale'), ('SHARK', 'a grey shark with a toothy grin'), ('TURTLE', 'a green sea turtle')]
def fish(): return ['a picture card of %s on a pale blue sea background, with the name "%s" printed at the bottom' % (p, n) for n, p in FISH]
STATS = {
 'cars': (['a low red sports car', 'a boxy blue family estate car', 'a yellow rally car splashed with mud', 'a silver luxury saloon', 'a tiny green city car', 'a black muscle car with a long bonnet'],
          ['THUNDER GT', 'FAMILY STAR', 'MUD RUNNER', 'SILVER CROWN', 'CITY BUG', 'NIGHT HAMMER'], [('TOP SPEED', 'mph', 80, 210), ('POWER', 'bhp', 50, 650), ('WEIGHT', 'kg', 700, 2200), ('0-60', 'secs', 3, 16)]),
 'dinosaurs': ([x for x in ['a tyrannosaurus with huge jaws', 'a three-horned triceratops', 'a long-necked plant eater', 'a stegosaurus with tall back plates', 'a small feathered raptor', 'a flying reptile with leathery wings']],
          ['TYRANNOSAURUS', 'TRICERATOPS', 'BRACHIOSAURUS', 'STEGOSAURUS', 'VELOCIRAPTOR', 'PTERANODON'], [('HEIGHT', 'm', 1, 13), ('WEIGHT', 'tonnes', 1, 50), ('SPEED', 'km/h', 10, 60), ('KILLER RATING', '/10', 1, 10)]),
 'aircraft': (['a silver propeller fighter plane', 'a huge four-engine airliner', 'a black jet fighter with swept wings', 'a red stunt biplane', 'a yellow seaplane on floats', 'a big grey cargo plane'],
          ['SKY HAWK', 'JUMBO STAR', 'SHADOW JET', 'LOOP RED', 'LAKE HOPPER', 'HEAVY LIFTER'], [('TOP SPEED', 'mph', 120, 1400), ('RANGE', 'miles', 300, 8000), ('WINGSPAN', 'm', 8, 68), ('CREW', '', 1, 14)]),
 'monsters': (['a hairy swamp monster dripping weed', 'a giant robot with glowing eyes', 'a three-headed dragon', 'a jelly blob monster', 'a stone giant', 'a shadowy vampire bat'],
          ['BOG BEAST', 'MEGA BOT', 'TRI-DRAGON', 'GLOOP', 'ROCK TITAN', 'NIGHT WING'], [('STRENGTH', '', 10, 100), ('FEAR FACTOR', '', 10, 100), ('SPEED', '', 10, 100), ('MAGIC', '', 10, 100)]),
 'ships': (['a tall sailing ship', 'a grey battleship', 'a bright tugboat', 'a sleek white cruise liner', 'a rusty cargo ship', 'a submarine breaking the surface'],
          ['SEA QUEEN', 'IRON GUARD', 'LITTLE TUG', 'OCEAN PEARL', 'RUST BUCKET', 'DEEP RAY'], [('LENGTH', 'm', 20, 340), ('SPEED', 'knots', 5, 35), ('CREW', '', 4, 2000), ('BUILT', '', 1890, 2020)]),
}
def stats():
    R = random.Random(10901 * 7 + 3); out = []
    for theme, (pics, names, cats) in STATS.items():
        for pic, name in zip(pics, names):
            lines = ['"%s %d%s" on the %s line' % (c, R.randint(lo, hi), (' ' + u if u and not u.startswith('/') else u), o) for (c, u, lo, hi), o in zip(cats, ('first', 'second', 'third', 'fourth'))]
            out.append('a %s stats card with a picture of %s in the top half, the name "%s" across the middle, and a list below reading %s' % (theme, pic, name, ', '.join(lines)))
    return out
def shed():
    cs = ['red', 'blue', 'green', 'yellow']
    out = ['a %s card with a big white oval tilted across the middle holding the number "%d"' % (c, n) for c in cs for n in (0, 3, 7, 9)]
    out += ['a %s action card with two curved arrows and the words "%s"' % (c, w) for c in cs for w in ('REVERSE',)]
    out += ['a %s action card with a circle crossed by a line and the word "SKIP"' % c for c in cs]
    out += ['a %s action card with two small stacked cards and "+2" in the centre' % c for c in cs]
    out += ['a black wild card with a circle split into red, blue, green and yellow quarters and the word "WILD"']
    return out
FAMILY = [('Mr', 'the Baker', 'a round man in a tall white hat holding a loaf'), ('Mrs', 'the Baker', 'a smiling woman in an apron with a tray of buns'), ('Master', 'the Baker', 'a boy carrying a basket of rolls'),
          ('Mr', 'the Butcher', 'a man in a striped apron holding a string of sausages'), ('Mrs', 'the Grocer', 'a woman weighing apples on a scale'), ('Mr', 'the Postman', 'a man with a sack of letters'),
          ('Mrs', 'the Painter', 'a woman holding a dripping brush'), ('Mr', 'the Fisherman', 'a man in a sou\'wester holding a big fish')]
def family(): return ['a happy families card with a funny painted picture of %s and the name "%s __name_surname__ %s" printed at the bottom' % (p, a, b) for a, b, p in FAMILY]
SNAP = ['a red apple', 'a blue umbrella', 'a yellow duck', 'a green frog', 'a brown teddy bear', 'a striped cat', 'a spotted dog', 'an orange carrot']
def snap(): return ['a snap card with a single picture of %s in the middle of a white face with a coloured border' % p for p in SNAP]
SUITS = [('hearts', 'red', 'heart'), ('diamonds', 'red', 'diamond'), ('clubs', 'black', 'club'), ('spades', 'black', 'spade')]
RANKS = [('ace', 'A'), ('two', '2'), ('three', '3'), ('four', '4'), ('five', '5'), ('six', '6'), ('seven', '7'), ('eight', '8'), ('nine', '9'), ('ten', '10')]
FACES = [('jack', 'J', 'a young man in a feathered cap shown in profile'), ('queen', 'Q', 'a crowned woman holding a flower'), ('king', 'K', 'a bearded crowned king holding a sword')]
def playing():
    out = ['a playing card, the %s of %s, with "%s" and a small %s %s in two corners and %s %s symbols laid out in the middle' % (r, s, v, c, sym, c, sym) for s, c, sym in SUITS for r, v in RANKS]
    out += ['a playing card, the %s of %s, with "%s" in two corners and a mirrored double-ended picture of %s in %s and gold' % (r, s, v, pic, c) for s, c, sym in SUITS for r, v, pic in FACES]
    out += ['a joker card showing a jester in a belled hat and the word "JOKER" down one side', 'a second joker card showing a grinning jester juggling, with "JOKER" in two corners']
    return out
# Tarot: the 22 trump cards each with its traditional title and picture, and four suits of fourteen cards
MAJOR = [('0', 'THE FOOL', 'a young traveller with a bundle on a stick stepping towards a cliff edge with a small dog'), ('I', 'THE MAGICIAN', 'a figure at a table of cup, wand, sword and coin, one arm raised'),
         ('II', 'THE HIGH PRIESTESS', 'a robed woman seated between a dark and a light pillar holding a scroll'), ('III', 'THE EMPRESS', 'a crowned woman on cushions in a field of wheat'),
         ('IV', 'THE EMPEROR', 'a bearded ruler on a stone throne carved with rams'), ('V', 'THE HIEROPHANT', 'a robed religious figure raising two fingers before two kneeling followers'),
         ('VI', 'THE LOVERS', 'a man and a woman standing beneath a winged figure in the sun'), ('VII', 'THE CHARIOT', 'a crowned figure in a chariot drawn by one black and one white sphinx'),
         ('VIII', 'STRENGTH', 'a woman gently closing the jaws of a lion'), ('IX', 'THE HERMIT', 'an old cloaked man holding a lantern on a mountain top'),
         ('X', 'WHEEL OF FORTUNE', 'a great wheel marked with symbols turning in the clouds'), ('XI', 'JUSTICE', 'a seated figure holding scales and an upright sword'),
         ('XII', 'THE HANGED MAN', 'a calm man hanging upside down by one foot from a living tree, a glow round his head'), ('XIII', 'DEATH', 'a skeleton in black armour on a white horse carrying a banner with a white rose'),
         ('XIV', 'TEMPERANCE', 'a winged figure pouring water between two cups, one foot in a stream'), ('XV', 'THE DEVIL', 'a horned goat-headed figure above two chained figures'),
         ('XVI', 'THE TOWER', 'a tall tower struck by lightning, its crown blown off and flames from the windows'), ('XVII', 'THE STAR', 'a kneeling figure pouring water into a pool under one large star and seven small ones'),
         ('XVIII', 'THE MOON', 'a moon with a face above a dog and a wolf howling, a crayfish crawling from a pool'), ('XIX', 'THE SUN', 'a bright smiling sun above a child on a white horse among sunflowers'),
         ('XX', 'JUDGEMENT', 'a winged figure blowing a trumpet as figures rise from below with raised arms'), ('XXI', 'THE WORLD', 'a dancing figure inside a wreath with a creature in each corner')]
MINOR_SUITS = [('WANDS', 'wooden staffs sprouting leaves'), ('CUPS', 'golden goblets'), ('SWORDS', 'steel swords'), ('PENTACLES', 'gold coins marked with a five-pointed star')]
MINOR_RANKS = ['ACE', 'TWO', 'THREE', 'FOUR', 'FIVE', 'SIX', 'SEVEN', 'EIGHT', 'NINE', 'TEN']
COURT = [('PAGE', 'a youth holding'), ('KNIGHT', 'a knight on horseback holding'), ('QUEEN', 'a crowned queen on a throne holding'), ('KING', 'a crowned king on a throne holding')]
def tarot():
    out = ['a tarot card numbered "%s" at the top and titled "%s" at the bottom, showing %s' % (n, t, p) for n, t, p in MAJOR]
    out += ['a tarot card titled "%s OF %s" at the bottom, showing %s' % (r, s, ('a single large one of the ' + d + ' held by a hand from a cloud') if r == 'ACE' else ('%s %s arranged in a pattern' % (r.lower(), d))) for s, d in MINOR_SUITS for r in MINOR_RANKS]
    out += ['a tarot card titled "%s OF %s" at the bottom, showing %s one of the %s' % (c, s, who, d) for s, d in MINOR_SUITS for c, who in COURT]
    return out
GAMES = {
 'trick': ('a trick-taking card game played with a 57-card deck of four coloured suits, red, yellow, green and black, each numbered 1 to 14, and one special bird card', trick(), 'players taking turns to lay one card each into the middle to win the trick, a small pile of won tricks beside each player and a score pad with a pencil'),
 'race': ('a road-race card game in which players lay distance cards to reach the finish while playing hazards on each other, fixing them with remedy cards and protecting themselves with safety cards', race(), 'each player\'s row of laid distance cards in front of them, a hazard card laid on top of one player\'s pile and the draw pile in the middle'),
 'fish': ('a fishing card game in which players ask each other for matching picture cards to collect sets of four', fish(), 'a messy pond of face-down cards in the middle and a few finished sets of four laid face up'),
 'stats': ('a stats comparison card game in which players read out one number from their top card and the highest number wins the cards', stats(), 'two players each holding a pile face down, the top cards turned over side by side to compare their numbers'),
 'shed': ('a colour-matching card game in which players try to get rid of their cards by matching the colour or number of the top card, with action cards that skip, reverse or make the next player draw', shed(), 'a discard pile in the middle with the top card face up, a draw pile beside it and players\' fanned hands'),
 'family': ('a happy families card game in which players collect the four members of each illustrated family', family(), 'completed families laid out in rows of four and a player holding a hand of picture cards'),
 'snap': ('a snap card game in which players turn cards over together and shout when two pictures match', snap(), 'two piles of face-up cards side by side showing the same picture and two hands slapping down at once'),
 'playing': ('an ordinary deck of 52 playing cards in four suits of hearts, diamonds, clubs and spades, ace to ten with a jack, queen and king in each suit, plus two jokers', playing(), 'a game of cards laid out with a few tricks taken, a discard pile and a scattering of coins'),
}
GAMES['tarot'] = ('a tarot deck of 78 cards, 22 picture trump cards with titles and four suits of wands, cups, swords and pentacles', tarot(), 'cards laid out in a cross-shaped spread on a cloth, a few turned face up and the rest of the deck stacked beside them')
for _t in RACE:
    GAMES['race_' + _t] = ('a road-race card game themed on %s, in which players lay distance cards to reach the finish while playing hazards on each other, fixing them with remedy cards and protecting themselves with safety cards' % {'motorcar': 'motorcars', 'cyclist': 'bicycle racing', 'aeroplane': 'aeroplane races', 'coach': 'horse-drawn coaches', 'motorbike': 'motorbike racing'}[_t],
                           race_theme(_t), 'each player\'s row of laid distance cards in front of them, a hazard card laid on top of one player\'s pile and the draw pile in the middle')
PARTS = {
 'trick': ['a score pad headed "SCORE" with columns for "US" and "THEM", and a short pencil', 'a small folded leaflet with "HOW TO PLAY" on the cover'],
 'race': ['a score pad headed "SCORE" with rows for "DISTANCE", "SAFETIES" and "TRIP COMPLETE"', 'a plastic card tray with divided slots for each player'],
 'fish': ['a small folded leaflet with cartoon fish and "HOW TO PLAY" on the cover'], 'stats': ['a small card listing "TOP SPEED", "POWER", "WEIGHT" and "0-60" down one side', 'a rubber band holding the deck together'],
 'shed': ['a score pad headed "SCORE" with columns of names', 'a small folded leaflet with "HOW TO PLAY" on the cover'], 'family': ['a small folded leaflet with a picture of the baker family and "HOW TO PLAY" on the cover'],
 'snap': ['a small folded leaflet with a picture of two hands slapping down and "HOW TO PLAY" on the cover'], 'playing': ['a cellophane wrapper torn open beside the deck', 'a pile of poker chips in red, white and blue'],
 'tarot': ['a small booklet with "THE MEANING OF THE CARDS" on the cover', 'a square of dark silk cloth for laying out the cards'],
}
BOX = ['a small flip-top card box of printed card with a tuck flap', 'a new deck still sealed in clear cellophane with a red tear strip', 'a hinged tin box with a printed lid', 'a two-part cardboard box with a lift-off lid and a plastic tray inside holding the cards',
       'a slim box with a die-cut window showing the top card', 'a worn cardboard box held shut with an elastic band']
BOX_COND = ['crisp and new', 'scuffed at the corners', 'with the lid split along one edge and taped', 'faded by sunlight', 'dented and well loved', 'with a price sticker still on the back']
from v109_cardgames2 import GAMES2, PARTS2
GAMES.update(GAMES2); PARTS.update(PARTS2)
def build(final=None):
    G = {}
    for d in DECADES: G['cg_decade_%s_look' % d] = [LOOK[d]]
    G['cg_decade_look'] = ['__cg_decade_%s_look__' % d for d in DECADES]
    G['cg_box_style'] = BOX; G['cg_box_condition'] = BOX_COND
    for k, v in PARTS.items(): G['cg_parts_%s' % k] = v
    G['cg_condition'] = CONDITION; G['cg_condition_one'] = [c.replace('The cards are', 'The card is').replace(' on one.', '.').replace('with one bent corner', 'with one bent corner') for c in CONDITION]; G['cg_table'] = TABLE; G['cg_photo'] = PHOTO; G['cg_title'] = TITLE
    allp = []
    for k, (desc, cards, play) in GAMES.items():
        b = 'cg_%s' % k
        G[b + '_desc'] = [desc]; G[b + '_card'] = cards
        G[b + '_card_prompt'] = ['A single card from __%s_desc__, lying on __cg_table__. It is __%s_card__, __cg_decade_look__. __cg_condition_one__ __cg_photo__' % (b, b)]
        G[b + '_hand_prompt'] = ['A hand of cards from __%s_desc__, fanned out in two hands seen from the player\'s own view above __cg_table__. The front card is __%s_card__, and behind it is __%s_card__. All the cards are __cg_decade_look__. __cg_condition__ __cg_photo__' % (b, b, b)]
        G[b + '_play_prompt'] = ['A tabletop scene of __%s_desc__, in progress on __cg_table__, with %s. The card on top is __%s_card__, and the other cards lie face down showing backs printed with a repeating pattern of small diamonds. The cards are __cg_decade_look__. __cg_condition__ __cg_photo__' % (b, play, b)]
        pk = 'race' if k.startswith('race') else k
        G[b + '_parts'] = ['__cg_parts_%s__' % pk]
        G[b + '_box_prompt'] = ['The box for __%s_desc__, __cg_box_style__, standing on __cg_table__, printed with the title "__cg_title__" across the front above a picture of __%s_card__, __cg_decade_look__. The box is __cg_box_condition__. __cg_photo__' % (b, b),
                                'The complete contents of __%s_desc__ laid out on __cg_table__ beside its open box, __cg_box_style__ printed with the title "__cg_title__", showing the deck squared up with __%s_card__ on top, and __%s_parts__. Everything is __cg_decade_look__. __cg_photo__' % (b, b, b)]
        G[b + '_play_prompt'] = [l.replace(' The card on top is', ' Next to the cards you can see __%s_parts__. The card on top is' % b) for l in G[b + '_play_prompt']]
        G[b + '_prompt'] = ['__%s_card_prompt__' % b, '__%s_hand_prompt__' % b, '__%s_play_prompt__' % b, '__%s_play_prompt__' % b, '__%s_box_prompt__' % b]
        allp.append('__%s_prompt__' % b)
    G['cg_any_prompt'] = allp
    return G
