"""Uniforms, work clothes, ceremonial dress, costumes and cosplay (uniform_*), plus full-coverage printed "trompe-l'oeil" T-shirts that imitate them in flat 2D print.
Files:
  uniform_name[_<group>]     the wearer/role with its place or era          uniform_outfit[_<group>]   role + every garment, one line
  uniform_prompt[_<group>]   picker for finished outfit lines                uniform_upper/_lower/_head/_feet/_carried   garments from every group, for mix-and-match
  uniform_mix                a free mix of upper body, lower body, headwear and footwear from different groups (the ludicrous option)
  uniform_tee[_<group>]      T-shirt whose all-over print imitates that uniform, flat and two-dimensional    uniform_tee_prompt   picker
  uniform_tee_style, uniform_tee_base, uniform_tee_neck, uniform_tee_body, uniform_tee_note   parts for your own tee prompts
Groups: medical emergency military aviation_sea_road trades hospitality_retail sport_performance ceremonial_world costume_genre ludicrous hobby formal
Adult people only.  Original descriptive wording, no brands or real people.  Deterministic."""
import os, sys, re, random, zlib, shutil
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from paths import FINAL
from uniform_data5 import U

def rg(*k): return random.Random(zlib.crc32('|'.join(map(str, k)).encode()))
def art(x): return ('a ' if x[0].isdigit() or x[0].lower() not in 'aeiou' else 'an ') + x
def cap(x): return x[:1].upper() + x[1:]
def dash(x): return '' if x.strip() == '-' else x.strip()
def rows(g):
    out = []
    for r in U[g]:
        n, tag, up, lo, he, fe, ca = [dash(x) for x in r.split('|')]
        out.append(dict(name=n, tag=tag, up=up, lo=lo, he=he, fe=fe, ca=ca))
    return out
def join(parts):
    parts = [p for p in parts if p]
    if len(parts) <= 1: return ''.join(parts)
    return ', '.join(parts[:-1]) + ' and ' + parts[-1]

BASE = [f'{c} cotton' for c in "white, heather grey, black, navy, charcoal, cream, sand, light blue, sage green, faded red, off-white, stone".split(', ')]
NECK = "crew-neck, V-neck, boat-neck, scoop-neck, long-sleeved crew-neck, ringer-style, boxy oversized, straight-cut, cropped, heavyweight".split(', ')
STYLE = ["a photoreal all-over print that looks like a real photograph of the outfit", "a lifelike photographic full-coverage print with natural fabric texture and shading", "a hyper-realistic sublimation print showing the real outfit in fine detail", "a realistic printed photo-texture that makes the shirt look like the real garment", "a seamless photoreal digital print with true-to-life colours", "an all-over sublimation print that covers the entire shirt", "a bold flat-colour illustration with thick black outlines", "a clean vector illustration print with flat colour fills", "a hand-drawn line-art print with flat colour fills", "a pop-art halftone print", "a vintage novelty-shirt print", "a retro screen-printed illustration with limited colours", "a comic-style inked illustration print", "a glossy all-over digital print", "a lightly distressed worn-in print", "a high-detail print that runs onto the sleeves and around the back"]
BODY = ["the outfit's front panels run straight down the shirt's front with its shoulders sitting on the shirt's shoulder seams, and its sleeves are printed along the shirt's sleeves to cuffs at the sleeve hems, showing", "the printed outfit runs from the neckline to the hem and from one sleeve hem to the other, its shoulders on the shirt's shoulder seams, showing", "the shirt's neckline is the outfit's collar opening, the shirt's sleeves carry the outfit's sleeves, and the shirt's hem is the outfit's lower edge, showing", "the outfit is printed across the whole front, over the shoulders and down both sleeves, showing", "every panel of the shirt, front, shoulders and sleeves, is a panel of the outfit, showing"]
FILL = ["The design is enlarged to fill the entire shirt, edge to edge, with no blank margin around it.", "The print covers every part of the shirt from the ribbed collar band to the hem and out to both sleeve hems, and wraps around the side seams to the back.", "No plain shirt fabric shows except the ribbed collar band, because the outfit fills the whole shirt.", "The outfit's colours flood the entire front and both sleeves as one continuous print, and the back carries the matching back of the outfit.", "The print is cut to the T-shirt's shape, so the shirt itself looks like the outfit being worn, with the sleeves as the outfit's sleeves."]
NOTE = ["The illusion is purely flat and two-dimensional, with no real fabric, buttons or pockets beyond the print.", "It is a trompe-l'oeil T-shirt: a plain cotton shirt pretending to be the outfit.", "The printed collar and lapels line up with the shirt's actual neckline.", "Tiny printed shadows and fold lines suggest the garment without any real depth.", "It is the kind of novelty tee that tricks the eye from across a room.", "The print wraps around the sides so the outfit seems to continue around the body.", "It is a flat print, not a framed picture, not a small centred graphic, not a standing figure and not a drawing of a garment on a hanger."]
NECK_SHORT = ["short-sleeved crew-neck", "short-sleeved V-neck", "short-sleeved boxy oversized", "short-sleeved straight-cut", "short-sleeved ringer-style", "short-sleeved heavyweight", "short-sleeved scoop-neck"]
NECK_LONG = ["long-sleeved crew-neck", "long-sleeved ringer-style", "long-sleeved heavyweight", "long-sleeved boxy oversized", "long-sleeved straight-cut", "long-sleeved V-neck"]
SHAPE_LONG = ["The shirt is a long-sleeved T-shirt because the outfit has long sleeves, so the outfit's sleeves are printed along the whole length of the shirt's sleeves to printed cuffs at the wrist hems, and nothing extends beyond the shirt's wrist hems or bottom hem.", "A long-sleeved shirt is used so the outfit's long sleeves fit exactly: the printed sleeves run the full length of the shirt's sleeves and end at the shirt's wrist hems, with nothing sticking out past them or below the hem."]
SHAPE_SHORT = ["The shirt is a short-sleeved T-shirt, so the outfit's sleeves are printed only as far as the shirt's short sleeve hems and end there, with nothing printed or attached below the sleeve hems or the bottom hem: no forearms, no long sleeves, no cuffs, no extra layers.", "A short-sleeved shirt is used so the outfit is printed as short sleeves or bare upper arms ending exactly at the shirt's sleeve hems, with empty space below them and below the hem."]
LONGRX = __import__('re').compile(r"coat|jacket|robe|cassock|tailcoat|gown|kimono|habit|jerkin|hauberk|armour|cloak|cape|smock|doublet|parka|jumper|sweater|cardigan|blouse|long-sleeved|bodysuit|jumpsuit|coverall|surcoat|vestment|kaftan|thobe|dress|suit|tunic|haori|poncho|shawl|flight|anorak|windbreaker|shirt with a long|boubou|djellaba|ruff|alb|stole|wrap|overalls with a|sleeved", __import__('re').I)
SHORTRX = __import__('re').compile(r"short-sleeved|short sleeve|scrub top|polo|T-shirt|singlet|sleeveless|vest|apron|bare|leotard|swimsuit|jersey|tabard|bib|harness", __import__('re').I)
def sleeves(up, r=None):
    if r is not None and armpart(r): return 'long'
    if r is not None and r.get('force') == 'short': return 'short'
    strong = LONGRX.search(up.replace('lead apron', ''))
    if strong: return 'long'
    return 'short' if SHORTRX.search(up) else 'long'
