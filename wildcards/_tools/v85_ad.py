"""v85 - adult: level 6, expression and body-change modifiers, messy and wrestling genres, gear (materials, garments, uniforms, kilts, tailoring, pony, furniture, roleplay, fetish focus)."""
import os, sys, re, glob
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
DATA = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data', 'v85_adult')
GEN = ['pose', 'body', 'setting', 'object', 'group', 'location']
def clean(l): return re.sub(r'\s+', ' ', l.replace(':', ' -').replace(';', ',').replace('{', '').replace('}', '').replace('|', ' ').replace('"', '').replace('__', '_')).strip()
def rd(fn): return list(dict.fromkeys(clean(l) for l in open(fn, encoding='utf8') if clean(l)))
def build(final=None):
    G = {}
    for fn in sorted(glob.glob(os.path.join(DATA, 'adult_*.txt'))):
        G[os.path.basename(fn)[:-4]] = rd(fn)
    have = lambda n: n in G
    for g in GEN:   # level 6 kept apart from the L1-L5 mixes
        pass
    if all(have('adult_l6_' + g) for g in GEN):
        G['adult_l6_solo_prompt'] = ['__adult_l6_%s__' % g for g in ('pose', 'body', 'setting', 'object')]
        G['adult_l6_group_prompt'] = ['__adult_l6_%s__' % g for g in ('group', 'location')]
        G['adult_l6_prompt'] = ['__adult_l6_solo_prompt__', '__adult_l6_group_prompt__']
    for kind in ('expression', 'bodychange', 'messy', 'wrestling'):
        refs = ['__adult_l%d_%s__' % (L, kind) for L in range(1, 7) if have('adult_l%d_%s' % (L, kind))]
        if refs: G['adult_' + kind] = refs
    for L in range(1, 7):
        for kind in ('messy', 'wrestling'):
            if have('adult_l%d_%s' % (L, kind)) and have('adult_l%d_expression' % L):
                G['adult_l%d_%s_prompt' % (L, kind)] = ['__adult_l%d_%s__, __adult_l%d_expression__, __adult_l%d_bodychange__.' % (L, kind, L, L)]
        if have('adult_l%d_expression' % L) and have('adult_l%d_bodychange' % L) and all(have('adult_l%d_%s' % (L, g)) for g in GEN):
            G['adult_l%d_full_prompt' % L] = ['__adult_l%d_prompt__ __adult_l%d_expression__, __adult_l%d_bodychange__.' % (L, L, L)]
    gear = sorted(k for k in G if k.startswith('adult_gear_'))
    if gear: G['adult_gear'] = ['__%s__' % k for k in gear]
    G['v85_ad_entry_points'] = [k for k in G if k.endswith('_prompt')] + ['adult_gear', 'adult_expression', 'adult_bodychange']
    return G
if __name__ == '__main__':
    G = build(); print(len(G), {k: len(v) for k, v in G.items() if len(v) > 20})
