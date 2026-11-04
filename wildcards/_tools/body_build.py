"""Builds the body-type layer.  python body_build.py <source_dir> <prompts_dir> <age_wildcards_dir> <out_dir>"""
import re, csv, random, collections
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from paths import wc_dir, DATA, TOOLS, gender
from gender import IS_M, pron
WC = wc_dir(); TPL = os.path.join(DATA, 'src_templates_m' if gender() == 'm' else 'src_templates'); AUDIT = os.path.join(TOOLS, 'audit'); os.makedirs(AUDIT, exist_ok=True)
from wcbuild import allocate
from body_model import *
import supplements as SUPPL, statistics
SRC = AGEWC = OUT = WC; PROMPTS = TPL; N = 1000
FILES = "body_build body_compos body_bones body_ratio body_proprtn musc_shldr musc_arms musc_chest musc_abs musc_hips musc_legs musc_veins neck_length neck_muscle neck_clav neck_crease".split()
PILOT_WEIGHTED = {'body_build'}
def rl(p): return [l.strip() for l in open(p, encoding='utf8', errors='replace').read().split('\n')]
def uniq(p):
    c = collections.OrderedDict()
    for l in rl(p):
        if l: c[l] = c.get(l, 0) + 1
    return c
def write(name, lines, seed=None):
    if seed is not None: random.Random(seed).shuffle(lines)
    open(os.path.join(OUT, name + '.txt'), 'w', encoding='utf8', newline='\n').write('\n'.join(lines) + '\n')
FLAT_FACTOR = 0.35      # options that say nothing about build (asymmetry, scars, alignment...) are incidental features, so rarer
AGE_EXP = 0.7           # soften the age kernel inside an archetype so rare archetype/age pairings stay coherent
banded = {}; report = []; seed = 0
for f in FILES:
    counts = uniq(os.path.join(SRC, f + '.txt')); opts = list(counts)
    base = {o: base_weight(f, o, counts if f in PILOT_WEIGHTED else None) for o in opts}
    cs = {o: coords(o, f) for o in opts}; sp = {o: spec_for(f, o)[0] for o in opts}
    sw = statistics.mean(counts.values()) if f in PILOT_WEIGHTED else 1.0
    for o, t in SUPPL.options(f):                       # extra old-age (O2/O3) and obese (H2/H3) options
        if o in base: continue
        opts.append(o); base[o] = sw; cs[o] = supp_coords(f, o); sp[o] = SUPPL.spec_for_supp(t)
    banded[f] = any(s[0] != 'flat' for s in sp.values())
    for a in ARCH:
        for band in (['y', 'm', 'o'] if banded[f] else ['-']):
            w = [base[o] * (FLAT_FACTOR if cs[o] is None else 1.0) * arch_kernel(cs[o], a) * ((Kband(sp[o], band) if band != '-' else 1.0) ** AGE_EXP) for o in opts]
            cnt = allocate(w, N); lines = []
            for o, c in zip(opts, cnt): lines += [o] * c
            name = f"bt_{a}_{band}_{f}" if band != '-' else f"bt_{a}_{f}"
            seed += 1; write(name, lines, seed)
            for o, c in zip(opts, cnt): report.append((f, o, a, band, round(c / N * 100, 2)))
def ref(f, a, band): return f"bt_{a}_{band}_{f}" if banded[f] else f"bt_{a}_{f}"
# ---- per (archetype, age bracket) body templates ----
tpl = [l for l in rl(os.path.join(PROMPTS, 'prompt_char_body.tpl')) if l]
for b in BRACKETS:
    p = bname(b); band = BAND_OF[b]
    for a in ARCH:
        out = []
        for l in tpl:
            def sub(m):
                r = m.group(1)
                if r == 'body_height': return f"__{p}_body_height__"
                if r in FILES: return f"__{ref(r, a, band)}__"
                return m.group(0)
            out.append(re.sub(r'__([A-Za-z0-9_\-]+?)__', sub, l))
        write(f"bt_{a}_{p}_prompt_char_body", out)
    # picker replaces the bracket's body section (keeps the same file name the age master already calls)
    cnt = allocate(SHARE[b], 1000); lines = []
    for a, c in zip(ARCH, cnt): lines += [f"__bt_{a}_{p}_prompt_char_body__"] * c
    write(f"{p}_prompt_char_body", lines, seed=7)
    # face templates: drop the neck sentence (neck now lives in the body section, where it follows the body type)
    face = open(os.path.join(AGEWC, f"{p}_prompt_char_face.txt"), encoding='utf8').read()
    face = face.replace(" Her neck is __neck_length__ with __neck_clav__.", "")
    open(os.path.join(OUT, f"{p}_prompt_char_face.txt"), 'w', encoding='utf8', newline='\n').write(face)
with open(os.path.join(AUDIT, 'body_affinity_audit_' + gender() + '.csv'), 'w', newline='', encoding='utf8') as fh:
    w = csv.writer(fh); w.writerow(['file', 'option', 'archetype', 'age_band', 'percent_in_file']); w.writerows(report)
print('built', len(os.listdir(OUT)), 'files; banded:', {f: banded[f] for f in FILES})
