"""Contradiction test: expands the create_ prompts many times and counts contradictions. python v42_contra.py [N] [target ...]"""
import re, sys, os, random, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from expand import load, expand, clean
from paths import wc_dir
N = int(sys.argv[1]) if len(sys.argv) > 1 and sys.argv[1].isdigit() else 200
files = load([wc_dir()])
T = [a for a in sys.argv[1:] if not a.isdigit()] or ['f_create_random_woman', 'm_create_random_man', 'any_create_random_person_base', 'f_create_random_woman_short', 'm_create_random_man_short',
     'any_create_random_person', 'any_create_random_person_short', 'f_create_random_woman_w_clothes', 'm_create_random_man_topless', 'f_create_random_woman_mismatched', 'm_create_random_man_unlinked']
AGE = re.compile(r'\b(\d{2,3}) years old')
OLDF = re.compile(r'youthful|freshness of early adulthood|smooth and unlined|unwrinkled|baby[- ]?faced|young adult|taut unlined', re.I)
YOUNGF = re.compile(r'\bfrail\b|very old|elderly|ancient-looking|(?<!un)wrinkled|age spots|liver spots|centenarian|senior|shrunken', re.I)
BALD = re.compile(r'\b(bald|balding|shaved head|hairless scalp|no hair on (?:the|their|his|her) head)\b', re.I)
HAIRSTYLE = re.compile(r'(?:-length hair|\bbraids?\b|\bbun\b|ponytail|\blayers\b|\bbangs\b|\bfringe\b|\bcurls\b|waves)', re.I)
TALL = re.compile(r'towering|very tall|tall stature|tall height|statuesque', re.I); SHORT = re.compile(r'compact squat short|very short|short height|short stature|diminutive', re.I)
THIN = re.compile(r'\b(emaciated|bird-boned|skeletal|very thin|frail)\b', re.I); BIG = re.compile(r'\b(very heavy|obese|massive|muscular and bulky|heavily muscled|bodybuilder)\b', re.I)
COLORS = 'black|brown|blonde|blond|red|auburn|grey|gray|white|silver|platinum|ginger|chestnut|raven|dark|light'
HAIRCOL = re.compile(r'\b(' + COLORS + r')[a-z\- ]{0,25}? hair\b', re.I)
LABEL = re.compile(r'(?<![\w])[A-Z][A-Za-z ]{2,30}: ')
DBL = re.compile(r'\b(a|an) (a|an) [a-z]')
GEND = re.compile(r'\b(she|he|her|his|him|woman|women|man|men|girl|boy|lady|gentleman|herself|himself)\b', re.I)
def checks(t, name):
    out = []; m = AGE.search(t); age = int(m.group(1)) if m else None
    realistic = not ('mismatched' in name or 'unlinked' in name)
    if age and realistic and age >= 60 and OLDF.search(t): out.append('old age with youthful skin words: ' + OLDF.search(t).group(0))
    if age and realistic and age < 45 and YOUNGF.search(t): out.append('young age with elderly words: ' + YOUNGF.search(t).group(0))
    if BALD.search(t) and HAIRSTYLE.search(t): out.append('bald and a hairstyle')
    if TALL.search(t) and SHORT.search(t): out.append('tall and short')
    if THIN.search(t) and BIG.search(t): out.append('thin and big')
    cols = {c.lower() for c in re.findall(r'\b(black|brown|blonde|blond|red|auburn|grey|gray|white|silver|platinum|ginger|raven)[a-z\-]* (?:[a-z\-]+ ){0,3}hair\b', t, re.I)}
    cols = {'grey' if c == 'gray' else ('blonde' if c == 'blond' else c) for c in cols}
    if len(cols) >= 3: out.append('3+ hair colours: ' + ','.join(sorted(cols)))
    if LABEL.search(t): out.append('label colon: ' + LABEL.search(t).group(0))
    if DBL.search(t): out.append('double article')
    if re.search(r'\.\.(?!\.)|,\s*,| ,|\s{2,}', t): out.append('punctuation')
    if name.startswith('any_create_random_person_base') or (name.startswith('any_create') and 'person' not in name.split('_create_random_')[1].split('_')[0]) :
        pass
    if name.startswith('any_create_random_person_base') and GEND.search(t): out.append('gendered word in any_ output: ' + GEND.search(t).group(0))
    return out
rng = random.Random(42); total = collections.Counter(); ex = {}
for name in T:
    if name not in files: print('missing', name); continue
    cnt = collections.Counter(); bad = 0
    for i in range(N):
        t = clean(expand(files, '__' + name + '__', rng)); r = checks(t, name)
        if r: bad += 1
        for x in r: k = x.split(':')[0]; cnt[k] += 1; ex.setdefault((name, k), x + ' | ' + t[:160])
    print(f'{name}: {bad}/{N} prompts with a problem', dict(cnt.most_common(6)))
    for k in list(cnt)[:3]: print('     e.g.', ex[(name, k)][:260])
