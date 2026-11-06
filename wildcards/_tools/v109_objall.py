"""v109 - one object builder for every kind of object named in the Location Inventory (user 2026-11-06).
Each object kind (grouped by its head noun across the items, furniture, installed, incidental, signature and traces fields of all 1,422 records) gets
ob_<noun>_type     the document's own phrases for that object (cleaned by the v109_loc text, negation, brand and measurement rules)
ob_<noun>_material materials named with that object in the document, else its material class pool
ob_<noun>_colour / _wear / _detail / _era   shared pools from v75_obj by material class
ob_<noun>_text     (objects that carry text) quoted text from the name-system generators, one line per text with its position
ob_<noun>_short / _phrase / _full
Nouns that already had a builder (v75, v109_obj) keep it. Which head nouns are real objects, and their class and text kind, is decided by reading the
list (data/v109_objall_review.tsv); nothing is guessed silently."""
import os, re, sys, json, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from famlib import P
import v75_obj, v109_obj, v109_loc, v109_locparse, v109_locbrands
HERE = os.path.dirname(os.path.abspath(__file__))
REVIEW = os.path.join(HERE, 'data', 'v109_objall_review.tsv')
FIELDS = ('items', 'furniture', 'installed', 'incidental', 'signature', 'human traces')
SPLIT = r'\b(with|on|in|of|from|at|for|by|under|over|behind|beside|against|left|still|and|or|to|that|which|where|hung|pinned|leaning|set|propped|stacked|full|half|kept|folded|taped|clipped|rolled|dropped|coiled|bolted|parked|caught|laid|fixed)\b'
MATWORDS = {'metal': r'steel|iron|brass|copper|alumin\w*|chrome|chromed|tin|zinc|bronze|pewter|galvani[sz]ed|metal|wire|enamelled steel',
            'wood': r'wood|wooden|oak|pine|timber|plywood|ply|teak|mahogany|walnut|beech|ash|birch|bamboo|wicker|cane|rattan|deal|elm|cedar',
            'plastic': r'plastic|vinyl|acrylic|nylon|rubber|polypropylene|pvc|melamine|laminate|resin|fibreglass|fiberglass|polystyrene|foam',
            'paper': r'paper|card|cardboard|newsprint|parchment',
            'textile': r'cloth|cotton|wool|woollen|woolen|linen|canvas|fabric|felt|leather|velvet|silk|hessian|denim|tweed|knitted|quilted|suede',
            'glass': r'glass|ceramic|china|porcelain|stoneware|earthenware|enamel|terracotta|pottery|crystal',
            'fabricated': r'concrete|stone|brick|tile|tiled|plaster|marble|granite|slate|cast stone|terrazzo|cob'}
