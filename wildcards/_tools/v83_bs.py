"""v83 - brand style wildcards: 'In the style of <Company>, <distilled style>'. Real company names live only in maker_ files."""
import os, sys, re, glob
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from famlib import slug
HERE = os.path.dirname(os.path.abspath(__file__))
FINAL = '/home/claude/w/wildcards'
def clean(t):
    t = t.replace(':', ' -').replace(';', ',').replace('{', '').replace('}', '').replace('|', ' ').replace('__', '_').replace('"', "'")
    return re.sub(r'\s+', ' ', t).strip()
def era_bucket(e):
    m = re.search(r'(1[0-9]{3}|20[0-9]{2})', e)
    if m: y = int(m.group(1))
    elif re.search(r'(\d+)(st|nd|rd|th) century', e): y = (int(re.search(r'(\d+)(st|nd|rd|th) century', e).group(1)) - 1) * 100
    else: y = 2000
    if 'ancient' in e.lower() or 'medieval' in e.lower(): y = min(y, 1500)
    return 'before_1900' if y < 1900 else '1900_1945' if y < 1946 else '1946_1979' if y < 1980 else '1980_present'
def load():
    B = []; seen = set()
    for fn in sorted(glob.glob(HERE + '/v83_bs_*.py')):
        ns = {}
        exec(open(fn, encoding='utf8').read(), ns)
        grp = os.path.basename(fn)[7:-3]
        for name, region, era, ind, text in ns['B']:
            key = slug(name)
            if key in seen: continue
            seen.add(key)
            t = clean(text)
            if not t.lower().startswith('in the style of'): t = 'In the style of %s, %s' % (name, t)
            B.append((clean(name), region, era, ind, t, grp))
    ES = {}
    for fn in (sorted(glob.glob(HERE + '/data/v83_es/out_*.py')) + sorted(glob.glob(HERE + '/data/v83_es/out2_*.py')) + sorted(glob.glob(HERE + '/data/v83_es/out3_*.py')) + sorted(glob.glob(HERE + '/data/v83_es/out4_*.py')) + sorted(glob.glob(HERE + '/data/v83_es/out5_*.py')) + sorted(glob.glob(HERE + '/data/v83_es/out6_*.py')) + sorted(glob.glob(HERE + '/data/v83_es/out7_*.py')) + sorted(glob.glob(HERE + '/data/v83_es/out8_*.py'))):
        ns = {}; exec(open(fn, encoding='utf8').read(), ns)
        for name, region, era, ind, text in ns['B']: ES[slug(name)] = re.sub(r'@@([a-z0-9_]+)@@', r'__\1__', clean(re.sub(r'__([a-z0-9_]+)__', r'@@\1@@', text)))
    return [(n, r, e, i, ES.get(slug(n), t), g) for n, r, e, i, t, g in B]