SHEERRX = __import__('re').compile(r"sheer|lace|tulle|mesh|\bnet\b|netting|fishnet|translucent|gauze|organza|chiffon|see-through|transparent|gossamer|muslin|voile", __import__('re').I)
def sheer(r): return bool(SHEERRX.search(' '.join([r['up'], r['lo'], r['he']])))
SKIN = ["a flat printed mid-tone brown tanned skin tone", "a flat printed warm mid-tone brown tanned skin tone", "a flat printed mid-tone golden-brown tanned skin tone", "a flat printed mid-tone brown tanned skin tone", "a flat printed warm tanned mid-brown skin tone", "a flat printed mid-tone brown tanned skin tone", "a flat printed deep brown skin tone", "a flat printed light tan skin tone", "a flat printed rich medium-brown skin tone"]
SHEERNOTE = ["Wherever the outfit is sheer, lace, mesh or net, the print includes {skin} underneath it, printed flat on the opaque cotton so it reads as skin seen through the material, with no real transparency.", "The sheer parts of the outfit are printed over {skin}, so the pattern appears to sit on skin, all of it flat ink on opaque cotton.", "Under every lace, net, mesh or see-through area the print shows {skin}, as a printed illusion on solid cotton."]
ARMRX = __import__('re').compile(r"gauntlets?|gloves?|mittens?|arm guards?|arm pads?|bracers?|vambraces?|wristbands?|sleeve garters?|cuffs?|sleeves? rolled|rolled sleeves|rolled-up sleeves|bare arms|water sleeves|long water sleeves|forearm|wrist|bangles?|armbands?|arm warmers?|bandages|bandaged|body paint|bells and ribbons", __import__('re').I)
ARMNOTE = ["The outfit has {part} on the forearm and wrist, so the shirt's sleeves are lengthened to the wrist and the printed {part} sits at the end of each sleeve, with nothing beyond the wrist hem.", "To show the {part} on the wearer's forearms, the shirt is made with sleeves that run all the way to the wrist, and the printed {part} appear on those lengthened sleeves.", "The sleeves are extended to full wrist length so the {part} that the outfit wears on the forearms can be printed on them, ending exactly at the wrist hems."]
def armpart(r):
    t = ' '.join([r['up'], r['ca']]); m = ARMRX.search(t)
    return m.group(0).lower() if m else None
NOFIG = ["The sleeves carry only the outfit's sleeve cloth: no second figure, no head, no face, no hair and no repeated copy of the outfit is printed on them, and the print has only one outfit running across the whole shirt.", "No head, face or hair is printed anywhere; the outfit simply begins at the neckline, and there is no person, no portrait and no mannequin pictured inside the print.", "The print is one single outfit, not a picture of a person: no figure, no head, no face, no small copy of the outfit on the sleeves or the sides, and no white or coloured backdrop behind it.", "There is no person in the print, only the outfit's cloth, trims and fastenings laid out across the shirt, with printed skin visible only where the outfit is open or bare."]
OPENRX = __import__('re').compile(r"open|low|plunging|sweetheart|deep|scoop|bare|strapless|sleeveless|leotard|crop|midriff|harness|singlet|vest|apron|bodice|halter|v-neck|loose shirt|laced|lacing|neckline|unbuttoned|undone|bikini|swimsuit|wetsuit|shirt|kurta|dhoti|toga|chiton|tunic|blouse|bandage|body paint", __import__('re').I)
SKINBITS = ["a flat printed collarbone and upper chest of {skin} showing at the open neckline", "a flat printed line of cleavage in {skin} at a low or sweetheart neckline", "flat printed chest hair on {skin} showing at the open collar", "flat printed belly hair on {skin} showing at a bare midriff or between shirt buttons", "flat printed bare skin in {skin} at the throat, chest and forearms where the outfit is open", "a flat printed bare chest in {skin} with printed chest hair where the outfit is worn open", "flat printed skin in {skin} at the neckline, with fine printed body hair where it would naturally show", "a printed glimpse of bare midriff in {skin} with a printed navel and light belly hair"]
def skinbits(r, R):
    t = ' '.join([r['up']])
    return OPENRX.search(t) and R.random() < .6
