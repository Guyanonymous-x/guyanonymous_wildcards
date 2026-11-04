"""v76 stage B - e-reader and mobile phone timelines. Brand-free descriptions in ereader_ and phone_ files; real device names only in maker_ereader_* and maker_phone_* files."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from famlib import P, slug
# key|label|years|look
EREADERS = """handheld_ebook_1990s|late-1990s handheld electronic book|1998-2001|a chunky grey handheld with a small backlit monochrome LCD, a thick bezel, a stylus and a row of page buttons down the side
first_ink_reader|first e-ink reader|2004-2006|a slim grey reader with a pale e-ink screen, a wide bezel and a cluster of buttons beside the screen
wedge_keyboard_reader|wedge-shaped keyboard reader|2007-2008|a large white wedge-shaped reader with a six-inch grey screen, a thick bezel, a narrow strip of keys under the screen and a scroll wheel
slim_keyboard_reader|slimmer keyboard reader|2009-2010|a slimmer white reader with a full row of small keyboard keys, a five-way pad and a sharper grey screen
large_format_reader|large-format reader|2009|a tall slim reader with a nearly ten-inch screen for newspapers and documents, silver edges and a small keypad
basic_button_reader|basic button reader|2011|a small light plastic reader with a five-way pad and page buttons, a grey screen and no keyboard
touch_reader_ir|early touch reader|2011|a small bezel-framed reader with a touch screen, no buttons except a single power slider and a visible infrared border
front_lit_reader|front-lit reader|2012-2013|a slim reader with a crisp screen lit from the edge, a soft rubber back, a thin bezel and a small logo-free power button
flat_glass_reader|flat-glass premium reader|2014-2015|a thin reader with a flat glass front with no recess, a magnesium shell and pressure-sensing page-turn zones in the bezel
stepped_back_reader|stepped-back reader|2016-2017|a very thin asymmetric reader with a thick edge on one side that fits the hand and physical page-turn buttons, a leather cover and a metal back
waterproof_large_reader|waterproof seven-inch reader|2017-2018|a larger sealed reader with a seven-inch screen, an auto-rotating display and a smooth aluminium back
flush_front_reader|flush-front reader|2018-2020|a thin flush-fronted reader with a soft matte back, a flat screen edge-to-edge and a slim rubber frame
warm_light_reader|warm-light reader|2021-2023|a larger six-inch reader with thin bezels, a smooth rubber back, adjustable warm lighting and a dark-mode page
stylus_note_reader|stylus note-taking reader|2022-2024|a big ten-inch paper-textured e-ink tablet with a wide left edge, a magnetic pen on the side and handwritten notes on the page
colour_ink_reader|colour e-ink reader|2024-2025|a seven-inch reader with a softly saturated colour page, a matte back and thin bezels
android_ink_tablet|e-ink tablet|2020-2025|a slim e-ink tablet with a pen, a thin metal frame and a note app showing a drawn diagram
foldable_ink_book|foldable e-ink book|2026|a book-like device with two e-ink pages joined by a hinge, a leather spine and a page-turn crease in the middle
pocket_ink_reader|pocket e-ink reader|2023-2026|a palm-sized e-ink reader with a six-inch screen, a button strip and a lanyard hole
page_button_reader|reader with page-turn buttons|2019-2025|a rounded reader with a grip on one side, two physical page-turn buttons and a tilted screen
"""
PHONES = """bag_phone|bag phone|1983-1989|a heavy beige handset on a coiled cord connected to a leather carry bag with a thick battery inside
brick_phone|brick phone|1983-1990|a beige handheld brick as long as a forearm with a stub antenna, a number pad and a small red LED display
stubby_antenna_phone|stubby-antenna handset|1990-1995|a small grey candybar handset with a short rubber antenna, a green dot-matrix display and a row of round keys
first_flip_phone|first flip phone|1996-1998|a very small flip phone with a hinged cover over the keypad and a short stub antenna
slider_banana_phone|slider phone|1996-1998|a curved banana-shaped slider that opens to reveal the keypad, a small green screen and a stubby antenna
snake_candybar|mono-screen candybar|1998-2002|a tough rounded candybar with a monochrome green screen, clicky keys, a swap-on coloured cover and a stubby antenna
colour_screen_candybar|colour-screen candybar|2002-2004|a slim candybar with a small colour screen, silver keys and a short pop-up antenna
camera_phone_early|early camera phone|2003-2005|a chunky candybar with a lens on the back, a small colour screen and a joystick on the front
razor_clamshell|slim clamshell phone|2004-2007|a very thin metal clamshell with a glowing keypad etched from a single sheet and a small external screen
swivel_phone|swivel phone|2004-2006|a phone whose screen pivots sideways to reveal a keypad
fashion_phone|fashion phone|2004-2008|a slim glossy phone with a jewelled touch, mirrored back and bright colour options
qwerty_business_phone|keyboard business phone|2005-2012|a wide candybar with a small screen above a full qwerty keyboard of tiny round keys and a scroll ball
communicator_clamshell|communicator clamshell|2004-2009|a large clamshell that opens to a wide screen above a full keyboard
early_touchscreen|early touchscreen phone|2007|a small slab with a large touchscreen and a single home button below
slab_smartphone|first-wave slab smartphone|2008-2012|a black glass slab with rounded corners, a home button and a small camera lens at the back
slider_keyboard_smartphone|slide-out keyboard smartphone|2009-2012|a touchscreen slab that slides sideways to show a full keyboard
big_screen_smartphone|big-screen smartphone|2012-2015|a large slab with thin metal edges, a sharp bright screen and a rounded back
bezeless_smartphone|bezel-less smartphone|2016-2018|a glass phone with a screen that curves around the edges and almost no bezel
notch_smartphone|notch smartphone|2017-2020|a glass slab with a screen cut-out at the top for the camera, a glossy glass back and a camera bump
triple_lens_smartphone|multi-lens smartphone|2019-2024|a slab with a square camera bump with three or four lenses and a flash
foldable_book_phone|book-style foldable|2019-2025|a phone that opens like a book to a tablet-sized screen with a visible crease
flip_foldable|flip foldable|2020-2025|a compact clamshell with a folding screen and a small cover screen
slim_fold_phone|slim modern folder|2024-2026|a very thin foldable with a barely visible crease and a rounded metal frame
rollable_phone|rollable phone|2025-2026|a phone whose screen slides out sideways from the frame to double its width
retro_revival_phone|revival brick phone|2017-2022|a modern rugged phone shaped like an old brick with a physical keypad and a thick battery
rugged_phone|rugged work phone|2015-2025|a thick phone with rubber bumpers, steel screws and a bright orange or yellow trim
glass_slab_future|transparent glass phone|the future|a see-through thin glass slab with an interface floating in the middle and no visible edges
wrist_band_phone|wrist-worn phone|the future|a wide flexible band around the wrist with a bright curved screen and a thin projected display above it
smart_glasses_phone|smart-glasses phone|the future|a pair of light frame glasses with a small glowing display in one lens and a touch strip on the arm
projection_phone|holographic phone|the future|a small flat disc that projects a floating screen above it
"""
E1 = ["a first-generation Kindle (2007), a large white wedge-shaped reader with a keyboard strip", "a Sony Reader PRS-500 (2006), a slim silver reader with a row of buttons and a small grey screen", "a Nook (2009), a white reader with a small colour touch strip under the e-ink screen", "a Kobo reader (2010), a slim reader with a quilted back", "a Kindle Keyboard (2010), a slim keyboard reader with a five-way controller", "a Kindle Paperwhite (2012), a front-lit slim reader with a rubber back", "a Kindle Voyage (2014), a thin reader with a flat glass front and a magnesium shell", "a Kindle Oasis (2016), a thin reader with a thick edge, a stepped back and page-turn buttons", "a Kobo Libra (2019), a reader with a grip and two page-turn buttons", "a reMarkable 2 (2020), a thin paper-like tablet with a stylus", "a Kindle Scribe (2022), a ten-inch note-taking reader with a pen", "a Kindle Colorsoft (2024), a colour e-ink reader", "a Kobo Elipsa (2021), a large e-ink reader with a stylus", "a Boox Note (2020), an e-ink tablet with a pen"]
P1 = ["a Motorola DynaTAC 8000X (1983), a cream brick handset with a stub antenna", "a Nokia 3310 (2000), a rounded tough candybar with a small mono screen", "a Motorola StarTAC (1996), a tiny clamshell with a stub antenna", "a Nokia 8110 (1996), a curved slider that hides the keypad", "a Motorola Razr V3 (2004), a thin metal clamshell with an etched keypad", "a BlackBerry 6210 (2003), a wide phone with a full qwerty keyboard", "an Apple iPhone (2007), a black glass slab with one home button", "a Samsung Galaxy S (2010), a slim black slab with a bright screen", "a Samsung Galaxy Fold (2019), a book-style foldable with a visible crease", "a Nokia N-Gage (2003), a taco-shaped gaming phone", "a Sony Ericsson T68i (2001), a small candybar with a colour screen", "a Motorola Razr foldable (2020), a flip foldable revival", "a Nokia 3310 reissue (2017), a coloured revival candybar"]
SCREEN = P('a page of a novel with a large chapter heading; a page of dense small print; a book cover thumbnail grid; a page of a cookbook with a photograph; the sleep screen showing a quiet drawing; a library list with progress bars; a page with a highlighted sentence and a small note; the text of a newspaper article in two columns')
CASE = P("out of any case; in a folding leather cover; in a soft fabric sleeve; in a clear plastic shell; in a magnetic flip cover; in a padded zip pouch; fitted with a sticker on the back; in a hand-knitted cosy")
WEAR = P("brand new; lightly scratched; worn smooth at the edges; with a cracked corner; yellowed with age; covered in fingerprints; with the paint rubbed off at the corners; with a sticker partly peeled")
REST = P("on a bedside table; on a café table beside a cup; in a hand; on a train seat; on a kitchen counter; on a desk with a stack of papers; on the arm of a sofa; beside a pair of reading glasses; on a car dashboard")
PSCREEN = P("a lock screen with a large clock; a map with a route line; a grid of coloured app icons; a text conversation with short messages; a photograph of a landscape; a blank dark screen; a green monochrome screen with a number; a dial pad with a number being entered")
PHONE_CASE = P("out of any case; in a leather belt holster; in a silicone case; in a flip cover; hanging from a lanyard; in a rugged rubber shell; fitted with a phone ring on the back; decorated with a hand-painted back")
PSCREEN_OLD = P("a phone number in small red digits; a number and a signal bar in green monochrome; a short text message in blocky letters; a signal icon and a clock on a small colour screen; a number being entered on the dial pad; a pixel game of a snake")
PSCREEN_FUT = P("a floating blue interface with soft glowing icons; a map drawn in light above the surface; a video call with a transparent frame; a glowing clock and weather display; a stream of messages in thin light")
OLD_END = 'early_touchscreen'
def build(final=None):
    G = {}
    for k, v in (('ereader_screen', SCREEN), ('ereader_case', CASE), ('ereader_wear', WEAR), ('ereader_rest', REST), ('phone_screen', PSCREEN), ('phone_screen_old', PSCREEN_OLD), ('phone_screen_future', PSCREEN_FUT), ('phone_case', PHONE_CASE), ('phone_wear', WEAR), ('phone_rest', REST)): G[k] = v
    G['ereader_text'] = ['"%s"' % t for t in ("Chapter One", "The Long Way Home", "Part Two", "A Quiet Season", "Prologue", "Notes", "Contents")]
    for pre, rows, noun in (('ereader', EREADERS, 'e-reader'), ('phone', PHONES, 'mobile phone')):
        keys = []; seen_new = False
        for row in rows.strip().split('\n'):
            k, label, yrs, look = row.split('|')
            if k == OLD_END: seen_new = True
            scr = '__phone_screen_future__' if yrs == 'the future' else ('__phone_screen__' if seen_new else '__phone_screen_old__')
            G['%s_%s_look' % (pre, k)] = ['%s %s from %s, %s' % ('an' if label[0] in 'aeio' else 'a', label, yrs, look)]
            if pre == 'ereader':
                G['%s_%s_prompt' % (pre, k)] = ['The subject is __ereader_%s_look__. The screen shows __ereader_screen__. It is %s, __ereader_wear__, and it is __ereader_rest__.' % (k, '__ereader_case__')]
            else:
                G['%s_%s_prompt' % (pre, k)] = ['The subject is __phone_%s_look__. The screen shows %s. It is %s, __phone_wear__, and it is __phone_rest__.' % (k, scr, '__phone_case__')]
            keys.append(k)
        for suf in ('look', 'prompt'): G['%s_%s' % (pre, suf)] = ['__%s_%s_%s__' % (pre, k, suf) for k in keys]
        G['%s_timeline' % pre] = ['__%s_%s_look__' % (pre, k) for k in keys]
    G['maker_ereader_models'] = E1; G['maker_phone_models'] = P1
    G['maker_ereader_prompt'] = ['The subject is __maker_ereader_models__. The screen shows __ereader_screen__. It is __ereader_case__, __ereader_wear__, and it is __ereader_rest__.']
    G['maker_phone_prompt'] = ['The subject is __maker_phone_models__. The screen shows __phone_screen__. It is __phone_case__, __phone_wear__, and it is __phone_rest__.']
    G['v76_dev_entry_points'] = ['ereader_prompt', 'ereader_timeline', 'phone_prompt', 'phone_timeline', 'maker_ereader_prompt', 'maker_phone_prompt']
    return G
if __name__ == '__main__': print(len(build()))
