# v109 card games, part 2: eleven more family and hobby card games with special decks, unbranded and described by look and rules.
# Together with v109_cardgames.GAMES these make the 20 most common kinds of special-deck card games of the last hundred years.
# Each entry: (description, cards, what a game in progress looks like); PARTS2: extra parts and packaging for each.

def old_maid():
    pairs = [('a grinning chimney sweep with a brush', 'SOOTY SAM'), ('a baker holding a cake', 'BAKER BILL'), ('a sailor with a pipe', 'SAILOR JACK'), ('a farmer with a pitchfork', 'FARMER GILES'),
             ('a nurse with a tray', 'NURSE NELL'), ('a policeman with a whistle', 'CONSTABLE CROW'), ('a clown with a red nose', 'CLOWN COCO'), ('a cook with a ladle', 'COOK KATE')]
    out = ['a pairs card with a funny painted picture of %s and the name "%s" printed at the bottom' % p for p in pairs]
    out.append('the single odd card left over, showing a cross old woman in a bonnet and the words "OLD MAID" at the bottom')
    return out
def pit():
    goods = [('sacks of golden wheat', 'WHEAT'), ('yellow corn cobs', 'CORN'), ('bundles of oats', 'OATS'), ('bales of barley', 'BARLEY'), ('bags of coffee beans', 'COFFEE'), ('bales of white cotton', 'COTTON'), ('a heap of sugar cane', 'SUGAR')]
    out = ['a trading card showing %s with the word "%s" across the top and "TRADE ME" in small letters at the bottom' % g for g in goods]
    out += ['a special card showing a charging bull with the word "BULL" across the top', 'a special card showing a grizzly bear with the word "BEAR" across the top']
    return out
def flinch():
    out = ['a number card with a big number "%d" printed in the centre and in each corner, the colour of the number changing from card to card' % n for n in range(1, 16)]
    out += ['a wild card in rainbow colours with the word "WILD" across the middle']
    return out
def phase():
    cs = ['red', 'blue', 'green', 'yellow']
    out = ['a %s number card with a big number "%d" in the centre' % (c, n) for c in cs for n in (1, 4, 8, 12)]
    out += ['a wild card with a starburst and the word "WILD"', 'a blue skip card with a circle crossed by a line and the word "SKIP"']
    return out
def bomb():
    out = ['a cartoon card with "BOOM CARD" across the top, a fizzing round black bomb with a lit fuse in the middle and "YOU ARE OUT" at the bottom', 'a card with "DEFUSE" across the top, a pair of wire cutters snipping a fuse in the middle and "SAVES YOU FROM THE BOMB" at the bottom',
           'a card with "SEE THE FUTURE" across the top, a crystal ball in the middle and "PEEK AT THE TOP THREE CARDS" at the bottom', 'a card with "SKIP" across the top, a running cartoon goat in the middle and "END YOUR TURN NOW" at the bottom', 'a card with "ATTACK" across the top, a pointing hand in the middle and "NEXT PLAYER TAKES TWO TURNS" at the bottom',
           'a card with "SHUFFLE" across the top, a mixing bowl of cards in the middle and "MIX THE DRAW PILE" at the bottom', 'a card with "NOPE" across the top, a raised palm in the middle and "STOP ANY ACTION" at the bottom', 'a card with "FAVOUR" across the top, a pickpocket in the middle and "TAKE A CARD FROM ANY PLAYER" at the bottom']
    return out
def creature():
    mons = [('a small orange fire lizard with a flaming tail', 'EMBERLING', 60, 'FLAME TAIL', 30), ('a round blue water frog with big eyes', 'BUBBLOP', 50, 'WATER JET', 20), ('a leafy green turtle with a tree on its shell', 'MOSSHELL', 80, 'VINE WHIP', 40),
            ('a yellow electric mouse-like creature', 'ZAPLET', 40, 'SPARK', 20), ('a purple ghost with a long grin', 'SPOOKLE', 70, 'SHADOW BITE', 50), ('a rocky grey armadillo', 'GRAVLOK', 90, 'ROCK ROLL', 40)]
    return ['a creature battle card with a yellow border, the creature name "%s" at the top left, "HP %d" at the top right, a picture of %s in a framed window, and below it an attack line reading "%s %d" with "WEAKNESS WATER" in small letters along the bottom edge' % (n, hp, p, a, dmg) for p, n, hp, a, dmg in mons] + \
           ['an energy card with "FIRE ENERGY" across the top and a large glowing flame symbol in the middle', 'an energy card with "WATER ENERGY" across the top and a large glowing water drop symbol', 'an energy card with "LEAF ENERGY" across the top and a large glowing leaf symbol']
