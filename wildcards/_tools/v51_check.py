"""v51 prompt-quality checker.  python v51_check.py [N] [entry ...]
No entries = a default panel (people, objects, rooms, poses, settings). Samples each entry point N times and reports the rate and an example per problem:
person contradictions, grammar (double words, a/an, orphan punctuation, label colons, pronoun clashes), item contradictions, setting contradictions."""
import re, sys, os, random, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from expand import load, expand, clean
from paths import wc_dir
AGE = re.compile(r'\b(\d{2,3}) years old')
OLDF = re.compile(r'youthful|freshness of early adulthood|smooth and unlined|unwrinkled|baby[- ]?faced|taut unlined', re.I)
YOUNGF = re.compile(r'very old|elderly|ancient-looking|(?<!un)wrinkled|age spots|liver spots|centenarian', re.I)
BALD = re.compile(r'\b(bald|balding|shaved bald head|hairless scalp)\b', re.I)
HAIRSTYLE = re.compile(r'(?:-length hair|\bbraids?\b|\bbun\b|ponytail|\blayers\b|\bbangs\b|\bfringe\b|\bcurls\b)', re.I)
TALL = re.compile(r'towering|very tall|tall stature|statuesque', re.I); SHORT = re.compile(r'very short|short stature|diminutive', re.I)
THIN = re.compile(r'\b(emaciated|bird-boned|skeletal|very thin)\b', re.I); BIG = re.compile(r'\b(very heavy|obese|massive|heavily muscled|bodybuilder)\b', re.I)
LABEL = re.compile(r'(?<![\w])[A-Z][A-Za-z ]{2,30}: ')
DBLART = re.compile(r'\b(a|an) (a|an|the) [a-z]', re.I)
DBLWORD = re.compile(r'\b([A-Za-z]{3,}) \1\b', re.I)
AAN_BAD = re.compile(r'\ba (?=[aeiou][a-z]{2})(?!uni|use|usu|one|eur|ubi)|\ban (?=[bcdfgjklmnpqrstvwxz][a-z]{2})(?!hour|honest|heir|honou?r)', re.I)
PUNCT = re.compile(r'\.\.(?!\.)|,\s*,|\s,|\s\.|,\.|\(\s|\s\)|^\s*[,.;]')
PRON = re.compile(r'\b(his|her|him|hers|himself|herself)\b', re.I)
SOFT = re.compile(r'\b(velvet|silk|plush|fleece|brushed cotton|woolly)\b', re.I); HARD = re.compile(r'\b(steel|iron|chrome|brass|copper|bronze|glass|ceramic|stone|marble|concrete)\b', re.I)
SIZEBAD = re.compile(r'\b(size|length|shape|type) is (a|an) [^.]*\b\1\b', re.I)
RAIN = re.compile(r'\b(rain|storm|downpour|drizzle|snow|blizzard|fog)\b', re.I); CLEAR = re.compile(r'\b(clear blue sky|cloudless|bright sunshine|harsh midday sun|blazing sun)\b', re.I)
NIGHT = re.compile(r'\b(night|midnight|moonlit|moonlight|after dark)\b', re.I); DAY = re.compile(r'\b(midday|noon|bright daylight|morning sun|afternoon sun|sunrise)\b', re.I)
IND = re.compile(r'\b(indoors|inside a|in a (?:living|bed|bath|kitchen)room|interior)\b', re.I); WEATHER_OUT = re.compile(r'\b(snowing|raining|windy)\b', re.I)
def checks(t, person):
    o = []
    m = AGE.search(t); age = int(m.group(1)) if m else None
    if person:
        if age and age >= 60 and OLDF.search(t): o.append('old age + youthful words')
        if age and age < 45 and YOUNGF.search(t): o.append('young age + elderly words')
        if BALD.search(t) and HAIRSTYLE.search(t): o.append('bald + hairstyle')
        if TALL.search(t) and SHORT.search(t): o.append('tall + short')
        if THIN.search(t) and BIG.search(t): o.append('thin + big')
        sx = {'f' if re.search(r'\b(she|her|hers|herself)\b', t, re.I) else '', 'm' if re.search(r'\b(he|him|his|himself)\b', t, re.I) else ''} - {''}
        if len(sx) == 2: o.append('mixed he/she pronouns')
    if LABEL.search(t): o.append('label colon')
    if DBLART.search(t): o.append('double article')
    if DBLWORD.search(t): o.append('repeated word')
    if AAN_BAD.search(t): o.append('a/an mismatch')
    if PUNCT.search(t): o.append('punctuation')
    if SIZEBAD.search(t): o.append('Its size is a ... size')
    if SOFT.search(t) and HARD.search(t) and re.search(r'(finish|surface) (is|of) [^.]*\b(velvet|silk|plush|fleece)', t, re.I) and re.search(r'\b(steel|iron|chrome|brass|glass|ceramic|stone|marble)\b[^.]*(finish|surface)', t, re.I): o.append('soft finish on hard material')
    if NIGHT.search(t) and DAY.search(t): o.append('night + day light')
    if RAIN.search(t) and CLEAR.search(t): o.append('rain + clear sky')
    return o
DEFAULT = [('any_create_random_person_w_clothes', 1), ('f_create_random_woman_w_clothes', 1), ('m_create_random_man_w_clothes', 1), ('pose_prompt', 0), ('setting_prompt', 0), ('room_prompt_full', 0),
           ('furn_built_prompt', 0), ('seat_prompt', 0), ('furn_beds_prompt', 0), ('furn_bathroom_prompt', 0), ('furn_kitchen_prompt', 0), ('home_electronics_prompt', 0), ('perfume_prompt', 0), ('acc_sunglasses_prompt', 0),
           ('interact_two_prompt', 0), ('liquid_prompt', 0), ('fit_random_prompt', 0)]
if __name__ == '__main__':
    N = int(next((a for a in sys.argv[1:] if a.isdigit()), 200)); ents = [(a, 1 if re.search(r'create_random|person', a) else 0) for a in sys.argv[1:] if not a.isdigit()] or DEFAULT
    files = load([wc_dir()]); rng = random.Random(51); tot = collections.Counter(); bad_all = n_all = 0
    for name, person in ents:
        if name not in files: print('missing', name); continue
        cnt = collections.Counter(); ex = {}; bad = 0
        for _ in range(N):
            t = clean(expand(files, '__' + name + '__', rng)); r = checks(t, person)
            if r: bad += 1
            for x in set(r): cnt[x] += 1; ex.setdefault(x, t)
        bad_all += bad; n_all += N; tot.update(cnt)
        print(f'{name}: {bad}/{N} ({100*bad//N}%)  {dict(cnt.most_common(5))}')
        for k in list(cnt)[:2]:
            m = re.search(r'.{0,70}' + {'punctuation': PUNCT.pattern, 'repeated word': DBLWORD.pattern, 'double article': DBLART.pattern, 'a/an mismatch': AAN_BAD.pattern, 'label colon': LABEL.pattern, 'Its size is a ... size': SIZEBAD.pattern}.get(k, '.') + r'.{0,50}', ex[k], re.I)
            print('     ', k, '|', (m.group(0) if m else ex[k][:120]).replace('\n', ' '))
    print(f'\nOVERALL {bad_all}/{n_all} prompts with a problem ({100*bad_all//max(n_all,1)}%)'); print(dict(tot.most_common()))
