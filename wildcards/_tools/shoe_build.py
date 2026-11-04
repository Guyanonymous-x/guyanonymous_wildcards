"""Builds the SHOE wildcards (files named shoe_*).  Runs after the women's and men's libraries are merged (build_all.py calls it); shoes are not gendered.

The design follows the 1000-line sample file (data/shoe_vocab.json holds every value harvested from it, all kept):
  * SIX QUALITY TIERS t1..t6 (budget -> value -> mid-range -> premium -> luxury couture -> museum-grade one-of-a-kind).  The tier drives the tier word,
    materials, construction, hardware, sole, lining, finish AND the price band (EUR 12-57 / 40-155 / 135-595 / 510-1,950 / 4,000-20,000 / 110,000-311,000).
  * SEVEN SHOE CLASSES: boot, heel, flat, sneaker, sandal, slipper, clog (about 300 shoe types).  Every type knows how it closes (laces, zip, buckle, slip-on ...)
    and what kind of sole/heel it has, so a loafer never "laces up" and a stiletto never gets a lug sole.
  * NEW VARIABLES: purpose (what the shoe is for), target audience (adults only), pattern, camera/photo style, price overlay.

FINISHED PROMPTS (coherent, ready to use)
  shoe_prompt_master            picks a tier (cheap more often than luxury), then a class, then a finished prompt
  shoe_prompt_t1 .. t6          one tier, any class        shoe_prompt_boot|heel|flat|sneaker|sandal|slipper|clog    one class, any tier
  shoe_full_<class>_t<n>        the finished prompts themselves (250 each, 42 files);  shoe_full_t<n>, shoe_full_<class> and shoe_full are the pickers
  shoe_prompt_mix_t1 .. t6, shoe_prompt_mix    "free mix" templates in the style of the sample: every slot is picked independently from the component files
  shoe_prompt_feet              a close-up of someone's feet in shoes (uses shoe_worn)
SHORT PHRASES for character prompts (use them in your own outfit templates):  shoe_worn, shoe_worn_<class>, shoe_worn_senior, shoe_floor
COMPONENTS (use them in your own templates):
  shoe_word_t<n> shoe_type shoe_type_<class> shoe_designer shoe_designer_bare shoe_material_t<n> shoe_colour shoe_colour_t<n> shoe_pattern shoe_pattern_sentence
  shoe_toe shoe_toe_art shoe_aesthetic shoe_detail_t<n> shoe_technique_t<n> shoe_construction_t<n> shoe_heel_<high|mid|stack|cuban|wedge|platform> shoe_heelmat_t<n>
  shoe_sole_t<n> shoe_closure_t<n> shoe_lining_t<n> shoe_footbed_t<n> shoe_finish_t<n> shoe_practical shoe_whimsical shoe_extras_t<n>
  shoe_purpose shoe_purpose_<class> shoe_audience shoe_audience_<class> shoe_audience_t<n> shoe_price_t<n> shoe_overlay_t<n> shoe_photo
Deterministic (fixed seed).  No curly braces or pipe characters are written."""
import os, sys, json, random, re
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from paths import FINAL, DATA
from shoe_data import *
import shoe_data2 as D2
WC = sys.argv[1] if len(sys.argv) > 1 and os.path.isdir(sys.argv[1]) else FINAL
V = json.load(open(os.path.join(DATA, 'shoe_vocab.json'), encoding='utf8'))
FULL_N = 250                       # finished prompts per (class, tier)
BAD = re.compile(r'[{}|]')
written = []
def uniq(xs):
    seen = set(); out = []
    for x in xs:
        x = x.strip()
        if x and x not in seen: seen.add(x); out.append(x)
    return out
_A = re.compile(r'\b([Aa])( )([aeiouAEIOU][\w\-]*)')
_AN = re.compile(r'\b([Aa]n)( )([^aeiouAEIOU\W\d][\w\-]*)')
_VOWEL_CONS = ('one', 'uni', 'use', 'usu', 'eu', 'ura', 'ut')
_CONS_VOWEL = ('hour', 'honest', 'heir', 'honour')
def fix_articles(l):
    l = _A.sub(lambda m: m.group(0) if m.group(3).lower().startswith(_VOWEL_CONS) else m.group(1) + 'n' + m.group(2) + m.group(3), l)
    return _AN.sub(lambda m: m.group(0) if m.group(3).lower().startswith(_CONS_VOWEL) else m.group(1)[0] + m.group(2) + m.group(3), l)
