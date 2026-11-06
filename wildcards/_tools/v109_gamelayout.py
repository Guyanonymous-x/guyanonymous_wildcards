"""v109 - top-down views of every card game and board game (user 2026-11-06), in two forms:
1. a natural-language prompt looking straight down at the table;
2. a layout JSON prompt (pre-filled by export(), kept out of the wildcard files because wildcard tools read {...} as a choice block) in the format the Moss Image training used (docs/MOSS_IMAGE_NOTES.txt): {"summary": {"meta", "canvas", "caption"},
   "items": [{"label", "caption", "text", "bbox"}], "bbox_coord_space": "abs_centralized", "bbox_format": "yxyx"}, boxes on a 1024 canvas
   with the centre at 0,0 (y1, x1, y2, x2). Each box carries one part of the game: the board or layout, each player's place, the piles,
   the parts and the box lid with its title in the text field.
Inside the JSON, quoted card text uses single quotes (copies of the pools with the suffix _jq) so the JSON stays valid after expansion.
The paper's prompt-strategy test scored layout JSON best for designed layouts; our own test found boxes ignored for whole-body groups,
so these are offered for flat table layouts, where boxes are simplest.

Files: cg_<game>_topdown_prompt, bg_<game>_topdown_prompt, cg_topdown_any_prompt, bg_topdown_any_prompt, and *_jq copies of pools used inside the JSON.
Export: docs/layout_json/Guyanonymous_Wildcards_games_topdown_layout_json.txt (one layout JSON prompt per line)."""
import json, re
LAYOUT = {}
from v109_cardgames import GAMES as CG
from v109_boardgames2 import GAMES as BG2
THEMES = ['city', 'seaside', 'space', 'medieval', 'western', 'underwater', 'fantasy']
STAGES = ('partial', 'setup', 'end')
def box(x1, y1, x2, y2): return [y1, x1, y2, x2]
def layout(caption, items):
    d = {'summary': {'meta': ['photo'], 'canvas': 'single', 'caption': caption}, 'items': items, 'bbox_coord_space': 'abs_centralized', 'bbox_format': 'yxyx'}
    return json.dumps(d, ensure_ascii=False, separators=(',', ':'))
