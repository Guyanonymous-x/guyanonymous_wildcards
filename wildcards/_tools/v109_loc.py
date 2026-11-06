"""v109 - full Location Inventory conversion (all 1,422 records of the 350 Locations document, user 2026-11-06), replacing the v75 pilot
(same IDs for the 325 pilot records). Per location loc_<cat>_<name>_*:
  _items, _incidental, _furniture, _installed, _signature, _materials, _palette, _light, _traces, _condition, _time, _region, _sign
  _clean (the place only), _scene (everything), _scene_plus (adds anywhere items), _time_scene, _era_scene, _region_scene, _people.
Text rule: phrases naming printed or written things are dropped; where the record has signage, a _sign pool gives quoted name-system text.
Negated phrases are dropped. 'Dimensions & fit' is never used. Child-related places use adults aged 25 and over in everyday clothing, draw only on
filtered anywhere pools, and are checked for adult vocabulary (CHILD_SAFE_CHECK); no adult_ file references any loc_ file."""
import os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from famlib import slug
import v109_locparse, v109_locbrands
TAGNAMES = ['enclosure', 'access', 'function', 'scale', 'era', 'light', 'occupancy', 'condition', 'climate', 'acoustic', 'materials', 'camera']
NEG = re.compile(r"\b(no|not|never|without|nothing|none|nobody|neither|nor)\b|n't\b", re.I)
TEXTY = re.compile(r"\b(licen[cs]e plates?|number plates?|registration plates?|l plates?|words?|couplets?|scrolls? of|calligraphy|folders?|binders?|reference folders?|manuals?|quotations?|livery|liveries|newsprint|card and paper display|paper displays?|wall displays?|displays? of work|numbered|pages?|workbooks?|exercise books?|digits|rate boards?|brand(?!-new)|brands|receipts?|leaflets?|flyers?|brochures?|tickets?|newspapers?|magazines?|labels?|labell?ed|price tags?|name tags?|name badges?|luggage tags?|stickers?|notices?|posters?|banners?|placards?|charts?|maps?|calendars?|certificates?|diplomas?|letters?|post-it|sticky notes?|notes?|notebooks?|lists?|timetables?|schedules?|directory|directories|business cards?|greetings? cards?|birthday cards?|postcards?|menus?|menu boards?|signs?|signage|signposts?|placards?|plaques?|name ?plates?|nameplate|door plates?|lettering|lettered|inscriptions?|inscribed|logos?|branded|branding|slogans?|wordmarks?|captions?|headlines?|graffiti|writing|written|handwritten|printed|print-?outs?|scrawled|stencilled|stenciled|numbers? painted|whiteboards? with|blackboards? with|chalkboards? with|screens? showing|readouts?|scoreboards?|departure boards?|ledgers?|logbooks?|log books?|forms?|paperwork|documents?|files? of|folders? of|reports?|invoices?|bills?|cheques?|checks? (?:on|in|from)|envelopes?|packets? of|boxes? of|cartons? of|jars? of|tins? of|cans? of|bottles? of|tubes? of)\b", re.I)
SIGNY = re.compile(r"\b(signs?|signage|shop ?front|fascia|name ?plates?|nameplate|door plates?|plaques?|menu boards?|menus?)\b", re.I)
ADULT = re.compile(r"\b(nude|naked|nudity|sex|sexual|sexy|erotic|condoms?|lubricant|lube|lingerie|genitals?|penis|vagina|vulva|breasts?|nipples?|aroused|arousal|fetish|bondage|porn\w*|strip(?:per|pers|tease|ping)?|brothel|escorts?|lap ?dance|adult toys?|sex toys?|vibrators?|dildos?|clients? undress|bedding changed between|punters?|working girls?|condom|whips?|handcuffs?|restraints?)\b", re.I)
CHILD = re.compile(r"\b(child|children|childhood|kids?|nursery|nurseries|playground|play area|playroom|school|classroom|cr[eè]che|toddlers?|bab(?:y|ies)|infants?|pupils?|reception class|primary|secondary|youth|teen\w*|nappy|nappies|changing table|soft play|day ?care|kindergarten|scout|guide hut)\b", re.I)
# Signs: business keyword in the title -> name generator; else the category default.
BUSINESS = [('pub', 'name_pub'), ('bar', 'name_bar'), ('cafe', 'name_cafe'), ('coffee', 'name_cafe'), ('tea room', 'name_cafe'), ('bakery', 'name_bakery'),
            ('butcher', 'name_butcher'), ('pharmacy', 'name_pharmacy'), ('chemist', 'name_pharmacy'), ('book', 'name_bookshop'), ('hotel', 'name_hotel'),
            ('motel', 'name_hotel'), ('inn', 'name_pub'), ('bank', 'name_bank'), ('garage', 'name_garage'), ('gym', 'name_gym'), ('hair salon', 'name_hair_salon'), ('beauty salon', 'name_hair_salon'), ('nail salon', 'name_hair_salon'),
            ('barber', 'name_hair_salon'), ('laundr', 'name_laundromat'), ('cinema', 'name_cinema'), ('arcade', 'name_arcade'), ('record', 'name_record_store'),
            ('tattoo', 'name_tattoo_studio'), ('toy', 'name_toy_shop'), ('flower', 'name_flower_shop'), ('florist', 'name_flower_shop'), ('grocer', 'name_grocery'),
            ('supermarket', 'name_grocery'), ('hardware', 'name_hardware_store'), ('liquor', 'name_liquor_store'), ('off-licence', 'name_liquor_store'),
            ('pawn', 'name_pawn_shop'), ('pizz', 'name_pizzeria'), ('diner', 'name_diner'), ('petrol', 'name_petrol_station'), ('gas station', 'name_petrol_station'),
            ('restaurant', 'name_restaurant'), ('sushi', 'name_restaurant'), ('food', 'name_restaurant'), ('deli', 'name_brand'), ('shop', 'name_brand'), ('store', 'name_brand')]
