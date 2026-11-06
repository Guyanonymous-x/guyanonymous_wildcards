"""v109 - adventure, extreme, solo outdoor and workout activities (user 2026-11-06), from the Wikipedia list of extreme and adventure
sports and its linked pages, plus solo outdoor activities and workouts. Every activity is named and then described in plain words.
Activity, person, clothing, equipment, pose, place, light, weather and camera are separate pools and mix freely: each activity lists
several kinds of place (trail running happens in forests, on ridges, on coast paths, in deserts...), and each place brings its own light.
Text on clothing (team names, race numbers) is quoted, from the name system (name_team, name_jersey_number).

Files: adv_person_<age>_w/_m (ages: young 18-44, adult 18-64, wide 18-74), adv_loc_<place>, adv_light_<kind>, adv_place_<place> (place + its light
       + weather), adv_weather, adv_camera_<kind>,
       adv_<k>_label/_outfit/_equipment/_pose_w/_pose_m/_place/_camera/_prompt/_gear_prompt/_place_prompt,
       adv_extreme_prompt, adv_outdoor_prompt, adv_workout_prompt, adv_any_prompt, adv_pose_any, adv_any_gear_prompt."""
import os, re
from v109_adv_data import LOC, LIGHT, LIGHT_OF, CAMERA, WEATHER, ACT
AGES = {'young': ('age18_24', 'age25_34', 'age35_44'), 'adult': ('age18_24', 'age25_34', 'age35_44', 'age45_54', 'age55_64'),
        'wide': ('age18_24', 'age25_34', 'age35_44', 'age45_54', 'age55_64', 'age65_74')}
INDOOR = {'gym', 'box_gym', 'garage_gym', 'studio', 'home', 'pool', 'cave'}
FIRST = {'outdoor': 'hiking'}
def _lines(final, src, name):
    if name in src: return src[name]
    with open(os.path.join(final, name + '.txt'), encoding='utf8') as f: return [l.rstrip('\n') for l in f if l.strip()]
def pron(t, g):
    d = {'s': 'she', 'S': 'She', 'p': 'her', 'o': 'her'} if g == 'w' else {'s': 'he', 'S': 'He', 'p': 'his', 'o': 'him'}
    return t.format(**d)
def gfit(o, g):
    for a, w, m in (('swimming trunks or a swimsuit', 'a swimsuit', 'swimming trunks'), ('board shorts or a swimsuit', 'a swimsuit', 'board shorts'),
                    ('a swimsuit or shorts and a T-shirt', 'a swimsuit', 'shorts and a T-shirt'), ('a T-shirt and shorts', 'a T-shirt and shorts', 'a T-shirt and shorts')):
        if a in o: return o.replace(a, w if g == 'w' else m)
    if g == 'm' and o.startswith('a swimsuit'): return o.replace('a swimsuit', 'swimming trunks', 1)
    if g == 'm' and o == 'a sleek swimsuit': return 'sleek swimming trunks'
    return o
def build(final, src=None):
    src = src or {}; G = {}
    W = _lines(final, src, 'f_create_random_woman_short'); M = _lines(final, src, 'm_create_random_man_short')
    for a, ages in AGES.items():
        G['adv_person_%s_w' % a] = [l for l in W if any(x in l for x in ages)]
        G['adv_person_%s_m' % a] = [l for l in M if any(x in l for x in ages)]
    for t, v in LOC.items(): G['adv_loc_%s' % t] = v
    for t, v in LIGHT.items(): G['adv_light_%s' % t] = v
    for t, v in CAMERA.items(): G['adv_camera_%s' % t] = v
    G['adv_weather'] = [w for w in WEATHER if w] ; G['adv_weather_maybe'] = [w if w else '' for w in WEATHER]
    for t in LOC:
        lg = LIGHT_OF.get(t, 'day')
        G['adv_place_%s' % t] = ['__adv_loc_%s__. The light is __adv_light_%s__.%s' % (t, lg, '' if t in INDOOR else ' __adv_weather_maybe__')]
    groups = {'extreme': [], 'outdoor': [], 'workout': []}; poses = []; gear = []
    section = 'extreme'
    for k, (labels, age, outfits, equip, ps, tags, cams) in ACT.items():
        if k == 'hiking': section = 'outdoor'
        if k == 'barbell': section = 'workout'
        b = 'adv_%s' % k
        bad = [t for t in tags if t not in LOC]
        if bad: raise KeyError('v109_adv: %s has unknown places %s' % (k, bad))
        G[b + '_label'] = labels
        G[b + '_outfit_w'] = [gfit(o, 'w') for o in outfits]
        G[b + '_outfit_m'] = [gfit(o, 'm') for o in outfits if 'sports bra' not in o] or [gfit(o, 'm') for o in outfits]
        G[b + '_equipment'] = equip
        G[b + '_pose_w'] = [pron(p, 'w') for p in ps]; G[b + '_pose_m'] = [pron(p, 'm') for p in ps]
        G[b + '_place'] = ['__adv_place_%s__' % t for t in tags]
        G[b + '_camera'] = ['__adv_camera_%s__' % c for c in cams]
        G[b + '_prompt'] = ['__%s_label__. __adv_person_%s_%s__ %s wears __%s_outfit_%s__, and %s gear is __%s_equipment__. %s is __%s_pose_%s__. The scene is __%s_place__ __%s_camera__'
                            % (b, age, g, 'She' if g == 'w' else 'He', b, g, 'her' if g == 'w' else 'his', b, 'She' if g == 'w' else 'He', b, g, b, b) for g in ('w', 'm')]
        G[b + '_gear_prompt'] = ['The gear for __%s_label__, laid out neatly on the ground and photographed from above, showing __%s_equipment__, with the clothing beside it, __%s_outfit_w__. Clean flat-lay photograph with soft even light.' % (b, b, b)]
        G[b + '_place_prompt'] = ['A place for __%s_label__, empty of people. The scene is __%s_place__ Wide landscape photograph, the whole scene in focus.' % (b, b)]
        groups[section].append('__%s_prompt__' % b); poses += ['__%s_pose_w__' % b, '__%s_pose_m__' % b]; gear.append('__%s_gear_prompt__' % b)
    for g, v in groups.items(): G['adv_%s_prompt' % g] = v
    G['adv_any_prompt'] = groups['extreme'] + groups['outdoor'] + groups['workout']
    G['adv_pose_any'] = poses; G['adv_any_gear_prompt'] = gear
    G['adv_names'] = list(ACT)
    return G