def spell():
    cards = [('a knight in silver armour raising a sword', 'SILVER PALADIN', '3', 'CREATURE', '3/3', 'GUARDS ALL ALLIES'), ('a dragon breathing fire over a city', 'CINDER WYRM', '6', 'CREATURE', '6/5', 'FLYING'),
             ('a bolt of lightning striking a tower', 'STORM BOLT', '1', 'SPELL', '', 'DEAL 3 DAMAGE TO ANY TARGET'), ('a misty forest clearing', 'FOREST', '', 'LAND', '', 'ADD ONE GREEN ENERGY'), ('a dark wizard reading a glowing book', 'GRIM SCHOLAR', '2', 'CREATURE', '1/2', 'DRAW A CARD'),
             ('a shining sword floating in light', 'BLADE OF DAWN', '2', 'ITEM', '', 'EQUIPPED CREATURE GETS +2/+0')]
    out = []
    for p, n, cost, t, pw, rule in cards:
        line = 'a fantasy battle card with a dark frame, the card name "%s" across the top' % n
        if cost: line += ' with a small round cost circle reading "%s" in the corner' % cost
        line += ', a painted picture of %s, the type line "%s" across the middle and a pale text box below reading "%s"' % (p, t, rule)
        if pw: line += ' with "%s" in the bottom corner' % pw
        out.append(line)
    return out
def hanafuda():
    months = [('pine trees and a crane', 'January'), ('plum blossom and a bush warbler', 'February'), ('cherry blossom and a curtain', 'March'), ('wisteria and a cuckoo', 'April'), ('irises and a bridge', 'May'), ('peonies and butterflies', 'June'),
              ('bush clover and a boar', 'July'), ('pampas grass and a full moon', 'August'), ('chrysanthemums and a sake cup', 'September'), ('maple leaves and a deer', 'October'), ('willow, a frog and a man with an umbrella', 'November'), ('paulownia and a phoenix', 'December')]
    # month names are left out of the wording: naming them made the model letter the cards
    return ['a small stiff flower card, narrow and about half the size of a playing card, painted in a flat traditional Japanese style with %s in bold red, black and gold on a plain cream ground inside a thin black edge' % m[0] for m in months] + \
           ['a small stiff flower card painted in a flat traditional Japanese style with %s and a plain red ribbon banner across it, inside a thin black edge' % m[0] for m in months[:3]]
def letters():
    L = [('A', 2), ('E', 2), ('S', 3), ('R', 4), ('T', 4), ('K', 8), ('Q', 15), ('Z', 14), ('M', 6), ('O', 2)]
    return ['a word-building letter card with a big capital "%s" in the centre and a small "%d" points number in the corner' % l for l in L] + ['a wild letter card with a star and the word "ANY"']
def symbols():
    sets = ['a sun, a padlock, a carrot, a ladybird, a snowman, a key, an anchor and a cheese', 'a dog, a lightning bolt, a key, a heart, a cactus, a pencil, an igloo and a bomb', 'a clock, a tree, a carrot, a ghost, a spider, a dolphin, a lips shape and a question mark',
            'a moon, a dinosaur, a key, a candle, an eye, a bottle, a snowflake and a hammer']
    return ['a round card printed with eight small symbols of different sizes scattered across it, %s' % s for s in sets]