def w(name, lines):
    lines = [fix_articles(l) for l in lines]
    for l in lines:
        if BAD.search(l): sys.exit(f'forbidden character in {name}: {l[:80]}')
    open(os.path.join(WC, name + '.txt'), 'w', encoding='utf8', newline='\n').write('\n'.join(lines) + '\n'); written.append(name)
def art(x): return ('an ' if re.match(r'[aeiouAEIOU]', x) else 'a ') + x
def cap(x): return x[0].upper() + x[1:]
def ex(n): return os.path.exists(os.path.join(WC, n + '.txt'))
def level(t): return 'LOW' if t in ('T1', 'T2') else 'MID' if t in ('T3', 'T4') else 'HIGH'
def tn(t): return t[1]                         # 'T3' -> '3'
def ref(n): return f'__{n}__'
# ============================================================ vocabulary assembly (sample values first, then new ones)
def per_tier(sample, extra=None, fixed=None):
    out = {}
    for t in T:
        out[t] = uniq(list(sample.get(t, [])) + list((extra or {}).get(t, [])))
    return out
TYPEINFO = {}                                   # type -> (class, closure kinds, sole kind)
TYPES_BY = {c: [] for c in CLASSES}
for c in CLASSES:
    for row in TYPES[c]:
        n, ck, sk = row.split('|'); TYPEINFO[n] = (c, ck.split(','), sk); TYPES_BY[c].append(n)
missing = [x for x in V['type'] if x not in TYPEINFO]
SAMPLE_CLASS = {  # sample types that are not in the hand-written catalogue are filed here
}
for x in missing:
    sys.exit('sample type not classified: ' + x)
ALL_TYPES = uniq([t for t in V['type']] + [n for c in CLASSES for n in TYPES_BY[c]])
DESIGNERS_BARE = uniq(V['designer'] + D2.DESIGNER_EXTRA)
def clean_designer(d): return re.sub(r'^(an?|the) ', '', d)
DESIGNERS_BARE = uniq([clean_designer(d) for d in DESIGNERS_BARE])
MAT = per_tier(V['material'], D2.MATERIAL)
CON = per_tier(V['construction'], D2.CONSTRUCTION_EXTRA)
DET_BAD = {'raw', 'plain', 'flat', 'a naturally mottled', 'a gently pointed'}
DET = {t: uniq([d for d in V['detail'][t] if d not in DET_BAD and len(d) > 8] + D2.DETAIL_EXTRA) for t in T}
TECH = {t: uniq(V['technique'][t] + D2.TECHNIQUE_EXTRA[t]) for t in T}
TOES = uniq([art(x) if not re.match(r'^(an?|the) ', x) else x for x in V['toe']] + D2.TOE)
AESTH = uniq(['a ' + x if not re.match(r'^(an?|the|squares|tessellated|honest|unembellished|unpolished|outlined|exposed|even) ', x) else x for x in V['aesthetic']] + D2.AESTHETIC)
AESTH = uniq([x for x in AESTH])
GEN_COLOURS = D2.COLOUR_SINGLE
# ------------------------------------------------------------------ colours: sample + singles + generated pairs
def colour_pairs(R, n):
    out = []
    for _ in range(n * 3):
        a, b = R.sample(GEN_COLOURS, 2)
        c = R.random()
        out.append(f'{a} and {b}' if c < .6 else f'{a} with {b} accents' if c < .8 else f'{a} with {b} trim' if c < .9 else f'{a} on {b}')
        if len(set(out)) >= n: break
    return uniq(out)[:n]
R0 = random.Random(7001)
COL_PAIRS = colour_pairs(R0, 420)
ALL_COL = uniq(V['colour'] + GEN_COLOURS + COL_PAIRS)
COL_T = {}
for t in T:
    R = random.Random(7100 + int(tn(t)))
    base = uniq(list(V['colour']) if False else [])
    COL_T[t] = uniq(D2.COLOUR_SPECIAL[t] + GEN_COLOURS + R.sample(COL_PAIRS, 160))
