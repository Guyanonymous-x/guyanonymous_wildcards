"""v109 - property-trading board game creator (user 2026-11-06): an unbranded game in which players roll two dice, move tokens round a
square board of 40 spaces, buy streets, collect rent and build small houses and hotels. Street names, town names and the game title come
from the name system and every word or number on the board, cards and money is quoted. Themes (city, seaside, space, medieval, wild west,
underwater, fantasy) and decade looks change the art. Boards, title deed cards, chance-style cards, play money, tokens, houses and hotels,
dice, the box and the whole game in play.

Files: bg_theme, bg_decade_<d>_look, bg_street, bg_group, bg_board, bg_deed, bg_chance_card, bg_money, bg_token, bg_building, bg_dice,
       bg_box, bg_box_condition, bg_condition, bg_board_prompt, bg_deed_prompt, bg_card_prompt, bg_money_prompt, bg_pieces_prompt,
       bg_box_prompt, bg_contents_prompt, bg_play_prompt, bg_any_prompt."""
DECADES = ['1930s', '1950s', '1970s', '1990s', '2020s']
LOOK = {
 '1930s': 'printed in muted reds, greens and creams on heavy linen-backed board with neat serif lettering and small engraved-style drawings',
 '1950s': 'printed in cheerful bright colours with rounded lettering and painted cartoon drawings',
 '1970s': 'printed in orange, brown and avocado tones with chunky rounded lettering and stylised drawings',
 '1990s': 'printed in glossy saturated colours with bold outlined lettering and cartoon art',
 '2020s': 'printed in clean flat colours with neat sans-serif lettering and simple graphic icons',
}
THEME = {
 'city': ('a busy city', ['Street', 'Avenue', 'Road', 'Square', 'Lane', 'Place'], ['a railway station', 'a bus depot', 'a tram stop', 'an airport'], ['a power station', 'a water works']),
 'seaside': ('a seaside resort', ['Promenade', 'Parade', 'Pier', 'Esplanade', 'Bay', 'Cove'], ['a ferry terminal', 'a harbour', 'a lifeboat station', 'a beach tram'], ['an ice cream factory', 'a lighthouse']),
 'space': ('a space colony', ['Crater', 'Dome', 'Orbit', 'Ring', 'Station', 'Ridge'], ['a launch pad', 'a moon shuttle', 'a teleporter', 'a star port'], ['an oxygen plant', 'a solar farm']),
 'medieval': ('a medieval kingdom', ['Keep', 'Market', 'Gate', 'Hall', 'Abbey', 'Mill'], ['a coaching inn', 'a river ferry', 'a stable yard', 'a drawbridge'], ['a windmill', 'a well']),
 'western': ('a wild west frontier town', ['Gulch', 'Ranch', 'Creek', 'Ridge', 'Trail', 'Canyon'], ['a stagecoach stop', 'a railroad depot', 'a river boat landing', 'a pony express post'], ['a gold mine', 'a water tower']),
 'underwater': ('an underwater city', ['Reef', 'Lagoon', 'Trench', 'Grotto', 'Current', 'Shoal'], ['a submarine dock', 'a whale taxi', 'a bubble lift', 'a current tunnel'], ['a pearl farm', 'a kelp mill']),
 'fantasy': ('a fantasy realm', ['Tower', 'Glade', 'Hollow', 'Spire', 'Grove', 'Vale'], ['a dragon roost', 'a griffin post', 'a portal stone', 'a flying ship dock'], ['a crystal mine', 'a wizard well']),
}
GROUPS = [('brown', 60, 2), ('pale blue', 100, 6), ('pink', 140, 10), ('orange', 180, 14), ('red', 220, 18), ('yellow', 260, 22), ('green', 300, 26), ('dark blue', 400, 50)]
CORNERS = ['"START" with a big arrow and "COLLECT 200 AS YOU PASS"', '"JAIL" with a barred window and "JUST VISITING" along the edge', '"FREE PARKING" with a little parked car', '"GO TO JAIL" with a pointing policeman']
TOKENS = ['a tiny silver racing car', 'a little silver dog', 'a small silver boot', 'a silver top hat', 'a silver sailing ship', 'a silver thimble', 'a small silver wheelbarrow', 'a silver iron',
          'a little silver cat', 'a silver rocket', 'a silver horse and rider', 'a silver teapot']