CATSIGN = {'retail': 'a shop sign reading "__name_brand__"', 'food': 'a sign over the entrance reading "__name_restaurant__"', 'work': 'a door plate reading "__name_company__"',
           'depot': 'a sign on the wall reading "__name_company__"', 'civic': 'a plaque by the door reading "__name_town__"', 'transport': 'a sign reading "__name_town__"',
           'culture': 'a sign over the entrance reading "__name_town__ __loc_venue_word__"', 'health': 'a door sign reading "Room __name_number_small__"',
           'edu': 'a sign by the door reading "__name_surname__ __loc_edu_word__"', 'vice': 'a small sign by the door reading "__name_brand__"',
           'wealth': 'a stone plaque by the gate reading "__name_surname__ __loc_house_word__"', 'outdoor': 'a wooden sign on a post reading "__name_town__"',
           'circ': 'a sign on the wall reading "__loc_circ_word__"', 'odd': 'a weathered sign reading "__name_town__"', 'ext': 'a house number by the door reading "__name_number_small__"',
           'home': 'a framed print reading "__name_town__"', 'bath': 'a sign on the door reading "__loc_bath_word__"', 'vehicle': 'a small plate reading "__name_brand_upper__"',
           'dwelling': 'a hand-painted board reading "__name_surname__"', 'secret': 'a small brass plate reading "__name_surname__"'}