# per-tier sample colours that were observed are folded in so nothing is lost
OBS = json.load(open('/dev/null')) if False else None
# ============================================================ heels and soles
HEEL = {
 'high': L("""a 4-inch stiletto heel
a slender 3.75-inch architectural heel
a sculpted 3.5-inch flared heel
a 3-inch cone heel
a 4.5-inch spool heel
a 4-inch curved sculpted heel
a 3.5-inch Louis heel
a 4-inch needle heel
a 4.5-inch pencil heel
a 3.75-inch tapered heel
a 4-inch trumpet heel
a 5-inch skyscraper stiletto
a 3.5-inch sculpted cylinder heel
a 4-inch geometric cut-out heel
a 3.5-inch pyramid heel"""),
 'mid': L("""a 2-inch kitten heel
a 3-inch block heel
a chunky 3-inch sculpted heel
a curved 2.5-inch Louis heel
a 2.5-inch stacked heel
a 2-inch flared heel
a 2.5-inch spool heel
a 3-inch squared heel
a 2-inch comma heel
a 2.25-inch tapered heel"""),
 'stack': L("""a 1-inch stacked heel
a 1.25-inch stacked heel
a 1.5-inch block heel
a low 0.75-inch heel
a 1.75-inch block heel
a flat 0.5-inch heel
a 1.25-inch walking heel
a 1.5-inch chunky heel"""),
 'cuban': L("""a 2-inch Cuban heel
a 2.5-inch angled riding heel
a 1.75-inch underslung heel
a 2-inch walking heel
a 2.25-inch slanted heel"""),
 'wedge': L("""a 2-inch wedge
a 3-inch wedge
a 4-inch wedge
a 2.5-inch wedge
a gently sloped 2-inch wedge
a 3.5-inch sculpted wedge"""),
 'platform': L("""a 5-inch heel over a 1.5-inch platform
a chunky 2-inch platform
a 3-inch platform
a 4-inch heel over a 1-inch platform
a 1.5-inch flatform
a 3.5-inch wedge platform"""),
}
HEELMAT = per_tier(V['heel_material'], {
 'T1': L("molded plastic\nhollow ABS plastic\nrubber-capped plastic\nstacked faux-wood\nthin stacked card"),
 'T2': L("rubber-capped plastic\nstacked faux-wood\nstacked composite leather\ndurable molded rubber"),
 'T3': L("stacked leather\ncovered matching leather\nsolid beechwood\nstacked leather with a rubber top lift"),
 'T4': L("leather-covered wood\npolished stacked leather\nlacquered wood\nsolid hardwood wrapped in calf"),
 'T5': L("lacquered beechwood\nsculpted brass\nhand-carved walnut\nhand-carved rosewood\nsilver-plated brass"),
 'T6': L("polished jade\nsolid gold plate over bronze\ncarved rock crystal\ncarved lapis lazuli\ncast silver set with gems\nhand-carved ebony inlaid with gold")})
RUB = {'LOW': L("molded rubber\nthin rubber\nrecycled-tire rubber\nthermoplastic rubber\ninjection-molded foam\nlightweight molded EVA\nflat foam-rubber\nPVC"),
       'MID': L("natural rubber\ndual-density rubber\ncrepe rubber\ncushioned phylon\nstitched natural rubber\nsiped natural rubber\nshock-absorbing foam"),
       'HIGH': L("hand-cut natural rubber\nhand-bevelled rubber\nhand-polished rubber\nrubber inlaid with leather\nrubber edged in gold\nbespoke-moulded rubber\nrubber cut from a single block")}
LEA = {'LOW': L("thin synthetic\nstamped composite\nbonded leather\nplastic-coated\nmolded plastic"),
       'MID': L("stacked leather\noak-bark-tanned leather\nchanneled leather\nclosed-channel leather\nhand-burnished leather\nsewn leather"),
       'HIGH': L("hand-bevelled leather\nhand-burnished rosewood-stained leather\nlacquered leather\ngilt-edged leather\nmother-of-pearl-edged leather\nhand-stitched leather\nhand-lacquered leather")}
FIN = {'LOW': L("plain\nunfinished\npainted\nvarnished\nrough-cut"), 'MID': L("carved\nlacquered\nhand-sanded\nwaxed\noiled"), 'HIGH': L("hand-carved and gilded\nhand-lacquered\ninlaid\nmother-of-pearl-inlaid\nengraved")}
SOLE_KIND = {  # kind -> (adjective pool, noun phrases)
 'flat': (LEA, L("flat sole\nslim flexible sole\nlow-profile sole\nstreamlined outsole")),
 'dress': (LEA, L("sole\nouter sole\nhalf sole with a heel lift\nsole")),
 'stack': (LEA, L("sole\nsole with a rubber heel lift\nouter sole")),
 'sport': (RUB, L("cushioned running sole\ncourt-grip outsole\nsole unit with a thick midsole\nlightweight sole")),
 'lug': (RUB, L("lug sole\ncommando sole\ntrail tread sole\nlugged outsole\ndeep-tread sole")),
 'soft': (RUB, L("flexible indoor sole\nnon-slip house sole\npadded sole\ngripper-dotted sole")),
 'rubber': (RUB, L("slip-resistant sole\ncushioned work sole\nnon-marking sole\noil-resistant rocker sole")),
 'crepe': (RUB, L("crepe sole\ngum sole\nsoft crepe outsole")),
 'thin': (RUB, L("zero-drop flexible sole\nground-feel minimal sole\nlow-stack flexible sole")),
 'comfort': (RUB, L("extra-depth comfort sole\nrocker comfort sole\nwide cushioned sole\northotic-friendly sole")),
 'thong': (RUB, L("foam flip-flop sole\ncontoured thong footbed sole\nthong sole")),
 'wood': (FIN, L("wooden sole\nshaped wooden base\nclog sole carved from a single block")),
 'cork': (FIN, L("cork-bed sole\nlayered cork sole")),
 'rope': (FIN, L("coiled jute-rope sole\nbraided rope sole")),
 'platform': (RUB, L("outsole\nsole\ngrip outsole")),
}
def outsole(R, kind, t):
    adjs, nouns = SOLE_KIND[kind]
    a = R.choice(adjs[level(t)]); n = R.choice(nouns)
    if kind in ('wood', 'cork', 'rope'): return f'{art(a)} {n}'
    return f'{art(a)} {n}'
