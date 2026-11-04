"""Shop-style garment sections (lingerie, bras, panties, sleep and loungewear, accessories, sale/costume): detailed front/back/coverage descriptions."""
import os, re, sys, random, zlib
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import garment_shop_data as D1, garment_shop_data2 as D2
FINAL = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
BAD = re.compile(r"\b(woman|women|man|men|girl|girls|boy|boys|female|male|ladies|lady|gentleman|kid|kids|child|children|toddler|baby|infant|junior|teen|teenage|elderly|senior|schoolgirl|schoolboy|men's|women's|cheerleader|school)\b|[{}|]|__", re.I)
SEC = {'ultra': 'ultra', 'lingerie': 'lingerie', 'bras': 'bras', 'panties': 'panties', 'clothing_sleep': 'clothing_sleep', 'accessories': 'accessories', 'sale': 'sale', 'swim': 'swim'}
FIXCAP = {'chinese': 'Chinese', 'french': 'French', 'cuban': 'Cuban', 'parisian': 'Parisian'}
def fixcap(s):
    return re.sub(r'\b(chinese|french|cuban|parisian)\b', lambda m: FIXCAP[m.group(1)], s)
def cov(c, u):
    a = 'It covers no part of the body' if c in ('nothing', 'none') else f'It covers {c}'
    b = 'nothing is left uncovered' if u in ('nothing', 'none') else f'it leaves {u} uncovered'
    return f'{a}; {b}.'
def article(w): return 'An' if w[0].lower() in 'aeiou' else 'A'
def pick(r, s): return r.choice(s.split('|'))
def line(rng, sec, name, front, back, c, u, fit, fab, col, trim, t):
    name = fixcap(name); cv = cov(c, u)
    if t == 0: return f'{article(col)} {col} {fab} {name}. Front: {front}. Back: {back}. {cv} Cut and fit: {fit}. Trimmed with {trim}.'
    if t == 1: return f'{col.capitalize()} {name} in {fab}, with {trim}. From the front: {front}. From the back: {back}. {cv} The cut is {fit}.'
    return f'{name.capitalize()} in {col} {fab}. Seen from the front, {front}; seen from the back, {back}. {cv} Fit: {fit}. Details include {trim}.'
def build():
    G = {}; allx = []
    for sec in SEC:
        rng = random.Random(zlib.crc32(sec.encode())); out = []; names = []
        for r in D1.S.get(sec, []):
            name, front, back, c, u, fit, fab, cols = r
            cl = [x.strip() for x in cols.split(',')]
            for i, col in enumerate(cl):
                out.append(line(rng, sec, name, front, back, c, u, fit, fab, col, pick(rng, D2.TRIM), i % 3)); 
            names.append(fixcap(name))
        for r in D2.B[sec]:
            name, front, back, c, u, fit = r
            for i in range(6):
                fab = pick(rng, D2.FAB[sec])
                for _ in range(12):
                    if not any(w in (name + ' ' + front).lower() for w in fab.lower().split() if len(w) > 3): break
                    fab = pick(rng, D2.FAB[sec])
                else: fab = 'soft stretch fabric'
                out.append(line(rng, sec, name, front, back, c, u, fit, fab, pick(rng, D2.COL), pick(rng, D2.TRIM), i % 3))
            names.append(fixcap(name))
        out = [x for x in dict.fromkeys(out) if not BAD.search(x)]
        names = [x for x in dict.fromkeys(names) if not BAD.search(x)]
        G[f'garment_shop_{sec}'] = out; G[f'garment_shop_{sec}_name'] = names; allx += out
    G['garment_shop_fabric'] = sorted({f for v in D2.FAB.values() for f in v.split('|')})
    G['garment_shop_trim'] = D2.TRIM.split('|'); G['garment_shop_colour'] = D2.COL.split('|')
    G['garment_shop_all'] = allx
    G['garment_shop_prompt'] = [f'wearing {x[0].lower() + x[1:]}' for x in random.Random(5).sample(allx, min(600, len(allx)))]
    return G
def run(final):
    G = build()
    for n, l in G.items():
        assert l and all(l) and not any(re.search(r'[{}|]', x) for x in l), n
        open(os.path.join(final, n + '.txt'), 'w', encoding='utf8', newline='\n').write('\n'.join(l) + '\n')
    print('garment shop:', len(G), 'files;', len(G['garment_shop_all']), 'descriptions'); return G
def export_aoo(out, prefix='aoo_'):
    G = build(); n = 0
    for name, lines in G.items():
        keep = list(dict.fromkeys(lines)); random.Random(zlib.crc32(name.encode())).shuffle(keep)
        open(os.path.join(out, prefix + name + '.txt'), 'w', encoding='utf8', newline='\n').write('\n'.join(keep) + '\n'); n += 1
    return n
if __name__ == '__main__':
    a = [x for x in sys.argv[1:] if os.path.isdir(x)]; run(os.path.abspath(a[0]) if a else FINAL)