def P(x): return [i.strip() for i in x.split(';') if i.strip()]
SUBJ = {
 'vehicle': 'a two-door coupe; a four-door saloon car; a convertible with the roof down; a small hatchback; a family estate car; a pickup truck; an off-road utility vehicle; a delivery van; a sports car seen from the front corner; a city bus; a motorcycle; a scooter',
 'transport': 'a motorcycle standing on its kickstand; a bicycle leaning on a wall; a small propeller aircraft on a runway; a steam locomotive at a platform; a passenger train carriage; a river boat at a jetty; a tractor in a field; a heavy truck in a lay-by; a rocket on a launch pad; a speedboat on calm water; a city tram; a pair of roller skates',
 'fashion': 'a long coat on a mannequin; a handbag on a table; a pair of shoes on a plinth; a shirt folded flat; a dress on a hanger; a woollen jumper; a pair of trousers; a hat and scarf set; a leather jacket; a pair of boots; a woman in a full outfit standing in a doorway; a man in a full outfit leaning on a wall',
 'tech': 'a desktop radio; a handheld camera; a wristwatch on a cushion; a pair of headphones; a kitchen appliance on a worktop; a power drill on a bench; a portable record player; a desk lamp; a small computer with a keyboard; a games console with two controllers; a telephone; an electric guitar on a stand',
 'home': 'an armchair in a bright room; a dining chair beside a table; a table lamp; a ceramic teapot with cups; a glass vase with flowers; a set of dinner plates; a sofa against a wall; a wall clock; a cooking pot on a hob; a bookshelf with books; a rug on a wooden floor; a set of cutlery',
 'media': 'a lone adventurer standing in a landscape; a small group of friends in a street; a toy on a shelf; a movie-poster style scene with two characters; a book cover with an illustrated scene; a record sleeve with a bold design; a hero beside a creature; a village with a winding road; a character portrait from the chest up; a battle scene with several figures; a quiet kitchen with a cat; a castle on a hill',
 'packaging': 'a bottle on a counter; a tin on a shelf; a chocolate bar with its wrapper; a cafe interior with a counter; a shop front on a street; a cosmetics jar and box; a snack packet; a row of cans; an aircraft cabin interior; a hotel lobby; a gift box with tissue paper; a restaurant table set for two',
 'heritage': 'a handmade vase; a woven textile hanging on a wall; a pen on a writing desk; a musical instrument on a stand; a set of tea bowls; a carved wooden box; a printed page from a book; a metal jug and basin; a framed pattern tile; a piece of jewellery on velvet; a pair of ceramic figures; a folded rug',
 'modern_misc': 'a pair of trainers; a backpack on a rock; a camping stove on a table; a train station platform; a street sign on a pole; a stamp-like poster design; a metro entrance; a water bottle; a jacket on a hook; a stadium seen from the stands; a postal van; a bicycle helmet',
 'any': 'a chair; a jacket; a kettle; a car parked on a street; a shop front; a bowl and a cup; a lamp on a table; a bag on a bench; a pair of shoes; a packet of food; a clock on a wall; a person standing in a doorway',
}
GROUP_SUBJ = {'cars_eu': 'vehicle', 'cars_world': 'vehicle', 'transport': 'transport', 'fashion_eu': 'fashion', 'fashion_world': 'fashion', 'tech': 'tech', 'home': 'home', 'media': 'media', 'packaging': 'packaging', 'heritage': 'heritage', 'modern_misc': 'modern_misc'}
VIEW = P('shown in a clean studio photograph with soft even light; shown in natural daylight; shown in soft window light; shown on a plain pale backdrop with a soft shadow; shown in a detailed close-up that fills the frame; shown as a full view of the whole object; shown at a three-quarter angle with a softly blurred background; shown centred with plenty of empty space around it; shown in warm late-afternoon sun with long gentle shadows; shown in cool overcast light on a pale grey surface; shown under a single warm lamp with the background fading to dark; shown from slightly above on a plain wooden table; shown from a low angle against a clear sky; shown in bright morning light with a crisp shadow beside it; shown in the glow of early evening with a softly lit background; shown on a plain painted wall in even daylight; shown from the side in a simple profile view; shown straight on, centred and symmetrical; shown in dappled light through leaves; shown beside a window on a cloudy day; shown on a plain concrete floor in cool even light; shown against a deep solid colour backdrop with a gentle rim light; shown from above in a flat lay on a neutral surface; shown in warm gallery lighting on a simple plinth')
NOTEXT = 'The surfaces are plain and unmarked, and the style is carried by colour, shape, material and pattern alone.'
TEXTRE = re.compile(r'\b(wordmarks?|logos?|lettering|lettered|capitals?|capital letters|uppercase|lowercase|fine print|tiny text|slogans?|typefaces?|typography|serif|sans-serif|italic|monograms?|signage|text|words?|wording|initials|script|calligraphy|legends?|captions?|titles?|headlines?|names?|numerals?|numbers?|digits?|figures|numbered|badges?|tags?|labels?|signs?|banners?|emblems?|crests?|insignia|stamps?|seals?|plaques?|placards?|posters?|billboards?|stickers?|patches)\b', re.I)
MOOD_START = re.compile(r'^(Photography|Photographs?|Photos?|Imagery|Graphic advertising|Advertising|Advertisements?|Graphics|Campaigns?|Layouts?|Ads?|Print ads?|Posters?|Shop|Stores?|Interiors?|Storefronts?|Settings?|Scenes?|Film|Films|Cinematography|Lighting|Mood)\b')
MOOD_ANY = re.compile(r'\b(photograph\w*|backdrops?|campaigns?|advertis\w*|storefronts?|cinematic|camera|shot low|photos?|ramps?|graffiti|landscapes?|interiors?|showrooms?|skate-park|street-level|pubs?|cafes?|kitchens?|crowds?|models?|city streets?|shopfronts?|scenes?|settings?|rooms?)\b', re.I)
OBJRE = re.compile(r"\b(shoes?|sneakers?|trainers?|boots?|soles?|laces?|eyelets?|toe caps?|heels?|cars?|coupes?|saloons?|sedans?|estates?|hatchbacks?|vehicles?|lorr(?:y|ies)|trucks?|vans?|buses|bus|trams?|trains?|locomotives?|carriages?|aircraft|aeroplanes?|airliners?|jets?|ships?|boats?|yachts?|bonnets?|grilles?|bumpers?|headlamps?|headlights?|wheels?|tyres?|tires?|fenders?|wings|tail fins?|dashboards?|cabins?|engines?|bicycles?|bikes?|motorcycles?|scooters?|handbags?|purses?|wallets?|watch(?:es)?|cameras?|lenses|radios?|televisions?|computers?|keyboards?|telephones?|phones?|bottles?|cans?|packets?|jars?|tins?|cartons?|chairs?|sofas?|tables?|desks?|lamps?|kettles?|toasters?|stores?|shops?|shopfronts?|storefronts?|forecourts?|pumps?|petrol|stations?|terminals?|restaurants?|cafes?|kitchens?|jackets?|coats?|dresses|skirts?|trousers|jeans|shirts?|t-shirts?|knitwear|hats?|caps?|gloves?|scarves|scarf|bags?|backpacks?|rucksacks?|luggage|suitcases?|toys?|dolls?|figures?|consoles?|controllers?|joysticks?|typewriters?|records?|cameras?|film)\b", re.I)
def obj_clean(body):
    sents = re.split(r'(?<=[.])\s+', body.strip())
    keep = [x for x in sents if not OBJRE.search(x)]
    if len(' '.join(keep).split()) >= 30: return ' '.join(keep), True
    return body, False
