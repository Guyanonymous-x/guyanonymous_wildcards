"""Expansion layer for the accessory system: fills every slot file with authored vocabulary (vocab_acc_a/b) so no file is blank-only and each has 200+ distinct lines."""
import random, re, zlib, itertools
from vocab_acc_a import GRADES, BAND, ADJ, LEAD, WHIM, TAILS
import vocab_acc_b as B

def rngk(*k): return random.Random(zlib.crc32('|'.join(map(str, k)).encode()))
def cap(s): return s[:1].upper() + s[1:] if s else s
CLASS = {'backpack': ['bag'], 'purse': ['bag'], 'wallet': ['bag'], 'ring': ['metal'], 'bracelet': ['metal', 'bead'], 'necklace': ['metal', 'bead'], 'sock': ['knit'], 'cane': ['cane']}
BEAD_MODS = dict.fromkeys(B.GRADES if hasattr(B, 'GRADES') else GRADES, None)
BEAD_MOD = {'low': "lightweight, plain, smooth, uniform, glossy, painted, colour-coated, bright".split(', '), 'mid': "polished, matched, faceted, tumbled, frosted, smooth, graduated, hand-selected".split(', '), 'high': "hand-matched, flawless, luminous, graduated, hand-selected, deeply lustrous, rare, perfectly round".split(', ')}
HAT_MODS = {'straw': {'low': "lightweight, coarse, loosely woven, paper-thin, plain".split(', '), 'mid': "tightly woven, natural, soft, supple, fine".split(', '), 'high': "very fine, silk-soft, hand-plaited, gossamer, flawless".split(', ')},
            'fur': {'low': "plush, fluffy, thick, soft".split(', '), 'mid': "dense, supple, lustrous, thick-pile".split(', '), 'high': "silken, velvety, deep-pile, hand-selected, flawless".split(', ')},
            'cloth': {'low': "lightweight, plain, soft, coated".split(', '), 'mid': "brushed, tightly woven, soft-touch, washed".split(', '), 'high': "silken, hand-woven, lustrous, rich, hand-finished".split(', ')}}
HAT_CLASS_KEYS = [('straw', r'straw|raffia|sinamay|panama|palm|seagrass|sisal|jute|rush|paper'), ('fur', r'fur|shearling|sheepskin|fleece|mink|fox|sable'),
                  ('knit', r'knit|yarn|cashmere|alpaca|merino|lambswool|rib'), ('felt', r'felt|wool|melton|tweed|flannel|pounced')]
def hat_class(mats):
    t = ' '.join(mats).lower(); sc = {k: len(re.findall(p, t)) for k, p in HAT_CLASS_KEYS}; sc['cloth'] = 1
    return max(sc, key=lambda k: (sc[k], k != 'cloth'))

import vocab_acc_extrav as X
PLURAL = {'sock'}; PAIR = {'sock'}
TECHCLS = {'backpack': 'bag', 'purse': 'bag', 'wallet': 'bag', 'ring': 'metal', 'bracelet': 'metal', 'necklace': 'metal', 'sock': 'knit', 'cane': 'cane', 'hat': 'hat'}
EXCLS = {'bag': 'bag', 'metal': 'metal', 'bead': 'metal', 'knit': 'knit', 'cane': 'cane'}
def ext_mat(cls, g, r, n):
    if g not in ('luxury', 'showpiece'): return set()
    k = EXCLS.get(cls, 'hat') if cls != 'hat' else 'hat'
    items = list(X.EXMAT[k]); cons = list(X.EXCON[k]); out = set(); share = 0.7 if g == 'showpiece' else 0.25
    combos = [f'{i}, {c}' for i in items for c in cons]; r.shuffle(combos)
    return set(combos[:int(n * share)])
