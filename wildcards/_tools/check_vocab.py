"""Checks the expanded wildcards folder: option counts, forbidden characters, colour wording in non-colour files, and a sample of resolved prompts.
Usage: python check_vocab.py [wildcards_folder] [--prompts N] [--seed S]"""
import os, re, sys, random, collections
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from paths import FINAL
a = sys.argv[1:]; D = FINAL
for x in a:
    if os.path.isdir(x): D = os.path.abspath(x)
NP = int(a[a.index('--prompts') + 1]) if '--prompts' in a else 0
SEED = int(a[a.index('--seed') + 1]) if '--seed' in a else 1
REF = re.compile(r'__([A-Za-z0-9_\-/]+)__')
files = {}
for f in os.listdir(D):
    if f.endswith('.txt'): files[f[:-4]] = [l.rstrip('\n') for l in open(os.path.join(D, f), encoding='utf8', errors='replace')]
bad_chars = [(n, i) for n, ls in files.items() for i, l in enumerate(ls) if re.search(r'[{}|]', l)]
print('files', len(files), '| lines with { } |:', len(bad_chars), bad_chars[:3])
# counts for the source option files
SKIP = re.compile(r'^([fm]_)?(age\d|bt_|opt_inl|prompt_|shoe_|acc_shoe_|demo|grp)|^(shoe_|acc_shoe_|demo|grp)')
small = []
for n, ls in sorted(files.items()):
    if SKIP.match(n): continue
    nb = [l.strip() for l in ls if l.strip()]
    if any(REF.search(l) for l in nb[:50]): continue            # template / pointer files
    u = len(set(nb))
    if u < 200: small.append((u, n))
print(f'{len(small)} non-template source files below 200 distinct options:')
print(', '.join(f'{n}={u}' for u, n in sorted(small)))
# colour words in files that are not about colour
COL = re.compile(r'\b(black|white|red|blue|green|yellow|orange|purple|pink|brown|grey|gray|golden|silver|crimson|scarlet|violet|teal|turquoise|navy|beige|ivory|cream|tan|copper|bronze)\b', re.I)
COLFILE = re.compile(r'(color|colour|dem_tone|tone|hair_shine|lite_color|styl_color|outfit_pattern|clth_pattern|outfit_cosplay|countries|cosplay|names|mark_tattoo|mark_paint|mark_cyber|shoe|acc_glasses|make_|settings10000|creativeLocations|obj_|env_|acc_props|poses|prompt|opt_|clothing|outfit_|style_photographers|_age|^age|^bt_|facialExpr|health|dem_|hairstyle|hair_style|f_hair|m_hair)')
rows = []
for n, ls in sorted(files.items()):
    if COLFILE.search(n): continue
    nb = [l for l in ls if l.strip()]
    if not nb: continue
    hit = sum(1 for l in nb if COL.search(l))
    if hit: rows.append((hit, len(nb), n))
print('files with colour words outside colour files (hits/lines):', ', '.join(f'{n}:{h}/{t}' for h, t, n in sorted(rows, reverse=True)[:25]))
# prompt sample
def expand(line, rng, depth=0):
    if depth > 12: return line
    def sub(m):
        r = m.group(1); ls = [l for l in files.get(r, ['']) ]
        if r not in files: return f'<<MISSING {r}>>'
        return expand(rng.choice(ls), rng, depth + 1)
    return REF.sub(sub, line)
if NP:
    rng = random.Random(SEED)
    masters = [n for n in files if n in ('f_prompt_master', 'm_prompt_master', 'f_prompt_master_by_age', 'm_prompt_master_by_age')]
    for i in range(NP):
        m = rng.choice(masters); line = rng.choice([l for l in files[m] if l.strip()])
        p = expand(line, rng)
        print(f'\n[{i+1}] ({m})', ' '.join(p.split())[:1500])