def clean_sents(sents):
    out = []
    for x in sents:
        if TEXTRE.search(x):
            allp = re.split(r',\s+', x.rstrip('.'))
            if TEXTRE.search(allp[0]): continue
            parts = [q for q in allp if not TEXTRE.search(q)]
            if len(' '.join(parts).split()) < 5: continue
            x = ', '.join(parts) + '.'
            x = re.sub(r',\s+(and|or)\s*\.$', '.', x)
        out.append(x)
    return out
def split_mood(t):
    sents = re.split(r'(?<=[.])\s+', t.strip()); obj = []; mood = []
    for j, x in enumerate(sents):
        (mood if j and ( (MOOD_START.match(x) or MOOD_ANY.search(x))) else obj).append(x)
    if len(' '.join(obj).split()) < 45: return ' '.join(clean_sents(sents)).strip(), ''
    return ' '.join(clean_sents(obj)), ' '.join(mood)
def build(final=None):
    B = load(); G = {}
    B = [(x[0], x[1], x[2], x[3], split_mood(x[4])[0], x[5], split_mood(x[4])[1]) for x in B]
    MOOD = {x[0]: x[6] for x in B}; B = [x[:6] for x in B]
    NAT = re.compile(r'^(American|British|English|Finnish|Swedish|Danish|Norwegian|Italian|French|German|Dutch|Swiss|Japanese|Chinese|Korean|Indian|Mexican|Russian|Soviet|Scandinavian|Nordic|Victorian|Edwardian|Georgian|Art|Bauhaus|Mid|Hungarian|Czech|Polish|Turkish|Persian|Iranian|Ottoman|Islamic|African|Brazilian|Peruvian|Australian|Canadian|Thai|Vietnamese|Indonesian|Balinese|Spanish|Portuguese|Greek|Irish|Scottish|Welsh|Austrian|Belgian)\b')
    LOW = set(w for x in B for w in re.findall(r'[a-z]+', x[4]))
    def unnamed(n, t):
        body = t[len('In the style of ' + n):].lstrip(' ,.') if t.startswith('In the style of ' + n) else re.sub(r'^In the style of [^,.]*[,.]\s+', '', t)
        body = obj_clean(body)[0]
        HEADS = re.match(r'^(Palette|Materials?|Surfaces|Forms?|Shapes?|Colou?rs?|Finishes|Details)\b', body)
        if not NAT.match(body) and not HEADS: body = body[0].lower() + body[1:]
        for part in sorted({n} | {p for p in re.split(r'[ -]+', n) if len(p) > 3}, key=len, reverse=True):
            if part != n and (part.lower() in LOW or NAT.match(part)): continue
            body = re.sub(r'(?<![A-Za-z])' + re.escape(part) + r'(?![A-Za-z])', 'this brand', body)
        body = re.sub(r' this brand (red|blue|green|yellow|orange|pink|gold|brown|black|white)', r' \1', body)
        body = body.rstrip(' ,;')
        if not body.endswith('.'): body += '.'
        return ('Styled in a design language. ' if HEADS else ('Styled after ' if re.match(r'(?i)(a|an|the)\b', body) else 'Styled in a design language of ')) + body + ' ' + NOTEXT + ' This styling applies to the object itself and not to its surroundings.'
    def core(n, t):
        u = unnamed(n, t)
        heads = u.startswith('Styled in a design language. ')
        b = u
        for p in ('Styled in a design language. ', 'Styled after ', 'Styled in a design language of '):
            if b.startswith(p): b = b[len(p):]; break
        b = b.replace(' ' + NOTEXT, '').replace(' This styling applies to the object itself and not to its surroundings.', '')
        return heads, b
    U = {x[0]: unnamed(x[0], x[4]) for x in B}
    # plain name = style only (brand name not included), _named = starts with 'In the style of <Brand>,'
    for name, region, era, ind, t, grp in B:
        G['maker_bs_' + slug(name)] = [U[name]]
        G['maker_bs_' + slug(name) + '_named'] = [U[name]]  # same text: the file name carries the brand, the prompt does not
        _m = ' '.join(clean_sents(re.split(r'(?<=[.])\s+', MOOD[name].strip()))) if MOOD[name] else ''
        if _m: G['maker_bs_' + slug(name) + '_mood'] = [_m]
    MK = 'The style is carried by colour, shape, material and line work.'
    G['maker_brand_style_marked'] = [U[x[0]].replace(NOTEXT, MK) for x in B]
    def agg(key, rows):
        G['maker_brand_style' + key] = [U[x[0]] for x in rows]
        G['maker_brand_style' + key + '_named'] = [U[x[0]] for x in rows]
    agg('', B)
    for grp in sorted({x[5] for x in B}): agg('_' + grp, [x for x in B if x[5] == grp])
    for r in sorted({x[1] for x in B}): agg('_region_' + slug(r), [x for x in B if x[1] == r])
    for e in ('before_1900', '1900_1945', '1946_1979', '1980_present'): agg('_era_' + e, [x for x in B if era_bucket(x[2]) == e])
    for i in sorted({x[3] for x in B}):
        L = [x for x in B if x[3] == i]
        if len(L) >= 4: agg('_industry_' + slug(i), L)
    for name, region, era, ind, t, grp in B:   # enrich thin existing make files
        fn = os.path.join(FINAL, 'maker_%s_style.txt' % slug(name))
        if os.path.exists(fn):
            old = [l.strip() for l in open(fn, encoding='utf8') if l.strip() and '__maker_bs_' not in l]
            G['maker_%s_style' % slug(name)] = old + ['__maker_bs_%s__' % slug(name)]
    for name, region, era, ind, t, grp in B:
        body = t[len('In the style of ' + name):].lstrip(' ,.') if t.startswith('In the style of ' + name) else re.sub(r'^In the style of [^,.]*[,.]\s+', '', t); body = obj_clean(body)[0]; w = body.split()[:40]; cut = ' '.join(w)
        if len(w) >= 40:
            k = cut.rfind('.')
            if k > 90: cut = cut[:k + 1]
            else:
                w = w[:26]; cut = ' '.join(w)
                if ',' in cut: cut = cut[:cut.rfind(',')]
        cut = cut.rstrip(' ,.'); sj = '__bs_subject_%s__' % GROUP_SUBJ.get(grp, 'any')
        _u = unnamed(name, cut); G['bs_cell_' + slug(name)] = ['%s %s' % (sj, _u[0].lower() + _u[1:])]
        G['bs_cell_' + slug(name) + '_named'] = list(G['bs_cell_' + slug(name)])
    BADSUBJ = re.compile(r'\b(person|people|woman|women|man|men|friends|adventurer|hero|characters?|crowd|child|children|riders?|driver|passengers?|interior|cabin|lobby|platform|stadium|landscape|street|shop front|storefront|station|entrance|room|rooms|runway|cafe|scene|parked|port|harbour|hangar|garage|showroom|kitchen interior|stands|field|kiosk|stall|shop|fuel|railway|museum|shelter|postal|poster|cover|sleeve|page|sign|cinema|theatre|market|station)\b', re.I)
    for k, v in SUBJ.items(): G['bs_subject_' + k] = P('; '.join(x.strip() for x in v.split(';') if x.strip() and not BADSUBJ.search(x)))
    BUILD = 'a windmill; a two-storey house seen from the front; a stone cottage; a gatehouse with a pitched roof; a small chapel; a lighthouse; a clock tower; a garden pavilion; a tall narrow townhouse; a greenhouse; a lakeside cabin; a boathouse; a barn; a bandstand; a dovecote; a bridge-keeper\'s lodge'
    ACC = 'a leather belt; a pair of sunglasses; a wallet; a hat; a pair of gloves; a scarf; a tote bag; an umbrella; a backpack; a pair of earrings; a wristwatch on a cushion; a keyring; a phone case; a water bottle; a lunch box; a pair of socks'
    VEH = 'a made-up two-door coupe; an imaginary delivery van; a fictional motorcycle; a made-up bus; an imaginary tram; a fictional bicycle; a made-up small aircraft; an imaginary boat; a fictional tractor; a made-up sports car; an imaginary scooter; a fictional lorry'
    G['bs_subject_building'] = P(BUILD); G['bs_subject_accessory'] = P(ACC); G['bs_subject_madeup_vehicle'] = P(VEH)
    G['bs_subject_any'] = P('; '.join(x.strip() for x in SUBJ['any'].split(';') if x.strip() and not BADSUBJ.search(x)) + '; ' + BUILD + '; ' + ACC + '; ' + VEH)
    G['bs_view'] = VIEW
    grps = sorted({x[5] for x in B})
    import random as _rnd
    def noun(sj): return 'the ' + re.sub(r'^(a|an)\s+', '', re.sub(r' (on|in|at|beside|against|with|seen|leaning|standing|from|set) .*$', '', sj))
    def Cap(x): return x[0].upper() + x[1:]
    def objline(name, t, sj, mark=False):
        heads, body = core(name, t)
        head = Cap(sj) + (' done in a design language. ' if heads else ' done in a design language of ') + body
        return head + (' __bs_mark__' if mark else '') + ' Only that design language is used for %s, in a plain neutral setting, __bs_view__.' % noun(sj)
    POOL = {k: [x for x in G['bs_subject_' + k]] for k in list(SUBJ) + ['building', 'accessory', 'madeup_vehicle']}
    POOL['mark'] = [x for x in G['bs_subject_any'] if x not in set(BUILD.split('; ')) | set(VEH.split('; '))]
    NEUTRAL = {x[0] for x in B if obj_clean(re.sub(r'^In the style of [^,.]*[,.]\s+', '', x[4]))[1]}
    print('object-neutral styles', len(NEUTRAL))
    for g in grps:
        L = []
        for name, region, era, ind, t, grp in B:
            if grp != g: continue
            if GROUP_SUBJ.get(grp, 'any') == 'any' and name not in NEUTRAL: continue
            pool = POOL[GROUP_SUBJ.get(grp, 'any')]; r = _rnd.Random(slug(name)); k = min(6, len(pool))
            L += [objline(name, t, sj) for sj in r.sample(pool, k)]
        G['bs_obj_' + g] = L
    for kind in ('building', 'accessory', 'madeup_vehicle'):
        L = []
        for name, region, era, ind, t, grp in B:
            if name not in NEUTRAL: continue
            r = _rnd.Random(slug(name) + kind); L += [objline(name, t, sj) for sj in r.sample(POOL[kind], 3)]
        G['bs_objk_' + kind] = L
    L = []
    for name, region, era, ind, t, grp in B:
        if name not in NEUTRAL: continue
        r = _rnd.Random(slug(name) + 'mk'); L += [objline(name, t, sj, True) for sj in r.sample(POOL['mark'], 3)]
    G['bs_objm'] = L
    for name, region, era, ind, t, grp in B:
        if slug(name) == 'converse':
            r = _rnd.Random('conv'); pool = POOL['mark']
            G['bs_obj_converse'] = [objline(name, t, sj) for sj in r.sample(pool, min(12, len(pool)))]
            G['bs_objm_converse'] = [objline(name, t, sj, True).replace('__bs_mark__', '__maker_bs_converse_mark__') for sj in r.sample(pool, min(12, len(pool)))]
    for g in grps:
        for sfx in ('', '_named'): G['bs_%s_prompt%s' % (g, sfx)] = ['__bs_obj_%s__' % g]
    for kind in ('building', 'accessory', 'madeup_vehicle'):
        for sfx in ('', '_named'): G['bs_%s_prompt%s' % (kind, sfx)] = ['__bs_objk_%s__' % kind]
    G['bs_marked_prompt'] = ['__bs_objm__']
    G['bs_prompt'] = ['__bs_%s_prompt__' % g for g in grps] + ['__bs_%s_prompt__' % k for k in ('building', 'accessory', 'madeup_vehicle')]
    G['bs_prompt_named'] = ['__bs_%s_prompt_named__' % g for g in grps] + ['__bs_%s_prompt_named__' % k for k in ('building', 'accessory', 'madeup_vehicle')]
    G['v83_bs_entry_points'] = ['bs_prompt', 'bs_prompt_named', 'bs_marked_prompt', 'maker_brand_style', 'maker_brand_style_named'] + ['bs_%s_prompt' % g for g in grps] + ['bs_building_prompt', 'bs_accessory_prompt', 'bs_madeup_vehicle_prompt', 'bs_building_prompt_named', 'bs_accessory_prompt_named', 'bs_madeup_vehicle_prompt_named']
    return G
if __name__ == '__main__':
    G = build(); print(len(G), len(load()))
