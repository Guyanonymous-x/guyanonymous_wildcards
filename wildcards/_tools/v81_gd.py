"""v81 stage B - gadgets and tech devices (gd_). Phones, wearables, readers, tablets, handhelds, computers and peripherals.
Each kind has its own era, body, screen, controls, material, colour and feature lists; any text on a screen is written out line by line in quotes."""
import os, sys, re
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from famlib import P
from v81_gd_data1 import G1, G1b
from v81_gd_data2 import G2
KINDS = {}; KINDS.update(G1); KINDS.update(G1b); KINDS.update(G2)
CONTENT = {
 'watch': '''a watch face with the large time "10:09" and the date "Tue 14"; a watch face with the words "Steps 8,204" and a small ring graph; a watch face with the line "Heart rate 72" and a pulse wave; a watch face with the lines "Next meeting" and "3:30 PM"; a watch face with the word "Timer" and the digits "04:59"; a dark watch face with the line "Low battery" in small white letters; a watch face with the weather lines "18 degrees" and "Light rain"; a watch face with the lines "Run" and "5.2 km"''',
 'console': '''a screen with the title "Press Start" in blocky letters; a game screen with the lines "Score 004200" and "Lives 3"; a menu with the lines "New Game", "Continue" and "Options"; a screen with a small pixel hero and the words "Level 2"; a screen with the line "Game Over" over a dark background; a screen with the lines "Player One" and "Ready"; a puzzle screen with the word "Combo" and the number "x4"; a pixel map with the line "Enter the cave"''',
 'music': '''a screen with the lines "Now Playing" and "Track 07"; a list with the lines "Summer Road", "Blue Hour" and "Late Train"; a screen with the title "Slow River" and the time "2:41 / 4:05"; a screen with the word "Shuffle" and a small arrow; a screen with the line "Battery low"; a screen with the lines "Album: Open Fields" and "12 songs"; a screen with the word "Paused" and a row of bars; a tape label handwritten "Mix for the road"''',
 'camera': '''a rear screen showing a photograph of a harbour with the number "0142" in the corner; a rear screen with a menu listing "Flash", "Timer" and "Size"; a rear screen with the line "Memory full"; a rear screen showing a portrait with a small box round the face; a rear screen with the lines "ISO 400" and "f/2.8"; a rear screen with a grid of tiny thumbnails; a rear screen with the word "Recording" and a red dot; a top screen with the number "36" shots left''',
 'calc': '''a display reading "3.14159"; a display reading "1,024"; a display reading "0.5"; a display reading "42"; a display reading "99999999"; a display reading "12 x 12 = 144"; a display with the word "ERROR"; a display reading "7.25"''',
 'gps': '''a map with a route line and the text "Turn left in 200 m"; a map screen with the lines "Arrive 14:32" and "12 km"; a screen with the line "Recalculating" over a map; a screen with the words "Speed limit 50" in a red circle; a screen with a compass and the line "North 12 degrees"; a screen with the lines "Home" and "Work" as large buttons; a map with the street name "Mill Road" in bold; a screen with the line "Signal lost"''',
 'speaker': '''a small display with the time "07:30"; a small display with the word "Listening"; a small display with the number "21"; a small display with the word "Muted"; a small display with the time "22:45"; a small display with the word "Setup"''',
 'terminal': '''a green screen with the lines "LOAD GAME" and "READY."; an amber screen with the lines "LOGIN:" and "PASSWORD:"; a black screen with the line "C:\\> DIR" and a blinking cursor; a screen with the lines "10 PRINT HELLO" and "RUN"; a screen with the line "SYNTAX ERROR" in capitals; a screen with the lines "READY" and a block cursor; a screen with the lines "WELCOME OPERATOR" and "ENTER COMMAND"; a screen with a table of numbers and the heading "PAYROLL"''',
 'desktop': '''a screen showing a blue desktop with a window titled "Documents"; a screen showing a spreadsheet with the heading "Budget" over columns of numbers; a screen showing a word processor page with the title "Quarterly Report"; a screen showing a login box with the line "Welcome"; a screen showing a web page with the heading "Today"; a screen showing a game scene with the word "Paused"; a screen showing a folder window with the lines "Photos", "Music" and "Letters"; a dark screen with the line "Starting up" and a progress bar'''}