SOLE_VERB = ['rest on', 'stand on', 'sit on']
def sole_phrase(R, sk, t):
    """Returns the part after 'They rest on' for a shoe with sole kind sk."""
    if sk in ('high', 'mid', 'stack', 'cuban', 'wedge'):
        hk = {'high': 'high', 'mid': 'mid', 'stack': 'stack', 'cuban': 'cuban', 'wedge': 'wedge'}[sk]
        under = outsole(R, 'dress' if sk != 'wedge' else 'flat', t) if sk != 'stack' else outsole(R, 'stack', t)
        mat = R.choice(HEELMAT[t])
        if sk == 'wedge': return f'{R.choice(HEEL[hk])} of {mat} above {under}'
        return f'{R.choice(HEEL[hk])} of {mat} above {under}'
    if sk == 'platform':
        return f'{R.choice(HEEL["platform"])} of {R.choice(HEELMAT[t])} above {outsole(R, "platform", t)}'
    return outsole(R, sk, t)
# ============================================================ closures
def closure_sentence(R, kind, t):
    h = lambda k: R.choice(D2.HW[k][t])
    if kind == 'lace': return R.choice([f'It laces up with {h("lace")} through {h("eyelet")}.', f'{cap(h("lace"))} thread through {h("eyelet")} to close it.', f'It fastens with {h("lace")} threaded through {h("eyelet")}.'])
    if kind == 'hook': return f'It laces through speed hooks with {h("lace")}.'
    if kind == 'zip': return R.choice([f'A {h("zip")} runs up the inner side.', f'A {h("zip")} runs up the back of the shaft.', f'It closes with a {h("zip")} on the outer side.'])
    if kind == 'button': return f'It fastens with a row of {h("button")}.'
    if kind == 'buckle': return R.choice([f'A slim strap wraps the instep and fastens with a {h("buckle")}.', f'It closes with a {h("buckle")} on a slim strap.', f'Two straps cross the instep, each fastened with a {h("buckle")}.'])
    if kind == 'strap': return R.choice([f'A {h("strap")} wraps the ankle and fastens with a {h("buckle")}.', f'A {h("strap")} crosses the instep and fastens with a {h("buckle")}.'])
    if kind == 'hookloop': return R.choice(['Wide hook-and-loop straps let it fasten in a second.', 'Adjustable hook-and-loop straps hold the foot securely.'])
    if kind == 'elastic': return R.choice(['Elastic side gussets and a rear pull tab make it easy to pull on.', 'Stretch elastic panels let it slip on and off easily.'])
    if kind == 'pull': return R.choice(['Leather pull loops at the top make it easy to pull on.', 'It pulls on by a pair of stitched pull straps.', 'A rear pull tab helps it on.'])
    if kind == 'slip': return R.choice(['It slides on without any closures.', 'It slips on easily with no fastenings.', 'It is a fastening-free slip-on design.'])
    if kind == 'ribbon': return R.choice([f'Long {h("ribbon")} tie around the ankle.', f'{cap(h("ribbon"))} wind up the ankle and tie in a bow.'])
    if kind == 'thong': return R.choice(['A thong post sits between the first two toes.', 'A toe post holds the foot, anchored to the sole.'])
    if kind == 'toggle': return R.choice(['A quick-pull bungee lace with a cord-lock toggle secures the fit.', 'A cord and toggle pull the collar snug.'])
    raise KeyError(kind)