MATRX = {k: re.compile(r'\b(' + v + r')\b', re.I) for k, v in MATWORDS.items()}
CLS = {'M': 'metal', 'W': 'wood', 'P': 'plastic', 'R': 'paper', 'T': 'textile', 'G': 'glass', 'A': 'appliance', 'F': 'fabricated'}
# Text kinds: how text appears on the object, always quoted, from the name system (NAME_SYSTEM.txt).
TEXT = {
 'sign': ['reading "__name_shop__"', 'reading "__name_town__"', 'reading "__name_company__"', 'reading "__name_cafe__"'],
 'label': ['with a small label reading "__name_brand__"', 'with a label reading "__name_brand__" on the first line and "__name_product_type__" on the second line'],
 'product': ['with a label reading "__name_brand__" on the first line and "__name_weight__" on the second line', 'with a printed label reading "__name_brand__"'],
 'book': ['with "__name_book_title_any__" on the cover', 'with "__name_book_title_any__" on the spine'],
 'newspaper': ['with the masthead "__name_newspaper__" and the headline "__name_headline__"'],
 'magazine': ['with the title "__name_magazine__" across the top of the cover'],
 'poster': ['reading "__name_movie__" in large letters', 'reading "__name_band__" on the first line and "__name_town__" on the second line'],
 'ticket': ['printed with "__name_town__" on the first line and "__name_number_small__" on the second line'],
 'receipt': ['printed with "__name_shop__" at the top and "__name_price__" at the bottom'],
 'menu': ['listing __text_menu_item__ on the first line and __text_menu_item__ on the second line'],
 'card': ['printed with "__name_person__"', 'printed with "__name_company__" on the first line and "__name_person__" on the second line'],
 'badge': ['printed with "__name_person__"', 'printed with "__name_first__"'],
 'certificate': ['printed with "__name_person__" in large script'],
 'map': ['with the title "__name_town__" across the top'],
 'calendar': ['showing "__name_year__" across the top'],
 'record': ['with "__name_album__" on the first line and "__name_band__" on the second line'],
 'plate': ['reading __text_plate__'],
 'plaque': ['reading "__name_person__" on the first line and "__name_year__" on the second line'],
 'notice': ['reading "__name_hours__"', 'reading __text_notice__'],
 'cover': ['with "__name_company__" on the cover'],
 'score': ['showing "__name_town__" on the first line and "__name_number_small__" on the second line'],
}
COUNTED = r'(?:a |an |the |one |two |three |four |several |some )?(?:pair|pairs|set|sets|stack|stacks|pile|piles|row|rows|bundle|bundles|collection|heap|bunch|handful|couple|scatter|layer|line|lot|lots|number|range|selection|assortment|array|cluster|tangle|drift|clutter|few|dozen|string|chain) of '
def nounphrase(p):
    p = p.lower().strip()
    p = re.sub(r'^' + COUNTED, '', p)
    np = re.split(SPLIT, p)[0].strip()
    return re.sub(r"[^a-z' -]", '', np).strip()
STRIP = re.compile(r"\b(a|an|the|one|two|three|four|five|six|several|some|many|few|its|their|his|her|our|this|that|these|those|old|new|newer|older|worn|broken|battered|dented|rusty|rusted|chipped|dusty|faded|cracked|dirty|clean|empty|full|half-empty|used|unused|spare|cheap|plain|little|small|large|big|tiny|huge|tall|short|long|heavy|light|single|odd|stray|loose|lone|lost|abandoned|discarded|forgotten|dropped|leftover|left|good|best|fine|nice|ugly|old-fashioned|modern|vintage|antique|original|period|replacement|matching|mismatched|assorted|various|other|extra|second|third|last|first|neat|tidy|messy|scattered|sagging|stained|scratched|peeling|warped|bent|burnt|scorched|chewed|torn|ripped|frayed|half|whole|entire|own|same|cold|hot|warm|wet|damp|dry|new-looking|well-used|much-used|polished|painted|unpainted|varnished|lacquered|black|white|grey|gray|red|blue|green|yellow|orange|brown|pink|purple|cream|beige|silver|gold|golden|navy|dark|pale|bright|faded)\b", re.I)
def head(p):
    np = nounphrase(p)
    if not np: return None
    w = re.sub(r"'s$", '', np.split()[-1]); s = re.sub(r'ies$', 'y', w); s = re.sub(r'(ches|shes|xes|sses)$', lambda m: m.group(1)[:-2], s); s = re.sub(r'(?<!s)s$', '', s)
    return s if len(s) > 2 else None
def phrases_by_head():
    H = collections.defaultdict(list)
    for r in v109_locparse.parse():
        for k, v in r['f'].items():
            if not k.startswith(FIELDS): continue
            for ph in v109_loc.split_commas(v109_locbrands.debrand(v)):
                ph = ph.strip()
                if ph and len(ph) <= 160:
                    h = head(ph)
                    if h: H[h].append(ph)
    return H
def load_review(path=REVIEW):
    R = {}
    if not os.path.exists(path): return R
    for l in open(path, encoding='utf8'):
        l = l.rstrip('\n')
        if not l or l.startswith('#'): continue
        noun, cls, text = (l.split('\t') + ['', ''])[:3]
        R[noun] = (cls, text)
    return R