import re as _re
VLABEL = {'male': 'a masculine cut', 'female': 'a feminine cut', 'sexy_male': 'a sexy masculine costume-shop style', 'sexy_female': 'a sexy feminine costume-shop style'}
VPHRASE = {
 'male': [("cut for a masculine frame with broad shoulders", None), ("tailored in a masculine cut with a straight waist", None), ("in a masculine cut with a roomy chest and shoulders", None)],
 'female': [("cut for a feminine figure with a fitted waist", None), ("tailored in a feminine cut with a nipped-in waist", None), ("in a feminine cut with shaped seams and a flattering line", None)],
 'sexy_male': [("a sexy version worn open at the chest, the shirt unbuttoned to the waist, with tight trousers and rolled sleeves", None), ("a sexy version with a bare chest and abs under a short open jacket and tight low-slung trousers", 'short'), ("a sexy fitted version with a deep open neckline, bare muscular forearms and a tight waist", 'short'), ("a sexy sleeveless version with bare arms and chest, fitted trousers and boots", 'short')],
 'sexy_female': [("a sexy costume-shop version, short and fitted with a plunging neckline, a cinched waist, a short hemline, stockings and high heels", None), ("a sexy version with a bare midriff, a plunging neckline, a very short skirt and heels", 'short'), ("a sexy fitted version in glossy tight material, off-the-shoulder, with a thigh-high hemline and boots", 'short'), ("a sexy version with a corset bodice, deep cleavage, a short skirt and fishnet stockings", 'short')]}
def variant(r, v):
    R = rg('variant', v, r['name']); ph, force = R.choice(VPHRASE[v]); r2 = dict(r)
    r2['name'] = f"{r['name']} in {VLABEL[v]}"; r2['style'] = ph; r2['force'] = force
    if v in ('male', 'sexy_male') and r['lo'] and 'kilt' not in r['lo']: r2['lo'] = _re.sub(r"(a |an )?([\w-]+ )*skirt\b", 'trousers', r['lo'])
    return r2
TAIL = ["The outfit's own colours continue over the shoulders and down the sleeves, so no separate background colour, border or plain patch shows around the print.", "No background colour shows around the print: the outfit itself reaches every seam, shoulder and sleeve hem.", "The shoulders and sleeves are filled with the outfit's own cloth, not a backdrop colour or a plain field."]
ARMS = ["Arms and hands appear only at the sleeve ends and never cross the front of the shirt, so the front panel is one uninterrupted piece of the outfit.", "No arm or hand is printed across the chest or waist; the front is a single uninterrupted panel and the arms live on the sleeves.", "The front panel stays unbroken, with no printed arm, hand or pocket crossing it from the sides."]
SHAPE = ["The T-shirt keeps its ordinary T-shirt silhouette and sleeve length, with no added sleeves, layers, capes, cuffs or extra fabric beyond its own outline; the outfit's sleeves are printed only as far as the shirt's own sleeve hems and end there.", "The shirt's shape is not changed at all: same neckline, same sleeve length, same hem, with nothing added or extended, and the outfit's sleeves stop exactly where the shirt's sleeves stop. Nothing hangs below the sleeve hems or the bottom hem: no long sleeves, no under-layers, no extra garments.", "The garment is a normal unaltered T-shirt, so the outfit must fit inside its outline, including the sleeves, which end at the shirt's sleeve hems even if the outfit's sleeves are longer. Beyond them is empty space: no sleeve, cuff, forearm or layer of any kind sticks out below the sleeve hems or the hem."]
FLAT = ["Everything is flat ink on opaque cotton: lace, tulle, mesh, fur, feathers, sequins, armour and metal are only printed patterns, never real sheer, raised, layered or see-through material, and the shirt itself is never see-through.", "The shirt is solid and opaque and nothing is real but the cotton: every texture, transparency and sheen is a printed picture, not a material.", "No part of the shirt is translucent, layered or three-dimensional; delicate or sheer parts of the outfit are drawn as flat printed patterns on opaque cotton."]
BACK = ["The back of the shirt is printed just as completely, edge to edge, with the back of the same outfit: its back collar, shoulder blades and the backs of both sleeves.", "Turn the shirt around and the back carries the matching back of the outfit, printed edge to edge with nothing left plain.", "The print wraps all the way round: the back of the shirt shows the rear of the outfit from the back collar to the hem and along both sleeves.", "Front and back are both fully printed, the back showing how the same outfit looks from behind."]
CLEAN = ["No background colour or shirt colour shows around the outfit, at the shoulders or on the sleeves: the outfit's own cloth covers them completely, right out to the sleeve hems.", "The outfit's fabric runs seamlessly over the shoulders and sleeves with no coloured background, border or gap between the print and the shirt's edges.", "There is no background behind the outfit: the print reaches every seam of the shirt, so the shoulders and sleeves are outfit cloth, not shirt colour."]
ARMS = ["The arms hang straight down inside the sleeves, printed only along the sleeves, and no arm or hand crosses in front of the torso or the waist.", "Both arms are printed straight down the sleeves, with no hand on the hip, no hand across the body and no arm crossing the front."]
HANDS = ["printed cuffs at the sleeve hems", "printed gloves emerging at the sleeve hems", "printed cuffs and wrists at the sleeve hems", "printed cuffs where the sleeves end"]
PRINTLOW = ["a printed belt at the waist, with the top of {lo} cut off by the hem", "a printed waistband showing only the top of {lo}", "the printed top of {lo} reaching the hem and ending there"]
LEGS = ["The print stops at the shirt's bottom hem: no legs, thighs, knees, stockings, tights, fishnets, boots or shoes are shown, and a skirt or trousers appear only as far as the hem cuts them off.", "Nothing is printed below the hem: the lower half of the outfit is cut off by the hem, with no bare legs, no hosiery and no footwear.", "The shirt ends at the hem and so does the picture: no skin, leg, stocking or shoe appears at or below it."]
SIL = ["The outline is exactly an ordinary T-shirt's, with straight side seams and a round neckline, and sleeves cut to the length, width and angle of the outfit's own sleeves; no coat tails, skirts, capes, collars, sleeves or any other shape stick out beyond it, and the space outside the shirt is plain empty background.", "The silhouette is a plain T-shirt and nothing else: all of the outfit is drawn inside that shape, and no part of it extends past the side seams, shoulders, sleeve hems or bottom hem.", "The shirt keeps its own T-shirt outline from neckline to hem; the outfit is only printed on it and never changes its shape or adds pieces around it."]
NOARM = ["No arms, hands, fingers or skin are printed beside the body or hanging below the sleeve hems; the sleeves hold only the outfit's sleeve cloth.", "There are no printed arms or hands at the sides of the torso, and no cream, white or skin-coloured patches on the sleeves or at the sides unless the outfit itself has them."]
STYLE_TEE = [(r",? (and )?(with )?(a |an )?(tight |short |very short )?(low-slung )?(trousers|skirt)\b[^,]*", ''), (r",? (and )?(stockings|fishnet stockings|boots|heels|high heels)\b[^,]*", ''), (r",? (and )?(a )?(short |thigh-high )hemline[^,]*", ''), (r" and (stockings|boots|heels)[^,.]*", ''), (r",? (and )?(a )?very short skirt[^,]*", '')]
def tee_style(st):
    for rx, rep in STYLE_TEE: st = _re.sub(rx, rep, st)
    st = _re.sub(r",?( and)? with\s*$", '', st.strip(' ,')); return st.strip(' ,')