ALL_KINDS = ['lace', 'hook', 'zip', 'button', 'buckle', 'strap', 'hookloop', 'elastic', 'pull', 'slip', 'ribbon', 'thong', 'toggle']
# ============================================================ extras
PRACT = uniq(V['practical'] + D2.PRACTICAL_EXTRA)
WHIM = uniq(V['whimsical'] + D2.WHIMSY_EXTRA)
PR_BAD = {'heel': ['lace pressure', 'siped', 'waterproof', 'debris', 'toe bumper', 'kick guard', 'metatarsal', 'oil-resistant', 'salt', 'drain', 'quick-drying', 'laces', 'Velcro', 'rocker', 'hook-and-loop'],
          'sandal': ['lace pressure', 'waterproof membrane', 'debris', 'salt', 'toe bumper', 'Velcro', 'laces', 'tongue'], 'slipper': ['lace', 'siped', 'debris', 'waterproof', 'metatarsal', 'kick guard', 'oil-resistant', 'salt', 'toe bumper', 'tongue', 'shank'],
          'clog': ['lace', 'Velcro', 'tongue'], 'flat': ['siped', 'metatarsal'], 'sneaker': [], 'boot': [], 'platform': ['lace pressure', 'siped', 'metatarsal', 'oil-resistant', 'salt'], 'novelty': ['siped', 'metatarsal', 'oil-resistant', 'salt'], 'exotic': ['lace pressure', 'siped', 'waterproof', 'debris', 'toe bumper', 'kick guard', 'metatarsal', 'oil-resistant', 'salt', 'drain', 'quick-drying', 'Velcro', 'rocker', 'hook-and-loop']}
def extras_sentence(R, cls=None):
    bad = PR_BAD.get(cls, []) if cls else []
    P = [x for x in PRACT if not any(b in x for b in bad)]
    a = R.choice(P); b = R.choice([x for x in P if x != a]); wh = R.choice(WHIM); wh2 = R.choice([x for x in WHIM if x != wh]); r = R.random()
    if r < .39: return f'Practical details include {a} and {b}.'
    if r < .59: return f'Alongside {a}, they add {wh} for playfulness.'
    if r < .80: return f'They balance {a} with the whimsy of {wh}.'
    return f'Whimsical touches include {wh} and {wh2}.'
# ============================================================ prices
def fmt(v):
    s = f'{v:,.2f}' if abs(v - round(v)) > 1e-9 else f'{int(round(v)):,}'
    return '€' + s
def prices(t):
    lo, hi = PRICE_BAND[t]; out = [p for p in V['price'][t]]
    if t == 'T1': vals = [x + .99 for x in range(11, 57)] + [x + .95 for x in range(12, 57, 3)]
    elif t == 'T2': vals = [x + .99 for x in range(39, 155)] + list(range(45, 156, 5))
    elif t == 'T3': vals = list(range(135, 596, 5)) + [x + .99 for x in range(139, 590, 25)]
    elif t == 'T4': vals = list(range(510, 1951, 5))
    elif t == 'T5': vals = list(range(4000, 20001, 50))
    else: vals = list(range(110000, 311001, 1000))
    out += [fmt(v) for v in vals if lo - 1e-9 <= v <= hi + 1e-9]
    return uniq(out)
PRICE = {t: prices(t) for t in T}
OVL_POS = ['bottom right hand corner', 'bottom left hand corner', 'top right hand corner', 'top left hand corner', 'bottom centre']
def overlay(R, price):
    pos = 'bottom right hand corner' if R.random() < .88 else R.choice(OVL_POS)
    font = 'professional serif font' if R.random() < .9 else R.choice(['clean sans-serif font', 'elegant script font', 'small bold sans-serif font'])
    return f'Overlay, in {font}, "Price: {price}" in the {pos} of the image.'
