"""v64 - hobbies, music and sport: activity packs (clothes, equipment, setting, action) with person and no-person entries."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from paths import FINAL
from famlib import P, slug, run_mod, export_aoo_mod
import v64_data as D
def build(final=FINAL):
    G = {}; by = {'hobby': [], 'sport': [], 'music': []}; names = []
    R = D.parse()
    G['act_age'] = P("in their twenties; in their thirties; in their forties; in their fifties; in their sixties; in their seventies")
    for r in R:
        s = slug(r['name']); pre = 'act_%s_' % s; by[r['sec']].append(s); names.append(r['name'])
        G[pre + 'clothes'] = r['clothes']; G[pre + 'equip'] = r['equip']; G[pre + 'setting'] = r['setting']; G[pre + 'action'] = r['action']
        sector = {'hobby': 'a hobby', 'sport': 'a sport', 'music': 'music'}[r['sec']]
        G[pre + 'prompt'] = ['A person __act_age__, taking part in %s, which is %s. They wear __%sclothes__. Equipment nearby includes __%sequip__. The person is __%saction__. The place is __%ssetting__.' % (sector, r['name'].lower(), pre, pre, pre, pre)]
        G[pre + 'gear_prompt'] = ['The equipment for %s, laid out on a plain surface, which is __%sequip__.' % (r['name'].lower(), pre)]
        G[pre + 'scene_prompt'] = ['A place for %s, which is __%ssetting__. __%sequip__ can be seen.' % (r['name'].lower(), pre, pre)]
        G[pre + 'frame_prompt'] = ['__frame_clarity__ __frame_ratio__ __%sprompt__ __frame_person_style__, __frame_person_full__ Lighting is __frame_light__.' % pre]
    for sec, lst in by.items():
        G['act_%s_prompt' % sec] = ['__act_%s_prompt__' % s for s in lst]
        G['act_%s_names' % sec] = [n for n, rr in zip(names, R) if rr['sec'] == sec]
    G['act_prompt'] = ['__act_%s_prompt__' % s for l in by.values() for s in l]
    G['act_frame_prompt'] = ['__act_%s_frame_prompt__' % s for l in by.values() for s in l]
    G['act_gear_prompt'] = ['__act_%s_gear_prompt__' % s for l in by.values() for s in l]
    G['act_scene_prompt'] = ['__act_%s_scene_prompt__' % s for l in by.values() for s in l]
    G['act_names'] = list(names)
    G['v64_entry_points'] = ['act_prompt', 'act_hobby_prompt', 'act_sport_prompt', 'act_music_prompt', 'act_frame_prompt', 'act_gear_prompt', 'act_scene_prompt']
    return G
def run(final): return run_mod(sys.modules[__name__], final)
def export_aoo(out):
    return export_aoo_mod(build(FINAL), out, skip=tuple(['act_frame_prompt'] + ['act_%s_frame_prompt' % slug(r['name']) for r in D.parse()]))
if __name__ == '__main__': run(FINAL)
