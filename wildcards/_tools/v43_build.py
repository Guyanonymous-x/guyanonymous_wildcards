"""v43: bodies, teeth, tattoos. (1) removes every LoRA tag/trigger and deletes f_body_labia2; (2) rebuilds the vulva/labia/clitoris and male genital files as random clinical systems (flaccid/unaroused default, erect/aroused as separate manual-only files, skin tone matched, near-average sizes);
(3) age- and dental-access-weighted teeth (age*_lip_teeth + teeth_access_*); (4) temporary, henna and bad-tattoo files. Idempotent."""
import os, re, sys, random, glob
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from paths import FINAL
BR = ['18_24', '25_34', '35_44', '45_54', '55_64', '65_74', '75_84', '85_94', '95_120']
LORA = re.compile(r'\s*<lora:[^>]*>\s*,?|\bm33typu55y\s*,?\s*', re.I)
def wr(wc, n, lines):
    lines = list(dict.fromkeys(lines)) if n.startswith('tattoo_') and False else lines
    open(os.path.join(wc, n + '.txt'), 'w', encoding='utf8', newline='\n').write('\n'.join(lines) + '\n')
def pick(rng, items):  # items: (text, weight)
    t = sum(w for _, w in items); r = rng.uniform(0, t)
    for x, w in items:
        r -= w
        if r <= 0: return x
    return items[-1][0]
def strip_lora(wc):
    n = 0
    p = os.path.join(wc, 'f_body_labia2.txt')
    if os.path.exists(p): os.remove(p); n += 1
    for f in glob.glob(os.path.join(wc, '*.txt')):
        t = open(f, encoding='utf8').read()
        if '<lora' in t or 'm33typu55y' in t:
            u = LORA.sub(' ', t); u = re.sub(r'(?m)^[ \t,]+', '', u); u = re.sub(r',\s*,', ',', u)
            open(f, 'w', encoding='utf8', newline='\n').write(u); n += 1
    return n
def female(wc):
    rng = random.Random(4301)
    wr(wc, 'f_body_labia_majora', [
        'full, plump outer labia majora that meet softly at the centre', 'smooth, moderately full outer labia majora that close neatly over the inner folds',
        'slim, flat outer labia majora with a narrow, shallow cleft', 'rounded, cushioned outer labia majora with a gentle central seam',
        'soft, slightly asymmetrical outer labia majora, one side a little fuller than the other', 'firm, well-defined outer labia majora with a clean, even outline',
        'relaxed, softly folded outer labia majora with fine creases in the skin', 'thin, slightly loose outer labia majora with a faint crepe-like texture',
        'prominent, rounded outer labia majora raised above the surrounding skin', 'gently curved outer labia majora of average fullness'])
    wr(wc, 'f_body_vulva_tone', [
        'matching the rest of her skin tone, slightly deeper in the folds', 'a shade deeper than the surrounding skin, evenly pigmented',
        'close to the colour of her thighs, with a soft pink-brown tone at the inner edges', 'a warm deeper tone than her abdomen, with smooth even colour',
        'the same tone as her inner arms, with slightly darker pigmentation along the outer folds', 'evenly matched to her overall skin tone, with a faint rosy flush along the inner edges',
        'a rich deeper tone than the surrounding skin, with subtle variation at the folds', 'pale and matching her skin, with soft pink inner edges'])
    wr(wc, 'f_body_clitoris', [
        'a small clitoral glans, mostly covered by a smooth clitoral hood, in an unaroused resting state',
        'an average-sized clitoral glans partly visible beneath a neat clitoral hood, unaroused',
        'a clitoral hood with a barely visible glans, soft and relaxed, matching the surrounding skin tone',
        'a modest clitoral glans of average size, resting beneath a smooth hood, with skin tone matching the vulva',
        'a slightly prominent clitoral hood with the glans lightly visible at its lower edge, unaroused',
        'a small, tucked clitoral hood with a smooth contour and no visible glans',
        'an average clitoral glans, slightly rosy in tone, resting under a thin clitoral hood',
        'a clitoral hood of moderate size with a faint central fold, glans mostly concealed, at rest'])
    wr(wc, 'f_body_clitoris_aroused', [
        'a slightly enlarged clitoral glans, more visible and a shade deeper in tone, with the clitoral hood drawn back a little',
        'a firm, noticeably swollen clitoral glans, fuller and deeper in colour than at rest, with the hood retracted',
        'an engorged clitoral glans of average size, slightly glossy, with the surrounding labia darker and fuller',
        'a visibly swollen clitoral glans emerging from the hood, with a deeper flush across the vulva'])
    lines = []
    tmpl = ['Her vulva has __f_body_labia_majora__, and __f_body_labia__. Her clitoral area shows __f_body_clitoris__. The skin of the vulva is __f_body_vulva_tone__.',
            'Her vulva shows __f_body_labia_majora__, with the skin __f_body_vulva_tone__. __f_pubichair__. Further, __f_body_labia__.',
            'Her vulva is formed by __f_body_labia_majora__. Her clitoris is __f_body_clitoris__, and the skin of the area is __f_body_vulva_tone__.',
            'Her genital area has __f_body_labia_majora__ and __f_body_clitoris__, with the tone being __f_body_vulva_tone__, and __f_pubichair__.']
    for i in range(160): lines.append(tmpl[i % 4])
    wr(wc, 'f_body_vulva', lines)