WORDS = {'loc_venue_word': ['Theatre', 'Hall', 'Gallery', 'Museum', 'Playhouse', 'Arts Centre', 'Picture House', 'Concert Hall'],
         'loc_health_word': ['Ward 3', 'Outpatients', 'Radiology', 'Pharmacy', 'Reception', 'Day Unit', 'Clinic 2', 'Physiotherapy'],
         'loc_edu_word': ['Hall', 'Library', 'Building', 'Wing', 'Centre', 'Studio'],
         'loc_house_word': ['House', 'Hall', 'Court', 'Manor', 'Park', 'Lodge'],
         'loc_circ_word': ['Way Out', 'Stairs', 'Lifts', 'Level 2', 'Platforms', 'Reception'],
         'loc_bath_word': ['Toilets', 'Washroom', 'Showers', 'Changing'],
         'loc_person_action': ['standing in the middle of the space', 'walking through the space', 'pausing to look around', 'sitting for a moment',
                               'carrying a cardboard box', 'checking something on a phone', 'leaning against a wall', 'tidying a surface',
                               'talking quietly on a phone', 'looking out of a window', 'opening a cupboard', 'wiping down a counter',
                               'adjusting the lights', 'putting something back in its place', 'waiting near the door', 'stretching after a long shift']}
def clean_phrase(t):
    t = t.replace(' --- ', ', ').replace('---', ', ').replace(' -- ', ', ').replace('--', '-')
    t = re.sub(r',\s*which\b.*$', '', t)
    t = re.sub(r',?\s+(?:because|so that|which makes|which is why|so the|so it|so that the)\b.*$', '', t)
    t = t.replace(' — ', ', ').replace(' – ', ', ').replace('—', ', ').replace('–', '-').replace(':', ' -').replace('→', 'to')
    return re.sub(r'\s+', ' ', t.strip().rstrip('.').strip())
def split_commas(t):
    out, depth, cur = [], 0, ''
    for n, ch in enumerate(t):
        if ch == ',' and 0 < n < len(t) - 1 and t[n - 1].isdigit() and t[n + 1].isdigit(): cur += ch; continue
        if ch == '(': depth += 1
        if ch == ')': depth = max(0, depth - 1)
        if ch == ',' and depth == 0: out.append(cur); cur = ''
        else: cur += ch
    out.append(cur)
    return [deneg(clean_phrase(x)) for x in out if clean_phrase(x)]
def split_semi(t): return [clean_phrase(x) for x in t.split(';') if clean_phrase(x)]
def split_semi_pruned(t, child=False, clause_ok=False):
    """Semicolon parts with any negated or text-bearing comma sub-phrase removed (keeps 'a low pendant over the table' from 'a low pendant over the table, neon sign, no daylight')."""
    out = []
    for part in split_semi(t):
        subs = [x for x in split_commas(part) if keep(x, child, clause_ok)]
        if subs: out.append(', '.join(subs))
    return out
DENEG = re.compile(r"\s*,?\s*\b(?:with|and|but|so|or|while)?\s*\b(?:no|not|never|nothing|without|none)\b.*$", re.I)
def deneg(p):
    """Cut a trailing negated clause ('flat fluorescent with no daylight' -> 'flat fluorescent'); phrases that start negated are left for keep() to drop."""
    q = DENEG.sub('', p).strip().rstrip(',').strip()
    if q and q.split()[-1].lower() in AUX: return p
    return q if q and len(q.split()) >= 2 and q != p else p
