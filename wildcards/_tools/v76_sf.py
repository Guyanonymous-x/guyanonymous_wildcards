"""v76 stage A - science fiction: visual styles, alien species, locations, vehicles, robots and suits (item 61). Looks only; no franchise names."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from famlib import P, slug
from v76_sf_data import STYLES, ALIENS, SFLOC, SFVEH, ROBOTS, SUITS
def art(label): 
    l = label.lower(); return 'an' if l[0] in 'aeio' and not l.startswith(('eu', 'one')) or (l[0] == 'u' and not l.startswith(('uni', 'use'))) else 'a'
POSE = P("standing still and looking at the viewer; walking slowly forward; half turned with a glance back; leaning on a rail; seated with hands folded; holding up one hand in greeting; reaching toward a glowing panel; crouched to examine something on the floor")
ALIEN_WEAR = P("a plain grey tunic with a belt of pouches; a long embroidered robe in deep colours; a patched work harness; a sleek one-piece suit with glowing trim; a ceremonial sash and collar of metal; nothing but a few jewelled bands; a translucent cloak over a breathing mask; layered travel cloth with a hood")
ALIEN_CARRY = P("a small glowing device in one hand; a rolled chart under the arm; a tray of strange fruit; a carved staff; a satchel of tools; a sealed sample jar; a data slate; a lantern")
VIEW = P("in a full-body view with space around it; in a close portrait filling the frame; from a low angle looking up; from the side as it passes; over the shoulder of a human companion; in a wide shot that shows its surroundings")
DETAIL = P("hand-written labels on the panels; a coffee mug left on a console; cables hanging in loops; scuffed deck plates worn pale; a small plant in a pot; a sticker on a door; pipes sweating with condensation; a flickering strip light; taped notes by the door; a patch of fresh paint over old damage")
PEOPLE = P("a pair of crew members in coveralls talking; a lone technician working; a child watching from a doorway; an alien and a human sharing a meal; a robot trundling past; no one, the place silent; a crowd moving in both directions; a guard standing watch")
SITU = P("against a field of stars; on a rain-wet landing pad at night; in a hangar being repaired by drones; crossing a nebula of coloured gas; descending through thick clouds; parked in a dust storm on a barren world; docked at a busy station; skimming low over a frozen plain")
VIEW_V = P("from a three-quarter front angle; from directly beside it; from low behind its engines; from far away, small against the sky; in a close view of the cockpit; in a close view of the hull markings")
SUIT_WEAR = P("clean and newly issued; scuffed and taped at the seams; covered in red dust; frosted at the joints; patched and re-patched; stained with grease; hung with tools and tethers; with a crack across the visor")
FAUNA = set('gas_giant_floater glass_whale jelly_swarm burrower quill_beast lantern_angler coral_builder dust_mite_swarm sky_manta sand_stalker sky_whale_herd plasma_entity swamp_hulk mirror_scale_serpent fire_salamander gelatinous_blob dream_eater iron_hound raptor_hunter spore_bloom mycelial_colony'.split())
FAUNA_POSE = P("resting quietly; moving slowly through its habitat; watching the viewer with caution; feeding; startled and alert; curled up asleep; circling slowly")
WILD = ['alien_jungle', 'crystal_cavern', 'alien_beach', 'asteroid_garden', 'alien_ruin', 'exo_world_farm', 'ice_moon_base', 'black_hole_vista']

def build(final=None):
    G = {}
    for k, v in (('alien_pose', POSE), ('alien_wear', ALIEN_WEAR), ('alien_carry', ALIEN_CARRY), ('alien_view', VIEW), ('detail', DETAIL), ('people', PEOPLE), ('veh_situation', SITU), ('veh_view', VIEW_V), ('suit_wear', SUIT_WEAR)): G['sf_' + k] = v
    # styles
    sk = []
    for row in STYLES.strip().split('\n'):
        k, label, look, wear, light = row.split('|')
        G['sf_style_%s_look' % k] = [look]; G['sf_style_%s_wear' % k] = [wear]; G['sf_style_%s_light' % k] = [light]
        G['sf_style_%s_prompt' % k] = ['A science fiction scene in the %s style. The setting has %s. The people wear %s. The light is %s. A detail is __sf_detail__. Present are __sf_people__. The view is __loc_shot__.' % (label, '__sf_style_%s_look__' % k, '__sf_style_%s_wear__' % k, '__sf_style_%s_light__' % k)]
        sk.append(k)
    G['sf_style_names'] = [r.split('|')[1] for r in STYLES.strip().split('\n')]
    G['sf_style_prompt'] = ['__sf_style_%s_prompt__' % k for k in sk]
    # aliens
    ak = []
    for row in ALIENS.strip().split('\n'):
        k, label, look = row.split('|')
        G['sf_alien_%s_look' % k] = ['%s %s, %s' % (art(label), label, look)]
        if k in FAUNA:
            G['sf_alien_%s_prompt' % k] = ['The subject is __sf_alien_%s_look__. It is __sf_fauna_pose__. It is shown __sf_alien_view__. Its habitat is __sf_wild_look__.' % k]
        else:
          G['sf_alien_%s_prompt' % k] = ['The subject is __sf_alien_%s_look__. It wears __sf_alien_wear__ and carries __sf_alien_carry__. It is __sf_alien_pose__. It is shown __sf_alien_view__. The surroundings are __sf_loc_look__.' % k]
        G['sf_alien_%s_short' % k] = ['__sf_alien_%s_look__.' % k]
        ak.append(k)
    G['sf_fauna_pose'] = FAUNA_POSE
    G['sf_wild_look'] = ['__sf_loc_%s_look__' % w for w in WILD]
    for suf in ('look', 'prompt', 'short'): G['sf_alien_' + suf] = ['__sf_alien_%s_%s__' % (k, suf) for k in ak]
    G['sf_alien_pair_prompt'] = ['Two alien beings stand together in conversation. On the left is __sf_alien_look__. On the right is __sf_alien_look__. They are in __sf_loc_look__, with __sf_detail__.']
    # locations
    lk = []
    for row in SFLOC.strip().split('\n'):
        k, label, look, light = row.split('|')
        G['sf_loc_%s_look' % k] = ['%s %s, %s' % (art(label), label, look)]
        G['sf_loc_%s_light' % k] = [light]
        G['sf_loc_%s_prompt' % k] = ['The place is __sf_loc_%s_look__. The light is __sf_loc_%s_light__. A detail is __sf_detail__. Present are __sf_people__.' % (k, k)]
        G['sf_loc_%s_short' % k] = ['__sf_loc_%s_look__.' % k]
        lk.append(k)
    for suf in ('look', 'prompt', 'short'): G['sf_loc_' + suf] = ['__sf_loc_%s_%s__' % (k, suf) for k in lk]
    # vehicles
    vk = []
    for row in SFVEH.strip().split('\n'):
        k, label, look, marks = row.split('|')
        G['sf_veh_%s_look' % k] = ['%s %s, %s' % (art(label), label, look)]
        G['sf_veh_%s_marks' % k] = [marks]
        G['sf_veh_%s_prompt' % k] = ['The subject is __sf_veh_%s_look__. Its markings and wear are %s. It is shown %s, %s.' % (k, '__sf_veh_%s_marks__' % k, '__sf_veh_view__', '__sf_veh_situation__')]
        G['sf_veh_%s_short' % k] = ['__sf_veh_%s_look__.' % k]
        vk.append(k)
    for suf in ('look', 'prompt', 'short'): G['sf_veh_' + suf] = ['__sf_veh_%s_%s__' % (k, suf) for k in vk]
    # robots and suits
    rk = []
    for row in ROBOTS.strip().split('\n'):
        k, label, look = row.split('|'); G['sf_robot_%s_look' % k] = ['%s %s, %s' % (art(label), label, look)]
        G['sf_robot_%s_prompt' % k] = ['The subject is __sf_robot_%s_look__. It is __sf_alien_pose__, in __sf_loc_look__. A detail is __sf_detail__.' % k]; rk.append(k)
    for suf in ('look', 'prompt'): G['sf_robot_' + suf] = ['__sf_robot_%s_%s__' % (k, suf) for k in rk]
    uk = []
    for row in SUITS.strip().split('\n'):
        k, label, look = row.split('|'); G['sf_suit_%s_look' % k] = ['%s %s, %s' % (art(label), label, look)]
        G['sf_suit_%s_prompt' % k] = ['The subject is __sf_suit_%s_look__, which is __sf_suit_wear__. It is worn by a person who is __sf_alien_pose__, in __sf_loc_look__.' % k]; uk.append(k)
    for suf in ('look', 'prompt'): G['sf_suit_' + suf] = ['__sf_suit_%s_%s__' % (k, suf) for k in uk]
    G['sf_prompt'] = ['__sf_style_prompt__', '__sf_alien_prompt__', '__sf_loc_prompt__', '__sf_veh_prompt__', '__sf_robot_prompt__', '__sf_suit_prompt__']
    G['v76_sf_entry_points'] = ['sf_prompt', 'sf_style_prompt', 'sf_alien_prompt', 'sf_alien_pair_prompt', 'sf_loc_prompt', 'sf_veh_prompt', 'sf_robot_prompt', 'sf_suit_prompt']
    return G
if __name__ == '__main__': print(len(build()))
