"""Accessories, mobility/health aids, poses and settings conditioned on AGE and BODY TYPE.     (build_all.py step 'access'; run after 'age' and 'body')
  age<lo>_<hi>_acc_hats | acc_jewelry | acc_props        the 3 accessory lists re-weighted by age (nothing is dropped: every option stays in the file)
  age<lo>_<hi>_aids_<arch>      sentence-ready optional aids (cane, walker, wheelchair, hearing aid, brace ...) - blank = none; far more likely when old, frail or very heavy
  age<lo>_<hi>_aids             the same without body type
  age<lo>_<hi>_settings_<arch>  500 settings drawn from settings10000.txt, weighted by age and body type (nightclub vs church, gym vs bench ...)
  age<lo>_<hi>_prompt_setting_<arch>        the prompt_setting template pointing at that file
  age<lo>_<hi>_pose_action_<arch> | pose_twist_<arch> | pose_weight_<arch>   poses weighted by age (already) x body type
  age<lo>_<hi>_prompt_pose_expression_<arch>   the pose/expression template pointing at those files
<arch> = thin slim avg athl curvy heavy vheavy musc frail.  clothing_build.py uses all of these in the per-age, per-body-type master prompts."""
import os, sys, random, re, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from paths import wc_dir
from gender import pron
from age_model import *
from body_model import ARCH
from wcbuild import allocate
WC = wc_dir(); N = 500
def rl(n): return [l.rstrip('\r\n') for l in open(os.path.join(WC, n + '.txt'), encoding='utf8', errors='replace')]
def write(n, lines, seed=None):
    if seed is not None: random.Random(seed).shuffle(lines)
    open(os.path.join(WC, n + '.txt'), 'w', encoding='utf8', newline='\n').write('\n'.join(lines) + '\n')
def wsample(R, items, weights, k):         # weighted sample WITHOUT replacement (Efraimidis-Spirakis)
    keys = sorted(((R.random() ** (1.0 / max(w, 1e-9)), i) for i, w in enumerate(weights)), reverse=True)[:k]
    return [items[i] for _, i in keys]
def kw_spec(table, t, default=FLAT):
    t = t.lower()
    for k, sp in table:
        if k in t: return sp
    return default
# ---------------- accessories by age ----------------
ACC_AGE = [('baby bottle', P(33, 8, .05)), ("child's toy", P(35, 9, .05)), ('teddy bear', D(40, 12, .2)), ('skateboard', D(30, 8, .03)), ('smartphone', D(60, 15, .3)), ('handheld game', D(32, 9, .04)),
  ('headphones', D(52, 15, .15)), ('frisbee', D(40, 12, .08)), ('water gun', D(30, 8, .03)), ('kite', D(45, 14, .15)), ('spray', D(38, 10, .1)), ('selfie', D(45, 14, .1)), ('sketchbook', D(55, 15, .3)), ('drone', D(50, 14, .1)),
  ('gym bag', D(55, 14, .2)), ('backpack', D(45, 14, .2)), ('yoga mat', D(58, 14, .3)), ('football', D(40, 12, .1)), ('tennis', D(55, 15, .25)),
  ('cane', U(72, 7, .005, 5)), ('walking', U(60, 12, .1, 2)), ('pocket watch', U(60, 12, .05, 3)), ('reading glasses', U(52, 10, .03, 3)), ('knitting', U(60, 12, .02, 4)), ('crochet', U(60, 12, .02, 4)), ('newspaper', U(50, 14, .1, 2)),
  ('pill', U(60, 12, .02, 3.5)), ('rosary', U(60, 14, .05, 3)), ('prayer beads', U(55, 14, .1, 2)), ('crossword', U(55, 12, .03, 3)), ('magnif', U(65, 10, .02, 3)), ('embroidery', U(55, 14, .05, 3)), ('diary', U(50, 14, .1, 2)),
  ('thermos', U(50, 14, .2, 1.8)), ('folded umbrella', U(45, 15, .3, 1.4)), ('garden', U(45, 14, .1, 2)), ('watering can', U(50, 14, .1, 2.2)), ('shawl', U(60, 12, .1, 2.5)), ('handkerchief', U(60, 12, .05, 2.5)), ('pipe', U(55, 14, .05, 2.5)),
  ('briefcase', P(45, 14, .2)), ('stethoscope', P(40, 14, .1)), ('diploma', D(30, 8, .03)), ('hearing', U(65, 10, .01, 3)), ('beaded', FLAT)]
