"""v74 - foundation release: books and periodicals (70), signage, lettering engine, advertising signs and labelled containers (71, 51, 52), vehicle interiors (73),
architecture upgrade (63), creature body-plan and hybrid builders with powers and effects, paper and print collections.
Stages live in v74_books, v74_sign, v74_vint, v74_arch, v74_creature, v74_paper; this file merges them."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from paths import FINAL
from famlib import run_mod, export_aoo_mod
import v74_books, v74_sign, v74_vint, v74_arch, v74_creature, v74_paper
MODS = [v74_books, v74_sign, v74_vint, v74_arch, v74_creature, v74_paper]
def build(final=FINAL):
    G = {}
    for m in MODS:
        g = m.build(final)
        for k, v in g.items():
            if k.endswith('_entry_points'): continue
            if k in G and G[k] != v: raise SystemExit('duplicate file name with different content: ' + k)
            G[k] = v
    ep = []
    for m in MODS: ep += m.build(final).get('v74_%s_entry_points' % m.__name__.split('_')[1], [])
    G['v74_entry_points'] = ep
    return G
def run(final): return run_mod(sys.modules[__name__], final)
def export_aoo(out): return export_aoo_mod(build(FINAL), out, skip=('pw_person_who', 'pw_person_prompt'))
if __name__ == '__main__': run(FINAL)
