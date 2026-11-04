"""Ugly-sweater take on every uniform, costume and cosplay archetype (uniform_sweater_*): a chunky novelty knit that shows the outfit in kitschy jacquard / intarsia knitting with 3D add-ons (pom-poms, felt collars, tinsel, bells, knitted-on pockets).
Kinds: sweater (pullover), cardigan, vest (sleeveless), dress (sweater dress), onesie (knitted ugly-sweater onesie, hooded for any headwear).
Files: uniform_sweater_<kind>_<group>[_<male|female|sexy_male|sexy_female>], uniform_sweater_<kind>[_<version>], uniform_sweater, uniform_sweater_gendered, uniform_sweater_random; parts uniform_sweater_yarn / _knit / _addon / _occasion / _note
Adult wording, deterministic."""
import os, sys, re, random, zlib, shutil
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from paths import FINAL
import uniform_build as ub
from uniform_build import U, rows, variant, rg, art, cap, VLABEL
import onesie_build as ob
KINDS = {'sweater': 'pullover sweater', 'cardigan': 'button-front cardigan', 'vest': 'sleeveless sweater vest', 'dress': 'knitted sweater dress', 'onesie': 'knitted ugly-sweater onesie'}
YARN = ["chunky wool", "fuzzy acrylic", "thick cable-knit wool", "soft chenille", "bulky cotton", "mohair-blend", "fluffy brushed yarn", "shiny lurex-flecked yarn", "heavy Aran wool", "sparkly metallic yarn", "pom-pom yarn", "tinsel-flecked yarn"]
KNIT = ["bold jacquard knitting", "chunky intarsia knitting", "fair-isle style knitting", "oversized picture knitting", "cable-and-jacquard knitting", "garish colour-block knitting", "novelty picture-panel knitting", "loud all-over jacquard knitting"]
ADDON = ["fluffy pom-poms", "a felt collar sewn on", "tinsel trim", "jingling bells", "knitted-on pockets that stand out", "3D knitted buttons", "yarn fringe", "sequinned patches", "a stitched-on felt badge", "tassels", "a chunky ribbed collar", "ribbed cuffs and hem in a contrast colour", "puffy appliqué shapes", "tiny blinking-light-style beads", "a woolly belt with a big buckle", "knitted epaulettes", "pom-pom tassels along the hem", "snowflake and star motifs along the borders"]
OCCASION = ["Christmas-party", "winter-holiday", "Halloween-party", "retro ski-lodge", "1980s novelty", "grandma-knitted", "Thanksgiving", "New-Year", "Valentine's", "springtime novelty", "birthday-party", "cosy cabin", "pub-quiz", "fancy-dress party"]
NOTE = ["It is gloriously ugly and kitsch, a proper novelty sweater with the outfit knitted across the front.", "The look is deliberately over-the-top: loud colours, chunky stitches and cheerfully tacky details.", "A real knitted garment, bulky and bright, with the outfit's design knitted in rather than printed.", "Delightfully tacky, in thick knit with visible stitches throughout."]
BORDER = ["A band of knitted snowflakes, stars or small repeating motifs runs around the yoke and the hem.", "Zig-zag knitted borders in contrasting colours frame the neckline, cuffs and hem.", "Repeating knitted motifs in the outfit's colours run in bands across the chest and the sleeves."]
def sweater(r, seed, kind):
    r = ub.nobody(r); R = rg(seed, r['name'], 'sw-' + kind); n = ub.tee_name(r['name'])
    sk, sph, snote = ub.sleeve_style(r)
    sleeve = {'vest': 'sleeveless'}.get(kind) or ('long-sleeved' if sk == 'long' else 'short-sleeved' if sk == 'short' else sph)
    yarn = R.choice(YARN); knit = R.choice(KNIT); occ = R.choice(OCCASION)
    adds = R.sample(ADDON, 3)
    desc = KINDS[kind]
    if kind == 'onesie':
        hood = bool(r['he']) or R.random() < .5
        desc = f"{'hooded ' if hood else ''}{desc} {R.choice(ob.FEET_YES if R.random() < .5 else ob.FEET_NO)}"
    t = f"{cap(art(R.choice(ob.ADULT)))} {sleeve} {occ} {desc} in {yarn}, an ugly-sweater take on the outfit of {art(n)}, made in {knit}. "
    t += f"The outfit is knitted across the whole garment: {r['up']}" + (f", with {r['lo']} knitted around the lower half" if r['lo'] and kind in ('dress', 'onesie') else '') + ", in bright cartoonish colours with thick visible stitches. "
    if r['he'] and kind == 'onesie': t += f"The hood is knitted as {r['he']}. "
    elif r['he'] and R.random() < .35: t += f"A knitted hood or collar carries {r['he']}. "
    if r['ca'] and R.random() < .5: t += f"A little knitted version of {re.sub(r'^(a|an|the|some) ', '', r['ca'])} is worked into the front. "
    if r.get('style') and ub.tee_style(r['style']): t += f"The outfit is {ub.tee_style(r['style'])}. "
    t += f"Standing out from the knit are {ub.join(adds) if hasattr(ub, 'join') else ', '.join(adds)}. {R.choice(BORDER)}"
    t += (' ' + snote if snote else '') + (R.choice(ub.ANGNOTE) if ub.sleeve_angle(r) else '')
    ap = ub.armpart(r)
    if ap: t += f" The {ap} are knitted on at the ends of the sleeves."
    if ub.sheer(r): t += " The sheer parts of the outfit are made as open lacy knitting over a lining in __onesie_skin__."
    if ub.skinbits(r, R): t += " The open neckline shows a knitted panel in __onesie_skin__."
    t += ' ' + R.choice(ob.ASSEMBLY if False else NOTE)
    return t
