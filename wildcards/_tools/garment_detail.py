"""Generic detail engine: turns a clothing name into a full description (front, back, covered, uncovered, cut and fit) from its head garment and its modifiers.
Used for the optional garment_<family>_detail files; the plain name files are unchanged."""
import re
def has(n, *w): return any(re.search(r'\b' + x + r'\b' if x.isalpha() else x, n) for x in w)
# head noun -> (kind, front, back, covered, uncovered, fit)
HEADS = [
 (('bra', 'bralette', 'bustier', 'corset', 'cincher', 'bandeau', 'top', 'tank', 'camisole', 'cami', 'blouse', 'shirt', 'tee', 't-shirt', 'tunic', 'sweater', 'jumper', 'cardigan', 'hoodie', 'vest', 'waistcoat', 'bolero', 'halter', 'crop', 'jersey', 'smock', 'singlet', 'doublet', 'jerkin', 'polo', 'henley'), 'top', 'a top covering the chest and torso', 'a back panel that matches the front', 'the chest and the upper body', 'the legs and the lower body', 'fitted through the torso'),
 (('trousers', 'pants', 'jeans', 'shorts', 'breeches', 'leggings', 'tights', 'bloomers', 'culottes', 'chinos', 'joggers', 'slacks', 'knickers', 'britches', 'harem'), 'bottom', 'a waistband and two leg tubes covering the hips and legs', 'a full seat panel covering the buttocks', 'the hips, the seat and the legs', 'the torso', 'sits at the waist or hips'),
 (('skirt', 'kilt', 'sarong', 'petticoat', 'tutu', 'pareo', 'lungi', 'dhoti', 'wrap'), 'skirt', 'a waistband with a hanging skirt covering the hips and thighs', 'a matching skirt panel with a seam or slit at the back', 'the hips and the upper legs', 'the torso and the lower legs', 'hangs from the waist'),
 (('dress', 'gown', 'frock', 'robe', 'kimono', 'kaftan', 'caftan', 'abaya', 'jilbab', 'sari', 'saree', 'cheongsam', 'qipao', 'hanbok', 'dirndl', 'sundress', 'nightgown', 'nightdress', 'chemise', 'slip', 'negligee', 'babydoll', 'peignoir', 'shift', 'muumuu'), 'dress', 'a one-piece garment covering the torso and falling to the hem', 'a back that falls from the shoulders to the hem', 'the torso, the hips and part of the legs', 'the arms and the lower legs', 'falls from the shoulders or bust'),
 (('jumpsuit', 'coverall', 'overalls', 'dungarees', 'romper', 'playsuit', 'bodysuit', 'catsuit', 'leotard', 'unitard', 'onesie', 'boilersuit', 'unionsuit', 'union', 'suit'), 'onepiece', 'a one-piece garment covering the torso and legs in a single piece', 'a back panel with a zip, buttons or snaps', 'the torso and the legs', 'the head, hands and feet', 'one continuous piece from shoulders to legs'),
 (('jacket', 'coat', 'cape', 'cloak', 'poncho', 'parka', 'duster', 'blazer', 'overcoat', 'trench', 'anorak', 'windbreaker', 'bomber', 'mantle', 'shawl', 'stole', 'wrap', 'cardigan'), 'outer', 'an open or fastened front with lapels or a collar', 'a back panel falling from the shoulders', 'the torso and arms over other clothes', 'whatever lies below its hem and the body parts outside it', 'worn over other layers'),
 (('thong', 'panty', 'panties', 'brief', 'briefs', 'boxer', 'boxers', 'knicker', 'g-string', 'garter', 'stockings', 'hosiery', 'pantyhose'), 'under', 'a small front panel on a waistband or garter', 'a back panel or strap', 'the groin and the hips', 'the rest of the body', 'low or high rise, snug'),
]
def head(n):
    best = None; bp = -1
    for words, *rest in HEADS:
        for w in words:
            m = list(re.finditer(r'\b' + re.escape(w) + r's?\b', n))
            if m and m[-1].start() > bp: best = (words, rest); bp = m[-1].start()
    return best[1] if best else None
def detail(name):
    n0 = name.lower()
    if re.search(r'neck corset|posture collar', n0): return 'Front: a tall rigid band wrapping the neck from the collarbone toward the chin, laced or buckled at the front. Back: the band closes or laces at the back of the neck. It covers the neck and holds the head upright, and leaves the shoulders, chest and the rest of the body uncovered. Cut and fit: snug and stiff, boned or reinforced, adjustable by the lacing'
    parts = [p.strip() for p in re.split(r' and | with a matching | plus ', n0) if p.strip()]
    hp = [p for p in parts if head(p) and len(p.split()) > 1]
    if len(hp) >= 2 and len(set(head(p)[0] for p in hp)) >= 2:
        return ' -- '.join(f'Piece {i + 1} ({p}): ' + _one(p) for i, p in enumerate(hp[:3]))
    return _one(n0)
