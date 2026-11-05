"""v86 - adult kilts L4-L6, pony and torn clothing L1-L6, ejaculate extras, adult achievement merit badges/medals/pins/badges, emergency and military insignia (invented places), pinback buttons."""
import os, sys, re, glob
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
DATA = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data', 'v86_adult')
def clean(l): return re.sub(r'\s+', ' ', l.replace(':', ' -').replace(';', ',').replace('{', '').replace('}', '').replace('|', ' ').replace('"', '').replace('__', '_')).strip()
def rd(fn): return list(dict.fromkeys(clean(l) for l in open(fn, encoding='utf8') if clean(l)))
ADT = ('dating', 'kink', 'sex', 'fetish'); SERV = ('police', 'fire', 'ambulance', 'military')
def build(final=None):
    G = {}
    for fn in sorted(glob.glob(os.path.join(DATA, '*.txt'))):
        n = os.path.basename(fn)[:-4]
        if n.endswith('_prompt'): continue
        G[n] = rd(fn)
    have = lambda n: n in G
    ref = lambda ns: ['__%s__' % n for n in ns if have(n)]
    for f in ('merit', 'medal', 'pin', 'badge'):
        pre = 'acc_meritbadge_adult_' if f == 'merit' else 'acc_%s_adult_' % f
        G[pre.rstrip('_') + '_prompt'] = ref(pre + a for a in ADT)
    for f in ('medal', 'pin', 'badge'):
        G['insignia_%s_prompt' % f] = ref('insignia_%s_%s' % (f, s) for s in SERV)
    G['insignia_prompt'] = ref('insignia_' + s for s in SERV)
    G['insignia_all_prompt'] = ref('insignia_prompt insignia_medal_prompt insignia_pin_prompt insignia_badge_prompt'.split())
    pb = [n for n in G if n.startswith('pinback_')]
    G['pinback_prompt'] = ['__%s__' % n for n in sorted(pb)]
    for k in ('kilts', 'pony', 'torn'):
        G['adult_%s_levels' % k] = ref('adult_l%d_%s' % (L, k) for L in range(1, 7))
    G['adult_l6_ejaculate_extras_prompt'] = ref(['adult_l6_ejaculate_extras'])
    G['adult_achievement_prompt'] = ref(['acc_meritbadge_adult_prompt', 'acc_medal_adult_prompt', 'acc_pin_adult_prompt', 'acc_badge_adult_prompt'])
    G['v86_ad_entry_points'] = [k for k in G if k.endswith('_prompt') or k.endswith('_levels')]
    return G
