"""v87 - male wrestling lines L1-L3."""
import os, sys, re, glob
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from v86_ad import clean, rd
DATA = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data', 'v87_adult')
def build(final=None):
    G = {}
    for fn in sorted(glob.glob(os.path.join(DATA, 'adult_*.txt'))): G[os.path.basename(fn)[:-4]] = rd(fn)
    lv = [L for L in range(1, 7) if 'adult_l%d_wrestling_mm' % L in G]
    G['adult_wrestling_mm'] = ['__adult_l%d_wrestling_mm__' % L for L in lv]
    for L in lv: G['adult_l%d_wrestling_mm_prompt' % L] = ['__adult_l%d_wrestling_mm__, __adult_l%d_expression__, __adult_l%d_bodychange__.' % (L, L, L)]
    G['v87_ad_entry_points'] = ['adult_wrestling_mm'] + ['adult_l%d_wrestling_mm_prompt' % L for L in lv]
    return G
