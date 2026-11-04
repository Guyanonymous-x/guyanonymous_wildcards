"""Anklet / ankle-height socks and odd, translucent and unusual sock materials (netting, fur, leather, rubber, metal, glass, feather...)."""
import re
from acc_expand import rngk
from vocab_acc_a import GRADES, BAND, ADJ
import vocab_acc_sock as K

def art(a): return ('an ' if a[0] in 'aeiou' else 'a ') + a
def run(F):
    F['acc_sock_length'] = sorted({f'{n}' for n, _ in K.STYLES} | {f'{n}. {f}' for n, f in K.STYLES})
    F['acc_sock_length_thigh'] = sorted({f'{n}' for n, _ in K.THIGH} | {f'{n}. {f}' for n, f in K.THIGH})
    F['acc_sock_length_ankle'] = sorted({f'{n}' for n, _ in K.ANKLE} | {f'{n}. {f}' for n, f in K.ANKLE})
    F['acc_sock_oddform'] = sorted(set(x.rstrip('.') + '.' for x in K.ODDFORM))
    for g in GRADES:
        b = BAND[g]; r = rngk('sockplus', g); adjs = list(ADJ[g])
        mats = {f'{m}, {c}' for m in K.ODD[b] for c in K.ODDCON[b]}
        if g in ('luxury', 'showpiece'):   # let the higher grades borrow the finest of the middle band too
            mats |= {f'{m}, {c}' for m in K.ODD['mid'] for c in K.ODDCON['high']}
        mats = sorted(mats); r.shuffle(mats); F[f'acc_sock_mat_odd_{g}'] = mats[:700]
        odd, ank, anko = set(), set(), set()
        for name, form in K.STYLES:
            for a in r.sample(adjs, 10):
                for _ in range(2):
                    odd.add(f"a pair of {a} {name}, made of __acc_sock_mat_odd_{g}__. {form} __acc_sock_oddform__")
                odd.add(f"a pair of {a} {name}, made of __acc_sock_mat_odd_{g}__. {form}")
        for name, form in K.ANKLE:
            for a in r.sample(adjs, 14):
                ank.add(f"a pair of {a} {name}, made of __acc_sock_mat_all_{g}__. {form}")
                anko.add(f"a pair of {a} {name}, made of __acc_sock_mat_odd_{g}__. {form} __acc_sock_oddform__")
        thi = set()
        for name, form in K.THIGH:
            for a in r.sample(adjs, 14):
                thi.add(f"a pair of {a} {name}, made of __acc_sock_mat_all_{g}__. {form}")
                thi.add(f"a pair of {a} {name}, made of __acc_sock_mat_odd_{g}__. {form} __acc_sock_oddform__")
                thi.add(f"a pair of {a} {name}, made of __acc_sock_mat_odd_{g}__. {form}")
        F[f'acc_sock_cluster_thigh_{g}'] = sorted(thi)
        F[f'acc_sock_cluster_odd_{g}'] = sorted(odd); F[f'acc_sock_cluster_ankle_{g}'] = sorted(ank | anko)
        tails = [f'In __acc_colour__. __acc_sock_trim_{g}__ __acc_sock_extras__', f'__acc_sock_design__, __acc_sock_tech_{g}__. __acc_sock_extras__', f'In __acc_colour__. __acc_sock_finish_{g}__ __acc_sock_extras__', f'__acc_sock_design__. __acc_sock_trim_{g}__ __acc_sock_lining_{g}__']
        F[f'acc_sock_prompt_odd_{g}'] = [f'__acc_sock_cluster_odd_{g}__ ' + t for t in tails]
        F[f'acc_sock_prompt_ankle_{g}'] = [f'__acc_sock_cluster_ankle_{g}__ ' + t for t in tails]
        F[f'acc_sock_prompt_thigh_{g}'] = [f'__acc_sock_cluster_thigh_{g}__ ' + t for t in tails]
    sh = set(F.get('acc_sock_short', []))
    for g in GRADES:
        r = rngk('sockshort', g); adjs = list(ADJ[g]); bases = list(K.ODD[BAND[g]])
        for name, _ in K.STYLES:
            for _i in range(8 if name in {n for n, _ in K.ANKLE + K.THIGH} else 4):
                sh.add(f"a pair of {r.choice(adjs)} {name} made of {r.choice(bases)}, coloured in __acc_colour__")
    F['acc_sock_short'] = sorted(sh)
    F['acc_sock_prompt'] = ([f'__acc_sock_prompt_{g}__' for g in GRADES] + [f'__acc_sock_prompt_novelty_{g}__' for g in GRADES] * 2
                            + [f'__acc_sock_prompt_odd_{g}__' for g in GRADES] * 3 + [f'__acc_sock_prompt_ankle_{g}__' for g in GRADES] * 3 + [f'__acc_sock_prompt_thigh_{g}__' for g in GRADES] * 3)
    # tidy doubled modifier words in every sock file
    for n in list(F):
        if n.startswith('acc_sock'): F[n] = [re.sub(r'\b([A-Za-z]{5,}) \1\b', r'\1', l) for l in F[n]]
    return F
