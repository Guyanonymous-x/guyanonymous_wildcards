"""v83 showcase: 40 prompts built only from wildcard text plus joining words. Scenes spread over regions and eras; grids compare four or nine brand styles."""
import sys, os, random
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from v74_showcase import pull, grid, sizes, cap
import v83_bs as b
RATIOS = [(4, 5), (3, 2), (1, 1), (4, 5), (3, 2)]
def build(off=0):
    S = []; add = lambda i, t, ratio, text: S.append((i, t, ratio, text)); B = b.load(); sl = b.slug
    rng = random.Random(8450 + off)
    by = {}
    for x in B: by.setdefault(x[1], []).append(x)
    quota = {'Europe': 4, 'North America': 3, 'East Asia': 4, 'South Asia': 2, 'Southeast Asia': 1, 'Middle East': 2, 'Africa': 2, 'Latin America': 3, 'Oceania': 1, 'Russia and Eastern Europe': 3}
    picks = []
    for r, q in quota.items():
        L = sorted(by.get(r, []), key=lambda x: b.era_bucket(x[2])); rng.shuffle(L)
        got = []; seen = set()
        for x in L:
            e = b.era_bucket(x[2])
            if e in seen and len(got) < len(set(y[2] for y in L)) and len(seen) < 4: continue
            seen.add(e); got.append(x)
            if len(got) == q: break
        picks += got
    for n, x in enumerate(picks[:25], 1):
        name, region, era, ind, t, grp = x
        add('S%02d' % n, '%s (%s, %s)' % (name, region, era), RATIOS[n % 5], pull('__maker_bs_%s%s__' % (sl(name), '_named' if n % 2 else ''), n) + ' ' + pull('The subject is __bs_subject_any__, designed completely in that style and __bs_view__.', n))
    G = [('cars of four makes', 4, 'car', ['__bs_cell_%s_named__' % sl(x) for x in ('Tatra', 'Citroen', 'Studebaker', 'Toyota')]),
         ('fashion houses', 4, 'garment', ['__bs_cell_%s_named__' % sl(x) for x in ('Chanel', 'Burberry', 'Emilio Pucci', 'Levi Strauss')]),
         ('electronics', 4, 'device', ['__bs_cell_%s_named__' % sl(x) for x in ('Braun', 'Sony', 'Olivetti', 'Teenage Engineering')]),
         ('home and ceramics', 4, 'home object', ['__bs_cell_%s_named__' % sl(x) for x in ('Wedgwood', 'Iittala', 'Fornasetti', 'Alessi')]),
         ('animation studios', 4, 'scene', ['__bs_cell_%s_named__' % sl(x) for x in ('Studio Ghibli', 'Aardman', 'Disney classic', 'Hanna-Barbera')]),
         ('airlines and food', 4, 'branded item', ['__bs_cell_%s_named__' % sl(x) for x in ('Pan Am', 'Coca-Cola', 'Cadbury', 'Singapore Airlines')])]
    # remaining grids use industry/region pools, 4 or 9 cells
    pools = [('Europe', 4), ('East Asia', 4), ('South Asia', 4), ('Africa', 4), ('Latin America', 4), ('Middle East', 4), ('Russia and Eastern Europe', 9), ('North America', 9), ('Oceania', 4)]
    for r, c in pools:
        L = by.get(r, [])
        refs = ['__bs_cell_%s%s__' % (sl(L[(i * 7 + off) % len(L)][0]), '_named' if i % 2 else '') for i in range(c)]
        G.append(('%s styles' % r, c, 'designed object', refs))
    for n, (t, c, what, refs) in enumerate(G[:15], 1): add('G%02d' % n, t, (1, 1), grid(c, what, refs, off + 40 + n))
    return S
if __name__ == '__main__':
    for i, t, ratio, text in build(): print('##', i, t, ratio, len(text)); print(text); print()