def trivia():
    cats = [('blue', 'GEOGRAPHY'), ('pink', 'ENTERTAINMENT'), ('yellow', 'HISTORY'), ('brown', 'ARTS'), ('green', 'SCIENCE'), ('orange', 'SPORT')]
    return ['a question card with six coloured bands down one side, the %s band labelled "%s" with the question "%s"' % (c, n, q) for (c, n), q in zip(cats, ('WHICH RIVER FLOWS THROUGH THE CAPITAL?', 'WHO SANG THE SUMMER HIT?', 'IN WHAT YEAR DID THE BRIDGE OPEN?', 'WHO PAINTED THE BLUE HORSES?', 'WHAT GAS DO PLANTS BREATHE IN?', 'HOW MANY PLAYERS ARE IN A TEAM?'))]

GAMES2 = {
 'old_maid': ('an old maid card game of matching pairs of funny characters, in which the player left holding the one odd card loses', old_maid(), 'pairs laid down face up in front of each player and one player holding out a fan of cards for another to pick from'),
 'pit': ('a noisy trading card game in which players swap cards of farm goods to collect a full set of one kind, with special bull and bear cards', pit(), 'players holding cards out to swap, a brass bell in the middle of the table and scattered goods cards'),
 'sequence': ('a numbered patience race game in which players build piles in order from 1 to 15 from their own stock pile', flinch(), 'several shared build piles running up in order in the middle of the table and each player\'s face-down stock pile beside them'),
 'phase': ('a rummy-style card game of coloured numbers 1 to 12 in which players complete a series of set and run goals', phase(), 'runs and sets laid face up in front of each player and a discard pile in the middle'),
 'bomb': ('a party card game in which players draw cards and try to avoid the bomb card, using defuse and action cards to stay in', bomb(), 'a draw pile in the middle, a bomb card just turned over and a player reaching for a defuse card'),
 'creature': ('a collectible creature battle card game in which cute monsters with hit points and attacks battle each other using energy cards', creature(), 'two players facing each other with creature cards laid out in front of them, energy cards attached and small damage counters on the cards'),
 'spell': ('a collectible fantasy battle card game of creatures, spells and lands, each card with a cost, a painting and a short line of rules text', spell(), 'a row of land cards turned sideways, creature cards in play facing the opponent and a life counter die beside each player'),
 'hanafuda': ('a set of 48 small stiff Japanese flower cards with plain black backs, four for each month of the year, painted with seasonal plants and animals', hanafuda(), 'cards laid in a grid on a low table, players holding small hands and a pile of captured cards beside each'),
 'letters': ('a word-building card game in which players make words from letter cards, each letter worth points', letters(), 'words spelled out in rows of letter cards in front of each player and a score pad with tallies'),
 'symbols': ('a quick-spotting card game of round cards, each with eight symbols, where any two cards share exactly one symbol', symbols(), 'two round cards side by side with a hand pointing at the one matching symbol, and a pile of won cards'),
 'trivia_cards': ('a trivia quiz card game of question cards in six coloured subject categories', trivia(), 'a box of question cards, one card held up to be read, and a score pad'),
}
PARTS2 = {
 'old_maid': ['a small folded leaflet with the old maid card and "HOW TO PLAY" on the cover'], 'pit': ['a small brass hand bell', 'a score pad headed "SCORE"'],
 'sequence': ['a card reading "BUILD FROM 1 TO 15" across the top'], 'phase': ['a score pad headed "PHASE" with numbered rows', 'a small card reading "PHASE 1 TWO SETS OF THREE" on the first line and "PHASE 2 ONE SET OF THREE AND ONE RUN OF FOUR" on the second line'],
 'bomb': ['a folded leaflet with a cartoon bomb and "HOW TO PLAY" on the cover'], 'creature': ['small round red damage counters', 'a coin for deciding who goes first', 'a folded paper play mat'],
 'spell': ['a pair of twenty-sided dice used as life counters', 'a deck box of hard plastic', 'a play mat of rubber-backed cloth'],
 'hanafuda': ['a small paper box with a printed lid', 'a cushion mat for playing on'], 'letters': ['a score pad headed "WORDS" with columns of names', 'a sand timer'],
 'symbols': ['a round tin with a printed lid'], 'trivia_cards': ['a sand timer', 'a score pad headed "QUIZ"'],
}
