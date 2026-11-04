"""v44: accessories and wardrobe. New families (item descriptions only): monocle, noveltyglasses, sunglasses, glassesadd, shawl, muff, teeth (costume), wearabletech (by era), lapelpin, patch, meritbadge (skills + adulting), ball, sport_*; small/plastic earrings; plastic and novelty ranges for ten more families; garment fit modifiers (fit_*, manual). Idempotent."""
import os, re, sys, glob, random, zlib
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from paths import FINAL
import v40_build as V, v44_data_a as A, v44_data_b as B
CL = ["red", "blue", "green", "yellow", "orange", "pink", "purple", "black", "white", "teal", "silver", "gold", "turquoise", "navy", "cream", "burgundy"]
FAMS = [('acc_monocle', A.MONOCLE, 'Wearing __acc_monocle_short__.'), ('acc_noveltyglasses', A.NOVGL, 'Wearing __acc_noveltyglasses_short__.'), ('acc_sunglasses', A.SUN, 'Wearing __acc_sunglasses_short__.'),
        ('acc_glassesadd', A.GADD, 'Wearing __acc_glassesadd_short__.'), ('acc_shawl', A.SHAWL, 'Wearing __acc_shawl_short__.'), ('acc_muff', A.MUFF, 'Holding __acc_muff_short__.'),
        ('acc_teeth', A.TEETH, 'Wearing __acc_teeth_short__.'), ('acc_lapelpin', B.PINS, 'Wearing __acc_lapelpin_short__.'), ('acc_patch', B.PATCH, 'With __acc_patch_short__ sewn on.'),
        ('acc_meritbadge_skills', B.BADGE_SKILL, 'Wearing __acc_meritbadge_skills_short__.'), ('obj_ball', B.BALLS, 'Holding __obj_ball_short__.'),
        ('acc_earring_small', A.EAR_SMALL, 'Wearing __acc_earring_small_short__.'), ('acc_earring_plastic', A.EAR_PLASTIC, 'Wearing __acc_earring_plastic_short__.')]
ADULT_BG = ['navy blue', 'forest green', 'burgundy', 'slate blue', 'charcoal', 'dark teal', 'maroon', 'olive']
ADULT_EDGE = ['golden yellow', 'cream', 'silver-grey', 'tan', 'white', 'bright orange']
COLOURABLE = re.compile(r'plastic|fabric|wool|silk|cotton|nylon|rubber|silicone|acrylic|felt|foam|velvet|leather|resin|knit|cashmere|polyester|twill|canvas|vinyl|latex|alpaca|chiffon|voile|lycra|elastic|neoprene|chenille|PVC|polymer|mesh|ribbon|denim|suede|cardboard|sequins|plush', re.I)
def grp(pre, rows, n):
    c = [r for r in rows if any(COLOURABLE.search(m) for m in r[2])]; k = [r for r in rows if r not in c]; G = {}
    for part, cols in ((c, CL), (k, None)):
        if not part: continue
        g = V.group(pre, part, cols, n)
        for key, v in g.items(): G.setdefault(key, []).extend(v)
    return {key: sorted(set(v)) if key in (pre, pre + '_short', pre + '_material') else v for key, v in G.items()}
def adulting():
    p = os.path.join(HERE, 'data', 'badge_prompts_examples.txt')
    if not os.path.exists(p): return []
    out = []; R = random.Random(4401)
    for l in open(p, encoding='utf8'):
        m = re.search(r'centre image: (.*?), rendered in', l); w = re.search(r'the words "([^"]+)"', l)
        if not m or not w: continue
        out.append(f'A round embroidered merit badge with a {R.choice(ADULT_BG)} twill background and a raised {R.choice(ADULT_EDGE)} border, showing {m.group(1)}, with the words {w.group(1).title()} stitched on a curved ribbon banner across the lower part. Its back is an iron-on or sew-on backing')
    return out