AUX = {'do', 'does', 'did', 'can', 'could', 'will', 'would', 'should', 'may', 'might', 'must', 'is', 'are', 'was', 'were', 'has', 'have', 'had', 'that', 'which', 'whose', 'who', 'it', 'they', 'and', 'or', 'but', 'with', 'of', 'to', 'the', 'a', 'an'}
CLAUSE = re.compile(r"\b(changes?|makes?|gives|turns|falls|lands|comes|goes|stays|reads|shows|means|appears|varies|depends|matters|works|needs|seems|looks like|is|are|was|were|which|because|whereas|meaning|so that|has been|have been|it's|there's)\b", re.I)
MEASURE = re.compile(r"\d[\d,.]*\s*(mm|cm|m|km|kg|g|ml|l|°|degrees|ft|in|metres?|meters?|feet|inches|litres?|liters?)\b|\d+\s*[x×]\s*\d+", re.I)
META = re.compile(r'\b(dataset|data set|this group|in this group|this list|this record|records? in|the darkest record|the brightest record|this section|this tab|this record|the record|see record|records? \d+|cross-referenc\w*|this inventory|the inventory)\b', re.I)
KIDPERSON = re.compile(r"\b(child|children|kids?|toddlers?|bab(?:y|ies)|infants?|pupils?|schoolchildren|schoolboys?|schoolgirls?|teen(?:ager)?s?|boys?|girls?|youngsters?|minors?)\b(?!['’]s)", re.I)
BRANDS = re.compile(r"\b(AdBlue|Airstream|Amtrak|Bloomberg|Bluetooth|Dyneema|IKEA|Lamson|Madame Tussauds|Powerlock|RNLI|KNRM|DGzRS|ADAC|Rega|Routemaster|Crown Derby|Rolling Stones|Steenbeck|Truma|UNHCR|Zimmer|Wagons-Lits|Nightjet|TGV|S-Bahn|London Underground|Caledonian Sleeper|Setright|Alde|Aldis|St John Ambulance|Trinity House|Northern Lighthouse Board|Coast Guard|Royal Navy|British Legion|NHS|Forestry Commission|Motorhome Club|Caravanning Club|Mountain Bothies Association|Gideon|Pullman|Formica|Hoover|Tannoy|Portakabin|Velcro|Thermos|Sellotape|Biro|Lego|Jacuzzi|Perspex|Tupperware|Rawlplug|Anglepoise|Dyson|Aga|Belfast sink|Le Creuset|Smeg|Calor|Hornby|Meccano|Monopoly|Scrabble|Coca-Cola|Pepsi|Heinz|Marmite|Guinness)\b")
FRAG = re.compile(r'^(with|for|if|as|than|usually|often|sometimes|always|mostly|rarely|then|also|both|either|plus|perhaps|possibly|each|every|especially|mainly|only|even|still|now|once|so|too|very)\b', re.I)
SENSORY = re.compile(r"\b(smells?|smelling|smelt|scents?|scented|odou?rs?|aromas?|stinks?|stench|whiffs?|reeks?|reek|tastes?|tasting|flavou?rs?|sounds?|noises?|noisy|hums?|humming|buzz\w*|echo\w*|silence|silent|quiet|hushed|creak\w*|rattl\w*|tick\w*|ringing|ringtones?|music playing|chatter\w*|murmur\w*|whirr\w*|drone|droning|hiss\w*|crackl\w*|thud\w*|clatter\w*|clank\w*|beep\w*|bleep\w*|announcements?|audible|loud|muffled|smoky smell|musty|stale air|fragrant|fragrance|perfumed air)\b", re.I)
def keep(p, child, clause_ok=False):
    if SENSORY.search(p): return False
    if FRAG.search(p) or META.search(p) or KIDPERSON.search(p) or BRANDS.search(p): return False
    if MEASURE.search(p): return False
    if not clause_ok and CLAUSE.search(p): return False
    if NEG.search(p) or TEXTY.search(p) or len(p) < 3 or len(p) > 240: return False
    if p.lower().startswith(('none', 'n/a', 'and ', 'or ')): return False
    if child and ADULT.search(p): return False
    return True
LIGHTWORD = re.compile(r'\b(\w*lit|\w*light\w*|overhead|fittings?|fixtures?|tubes?|cast|glow|warm\w*|cool\w*|cold|harsh|soft\w*|flicker\w*|exposed|contrast\w*|amber|orange|blue|green|yellow|white|red|grey|gray|golden|pale|flat|even|ambient|reflect\w*|sky|open|light\w*|lamps?|glow\w*|sun\w*|daylight|bulbs?|fluorescent|LEDs?|windows?|dark\w*|dim\w*|bright\w*|shad\w*|candle\w*|fire\w*|flames?|lit|neon|torch\w*|beams?|lanterns?|spotlights?|downlights?|floodlights?|skylights?|rooflights?|moon\w*|stars?|dusk|dawn|gloom\w*|murk\w*|haze|glare|tungsten|sodium|halogen|strip|pendant|chandelier|sconce|uplight\w*|backlit|glass|overcast|cloud\w*)\b', re.I)
def article(t):
    w = t.lower()
    if re.match(r'(x-ray|mri|mot|sos|fbi|hgv|nhs|rnli|ecg|ent|f1|8|11|18)\b', w): return 'an'
    if re.match(r'(uni[^m]|use|usu|euro|one\b|once|ewe)', w): return 'a'
    return 'an' if w[:1] in 'aeiou' else 'a'