CHANCE = [('LUCKY BREAK', 'ADVANCE TO START'), ('LUCKY BREAK', 'BANK PAYS YOU 50'), ('LUCKY BREAK', 'GO BACK THREE SPACES'), ('LUCKY BREAK', 'GET OUT OF JAIL FREE'),
          ('TOWN CHEST', 'BIRTHDAY GIFT COLLECT 10'), ('TOWN CHEST', 'DOCTOR FEES PAY 50'), ('TOWN CHEST', 'YOU WIN SECOND PRIZE COLLECT 10'), ('TOWN CHEST', 'STREET REPAIRS PAY 40 PER HOUSE')]
MONEY = [('1', 'white'), ('5', 'pink'), ('10', 'yellow'), ('20', 'green'), ('50', 'blue'), ('100', 'beige'), ('500', 'orange')]
CONDITION = ['crisp and new, the board perfectly flat', 'well played, the board soft along the fold and the money crumpled', 'old and worn, the corners of the box split and the cards dog-eared', 'faded by sunlight, with a few pieces replaced by buttons', 'scuffed and well loved, with a tea stain on one corner of the board']
BOX_COND = ['crisp and new in its shrink-wrap', 'scuffed along the edges', 'with the lid corners split and taped', 'faded and dented', 'with a price sticker on the lid']
TABLE = ['a wooden kitchen table', 'a living room carpet', 'a dining table under a hanging lamp', 'a caravan table', 'a coffee table beside a sofa']
PHOTO = ['Natural light photograph from above with true colours, every word readable.', 'Warm photograph at table height with a shallow depth of field.', 'Overhead photograph of the whole layout in sharp focus.']
TITLE = ['__name_town__ Tycoon', 'Property Empire', '__name_town__ Estates', 'Landlord of __name_town__', 'Rent Day', 'Big Deal']

