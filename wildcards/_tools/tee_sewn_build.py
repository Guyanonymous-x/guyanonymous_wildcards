"""Sewn T-shirts (uniform_tee_sewn*): the T-shirt itself is a real cut-and-sew garment made as the uniform, from panels of fabric stitched together (sewn collar, lapels, pockets, buttons, belts and trims, colour-blocked in the outfit's colours) - not a print on a plain shirt.
Files: uniform_tee_sewn_<group>[_<male|female|sexy_male|sexy_female>], uniform_tee_sewn[_<version>], uniform_tee_sewn_gendered, uniform_tee_sewn_random;  parts uniform_tee_sewn_fabric, uniform_tee_sewn_assembly, uniform_tee_sewn_note
Adult wording, deterministic."""
import os, sys, re, random, zlib, shutil
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from paths import FINAL
import uniform_build as ub
from uniform_build import U, rows, variant, rg, art, cap, VLABEL
import onesie_build as ob
NECK = ["crew-neck", "V-neck", "scoop-neck", "boat-neck", "henley-placket", "ringer-style", "boxy", "straight-cut", "heavyweight"]
FAB = ob.FABRIC
FAB_PLAIN = ["cotton jersey", "cotton twill", "linen", "wool-blend suiting", "denim", "canvas", "satin", "velvet", "corduroy", "flannel", "poplin", "knit jersey", "ribbed knit", "quilted cotton", "felt", "faux leather", "mesh", "tulle", "organza", "brocade"]
TOP = ["The shirt is built as {up}, cut from {m1} and {m2} in the outfit's colours, with a real sewn collar, real pockets, buttons or fastenings, and trims stitched on.", "The top is made as {up}, in {m1} with {m2} trims, every collar, lapel, strap and pocket a separate sewn piece.", "It is {up} made in cloth: {m1} panels with {m2} details, joined by visible seams and finished with real stitched trims."]
HEM = ["The shirt ends in a straight hem, with a sewn belt or sash at the waist where the outfit has one.", "The garment runs down to a straight hem, finished with a sewn waistband, belt or sash band.", "A straight finished hem closes the bottom of the shirt, with the outfit's belt or sash stitched across it where there is one."]
ASSEMBLY = ["It is tailored like a real shirt, with proper seams, hems and stitching lines, entirely in the outfit's own colours and cloths.", "The shirt is assembled from cut panels joined with visible seams, topstitching and piping, hanging as one coherent piece in the outfit's own cloth.", "Layered fabric pieces are sewn together and colour-blocked in the outfit's colours, with finished edges and neat stitching throughout.", "Every detail is real fabric: panels cut, stitched together and finished with seam binding, with the outfit's details made as sewn pieces."]
NOTE = ["It is a cut-and-sew costume T-shirt: a real garment sewn to look like the outfit.", "A wearable shirt version of the outfit, made from sewn panels with real trims.", "The T-shirt is the outfit itself, constructed from fabric pieces, comfortable and wearable as a shirt."]
SHAPE = ["The shirt keeps the shape of an ordinary T-shirt, with a round neckline, straight side seams, sleeves and a straight open hem.", "It is a T-shirt in shape: straight-sided, with set-in sleeves and a straight hem.", "The sewn garment has a standard T-shirt silhouette with a straight hem across the bottom."]
def sewn_tee(r, seed):
    r = ub.nobody(r); R = rg(seed, r['name'], 'tee-sewn'); n = ub.tee_name(r['name'])
    sk, sph, snote = ub.sleeve_style(r); sl = sk if sk in ('long', 'short') else 'cut'
    sleeve = 'long-sleeved' if sl == 'long' else 'short-sleeved' if sl == 'short' else sph
    fab = R.sample(FAB, 3) if R.random() < .5 else R.sample(FAB_PLAIN, 3)
    t = f"{cap(art(R.choice(ob.ADULT)))} {sleeve} {R.choice(NECK)} T-shirt in {fab[2]}, sewn as a real fabric version of the outfit of {art(n)}. "
    t += R.choice(TOP).format(up=r['up'], m1=fab[0], m2=fab[1])
    if r.get('style') and ub.tee_style(r['style']): t += f" The outfit is {ub.tee_style(r['style'])}."
    if r['he'] and R.random() < .4: t += f" A hood at the collar is sewn as {r['he']}."
    t += (' ' + snote if snote else '') + (R.choice(ub.ANGNOTE) if ub.sleeve_angle(r) else '')
    ap = ub.armpart(r)
    if ap: t += f" The {ap} are sewn on as fabric pieces at the ends of the sleeves."
    if ub.sheer(r): t += " The sheer parts of the outfit are real sheer lace, net or mesh sewn over a lining in __onesie_skin__."
    if ub.skinbits(r, R): t += " The open neckline shows a sewn panel in __onesie_skin__."
    t += ' ' + R.choice(HEM) + ' ' + R.choice(SHAPE) + ' ' + R.choice(ASSEMBLY) + ' ' + R.choice(ub.FULLSHAPE).replace('T-shirt', 'garment').replace('shirt', 'garment') + ' ' + R.choice(NOTE) + ub.costume_more(r, R, True)
    return t
