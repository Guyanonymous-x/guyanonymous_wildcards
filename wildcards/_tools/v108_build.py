"""v108 build - overlays the v108 review fixes (v108_stage.fix) on v107, adds body_navel and act_frame_style."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from paths import FINAL
from famlib import run_mod, export_aoo_mod
import v107_build, v108_stage
from v53_build import decolon_line
HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
def build(final=FINAL):
    G = v107_build.build(final)
    import glob, re
    for p in glob.glob(os.path.join(final, 'act_*_scene_prompt.txt')) + glob.glob(os.path.join(final, 'act_*_frame_prompt.txt')) + glob.glob(os.path.join(final, 'fluid_scene_squirt.txt')):
        k = os.path.basename(p)[:-4]
        if k not in G: G[k] = [l.rstrip('\n') for l in open(p, encoding='utf8') if l.strip()]
    G['body_navel'] = [l.rstrip('\n') for l in open(os.path.join(HERE, 'body_navel.txt'), encoding='utf8') if l.strip()]
    for k in [k for k in G if k.startswith('adult_')]: G[k] = list(dict.fromkeys(decolon_line(x) for x in G[k]))
    G = v108_stage.fix(G)
    for k in [k for k in G if k.startswith('adult_')]: G[k] = list(dict.fromkeys(decolon_line(x) for x in G[k]))
    G['v108_entry_points'] = ['body_navel', 'act_frame_style', 'adult_l6_panel_mm', 'adult_l6_panel_ww']
    return G
def run(final): return run_mod(sys.modules[__name__], final)
def export_aoo(out): return export_aoo_mod(build(FINAL), out)