BADMOD = re.compile(r"\b(facing|showing|reading|holding|carrying|leaning|below|above|as|under|over|into|onto|through|near|beside|behind|between|holding|run|down|up|out|off|mark|marks|room|box|area|side|end|top|bottom|front|back|left|right|centre|center|middle|inside|outside|nine|ten|eleven|twelve|competing|aid|planted|concealed|blackened|deadline|specification|supplier|property|scorch|wax|bike|service|parts|rear|its|it|is|are|was|were|has|have|had|very|most|more|less|only|just|also|even|still|then|now|there|here|where|when|while|which|who|what|whose)\b", re.I)
GOODED = {'insulated', 'padded', 'laminated', 'framed', 'wired', 'mounted', 'wall-mounted', 'quilted', 'reinforced', 'heated', 'refrigerated', 'motorised', 'motorized', 'hinged', 'lidded', 'handled', 'fitted', 'built-in', 'boxed', 'striped', 'checked', 'pleated', 'embroidered', 'beaded', 'studded', 'fringed', 'hooded', 'lined', 'enamelled', 'glazed', 'battery-powered', 'hand-held', 'handheld', 'coin-operated', 'flat-packed', 'flat-pack'}
MATALL = re.compile(r'\b(' + '|'.join(MATWORDS.values()) + r')\b', re.I)
def form_and_material(p, noun):
    """'an old stovetop kettle in the booth' -> ('stovetop kettle', None); 'a cracked ceramic mug' -> ('mug', 'ceramic')."""
    np = nounphrase(p)
    if not np: return None, None
    words = np.split()
    last = words[-1]
    mods = ' '.join(words[:-1])
    mat = None
    near = ' '.join(words[-3:-1])
    m = MATALL.search(near)
    if m: mat = m.group(1).lower()
    mods = MATALL.sub(' ', mods); mods = STRIP.sub(' ', mods)
    mods = re.sub(r"\b\w+-(?:coloured|colored|toned|handled)\b", ' ', mods)
    mods = re.sub(r'\s+', ' ', mods).strip(" -'")
    if len(mods.split()) > 2 or re.search(r"'s?$|\d", mods) or BADMOD.search(mods) or any(w.endswith('ed') and w not in GOODED for w in mods.split()) or any(re.search(r'[^su]s$', w) and len(w) > 3 for w in mods.split()): mods = ''
    form = (mods + ' ' + noun).strip() if mods else noun
    return form, mat
def clean_type(p, texty):
    p = re.sub(r'\s+', ' ', p).strip().rstrip('.').strip()
    if v109_loc.NEG.search(p) or v109_loc.MEASURE.search(p) or v109_loc.META.search(p) or v109_loc.KIDPERSON.search(p) or v109_loc.BRANDS.search(p) or v109_loc.CLAUSE.search(p): return None
    if not texty and v109_loc.TEXTY.search(p): return None
    if texty and re.search(r'\b(reading|says|saying|printed with|headed|titled|marked)\b', p): return None
    if not re.match(r'(?i)(a|an|the|one|two|three|four|several|some|old|new|\w+)\b', p): return None
    return p[0].lower() + p[1:]
SUBSTANCE = {'shampoo': 'a bottle of', 'toothpaste': 'a tube of', 'talc': 'a tin of', 'hairspray': 'a can of', 'deodorant': 'a can of', 'aftershave': 'a bottle of',
             'de-icer': 'a can of', 'sunscreen': 'a bottle of', 'polish': 'a tin of', 'disinfectant': 'a bottle of', 'bleach': 'a bottle of', 'lotion': 'a bottle of'}
