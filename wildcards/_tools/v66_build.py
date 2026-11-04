"""v66 - fantasy, sci-fi and history worlds; also applies consolidation fixes to v63 (labels) and v64 (equipment wording)."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from paths import FINAL
from famlib import P, slug, run_mod, export_aoo_mod
import v66_data as D
SEC = {'history': 'a historical setting', 'fantasy': 'a fantasy setting', 'scifi': 'a science fiction setting'}
def build(final=FINAL):
    G = {}; by = {'history': [], 'fantasy': [], 'scifi': []}; labels = {}
    for r in D.parse():
        k = r['key']; pre = 'world_%s_' % k; by[r['sec']].append(k)
        G[pre + 'dress'] = r['dress']; G[pre + 'props'] = r['props']; G[pre + 'setting'] = r['setting']; G[pre + 'action'] = r['action']
        G[pre + 'prompt'] = ['A person __culture_age__, in %s, which is %s. They wear __%sdress__ and carry __%sprops__. The person is __%saction__. The place is __%ssetting__.' % (SEC[r['sec']], r['label'], pre, pre, pre, pre)]
        G[pre + 'place_prompt'] = ['A place in %s, which is %s. It is __%ssetting__. Visible nearby are __%sprops__.' % (SEC[r['sec']], r['label'], pre, pre)]
        G[pre + 'frame_prompt'] = ['__frame_clarity__ __frame_ratio__ __%sprompt__ __frame_person_style__, __frame_person_full__ Lighting is __frame_light__.' % pre]
    for sec, lst in by.items():
        G['world_%s_prompt' % sec] = ['__world_%s_prompt__' % k for k in lst]
        G['world_%s_place_prompt' % sec] = ['__world_%s_place_prompt__' % k for k in lst]
        G['world_%s_frame_prompt' % sec] = ['__world_%s_frame_prompt__' % k for k in lst]
    allk = [k for l in by.values() for k in l]
    G['world_prompt'] = ['__world_%s_prompt__' % k for k in allk]
    G['world_place_prompt'] = ['__world_%s_place_prompt__' % k for k in allk]
    G['world_frame_prompt'] = ['__world_%s_frame_prompt__' % k for k in allk]
    G['world_names'] = [r['label'] for r in D.parse()]
    G['v66_entry_points'] = ['world_prompt', 'world_history_prompt', 'world_fantasy_prompt', 'world_scifi_prompt', 'world_place_prompt', 'world_frame_prompt']
    return G
def run(final):
    import v63_build, v64_build
    v63_build.run(final); v64_build.run(final)
    return run_mod(sys.modules[__name__], final)
def export_aoo(out):
    import v63_build, v64_build
    v63_build.export_aoo(out); v64_build.export_aoo(out)
    sk = tuple(['world_frame_prompt'] + ['world_%s_frame_prompt' % s for s in SEC] + ['world_%s_frame_prompt' % r['key'] for r in D.parse()])
    return export_aoo_mod(build(FINAL), out, skip=sk)
if __name__ == '__main__': run(FINAL)
