"""v75 stage A - legendary creatures from around the world (about 120) and archetypal sacred or divine figures (18), described by looks only,
with shared pools for viewpoint, pose, light, depiction and mood. Builds on the v74 creature builders (cb_, pw_)."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from famlib import P, slug
from v75_leg_data import LEG, DEI
GROUP = {'Europe': 'europe', 'Britain': 'europe', 'Britain and Ireland': 'europe', 'Ireland': 'europe', 'Scotland': 'europe', 'Scotland and Ireland': 'europe', 'England': 'europe', 'Scandinavia': 'europe', 'Norse': 'europe', 'Slavic lands': 'europe', 'Germanic lands': 'europe', 'France': 'europe', 'Northern Europe': 'europe', 'Central Europe': 'europe',
         'Greece': 'mediterranean', 'Greece and Egypt': 'mediterranean', 'Egypt': 'mediterranean', 'Egypt and Greece': 'mediterranean', 'Greece and North Africa': 'mediterranean',
         'Arabia': 'middle_east', 'Persia': 'middle_east', 'Arabia and Persia': 'middle_east', 'Mesopotamia': 'middle_east',
         'South Asia': 'south_asia', 'Himalayas': 'south_asia',
         'China': 'east_asia', 'East Asia': 'east_asia', 'Japan': 'east_asia', 'Korea': 'east_asia', 'China and Korea': 'east_asia',
         'Southeast Asia': 'southeast_asia', 'Philippines': 'southeast_asia',
         'Southern Africa': 'africa', 'Central Africa': 'africa', 'West Africa': 'africa', 'South Africa': 'africa',
         'North America': 'americas', 'Mesoamerica': 'americas', 'Mexico': 'americas', 'Latin America': 'americas', 'Brazil': 'americas', 'Amazon': 'americas',
         'Australia': 'oceania', 'Worldwide': 'worldwide'}
VIEW = P("from a low angle looking up at it; from far away as a figure in a vast landscape; in a close portrait filling the frame; in a full-body view with space around it; from over the shoulder of a small watching traveller; in profile against the sky; coming straight toward the viewer")
POSE = P("standing perfectly still and watching the viewer; moving slowly forward; turned half away with a glance back; looking up at something unseen; surrounded by drifting mist; at rest with the head lifted; caught in the instant before it moves; poised at the edge of its lair")
LIGHT = P("with soft shadows and rich colour; with a faint haze in the air; with strong side light and a sharp subject; with muted cool colours; with a low camera and a wide lens; with a shallow depth of field and fine texture; with dramatic contrast between light and dark; with warm saturated colour")
ART = P("a richly detailed oil painting; a cinematic film still; a carved stone relief; an illuminated manuscript page with gold leaf; a woodcut print with bold lines; a woven tapestry with faded thread; a lacquered screen painting; an ink-wash painting on silk; a museum diorama behind glass; a bronze statue on a plinth; a stained-glass window; a field sketch in a naturalist's notebook")
DETAIL = P("a clear view of fine scale, fur or feather detail; a scattering of old offerings at its feet; ancient ruins half hidden behind it; a small group of villagers watching from a safe distance; carved symbols glowing faintly on the ground; a trail of broken branches and tracks leading to it; scraps of old banners blowing nearby; an old shrine marked with ribbons; smoke or mist curling around its feet")
WITNESS = P("a lone traveller with a lantern; a shepherd with a crook and a dog; a young hunter with a bow; a robed scholar with a notebook; a pair of children holding hands; an old woman with a basket; a knight in worn armour; a fisherman with a net; a priest in plain robes; a merchant with a loaded mule")
SACRED_POSE = P("seated on a high throne with open hands; standing with both arms spread wide; walking slowly with one hand raised; kneeling in the water with a calm face; floating a little above the ground; looking down with a gentle smile; holding a symbol of office in both hands")
OFFER = P("fresh flowers and burning incense; fruit and bread on a stone altar; floating lamps on a dark pool; strings of coloured ribbons; fallen petals on the steps; bowls of rice and milk; carved wooden figures in rows; a ring of candles")

def ART_(label):
    l = label.lower()
    return 'an' if l[0] in 'aeio' and not l.startswith(('eu', 'one')) or (l[0] == 'u' and not l.startswith(('uni', 'use'))) else 'a'

def build(final=None):
    G = {}
    for k, v in (('view', VIEW), ('pose', POSE), ('light', LIGHT), ('depiction', ART), ('detail', DETAIL), ('witness', WITNESS)): G['leg_' + k] = v
    G['leg_sacred_pose'] = SACRED_POSE; G['leg_offering'] = OFFER
    keys = []; by = {}
    for row in LEG.strip().split('\n'):
        k, label, region, look, hab = row.split('|')
        art = ART_(label)
        G['leg_%s_look' % k] = ['%s %s, %s' % (art, label, look)]
        G['leg_%s_habitat' % k] = [hab]
        G['leg_%s_prompt' % k] = ['The subject is __leg_%s_look__. It is __leg_pose__. Its surroundings are %s. It is shown __leg_view__, __leg_light__. A detail is __leg_detail__. Another is __leg_detail__.' % (k, hab)]
        G['leg_%s_scene' % k] = ['The subject is __leg_%s_look__. It is __leg_pose__. Its surroundings are %s. __setting_conditions_any__' % (k, hab)]
        G['leg_%s_short' % k] = ['__leg_%s_look__.' % k]
        G['leg_%s_encounter' % k] = ['The subject is __leg_%s_look__. Its surroundings are %s. In the foreground is __leg_witness__, small beside it. It is shown __leg_light__. A detail is __leg_detail__.' % (k, hab)]
        G['leg_%s_art' % k] = ['A picture made as __leg_depiction__, showing __leg_%s_look__. Its surroundings are %s.' % (k, hab)]
        keys.append(k); by.setdefault(GROUP[region], []).append(k)
    for suf in ('look', 'prompt', 'short', 'encounter', 'art', 'scene'): G['leg_' + suf] = ['__leg_%s_%s__' % (k, suf) for k in keys]
    G['leg_names'] = [r.split('|')[1] for r in LEG.strip().split('\n')]
    for g, ks in by.items():
        for suf in ('look', 'prompt', 'short', 'encounter', 'art', 'scene'): G['leg_%s_%s' % (g, suf)] = ['__leg_%s_%s__' % (k, suf) for k in ks]
    G['leg_pair_prompt'] = ['Two legendary beings face each other across an open space. On the left is __leg_look__. On the right is __leg_look__. It is shown __leg_light__, with __leg_detail__.']
    
    # sacred and divine archetypes
    dk = []
    for row in DEI.strip().split('\n'):
        k, label, look, hab = row.split('|')
        G['leg_sacred_%s_look' % k] = ['%s %s, %s' % (ART_(label), label, look)]
        G['leg_sacred_%s_prompt' % k] = ['The subject is __leg_sacred_%s_look__. The figure is __leg_sacred_pose__. Its surroundings are %s. Around the figure are __leg_offering__. It is shown __leg_light__.' % (k, hab)]
        G['leg_sacred_%s_art' % k] = ['A picture made as __leg_depiction__, showing __leg_sacred_%s_look__. Its surroundings are %s.' % (k, hab)]
        dk.append(k)
    for suf in ('look', 'prompt', 'art'): G['leg_sacred_' + suf] = ['__leg_sacred_%s_%s__' % (k, suf) for k in dk]
    G['v75_leg_entry_points'] = ['leg_prompt', 'leg_short', 'leg_encounter', 'leg_art', 'leg_scene', 'leg_pair_prompt', 'leg_sacred_prompt', 'leg_sacred_art'] + ['leg_%s_prompt' % g for g in by]
    return G
if __name__ == '__main__':
    G = build(); print(len(G))
