"""v105 - level panels, typed acts, positions, kink panels, semen wording."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from paths import FINAL
from famlib import run_mod, export_aoo_mod
import v104_build, v105_stage, v105_solo
def build(final=FINAL):
    G = v104_build.build(final)
    ep = G.pop('v104_entry_points')
    for k, v in v105_stage.build(final).items():
        if k.endswith('_entry_points'): ep += v; continue
        G[k] = v
    for k, v in v105_solo.build(final).items():
        if k.endswith('_entry_points'): ep += v; continue
        G[k] = v
    print('v105 wording', v105_stage.wording(G))
    G['v105_entry_points'] = ep
    return G
def run(final): return run_mod(sys.modules[__name__], final)
def export_aoo(out): return export_aoo_mod(build(FINAL), out)
if __name__ == '__main__': run(FINAL)