def male(wc):
    rng = random.Random(4302)
    size = [('small', 12), ('slightly below average', 14), ('average', 36), ('slightly above average', 24), ('above-average', 11), ('large', 3)]
    circ = ['circumcised, with a smooth exposed glans', 'circumcised, with a visible healed circumcision line below the glans', 'uncircumcised, with the foreskin covering the glans', 'uncircumcised, with a partly retracted foreskin', 'uncircumcised, with the foreskin gathered loosely at the tip']
    veins = ['with a pronounced vein pattern along the shaft', 'with a few faint veins along the shaft', 'with smooth shaft skin and almost no visible veins', 'with shaft skin slightly darker than the surrounding skin', 'with shaft skin matching the surrounding skin tone']
    pub = ['below a fully shaved pubic area', 'below groomed trimmed pubic hair', 'below a natural untrimmed pubic area', 'below a thin natural pubic patch', 'below a neatly shaped pubic area']
    scr = ['with a relaxed hanging scrotum', 'with a lightly haired scrotum', 'with a smooth, tight scrotum', 'with a loosely wrinkled scrotum', 'with a scrotum slightly darker than the surrounding skin']
    L = []
    for _ in range(120):
        L.append(f"His penis is {pick(rng, size)} when flaccid, {rng.choice(circ)}, {rng.choice(veins)}, {rng.choice(pub)}, {rng.choice(scr)}.")
    wr(wc, 'm_body_genitals', L)
    esz = [('about average in length and girth', 40), ('slightly above average in length', 22), ('slightly below average in length', 18), ('longer than average', 10), ('shorter but thick', 6), ('slender and long', 4)]
    ang = ['pointing straight outward', 'curving gently upward', 'angled slightly upward', 'standing nearly upright against the abdomen', 'curving slightly to one side']
    E = []
    for _ in range(40):
        E.append(f"His penis is erect, {pick(rng, esz)}, {rng.choice(circ)}, {rng.choice(veins)}, {rng.choice(ang)}, {rng.choice(pub)}, {rng.choice(scr).replace('relaxed hanging', 'drawn-up')}.")
    wr(wc, 'm_body_genitals_erect', E)
# ---------- teeth ----------
TEETH = {  # state -> list of phrases
 'perfect': ['perfect straight glowing white teeth', 'even, evenly spaced white teeth from professional orthodontic care', 'straight, bright, evenly aligned teeth with a symmetrical smile line', 'smooth, uniform white teeth with clean edges', 'aligned teeth with a closed-mouth smile', 'neatly aligned white teeth with a straight bite'],
 'natural': ['natural-looking teeth with a small chip', 'slightly uneven but healthy teeth of a natural ivory shade', 'natural ivory teeth with a slight overlap at the lower front', 'mostly straight teeth with a faint gap between the upper front teeth', 'healthy teeth with a slight overbite', 'small even teeth with one slightly rotated incisor', 'pointed canine teeth with a straight bite'],
 'flawed': ['crooked overlapping yellowed teeth', 'crowded teeth with a gap between the front teeth', 'gappy front teeth with a diastema', 'a snaggletooth jutting forward', 'teeth with visible grey fillings in the back molars', 'protruding upper teeth with an overbite', 'a visible underbite with slightly uneven lower teeth', 'worn, shortened teeth from grinding', 'teeth with a metal crown on one canine and mild staining', 'teeth with brace-straightened alignment and a few small marks left on the enamel'],
 'stained': ['yellowed irregular teeth', 'stained dark tobacco teeth', 'teeth stained brown from tea and age', 'teeth with grey-brown staining near the gum line', 'uneven teeth with heavy plaque and yellow-brown colour', 'chalky teeth with pitted white spots'],
 'missing_few': ['a missing upper front tooth leaving a visible gap', 'a missing canine tooth and a few small gaps', 'a few missing back teeth, visible when the mouth opens wide', 'one missing lower incisor and the rest slightly crooked', 'gaps where two teeth are missing and the neighbouring teeth have shifted'],
 'missing_many': ['many missing teeth with only a few worn teeth remaining at the front', 'very few remaining teeth, short, brown and widely spaced, with large gaps', 'a mostly toothless upper jaw with a few remaining lower teeth', 'a sparse set of broken, decayed teeth with several gaps', 'heavily decayed, broken teeth with visibly receded gums'],
 'dentures': ['a full set of even white dentures with a slightly artificial uniform look', 'upper dentures with natural teeth remaining below', 'a partial denture replacing the missing back teeth, with a thin visible metal clasp', 'full dentures with a bright, perfectly regular row of teeth', 'gold-capped teeth at the front among otherwise natural teeth'],
}
# tier -> state weights (dental access), then age shift
TIER = {'high': {'perfect': 30, 'natural': 35, 'flawed': 14, 'stained': 4, 'missing_few': 3, 'missing_many': 0, 'dentures': 4},
        'mid': {'perfect': 8, 'natural': 28, 'flawed': 24, 'stained': 12, 'missing_few': 9, 'missing_many': 3, 'dentures': 4},
        'low': {'perfect': 2, 'natural': 18, 'flawed': 24, 'stained': 18, 'missing_few': 16, 'missing_many': 10, 'dentures': 2}}