FULLSHAPE = ["The outfit is drawn to fill the whole shirt shape completely, with straight sides running from the armpits to the hem and no waist, hip, bust or belly shaping, so it suits any body size and is neither slim nor broad; there are no gaps, cream patches or empty areas at the sides.", "The outfit is not shaped to a body: it is stretched to the T-shirt's own rectangle and fills it fully, shoulder to shoulder and sleeve to sleeve, with no nipped waist, no hourglass, no muscular taper and no empty space at the sides.", "The uniform fills the entire shirt outline, edge to edge, with straight untapered sides, so the print neither looks slim nor heavy and fits every body type."]
def tee_name(n): return _re.sub(r" in a (masculine|feminine) cut", r" in a \1-styled version", n)
_BODYSHAPE = _re.compile(r"cut for a|tailored in a|in a (masculine|feminine) cut|nipped|flattering line|fitted waist|straight waist|broad shoulders|roomy chest", _re.I)
_old_tee_style = tee_style
def tee_style(st):
    if _BODYSHAPE.search(st) and 'sexy' not in st: return ''
    st = _re.sub(r",? (and )?(with )?a? ?(cinched|tight|fitted) (waist|trousers)[^,]*", '', _old_tee_style(st))
    st = st.replace('a sexy fitted version', 'a sexy version').replace('a sexy costume-shop version, short and fitted', 'a sexy costume-shop version')
    st = _re.sub(r",?( and)? with\s*$", '', st.strip(' ,')); return st.strip(' ,')
_WAIST = _re.compile(r",? ?(and )?(with )?(a |an )?(nipped|nipped-in|fitted|cinched|tapered|tight|hourglass|shaped|slim|figure-hugging|body-hugging)[ -]?(in )?(waist|waistline|fit|cut|silhouette|bodice)\b|\b(figure-hugging|body-hugging|skin-tight|slim-fit|slim-cut)\b ?", _re.I)
def nobody(r):
    r2 = dict(r)
    for k in ('up', 'lo'): r2[k] = _WAIST.sub('', r[k]).replace('  ', ' ').strip(' ,')
    return r2

SLX = [("sleeveless", _re.compile(r"sleeveless|vest|tank|singlet|strapless|halter|bib|tabard|bare arms|armless", _re.I), "sleeveless", "The shirt is cut sleeveless, with armholes where the outfit's sleeves would start, so no sleeve, arm or cuff is printed or attached."),
 ("cap", _re.compile(r"cap sleeve|puff sleeve|puffed sleeve|short puffed", _re.I), "cap-sleeved", "The shirt's sleeves are cut as short cap sleeves, ending high on the upper arm exactly where the outfit's sleeves end, with nothing printed or attached below them."),
 ("elbow", _re.compile(r"elbow|half-sleeve|half sleeve|sleeves? rolled|rolled sleeves|rolled-up sleeves|rolled to the elbow", _re.I), "elbow-length-sleeved", "The shirt's sleeves are tailored to end at the elbow, exactly where the outfit's sleeves end, and nothing is printed or attached below the sleeve hems."),
 ("threeq", _re.compile(r"three-quarter|3/4|bracelet-length|bracelet sleeve|kimono|haori|furisode|wide sleeve|bell sleeve|pagoda|batwing|angel sleeve|hanbok|jeogori", _re.I), "three-quarter-sleeved", "The shirt's sleeves are tailored to end about two-thirds of the way down the arm, exactly where the outfit's sleeves end, and nothing is printed or attached below the sleeve hems.")]
ANGLE = _re.compile(r"angled|slanted|diagonal|pointed|dagged|slashed|flared|bell|wide|hanging|batwing|kimono|haori|furisode|pagoda|angel|jeogori|hanbok|cape|cloak|poncho|scalloped|curved cuff|gauntlet", _re.I)
ANGNOTE = [" The sleeve hems are cut at an angle, slanted, pointed or curved, to follow the outfit's own cuffs, and the print follows that edge exactly.", " The shirt's sleeves are tailored to the outfit's cut: wide or flared where the outfit's sleeves flare, ending at the same slant or curve, with the print filling the whole sleeve shape."]
NECK_CORE = ["crew-neck", "V-neck", "scoop-neck", "boat-neck", "straight-cut", "boxy", "ringer-style", "heavyweight"]
SLEEVE_CUT = ["The T-shirt's sleeves can be cut to any length to match the outfit: sleeveless, cap, short, elbow-length, three-quarter or full length.", "The shirt is tailored so its sleeves finish exactly where the outfit's sleeves finish, whether high on the arm, at the elbow, two-thirds of the way down, at the wrist, or at an angle.", "The sleeve hems of the shirt follow the outfit's sleeve ends: straight, slanted, pointed, curved or flared."]
def sleeve_style(r):
    if armpart(r): return ('long', None, None)
    if r.get('force') != 'short':
        for k, rx, ph, note in SLX:
            if rx.search(r['up']) and not (k == 'sleeveless' and _re.search(r'jacket|coat|blouse|shirt|cardigan|kimono|robe', r['up'], _re.I) and not _re.search(r'sleeveless (jacket|coat|shirt|blouse|top|vest)|vest|tank|singlet|bib|tabard|halter|strapless', r['up'], _re.I)): return (k, ph, note)
    return (sleeves(r['up'], r), None, None)
