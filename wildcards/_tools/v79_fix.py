"""v79 stage C - full physical descriptions for the named e-reader and phone models (v76 lines only had a few words each). Real names stay in maker_ files only."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

EREADERS = [
"a first-generation Kindle (2007), a wedge-shaped white plastic reader about the size of a paperback, thick at the bottom edge and thin at the top, with a small grey four-shade e-ink screen at the top, a full-width curved strip of small keyboard keys below it, a silver scroll wheel and a thin vertical page-turn bar down each side",
"a Sony Reader PRS-500 (2006), a slim silver metal-fronted reader with a dark grey bezel around a small six-inch grey e-ink screen, a row of small round number buttons along the bottom, a short joystick pad on the left side and a smooth dark leather-textured back",
"a Nook (2009), a white plastic reader with a grey e-ink screen of about six inches, a thin dark grey bezel, a small colour touch strip under the screen, a rounded back with a smooth soft-touch finish and two narrow page-turn buttons on each side",
"a Kobo reader (2010), a slim reader with a five-inch grey e-ink screen, a wide pale bezel, a single square button below the screen and a pattern of small quilted diamonds across the soft matte back",
"a Kindle Keyboard (2010), a slim off-white plastic reader about the size of a small paperback, a six-inch grey e-ink screen above a full qwerty keyboard of small rectangular keys with a five-way button beside it, a thin silver edge and page-turn bars on both sides",
"a Kindle Paperwhite (2012), a slim black reader with a six-inch front-lit e-ink screen, a thin flat black bezel with no buttons, a small logo at the bottom of the bezel and a soft-touch rubber back with a pale grey logo",
"a Kindle Voyage (2014), a thin black reader with a six-inch front-lit e-ink screen set flush in a single sheet of flat glass, a slim magnesium shell with a tapered back and four small pressure-sensitive page-turn marks in the bezel at both sides",
"a Kindle Oasis (2016), a thin asymmetrical reader with a seven-inch e-ink screen, a very thick rounded edge on one side holding two page-turn buttons and a battery, a thin opposite edge, a stepped metal back and a matt silver finish",
"a Kobo Libra (2019), an asymmetrical seven-inch e-ink reader with a thick left edge carrying two page-turn buttons, a flat white screen, a rounded back with a soft grip pattern and a slim bezel on the other sides",
"a reMarkable 2 (2020), a very thin tablet with a ten-inch paper-textured greyscale e-ink screen, a wide left edge in dark grey wrapped in a smooth grey fabric-like grip, a thin brushed aluminium body and a slim magnetic stylus clipped to the side",
"a Kindle Scribe (2022), a large ten-inch e-ink tablet with a wide flat grey bezel on the left holding a slim grey pen on a magnetic strip, a thin aluminium body in grey and a handwritten notebook page on the screen",
"a Kindle Colorsoft (2024), a thin seven-inch e-ink reader with a slightly warm-toned colour screen showing a muted book cover, a flat black bezel and a smooth dark back with a single logo",
"a Kobo Elipsa (2021), a big ten-inch e-ink reader with a wide white left bezel, a slim matt white body, a fine pen resting along its edge and a page marked with handwritten notes",
"a Boox Note (2020), a thin ten-inch e-ink tablet with a flat white bezel, a silver metal back, a small row of tiny buttons along the bottom edge, a thin stylus and a page with sketches on screen",
]
PHONES = [
"a Motorola DynaTAC 8000X (1983), a tall cream plastic brick of a handset about thirty centimetres long, with a long thin rubbery stub antenna on top, a small row of red digits above a large grid of chunky square grey number keys and a thick curved earpiece grille at the top",
"a Nokia 3310 (2000), a small rounded candybar phone with a smooth two-tone blue plastic case, a small grey monochrome screen with a small bump at the top, a curved navigation key below it and a grid of soft curved number keys",
"a Motorola StarTAC (1996), a tiny silver-grey clamshell with a short stub antenna on top, a small flip cover that folds down over a grid of small round number keys and a small single-line screen on the inside",
"a Nokia 8110 (1996), a curved dark grey slider phone shaped like a banana, with a hinged cover that slides down to reveal a small keypad and a small monochrome screen above it",
"a Motorola Razr V3 (2004), an ultra-thin silver aluminium clamshell with a smooth flat cover, a glowing blue etched keypad cut from a single sheet of metal, a small outer screen and a thin black bezel around the main screen",
"a BlackBerry 6210 (2003), a wide dark grey phone with a small colour screen at the top above a full qwerty keyboard of small tight rounded keys, a silver scroll wheel on the right side and a short stub antenna",
"an Apple iPhone (2007), a slim black glass-fronted slab with a silver aluminium back and a black plastic band at the bottom, a large touch screen with rounded corners, one round home button below the screen and a thin silver rim",
"a Samsung Galaxy S (2010), a slim black plastic slab with a large bright four-inch screen, a thin black bezel, one central physical button with a touch key either side and a slightly textured black back",
"a Samsung Galaxy Fold (2019), a book-style foldable phone with a small narrow screen on its outside and a large tablet-sized screen inside that folds along a visible vertical crease, a silver hinge down the spine and thick dark bezels at the top",
"a Nokia N-Gage (2003), a wide curved taco-shaped gaming phone in silver and black, with a small screen in the centre, a round directional pad on the left, a grid of number keys on the right and a speaker slot on the thin top edge",
"a Sony Ericsson T68i (2001), a small silver and dark grey candybar with a small colour screen, a rounded joystick below it, a grid of soft flat keys and a short stub antenna",
"a Motorola Razr foldable (2020), a flip foldable with a tall glossy screen that folds in half along a horizontal crease, a thin metal body in black, a small outer screen on the lower half and a chin below the main screen",
"a Nokia 3310 reissue (2017), a small rounded candybar with a glossy bright yellow plastic case, a small colour screen, a curved navigation key and a grid of soft curved number keys",
]
ERS = [
'a page of a novel with the heading "Chapter One" and the lines "The rain had not stopped since morning." and "She left the key on the table."',
'a page of dense small print with the lines "It was a quiet town, and the people kept to themselves." and "Nobody asked where the river went."',
'a grid of book cover thumbnails with the titles "The Long Way Home", "A Quiet Season" and "Salt and Smoke" under them',
'a page of a cookbook with the heading "Lentil Soup" and the lines "Two cups of lentils." and "One onion, chopped fine."',
'the sleep screen showing a quiet line drawing with the words "Sleeping" and "Tap to wake" at the bottom',
'a library list with the lines "The Long Way Home - 80%" and "A Quiet Season - 12%" beside progress bars',
'a page with the highlighted sentence "The sea does not keep its promises." and a small note reading "Check this quote"',
'the text of a newspaper article in two columns, with the headline "Harbour Opens Early" and the first line "Boats were out before dawn."',
'a contents page with the lines "Prologue", "Part One", "Part Two" and "Notes" and page numbers beside them',
'a settings page with the lines "Brightness", "Warmth" and "Font size" beside small slider bars',
]
PS = [
'a lock screen with the large clock "09:41" and the line "Tuesday 12 March"',
'a map with a route line and the text "12 min" and "Turn left on Mill Road"',
'a grid of coloured app icons with the labels "Mail", "Maps", "Photos" and "Music"',
'a text conversation with the messages "Are you free tonight?" and "Yes, see you at eight"',
'a photograph of a landscape with the caption "Lake Day" under it',
'a dark screen with the single line "Low battery" in small white letters',
'a dial pad with the number "555 0142" being entered',
'a notification list with the lines "Meeting at 3" and "2 new messages"',
]
PSO = [
'a green monochrome screen with the line "CALLING..." and the number "555 0142"',
'a small grey screen with the lines "MENU" and "MESSAGES"',
'a pale screen with the line "SIGNAL" above a row of bars',
'a pixel screen with the lines "NEW MESSAGE" and "FROM HOME"',
'a monochrome screen with the clock "10:15" and the line "SNAKE" under a small picture',
'a pale screen with the lines "SELECT" and "BACK" at the bottom',
]
PSF = [
'a clear floating display with the lines "Good evening" and "Two messages"',
'a curved screen showing the lines "Call from Anna" and "Answer"',
'a translucent panel with the clock "21:30" and the line "Rain at ten"',
'a mirror-like screen with the lines "Welcome back" and "Tap to begin"',
'a glowing sheet of glass with the lines "Tomorrow, 8:00" and "Wake up"',
]
def build(final=None):
    return {'maker_ereader_models': EREADERS, 'maker_phone_models': PHONES, 'ereader_screen': ERS, 'phone_screen': PS, 'phone_screen_old': PSO, 'phone_screen_future': PSF, 'v79_fix_entry_points': ['maker_ereader_prompt', 'maker_phone_prompt', 'ereader_prompt', 'phone_prompt']}
if __name__ == '__main__': print(len(build()))
