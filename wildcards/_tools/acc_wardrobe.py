"""Earrings, gloves, scarves and tights: four accessory families built to the same grade system as the other nine."""
import re
import acc_expand as E, vocab_acc_b as B, vocab_acc_extrav as X, vocab_acc_sock as K
import vocab_acc_wardrobe1 as W1, vocab_acc_wardrobe2 as W2
from acc_expand import rngk
from vocab_acc_a import GRADES, BAND, ADJ
from acc_pack import colour_lines

import vocab_acc_wardrobe3 as W3, vocab_acc_wardrobe4 as W4, vocab_acc_wardrobe5 as W5
MODMAP = {'metal': B.MOD_METAL, 'fabric': B.MOD_FABRIC, 'knit': B.MOD_KNIT}
FR = [', with enamel accents in', ', with accents in', ', in shades of', ', finished in', ', coloured in']
CFG = {}
def _add(names, cls, techc, pair, slots, pract, place, types, wear, plural=None):
    for c in names:
        CFG[c] = dict(cls=cls[c], tech=techc[c], pair=c in pair, plural=c in (plural if plural is not None else pair), slots=slots[c], pract=pract[c], place=place[c], types=types[c], wear=wear[c])
_add(W1.NEW, W1.CLS, {'ear': 'metal', 'glove': 'knit', 'scarf': 'knit', 'hose': 'knit'} and {c: {'ear': 'metal', 'glove': 'knit', 'scarf': 'knit', 'hose': 'knit'}[W1.CLS[c]] for c in W1.NEW}, W1.PAIR, W2.SLOTS, W2.PRACT, W2.PLACE, W2.TYPES, W2.WEAR, W1.PLURAL)
_add(W3.NEW, W3.CLS, W3.TECHC, W3.PAIR, W3.SLOTS, W3.PRACT, W3.PLACE, W3.TYPES, W3.WEAR)
_add(W4.NEW, W4.CLS, W4.TECHC, W4.PAIR, W4.SLOTS, W4.PRACT, W4.PLACE, W4.TYPES, W4.WEAR)
_add(W5.NEW, W5.CLS, W5.TECHC, W5.PAIR, W5.SLOTS, W5.PRACT, W5.PLACE, W5.TYPES, W5.WEAR)
NEW = list(CFG)
PLURALS = {c for c in NEW if CFG[c]['plural']}

def register():
    E.PLURAL |= PLURALS; E.PAIR |= {c for c in NEW if CFG[c]['pair']}
    B.MATS['lens'] = W5.MATS['lens']; B.CONS['lens'] = W5.CONS['lens']; B.MODS['lens'] = {g: ['clear', 'soft'] for g in GRADES}
    B.TECH['lens'] = W5.TECHLENS; X.EXMAT['lens'] = []; X.EXCON['lens'] = []
    for c in NEW:
        k = CFG[c]['cls']
        if k in W1.MATS: B.MATS[k] = W1.MATS[k]; B.CONS[k] = W1.CONS[k]; B.MODS[k] = MODMAP[W1.MODS[k]]
        E.CLASS[c] = [k]; E.EXCLS[k] = E.EXCLS.get(k, 'lens' if k == 'lens' else 'metal' if k == 'ear' else 'knit' if k == 'scarf' else 'bag')
        E.TECHCLS[c] = CFG[c]['tech']
        B.SLOTS[c] = CFG[c]['slots']; B.PRACT[c] = CFG[c]['pract']; B.PLACE[c] = CFG[c]['place']; B.TYPES[c] = CFG[c]['types']

def art(a): return ('an ' if a[0] in 'aeiou' else 'a ') + a

