"""Builds the age-conditioned wildcard layer. Run:  python age_build.py <source_wildcards_dir> <prompts_dir> <out_dir>
source_wildcards_dir = folder with your (cleaned) wildcard files; for weighted files it reads existing line counts as base weights."""
import re, csv, random, math, collections, zlib
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from paths import wc_dir, DATA, TOOLS, gender
from gender import IS_M, pron
WC = wc_dir(); TPL = os.path.join(DATA, 'src_templates_m' if gender() == 'm' else 'src_templates'); AUDIT = os.path.join(TOOLS, 'audit'); os.makedirs(AUDIT, exist_ok=True)
from wcbuild import allocate
from age_model import *
import supplements as SUPPL, statistics
SRC = OUT = WC; PROMPTS = TPL
N = 1000
PILOT_WEIGHTED = {'eye_color','hair_color','hair_texture','body_build','body_height','skin_wrinkle','facial_hair'}   # files whose line counts already encode likelihood
FILES = """skin_wrinkle skin_texture skin_glow skin_marks head_cheek head_jaw head_temple nose_crease eye_lid eye_lash eye_brow neck_crease neck_muscle
lip_fullness lip_cupid lip_corners lip_teeth lip_gums hair_color hair_texture hair_volume hair_line hair_shine body_build body_height body_compos body_bones
musc_arms musc_abs musc_chest musc_hips musc_legs musc_shldr musc_veins hand_fingers hand_knuckl hand_nails hand_feet eye_sclera eye_color pose_action pose_twist pose_weight""".split() + (['facial_hair'] if IS_M else [])

def read_lines(path): return [l.strip() for l in open(path, encoding='utf8', errors='replace').read().split('\n')]
def uniq_counts(path):
    c = collections.OrderedDict()
    for l in read_lines(path):
        if l: c[l] = c.get(l, 0) + 1
    return c
def write(name, lines, shuffle_seed=None):
    if shuffle_seed is not None: random.Random(shuffle_seed).shuffle(lines)
    open(os.path.join(OUT, name + '.txt'), 'w', encoding='utf8', newline='\n').write('\n'.join(lines) + '\n')
def build_weighted(opts, weights, total, none=0, min_each=1):
    cnt = allocate(weights, total - none, min_each); lines = []
    for o, c in zip(opts, cnt): lines += [o] * c
    return lines + [''] * none, dict(zip(opts, cnt))

report = []
# ---- 1. attribute files per bracket ----
for f in FILES:
    counts = uniq_counts(os.path.join(SRC, f + '.txt'))
    opts = list(counts)
    base = {o: base_weight(f, o, counts if f in PILOT_WEIGHTED else None) for o in opts}
    specs = {o: spec_for(f, o) for o in opts}
    sw = statistics.mean(counts.values()) if f in PILOT_WEIGHTED else 1.0
    for o, t in SUPPL.options(f):                       # extra very-old options (obese options live in the body-type layer)
        if t in ('O2', 'O3') and o not in base:
            opts.append(o); base[o] = sw; specs[o] = (SUPPL.spec_for_supp(t), 'supplement')
    for bi, b in enumerate(BRACKETS):
        w = [base[o] * Kbracket(specs[o][0], b) for o in opts]
        lines, cnt = build_weighted(opts, w, max(N, 4 * len(opts)), min_each=0 if len(opts) > 60 else 1)
        write(f"{bname(b)}_{f}", lines, shuffle_seed=zlib.crc32(f'{f}{bi}'.encode()) & 0xffff)
        tot = sum(cnt.values())
        for o in opts: report.append((f, o, specs[o][1], specs[o][0], base[o], bname(b), round(cnt[o] / tot * 100, 2)))

# ---- 2. age (years) per bracket ----
K_DECAY = [0, 0, 0, 0, 0.02, 0.05, 0.09, 0.22, 0.30]
for bi, b in enumerate(BRACKETS):
    ages = list(range(b[0], b[1] + 1))
    lines, _ = build_weighted([age_phrase(a) for a in ages], [math.exp(-K_DECAY[bi] * (a - b[0])) for a in ages], 2000)
    write(f"{bname(b)}_age_years", lines, shuffle_seed=bi)