HAT_AGE = [('baseball cap', D(55, 16, .3)), ('backwards', D(30, 8, .05)), ('beanie', D(55, 16, .3)), ('fascinator', U(40, 15, .15, 1.8)), ('pillbox', U(55, 14, .05, 2.5)), ('fedora', U(40, 15, .3, 1.6)), ('bowler', U(55, 14, .05, 2.5)),
  ('newsboy', U(45, 14, .15, 1.8)), ('panama', U(45, 14, .3, 1.5)), ('bucket', D(45, 14, .3)), ('bandana', D(48, 15, .2)), ('headscarf', U(45, 16, .3, 1.5)), ('trapper', U(40, 16, .3, 1.4)), ('hood', D(40, 12, .1)), ('no hat', FLAT)]
JEW_AGE = [('wedding band', U(30, 8, .02, 2.5)), ('pearl', U(45, 14, .1, 2.2)), ('diamond', U(40, 15, .3, 1.6)), ('plastic', D(30, 9, .05)), ('wooden beaded', D(35, 12, .15)), ('ear cuffs', D(40, 12, .08)), ('nose', D(35, 10, .05)),
  ('choker', D(38, 12, .1)), ('gothic', D(40, 12, .1)), ('skull', D(45, 14, .15)), ('hoop', D(55, 18, .3)), ('stacked', D(55, 16, .25)), ('turquoise', FLAT), ('gold chain', U(40, 15, .3, 1.6)), ('antique', U(50, 16, .15, 2)), ('brooch', U(55, 12, .02, 3.5)),
  ('no jewelry', FLAT)]
def age_acc():
    for fn, table in (('acc_props', ACC_AGE), ('acc_hats', HAT_AGE), ('acc_jewelry', JEW_AGE)):
        lines = [l for l in rl(fn) if l.strip()]; uniq = list(dict.fromkeys(lines)); cnt = collections.Counter(lines)
        for bi, b in enumerate(BRACKETS):
            wts = [cnt[o] * Kbracket(kw_spec(table, o), b) for o in uniq]
            if len(uniq) > 1500:                     # long file: sample 1500 distinct options for this age
                pick = wsample(random.Random(bi * 7 + 1), uniq, wts, 1500); lines_out = pick
            else:
                c = allocate(wts, max(len(uniq) * 2, 100)); lines_out = [o for o, k in zip(uniq, c) for _ in range(k)]
            write(f"{bname(b)}_{fn}", lines_out, seed=bi + 40)
