"""v77 - fantasy, horror, people interaction, toys and die-cast. Stages: v77_genre, v77_pi, v77_toy."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from paths import FINAL
from famlib import run_mod, export_aoo_mod
import v77_genre, v77_pi, v77_toy
MODS = [v77_genre, v77_pi, v77_toy]
def build(final=FINAL):
    G = {}
    for m in MODS:
        g = m.build(final)
        for k, v in g.items():
            if k.endswith('_entry_points'): continue
            if k in G and G[k] != v: raise SystemExit('duplicate file name with different content: ' + k)
            G[k] = v
    ep = []
    for m in MODS: ep += m.build(final).get('v77_%s_entry_points' % m.__name__.split('_')[1], [])
    G['v77_entry_points'] = ep
    return G
def run(final): return run_mod(sys.modules[__name__], final)
def export_aoo(out):
    G = build(FINAL)
    return export_aoo_mod(G, out, skip=[k for k in G if k.startswith('pi_')])
if __name__ == '__main__': run(FINAL)
