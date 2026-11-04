"""v79 - noir, pirates, spies, money and metalware collections, and full descriptions for named e-reader and phone models. Stages: v79_genre, v79_coll, v79_fix."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from paths import FINAL
from famlib import run_mod, export_aoo_mod
import v79_genre, v79_coll, v79_fix
MODS = [v79_genre, v79_coll, v79_fix]
def build(final=FINAL):
    G = {}
    for m in MODS:
        g = m.build(final)
        for k, v in g.items():
            if k.endswith('_entry_points'): continue
            if k in G and G[k] != v: raise SystemExit('duplicate file name with different content: ' + k)
            G[k] = v
    ep = []
    for m in MODS: ep += m.build(final).get('v79_%s_entry_points' % m.__name__.split('_')[1], [])
    G['v79_entry_points'] = ep
    return G
def run(final): return run_mod(sys.modules[__name__], final)
def export_aoo(out): return export_aoo_mod(build(FINAL), out)
if __name__ == '__main__': run(FINAL)