# ============================================================ quality ladder (replaces the old price/overlay files)
QUAL_HEAD = {
 'T1': ['bargain-bin quality', 'the cheapest quality available', 'throwaway quality', 'rock-bottom budget quality', 'very low-cost quality'],
 'T2': ['budget quality', 'plain everyday value quality', 'entry-level quality', 'low-cost but serviceable quality', 'discount-shop quality'],
 'T3': ['solid mid-range quality', 'good everyday quality', 'dependable mainstream quality', 'well-made department-store quality', 'comfortably average quality'],
 'T4': ['high-end quality', 'premium quality', 'fine specialist-maker quality', 'carefully crafted boutique quality', 'upper-tier designer quality'],
 'T5': ['luxury quality', 'couture-house quality', 'exceptionally expensive quality', 'master-atelier quality', 'heirloom luxury quality'],
 'T6': ['absurdly expensive quality', 'obscenely lavish quality', 'museum-piece quality that costs a fortune', 'one-of-a-kind quality for the richest buyers', 'quality beyond any sensible budget'],
}
QUAL_BODY = {
 'T1': ['glued together with visible excess adhesive', 'with uneven stitching and thin materials', 'that would not survive a month of wear', 'with a flimsy, flexible sole', 'with loose threads and printed-on details'],
 'T2': ['with basic materials and machine stitching', 'with a plain finish and little padding', 'built to last a season or two', 'with simple moulded parts', 'with basic hardware that works'],
 'T3': ['with sound stitching and sturdy materials', 'with a comfortable footbed and clean finish', 'built to last for years of normal wear', 'with tidy edges and reliable hardware', 'made with careful machine work'],
 'T4': ['with hand-finished details and top-grade materials', 'with refined lasting and polished edges', 'made in a small workshop with great care', 'with rare materials and tight, even stitching', 'with a resoleable construction and a perfect fit'],
 'T5': ['hand-made by master craftspeople from the rarest hides and metals', 'with gold-plated or gem-set hardware', 'made to measure over a carved personal last', 'with flawless finishing and exotic skins', 'made from materials of exceptional provenance'],
 'T6': ['encrusted with large gemstones and precious metals', 'cast in solid gold or platinum with diamond details', 'made from the rarest materials on earth', 'commissioned as a unique showpiece with jewelled soles', 'made with astonishing, impractical extravagance'],
}
QUALITY = {}
for _t in QUAL_HEAD:
    QUALITY[_t] = uniq([f'{h}, {b}' for h in QUAL_HEAD[_t] for b in QUAL_BODY[_t]] + QUAL_HEAD[_t])
# ============================================================ pattern sentences
PATT = uniq(D2.PATTERN)
PAT_PLAIN = {'plain, with no pattern at all': 'The upper is deliberately plain, with no pattern at all.', 'quiet tone-on-tone stitching': 'The upper is plain apart from quiet tone-on-tone stitching.',
             'subtle self-colour embossing': 'The upper is plain apart from subtle self-colour embossing.'}
def pattern_sentence(R, pat):
    if pat in PAT_PLAIN: return PAT_PLAIN[pat]
    return R.choice([f'The upper is decorated with {pat}.', f'A pattern of {pat} covers the upper.', f'The surface carries {pat}.', f'Its pattern is {pat}.', f'{cap(pat)} run across the vamp and quarters.' if pat.endswith('s') else f'{cap(art(pat))} runs across the vamp and quarters.'])
# ============================================================ full prompt generation
def make_line(R, cls, t):
    typ = R.choice(TYPES_BY[cls]); _, ck, sk = TYPEINFO[typ]
    word = R.choice(WORDS[t]); des = art(R.choice(DESIGNERS_BARE)); mat = R.choice(MAT[t]); col = R.choice(COL_T[t] if R.random() < .75 else ALL_COL); con = R.choice(CON[t])
    s = [f'A pair of {word} {typ} designed by {des}, made of {mat} in {col}, {con}.']
    # purpose / audience (new variables)
    r = R.random(); pur = R.choice(PURPOSE[cls])
    aud_any = R.choice(AUDIENCE_COMMON + AUDIENCE_TIER[t] * 2)                  # fits any purpose
    aud_cls = R.choice(AUDIENCE[cls] + AUDIENCE_TIER[t] + AUDIENCE_COMMON[:10])  # class-specific, used on its own
    if r < .18: pass
    elif r < .40: s.append(f'They are made for {aud_any} and built for {pur}.')
    elif r < .58: s.append(f'Aimed at {aud_any}, they are meant for {pur}.')
    elif r < .72: s.append(f'The design targets {aud_cls}.')
    elif r < .86: s.append(f'They are intended for {pur}.')
    else: s.append(f'Built for {pur}, they are aimed at {aud_any}.')
    # toe / detail / technique (three frames like the sample)
    toe = R.choice(TOES); det = R.choice(DET[t]); tec = R.choice(TECH[t]); fr = R.random()
    if R.random() < .3: det = f'{det}, {R.choice(AESTH)}'
    if fr < .45: s.append(f'They have {toe} and feature {det}, {tec}.')
    elif fr < .75: s.append(f'The signature detail is {det}, {tec}, paired with {toe}.')
    else: s.append(f'Shaped with {toe}, the upper showcases {det}, {tec}.')
    if R.random() < .6: s.append(pattern_sentence(R, R.choice(PATT)))
    s.append(f'They {R.choice(SOLE_VERB)} {sole_phrase(R, sk, t)}.')
    s.append(closure_sentence(R, R.choice(ck), t))
    s.append(extras_sentence(R, cls))
    if t in ('T5', 'T6') and R.random() < .7 or t in ('T3', 'T4') and R.random() < .25: s.append(f'They are finished with {R.choice(FINISH[t])}.')
    s.append(R.choice(FOOTBED[t]) + '.' if cls == 'sandal' or 'thong' in ck else R.choice(LININGS[t]) + '.')
    if R.random() < .33: s.append(R.choice(D2.PHOTO))
    return ' '.join(s)
