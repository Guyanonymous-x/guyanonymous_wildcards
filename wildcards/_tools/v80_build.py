"""v80 - treasure, card, mineral, sound, screen, art and nature collections. Stage: v80_coll."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from paths import FINAL
from famlib import run_mod, export_aoo_mod
import v80_coll
MODS = [v80_coll]
def build(final=FINAL):
    G = {}
    for m in MODS:
        g = m.build(final)
        for k, v in g.items():
            if k.endswith('_entry_points'): continue
            if k in G and G[k] != v: raise SystemExit('duplicate file name with different content: ' + k)
            G[k] = v
    ep = []
    for m in MODS: ep += m.build(final).get('v80_%s_entry_points' % m.__name__.split('_')[1], [])
    G['v80_entry_points'] = ep
    return G
def run(final): return run_mod(sys.modules[__name__], final)
def export_aoo(out): return export_aoo_mod(build(FINAL), out)
if __name__ == '__main__': run(FINAL)
