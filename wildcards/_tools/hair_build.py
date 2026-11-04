"""Builds the hair-type layer.  python hair_build.py <merged_wildcards_dir> <out_dir>"""
import re, csv, random, collections
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from paths import wc_dir, DATA, TOOLS, gender
from gender import IS_M, pron
WC = wc_dir(); TPL = os.path.join(DATA, 'src_templates_m' if gender() == 'm' else 'src_templates'); AUDIT = os.path.join(TOOLS, 'audit'); os.makedirs(AUDIT, exist_ok=True)
from wcbuild import allocate
from hair_model import *
SRC = OUT = WC; N = 1000
def rl(p): return [l.rstrip('\r\n') for l in open(p, encoding='utf8', errors='replace').read().split('\n')]
def uniq(p):
    c = collections.OrderedDict()
    for l in rl(p):
        l = l.strip()
        if l: c[l] = c.get(l, 0) + 1
    return c
def write(name, lines, seed=None):
    if seed is not None: random.Random(seed).shuffle(lines)
    open(os.path.join(OUT, name + '.txt'), 'w', encoding='utf8', newline='\n').write('\n'.join(lines) + '\n')
def fill(opts, w, total):
    total = max(total, 4 * len(opts)); cnt = allocate(w, total, 0 if len(opts) > 60 else 1); out = []
    for o, c in zip(opts, cnt): out += [o] * c
    return out
seed = 0
def nxt():
    global seed; seed += 1; return seed
# 1. ethnic lines split by hair type
eth = [l.strip() for l in rl(os.path.join(SRC, 'countries_ethnic_prompts.txt')) if l.strip()]
by = {T: [] for T in TYPES}; audit = []
for l in eth:
    t, s = line_type(l); by[t].append(l); audit.append((t, s, l))
for T in TYPES: write(f"countries_ethnic_prompts_{T}", by[T])
ANCH = [len(by[T]) / len(eth) * 100 for T in TYPES]
with open(os.path.join(AUDIT, 'hair_type_audit_' + gender() + '.csv'), 'w', newline='', encoding='utf8') as fh:
    w = csv.writer(fh); w.writerow(['hair_type', 'how_decided', 'ethnic_line']); w.writerows(audit)
# 2. curl per type
curl = list(uniq(os.path.join(SRC, 'hair_curl.txt')))
for T in TYPES:
    opts = [curl[i] for i, t in ORIG_CURL.items() if t == T] + [o for o, _ in CURL_NEW[T]]
    w = [CURL_ORIG_W[i] for i, t in ORIG_CURL.items() if t == T] + [x for _, x in CURL_NEW[T]]
    try:     # vocabulary expansion: more natural-language curl descriptions per hair type (each at 45% of the average original weight)
        import vocab_people as _vp
        _have = {o.lower() for o in opts}; _avg = sum(w) / len(w)
        for _o in _vp.CURL_TYPE[T]:
            if _o.lower() not in _have: opts.append(_o); w.append(_avg * 0.45)
    except ImportError:
        pass
    write(f"hair_curl_{T}", fill(opts, w, N), nxt())
# 3. texture / volume per type (x age bracket) - all 28 options kept at least once in every file
tex = uniq(os.path.join(SRC, 'hair_texture.txt')); vol = uniq(os.path.join(SRC, 'hair_volume.txt'))
def basew(f, o, counts, pil): return base_weight(f, o, counts if pil else None)
for T in TYPES:
    for f, cnts, tab, pil, short in (('hair_texture', tex, TEX_AFF, True, 'hairtex'), ('hair_volume', vol, VOL_AFF, False, 'hairvol')):
        opts = list(cnts); sp = {o: spec_for(f, o)[0] for o in opts}
        write(f"{short}_{T}", fill(opts, [basew(f, o, cnts, pil) * aff(tab, o, T) for o in opts], N), nxt())
        for b in BRACKETS:
            write(f"{bname(b)}_{short}_{T}", fill(opts, [basew(f, o, cnts, pil) * aff(tab, o, T) * Kbracket(sp[o], b) for o in opts], N), nxt())
# 4. hairstyles (originals once each where compatible, rest sampled from the grammar)
def style_file(T, b, n, rng):
    keep = [o for o, ts in ORIG_STYLE.items() if T in ts]
    return keep + [gen_style(T, b, rng) for _ in range(n - len(keep))]
for T in TYPES:
    for b in BRACKETS:
        write(f"{bname(b)}_hairstyle_{T}", style_file(T, b, N, random.Random(nxt())), nxt())
    rng = random.Random(nxt()); keep = [o for o, ts in ORIG_STYLE.items() if T in ts]; lines = keep[:]
    while len(lines) < N: lines.append(gen_style(T, rng.choices(BRACKETS, weights=BRACKET_SHARE, k=1)[0], rng))
    write(f"hairstyle_{T}", lines, nxt())
# global hair_style.txt rebuilt (2500 lines, all 28 originals kept)
rng = random.Random(nxt()); lines = list(ORIG_STYLE)
while len(lines) < 2500:
    T = rng.choices(TYPES, weights=[INDEP_SHARE[t] for t in TYPES], k=1)[0]
    lines.append(gen_style(T, rng.choices(BRACKETS, weights=BRACKET_SHARE, k=1)[0], rng))