# ---------------- aids ----------------
def A(text, sp, arch=None, base=1.0): return (text, sp, arch or {}, base)
AIDS = [A("She uses a wooden walking cane.", U(70, 7, .01, 5), {'frail': 3, 'heavy': 1.5, 'vheavy': 2.2, 'athl': .3, 'musc': .3}, 3),
  A("She walks with an adjustable aluminium cane.", U(72, 7, .01, 4), {'frail': 3, 'vheavy': 2}, 2), A("She leans on a four-wheeled rollator walker with a seat.", U(78, 6, .005, 5), {'frail': 3, 'vheavy': 2.5}, 2),
  A("She pushes a two-wheeled walking frame.", U(80, 6, .005, 5), {'frail': 3.5, 'vheavy': 2}, 1.5), A("She uses forearm crutches.", FLAT, {}, .8), A("She sits in a manual wheelchair.", U(68, 10, .05, 3.5), {'frail': 3, 'vheavy': 3, 'heavy': 1.6, 'athl': .5}, 2),
  A("She sits in a motorised mobility scooter.", U(68, 9, .01, 4), {'vheavy': 5, 'heavy': 2.2, 'frail': 2.5}, 1.5), A("She wears a hearing aid behind one ear.", U(58, 8, .02, 4), {}, 3), A("She wears hearing aids in both ears.", U(68, 7, .01, 4), {}, 2),
  A("She has a clear nasal cannula connected to a small portable oxygen tank.", U(72, 8, .005, 4), {'frail': 3.5, 'vheavy': 2.2, 'heavy': 1.4}, 1.2), A("She wears a supportive knee brace.", FLAT, {'heavy': 2, 'vheavy': 3, 'athl': 1.6, 'musc': 1.3}, 1.5),
  A("She wears a back brace under her clothing.", U(45, 14, .1, 2), {'heavy': 1.6, 'vheavy': 2.2, 'musc': 1.4}, 1), A("She wears a wrist splint.", FLAT, {}, 1), A("She wears a medical-alert bracelet.", U(48, 14, .1, 2.2), {'frail': 1.5}, 1.2),
  A("She wears thick compression stockings.", U(52, 12, .1, 2.5), {'heavy': 1.8, 'vheavy': 2.5, 'frail': 1.4}, 1.2), A("She wears orthopaedic shoes.", U(60, 10, .05, 3), {'heavy': 1.4, 'vheavy': 1.8, 'frail': 1.6}, 1.5),
  A("She holds a small pill organiser.", U(60, 10, .02, 3), {'frail': 1.8}, 1), A("She wears reading glasses on a cord around her neck.", U(52, 10, .02, 3), {}, 2), A("She holds a large magnifying glass.", U(70, 8, .01, 3), {'frail': 1.5}, .8),
  A("She wears a fitness tracker on one wrist.", D(55, 14, .2), {'athl': 2.5, 'musc': 1.8, 'slim': 1.3, 'heavy': .6, 'frail': .1}, 2), A("She wears a smart watch.", D(65, 16, .2), {'athl': 1.5}, 2),
  A("She has an insulin pump clipped at her hip.", FLAT, {'heavy': 1.8, 'vheavy': 2.5}, 1), A("She uses a white cane for the blind.", FLAT, {}, .4), A("She is accompanied by a guide dog in a harness.", FLAT, {}, .3),
  A("She wears a prosthetic leg.", FLAT, {}, .4), A("She wears a prosthetic hand.", FLAT, {}, .3), A("She wears a sports headband and wristbands.", D(45, 12, .05), {'athl': 3, 'musc': 2, 'heavy': .4, 'vheavy': .15, 'frail': .02}, 1),
  A("She wears an ankle support.", D(60, 15, .25), {'athl': 1.8, 'heavy': 1.4}, .8), A("She carries a folding stool to sit on when tired.", U(65, 10, .01, 4), {'frail': 3, 'vheavy': 2.5}, .8),
  A("She wears a hospital wristband.", FLAT, {'frail': 2}, .4), A("She wears a neck pillow around her shoulders.", FLAT, {}, .5), A("She wears a lightweight sun hat and a cooling towel around her neck.", U(35, 15, .3, 1.5), {'vheavy': 1.5, 'heavy': 1.3}, .8)]
ANY_P = [.015, .02, .03, .05, .09, .18, .34, .52, .65]          # share of people at that age with any visible aid
ARCH_P = {'thin': 1.1, 'slim': .7, 'avg': 1.0, 'athl': .5, 'curvy': 1.2, 'heavy': 1.8, 'vheavy': 3.0, 'musc': .6, 'frail': 3.2}
def aids():
    for bi, b in enumerate(BRACKETS):
        for a in ARCH + [None]:
            wts = [t[3] * Kbracket(t[1], b) * (t[2].get(a, 1.0) if a else 1.0) for t in AIDS]
            share = min(.97, ANY_P[bi] * (ARCH_P[a] if a else 1.0)); n = 400; n_any = round(n * share)
            c = allocate(wts, max(n_any, len(AIDS)))
            lines = [pron(t[0]) for t, k in zip(AIDS, c) for _ in range(k)]
            lines = lines[: max(n_any, len(AIDS))] if n_any >= len(AIDS) else lines
            lines += [''] * max(0, n - len(lines))
            write(f"{bname(b)}_aids_{a}" if a else f"{bname(b)}_aids", lines, seed=bi * 10 + (ARCH.index(a) if a else 99))