def build(final=None):
    G = {}
    for d in DECADES: G['bg_decade_%s_look' % d] = [LOOK[d]]
    G['bg_decade_look'] = ['__bg_decade_%s_look__' % d for d in DECADES]
    G['bg_title'] = TITLE; G['bg_condition'] = CONDITION; G['bg_box_condition'] = BOX_COND; G['bg_table'] = TABLE; G['bg_photo'] = PHOTO
    G['bg_token'] = TOKENS; G['bg_corner'] = CORNERS
    G['bg_dice'] = ['a pair of white dice with black pips', 'a pair of red see-through dice with white pips', 'a pair of wooden dice with burnt-in dots']
    G['bg_building'] = ['small green plastic houses and red plastic hotels', 'little wooden houses painted green and long red wooden hotels', 'tiny green houses and red hotels in bright plastic']
    G['bg_money'] = ['a play money note of %s paper printed with "%s" in each corner and in big numbers in the middle' % (c, v) for v, c in MONEY]
    G['bg_money_stack'] = ['neat stacks of play money in white, pink, yellow, green, blue, beige and orange notes, each printed with its value, "1", "5", "10", "20", "50", "100" and "500"']
    G['bg_chance_card'] = ['a %s card from the deck marked "%s", reading "%s" in bold letters' % (c, h, t) for h, t in CHANCE for c in ('orange', 'yellow')]
    themes = []
    for t, (place, suffixes, transport, utilities) in THEME.items():
        b = 'bg_%s' % t
        G[b + '_place'] = [place]
        G[b + '_street'] = ['__name_town__ %s' % s for s in suffixes]
        G[b + '_transport'] = transport; G[b + '_utility'] = utilities
        G[b + '_deed'] = ['a title deed card with %s colour band across the top holding the street name "__%s_street__", and below it "PRICE %d" on the first line, "RENT %d" on the second line and "WITH HOTEL %d" on the third line' % (('an ' if g[0] in 'aeiou' else 'a ') + g, b, price, rent, rent * 50) for g, price, rent in GROUPS]
        G[b + '_board'] = ['a square game board for a game set in %s, with 40 spaces running round the edge. The four corner squares read %s, %s, %s and %s. Streets in coloured groups run along each side, each printed with its name, such as "__%s_street__" and "__%s_street__". Four squares show %s, two squares show %s, and the centre holds the title "__bg_title__" in big letters'
                           % (place, CORNERS[0], CORNERS[1], CORNERS[2], CORNERS[3], b, b, ', '.join(transport), ' and '.join(utilities))]
        G[b + '_board_prompt'] = ['A complete board for a property-trading board game, laid flat on __bg_table__ and photographed from directly above. It is __%s_board__, __bg_decade_look__. The board is __bg_condition__. __bg_photo__' % b]
        G[b + '_deed_prompt'] = ['A fan of property title deed cards from a property-trading board game set in %s, lying on __bg_table__. The front card is __%s_deed__, and behind it is __%s_deed__. The cards are __bg_decade_look__. __bg_photo__' % (place, b, b)]
        G[b + '_box_prompt'] = ['The box for a property-trading board game set in %s, a wide flat cardboard box with a lift-off lid printed with the title "__bg_title__" in big letters above a picture of streets, houses and %s. The lid is __bg_decade_look__. The box is __bg_box_condition__. __bg_photo__' % (place, transport[0]),
                                'The open box of a property-trading board game set in %s, the lid printed "__bg_title__" leaning beside it, the plastic tray inside holding stacks of play money, two decks of cards, __bg_building__, __bg_dice__, the tokens and the folded board. __bg_photo__' % place]
        G[b + '_play_prompt'] = ['A family game of a property-trading board game in progress on __bg_table__. The board is __%s_board__, __bg_decade_look__. On the board stand __bg_token__ and __bg_token__, with __bg_building__ built on the streets. Beside the board are __bg_dice__, __bg_money_stack__ and a pile of title deed cards, the top one __%s_deed__. __bg_photo__' % (b, b)]
        G[b + '_prompt'] = ['__%s_board_prompt__' % b, '__%s_deed_prompt__' % b, '__%s_box_prompt__' % b, '__%s_play_prompt__' % b, '__%s_play_prompt__' % b]
        themes.append('__%s_prompt__' % b)
    G['bg_card_prompt'] = ['A small stack of cards from a property-trading board game, the top one __bg_chance_card__, lying beside the board on __bg_table__. The cards are __bg_decade_look__. __bg_photo__']
    G['bg_money_prompt'] = ['A fanned handful of play money from a property-trading board game on __bg_table__, the front note __bg_money__ and behind it __bg_money__. __bg_photo__']
    G['bg_pieces_prompt'] = ['The playing pieces of a property-trading board game laid out on __bg_table__, with __bg_token__, __bg_token__, __bg_token__ and __bg_token__, __bg_building__ and __bg_dice__. Close-up photograph in sharp focus.']
    G['bg_contents_prompt'] = ['Everything from a property-trading board game laid out neatly on __bg_table__, photographed from above, with the folded board, stacks of play money, title deed cards, two decks of cards marked "LUCKY BREAK" and "TOWN CHEST", __bg_building__, __bg_dice__ and the metal tokens, beside the box lid printed "__bg_title__". __bg_photo__']
    G['bg_theme_prompt'] = themes
    G['bg_any_prompt'] = themes * 2 + ['__bg_card_prompt__', '__bg_money_prompt__', '__bg_pieces_prompt__', '__bg_contents_prompt__']
    return G