write('hair_style', lines, nxt())
# 5. templates
HAIR_M = ["His hair has __hair_line__, and he wears it as __hair_style__. The curl pattern is __hair_curl__, and the strands are __hair_texture__, with __hair_volume__ and __hair_shine__.{ His hair is moving: __hair_motion__.|||}", "He wears __hair_style__. His hair has __hair_curl__, and the hair itself shows __hair_texture__, __hair_volume__ and __hair_shine__. At the forehead there is __hair_line__.", "His hairstyle is __hair_style__. The curl pattern is __hair_curl__, the texture is __hair_texture__, and the hair has __hair_volume__ with __hair_shine__; the hairline shows __hair_line__.{ His hair is moving: __hair_motion__.||||}"]
ident = [l for l in rl(os.path.join(TPL, 'prompt_char_identity_anchored.tpl')) if l.strip()]
hair = [  # rewritten so a style ending in "with a center part" never runs into a second "with ..."
 "Her hair has __hair_line__ with __hair_baby__, and she wears it as __hair_style__. The curl pattern is __hair_curl__, and the strands are __hair_texture__, with __hair_volume__ and __hair_shine__.{ Her hair is moving: __hair_motion__.|||}",
 "She wears __hair_style__. Her hair has __hair_curl__, and the hair itself shows __hair_texture__, __hair_volume__ and __hair_shine__. At the forehead there is __hair_line__ with __hair_baby__.",
 "Her hairstyle is __hair_style__. The curl pattern is __hair_curl__, the texture is __hair_texture__, and the hair has __hair_volume__ with __hair_shine__; the hairline shows __hair_line__.{ Her hair is moving: __hair_motion__.||||}"]
if IS_M: hair = HAIR_M
def retarget(l, mp): return re.sub(r'__([A-Za-z0-9_\-]+?)__', lambda m: f"__{mp[m.group(1)]}__" if m.group(1) in mp else m.group(0), l)
def physical(prefix, T, anchored):
    idn = f"__{prefix}prompt_char_identity_anchored_{T}__" if anchored else f"__{prefix}prompt_char_identity_independent__"
    return f"{idn} __{prefix}prompt_char_face__ __{prefix}prompt_char_hair_{T}__ __{prefix}prompt_char_skin__ __{prefix}prompt_char_body__ __{prefix}prompt_char_details__"
def phys_lines(prefix):
    ca = allocate(ANCH, 500); ci = allocate([INDEP_SHARE[t] for t in TYPES], 500); out = []
    for T, c in zip(TYPES, ca): out += [physical(prefix, T, True)] * c
    for T, c in zip(TYPES, ci): out += [physical(prefix, T, False)] * c
    return out
for b in BRACKETS:
    p = bname(b)
    for T in TYPES:
        write(f"{p}_prompt_char_identity_anchored_{T}", [retarget(l, {'countries_ethnic_prompts': f'countries_ethnic_prompts_{T}', 'dem_age': f'{p}_age_years'}) for l in ident])
        write(f"{p}_prompt_char_hair_{T}", [retarget(l, {'hair_style': f'{p}_hairstyle_{T}', 'hair_curl': f'hair_curl_{T}', 'hair_texture': f'{p}_hairtex_{T}', 'hair_volume': f'{p}_hairvol_{T}', 'hair_line': f'{p}_hair_line', 'hair_shine': f'{p}_hair_shine'}) for l in hair])
    cnt = allocate([INDEP_SHARE[t] for t in TYPES], 1000); pick = []
    for T, c in zip(TYPES, cnt): pick += [f"__{p}_prompt_char_hair_{T}__"] * c
    write(f"{p}_prompt_char_hair", pick, nxt())
    write(f"{p}_prompt_char_physical", phys_lines(p + '_' if False else f"{p}_"), nxt())
for T in TYPES:
    write(f"prompt_char_identity_anchored_{T}", [retarget(l, {'countries_ethnic_prompts': f'countries_ethnic_prompts_{T}'}) for l in ident])
    write(f"prompt_char_hair_{T}", [retarget(l, {'hair_style': f'hairstyle_{T}', 'hair_curl': f'hair_curl_{T}', 'hair_texture': f'hairtex_{T}', 'hair_volume': f'hairvol_{T}'}) for l in hair])
cnt = allocate([INDEP_SHARE[t] for t in TYPES], 1000); pick = []
for T, c in zip(TYPES, cnt): pick += [f"__prompt_char_hair_{T}__"] * c
write('prompt_char_hair', pick, nxt())
write('prompt_char_physical', phys_lines(''), nxt())
short = [l for l in rl(os.path.join(TPL, 'prompt_char_physical_short.tpl')) if l.strip()]
assert len(short) == 3 and '__hair_style__' in short[0]
lines = []
for l, shares in zip(short, (ANCH, [INDEP_SHARE[t] for t in TYPES], ANCH)):
    for T, c in zip(TYPES, allocate(shares, 333)):
        l = l.replace(' in __hair_style__', ', styled as __hair_style__')
        lines += [retarget(l, {'countries_ethnic_prompts': f'countries_ethnic_prompts_{T}', 'hair_style': f'hairstyle_{T}', 'hair_texture': f'hairtex_{T}'})] * c
write('prompt_char_physical_short', lines, nxt())
print('built', len(os.listdir(OUT)), 'files | anchored type shares', {TNAME[t]: round(a, 1) for t, a in zip(TYPES, ANCH)})