# ---------------- body type multipliers for poses and settings ----------------
ATH = {'athl': 2.2, 'musc': 1.9, 'slim': 1.3, 'thin': .9, 'avg': 1, 'curvy': .6, 'heavy': .35, 'vheavy': .12, 'frail': .04}
FRAIL = {'frail': 2.5, 'thin': 1.3, 'avg': .9, 'athl': .2, 'musc': .2, 'slim': .8, 'curvy': 1, 'heavy': 1, 'vheavy': 1.2}
SED = {'heavy': 1.6, 'vheavy': 2.0, 'curvy': 1.3, 'athl': .8, 'musc': .9, 'frail': 1.3, 'thin': .9}
LOWBODY = {'vheavy': .2, 'heavy': .5, 'frail': .25, 'curvy': .8, 'athl': 1.2, 'musc': 1.1}
POSE_ARCH = [('running', ATH), ('mid-jump', ATH), ('dancing', ATH), ('crouching low in dynamic', ATH), ('striding', ATH), ('dynamic', ATH), ('extreme', ATH), ('athletic', ATH), ('springy', ATH), ('light-footed', ATH), ('power pose', {'athl': 1.6, 'musc': 1.8, 'vheavy': .5, 'frail': .1}),
  ('stumbling', FRAIL), ('unsteady', FRAIL), ('huddled', FRAIL), ('cowering', FRAIL), ('hunched', FRAIL), ('leaning heavily', FRAIL), ('unbalanced', FRAIL), ('off-balance', FRAIL), ('staggering', FRAIL),
  ('kneeling', LOWBODY), ('perched', LOWBODY), ('crouch', LOWBODY), ('lying down', {'vheavy': .6, 'frail': .7}), ('sitting cross-legged', LOWBODY),
  ('lounging', SED), ('slouch', SED), ('sprawled', SED), ('heavy', SED), ('sitting', SED), ('leaning', SED), ('resting', SED), ('sinking', SED)]
SET_AGE = [('nightclub', D(36, 9, .02)), ('rave', D(32, 8, .01)), ('dorm', D(26, 5, .01)), ('hostel', D(34, 9, .03)), ('lecture hall', D(30, 7, .02)), ('gaming cafe', D(36, 9, .05)), ('rooftop party', D(40, 10, .05)),
  ('street racing', D(38, 9, .02)), ('pillow fight', D(34, 8, .03)), ('mosh', D(30, 8, .03)), ('karaoke', D(50, 14, .15)), ('fight club', D(42, 10, .05)), ('basketball court', D(45, 12, .08)), ('ski slope', D(55, 14, .1)),
  ('open-air gym', D(52, 14, .1)), ('capsule hotel', FLAT), ('burlesque', D(52, 14, .1)), ('strip club', D(48, 12, .05)), ('hostess bar', D(48, 12, .05)), ('dive bar', D(55, 14, .2)), ('cocktail lounge', D(60, 16, .3)),
  ('carnival', D(55, 16, .3)), ('tomato fight', D(40, 10, .05)), ('holi', D(50, 14, .2)), ('new year', D(60, 16, .3)), ('speakeasy', D(60, 16, .3)), ('skate', D(30, 8, .03)), ('arcade', D(40, 10, .1)),
  ('retirement', U(66, 8, .005, 6)), ('nursing', U(76, 7, .002, 8)), ('church', U(45, 14, .3, 2.2)), ('synagogue', U(45, 14, .3, 2)), ('orthodox church', U(45, 14, .3, 2.2)), ('funeral', U(45, 14, .3, 2)), ('cemetery', U(50, 14, .25, 2.2)),
  ('hospital ward', U(55, 14, .25, 2.5)), ('clinic', U(55, 14, .3, 2)), ('library', U(45, 15, .4, 1.6)), ('museum', U(50, 15, .4, 1.5)), ('tea house', U(45, 15, .4, 1.6)), ('tea ceremony', U(45, 15, .4, 1.6)), ('farmers', U(40, 15, .4, 1.5)),
  ('orchard', U(45, 15, .4, 1.5)), ('garden', U(50, 15, .3, 2)), ('porch', U(55, 14, .25, 2.2)), ('domino', U(58, 12, .1, 3)), ('mahjong', U(55, 12, .1, 3)), ('chess', U(55, 14, .15, 2.5)), ('golf', U(52, 14, .15, 2.5)),
  ('polo ground', U(40, 15, .2, 2)), ('auction', U(50, 14, .15, 2.5)), ('wine cellar', U(42, 14, .2, 1.8)), ('fine-dining', U(40, 14, .25, 1.8)), ('opera', U(48, 14, .1, 3)), ('yacht', U(42, 14, .15, 2)), ('cricket', U(48, 15, .3, 1.6)),
  ('penthouse', U(40, 14, .2, 1.6)), ('bathhouse', U(50, 15, .3, 1.5)), ('bench', U(55, 14, .25, 1.8)), ('village schoolroom', FLAT)]
