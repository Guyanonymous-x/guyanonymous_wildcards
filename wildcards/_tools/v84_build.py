"""v84 - adult update: sex/BDSM/fetish object files moved under adult_, five explicitness levels x six genres, plus the brand-style essence refresh (v83_bs)."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from paths import FINAL
from famlib import run_mod, export_aoo_mod
import v84_move, v84_ad, v83_bs
MODS = [v84_move, v84_ad, v83_bs]
AOO = '/home/claude/w/all_options_once'
def build(final=FINAL):
    G = {}; ep = []
    for m in MODS:
        g = m.build(final)
        for k, v in g.items():
            if k.endswith('_entry_points'): ep += v; continue
            if k in G and G[k] != v: raise SystemExit('duplicate file name with different content: ' + k)
            G[k] = v
    G['v84_entry_points'] = ep
    return G
def run(final):
    G = run_mod(sys.modules[__name__], final)
    S = v84_move.old_names(final) | v84_move.old_names(final)
    for f in os.listdir(final):
        if f.endswith('_entry_points.txt'):
            p = os.path.join(final, f); L = [l.rstrip('\n') for l in open(p, encoding='utf8')]; N = v84_move.rw(L, S)
            if N != L: open(p, 'w', encoding='utf8').write('\n'.join(N) + '\n')
    print('removed old', v84_move.cleanup(final, None)); return G
def export_aoo(out):
    r = export_aoo_mod(build(FINAL), out); v84_move.cleanup(FINAL, out); return r
if __name__ == '__main__': run(FINAL)