def mat_lines(c, cls_list, g, hatcls=None, target=420):
    band = BAND[g]; out = set(); r = rngk(c, 'mat', hatcls, g)
    for cls in (cls_list if not hatcls else [hatcls]):
        if hatcls: items = B.HAT_MATS['felt' if hatcls == 'felt' else hatcls][band]; cons = B.CONS['hat'][band]; mods = (B.MOD_FELT[g] if hatcls in ('felt',) else B.MOD_KNIT[g] if hatcls == 'knit' else HAT_MODS[hatcls][band])
        else:
            items = B.MATS[cls][band]; cons = B.CONS[cls][band]; mods = BEAD_MOD[band] if cls == 'bead' else B.MODS[cls][g]
        n = target // len(cls_list) if not hatcls else target
        if g == 'showpiece': n = int(n * 0.4)
        combos = [(m, i, k) for m in [''] + list(mods) for i in items for k in cons]; r.shuffle(combos)
        for m, i, k in combos[:n]: out.add(f"{(m + ' ') if m else ''}{i}, {k}")
        out.update(ext_mat('hat' if hatcls else cls, g, r, target // len(cls_list) if not hatcls else target))
    return out

def combine_lines(lib, items, target, seed):
    r = rngk(*seed); frames = lib['frames']; res = set()
    single = [f for f in frames]; multi = [f for f in frames if f == '{}.' or not f.startswith('{}')]
    def one(a, fr):
        if a[0].isupper() and fr != '{}.': return None
        return cap(fr.format(a))
    for a in items:
        for fr in single:
            x = one(a, fr)
            if x: res.add(x)
    def join(parts):
        if parts[0][0].isupper(): return '. '.join(parts)
        return ', '.join(parts[:-1]) + ' and ' + parts[-1] if len(parts) > 2 else ' and '.join(parts)
    tries = 0
    while len(res) < target and tries < target * 12:
        tries += 1; k = r.choice((2, 3, 4)); 
        if len(items) < k: continue
        parts = r.sample(items, k); fr = r.choice(multi)
        if parts[0][0].isupper():
            if any(not p[0].isupper() for p in parts): continue
            res.add(' '.join(p if p.endswith('.') else p + '.' for p in parts)); continue
        if any(p[0].isupper() for p in parts): continue
        res.add(cap(fr.format(join(parts))))
    return res

def slot_file(c, slot, g, existing, target=320, sub=None):
    libs = B.SLOTS[c]; lib = libs[slot] if slot != 'hardware' and slot != 'carry' else libs['hardware'][0 if slot == 'hardware' else 1]
    r = rngk(c, slot, g); items = list(lib[BAND[g]]); keep = max(6, int(len(items) * 0.85)); items = r.sample(items, min(keep, len(items)))
    out = set(existing) | combine_lines(lib, items, target, (c, slot, g, 'c'))
    if g in ('luxury', 'showpiece') and slot in ('trim', 'finish', 'interior') and c != 'contact':
        pool = {'trim': X.EXTRIM, 'finish': X.EXFIN, 'interior': X.EXLIN}[slot]; fr = lib['frames']; share = 0.7 if g == 'showpiece' else 0.25
        ext = set()
        for a in pool:
            for f in fr:
                if a[0].isupper() and f != '{}.': continue
                ext.add(cap(f.format(a)))
        for _ in range(int(target * share)):
            k = r.choice((1, 2, 3)); parts = r.sample(list(pool), k); fr_ = [f for f in fr if f == '{}.' or not f.startswith('{}')] or fr
            ext.add(cap(r.choice(fr_).format(', '.join(parts[:-1]) + (' and ' if k > 1 else '') + parts[-1])))
        out |= ext
    out.discard('')
    res = sorted(out); blanks = max(1, int(len(res) * (0.3 if slot in ('trim', 'finish') else 0.15)))
    return res + [''] * blanks

def tech_lines(c, g, existing, target=420):
    cls = TECHCLS[c]
    tl, pos = B.TECH[cls]; band = BAND[g]; r = rngk(c, 'tech', g); out = set(existing)
    mk = B.MAKERS[band]
    for t in tl[band]:
        out.add(t)
        for p in pos: out.add(f'{t} {p}')
    combos = [f'{t} {p}, {m}' for t in tl[band] for p in pos for m in mk]; r.shuffle(combos); out.update(combos[:max(0, target - len(out))])
    return sorted(out)

PMODS = "reinforced, hidden, padded, discreet, sturdy, concealed, neatly finished, well-placed, secure, slim, easily reached, double-stitched, tidy, roomy, unobtrusive, handy, smoothly working, firmly attached, carefully lined, compact, generously sized, quietly useful, well-positioned, tough".split(', ')
def pmod(item, m):
    if item.startswith(('a ', 'an ')):
        rest = item.split(' ', 1)[1]; return ('an ' if m[0] in 'aeiou' else 'a ') + m + ' ' + rest
    if item.startswith('the '): return 'the ' + m + ' ' + item[4:]
    return m + ' ' + item
def practical_files(c, pitems, witems):
    r = rngk(c, 'prw')
    base = sorted(set(pitems) | set(B.PRACT[c])); out = set(base)
    combos = [pmod(p, m) for p in base for m in PMODS]; r.shuffle(combos); out.update(combos[:max(0, 320 - len(out))])
    wb = sorted(set(witems) | set(WHIM)); w = set(wb)
    pl = B.PLACE[c]; wc = [f'{x} {p}' for x in wb for p in pl]; r.shuffle(wc); w.update(wc[:max(0, 360 - len(w))])
    return sorted(out), sorted(w)

def pairs(items, n, seed):
    r = rngk(*seed); out = set(); tries = 0
    while len(out) < n and tries < n * 10 and len(items) > 1:
        tries += 1; a, b = r.sample(items, 2); out.add(f'{a} and {b}')
    return sorted(out)

P_INTRO = ["Practical details include", "Useful features include", "It is also equipped with", "Built-in conveniences include", "For everyday use it offers", "Thoughtful touches include", "Functionally it provides", "It comes with", "Added for convenience is", "Its practical side includes"]
W_INTRO = ["Whimsical touches include", "A playful note comes from", "For fun it carries", "An unexpected detail is", "Its playful side shows in", "A touch of humour comes from", "Charmingly, it features", "A small surprise is"]
def extras_lines(c):
    pl = c in PLURAL; he = 'They' if pl else 'It'; ad = 'add' if pl else 'adds'; ba = 'balance' if pl else 'balances'
    P = [f'{i} __acc_{c}_practical_pair__.' for i in P_INTRO] + [f'{i} __acc_{c}_practical__.' for i in P_INTRO]
    W = [f'{i} __acc_{c}_whimsy_pair__.' for i in W_INTRO] + [f'{i} __acc_{c}_whimsy__.' for i in W_INTRO]
    out = P + W + [f'{p} {w}' for p in P for w in W]
    out += [f'Alongside __acc_{c}_practical__, {he.lower()} {ad} __acc_{c}_whimsy__ for playfulness.'] * 1 + [f'{he} {ba} __acc_{c}_practical__ with the whimsy of __acc_{c}_whimsy__.']
    if pl:
        for a, b in (('It is also', 'They are also'), ('Added for convenience is', 'Added for convenience are'), ('it offers', 'they offer'), ('It comes', 'They come'), ('it provides', 'they provide'), ('it ', 'they '), ('It ', 'They '), ('For everyday use they offer', 'For everyday use they offer')):
            out = [o.replace(a, b) for o in out]
        out = [o.replace('Functionally they provides', 'Functionally they provide').replace('they features', 'they feature') for o in out]
    out += ['__acc_artwork__'] * max(8, len(out) // 6)
    return out + [''] * (len(out) // 8)

def adj_files():
    ADV = "wonderfully, pleasantly, notably, genuinely, thoroughly, charmingly, distinctly, reassuringly, quietly, unmistakably, simply, deliberately".split(', ')
    F = {}
    for g in GRADES:
        base = list(ADJ[g]); r = rngk('adv', g); out = set(base)
        for a in base:
            for v in ADV: out.add(f'{v} {a}')
        F[g] = sorted(out)
    return F

SETTINGS = "on a plain neutral backdrop, against a softly blurred background, on a linen cloth, on a slab of stone, on a wooden tabletop, on a sheet of paper, on a velvet cushion, on a glass shelf, in a shop display, on a workbench, on a marble counter, against a studio sweep, under a single soft lamp, in natural window light, on a folded cloth, beside a few tools of the trade, on a mirrored surface, on a display stand, in a wooden tray, on an antique desk, on a rough canvas, on brushed metal, hung from a hook, on a bed of straw, in a lightbox, on a leather mat".split(', ')
def lead_lines():
    out = set(LEAD); 
    for l in LEAD:
        base = l[:-3] if l.endswith(' of') else l
        for s in SETTINGS: out.add(f'{base}, {s}, of')
    r = rngk('lead'); L = sorted(out); r.shuffle(L); return sorted(set(LEAD) | set(L[:420]))


def hat_fam_class(F, c, famid):
    cls = {}
    for fid in set(famid.values()):
        m = []
        for g in GRADES: m += F.get(f'acc_{c}_mat_{fid}_{g}', [])
        cls[fid] = hat_class(m)
    return cls

def expand_cat(c, F, tg, famid, pitems, witems):
    """tg: {(type, grade, pair): [list of other-sentence lists]}"""
    fids = sorted(set(famid.values())); hc = hat_fam_class(F, c, famid) if c == 'hat' else None
    for g in GRADES:
        for fid in fids:
            k = f'acc_{c}_mat_{fid}_{g}'
            F[k] = sorted(set(F[k]) - {'plain fabric, machine-sewn'} | mat_lines(c, CLASS.get(c, []), g, hc[fid] if hc else None, 420 if len(fids) == 1 else 300))
        F[f'acc_{c}_tech_{g}'] = tech_lines(c, g, [t for t in F[f'acc_{c}_tech_{g}'] if t != 'executed with care'])
        for slot, nm in (('trim', 'trim'), ('finish', 'finish'), ('interior', 'lining')):
            F[f'acc_{c}_{nm}_{g}'] = slot_file(c, slot, g, [l for l in F[f'acc_{c}_{nm}_{g}'] if l.strip()])
        F[f'acc_{c}_hardware_{g}'] = slot_file(c, 'hardware', g, [])
        if len(B.SLOTS[c]['hardware']) > 1: F[f'acc_{c}_carry_{g}'] = slot_file(c, 'carry', g, [])
    if c in ('bracelet', 'necklace'):
        BR = re.compile(r'pearl|bead|cord|thread|stone|crystal|jade|coral|shell|quartz|agate|silk|leather|hemp|lapis|turquoise|onyx|amber', re.I)
        TR = re.compile(r'bead|pearl|strand|stretch|string|cord|wrap|friendship|amulet|slider|rosary|prayer|charm', re.I)
        for g in GRADES:
            k = f'acc_{c}_mat_all_{g}'; old = [l for l in F[k] if l]
            bead = sorted({l for l in old if BR.search(l)} | mat_lines(c, ['bead'], g, None, 300)); metal = sorted({l for l in old if not BR.search(l)} | mat_lines(c, ['metal'], g, None, 300))
            F[k] = metal; F[f'acc_{c}_mat_bead_{g}'] = bead
            F[f'acc_{c}_cluster_{g}'] = [l.replace('_mat_all_', '_mat_bead_') if TR.search(l.split(', made of')[0]) else l for l in F[f'acc_{c}_cluster_{g}']]
    pr, wh = practical_files(c, pitems, witems)
    F[f'acc_{c}_practical'] = pr; F[f'acc_{c}_whimsy'] = wh
    F[f'acc_{c}_practical_pair'] = pairs(pr, 500, (c, 'pp')); F[f'acc_{c}_whimsy_pair'] = pairs(wh, 500, (c, 'wp'))
    F[f'acc_{c}_extras'] = extras_lines(c)
    # clusters: literal-adjective variants of observed types + extra item types with a form sentence
    pair = c in PAIR
    def fam_for(t):
        if c != 'hat': return fids[0]
        import re as _re
        for k, pat in B.HAT_FAMILY_KEYS.items():
            if _re.search(pat, t):
                for fid in fids:
                    if hc[fid] == k: return fid
        return fids[0]
    for g in GRADES:
        r = rngk(c, 'cl', g); adjs = list(ADJ[g]); cl = set(F[f'acc_{c}_cluster_{g}'])
        for (t, gg, p), lst in tg.items():
            if gg != g: continue
            fid = famid[t]
            for a in r.sample(adjs, 10):
                tail = r.choice(lst) if lst else []
                lead = ('a pair of ' + a) if p else (('an ' if a[0] in 'aeiou' else 'a ') + a)
                cl.add(f"{lead} {t}, made of __acc_{c}_mat_{fid}_{g}__." + (' ' + ' '.join(tail) if tail else ''))
        for t, form in B.TYPES[c]:
            fid = fam_for(t)
            pr_ = pair or form.startswith('They')
            cl.add(f"{'a pair of __acc_adjbare_%s__' % g if pr_ else '__acc_adj_%s__' % g} {t}, made of __acc_{c}_mat_{fid}_{g}__. {form}")
            for a in r.sample(adjs, 12):
                lead = ('a pair of ' + a) if pr_ else (('an ' if a[0] in 'aeiou' else 'a ') + a)
                cl.add(f"{lead} {t}, made of __acc_{c}_mat_{fid}_{g}__. {form}")
                cl.add(f"{lead} {t}, made of __acc_{c}_mat_{fid}_{g}__. {form} {'They also include' if pr_ else 'It also includes'} __acc_{c}_practical__.")
        if c in ('bracelet', 'necklace'):
            TR2 = re.compile(r'bead|pearl|strand|stretch|string|cord|wrap|friendship|amulet|slider|rosary|prayer|charm', re.I)
            cl = {l.replace('_mat_all_', '_mat_bead_') if TR2.search(l.split(', made of')[0]) else l for l in cl}
        F[f'acc_{c}_cluster_{g}'] = sorted(cl)
        carry = f' __acc_{c}_carry_{g}__' if f'acc_{c}_carry_{g}' in F else ''
        base = f'__acc_{c}_cluster_{g}__'
        F[f'acc_{c}_prompt_{g}'] = [f'{base} __acc_{c}_design__, __acc_{c}_tech_{g}__. __acc_{c}_extras__ __acc_{c}_trim_{g}__ __acc_{c}_finish_{g}__ __acc_{c}_lining_{g}__ __acc_{c}_hardware_{g}__{carry}',
                                    f'{base} __acc_{c}_design__, __acc_{c}_tech_{g}__. __acc_{c}_hardware_{g}__{carry} __acc_{c}_trim_{g}__ __acc_{c}_lining_{g}__ __acc_{c}_extras__',
                                    f'{base} __acc_{c}_design__, __acc_{c}_tech_{g}__. __acc_{c}_finish_{g}__ __acc_{c}_trim_{g}__ __acc_{c}_extras__',
                                    f'{base} __acc_{c}_design__, __acc_{c}_tech_{g}__. __acc_{c}_lining_{g}__ __acc_{c}_hardware_{g}__{carry} __acc_{c}_extras__ __acc_{c}_finish_{g}__',
                                    f'{base} __acc_{c}_design__, __acc_{c}_tech_{g}__. __acc_{c}_trim_{g}__ __acc_{c}_hardware_{g}__{carry} __acc_{c}_finish_{g}__ __acc_{c}_lining_{g}__ __acc_{c}_extras__']
    return F