SET_BODY = [('gym', ATH), ('boxing', ATH), ('muay thai', ATH), ('ski slope', ATH), ('swimming pool', {'athl': 1.8, 'slim': 1.3, 'heavy': .8, 'vheavy': .5, 'frail': .3}), ('dragon boat', ATH), ('rowing', ATH), ('charity race', ATH), ('football', ATH),
  ('basketball', ATH), ('trail', {'athl': 1.8, 'musc': 1.5, 'heavy': .45, 'vheavy': .2, 'frail': .08, 'curvy': .8}), ('mountain', {'athl': 1.8, 'musc': 1.5, 'heavy': .45, 'vheavy': .15, 'frail': .06}), ('glacier', {'athl': 1.8, 'vheavy': .1, 'frail': .05, 'heavy': .4}),
  ('volcano', {'athl': 1.8, 'vheavy': .1, 'frail': .05, 'heavy': .4}), ('dunes', {'athl': 1.6, 'vheavy': .15, 'frail': .05, 'heavy': .4}), ('steep stairway', {'athl': 1.6, 'vheavy': .1, 'frail': .05, 'heavy': .4}), ('rice terraces', {'athl': 1.5, 'vheavy': .2, 'frail': .08, 'heavy': .5}),
  ('coral reef', {'athl': 1.8, 'vheavy': .3, 'frail': .05}), ('waterfall', {'athl': 1.6, 'vheavy': .25, 'frail': .06}), ('refuge', {'athl': 1.6, 'vheavy': .2, 'frail': .06}), ('campsite', {'athl': 1.4, 'vheavy': .5, 'frail': .15}),
  ('sumo', {'heavy': 3, 'vheavy': 5, 'musc': 2, 'athl': .5, 'frail': .01, 'thin': .05, 'slim': .1}), ('buffet', SED), ('diner', SED), ('food court', SED), ('fast food', SED), ('noodle', SED), ('dumpling', SED), ('hawker', SED), ('kitchen', SED),
  ('bakery', SED), ('dim sum', SED), ('pub', SED), ('tea house', {'frail': 1.6, 'vheavy': 1.3}), ('library', {'frail': 1.6, 'vheavy': 1.3}), ('church', {'frail': 1.5, 'vheavy': 1.3}), ('clinic', {'frail': 1.6, 'vheavy': 1.3}), ('porch', {'frail': 1.6, 'vheavy': 1.4}),
  ('bench', {'frail': 1.8, 'vheavy': 1.5, 'heavy': 1.3}), ('museum', {'frail': 1.5, 'vheavy': 1.2}), ('hospital ward', {'frail': 2.2, 'vheavy': 1.5})]
def kw_mult(table, text, arch):
    m = 1.0; t = text.lower()
    for k, d in table:
        if k in t: m *= d.get(arch, 1.0)
    return max(m, 0.003)
def kw_age(table, text, b):
    m = 1.0; t = text.lower()
    for k, sp in table:
        if k in t: m *= Kbracket(sp, b)
    return m
def settings():
    src = [l.strip() for l in rl('settings10000') if l.strip()]
    ps = [l for l in rl('prompt_setting') if l.strip()]
    for bi, b in enumerate(BRACKETS):
        age_w = [kw_age(SET_AGE, s, b) for s in src]
        for ai, a in enumerate(ARCH):
            wts = [aw * kw_mult(SET_BODY, s, a) for aw, s in zip(age_w, src)]
            write(f"{bname(b)}_settings_{a}", wsample(random.Random(bi * 100 + ai + 5), src, wts, N), seed=bi * 100 + ai)
            write(f"{bname(b)}_prompt_setting_{a}", [l.replace('__settings10000__', f"__{bname(b)}_settings_{a}__") for l in ps])
def poses():
    for bi, b in enumerate(BRACKETS):
        p = bname(b)
        for f in ('pose_action', 'pose_twist', 'pose_weight'):
            lines = [l.strip() for l in rl(f"{p}_{f}") if l.strip()]; cnt = collections.Counter(lines); uniq = list(cnt)
            for a in ARCH:
                c = allocate([cnt[o] * kw_mult(POSE_ARCH, o, a) for o in uniq], N)
                write(f"{p}_{f}_{a}", [o for o, k in zip(uniq, c) for _ in range(k)], seed=bi * 1000 + ARCH.index(a) * 10 + len(f))
        tpl = [l for l in rl(f"{p}_prompt_pose_expression") if l.strip()]
        for a in ARCH:
            out = []
            for l in tpl:
                for f in ('pose_action', 'pose_twist', 'pose_weight'): l = l.replace(f"__{p}_{f}__", f"__{p}_{f}_{a}__")
                out.append(l)
            write(f"{p}_prompt_pose_expression_{a}", out)
if __name__ == '__main__':
    age_acc(); aids(); settings(); poses(); print('accessory / aids / setting / pose layer written')