def is_child(r): return r['cat'] == 'edu' or bool(CHILD.search(r['title']))
def sign_for(r):
    t = r['title'].lower()
    for k, gen in BUSINESS:
        stem = k in ('laundr', 'pizz', 'grocer', 'florist', 'pharmac', 'bak')
        if re.search(r'\b' + re.escape(k) + (r'' if stem else r'(?:s|es)?\b'), t): return ['a sign reading "__%s__"' % gen, 'a sign over the door reading "__%s__"' % gen]
    return [CATSIGN[r['cat']]]
def build(final=None):
    G = {}; idx = {}; pools = {k: {} for k in ('items', 'furniture', 'installed', 'traces', 'light')}; child_ids = set()
    recs = v109_locparse.parse()
    for r in recs:
        f = {k2: v109_locbrands.debrand(v2) for k2, v2 in r['f'].items()}; I = r['id']; child = is_child(r)
        def get(*names):
            for n in names:
                for k, v in f.items():
                    if k.startswith(n): return v
            return ''
        k = lambda xs: [x for x in xs if keep(x, child)]
        items = k(split_commas(get('items'))); inc = k(split_commas(get('incidental'))); furn = k(split_commas(get('furniture'))); inst = k(split_commas(get('installed')))
        sig = k(split_commas(get('signature'))); mraw = split_semi_pruned(get('materials'), child); light = [x for x in split_semi_pruned(get('light'), child) if len(x.split()) >= 2 and LIGHTWORD.search(x)]
        trace = k(split_commas(get('human traces'))); cond = split_semi_pruned(get('condition'), child); time = split_semi_pruned(get('time'), child); region = split_semi_pruned(get('regional'), child)
        mats, pal = mraw[:1], mraw[1:2]
        if not (items or furn or inst): print('skipped', I); continue
        has_sign = any(SIGNY.search(x) for x in split_commas(get('items')) + split_commas(get('installed')) + split_commas(get('signature')))
        r = dict(r, title=deneg(v109_locbrands.debrand(r['title'])))
        title = r['title'] if r['title'][1:2].isupper() else r['title'][0].lower() + r['title'][1:]
        for key, vals in (('items', items), ('incidental', inc), ('furniture', furn), ('installed', inst), ('signature', sig), ('materials', mats), ('palette', pal),
                          ('light', light), ('traces', trace), ('condition', cond), ('time', time), ('region', region)):
            if vals: G['%s_%s' % (I, key)] = vals
        if has_sign: G['%s_sign' % I] = sign_for(r)
        if not child and r['cat'] != 'vice':
            for key, vals in (('items', items), ('furniture', furn), ('installed', inst), ('traces', trace), ('light', light)):
                for v in vals: pools[key][v] = pools[key].get(v, 0) + 1
        clean = 'The place is %s %s.' % (article(title), title)
        if mats: clean += ' Its materials are __%s_materials__' % I + (', and the palette is __%s_palette__' % I if pal else '') + '.'
        elif pal: clean += ' The palette is __%s_palette__.' % I
        clean += ' The light is __%s__.' % (('%s_light' % I) if light else ('loc_anywhere_light_safe' if child else 'loc_anywhere_light'))
        if sig: clean += ' A distinguishing detail is __%s_signature__.' % I
        if has_sign: clean += ' On view is __%s_sign__.' % I
        G['%s_clean' % I] = [clean]
        for key, vals in (('items', items), ('furniture', furn), ('installed', inst)):
            if len(vals) >= 8: G['%s_%s_a' % (I, key)] = vals[0::2]; G['%s_%s_b' % (I, key)] = vals[1::2]
        two = lambda key, n: ('__%s_%s_a__ and __%s_%s_b__' % (I, key, I, key)) if n >= 8 else '__%s_%s__' % (I, key)
        body = ''
        if items: body += ' The loose items include %s.' % two('items', len(items))
        if furn: body += ' The furniture and equipment include %s.' % two('furniture', len(furn))
        if inst: body += ' The built-in features include %s.' % two('installed', len(inst))
        if inc: body += ' Left lying about is __%s_incidental__.' % I
        if trace: body += ' Signs of people include __%s_traces__.' % I
        if cond: body += ' This version of the place is __%s_condition__.' % I
        body += ' The view is __loc_shot__.'
        G['%s_scene' % I] = ['__%s_clean__%s' % (I, body)]
        G['%s_scene_plus' % I] = ['__%s_scene__ Also here are __%s__ and __%s__.' % (I, 'loc_anywhere_items_safe' if child else 'loc_anywhere_items', 'loc_anywhere_traces_safe' if child else 'loc_anywhere_traces')]
        if time: G['%s_time_scene' % I] = ['__%s_scene__ It is __%s_time__.' % (I, I)]
        if cond: G['%s_era_scene' % I] = ['__%s_clean__ This version of the place is __%s_condition__.%s The view is __loc_shot__.' % (I, I, (' The loose items include __%s_items__.' % I) if items else '')]
        if region: G['%s_region_scene' % I] = ['__%s_clean__ In its regional form, __%s_region__.%s The view is __loc_shot__.' % (I, I, (' The loose items include __%s_items__.' % I) if items else '')]
        person = 'loc_person_adult25' if child else 'loc_person'
        G['%s_people' % I] = ['__%s_clean__%s%s One person is here. __%s__ The person is __loc_person_action__. __frame_person_full__' % (
            I, (' The furniture and equipment include __%s_furniture__.' % I) if furn else ((' The built-in features include __%s_installed__.' % I) if inst else ''), (' It is __%s_time__.' % I) if time else '', person)]
        if child: child_ids.add(I)
        for key in ('all', r['cat']): idx.setdefault(key, []).append(I)
        if r['tags'] and len(r['tags']) >= 12:
            for nme, val in zip(TAGNAMES, r['tags']):
                for v in val.split(','):
                    v = slug(v.strip())
                    if v and v != 'varies': idx.setdefault('tag_%s_%s' % (nme, v), []).append(I)
    for key, v in pools.items():
        shared = sorted(x for x, c in v.items() if c >= 2 and len(x) < 90)
        if shared:
            G['loc_anywhere_%s' % key] = shared
            G['loc_anywhere_%s_safe' % key] = [x for x in shared if not ADULT.search(x)]
    for key, ids in idx.items():
        if key.startswith('tag_'): G['loc_%s' % key] = ['__%s_scene__' % i for i in ids]; continue
        pre = 'loc' if key == 'all' else 'loc_%s' % key
        G['%s_scene' % pre] = ['__%s_scene__' % i for i in ids]
        G['%s_clean' % pre] = ['__%s_clean__' % i for i in ids]
        G['%s_scene_plus' % pre] = ['__%s_scene_plus__' % i for i in ids]
        G['%s_people' % pre] = ['__%s_people__' % i for i in ids]
        for kind in ('time', 'era', 'region'):
            have = [i for i in ids if '%s_%s_scene' % (i, kind) in G]
            if have: G['%s_%s_scene' % (pre, kind)] = ['__%s_%s_scene__' % (i, kind) for i in have]
    G['loc_shot'] = ['a wide establishing view of the whole space', 'a close view on the most telling detail', 'a view through the doorway from the next room',
                     'a low angle near the floor looking along the space', 'a corner view in three-quarter perspective', 'an eye-level view from the entrance',
                     'a high view from one corner looking down', 'a centred, symmetrical view straight down the middle']
    for k2, v in WORDS.items(): G[k2] = v
    G['loc_person'] = ['__f_create_random_woman_short__ She is wearing __f_outfit_casual_mixed__.', '__f_create_random_woman_short__ She is wearing __f_outfit_formal_mixed__.',
                       '__m_create_random_man_short__ He is wearing __m_outfit_casual_mixed__.', '__m_create_random_man_short__ He is wearing __m_outfit_formal_mixed__.']
    G['loc_person_adult25'] = ['__loc_woman_adult25__ She is wearing __loc_outfit_modest_f__.', '__loc_man_adult25__ He is wearing __loc_outfit_modest_m__.']
    G['_child_ids'] = sorted(child_ids)
    G['v109_loc_entry_points'] = ['loc_scene', 'loc_scene_plus', 'loc_clean', 'loc_people', 'loc_time_scene', 'loc_era_scene', 'loc_region_scene'] + ['loc_%s_scene' % c for c in v109_locparse.CATS if c in idx]
    return G
