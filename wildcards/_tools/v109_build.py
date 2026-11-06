"""v109 build - overlays the v109 fixes on v108: v109_stage.fix (negations removed from the frame_* pack and style files) and v109_signs.fix (city signage with quoted name-system text) and v109_loc (all 1,422 Location Inventory records; the v75 pilot is rebuilt with its IDs)."""
import os, sys, re
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from paths import FINAL
from famlib import run_mod, export_aoo_mod
import v108_build, v109_stage, v109_signs, v109_loc, v109_obj, v109_objall, v109_era, v109_fixtures, v109_med, v109_med_era, v109_fixlib, v109_cards, v109_cards_pack, v109_adv, v109_sporttext, v109_cardgames, v109_boardgame, v109_boardgames2, v109_gamestages, v109_gamelayout, v109_art
def build(final=FINAL):
    G = v108_build.build(final)
    for k in v109_stage.REPL:
        if k not in G: G[k] = [l.rstrip('\n') for l in open(os.path.join(final, k + '.txt'), encoding='utf8') if l.strip()]
    G = v109_signs.fix(v109_stage.fix(G))
    L = v109_loc.build(final); L.update(v109_loc.adult25(final))
    bad = v109_loc.child_safe_check(L)
    if bad: raise ValueError('child-safe check failed: %r' % bad[:5])
    L.pop('_child_ids', None)
    G = {k: v for k, v in G.items() if not (k.startswith('loc_') and k not in L)}  # retire v75 pilot pools the full conversion no longer makes
    G.update(L)
    G.update(v109_obj.build())
    A = v109_objall.build(final); G.update(A)
    for suf in ('short', 'phrase', 'full'): G['ob_any_%s' % suf] = G['ob_any_%s' % suf] + ['__ob_%s_%s__' % (n, suf) for n in A['ob_v109all_names']]
    X = v109_fixtures.build(final); G.update(X)
    for suf in ('short', 'phrase', 'full'): G['ob_any_%s' % suf] = G['ob_any_%s' % suf] + ['__ob_%s_%s__' % (n, suf) for n in X['ob_fixture_names']]
    G = v109_era.fix(G, final)
    G = v109_fixlib.fix(G, final)
    G.update(v109_med.build(final, G))
    G = v109_med_era.fix(G, final, v109_med)
    G.update(v109_cards.build(final))
    G = v109_cards_pack.fix(G, final)
    G.update(v109_adv.build(final, G))
    G.update(v109_cardgames.build(final))
    G.update(v109_boardgame.build(final))
    G.update(v109_boardgames2.build(final))
    S = v109_gamestages.build(final); G.update(S)
    G['cg_any_prompt'] = G['cg_any_prompt'] + ['__cg_stage_any_prompt__'] * 6
    G['bg_all_any_prompt'] = G['bg_all_any_prompt'] + ['__bg_stage_any_prompt__'] * 6
    G = v109_gamelayout.build(G, final)
    G = v109_sporttext.fix(G, final)
    G['v109_entry_points'] = ['tc_any_prompt', 'tc_packaging_any_prompt', 'tc_sports_prompt', 'cg_any_prompt', 'cg_topdown_any_prompt', 'bg_all_any_prompt', 'bg_topdown_any_prompt',
                              'adv_any_prompt', 'adv_any_gear_prompt', 'ob_fixture_any_full', 'illustration_style_scribble_line_mild']
    G = v109_art.fix(G, final)
    return G
def run(final): return run_mod(sys.modules[__name__], final)
def export_aoo(out):
    """The All Options Once edition has no person files (as in v74), so v109 files that call people, directly or through other files, are
    left out of it: after the export, any file from this build that still points at a file missing from the edition is removed, repeatedly."""
    G = build(FINAL); n = export_aoo_mod(G, out)
    mine = {'aoo_' + k for k in G if not k.endswith('_entry_points')}
    names = {f[:-4] for f in os.listdir(out) if f.endswith('.txt')}
    while True:
        drop = []
        for f in mine & names:
            refs = set(re.findall(r'__([A-Za-z0-9_\-/]+)__', open(os.path.join(out, f + '.txt'), encoding='utf8').read()))
            if refs - names: drop.append(f)
        if not drop: break
        for f in drop: os.remove(os.path.join(out, f + '.txt')); names.discard(f)
    print('aoo: left out', len(mine - names), 'v109 files that call people')
    return n - len(mine - names)