def age_shift(b):
    i = BR.index(b)  # 0..8
    return {'perfect': max(0.2, 1.3 - 0.15 * i), 'natural': 1.0 if i < 5 else 0.7, 'flawed': 1.0, 'stained': 0.8 + 0.2 * i, 'missing_few': 0.4 + 0.45 * i, 'missing_many': 0.1 + 0.5 * i * (i / 4), 'dentures': 0.05 + 0.5 * max(0, i - 1)}
SMILE = ['', '', '', ', in a closed-mouth smile', ', when laughing', ', with a wide smile']
def teeth(wc):
    rng = random.Random(4303)
    allw = {s: sum(TIER[t][s] for t in TIER) / 3.0 for s in TEETH}
    for t in TIER:
        L = []
        for _ in range(240):
            s = pick(rng, [(k, v) for k, v in TIER[t].items() if v > 0]); L.append(rng.choice(TEETH[s]) + rng.choice(SMILE))
        wr(wc, 'teeth_access_' + t, L)
    for b in BR:
        sh = age_shift(b); L = []
        for _ in range(400):
            s = pick(rng, [(k, max(0.01, allw[k] * sh[k])) for k in TEETH]); L.append(rng.choice(TEETH[s]) + rng.choice(SMILE))
        wr(wc, f'age{b}_lip_teeth', L)
    wr(wc, 'lip_teeth', [x + rng.choice(SMILE) for x in sum(TEETH.values(), []) for _ in range(2)])