def sleeve_angle(r): return ANGLE.search(r['up']) is not None
NOLOW = ["The whole shirt, right down to the hem, is the upper-body garment, jacket, coat skirts, apron, sash or belt: no trousers, shorts, skirt, kilt, leggings or legs are printed anywhere on the lower half.", "The lower half of the shirt simply continues the top garment down to the hem, with at most a belt or sash at the waist; no trousers, shorts, skirts or bare legs appear below it.", "Only the upper body of the outfit is shown, running all the way to the hem; the outfit's trousers, shorts and skirts are not printed at all."]
NOBACK = ["There is no backdrop or scenery anywhere on the shirt, not at the shoulders, sleeves, sides or hem: no sky, sea, landscape, wall, painted background, clouds or colour wash, only the outfit's own cloth.", "No background of any kind is printed, not even faintly on the sleeves or shoulders: no sky, scenery, room or painted ground, and every inch is outfit fabric.", "The print is the outfit alone, with no scene, sky, horizon or backdrop behind or around it, including at the edges of the sleeves."]
EDGE = ["The outfit's cloth runs right up to the shirt's collar seam, out to the shoulder seams and all the way round the armholes and sleeve hems, so the outfit's shoulders are stretched to the shirt's own shoulders and no gap, sky, scenery or colour shows between the outfit and the shirt's edge.", "At the neckline, shoulders and armholes the print is cut exactly to the shirt's outline: the outfit's collar meets the real collar band, its shoulders end at the real shoulder seams, and nothing like a background or sky fills the corners around the neck, shoulders or arms.", "Where the outfit's outline would normally stop inside the shirt, it is enlarged until it reaches the shirt's neck, shoulder and sleeve edges, leaving no leftover background patches around them."]
PRINTHEAD = ["a printed collar around the real neckline", "a printed collar continuing the outfit up to the neckline"]

# ---- v28: positive wording only (say what the shirt IS; negative lists made image models draw skies, figures and bodysuits) ----
CLEAN = ["The outfit's own cloth covers the whole shirt as one continuous print, so shoulders, sleeves and body are all in the outfit's colours.", "The outfit's fabric runs seamlessly over the shoulders and down the sleeves, every part of the shirt in the outfit's own colours and textures.", "One continuous print of the outfit's cloth covers the shirt from collar band to hem and out to both sleeve hems."]
EDGE = ["The outfit's cloth runs unbroken from the collar band across both shoulders and down both sleeves to their hems, so every part of the shirt is outfit cloth.", "The outfit's collar meets the real collar band, its shoulders sit on the real shoulder seams and its sleeves fill the real sleeves, all in one piece of printed cloth.", "The print is cut exactly to the shirt: neck, shoulders, armholes, sleeves and hem are all covered in the outfit's own fabric."]
NOBACK = ["Every part of the shirt, shoulders and sleeves included, shows the outfit's own colours and cloth texture in one uniform print."]
FULLSHAPE = ["The outfit is stretched to the shirt's own straight-sided shape and fills it completely, so it suits any body size.", "The uniform fills the whole straight-sided shirt shape edge to edge, the same width at chest, waist and hem.", "The outfit is laid out on the shirt's own rectangle shape, fully covering it from side seam to side seam."]
NOLOW = ["The shirt is an ordinary T-shirt ending in a straight bottom hem, and the garment printed on it runs straight down the whole shirt to that hem.", "The printed top garment continues down the shirt to its straight hem, with at most a belt or sash at the waist.", "Only the upper garment is printed, running all the way down to the shirt's straight hem."]
LEGS = NOLOW
SIL = ["The shirt keeps the outline of an ordinary T-shirt: round neckline, straight side seams, sleeves, and a straight open hem.", "It is an ordinary T-shirt in shape, with a straight open hem and sleeves cut to match the outfit's sleeves.", "The shirt is a standard T-shirt shape with a straight hem across the bottom."]
NOARM = ["The sleeves show only the outfit's sleeve cloth.", "Each sleeve is the outfit's sleeve, in its cloth and trim."]
ARMS = NOARM
NOFIG = ["The picture is only the garment: its cloth, seams, buttons and trims laid flat across the whole shirt like a sewing pattern.", "Only the outfit's fabric, trims and fastenings are pictured, spread across the entire shirt as a continuous pattern.", "The print is the garment itself, flat and unfolded over the shirt, in its own cloth and colours."]
FLAT = ["Everything is flat ink on opaque cotton: lace, tulle, fur, feathers, sequins, armour and metal appear as printed patterns.", "The shirt is solid opaque cotton and every texture and sheen is a printed picture.", "All textures, transparencies and sheens are printed patterns on solid cotton."]
SHAPE_LONG = ["The shirt is a long-sleeved T-shirt matching the outfit's long sleeves, printed with the sleeves and cuffs all the way down to the wrist hems.", "A long-sleeved shirt is used so the outfit's long sleeves fit exactly, printed full length to the shirt's wrist hems."]
SHAPE_SHORT = ["The shirt is a short-sleeved T-shirt, and the outfit's sleeves are printed as short sleeves ending exactly at the shirt's sleeve hems.", "A short-sleeved shirt is used, and the outfit is printed as short sleeves that end at the shirt's sleeve hems."]
SLX = [(k, rx, ph, n) for (k, rx, ph, _), n in zip(SLX, ["The shirt is cut sleeveless, with armholes where the outfit's sleeves would start.", "The shirt's sleeves are cut as short cap sleeves, ending high on the upper arm where the outfit's sleeves end.", "The shirt's sleeves are tailored to end at the elbow, exactly where the outfit's sleeves end.", "The shirt's sleeves are tailored to end about two-thirds of the way down the arm, exactly where the outfit's sleeves end."])]