FIT_AREAS = {
 'fit_top_tight': ['the shirt is too small, with the buttons pulling and gaping across the chest', 'the top is tight across the chest, with horizontal strain lines in the fabric', 'the fabric of the top is pulled taut over the abdomen, riding up above the waistband', 'the sleeves of the top are tight around the upper arms, with the fabric pulled and the seams strained', 'the collar is tight at the neck, with the fabric bunching at the collar line', 'the seams at the sides of the top are strained, with small gaps opening between stitches', 'a seam at the shoulder is split, with the lining showing', 'the top is too short, leaving the midriff uncovered when the arms are raised'],
 'fit_top_loose': ['the shirt is too large, with the shoulder seams hanging below the shoulders', 'the top hangs loosely, with extra fabric pooling at the waist', 'the sleeves are too long and hang over the hands', 'the neckline gapes open, sagging forward at the collar', 'the fabric of the top is baggy around the torso, with soft folds hanging at the sides', 'the hem of the top reaches to mid-thigh, well past the intended length'],
 'fit_bottom_tight': ['the trousers are too tight at the hips and thighs, with diagonal strain lines pulling toward the seams', 'the fabric of the trousers is pulled tightly across the seat and the crotch seam is strongly outlined', 'the waistband digs in at the waist, with a soft fold of fabric rolling over the top edge', 'the trousers ride up between the legs, with the seam pulled snug', 'the thigh seams are stretched thin, and the fabric looks almost translucent at the strain points', 'the zip is pulled up with the fabric around it creased and stretched', 'the jeans are too short, ending well above the ankles', 'the shorts ride up at the hem, bunching high on the upper thighs'],
 'fit_bottom_loose': ['the trousers are baggy, with extra fabric bunching at the knees and ankles', 'the waistband sags low on the hips, exposing the top of the underwear waistband', 'the trousers are too long and pool in folds around the shoes', 'the seat of the trousers hangs loosely, with a drooping crotch seam', 'the skirt hangs too long and loose, with the hem dragging near the ground', 'the shorts are loose, with the legs hanging wide and baggy to the knees'],
 'fit_chest_bust': ['the garment is tight across the bust, with the fabric pulled and the seams outlined', 'the neckline gapes at the front, with the fabric standing away from the chest', 'the buttons across the bust are straining, with small gaps between them', 'the cups of the garment are too small, with the flesh swelling over the edges', 'the garment is loose across the chest, with the fabric hanging in folds', 'a dress bodice is too tight, with creases radiating from the centre of the chest'],
 'fit_general': ['the whole outfit is a size too small, with the fabric stretched tight in every seam', 'the whole outfit is a size too large, with loose fabric folding over itself', 'the garment looks as if it was made for a different body, with strained seams in some places and loose fabric in others', 'the outfit fits well, with smooth seams and a clean line', 'the garment has been taken in at the waist, with a snug but comfortable fit'],
}
SEV = ['slightly', 'noticeably', 'severely']
def fit_files():
    G = {}
    for k, v in FIT_AREAS.items(): G[k] = [x[0].upper() + x[1:] + '.' for x in v]
    G['fit_severity'] = ['The fit problem is slight.', 'The fit problem is clearly noticeable.', 'The fit problem is severe.']
    G['fit_random_prompt'] = [f'__{k}__' for k in FIT_AREAS if k != 'fit_general'] + ['__fit_general__']
    G['fit_random_prompt'] = G['fit_random_prompt'] + ['__fit_top_tight__ __fit_bottom_tight__', '__fit_top_loose__ __fit_bottom_loose__', '__fit_top_tight__ __fit_bottom_loose__', '__fit_top_loose__ __fit_bottom_tight__']
    G['fit_random_prompt_severity'] = ['__fit_random_prompt__ __fit_severity__']
    return G
