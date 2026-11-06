"""v107 build - overlays v107_stage (nipple/areola ladder, anal-area files, fuller yoga, dance and martial-arts lists) on v106."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from paths import FINAL
from famlib import run_mod, export_aoo_mod
import v106_build, v107_stage
def build(final=FINAL):
    G = v106_build.build(final)
    for k, v in v107_stage.build(final).items(): G[k] = v
    G['v107_entry_points'] = ['f_body_anus', 'm_body_anus', 'f_body_nipples', 'act_yoga_prompt', 'act_dance_classes_prompt', 'act_martial_arts_prompt']
    return G
def run(final): return run_mod(sys.modules[__name__], final)
def export_aoo(out): return export_aoo_mod(build(FINAL), out)
