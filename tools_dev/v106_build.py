"""v106 DRAFT build - overlays the v106 drafts on v105: bulge classes, panels (detailed pair geometry, hands, camera), acts and positions (detailed geometry), solo pools.
NOT released. Use build(FINAL) in memory or write_scratch(dir); do not run finish.py until the user approves."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from paths import FINAL
import v105_build, v106_panels, v106_acts, v106_positions, v106_solo, v106_bulge, v106_group, v106_face, v106_location
def build(final=FINAL):
    G = v105_build.build(final); ep = G.pop('v105_entry_points')
    for m in (v106_panels, v106_acts, v106_positions, v106_solo, v106_group, v106_face, v106_location):
        for k, v in m.build(final).items():
            if k.endswith('_entry_points'): continue
            G[k] = v
    for k, v in v106_bulge.build(final).items(): G[k] = v
    import re
    CAPS = re.compile(r'(?<=[.!?] )(a (?:second |third )?(?:man|woman)\b)')
    for k, v in G.items():
        if k.startswith(('adult_l', 'kink_panel')) and isinstance(v, list):
            G[k] = [CAPS.sub(lambda m: m.group(1)[0].upper() + m.group(1)[1:], x.replace(',,', ',').replace(',;', ';')) for x in v]
    G['v106_entry_points'] = list(dict.fromkeys(ep + [k for k in G if k.startswith('male_bulge_')] + ['adult_l4_wrestling_mm', 'adult_l5_wrestling_mm', 'adult_l6_wrestling_mm']))
    return G
def write_scratch(out):
    os.makedirs(out, exist_ok=True); G = build(FINAL)
    for n, l in G.items():
        if not n.endswith('_entry_points') or n == 'v106_entry_points':
            open(os.path.join(out, n + '.txt'), 'w', encoding='utf8').write('\n'.join(l) + '\n')
    return G