def build(G, final=None):
    def jq(name):
        if name + '_jq' not in G: G[name + '_jq'] = [l.replace('"', "'") for l in G[name]]
        return '__%s_jq__' % name
    cg_p, cg_l, bg_p, bg_l = [], [], [], []
    for k in CG:
        b = 'cg_%s' % k
        G[b + '_topdown_prompt'] = ['A flat top-down view looking straight down at __%s_desc__ laid out on __cg_table__, %s The cards in the middle include __%s_card__ face up. Each player\'s place sits at one edge of the table, and __%s_parts__ lies in one corner. The cards are __cg_decade_look__. __cg_condition__ Overhead photograph taken from directly above, the whole table in sharp focus.'
                                   % (b, '__%s_stage_%s__.' % (b, st), b, b) for st in STAGES]
        lays = []
        for st in STAGES:
            items = [
             {'label': 'object', 'caption': 'The centre of the table, %s. The card showing face up is %s.' % (jq('%s_stage_%s' % (b, st)), jq(b + '_card')), 'bbox': box(-200, -170, 200, 170)},
             {'label': 'object', 'caption': 'The nearest player\'s place at the bottom edge, a hand of cards fanned face up, %s.' % jq(b + '_card'), 'bbox': box(-300, 320, 300, 500)},
             {'label': 'object', 'caption': 'The far player\'s place at the top edge, a hand of cards held face down.', 'bbox': box(-260, -500, 260, -330)},
             {'label': 'object', 'caption': 'The left player\'s place, a small hand of cards face down.', 'bbox': box(-500, -230, -330, 230)},
             {'label': 'object', 'caption': 'The right player\'s place, a small hand of cards face down.', 'bbox': box(330, -230, 500, 230)},
             {'label': 'object', 'caption': jq(b + '_parts'), 'bbox': box(330, 330, 500, 500)},
             {'label': 'object', 'caption': 'The open card box lying on its side.', 'bbox': box(-500, -500, -330, -330)},
             {'label': 'text', 'caption': 'The title printed on the card box lid in bold letters.', 'text': '__cg_title__', 'bbox': box(-495, -450, -335, -380)},
            ]
            lays.append(layout('A flat top-down photograph looking straight down at %s on %s, every card and part laid out clearly. The cards are %s.' % (jq(b + '_desc'), '__cg_table__', '__cg_decade_look__'), items))
        LAYOUT[b] = lays
        cg_p.append('__%s_topdown_prompt__' % b)
    boards = [('bg_%s' % k, '__bg_%s_desc__' % k, '__bg_%s_board__' % k, '__bg_%s_pieces__' % k, '__bg_%s_parts__' % k) for k in BG2]
    boards += [('bg_%s' % t, 'a property-trading board game set in __bg_%s_place__' % t, '__bg_%s_board__' % t, '__bg_token__, __bg_token__ and __bg_building__' , '__bg_dice__, __bg_money_stack__ and two decks of event cards') for t in THEMES]
    for b, desc, board, pieces, parts in boards:
        G[b + '_topdown_prompt'] = ['A flat top-down view looking straight down at %s on __bg_table__. The board is %s, with %s Around it lie %s and %s. Everything is __bg_decade_look__. Overhead photograph taken from directly above, the whole board inside the frame and in sharp focus.'
                                   % (desc, board, '__%s_stage_%s__.' % (b, st), pieces, parts) for st in STAGES]
        lays = []
        for st in STAGES:
            items = [
             {'label': 'object', 'caption': 'The game board seen flat from above, %s, with %s.' % (board, jq('%s_stage_%s' % (b, st))), 'bbox': box(-390, -390, 390, 390)},
             {'label': 'object', 'caption': 'Playing pieces waiting beside the board, %s.' % pieces, 'bbox': box(-500, 400, -150, 500)},
             {'label': 'object', 'caption': 'Game parts beside the board, %s.' % parts, 'bbox': box(150, 400, 500, 500)},
             {'label': 'object', 'caption': 'The box lid lying beside the board.', 'bbox': box(-500, -500, -150, -400)},
             {'label': 'text', 'caption': 'The game title printed across the box lid in big letters.', 'text': '__bg_title__' if b[3:] in THEMES else '__bg_title2__', 'bbox': box(-480, -490, -170, -420)},
            ]
            lays.append(layout('A flat top-down photograph looking straight down at %s on __bg_table__, the whole board and every piece laid out clearly. Everything is __bg_decade_look__.' % desc, items))
        LAYOUT[b] = lays
        bg_p.append('__%s_topdown_prompt__' % b)
    # board pools that carry quoted words go into the JSON through their _jq copies
    for b, desc, board, pieces, parts in boards:
        for i, l in enumerate(LAYOUT[b]):
            for name in [board, pieces, parts, desc]:
                for ref in __import__('re').findall(r'__([a-z0-9_]+)__', name):
                    if ref in G and any('"' in x for x in G[ref]):
                        l = l.replace('__%s__' % ref, jq(ref))
            LAYOUT[b][i] = l
    G['cg_topdown_any_prompt'] = cg_p; G['bg_topdown_any_prompt'] = bg_p
    return G
def export(final, out, per=2, seed=20261106):
    """Write pre-filled layout JSON prompts (one per line) for every game and stage: the templates are expanded here with the library's
    pools, so the braces of the JSON never pass through a wildcard expander."""
    import sys, random, os
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    import expand as X
    W = X.load([final]); R = random.Random(seed); lines = []
    for b, lays in LAYOUT.items():
        for t in lays:
            for _ in range(per):
                body = re.sub(r'__([a-z0-9_]+)__', lambda m: X.clean(X.expand(W, m.group(0), R)).replace('\\', '').replace('"', "'"), t)
                json.loads(body)
                lines.append(body)
    with open(out, 'w', encoding='utf8', newline='\n') as f: f.write('\n'.join(lines))
    return len(lines)