# ---- 3. optional sentence files: tattoos and eyewear (blank = none) ----
tat = uniq_counts(os.path.join(WC, 'opt_tattoo.txt')); tat_opts = list(tat)
TAT_MULT = [1.1, 1.5, 1.5, 1.15, 0.8, 0.45, 0.25, 0.12, 0.06]
norm = sum(s / 100 * m for s, m in zip(BRACKET_SHARE, TAT_MULT)); OVERALL_TATTOOED = 12.0
for bi, b in enumerate(BRACKETS):
    share = OVERALL_TATTOOED * TAT_MULT[bi] / norm
    w = []
    for o in tat_opts:
        k = 1.0
        if 'faded' in o: k = Kbracket(U(50, 12, .1, 2.5), b)
        if 'fresh' in o: k = Kbracket(D(40, 10, .2), b)
        w.append(k)
    NT = 2500; none = min(round(NT * (100 - share) / 100), NT - len(tat_opts))
    lines, _ = build_weighted(tat_opts, w, NT, none); write(f"{bname(b)}_opt_tattoo", lines, shuffle_seed=100 + bi)

# ---- 3b. aging_summary: one sentence per image that states how old the person LOOKS (so 62 and 92 are not rendered alike) ----
import aging_text
for bi, b in enumerate(BRACKETS):
    write(f"{bname(b)}_aging_summary", [pron(x) for x in aging_text.lines(bi, 400)], shuffle_seed=300 + bi)
# ---- 4. per-bracket templates (re-pointing every age-linked reference to the bracket's own file) ----
COND = set(FILES) | {'opt_tattoo', 'aging_summary'}   # eyewear: acc_glasses is re-pointed to <bracket>_opt_eyewear (written by eyewear_build.py)
SECTIONS = ['prompt_char_identity_anchored', 'prompt_char_identity_independent', 'prompt_char_face', 'prompt_char_hair', 'prompt_char_skin',
            'prompt_char_body', 'prompt_char_details', 'prompt_char_physical', 'prompt_wardrobe', 'prompt_pose_expression']
def retarget(line, b):
    p = bname(b)
    def sub(m):
        r = m.group(1)
        if r == 'dem_age': return f"__{p}_age_years__"
        if r == 'acc_glasses': return f"__{p}_opt_eyewear__"
        if r in ('acc_hats', 'acc_jewelry', 'acc_props'): return f"__{p}_{r}__"
        if r == 'aids': return f"__{p}_aids__"
        if r in COND or r in SECTIONS: return f"__{p}_{r}__"
        return m.group(0)
    return re.sub(r'__([A-Za-z0-9_\-]+?)__', sub, line)
for b in BRACKETS:
    for sec in SECTIONS:
        lines = [l for l in read_lines(os.path.join(PROMPTS, sec + '.tpl')) if l]
        if sec.startswith('prompt_char_identity'): lines = [l + ' __aging_summary__' for l in lines]
        if sec == 'prompt_wardrobe': lines = [l + ' __aids__' for l in lines]
        write(f"{bname(b)}_{sec}", [retarget(l, b) for l in lines])
    p = bname(b)
    write(f"{p}_prompt_master", [
        f"__prompt_style__ __{p}_prompt_char_physical__ __{p}_prompt_wardrobe__ __{p}_prompt_pose_expression__ __prompt_setting__ __prompt_camera_light__",
        f"__{p}_prompt_char_physical__ __{p}_prompt_wardrobe__ __{p}_prompt_pose_expression__ __prompt_setting__ __prompt_camera_light__ __prompt_style__",
        f"__prompt_setting__ __{p}_prompt_char_physical__ __{p}_prompt_wardrobe__ __{p}_prompt_pose_expression__ __prompt_camera_light__ __prompt_style__"])
# ---- 5. picker: population-weighted bracket selection ----
cnt = allocate(BRACKET_SHARE, 1000); lines = []
for b, c in zip(BRACKETS, cnt): lines += [f"__{bname(b)}_prompt_master__"] * c
write('prompt_master_by_age', lines, shuffle_seed=9)
# ---- 6. audit CSV ----
with open(os.path.join(AUDIT, 'age_affinity_audit_' + gender() + '.csv'), 'w', newline='', encoding='utf8') as fh:
    wr = csv.writer(fh); wr.writerow(['file', 'option', 'tag_source', 'age_spec', 'base_weight', 'bracket', 'percent_in_bracket']); wr.writerows(report)
print('built', len(os.listdir(OUT)), 'files')
