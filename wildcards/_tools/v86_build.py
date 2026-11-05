"""v86 - adult update 3 plus pinback buttons and insignia."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from paths import FINAL
from famlib import run_mod, export_aoo_mod
import v84_ad, v85_ad, v83_bs, v86_ad
MODS = [v84_ad, v85_ad, v83_bs, v86_ad]
def build(final=FINAL):
    G = {}; ep = []
    for m in MODS:
        g = m.build(final)
        for k, v in g.items():
            if k.endswith('_entry_points'): ep += v; continue
            if k in G and G[k] != v: raise SystemExit('duplicate file name with different content: ' + k)
            G[k] = v
    for L in range(1, 7):
        if 'adult_l%d_prompt' % L in G and 'adult_l%d_expression' % L in G and 'adult_l%d_bodychange' % L in G:
            G['adult_l%d_full_prompt' % L] = ['__adult_l%d_prompt__ __adult_l%d_expression__, __adult_l%d_bodychange__.' % (L, L, L)]
            ep.append('adult_l%d_full_prompt' % L)
    G['v86_entry_points'] = ep
    return G
def run(final): return run_mod(sys.modules[__name__], final)
def export_aoo(out): return export_aoo_mod(build(FINAL), out)
if __name__ == '__main__': run(FINAL)
