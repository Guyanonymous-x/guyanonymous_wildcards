"""v109 - game stages (user 2026-11-06): every card game and board game can be shown partly set up or partly dealt, fully set up or dealt,
in the middle of play, and finished. Board games have stage lines written for each game; card games use stage lines that follow how
cards are dealt and played, with each game's own cards and parts. Added on top of v109_cardgames, v109_boardgame and v109_boardgames2.

Files: cg_<game>_stage_<partial|setup|mid|end>, cg_<game>_stage_prompt, bg_<game>_stage_<...>, bg_<game>_stage_prompt,
       cg_stage_any_prompt, bg_stage_any_prompt."""
from v109_cardgames import GAMES as CG
from v109_boardgames2 import GAMES as BG2

CARD = {
 'partial': ['a dealer halfway through dealing, cards flying out one at a time into small face-down piles in front of each place, the rest of the deck still in one hand',
             'the deck just shuffled and cut into two halves on the table, a few cards already dealt to each player',
             'cards being dealt round the table, some players already picking up their first cards while others wait'],
 'setup': ['every player\'s hand dealt and picked up, fanned and hidden, with the draw pile squared up in the middle and the top card turned face up beside it',
           'all the cards dealt into neat face-down piles in front of each player, the box and a folded leaflet with "HOW TO PLAY" on the cover set to one side',
           'a fresh game ready to start, the hands dealt, the score pad open with "SCORE" written across the top'],
 'end': ['the game just finished, one player laying down a winning hand with a grin while the others throw in their cards',
         'the cards gathered back into a messy pile, the score pad covered in tallies with a total circled at the bottom',
         'the last trick or the last card just played, the winner\'s pile of cards much taller than the rest',
         'the cards being squared up and slid back into the box at the end of the evening'],
}
BOARD = {
 'property': (['the board unfolded and the banker counting out play money into each player\'s starting pile, tokens still in the box', 'title deed cards being sorted by colour into the tray beside the board'],
              ['every token standing on the start square, each player with a neat fan of starting money, the two decks of cards face down on their squares in the middle and the houses and hotels piled beside the bank'],
              ['the game over, one player sitting behind tall piles of money and a fan of title deeds, other players\' empty spaces around the board and hotels crowding one side of the board', 'the board half packed away, money being sorted back into the tray']),
 'chess': (['pieces being set up on the board, the back rows half filled and pawns standing in a loose cluster at the side'], ['all thirty-two pieces in their starting places, two rows of pale pieces on one side and two rows of black pieces on the other, pawns in a straight line in front of the kings and queens'],
           ['the final position, a king toppled on its side in checkmate surrounded by the winning pieces, captured pieces lined up beside the board', 'the two players shaking hands across the board after a draw']),
 'draughts': (['counters being placed on the dark squares, one side complete and the other half done'], ['twelve counters of each colour on the dark squares of the three rows nearest each player, the middle two rows empty'],
              ['the finished game, only a few crowned kings left on one side and a pile of captured counters beside the board']),
 'backgammon': (['counters being stacked onto their starting points, the dice cups still empty'], ['the counters in their starting stacks of two, five, three and five on each side, the dice and doubling cube on the bar'],
                ['the game over, one player\'s counters all borne off and stacked in the tray at the side of the board, the doubling cube turned to "4"']),
 'snakes': (['the board being unfolded and the counters tipped out of the box'], ['all the counters lined up beside the square numbered "1", the die ready on the table'],
            ['one counter standing on the square numbered "100" at the top of the board, the other counters scattered lower down']),
 'ludo': (['counters being sorted into their coloured home corners'], ['four counters of each colour sitting in their home corners, the die and shaker cup in the middle'],
          ['all four counters of one colour home in the centre triangle, the other colours still strung around the cross']),
 'word_tiles': (['tiles being tipped into the cloth bag and players drawing their first seven'], ['the empty grid board with four racks of seven tiles each, the bag of tiles to one side and a blank score pad'],
                ['the finished board crowded with interlocking words, the bag empty, the score pad with columns added up and one total circled']),
 'mystery': (['the cards being sorted into suspects, weapons and rooms, three slipped secretly into the black envelope'], ['all six suspect pawns on their coloured starting squares round the edge of the house, the weapons placed one in each of six rooms and the remaining cards dealt out'],
             ['the black envelope opened and its three cards laid face up for everyone to see, the detective notes covered in ticks and crosses']),
 'conquest': (['players taking turns to place their first armies on territories, the map patchy with colours'], ['every territory claimed with one or more armies in six colours, the territory cards stacked face down beside the board'],
              ['one colour covering the whole map, the losing players\' armies back in their boxes']),
 'trivia_wheel': (['question cards being loaded into their holders, the playing pieces empty'], ['every playing piece on the hexagon hub in the centre, wedges in a dish and question boxes ready'],
                  ['one playing piece full with all six coloured wedges back on the hub, the winner holding up the final card']),
 'life_path': (['the buildings being clipped onto the board, cars waiting at the start with single drivers'], ['all the cars at the start of the road with one peg driver each, money and cards in the bank tray'],
               ['every car at the retirement end of the road, players counting their money, the cars crowded with peg families']),
 'battleship': (['players secretly placing their ships on the lower grids behind the raised lids'], ['both fleets hidden on the lower grids, the upper grids empty and the pegs in their trays'],
                ['one fleet sunk, every ship covered in red pegs and the upper grid of the winner scattered with white and red pegs']),
 'four_row': (['the frame standing empty, the discs being sorted into red and yellow piles'], ['the empty frame on its stand with twenty-one red and twenty-one yellow discs beside it'],
              ['a line of four yellow discs across the frame, the slider about to drop all the discs out']),
 'mancala': (['stones being counted into the cups, four in each'], ['four stones in each of the twelve cups and the two end stores empty'],
             ['the board almost empty, one store piled high and the other with only a few stones']),
 'go': (['the bowls being opened and the board wiped'], ['the empty grid board with the two bowls of black and white stones beside it'],
        ['the finished board covered in black and white groups, captured stones placed back on the board to count territory']),
 'star_checkers': (['marbles being sorted into the points of the star'], ['ten marbles of one colour filling each player\'s point of the star, the middle empty'],
                   ['one colour\'s marbles all moved into the opposite point of the star']),
 'hex_settle': (['the hexagon tiles being laid out to build the island and the number tokens placed on them'], ['the finished island in its sea frame, each player with two little houses and two roads placed and the robber on the desert'],
                ['the game over, one player\'s pieces spread over the island with cities and a long road, the score marked "10" on the track']),
 'train_routes': (['players choosing their first destination tickets, the train cards being shuffled'], ['the empty map board with each player\'s pile of plastic trains, five face-up train cards in a row and the decks beside it'],
                  ['routes across the map lined with trains of every colour, players adding up destination tickets on the score track']),
 'mahjong': (['the tiles being shuffled face down on the table with a clattering noise'], ['a square wall of face-down tiles stacked two high in the middle of the table, four racks waiting'],
             ['a winning hand of tiles laid face up in front of one player, the others revealing their tiles and scoring sticks changing hands']),
 'guess_face': (['the face windows being flipped up, the picture cards shuffled'], ['both trays with every face flipped up and each player holding one secret picture card'],
                ['one tray with only a single face left standing and the player revealing the matching card']),
}
BOARD.update({
 'dominoes': (['the dominoes being shuffled face down on the table with a clatter'], ['each player with seven dominoes stood on edge in front of them and the rest face down in a heap'], ['the line of dominoes finished, one player with no tiles left and the others counting their spots']),
 'number_tiles': (['tiles being drawn from the bag onto racks'], ['every rack holding fourteen tiles and the bag of the rest in the middle'], ['the table covered in runs and sets, one player\'s rack empty']),
 'dice_poker': (['the score pad being handed round, "SCORE" printed at the top'], ['the five dice in the cup and an empty score sheet ready'], ['the score sheet filled in with totals added at the bottom and one total circled']),
 'letter_cubes': (['the cubes being dropped into the tray'], ['the lid on, the tray ready to shake and the pads and pencils in front of each player'], ['word lists being compared, crossed out where players found the same words']),
 'code_pegs': (['one player hiding the code behind the shield'], ['the hidden code in place behind the shield and the rows of guess holes empty'], ['the shield lifted to show the hidden row matching the last guess']),
 'reversi': (['the four starting discs being placed in the middle'], ['two black and two white discs in a cross in the four middle squares and the rest in the tray'], ['the board full of discs, black clearly covering most of it']),
 'cribbage': (['the cards being shuffled and cut, the pegs at the start of the board'], ['six cards dealt to each player and the pegs at the start'], ['one peg in the final hole at the end of the track']),
 'jigsaw': (['the pieces tipped out of the box and being turned face up'], ['all the pieces face up and the edge pieces sorted into one pile'], ['the finished picture with every piece in place, the empty box beside it']),
 'bingo': (['cards and dabbers being handed out'], ['every player with a clean bingo card and a pile of counters, the cage full of balls'], ['one card with a full line of counters and the drawn balls lined up on the board']),
 'stack_tower': (['the blocks being stacked in the sleeve, three to a layer'], ['the tall neat tower standing straight on the table'], ['the tower fallen in a heap of blocks across the table']),
 'surgery': (['the ailment pieces being placed into their holes'], ['every piece in its hole and the tweezers ready'], ['every hole empty and the pieces lined up beside the patient']),
 'marble_drop': (['the straws being pushed through the tube one by one'], ['the tube full of crossing straws with all the marbles resting on top'], ['most of the marbles fallen into the tray and only a few straws left']),
 'drawing_guess': (['teams being chosen and pieces set at the start'], ['all pieces at the start of the track, the word cards and pad ready'], ['one team\'s piece on the final square and the pad full of funny drawings']),
 'floor_spots': (['the mat being unrolled on the floor'], ['the clean mat laid flat with the spinner beside it'], ['the players collapsed laughing on the mat']),
 'hippos': (['marbles being poured into the arena'], ['all the marbles in the middle of the arena and the hippos waiting'], ['the arena empty and each player\'s pile of marbles counted']),
 'flick_disc': (['discs being placed round the edge of the board'], ['the discs in their starting places round the rim'], ['most discs knocked off the board and one sitting in the centre hole']),
})
def build(final=None):
    G = {}
    for k in CG:
        b = 'cg_%s' % k
        for st, lines in CARD.items(): G['%s_stage_%s' % (b, st)] = lines
        G[b + '_stage_mid'] = ['__%s_play_prompt__' % b]
        G[b + '_stage_prompt'] = [('A tabletop scene of __%s_desc__ on __cg_table__, %s Next to the cards you can see __%s_parts__. The top card on show is __%s_card__. The cards are __cg_decade_look__. __cg_condition__ __cg_photo__' % (b, '__%s_stage_%s__.' % (b, st), b, b)) for st in ('partial', 'setup', 'end')] + ['__%s_play_prompt__' % b]
    G['cg_stage_any_prompt'] = ['__cg_%s_stage_prompt__' % k for k in CG]
    themes = ['city', 'seaside', 'space', 'medieval', 'western', 'underwater', 'fantasy']
    for k, (partial, setup, end) in BOARD.items():
        if k == 'property':
            for t in themes:
                b = 'bg_%s' % t
                for st, lines in (('partial', partial), ('setup', setup), ('end', end)): G['%s_stage_%s' % (b, st)] = lines
                G[b + '_stage_prompt'] = ['A property-trading board game set in __%s_place__ on __bg_table__, the board __%s_board__, %s with __bg_building__ and __bg_dice__ to hand. Everything is __bg_decade_look__ and __bg_condition__. __bg_photo__' % (b, b, '__%s_stage_%s__.' % (b, st)) for st in ('partial', 'setup', 'end')] + ['__%s_play_prompt__' % b]
            continue
        b = 'bg_%s' % k
        for st, lines in (('partial', partial), ('setup', setup), ('end', end)): G['%s_stage_%s' % (b, st)] = lines
        G[b + '_stage_prompt'] = ['A tabletop scene of __%s_desc__ on __bg_table__, with %s Next to the board you can see __%s_parts__. Everything is __bg_decade_look__. It is __bg_condition__. __bg_photo__' % (b, '__%s_stage_%s__.' % (b, st), b) for st in ('partial', 'setup', 'end')] + ['__%s_play_prompt__' % b]
    missing = set(BG2) - set(BOARD)
    if missing: raise KeyError('v109_gamestages: no stages for %s' % sorted(missing))
    G['bg_stage_any_prompt'] = ['__bg_%s_stage_prompt__' % k for k in BG2] + ['__bg_%s_stage_prompt__' % t for t in themes]
    return G
