"""v84 - adult wildcards: five explicitness levels x six genres (pose, body, setting, object, group, location), per-level prompts and a random mix."""
import os, sys, re
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
DATA = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data', 'v84_adult')
GEN = ['pose', 'body', 'setting', 'object', 'group', 'location']
LV = [1, 2, 3, 4, 5]
def clean(l): return re.sub(r'\s+', ' ', l.replace(':', ' -').replace(';', ',').replace('{', '').replace('}', '').replace('|', ' ').replace('"', '').replace('__', '_')).strip()
def build(final=None):
    G = {}
    for L in LV:
        for g in GEN:
            fn = os.path.join(DATA, 'adult_l%d_%s.txt' % (L, g))
            if not os.path.exists(fn): continue
            lines = list(dict.fromkeys(clean(l) for l in open(fn, encoding='utf8') if clean(l)))
            G['adult_l%d_%s' % (L, g)] = lines
    have = lambda L, g: 'adult_l%d_%s' % (L, g) in G
    for g in GEN:
        refs = ['__adult_l%d_%s__' % (L, g) for L in LV if have(L, g)]
        if refs: G['adult_%s' % g] = refs
    for L in LV:
        if all(have(L, g) for g in GEN):
            G['adult_l%d_solo_prompt' % L] = ['__adult_l%d_%s__' % (L, g) for g in ('pose', 'body', 'setting', 'object')]
            G['adult_l%d_group_prompt' % L] = ['__adult_l%d_%s__' % (L, g) for g in ('group', 'location')]
            G['adult_l%d_prompt' % L] = ['__adult_l%d_solo_prompt__' % L, '__adult_l%d_group_prompt__' % L]
    if all('adult_l%d_prompt' % L in G for L in LV):
        G['adult_prompt'] = ['__adult_l%d_prompt__' % L for L in LV]
        G['adult_solo_prompt'] = ['__adult_l%d_solo_prompt__' % L for L in LV]
        G['adult_group_prompt'] = ['__adult_l%d_group_prompt__' % L for L in LV]
        G['adult_levels'] = ['L1 suggestive', 'L2 sensual', 'L3 partial nudity', 'L4 explicit nudity', 'L5 explicit acts']
    G['v84_ad_entry_points'] = ['adult_prompt', 'adult_solo_prompt', 'adult_group_prompt'] + ['adult_l%d_prompt' % L for L in LV]
    return G
if __name__ == '__main__':
    G = build(); print(len(G), {k: len(v) for k, v in G.items() if k.startswith('adult_l')})