def run(final=FINAL):
    F = {}; G = list(U); VARS = list(VLABEL)
    for k in KINDS:
        for g in G:
            F[f'uniform_sweater_{k}_{g}'] = sorted({sweater(r, g + str(i), k) for r in rows(g) for i in range(2)})
            for v in VARS: F[f'uniform_sweater_{k}_{g}_{v}'] = sorted({sweater(variant(r, v), g + v, k) for r in rows(g)})
        F[f'uniform_sweater_{k}'] = [f'__uniform_sweater_{k}_{g}__' for g in G]
        for v in VARS: F[f'uniform_sweater_{k}_{v}'] = [f'__uniform_sweater_{k}_{g}_{v}__' for g in G]
    F['uniform_sweater'] = [f'__uniform_sweater_{k}__' for k in KINDS]
    F['uniform_sweater_gendered'] = [f'__uniform_sweater_{k}_{v}__' for k in KINDS for v in VARS]
    F['uniform_sweater_random'] = [f'__uniform_sweater_{k}_{g}__' for k in KINDS for g in G] + [f'__uniform_sweater_{k}_{v}__' for k in KINDS for v in VARS]
    F['uniform_sweater_yarn'] = YARN; F['uniform_sweater_knit'] = KNIT; F['uniform_sweater_addon'] = ADDON; F['uniform_sweater_occasion'] = OCCASION; F['uniform_sweater_note'] = NOTE; F['uniform_sweater_border'] = BORDER
    os.makedirs(final, exist_ok=True)
    for n, l in F.items():
        assert l and all(l) and not any(re.search(r'[{}|]', x) or re.match(r'\d+::', x) for x in l), n
        open(os.path.join(final, n + '.txt'), 'w', encoding='utf8', newline='\n').write('\n'.join(l) + '\n')
    print('sweaters:', len(F), 'files'); return F
def export_aoo(out, prefix='aoo_'):
    tmp = os.path.join(out, '_s_tmp'); os.makedirs(tmp, exist_ok=True); F = run(tmp); shutil.rmtree(tmp)
    names = set(F) | {'onesie_skin'}; ref = re.compile(r'__([A-Za-z0-9_\-/]+)__'); n = 0
    for name, lines in F.items():
        keep = list(dict.fromkeys(l for l in lines if l.strip()))
        keep = [ref.sub(lambda m: '__' + prefix + m.group(1) + '__' if m.group(1) in names else m.group(0), l) for l in keep]
        if not any('__' in l for l in keep): random.Random(zlib.crc32(name.encode())).shuffle(keep)
        open(os.path.join(out, prefix + name + '.txt'), 'w', encoding='utf8', newline='\n').write('\n'.join(keep) + '\n'); n += 1
    return n
if __name__ == '__main__':
    a = [x for x in sys.argv[1:] if os.path.isdir(x)]; run(os.path.abspath(a[0]) if a else FINAL)
