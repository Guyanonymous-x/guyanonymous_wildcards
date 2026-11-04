"""v59 - 120 professions and roles (health, trades, public service, office, creative, service, spiritual and ritual roles) built from parts."""
import os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from paths import FINAL
from famlib import slug, an, run_mod, export_aoo_mod
import v59_data as D
SECNAME = {'health': 'health and care', 'trades': 'trades, farming and food', 'public': 'public service and transport', 'office': 'office and professional', 'creative': 'creative and performing', 'service': 'service and hospitality', 'spiritual': 'spiritual and ritual roles'}
def build(final=FINAL):
    G = {}; jobs = D.parse(); bysec = {}
    for name, (sec, outfit, tool, work, act) in jobs.items():
        s = slug(name)
        G['job_%s_outfit' % s] = outfit; G['job_%s_tool' % s] = tool; G['job_%s_workplace' % s] = work; G['job_%s_action' % s] = act
        G['job_%s_prompt' % s] = ['%s, wearing __job_%s_outfit__, with __job_%s_tool__ close at hand. The person is __job_%s_action__. The place is __job_%s_workplace__.' % (an(name[0].lower() + name[1:] if name.split()[0] not in ('Anglican', 'Catholic', 'Orthodox', 'Protestant', 'Methodist', 'Buddhist', 'Zen', 'Tibetan', 'Hindu', 'Sikh', 'Shinto', 'Taoist', 'Sufi', 'Vodou') and name not in ('Zen priest',) else name), s, s, s, s)]
        bysec.setdefault(sec, []).append(s)
    for sec, l in bysec.items():
        G['job_sector_%s_prompt' % sec] = ['__job_%s_prompt__' % s for s in l]
        G['job_sector_%s_names' % sec] = [n for n, v in jobs.items() if v[0] == sec]
    G['job_names'] = list(jobs)
    G['job_prompt'] = ['__job_%s_prompt__' % slug(n) for n in jobs]
    G['job_person_prompt'] = ['__any_create_random_person_base_short__ Their work. __job_prompt__']
    G['job_frame_prompt'] = ['__frame_clarity__ __frame_ratio__ __any_create_random_person_base_short__ Their work. __job_prompt__ __frame_person_style__, __frame_person_full__ Lighting is __frame_light__.']
    G['v59_entry_points'] = ['job_prompt', 'job_person_prompt', 'job_frame_prompt', 'job_names'] + ['job_sector_%s_prompt' % s for s in bysec]
    return G
def run(final): return run_mod(sys.modules[__name__], final)
def export_aoo(out): return export_aoo_mod(build(FINAL), out, skip=('job_person_prompt', 'job_frame_prompt'))
if __name__ == '__main__': run(FINAL)