def outfit_lines(r, seed):
    R = rg(seed, r['name']); n = r['name']; t = f" ({r['tag']})" if r['tag'] else ''
    full = join([r['up'], r['lo'], r['he'], r['fe']]); out = set()
    if r.get('style'): full = full + ', ' + r['style']
    out.add(f"{art(n)}{t}, wearing {full}")
    if r['ca']: out.add(f"{art(n)}{t}, wearing {full} and carrying {r['ca']}")
    out.add(f"{art(n)}, dressed in {r['up']}" + (f" with {r['lo']}" if r['lo'] else ''))
    if r['he']: out.add(f"{art(n)}{t}, in {r['up']} and {r['he']}")
    if r['fe']: out.add(f"{art(n)}{t}, in {join([r['up'], r['lo']])} and {r['fe']}")
    out.add(f"A person dressed as {art(n)}{t}: {full}")
    out.add(f"{cap(r['up'])}, {r['lo'] + ', ' if r['lo'] else ''}{r['he'] + ', ' if r['he'] else ''}{r['fe'] + ', ' if r['fe'] else ''}the full outfit of {art(n)}".replace(', , ', ', '))
    return sorted(out)

# ---- costume tees: carry more of the costume, and novelty fake-body tees ----
MORE_N = ["the collar, neckwear and fastenings of the outfit", "the outfit's badges, insignia and emblems", "the belt, straps and buckles of the outfit", "its pockets, flaps and trims", "the headwear's emblem or crest worked into the chest", "the held item or gear of the outfit, shown as a patch or large motif on the chest or a sleeve", "the footwear's trim colours as stripes on the cuffs and hem", "the lower garment's colours and pattern as a band across the hem", "the most recognisable props and accessories of the outfit as appliqué pieces"]
MORE_T = ["The tee is clearly a costume tee, not a plain shirt: it shows {a}, {b} and {c}, so anyone can tell at a glance what outfit it stands for.", "To read as a costume rather than a plain top, it adds {a}, {b} and {c}, bold and large enough to identify the outfit from across a room.", "It carries enough of the costume to be unmistakable: {a}, {b} and {c}, all in the outfit's own colours."]
SWIMRX = re.compile(r"swim|bikini|bather|bathing|lifeguard|beach|diver", re.I)
MUSRX = re.compile(r"bodybuilder|strongman|strongwoman|gladiator|barbarian|caveman|wrestler|centurion|surfer|muscle|caveperson|viking|tarzan|gorilla|boxer|weightlift", re.I)
NB_SWIM = ["The front is a trompe-l'oeil swimsuit: a printed or appliqué bikini top or swimsuit neckline with a fake cleavage curve, fake skin in a warm tone, a shaped bust line, straps over the shoulders, and a fabric waistband or swimsuit trim at the hem, so the tee looks like a bathing suit.", "It is a novelty bathing-suit tee: padded sewn-in fake cleavage and skin tone panels at the neckline, a swimsuit top with straps and ties drawn across the chest, and the swimsuit's colours and pattern continuing down the body to a hemmed swimsuit-style waist.", "The tee imitates a swimsuit worn on bare skin: a fake skin-tone chest and shoulders, a built-up cleavage line with stitched shading, swimsuit straps, ruching and trim, all sewn or printed onto the shirt."]
NB_MUS = ["The front is a novelty fake torso: a sewn-in bare chest with raised, padded pectoral muscles, an abs panel, fake nipples as small stitched discs, fabric chest hair in tufts, and a skin-tone surface from collar to hem, all as a joke garment.", "It imitates a bare muscular upper body: padded sculpted pecs and abs with stitched definition lines, fake nipples, tufted fabric chest hair and arms with sewn biceps shapes, in a skin tone, on a plain T-shirt shape.", "A novelty muscle-torso tee: the whole front is a fake chest with built-up muscles, hairy fabric patches, small round stitched nipples and a belly button, with the costume's belt, straps or loincloth trim added at the waist."]
def novelty_body(r, R, sewn=False):
    t = r['name'] + ' ' + (r['up'] or '')
    if SWIMRX.search(t): s = R.choice(NB_SWIM)
    elif MUSRX.search(t): s = R.choice(NB_MUS)
    else: return ''
    return ' ' + s + (' The pieces are real sewn fabric, padded and stitched.' if sewn else ' The look is a flat printed illusion of a body with sewn trims.')
def costume_more(r, R, sewn=False):
    a, b, c = R.sample(MORE_N, 3)
    return ' ' + R.choice(MORE_T).format(a=a, b=b, c=c) + novelty_body(r, R, sewn)

