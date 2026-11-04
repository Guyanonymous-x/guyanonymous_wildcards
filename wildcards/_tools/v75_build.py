"""v75 - legendary creatures and sacred figures (item 60), plus the Location Inventory pilot and object builders (item 82) as they are added.
Stages live in v75_leg (and later v75_obj, v75_loc); this file merges them."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from paths import FINAL
from famlib import run_mod, export_aoo_mod
import v75_leg, v75_loc, v75_obj
MODS = [v75_leg, v75_loc, v75_obj]
def build(final=FINAL):
    G = {}
    for m in MODS:
        g = m.build(final)
        for k, v in g.items():
            if k.endswith('_entry_points'): continue
            if k in G and G[k] != v: raise SystemExit('duplicate file name with different content: ' + k)
            G[k] = v
    ep = []
    for m in MODS: ep += m.build(final).get('v75_%s_entry_points' % m.__name__.split('_')[1], [])
    G['v75_entry_points'] = ep
    return G
def run(final): return run_mod(sys.modules[__name__], final)
def export_aoo(out): return export_aoo_mod(build(FINAL), out)
if __name__ == '__main__': run(FINAL)