def build():
    G = {}
    for pre, rows, wear in FAMS:
        G.update(grp(pre, rows, 5)); G[pre + '_prompt'] = [f'__{pre}__']
    G['acc_meritbadge_adulting'] = adulting(); G['acc_meritbadge_adulting_prompt'] = ['__acc_meritbadge_adulting__']
    G['acc_meritbadge_prompt'] = ['__acc_meritbadge_skills_prompt__']
    # wearable tech by era
    allt = []
    for era, rows in B.TECH.items():
        pre = 'acc_wearabletech_' + era.replace('-', '_'); G.update(grp(pre, rows, 4)); G[pre + '_prompt'] = [f'__{pre}__']; allt += rows
    G.update(grp('acc_wearabletech', allt, 3)); G['acc_wearabletech_prompt'] = ['__acc_wearabletech__']
    # sport
    allsp = []; sp_prompts = []
    for sport, rows in B.SPORT.items():
        key = re.sub(r'[^a-z]+', '_', sport.lower()).strip('_'); pre = 'sport_' + key
        G.update(grp(pre, rows, 4)); G[pre + '_prompt'] = [f'__{pre}__']; sp_prompts.append(f'__{pre}_prompt__'); allsp += rows
    G.update(grp('sport_all', allsp, 3)); G['sport_prompt'] = sp_prompts
    # range audit
    for fam, (cheap, nov) in B.AUDIT.items():
        for kind, rows in (('plastic', cheap), ('novelty', nov)):
            pre = f'acc_{fam}_{kind}'; G.update(grp(pre, rows, 5)); G[pre + '_prompt'] = [f'__{pre}__']
    G.update(fit_files())
    G['v44_entry_points'] = ['__acc_monocle_prompt__', '__acc_noveltyglasses_prompt__', '__acc_sunglasses_prompt__', '__acc_glassesadd_prompt__', '__acc_shawl_prompt__', '__acc_muff_prompt__', '__acc_teeth_prompt__', '__acc_wearabletech_prompt__', '__acc_lapelpin_prompt__', '__acc_patch_prompt__', '__acc_meritbadge_prompt__', '__acc_meritbadge_adulting_prompt__', '__obj_ball_prompt__', '__sport_prompt__', '__acc_earring_small_prompt__', '__acc_earring_plastic_prompt__', '__fit_random_prompt__']
    return G
def _wr(folder, name, lines): open(os.path.join(folder, name + '.txt'), 'w', encoding='utf8', newline='\n').write('\n'.join(lines) + '\n')
def _wire(folder, prefix=''):
    """add the new ranges into the existing family prompt files so everyday small earrings are the most common"""
    for fam, kinds in (('earring', [('small', 5), ('plastic', 2)]),) + tuple((f, [('plastic', 2), ('novelty', 2)]) for f in B.AUDIT):
        for kind in ('prompt', 'short'):
            p = os.path.join(folder, f'{prefix}acc_{fam}_{kind}.txt')
            if not os.path.exists(p): continue
            t = open(p, encoding='utf8').read().rstrip('\n').split('\n'); add = []
            for sub, n in kinds:
                add += [f'__{prefix}acc_{fam}_{sub}_{kind}__'] * n if os.path.exists(os.path.join(folder, f'{prefix}acc_{fam}_{sub}_{kind}.txt')) else []
            if not add or any(a in t for a in add): continue
            _wr(folder, f'{prefix}acc_{fam}_{kind}', t + add)
def run(final):
    G = build()
    for n, l in G.items(): _wr(final, n, l)
    _wire(final); print('v44:', len(G), 'files'); return G
def export_aoo(out, prefix='aoo_'):
    G = build(); names_ = set(G); ref = re.compile(r'__([A-Za-z0-9_\-/]+)__'); n = 0
    for name, lines in G.items():
        keep = list(dict.fromkeys(ref.sub(lambda m: '__' + prefix + m.group(1) + '__' if m.group(1) in names_ else m.group(0), l) for l in lines))
        if not name.endswith('prompt') and 'entry_points' not in name: random.Random(zlib.crc32(name.encode())).shuffle(keep)
        _wr(out, prefix + name, keep); n += 1
    _wire(out, prefix); return n
if __name__ == '__main__':
    a = [x for x in sys.argv[1:] if os.path.isdir(x)]; run(os.path.abspath(a[0]) if a else FINAL)