PLACES = {
 'home': "on a sofa arm beside a mug of tea; on a bedside table next to a lamp; on a kitchen counter near a window; on a living room shelf; on a rug on the floor; on a wooden coffee table; at a desk in a warm room; on a bookshelf among paperbacks",
 'desk': "on a tidy wooden desk with a notebook; on a cluttered desk with sticky notes; on a white desk beside a plant; on a glass desk in a bright office; on a cafe table next to a coffee; on a drawing table with pencils; on a workbench with tools; on a school desk",
 'street': "held in a hand on a city street; on a bench in a park; on a cafe table by a window; on a train seat; on a bus window ledge; on a market stall; on a stone wall in the sun; in a coat pocket on a rainy day",
 'retro': "on a wood-panelled desk in a 1980s bedroom; in a cluttered garage workshop; on a formica kitchen table; in a dim computer room with grey cabinets; on a plastic-topped school desk; in a beige office with fluorescent lights; on a glass counter in an old electronics shop; in a basement with posters on the wall",
 'travel': "on a hotel bed beside a suitcase; at an airport gate; on a car dashboard; on a train table; on a mountain rock with a view; at a station bench; beside a map on a table; on a boat seat",
 'tech': "on a lab bench with cables; in a server room with cold light; on a workbench full of components; in a repair shop under a lamp; on a shelf of old electronics; in a cluttered hobby room; under a magnifying lamp; on an anti-static mat",
 'outdoor': "on a muddy building site; on a rocky trail; on a campsite table; on a workman's belt; on a rough wooden plank; on a boat deck; on a snowy ledge; at a market in the rain"}
WEAR = P("brand new and unmarked; lightly scuffed from daily use; covered in fingerprints; scratched along the edges; yellowed with age; worn smooth on the buttons; dusty in the seams; a little dented at one corner; faded by the sun; cleaned and polished; stained with coffee rings; held together with a strip of tape")
LIGHT = P("soft window light; warm lamp light; bright studio light; low golden sunlight; cool blue evening light; harsh midday sun; neon light from the side; grey overcast light; dim light with a faint glow; early morning light")
SHOT = P("a close-up product shot; a three-quarter view from above; a front view filling the frame; a side view in profile; a macro shot of the buttons and keys; a wide shot with the device in its place; a low angle looking up; a flat lay from directly above; a view with a soft blurred background; a shot with the device held in a hand")
def pl(n):
    if n.startswith('pair of '): return 'pairs of ' + n[8:]
    if n.endswith('mouse'): return n[:-5] + 'mice'
    if n.endswith('s'): return n
    if n.endswith('y') and n[-2] not in 'aeiou': return n[:-1] + 'ies'
    if n.endswith(('ch', 'sh', 'x')): return n + 'es'
    return n + 's'
def an(n): return ('An ' if n[:1].lower() in 'aeiou' else 'A ') + n
def strip_lead(x): return re.sub(r'^a (small |rear |top )?(screen|display)( showing| with)? ', '', x)
COL = r'(?:white|black|yellow|grey|gray|red|orange|silver|cream|pink|olive|gunmetal|green|blue|beige|brown|purple|tan)'
COLRE = re.compile(r'\b' + COL + r'(?:(?:,| and) ' + COL + r')*\s+', re.I)
COLEND = re.compile(r'\b(?:in|of) ' + COL + r'(?:(?:,| and) ' + COL + r')*\s+(?=with\b|and\b|,|\.|;|$)', re.I)
def decol(items): return [re.sub(r'\ba (?=(?:[aeio]|und|upp|upo)\w*)', 'an ', COLRE.sub('', COLEND.sub('', x))) for x in items]
def keep_screen(k, items, has_content):
    out = []
    for x in P(items):
        if has_content:
            if re.match(r'(no |none|a tiny row|a tiny single|a very small row|a faint|tiny status|a ring of|a thin light|a single green|a single blue|a status light|a small LED)', x): continue
        else:
            m = re.match(r'no [\w\- ]+?, (?:only |just )?(.*)', x)
            if m: x = m.group(1)
            elif x.startswith('no '): continue
        out.append(x)
    return out
