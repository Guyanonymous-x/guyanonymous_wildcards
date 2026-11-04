"""v49: every v44-v48 object family becomes a RANDOM ASSEMBLY of component files instead of a list of finished lines. For each type: __<family>_<type>_material__ (with colour where the material takes colour), shared finish and feature pools by category (comp_fin_*, comp_feat_*), a shared condition pool, and a `_random` file that builds one description from them. `<family>_prompt` and `<family>_phrase` now draw from the components, so rooms and poses get randomised furniture too. The finished-line files stay as `<family>` (premade) for anyone who wants them. Idempotent; runs after v48."""
import os, re, sys, glob, random, zlib
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from paths import FINAL
import v44_build as B4, v49_data as D
from v40_build import art
_wr = B4._wr
SOFT = re.compile(r'fabric|wool|leather|velvet|cotton|linen|canvas|silk|foam|cushion|vinyl|felt|fleece|nylon|polyester|rope|jute|quilt|cashmere|alpaca|chenille|lace|knit', re.I)
CLS = [('glass', re.compile(r'glass|crystal|ceramic|porcelain|china|enamel', re.I)), ('soft', SOFT), ('wood', re.compile(r'wood|oak|pine|beech|walnut|teak|cedar|mahogany|bamboo|rattan|cane|wicker|hardwood|lacquered', re.I)), ('metal', re.compile(r'steel|iron|brass|alumin|silver|gold|copper|bronze|chrome|titanium|zinc|metal|brass', re.I)), ('plastic', re.compile(r'plastic|acrylic|resin|silicone|rubber|polycarbonate|ABS|PVC|polymer|foam|jelly', re.I))]
def fin_of(ms, default):
    votes = {}
    for m in ms:
        for k, rx in CLS:
            if rx.search(m): votes[k] = votes.get(k, 0) + 1; break
    return max(votes, key=votes.get) if votes else default
def cat_of(pre):
    for p, c in D.PREFIX_CAT:
        if pre.startswith(p): return c
    for f in D.AUDIT_FAMS:
        if re.match(rf'acc_{f}_(plastic|novelty)$', pre): return 'jewellery'
    return None
def rd(final, n):
    p = os.path.join(final, n + '.txt')
    return [l for l in open(p, encoding='utf8').read().split('\n') if l.strip()] if os.path.exists(p) else None
def families(final):
    out = []
    for f in sorted(glob.glob(os.path.join(final, '*_type.txt'))):
        pre = os.path.basename(f)[:-9]
        if pre.endswith('_all') or cat_of(pre) is None: continue
        if os.path.exists(os.path.join(final, pre + '_short.txt')) and os.path.exists(os.path.join(final, pre + '.txt')): out.append(pre)
    return out
def build(final=FINAL):
    G = {'comp_colour': D.COLOUR}
    for k, v in D.FIN.items(): G[f'comp_fin_{k}'] = v
    for c, (fin, feats) in D.CATS.items(): G[f'comp_feat_{c}'] = feats
    G['comp_condition'] = ['__condition_01_pristine__'] + ['__condition_02_like_new__'] * 2 + ['__condition_03_good__'] * 4 + ['__condition_04_used__'] * 4 + ['__condition_05_worn__'] * 2 + ['__condition_06_shabby__', '__condition_07_damaged__']
    fams = families(final); done = []
    for pre in fams:
        cat0 = cat_of(pre)
        types = [l.split(', which is ', 1) for l in rd(final, pre + '_type') if ', which is ' in l]
        prem = rd(final, pre) or []
        mats = {}
        for l in prem:
            m = re.match(r'^(.+?), .*?\. Made (?:of|from) (.+?)(?:, in (.+?))?\.$', l)
            if m: mats.setdefault(m.group(1).lower(), []).append(m.group(2))
        rnd, phr = [], []; used = set()
        for name, desc in types:
            ms = sorted(set(mats.get(name.lower(), [])))
            if not ms: continue
            cat = cat0
            if cat == 'upholstery' and pre != 'support_lean' and len([m for m in ms if SOFT.search(m)]) * 2 < len(ms): cat = 'furniture'
            fin = D.CATS[cat][0]
            fin = fin_of(ms, fin)
            slug = re.sub(r'[^a-z0-9]+', '_', name.lower()).strip('_')[:34]; base = slug; i = 2
            while slug in used: slug = f'{base}_{i}'; i += 1
            used.add(slug)
            G[f'{pre}_{slug}_material'] = [m + (', in __comp_colour__' if B4.COLOURABLE.search(m) else '') for m in ms]
            rnd.append(f'{art(name)}, which is {desc}, made of __{pre}_{slug}_material__, its surface is __comp_fin_{fin}__, and it has __comp_feat_{cat}__. __comp_condition__')
            phr.append(f'{art(name)}, which is {desc}, made of __{pre}_{slug}_material__, its surface is __comp_fin_{fin}__, and it has __comp_feat_{cat}__')
        if not rnd: continue
        G[pre + '_random'] = rnd; G[pre + '_phrase'] = phr; (None if pre.startswith('tool_') else G.__setitem__(pre + '_prompt', [f'__{pre}_random__'])); done.append(pre)
    # combined pools now point at the group prompts
    for combo, parts in (('furn_all', [p for p in done if p.startswith('furn_')] + (['seat'] if 'seat' in done else [])), ('home_all', [p for p in done if p.startswith(('home_',)) or p == 'office_supplies']), ('sport_all', [p for p in done if p.startswith('sport_')]), ('acc_wearabletech', [p for p in done if p.startswith('acc_wearabletech_')])):
        if parts: G[combo + '_prompt'] = [f'__{p}_random__' for p in parts]
    G['v49_components'] = [f'__comp_colour__', '__comp_condition__'] + [f'__comp_feat_{c}__' for c in D.CATS]
    G['v49_families'] = done
    return G
def run(final):
    G = build(final)
    for n, l in G.items(): _wr(final, n, l)
    print('v49:', len(G), 'files,', len(G['v49_families']), 'families'); return G
def export_aoo(out, prefix='aoo_'):
    G = build(FINAL); names_ = set(G); ref = re.compile(r'__([A-Za-z0-9_\-/]+)__'); n = 0
    for name, lines in G.items():
        if name == 'v49_families': continue
        keep = list(dict.fromkeys(ref.sub(lambda m: '__' + prefix + m.group(1) + '__' if (m.group(1) in names_ or os.path.exists(os.path.join(out, prefix + m.group(1) + '.txt'))) else m.group(0), l) for l in lines))
        _wr(out, prefix + name, keep); n += 1
    return n
if __name__ == '__main__':
    a = [x for x in sys.argv[1:] if os.path.isdir(x)]; run(os.path.abspath(a[0]) if a else FINAL)