RESERVED = {'metal', 'wood', 'plastic', 'paper', 'textile', 'glass', 'appliance', 'fabricated', 'colour', 'era', 'any', 'names', 'v109all', 'v109'}
RENAME = {'paper': 'paper_sheet', 'glass': 'drinking_glass'}
MATNOUN = {'wooden': 'wood', 'woollen': 'wool', 'woolen': 'wool', 'knitted': 'knitted wool', 'quilted': 'quilted cotton', 'tiled': 'glazed tile', 'galvanised': 'galvanised steel',
           'galvanized': 'galvanized steel', 'chromed': 'chrome', 'ply': 'plywood', 'deal': 'deal pine', 'cane': 'woven cane', 'wire': 'wire mesh', 'card': 'card stock',
           'enamel': 'enamelled metal', 'china': 'bone china', 'crystal': 'cut crystal', 'cast stone': 'cast stone', 'tin': 'tinplate', 'cob': 'cob earth'}
def build(final=None, review=None):
    review = load_review() if review is None else review
    H = phrases_by_head(); G = {}; names = []
    have = set(v75_obj.build()['ob_names']) | set(v109_obj.build()['ob_v109_names'])
    for noun, (cls, text) in sorted(review.items()):
        if cls in ('', 'X') or noun in have or noun not in H: continue
        key = re.sub(r'[^a-z0-9]+', '_', noun).strip('_')
        key = RENAME.get(key, key + '_item' if key in RESERVED else key)
        texty = bool(text)
        forms = collections.Counter(); mats = collections.Counter()
        for p in H[noun]:
            if v109_loc.NEG.search(p) or v109_loc.BRANDS.search(p) or v109_loc.KIDPERSON.search(p) or v109_loc.SENSORY.search(p): continue
            f, m = form_and_material(p, noun)
            if f and not v109_loc.TEXTY.search(f.replace(noun, '')) and not v109_loc.ADULT.search(f.replace(noun, '')) and (texty or f == noun or not v109_loc.TEXTY.search(f)): forms[f] += 1
            if m: mats[m] += 1
        if noun == 'glass': forms = collections.Counter({f: c for f, c in forms.items() if f == 'glass' or re.search(r'\b(wine|water|pint|shot|cocktail|beer|champagne|whisky|whiskey|sherry|port|brandy|drinking|tall|highball|tumbler|half-pint|gin|juice|milk|tea|beaker)\b', f)})
        if noun in SUBSTANCE: types = ['%s %s' % (SUBSTANCE[noun], f) for f, _ in forms.most_common(30)] or ['%s %s' % (SUBSTANCE[noun], noun)]
        else: types = ['%s %s' % (v109_loc.article(f), f) for f, _ in forms.most_common(30)] or ['%s %s' % (v109_loc.article(noun), noun)]
        c = CLS[cls]
        G['ob_%s_type' % key] = types
        G['ob_%s_material' % key] = list(dict.fromkeys(MATNOUN.get(m, m) for m, _ in mats.most_common(10))) + (['__ob_%s_mat__' % c] if len(mats) < 4 else [])
        G['ob_%s_wear' % key] = ['__ob_%s_wear__' % c]; G['ob_%s_detail' % key] = ['__ob_%s_detail__' % c]; G['ob_%s_era' % key] = v75_obj.ERA
        G['ob_%s_short' % key] = ['__ob_%s_type__, in __ob_colour__' % key]
        G['ob_%s_phrase' % key] = ['__ob_%s_type__ in __ob_colour__' % key]
        full = '__ob_%s_type__, in __ob_colour__, made of __ob_%s_material__, __ob_%s_era__, __ob_%s_wear__, with __ob_%s_detail__' % (key, key, key, key, key)
        if texty:
            G['ob_%s_text' % key] = TEXT[text]
            G['ob_%s_short' % key] = ['__ob_%s_type__, in __ob_colour__, __ob_%s_text__' % (key, key)]
            G['ob_%s_phrase' % key] = ['__ob_%s_type__ in __ob_colour__, __ob_%s_text__' % (key, key)]
            full = full + ', __ob_%s_text__' % key
        G['ob_%s_full' % key] = [full]
        names.append(key)
    G['ob_v109all_names'] = names
    return G