def tee_lines(r, seed, k=9):
    r = nobody(r); R = rg(seed, r['name'], 'tee'); n = tee_name(r['name']); out = set(); tries = 0
    while len(out) < k and tries < 80:
        tries += 1
        sk, sph, snote = sleeve_style(r); sl = sk if sk in ('long', 'short') else 'cut'; ap = armpart(r); neckp = R.choice(NECK_LONG if sl == 'long' else NECK_SHORT) if sl != 'cut' else f"{sph} {R.choice(NECK_CORE)}"; head = f"A {neckp} cotton T-shirt, a real plain T-shirt and not a real garment, covered edge to edge in {R.choice(STYLE)}, designed to make the shirt look like the outfit of {art(n)}"
        extra = []
        if r['he'] and R.random() < .35: extra.append(R.choice(PRINTHEAD))
        if R.random() < .6: extra.append(R.choice(HANDS).format(ca=r['ca'] or 'nothing'))
        s = f"{head}. {R.choice(FILL)} {cap(R.choice(BODY))} {r['up']}.{(' The outfit is ' + tee_style(r['style']) + '.') if r.get('style') and tee_style(r['style']) else ''} {R.choice(BACK)} {R.choice(CLEAN)} {R.choice(SIL)} {R.choice(NOLOW)} {R.choice(EDGE)} {R.choice(FULLSHAPE)} {R.choice(SHAPE_LONG if sl == 'long' else SHAPE_SHORT) if sl != 'cut' else snote}{(R.choice(ANGNOTE) if sleeve_angle(r) else '')} {R.choice(FLAT)} {R.choice(NOFIG)}" + (' It may also show ' + R.choice(SKINBITS).format(skin='__uniform_tee_skin__') + ', all as flat ink.' if skinbits(r, R) else '') + (' ' + R.choice(ARMNOTE).format(part=ap) if ap else '') + (' ' + R.choice(SHEERNOTE).format(skin='__uniform_tee_skin__') if sheer(r) else '') + (f" It also shows {join(extra)}." if extra else '') + ' ' + R.choice(NOTE)
        out.add(s + costume_more(r, R, False))
    return sorted(out)