def build(final=None):
    G = {}; ep = []; kinds = []
    G['gd_wear'] = WEAR; G['gd_light'] = LIGHT; G['gd_shot'] = SHOT
    for g, v in PLACES.items(): G['gd_place_%s' % g] = P(v)
    for c, v in CONTENT.items(): G['gd_text_%s' % c] = [strip_lead(x) for x in P(v)]
    # reuse the v79 pools (phone_screen, phone_screen_old, phone_screen_future, ereader_screen) for the rest
    for k, (noun, pg, cont, era, body, screen, ctrl, mat, col, feat) in KINDS.items():
        has = bool(cont)
        G['gd_%s_era' % k] = P(era); G['gd_%s_body' % k] = decol(P(body)); G['gd_%s_screen' % k] = keep_screen(k, screen, has)
        G['gd_%s_controls' % k] = decol(P(ctrl)); G['gd_%s_material' % k] = decol(P(mat)); G['gd_%s_colour' % k] = P(col); G['gd_%s_feature' % k] = P(feat)
        REFMAP = {'phone': 'phone_screen', 'phone_old': 'phone_screen_old', 'phone_future': 'phone_screen_future', 'ereader': 'ereader_screen'}
        cref = ('__%s__' % REFMAP.get(cont, 'gd_text_%s' % cont)) if has else ''
        lead1 = 'Its display is' if has else 'Its lights and display are'
        lead2 = 'it has a display that is' if has else 'it shows lights and display details that are'
        G['gd_%s_look' % k] = [
          'Its body is __gd_%s_body__. %s __gd_%s_screen__%s. For controls it has __gd_%s_controls__. Its material is __gd_%s_material__. A notable detail is __gd_%s_feature__.' % (k, lead1, k, (', and it shows ' + cref) if has else '', k, k, k),
          'Built as __gd_%s_body__, %s __gd_%s_screen__%s. Its controls are __gd_%s_controls__, and its material is __gd_%s_material__. Look for __gd_%s_feature__.' % (k, lead2, k, (', showing ' + cref) if has else '', k, k, k)]
        G['gd_%s_prompt' % k] = [an(noun) + ', __gd_%s_era__. __gd_%s_look__ Its colours are __gd_%s_colour__. It looks __gd_wear__. It is __gd_place_%s__, in __gd_light__, and the image is __gd_shot__.' % (k, k, k, pg)]
        G['gd_%s_short' % k] = [an(noun) + ', __gd_%s_era__, with __gd_%s_body__, in __gd_%s_colour__.' % (k, k, k)]
        G['gd_%s_group_prompt' % k] = ['Three %s are shown together %s. The first is __gd_%s_body__, in __gd_%s_colour__. The second is __gd_%s_body__, in __gd_%s_colour__. The third is __gd_%s_body__, in __gd_%s_colour__. They look __gd_wear__, in __gd_light__.' % ((pl(noun), '__gd_place_%s__' % pg) + (k, k) * 3)]
        kinds.append(k); ep.append('gd_%s_prompt' % k)
    for s_ in ('prompt', 'group_prompt', 'short'): G['gd_' + s_] = ['__gd_%s_%s__' % (k, s_) for k in kinds]
    G['gd_types'] = [KINDS[k][0] for k in kinds]
    G['v81_gd_entry_points'] = ['gd_prompt', 'gd_group_prompt', 'gd_short'] + ep
    return G
if __name__ == '__main__':
    G = build(); print(len(G), len(KINDS))
    print(G['gd_watch_prompt'][0]); print(G['gd_watch_look'][0])