# ---------- tattoos ----------
PLACE = ['on the inner forearm', 'on the outer forearm', 'on the upper arm', 'on the shoulder', 'on the back of the neck', 'on the side of the neck', 'on the upper back', 'across the lower back', 'on the ribs', 'on the chest', 'on the hip', 'on the thigh', 'on the calf', 'on the ankle', 'on the top of the foot', 'on the back of the hand', 'on the wrist', 'behind the ear', 'on the fingers', 'on the collarbone', 'on the stomach']
def tattoos(wc):
    rng = random.Random(4304)
    T = []
    for _ in range(80):
        T.append(rng.choice(['a temporary transfer tattoo of __tattoo_subject__ ', 'a stick-on temporary tattoo of __tattoo_subject__ ', 'a temporary tattoo of __tattoo_subject__ in washable ink ']) + rng.choice(PLACE) + rng.choice([', sitting flat on the skin with a faint glossy film and slightly lifted edges', ', with the printed colours looking flat and bright, and one corner starting to peel', ', slightly faded and cracked from a few days of wear', ', with a thin visible edge of clear film around the design', ', with the outline slightly smudged where it has rubbed against clothing']))
    wr(wc, 'tattoo_temporary', T)
    motif = ['an intricate paisley pattern', 'a mandala with fine radiating petals', 'trailing floral vines with small leaves', 'a geometric lattice of diamonds and dots', 'a peacock feather motif', 'a lace-like pattern of curling scrolls', 'a band of repeating teardrop shapes', 'a sun-and-moon design with dotted borders', 'fine line work of crescents and stars', 'a cluster of flowers with delicate stems']
    hp = ['on the palm and fingers', 'across the back of the hand and up the wrist', 'around the wrist and forearm', 'on both hands in matching designs', 'on the top of the foot and around the ankle', 'along the forearm in a long trailing band', 'across the upper hands and fingertips', 'on the upper arm in a wide band', 'on the collarbone and shoulder']
    col = ['in deep reddish-brown stain', 'in fresh dark brown paste that has just been applied', 'in a faded orange-brown stain a week old', 'in a rich dark mahogany stain', 'in a pale ochre stain beginning to fade', 'in a dark chocolate stain with crisp lines']
    H = [f'henna body art showing {rng.choice(motif)} {rng.choice(hp)}, {rng.choice(col)}' for _ in range(80)]
    wr(wc, 'tattoo_henna', H)
    words = ['Forever', 'Always', 'Family', 'Strength', 'Believe', 'Beautiful', 'Courage', 'Freedom', 'Blessed', 'Destiny', 'Warrior', 'Faith']
    mistakes = ['with one letter swapped for a similar-looking letter so it reads wrongly spelled', 'with one letter doubled so it is visibly misspelled', 'with a letter missing in the middle so the word looks incomplete', 'with two letters reversed so the spelling is wrong', 'with the letters crowded together and uneven, the last letter squeezed against the edge', 'with a stray extra letter added at the end']
    flaws = ['wobbly uneven lines with thick and thin patches', 'blurred, blown-out ink spreading under the skin', 'a lopsided design where one side is bigger than the other', 'crooked baseline sloping downward across the skin', 'lines of varying depth with patchy faded gaps', 'a rushed, home-made look with shaky outlines']
    subj = ['a lopsided heart', 'a wonky rose with uneven petals', 'a skull with mismatched eye sockets', 'a crooked anchor', 'a barely recognisable animal with uneven proportions', 'a tribal pattern with uneven symmetry', 'a dragon with a deformed head', 'a clumsy butterfly with one wing smaller than the other']
    B = []
    for _ in range(60):
        B.append(f"a bad tattoo of the word {rng.choice(words)} {rng.choice(PLACE)}, {rng.choice(mistakes)}, with {rng.choice(flaws)}")
    for _ in range(60):
        B.append(f"a poorly done tattoo of {rng.choice(subj)} {rng.choice(PLACE)}, with {rng.choice(flaws)}, and the ink {rng.choice(['has faded to blue-grey', 'looks slightly raised', 'has spread softly at the edges', 'is uneven in darkness'])}")
    wr(wc, 'tattoo_bad', B)
    wr(wc, 'tattoo_novelty_random', ['__tattoo_temporary__', '__tattoo_henna__', '__tattoo_bad__'])
def run(final):
    n = strip_lora(final); female(final); male(final); teeth(final); tattoos(final); return n
AOO_FILES = ['f_body_labia_majora', 'f_body_vulva_tone', 'f_body_clitoris', 'f_body_clitoris_aroused', 'm_body_genitals_erect', 'teeth_access_high', 'teeth_access_mid', 'teeth_access_low', 'tattoo_temporary', 'tattoo_henna', 'tattoo_bad', 'lip_teeth']
def export_aoo(out):
    n = strip_lora(out)
    src = os.path.join(HERE, '..'); import tempfile
    tmp = tempfile.mkdtemp(); run_src = tmp
    for nm in AOO_FILES:
        pass
    # regenerate into a temp folder, then write unique lines as aoo_ files
    for fn in glob.glob(os.path.join(src, 'f_body_labia2.txt')): pass
    run_tmp = tmp; female(run_tmp); male(run_tmp); teeth(run_tmp); tattoos(run_tmp)
    for nm in AOO_FILES + ['m_body_genitals', 'f_body_clitoris']:
        p = os.path.join(run_tmp, nm + '.txt')
        if os.path.exists(p):
            seen = list(dict.fromkeys(l for l in open(p, encoding='utf8').read().split('\n') if l.strip()))
            seen = [re.sub(r'__([A-Za-z0-9_]+)__', lambda m: '__aoo_' + m.group(1) + '__' if os.path.exists(os.path.join(out, 'aoo_' + m.group(1) + '.txt')) else m.group(0), l) for l in seen]
            open(os.path.join(out, 'aoo_' + nm + '.txt'), 'w', encoding='utf8', newline='\n').write('\n'.join(seen) + '\n')
    for b in BR:
        seen = list(dict.fromkeys(l for l in open(os.path.join(run_tmp, f'age{b}_lip_teeth.txt'), encoding='utf8').read().split('\n') if l.strip()))
        open(os.path.join(out, f'aoo_age{b}_lip_teeth.txt'), 'w', encoding='utf8', newline='\n').write('\n'.join(seen) + '\n')
    return n
if __name__ == '__main__':
    a = [x for x in sys.argv[1:] if os.path.isdir(x)]; print('lora files cleaned:', run(os.path.abspath(a[0]) if a else FINAL))