def run(final=FINAL):
    F = {}; allr = []
    for g in U:
        rs = rows(g); allr += [(g, r) for r in rs]
        F[f'uniform_name_{g}'] = sorted({f"{art(r['name'])} ({r['tag']})" if r['tag'] else art(r['name']) for r in rs} | {r['name'] for r in rs})
        F[f'uniform_outfit_{g}'] = sorted({l for r in rs for l in outfit_lines(r, g)})
        F[f'uniform_prompt_{g}'] = [f'__uniform_outfit_{g}__']
        F[f'uniform_tee_{g}'] = sorted({l for r in rs for l in tee_lines(r, g)})
    F['uniform_tee_novelty_swimsuit'] = [x for x in NB_SWIM]; F['uniform_tee_novelty_torso'] = [x for x in NB_MUS]; F['uniform_tee_novelty_body'] = ['__uniform_tee_novelty_swimsuit__', '__uniform_tee_novelty_torso__']
    for g in U:
        F[f'uniform_tee_back_{g}'] = sorted({f"A {R_n} cotton T-shirt seen from behind, the whole back printed edge to edge with the back of the outfit of {art(tee_name(r['name']))}: the back of {r['up']}, running from the back collar over the shoulder blades and down both sleeves to the hem. Only the back is shown, as a flat print of the garment's cloth that fills the whole shirt, with the straight hem of an ordinary T-shirt at the bottom." for r in rows(g) for R_n in rg(g, r['name'], 'back').sample(NECK_LONG if sleeves(r['up'], r) == 'long' else NECK_SHORT, 3)})
    VARS = list(VLABEL)
    for g in U:
        for v in VARS:
            rs2 = [variant(r, v) for r in rows(g)]
            F[f'uniform_outfit_{g}_{v}'] = sorted({l for r in rs2 for l in outfit_lines(r, g + v)})
            F[f'uniform_prompt_{g}_{v}'] = [f'__uniform_outfit_{g}_{v}__']
            F[f'uniform_tee_{g}_{v}'] = sorted({l for r in rs2 for l in tee_lines(r, g + v, 4)})
    for v in VARS:
        F[f'uniform_prompt_{v}'] = [f'__uniform_prompt_{g}_{v}__' for g in U]
        F[f'uniform_outfit_{v}'] = [f'__uniform_outfit_{g}_{v}__' for g in U]
        F[f'uniform_tee_{v}'] = [f'__uniform_tee_{g}_{v}__' for g in U]
    F['uniform_prompt_gendered'] = [f'__uniform_prompt_{v}__' for v in VARS]
    F['uniform_tee_gendered'] = [f'__uniform_tee_{v}__' for v in VARS]
    TONES = {'very_deep_brown': 'very deep brown', 'deep_brown': 'deep brown', 'mid_brown_tan': 'mid-tone brown tanned', 'golden_olive': 'golden olive', 'light_tan': 'light tan', 'fair_pale': 'fair and pale'}
    F['uniform_skin_tone'] = [f'a flat printed {t} skin tone' for t in TONES.values()]
    ALLV = ['neutral'] + VARS
    for tk, tn in TONES.items():
        for v in ALLV:
            outs, tees = [], []
            for g in U:
                for r in rows(g):
                    r2 = r if v == 'neutral' else variant(r, v)
                    ol = outfit_lines(r2, g + v + tk); outs.append(rg(tk, v, r['name']).choice(ol) + f", with {tn} skin")
                    tl = tee_lines(r2, g + v + tk, 1)
                    tees.append(tl[0].replace('__uniform_tee_skin__', f'a flat printed {tn} skin tone') + f" Any printed skin, such as hands, wrists, neck, chest or forearms, is in a flat printed {tn} skin tone.")
            F[f'uniform_prompt_tone_{tk}_{v}'] = sorted(set(outs)); F[f'uniform_tee_tone_{tk}_{v}'] = sorted(set(tees))
        F[f'uniform_prompt_tone_{tk}'] = [f'__uniform_prompt_tone_{tk}_{v}__' for v in ALLV]
        F[f'uniform_tee_tone_{tk}'] = [f'__uniform_tee_tone_{tk}_{v}__' for v in ALLV]
    F['uniform_prompt_tone'] = [f'__uniform_prompt_tone_{tk}__' for tk in TONES]
    F['uniform_tee_tone'] = [f'__uniform_tee_tone_{tk}__' for tk in TONES]
    F['uniform_tee_random'] = [f'__uniform_tee_tone_{tk}__' for tk in TONES for _ in range(2 if tk == 'mid_brown_tan' else 1)]
    F['uniform_random'] = [f'__uniform_prompt_tone_{tk}__' for tk in TONES for _ in range(2 if tk == 'mid_brown_tan' else 1)]
    G = list(U)
    F['uniform_name'] = [f'__uniform_name_{g}__' for g in G]
    F['uniform_outfit'] = [f'__uniform_outfit_{g}__' for g in G]
    F['uniform_prompt'] = [f'__uniform_prompt_{g}__' for g in G]
    F['uniform_tee'] = [f'__uniform_tee_{g}__' for g in G]
    F['uniform_tee_back'] = [f'__uniform_tee_back_{g}__' for g in G]
    F['uniform_tee_back_note'] = BACK
    F['uniform_tee_clean'] = [t + ' ' + a for t in TAIL for a in ARMS]; F['uniform_tee_clean'] = CLEAN; F['uniform_tee_arms'] = ARMS; F['uniform_tee_arm'] = [x.format(part='gloves or cuffs') for x in ARMNOTE]; F['uniform_tee_nofig'] = NOFIG; F['uniform_tee_skin_detail'] = [x.format(skin='__uniform_tee_skin__') for x in SKINBITS]; F['uniform_tee_skin'] = SKIN; F['uniform_tee_sheer'] = [x.format(skin='__uniform_tee_skin__') for x in SHEERNOTE]; F['uniform_tee_shape'] = SHAPE; F['uniform_tee_shape_long'] = SHAPE_LONG; F['uniform_tee_shape_short'] = SHAPE_SHORT; F['uniform_tee_flat'] = FLAT; F['uniform_tee_legs'] = LEGS; F['uniform_tee_edge'] = EDGE; F['uniform_tee_nolower'] = NOLOW; F['uniform_tee_nobackdrop'] = NOBACK; F['uniform_tee_sleeve_cut'] = SLEEVE_CUT + [x[0].upper() + x[1:] if False else x for _, _, _, x in SLX] + [x.strip() for x in ANGNOTE]; F['uniform_tee_fullshape'] = FULLSHAPE; F['uniform_tee_silhouette'] = SIL; F['uniform_tee_noarm'] = NOARM
    F['uniform_tee_body_cap'] = [x[:1].upper() + x[1:] for x in BODY]
    F['uniform_tee_prompt'] = [f'__uniform_tee_{g}__' for g in G]
    F['uniform_upper'] = sorted({r['up'] for _, r in allr if r['up']})
    F['uniform_lower'] = sorted({r['lo'] for _, r in allr if r['lo']})
    F['uniform_head'] = sorted({r['he'] for _, r in allr if r['he']})
    F['uniform_feet'] = sorted({r['fe'] for _, r in allr if r['fe']})
    F['uniform_carried'] = sorted({r['ca'] for _, r in allr if r['ca']})
    F['uniform_tag'] = sorted({r['tag'] for _, r in allr if r['tag']})
    F['uniform_mix'] = ['A person in __uniform_upper__, __uniform_lower__, __uniform_head__ and __uniform_feet__', 'A person in __uniform_upper__ and __uniform_head__, holding __uniform_carried__', 'A person in __uniform_upper__, __uniform_lower__ and __uniform_feet__, carrying __uniform_carried__', 'A person dressed in __uniform_upper__ with __uniform_lower__ and __uniform_head__']
    F['uniform_tee_style'] = STYLE
    F['uniform_tee_base'] = BASE; F['uniform_tee_fill'] = FILL; F['uniform_tee_neck'] = [x.lstrip('a ') if False else x for x in NECK]
    F['uniform_tee_body'] = BODY; F['uniform_tee_note'] = NOTE
    F['uniform_tee_mix'] = ['A T-shirt covered edge to edge in __uniform_tee_style__, designed to look like a worn outfit. __uniform_tee_fill__ __uniform_tee_body_cap__ __uniform_upper__. __uniform_tee_back_note__ __uniform_tee_clean__ __uniform_tee_arms__ __uniform_tee_shape__ __uniform_tee_flat__ __uniform_tee_nofig__ __uniform_tee_note__', 'A T-shirt printed all over to look like a worn outfit. __uniform_tee_fill__ __uniform_tee_body_cap__ __uniform_upper__. __uniform_tee_back_note__ __uniform_tee_clean__ __uniform_tee_arms__ __uniform_tee_shape__ __uniform_tee_flat__ __uniform_tee_nofig__ __uniform_tee_note__']
    F['uniform_tee_prompt'] += ['__uniform_tee_mix__']
    os.makedirs(final, exist_ok=True)
    for n, l in F.items():
        assert l and all(l) and not any(re.search(r'[{}|]', x) or re.match(r'\d+::', x) for x in l), n
        open(os.path.join(final, n + '.txt'), 'w', encoding='utf8', newline='\n').write('\n'.join(l) + '\n')
    print('uniforms:', len(F), 'files;', sum(len(U[g]) for g in U), 'uniforms')
    return F
def export_aoo(out, prefix='aoo_'):
    tmp = os.path.join(out, '_u_tmp'); os.makedirs(tmp, exist_ok=True); F = run(tmp); shutil.rmtree(tmp)
    names = set(F); ref = re.compile(r'__([A-Za-z0-9_\-/]+)__'); n = 0
    for name, lines in F.items():
        keep = list(dict.fromkeys(l for l in lines if l.strip()))
        keep = [ref.sub(lambda m: '__' + prefix + m.group(1) + '__' if m.group(1) in names else m.group(0), l) for l in keep]
        if 'prompt' not in name and name != 'uniform_mix': random.Random(zlib.crc32(name.encode())).shuffle(keep)
        open(os.path.join(out, prefix + name + '.txt'), 'w', encoding='utf8', newline='\n').write('\n'.join(keep) + '\n'); n += 1
    return n
if __name__ == '__main__':
    a = [x for x in sys.argv[1:] if os.path.isdir(x)]; run(os.path.abspath(a[0]) if a else FINAL)