FINISH = {t: uniq(V['finish'].get(t, []) + D2.FINISH.get(t, [])) for t in T}
LININGS = {t: uniq(V['lining'][t] + D2.LININGS[t]) for t in T}
FOOTBED = {t: D2.FOOTBED[t] for t in T}
PURPOSE_ALL = uniq([x for c in CLASSES for x in PURPOSE[c]])
AUDIENCE_ALL = uniq(AUDIENCE_COMMON + [x for c in CLASSES for x in AUDIENCE[c]] + [x for t in T for x in AUDIENCE_TIER[t]])
# ============================================================ write component files
def weighted_refs(names_weights): return [ref(n) for n, wt in names_weights for _ in range(wt)]
def main():
    # tier words, types, designers
    for t in T: w(f'shoe_word_{t.lower()}', WORDS[t])
    w('shoe_type', ALL_TYPES)
    for c in CLASSES: w(f'shoe_type_{c}', TYPES_BY[c] if c != 'boot' else TYPES_BY[c])
    w('shoe_designer', [art(x) for x in DESIGNERS_BARE]); w('shoe_designer_bare', DESIGNERS_BARE)
    for t in T:
        tl = t.lower()
        w(f'shoe_material_{tl}', MAT[t]); w(f'shoe_construction_{tl}', CON[t]); w(f'shoe_detail_{tl}', DET[t]); w(f'shoe_technique_{tl}', TECH[t])
        w(f'shoe_colour_{tl}', COL_T[t]); w(f'shoe_heelmat_{tl}', HEELMAT[t]); w(f'shoe_lining_{tl}', LININGS[t]); w(f'shoe_footbed_{tl}', FOOTBED[t])
        w(f'shoe_audience_{tl}', AUDIENCE_TIER[t]); w(f'shoe_quality_{tl}', QUALITY[t])
        if t in FINISH and FINISH[t]: w(f'shoe_finish_{tl}', FINISH[t])
        else: w(f'shoe_finish_{tl}', [''])
        R = random.Random(7300 + int(tn(t)))
    w('shoe_quality', [x for t in T for x in QUALITY[t]])
    w('shoe_colour', ALL_COL); w('shoe_pattern', PATT); w('shoe_pattern_sentence', [pattern_sentence(random.Random(7400 + i), p) for i, p in enumerate(PATT)])
    w('shoe_toe_art', TOES); w('shoe_toe', [re.sub(r'^(an?|the) ', '', x) for x in TOES]); w('shoe_aesthetic', AESTH)
    for k in HEEL: w(f'shoe_heel_{k}', HEEL[k])
    # general sole file per tier: sample outsoles + every generated kind
    for t in T:
        R = random.Random(7500 + int(tn(t))); out = list(V['sole'][t]) + list(V['outsole'][t])
        for kind in SOLE_KIND:
            for _ in range(8): out.append(outsole(R, kind, t))
        w(f'shoe_sole_{t.lower()}', uniq(out))
        R = random.Random(7600 + int(tn(t))); cl = list(V['closure'][t])
        for kind in ALL_KINDS:
            for _ in range(10): cl.append(closure_sentence(R, kind, t).rstrip('.'))
        w(f'shoe_closure_{t.lower()}', uniq(cl))
        R = random.Random(7700 + int(tn(t))); w(f'shoe_extras_{t.lower()}', [extras_sentence(R) for _ in range(700)])
    w('shoe_practical', PRACT); w('shoe_whimsical', WHIM)
    w('shoe_purpose', PURPOSE_ALL); w('shoe_audience', AUDIENCE_ALL)
    for c in CLASSES: w(f'shoe_purpose_{c}', PURPOSE[c]); w(f'shoe_audience_{c}', uniq(AUDIENCE[c] + AUDIENCE_COMMON))
    # finished prompts
    for c in CLASSES:
        for t in T:
            R = random.Random(8000 + CLASSES.index(c) * 10 + int(tn(t))); seen = set(); lines = []
            while len(lines) < FULL_N:
                l = make_line(R, c, t)
                if l not in seen: seen.add(l); lines.append(l)
            w(f'shoe_full_{c}_{t.lower()}', lines)
    for t in T: w(f'shoe_full_{t.lower()}', weighted_refs([(f'shoe_full_{c}_{t.lower()}', CLASS_WEIGHT[c]) for c in CLASSES]))
    for c in CLASSES: w(f'shoe_full_{c}', weighted_refs([(f'shoe_full_{c}_{t.lower()}', TIER_WEIGHT[t]) for t in T]))
    w('shoe_full', weighted_refs([(f'shoe_full_{t.lower()}', TIER_WEIGHT[t]) for t in T]))
    # prompt pickers (these names are the ones to put into your own prompt templates)
    w('shoe_prompt_master', [ref('shoe_full')])
    for t in T: w(f'shoe_prompt_{t.lower()}', [ref(f'shoe_full_{t.lower()}')])
    for c in CLASSES: w(f'shoe_prompt_{c}', [ref(f'shoe_full_{c}')])
    # free-mix templates (every slot independent, like the sample)
    for t in T:
        tl = t.lower()
        base = (f'A pair of __shoe_word_{tl}__ __shoe_type__ designed by __shoe_designer__, made of __shoe_material_{tl}__ in __shoe_colour_{tl}__, __shoe_construction_{tl}__. '
                f'They have __shoe_toe_art__ and feature __shoe_detail_{tl}__, __shoe_technique_{tl}__. They rest on __shoe_sole_{tl}__. __shoe_closure_{tl}__. __shoe_extras_{tl}__. ')
        fin = f'They are finished with __shoe_finish_{tl}__. ' if t in ('T5', 'T6') else ''
        end = f'__shoe_lining_{tl}__.'
        w(f'shoe_prompt_mix_{tl}', [base + fin + end,
            base.replace('. They have', '. __shoe_pattern_sentence__ They have', 1) + fin + end,
            base.replace('. They have', f'. They are aimed at __shoe_audience__ and meant for __shoe_purpose__. They have', 1) + '__shoe_pattern_sentence__ ' + fin + end])
    w('shoe_prompt_mix', weighted_refs([(f'shoe_prompt_mix_{t.lower()}', TIER_WEIGHT[t]) for t in T]))
    # ---- short phrases to wear in character prompts
    FLOOR = L("""a worn wooden floor
a city pavement
a cobbled street
a patch of grass
a sandy beach
wet autumn leaves
a marble lobby floor
a gravel path
a dusty trail
fresh snow
a tiled kitchen floor
a polished ballroom floor
a red carpet
a muddy field
a rocky shore
a stone staircase
a concrete sidewalk
a sunlit wooden deck
a rain-slick street
a woven rug""")
    w('shoe_floor', FLOOR)
    WORN_W = {'T1': 20, 'T2': 35, 'T3': 28, 'T4': 12, 'T5': 4, 'T6': 1}
    def worn(R, cls=None, senior=False):
        cl = cls or R.choices(CLASSES, [CLASS_WEIGHT[c] for c in CLASSES])[0]
        t = R.choices(T, [WORN_W[x] for x in T])[0]
        typ = R.choice(['orthopedic comfort shoes', 'walking shoes', 'slip-on sneakers', 'house slippers', 'penny loafers', 'sheepskin slippers', 'low-top sneakers', 'moccasin slippers', 'ballet flats', 'hook-and-loop strap sneakers', 'cork-footbed sandals']) if senior else R.choice(TYPES_BY[cl])
        col = R.choice(GEN_COLOURS); mat = R.choice(MAT[t][:12]); s = f'{col} {typ} in {mat}'
        if R.random() < .45:
            ds = [d for d in DET[t] if len(d) > 12]; s += f' with {R.choice(ds)}'
        return f'wearing {s}'
    R = random.Random(7800); w('shoe_worn', uniq([worn(R) for _ in range(900)]))
    for i, c in enumerate(CLASSES):
        R = random.Random(7810 + i); w(f'shoe_worn_{c}', uniq([worn(R, c) for _ in range(300)]))
    R = random.Random(7830); w('shoe_worn_senior', uniq([worn(R, None, True) for _ in range(300)]))
    w('shoe_prompt_feet', ['A person\'s feet and lower legs, __shoe_worn__, standing on __shoe_floor__.'])
    print(f'Shoe wildcards: {len(written)} files written ({sum(1 for n in written if n.startswith("shoe_full_") and n.count("_") == 3)} finished-prompt files).')
if __name__ == '__main__': main()
