"""Novelty and historical hats, funny novelty socks, and wide-colour designs for every accessory category."""
import re
from acc_expand import rngk, cap
from acc_pack import colour_lines, sent_lines
from vocab_acc_a import GRADES, BAND, ADJ
import vocab_acc_nov as N, vocab_acc_b as B, vocab_acc_extrav as X
from vocab_lib import S

NOV_MAT = {'low': S("polyester plush, craft foam, felt sheets, printed polyester, inflatable PVC, molded foam, cardboard and paper, polyester faux fur, nylon mesh, fleece, rubberized foam, plastic sheeting, shiny lamé, bonded fibre, sponge foam, vinyl, glitter fabric, tulle"),
           'mid': S("hand-sewn felt, knit acrylic with stuffing, wool-felt appliqué, crocheted cotton, painted papier-mâché, wire-framed fabric, resin parts on felt, sculpted and painted foam, hand-felted wool, faux fur over wire shaping, quilted cotton, painted wood, corduroy, canvas with hand-painted details, rope and cork, plush velvet"),
           'high': S("hand-sculpted felt with gold embroidery, hand-painted resin set with jewels, hand-beaded sculpture on a wire frame, lacquered papier-mâché with gold leaf, couture millinery feathers and silk flowers, hand-blown glass parts, hand-felted merino sculpture, 3D-printed resin with crystals, carved wood painted by hand, silk velvet over a wire form, porcelain details on velvet, hand-cut metal and enamel")}
HIST_MAT = {'low': S("cotton twill, wool-blend felt, acrylic felt, polyester straw, printed cotton, polyester velvet, cotton canvas, faux fur, polyester satin, flannel"),
            'mid': S("wool felt, lambskin, karakul-look pile, woven palm leaf, woven bamboo, cotton velvet, horsehair braid, silk faille, oilskin, boiled wool, tweed, sheepskin, hand-woven straw, embroidered cotton, linen"),
            'high': S("fine beaver-look felt, hand-woven toquilla straw, silk velvet brocade, gold-embroidered velvet, lacquered bamboo, real-look sable pelt, silk taffeta with hand-pleating, hand-embroidered silk, lambskin with silver mounts, hand-felted vicuña-look cloth, brocade with metallic thread")}

def mats(kind, g):
    b = BAND[g]; r = rngk('nm', kind, g); items = (NOV_MAT if kind == 'nov' else HIST_MAT)[b]; cons = B.CONS['hat'][b]
    out = {f'{i}, {c}' for i in items for c in cons}
    if g in ('luxury', 'showpiece'):
        e = [f'{i}, {c}' for i in X.EXMAT['hat'] for c in X.EXCON['hat']]; r.shuffle(e); out |= set(e[:260 if g == 'showpiece' else 90])
    return sorted(out)

