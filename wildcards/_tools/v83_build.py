"""v83 - global brand style wildcards (maker_bs_*, maker_brand_style*) and richer illustration/photography style lists. Stages: v83_bs, v83_sd."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from paths import FINAL
from famlib import run_mod, export_aoo_mod
import v83_bs, v83_sd
MODS = [v83_bs, v83_sd]
def build(final=FINAL):
    G = {}; ep = []
    for m in MODS:
        g = m.build(final)
        for k, v in g.items():
            if k.endswith('_entry_points'): ep += v; continue
            if k in G and G[k] != v: raise SystemExit('duplicate file name with different content: ' + k)
            G[k] = v
    G['v83_entry_points'] = ep
    return G
def run(final): return run_mod(sys.modules[__name__], final)
def export_aoo(out): return export_aoo_mod(build(FINAL), out)
if __name__ == '__main__': run(FINAL)