def build(c):
    F = {}
    for g in GRADES:
        F[f'acc_{c}_cluster_{g}'] = []; F[f'acc_{c}_mat_all_{g}'] = ['x']; F[f'acc_{c}_tech_{g}'] = ['x']
        for n in ('trim', 'finish', 'lining'): F[f'acc_{c}_{n}_{g}'] = ['x']
    E.expand_cat(c, F, {}, {t: 'all' for t, _ in CFG[c]['types']}, [], [])
    pl = CFG[c]['pair']; k = CFG[c]['cls']
    # design: tradition x frame x motif, plus the wide-colour variants come from acc_novelty.run
    r = rngk(c, 'design'); design = set()
    metal = CFG[c]['cls'] == 'ear' and c not in ('earring',) or c == 'earring'
    pat = r'smith|jewel|enamel|glass|carver|granulator|painter|designer|artisan|artist|maker|craftsperson|couturier' if metal else r'weaver|dyer|embroider|seamstress|tailor|lace|milliner|designer|artist|artisan|craftsperson|couturier|Maori|Polynesian|batik|tapa'
    if c == 'contact': pat = r'designer|artist|artisan|craftsperson|couturier|painter|glass'
    trads = [t for t in W2.TRAD if re.search(pat, t)]
    for _ in range(900):
        t = r.choice(trads); a = 'an' if t[0].lower() in 'aeiou' else 'a'
        design.add(f"Designed by {a} {t}{r.choice(FR)} {r.choice(colour_lines())}; its signature detail is {r.choice(W2.MOTIF)}")
    F[f'acc_{c}_design'] = sorted(design)
    # short phrases
    sh = set()
    for g in GRADES:
        rs = rngk(c, 'short', g); adjs = list(ADJ[g])
        for name, _ in CFG[c]['types']:
            for _i in range(6):
                lead = ('a pair of ' + rs.choice(adjs)) if pl else art(rs.choice(adjs))
                sh.add(f"{lead} {name} made of __acc_{c}_mat_all_{g}__, coloured in __acc_colour__")
    F[f'acc_{c}_short'] = sorted(sh)
    # odd / translucent / unusual materials
    for g in GRADES:
        b = BAND[g]; rs = rngk(c, 'odd', g); adjs = list(ADJ[g])
        src = W1.ODD[k] if k in W1.ODD and W1.ODD[k] else K.ODD
        mats = sorted({f'{m}, {cn}' for m in src[b] for cn in K.ODDCON[b]})
        rs.shuffle(mats); F[f'acc_{c}_mat_odd_{g}'] = mats[:500]
        cl = set()
        for name, form in CFG[c]['types']:
            for a in rs.sample(adjs, 6):
                lead = ('a pair of ' + a) if pl else art(a)
                cl.add(f"{lead} {name}, made of __acc_{c}_mat_odd_{g}__. {form}")
        F[f'acc_{c}_cluster_odd_{g}'] = sorted(cl)
        tails = [f'In __acc_colour__. __acc_{c}_trim_{g}__ __acc_{c}_extras__', f'__acc_{c}_design__, __acc_{c}_tech_{g}__. __acc_{c}_extras__',
                 f'In __acc_colour__. __acc_{c}_finish_{g}__ __acc_{c}_extras__', f'__acc_{c}_design__. __acc_{c}_trim_{g}__ __acc_{c}_finish_{g}__']
        F[f'acc_{c}_prompt_odd_{g}'] = [f'__acc_{c}_cluster_odd_{g}__ ' + t for t in tails]
    F[f'acc_{c}_prompt'] = [f'__acc_{c}_prompt_{g}__' for g in GRADES] * 2 + [f'__acc_{c}_prompt_odd_{g}__' for g in GRADES]
    import acc_novelty; acc_novelty.run(F, c)
    return F

def build_all():
    register(); files = {}
    for c in NEW: files.update(build(c))
    # tidy doubled words
    VB = {'carries': 'carry', 'has': 'have', 'comes': 'come', 'adds': 'add', 'offers': 'offer', 'provides': 'provide', 'balances': 'balance', 'features': 'feature', 'shows': 'show', 'includes': 'include', 'is': 'are'}
    def pf(n, l):
        if any(n.startswith(f'acc_{c}_') for c in PLURALS):
            l = re.sub(r'\b([Tt]hey) (carries|has|comes|adds|offers|provides|balances|features|shows|includes)\b', lambda m: m.group(1) + ' ' + VB[m.group(2)], l)
        return l
    for n in list(files): files[n] = [pf(n, l) for l in files[n]]
    for n in list(files): files[n] = [re.sub(r'\b([A-Za-z]{5,}) \1\b', r'\1', l) for l in files[n]]
    return files

def verbs():
    return {c: [v.format(f'__acc_{c}_short__') for v in CFG[c]['wear']] for c in NEW}