def run(F, c):
    if c == 'hat':
        F['acc_hat_gimmick'] = sent_lines(N.GIMMICK_HAT, ['It has {}.', 'It is fitted with {}.', 'A funny detail: {}.', 'It comes with {}.'], 500, ('hg',))
        for g in GRADES:
            r = rngk('hn', g); adjs = list(ADJ[g]); F[f'acc_hat_mat_nov_{g}'] = mats('nov', g); F[f'acc_hat_mat_hist_{g}'] = mats('hist', g)
            nov, hist = set(), set()
            for name, form in N.NOV_HAT:
                for a in r.sample(adjs, 8):
                    lead = ('an ' if a[0] in 'aeiou' else 'a ') + a
                    nov.add(f"{lead} {name}, made of __acc_hat_mat_nov_{g}__. {form} __acc_hat_gimmick__")
                    nov.add(f"{lead} {name}, made of __acc_hat_mat_nov_{g}__. {form}")
            for name, form in N.HIST_HAT:
                for a in r.sample(adjs, 8):
                    lead = ('an ' if a[0] in 'aeiou' else 'a ') + a
                    hist.add(f"{lead} {name}, made of __acc_hat_mat_hist_{g}__. {form}")
                    hist.add(f"{lead} {name}, made of __acc_hat_mat_hist_{g}__. {form} __acc_hat_trim_{g}__")
            F[f'acc_hat_cluster_novelty_{g}'] = sorted(nov); F[f'acc_hat_cluster_hist_{g}'] = sorted(hist)
            F[f'acc_hat_prompt_novelty_{g}'] = [f'__acc_hat_cluster_novelty_{g}__ In __acc_colour__. __acc_hat_trim_{g}__ __acc_hat_finish_{g}__ __acc_hat_extras__', f'__acc_hat_cluster_novelty_{g}__ __acc_hat_design__, __acc_hat_tech_{g}__. __acc_hat_extras__', f'__acc_hat_cluster_novelty_{g}__ In __acc_colour__. __acc_hat_gimmick__']
            F[f'acc_hat_prompt_hist_{g}'] = [f'__acc_hat_cluster_hist_{g}__ __acc_hat_design__, __acc_hat_tech_{g}__. __acc_hat_trim_{g}__ __acc_hat_lining_{g}__ __acc_hat_extras__', f'__acc_hat_cluster_hist_{g}__ In __acc_colour__. __acc_hat_finish_{g}__ __acc_hat_extras__']
        F['acc_hat_prompt'] = [f'__acc_hat_prompt_{g}__' for g in GRADES] + [f'__acc_hat_prompt_novelty_{g}__' for g in GRADES] * 2 + [f'__acc_hat_prompt_hist_{g}__' for g in GRADES] * 2
    if c == 'sock':
        F['acc_sock_gimmick'] = sent_lines(N.GIMMICK_SOCK, ['They have {}.', 'They come with {}.', 'A funny detail: {}.', 'They are made with {}.'], 500, ('sg',))
        F['acc_sock_theme'] = sent_lines(N.SOCK_THEME, ['They are printed with {}.', 'They are knit with {} all over.', 'The pattern shows {}.', 'The theme is {}.', 'They show {} in a repeat.'], 700, ('st',))
        for g in GRADES:
            r = rngk('sn', g); adjs = list(ADJ[g]); nov = set()
            for name, form in N.NOV_SOCK:
                for a in r.sample(adjs, 8):
                    nov.add(f"a pair of {a} {name}, made of __acc_sock_mat_all_{g}__. {form} __acc_sock_gimmick__")
                    nov.add(f"a pair of {a} {name}, made of __acc_sock_mat_all_{g}__. {form} __acc_sock_theme__")
                    nov.add(f"a pair of {a} {name}, made of __acc_sock_mat_all_{g}__. {form}")
            F[f'acc_sock_cluster_novelty_{g}'] = sorted(nov)
            F[f'acc_sock_prompt_novelty_{g}'] = [f'__acc_sock_cluster_novelty_{g}__ In __acc_colour__. __acc_sock_trim_{g}__ __acc_sock_extras__', f'__acc_sock_cluster_novelty_{g}__ __acc_sock_design__, __acc_sock_tech_{g}__. __acc_sock_extras__', f'__acc_sock_cluster_novelty_{g}__ In __acc_colour__.']
        F['acc_sock_prompt'] = [f'__acc_sock_prompt_{g}__' for g in GRADES] + [f'__acc_sock_prompt_novelty_{g}__' for g in GRADES] * 3
        import acc_sockplus; acc_sockplus.run(F)
    # wide colours for every design file
    if c != 'backpack':
        FR = [', with enamel accents in', ', with accents in', ', in shades of', ', finished in', ', coloured in']; trads = {}
        for l in F[f'acc_{c}_design']:
            left, _, motif = l.partition('; its signature detail is ')
            for fr in FR:
                if fr in left: trads.setdefault(left.split(fr)[0], set()).add(motif); break
        add = {f'{who}{fr} __acc_colour__; its signature detail is {m}' for who, ms in trads.items() for m in sorted(ms) for fr in FR}
        F[f'acc_{c}_design'] = sorted(set(F[f'acc_{c}_design']) | add)
    return F