def _one(n0):
    n = n0; h = head(n)
    if re.search(r'corset|bustier|cincher|waist trainer|\bstays\b|corselette', n) and not re.search(r'neck corset', n):
        h = ('corset', 'a boned bodice that shapes and cinches the torso, with a busk, zip or lacing at the front' + (' and cups for the bust' if not re.search(r'cupless|underbust|cincher|trainer', n) else ''), 'lacing or hooks up the back with a modesty panel behind the laces', 'the ribs, waist and upper hips' + (' and the bust' if re.search(r'overbust|cup|bustier|dress', n) else ''), 'the legs, the shoulders' + ('' if re.search(r'overbust|cup|bustier|dress', n) else ' and the bust'), 'steel- or spiral-boned, tightly cinched at the waist, adjustable by the lacing')
    kind, front, back, cov, unc, fit = h if h else ('item', 'a front that matches the style of the garment', 'a matching back', 'the area the garment is made to cover', 'what lies outside its shape', 'cut to its style')
    F = [front]; B = [back]; C = [cov]; U = [unc]; X = [fit]
    # necklines and straps
    if has(n, 'plunging', 'plunge', 'deep-v', 'deep v'): F.append('a deep plunging neckline'); U.append('the upper chest')
    elif has(n, 'v-neck', 'v neck'): F.append('a V-shaped neckline')
    elif has(n, 'halter'): F.append('a halter neck tied or fastened behind the neck'); U.append('the shoulders and upper back')
    elif has(n, 'strapless', 'bandeau', 'tube'): F.append('no shoulder straps'); U.append('the shoulders')
    elif has(n, 'off-the-shoulder', 'off the shoulder', 'bardot'): F.append('a neckline sitting off the shoulders'); U.append('the shoulders')
    elif has(n, 'high-neck', 'high neck', 'turtleneck', 'mandarin', 'mock'): F.append('a high collar around the neck')
    elif has(n, 'scoop'): F.append('a scooped neckline')
    elif has(n, 'sweetheart'): F.append('a sweetheart neckline')
    if has(n, 'sleeveless'): F.append('no sleeves'); U.append('the arms')
    elif has(n, 'long-sleeved', 'long sleeve', 'long-sleeve'): F.append('sleeves to the wrists'); C.append('the arms')
    elif has(n, 'short-sleeved', 'short sleeve', 'cap sleeve'): F.append('short sleeves'); C.append('the upper arms')
    elif has(n, 'bell sleeve', 'bishop', 'puff', 'balloon sleeve'): F.append('full, gathered sleeves'); C.append('the arms')
    # back
    if has(n, 'backless', 'open-back', 'open back', 'low back', 'low-back'): B = ['an open back showing most of the back']; U.append('the back')
    elif has(n, 'lace-up back', 'laced back', 'lacing'): B.append('lacing up the centre back')
    elif has(n, 'zip'): B.append('a zip fastening')
    elif has(n, 'button'): B.append('a row of buttons')
    elif has(n, 'racerback'): B.append('straps meeting at a Y-shaped racerback')
    elif has(n, 'x-back', 'criss'): B.append('straps crossing at the back')
    # length
    n_all = n; n = re.sub(r'(long|short|three-quarter|cap)[- ]sleeve[sd]?', '', n)
    n = re.sub(r'\b(long|short)[- ](busk|torso|line|bodice|neck|waist|cuff|train|tail|fringe|tassel|ribbon|strap|chain|lace|ties?|sash|boning|collar|placket|zip|hood)s?\b', '', n)
    if has(n, 'mini', 'micro', 'short'): X.append('a short hem high on the thigh'); U.append('most of the legs')
    elif has(n, 'midi', 'knee-length', 'knee'): X.append('a hem at the knee')
    elif has(n, 'maxi', 'floor-length', 'floor length', 'full-length', 'full length', 'ankle-length', 'long'): X.append('a hem falling to the ankles or floor'); C.append('the legs')
    elif has(n, 'crop', 'cropped'): X.append('a cropped length ending above the waist'); U.append('the midriff')
    if has(n, 'slit', 'split'): X.append('a slit up the side showing the leg'); U.append('part of the leg')
    if has(n, 'cut-out', 'cutout', 'cut out', 'keyhole', 'window'): F.append('cut-out openings'); U.append('skin through the cut-outs')
    if has(n, 'sheer', 'mesh', 'net', 'fishnet', 'lace', 'chiffon', 'organza', 'tulle', 'gauze', 'transparent', 'see-through'):
        F.append('sheer or open-weave panels'); U.append('the skin seen through the sheer parts')
    if has(n, 'hooded', 'hood'): F.append('an attached hood'); C.append('the head')
    if has(n, 'belted', 'belt', 'sash', 'cinch', 'tie waist'): X.append('a defined waist with a belt or sash')
    if has(n, 'pocket'): F.append('pockets')
    if has(n, 'oversized', 'loose', 'baggy', 'relaxed', 'flowing'): X.append('a loose, roomy cut')
    if has(n, 'tight', 'fitted', 'bodycon', 'clinging', 'skin-tight', 'snug'): X.append('a close, body-hugging fit')
    if has(n, 'pleated'): X.append('pleats')
    if has(n, 'ruffle', 'ruffled', 'frill', 'flounce'): F.append('ruffles or frills')
    if has(n, 'fringe', 'fringed'): F.append('swinging fringe')
    if has(n, 'sequin', 'beaded', 'rhinestone', 'studded', 'spiked'): F.append('shiny embellishment across the surface')
    n = n_all
    if kind == 'top' and has(n, 'mini', 'micro', 'maxi', 'midi'): pass
    Cs = ' '.join(C)
    if 'the legs' in Cs: U = [u for u in U if 'legs' not in u]
    if 'the arms' in Cs: U = [u for u in U if u != 'the arms' and u != 'the arms and the lower legs']
    if kind == 'outer': U = [u for u in U if 'on its own' not in u] or ['whatever lies below its hem']
    if not U: U = ['only the parts outside its shape']
    def j(x): x = list(dict.fromkeys(x)); return x[0] if len(x) == 1 else ', '.join(x[:-1]) + ' and ' + x[-1]
    return f"Front: {j(F)}. Back: {j(B)}. It covers {j(C)}, and leaves {j(U)} uncovered. Cut and fit: {j(X)}"