def run(final=FINAL):
    F = {}; G = list(U); VARS = list(VLABEL)
    for g in G:
        F[f'uniform_tee_sewn_{g}'] = sorted({sewn_tee(r, g + str(i)) for r in rows(g) for i in range(3)})
        for v in VARS: F[f'uniform_tee_sewn_{g}_{v}'] = sorted({sewn_tee(variant(r, v), g + v + str(i)) for r in rows(g) for i in range(2)})
    F['uniform_tee_sewn'] = [f'__uniform_tee_sewn_{g}__' for g in G]
    for v in VARS: F[f'uniform_tee_sewn_{v}'] = [f'__uniform_tee_sewn_{g}_{v}__' for g in G]
    F['uniform_tee_sewn_gendered'] = [f'__uniform_tee_sewn_{v}__' for v in VARS]
    F['uniform_tee_sewn_random'] = [f'__uniform_tee_sewn_{g}__' for g in G] + [f'__uniform_tee_sewn_{v}__' for v in VARS]
    F['uniform_tee_sewn_fabric'] = FAB + FAB_PLAIN; F['uniform_tee_sewn_assembly'] = ASSEMBLY; F['uniform_tee_sewn_note'] = NOTE; F['uniform_tee_sewn_shape'] = SHAPE
    os.makedirs(final, exist_ok=True)
    for n, l in F.items():
        assert l and all(l) and not any(re.search(r'[{}|]', x) or re.match(r'\d+::', x) for x in l), n
        open(os.path.join(final, n + '.txt'), 'w', encoding='utf8', newline='\n').write('\n'.join(l) + '\n')
    print('sewn tees:', len(F), 'files'); return F
def export_aoo(out, prefix='aoo_'):
    tmp = os.path.join(out, '_t_tmp'); os.makedirs(tmp, exist_ok=True); F = run(tmp); shutil.rmtree(tmp)
    names = set(F) | {'onesie_skin'}; ref = re.compile(r'__([A-Za-z0-9_\-/]+)__'); n = 0
    for name, lines in F.items():
        keep = list(dict.fromkeys(l for l in lines if l.strip()))
        keep = [ref.sub(lambda m: '__' + prefix + m.group(1) + '__' if m.group(1) in names else m.group(0), l) for l in keep]
        if not any('__' in l for l in keep): random.Random(zlib.crc32(name.encode())).shuffle(keep)
        open(os.path.join(out, prefix + name + '.txt'), 'w', encoding='utf8', newline='\n').write('\n'.join(keep) + '\n'); n += 1
    return n
if __name__ == '__main__':
    a = [x for x in sys.argv[1:] if os.path.isdir(x)]; run(os.path.abspath(a[0]) if a else FINAL)
