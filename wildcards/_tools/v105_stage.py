"""v105 - panels by level, typed acts for L5/L6, named positions, kink panels, semen wording pass."""
import re, v105_panels, v105_acts, v105_positions
REP = [(r'shooting from the tip of his penis', 'leaving the tip of his penis'), (r'shooting from the tip in short spurts', 'leaving the tip __semen_amount__'),
       (r'flying upward in an arc', 'falling a short distance'), (r'arcs forward through the air', 'falls after a short distance'),
       (r'__semen_amount__ and (lands|falls)', r'__semen_amount__, and it \1')]
def wording(G):
    n = 0
    for k, v in G.items():
        if not k.startswith(('adult_l5', 'adult_l6', 'fluid_scene_semen')): continue
        out = []
        for l in v:
            o = l
            for a, b in REP: l = re.sub(a, b, l)
            l = l.replace('arcing', 'falling')
            if l != o: n += 1
            out.append(l)
        G[k] = out
    return n
def build(final):
    G = {}; ep = []
    for m in (v105_panels, v105_acts, v105_positions):
        for k, v in m.build(final).items():
            if k.endswith('_entry_points'): ep += v; continue
            G[k] = v
    ep += [k for k in G if k.startswith(('kink_panel_', 'adult_l5_position', 'adult_l6_position'))]
    G['v105_entry_points'] = ep
    return G