MODEST_OK = re.compile(r"\b(trousers|jeans|chinos|slacks|joggers|cardigan|jumper|sweater|blouse|shirt|polo|blazer|jacket|fleece|turtleneck|crewneck|crew-neck)\b", re.I)
MODEST_NO = re.compile(r"\b(off-shoulder|one-shoulder|off-the-shoulder|cold-shoulder|robe|kimono|slip|mesh|sheer|see-through|corset|crop\w*|mini\w*|shorts|swim\w*|slit|backless|bodycon|lingerie|bra|bralette|thong|strapless|halter|bodysuit|plunging|low-cut|tank|vest top|camisole|cami|bikini|sarong|leggings|heels|stilettos?|fishnet|lace|latex|leather trousers|pyjama\w*|nightdress|negligee|onesie|towel|tutu|costume|sexy|tight|skin-tight|figure-hugging|cut-?out)\b", re.I)
def adult25(final):
    """Adults aged 25 and over: the lines of the short person files whose age bracket is not 18-24, plus modest workwear (loc_outfit_modest_f/m)
    filtered from the everyday clothing files, used for people in child-related places."""
    out = {}
    for src, dst in (('f_clothing_everyday', 'loc_outfit_modest_f'), ('m_clothing_everyday', 'loc_outfit_modest_m')):
        out[dst] = sorted({l.strip() for l in open(os.path.join(final, src + '.txt'), encoding='utf8') if l.strip() and MODEST_OK.search(l) and not MODEST_NO.search(l) and not NEG.search(l)})
    for src, dst in (('f_create_random_woman_short', 'loc_woman_adult25'), ('m_create_random_man_short', 'loc_man_adult25')):
        out[dst] = [l.rstrip('\n') for l in open(os.path.join(final, src + '.txt'), encoding='utf8') if l.strip() and 'age18_24' not in l]
    return out
def child_safe_check(G):
    """Fails if any file built for a child-related place, or any file those places draw on, carries adult vocabulary."""
    bad = []
    for I in G['_child_ids']:
        for k, v in G.items():
            if k.startswith(I + '_') or k == I:
                bad += [(k, l) for l in v if ADULT.search(l)]
    for k in ('loc_anywhere_items_safe', 'loc_anywhere_traces_safe', 'loc_person_adult25', 'loc_person_action'):
        bad += [(k, l) for l in G.get(k, []) if ADULT.search(l)]
    return bad
if __name__ == '__main__':
    G = build(); print(len(G), 'files;', len(G['loc_scene']), 'locations;', len(G['_child_ids']), 'child-related'); print('child-safe problems:', child_safe_check(G)[:5])
