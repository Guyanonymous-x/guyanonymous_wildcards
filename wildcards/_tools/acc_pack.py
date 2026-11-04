"""Backpack-only extension: sculptural/experimental shapes, camping/frame/hauling/duffel utility packs, diverse materials and a very wide colour range."""
import re, itertools
from acc_expand import rngk, cap
from vocab_acc_a import GRADES, BAND, ADJ
import vocab_acc_pack as P

def colour_lines(n=1500):
    r = rngk('pack-colour'); out = set()
    def pick():
        b = r.choice(P.BASE)
        return (r.choice(P.MODC) + ' ' + b) if r.random() < 0.3 else b
    tries = 0
    while len(out) < n and tries < n * 20:
        tries += 1; a, b, c = pick(), pick(), pick()
        if len({a.split()[-1], b.split()[-1], c.split()[-1]}) < 3: continue
        out.add(r.choice(P.PATC).format(a=a, b=b, c=c))
    return sorted(out)

def sent_lines(items, frames, n, seed, pairs=True):
    r = rngk(*seed); out = set()
    for it in items:
        for f in frames: out.add(cap(f.format(it)))
    tries = 0
    while len(out) < n and tries < n * 12:
        tries += 1; k = r.choice((2, 2, 3)); parts = r.sample(items, k)
        j = ', '.join(parts[:-1]) + ' and ' + parts[-1]
        out.add(cap(r.choice(frames).format(j)))
    return sorted(out)

def mat_files(F):
    for g in GRADES:
        b = BAND[g]; r = rngk('pm', g)
        odd = [f'{m}, {c}' for m in P.MAT_ODD[b] for c in P.CONS_ODD[b]]; r.shuffle(odd)
        import acc_expand as E
        ex = E.ext_mat('bag', g, r, 600); ex2 = E.ext_mat('bag', g, rngk('pm2', g), 600)
        F[f'acc_backpack_mat_odd_{g}'] = sorted(set(odd[:420]) | ex)
        import vocab_acc_b as _B
        util = [f'{md} {m}, {c}' if md else f'{m}, {c}' for m in P.MAT_UTIL[b] for c in P.CONS_UTIL[b] for md in [''] + _B.MOD_FABRIC[g][:4]]; r.shuffle(util)
        F[f'acc_backpack_mat_util_{g}'] = sorted(set(util[:420]) | ex2)

