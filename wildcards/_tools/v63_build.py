"""v63 - global dress and culture: regional clothing, headwear, adornment, hairstyles, settings and occasions by region."""
import os, sys, re
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from paths import FINAL
from famlib import P, slug, run_mod, export_aoo_mod
import v63_data as D
AGES = P("in their twenties; in their thirties; in their forties; in their fifties; in their sixties; in their seventies; in their early eighties")
def hairfix(h):
    if re.search(r'beard|moustache', h): return None
    h = re.sub(r'^hair ', '', h)
    h = {'short neat hair': 'kept short and neat', 'short natural hair': 'kept short and natural', 'a shaved head': 'a shaved head'}.get(h, h)
    return h
def build(final=FINAL):
    G = {}; keys = []
    G['culture_age'] = AGES
    for r in D.parse():
        k = r['key']; keys.append(k)
        hair = [x for x in (hairfix(h) for h in r['hair']) if x]
        G['culture_%s_garment' % k] = r['garments']; G['culture_%s_head' % k] = r['head']; G['culture_%s_adorn' % k] = r['adorn']
        G['culture_%s_hair' % k] = hair; G['culture_%s_setting' % k] = r['setting']; G['culture_%s_event' % k] = r['event']
        pre = 'culture_%s_' % k
        G[pre + 'outfit'] = ['__%sgarment__, with __%shead__, and __%sadorn__' % (pre, pre, pre)]
        G[pre + 'prompt'] = ['A person __culture_age__, dressed in the traditional dress of %s. They wear __%soutfit__. The hair is __%shair__. The place is __%ssetting__, during __%sevent__.' % (r['label'], pre, pre, pre, pre)]
        G[pre + 'garment_prompt'] = ['A set of traditional clothing from %s, laid out on a plain surface, which is __%sgarment__.' % (r['label'], pre)]
        G[pre + 'scene_prompt'] = ['A scene in %s. The place is __%ssetting__. It is a time of __%sevent__.' % (r['label'], pre, pre)]
        G[pre + 'frame_prompt'] = ['__frame_clarity__ __frame_ratio__ __%sprompt__ __frame_person_style__, __frame_person_full__ Lighting is __frame_light__.' % pre]
    G['culture_region'] = [r['label'] for r in D.parse()]
    G['culture_prompt'] = ['__culture_%s_prompt__' % k for k in keys]
    G['culture_garment_prompt'] = ['__culture_%s_garment_prompt__' % k for k in keys]
    G['culture_scene_prompt'] = ['__culture_%s_scene_prompt__' % k for k in keys]
    G['culture_frame_prompt'] = ['__culture_%s_frame_prompt__' % k for k in keys]
    G['culture_garment'] = ['__culture_%s_garment__' % k for k in keys]
    G['culture_headwear'] = ['__culture_%s_head__' % k for k in keys]
    G['culture_adornment'] = ['__culture_%s_adorn__' % k for k in keys]
    G['culture_hairstyle'] = ['__culture_%s_hair__' % k for k in keys]
    G['culture_setting'] = ['__culture_%s_setting__' % k for k in keys]
    G['culture_event'] = ['__culture_%s_event__' % k for k in keys]
    G['v63_entry_points'] = ['culture_prompt', 'culture_frame_prompt', 'culture_garment_prompt', 'culture_scene_prompt']
    return G
def run(final): return run_mod(sys.modules[__name__], final)
def export_aoo(out): return export_aoo_mod(build(FINAL), out, skip=tuple(['culture_frame_prompt'] + ['culture_%s_frame_prompt' % r['key'] for r in D.parse()]))
if __name__ == '__main__': run(FINAL)