def run(F):
    F['acc_backpack_colour'] = colour_lines()
    mat_files(F)
    F['acc_backpack_oddfeature'] = sent_lines(P.FEATURE_ODD, ['It has {}.', 'Its distinguishing feature is {}.', 'Notable details include {}.', 'It is fitted with {}.', 'It also carries {}.'], 600, ('of',))
    F['acc_backpack_oddstrap'] = sorted({cap(f.format(s)) for s in P.STRAP_ODD for f in ['It is carried with {}.', 'It rides on {}.', 'The carry system is {}.', 'It has {}.', 'Its straps: {}.']})
    F['acc_backpack_oddpose'] = sorted({cap(p) for p in P.PLACE_ODD})
    F['acc_backpack_frame'] = sorted({cap(f'It rides on {a} {b}.') for a in P.FRAME_ITEMS for b in P.FRAME_SUSP} | {cap(f'It is built around {a}, {b}.') for a in P.FRAME_ITEMS for b in P.FRAME_SUSP})
    F['acc_backpack_gear'] = sent_lines(P.GEAR, ['Strapped to the outside are {}.', 'Lashed to it are {}.', 'Carried on the outside are {}.', 'Clipped and strapped on are {}.'], 600, ('gr',))
    F['acc_backpack_utilfeature'] = sent_lines(P.UTILFEAT, ['It has {}.', 'Its features include {}.', 'It is built with {}.', 'Details include {}.'], 600, ('uf',))
    # clusters
    for g in GRADES:
        r = rngk('pc', g); adjs = list(ADJ[g])
        odd, util = set(), set()
        for name, form in P.SHAPES:
            for a in r.sample(adjs, 8):
                lead = ('an ' if a[0] in 'aeiou' else 'a ') + a
                odd.add(f"{lead} {name}, made of __acc_backpack_mat_odd_{g}__. {form} __acc_backpack_oddfeature__ __acc_backpack_oddstrap__")
                odd.add(f"{lead} {name}, made of __acc_backpack_mat_odd_{g}__. {form} __acc_backpack_oddfeature__")
            odd.add(f"__acc_adj_{g}__ {name}, made of __acc_backpack_mat_odd_{g}__. {form} __acc_backpack_oddfeature__ __acc_backpack_oddstrap__")
        for name, form in P.UTIL:
            for a in r.sample(adjs, 8):
                lead = ('an ' if a[0] in 'aeiou' else 'a ') + a
                util.add(f"{lead} {name}, made of __acc_backpack_mat_util_{g}__. {form} __acc_backpack_utilfeature__ __acc_backpack_gear__")
                util.add(f"{lead} {name}, made of __acc_backpack_mat_util_{g}__. {form} __acc_backpack_frame__ __acc_backpack_utilfeature__")
                util.add(f"{lead} {name}, made of __acc_backpack_mat_util_{g}__. {form} __acc_backpack_utilfeature__")
            util.add(f"__acc_adj_{g}__ {name}, made of __acc_backpack_mat_util_{g}__. {form} __acc_backpack_utilfeature__ __acc_backpack_gear__")
        F[f'acc_backpack_cluster_odd_{g}'] = sorted(odd); F[f'acc_backpack_cluster_util_{g}'] = sorted(util)
        tech = f'__acc_backpack_tech_{g}__'
        F[f'acc_backpack_prompt_odd_{g}'] = [f'__acc_backpack_cluster_odd_{g}__ __acc_backpack_design__, {tech}. __acc_backpack_oddpose__.', f'__acc_backpack_cluster_odd_{g}__ __acc_backpack_design__, {tech}. __acc_backpack_trim_{g}__ __acc_backpack_finish_{g}__ __acc_backpack_extras__', f'__acc_backpack_cluster_odd_{g}__ __acc_backpack_design__, {tech}. __acc_backpack_lining_{g}__ __acc_backpack_extras__', f'__acc_backpack_cluster_odd_{g}__ __acc_backpack_design__, {tech}.']
        F[f'acc_backpack_prompt_util_{g}'] = [f'__acc_backpack_cluster_util_{g}__ __acc_backpack_design__, {tech}. __acc_backpack_trim_{g}__ __acc_backpack_finish_{g}__', f'__acc_backpack_cluster_util_{g}__ __acc_backpack_design__, {tech}. __acc_backpack_extras__', f'__acc_backpack_cluster_util_{g}__ __acc_backpack_design__, {tech}. __acc_backpack_hardware_{g}__ __acc_backpack_lining_{g}__', f'__acc_backpack_cluster_util_{g}__ __acc_backpack_design__, {tech}.']
    F['acc_backpack_prompt'] = [f'__acc_backpack_prompt_{g}__' for g in GRADES] + [f'__acc_backpack_prompt_odd_{g}__' for g in GRADES] * 2 + [f'__acc_backpack_prompt_util_{g}__' for g in GRADES] * 2
    # design: every palette replaced by the wide colour list
    FR = [', with enamel accents in', ', with accents in', ', in shades of', ', finished in', ', coloured in']
    des = set(); trads = {}
    for l in F['acc_backpack_design']:
        left, _, motif = l.partition('; its signature detail is ')
        for fr in FR:
            if fr in left:
                who = left.split(fr)[0]; trads.setdefault(who, set()).add(motif); break
    r = rngk('pdes')
    for who, ms in trads.items():
        for m in sorted(ms):
            for fr in FR: des.add(f'{who}{fr} __acc_backpack_colour__; its signature detail is {m}')
    for name, pals, motifs in P.TRADS:
        art = 'an' if name[0] in 'aeiou' else 'a'
        for m in motifs:
            for fr in FR: des.add(f'Designed by {art} {name}{fr} __acc_backpack_colour__; its signature detail is {m}')
            for pal in pals: des.add(f'Designed by {art} {name}, coloured in {pal}; its signature detail is {m}')
    F['acc_backpack_design'] = sorted(des)
    return F
