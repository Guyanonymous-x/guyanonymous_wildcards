"""v65 - cities and public places: 24 place types in parts, with regional style, time, weather and crowd files."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from paths import FINAL
from famlib import P, slug, run_mod, export_aoo_mod
import v65_data as D
STYLE = P("old stone buildings with steep tiled roofs and tall chimneys; whitewashed buildings with flat roofs and blue shutters; tall narrow brick houses with stepped gables; wooden buildings with carved balconies and deep eaves; low concrete buildings with flat roofs and rooftop water tanks; tall glass and steel towers with reflective faces; ornate stone buildings with carved fronts and iron balconies; low mud-brick buildings with flat roofs in warm earth tones; buildings with curved tiled roofs and painted wooden beams; colourful painted buildings in pink, yellow and green; grey stone buildings with slate roofs and small windows; buildings with domes, arches and tiled patterned fronts")
TIME = P("early morning light with long shadows; bright midday light; golden hour with warm low light; blue hour just after sunset; deep night with lit windows; soft late afternoon light")
WEATHER = P("clear dry air; light drizzle; heavy rain with umbrellas; fresh snow on the ground; warm still air; a windy day with blowing leaves; thin fog between the buildings; wet shining ground just after rain")
CROWD = P("completely empty; a few people far apart; a handful of people walking; a moderate flow of people; a dense crowd filling the space; one person alone in the middle")
INTERIOR = {'library', 'museum', 'metro', 'airport', 'arcade'}
def build(final=FINAL):
    G = {}; keys = []
    G['frame_city'] = P("Wide-angle view of the whole scene with a clear foreground, middle ground and background, a level horizon where one is visible and straight vertical lines, natural light, rich tonal range and sharp detail; Full view of the place from a comfortable distance with space around the main features, level framing, soft natural light and crisp detail on every surface")
    G['city_style'] = STYLE; G['city_time'] = TIME; G['city_weather'] = WEATHER; G['city_crowd'] = CROWD
    for r in D.parse():
        k = r['key']; keys.append(k); pre = 'city_%s_' % k
        for part in ('layout', 'surface', 'detail', 'activity', 'sign'): G[pre + part] = r[part]
        env = '' if k in INTERIOR else ' The buildings are __city_style__. The light is __city_time__, with __city_weather__.'
        lab = r['label'][0].upper() + r['label'][1:]
        G[pre + 'prompt'] = [lab + '. The layout is __' + pre + 'layout__. The ground is __' + pre + 'surface__. Details include __' + pre + 'detail__. The scene has __' + pre + 'activity__. Signage is __' + pre + 'sign__.' + env]
        G[pre + 'empty_prompt'] = [lab + ', __' + pre + 'layout__. The ground is __' + pre + 'surface__. Details include __' + pre + 'detail__.' + env + ' No people are visible.']
        G[pre + 'frame_prompt'] = ['__frame_clarity__ __frame_ratio__ __%sprompt__ __frame_city__' % pre]
    G['city_prompt'] = ['__city_%s_prompt__' % k for k in keys]
    G['city_empty_prompt'] = ['__city_%s_empty_prompt__' % k for k in keys]
    G['city_frame_prompt'] = ['__city_%s_frame_prompt__' % k for k in keys]
    G['city_names'] = [r['label'] for r in D.parse()]
    G['city_person_prompt'] = ['A person __culture_age__ in the scene. __city_%s_prompt__' % k for k in keys]
    G['city_person_frame_prompt'] = ['__frame_clarity__ __frame_ratio__ __city_person_prompt__ __frame_person_style__, __frame_person_full__ Lighting is __frame_light__.']
    G['v65_entry_points'] = ['city_prompt', 'city_empty_prompt', 'city_frame_prompt', 'city_person_prompt', 'city_person_frame_prompt']
    return G
def run(final): return run_mod(sys.modules[__name__], final)
def export_aoo(out):
    return export_aoo_mod(build(FINAL), out, skip=tuple(['city_frame_prompt', 'city_person_frame_prompt', 'city_person_prompt'] + ['city_%s_frame_prompt' % r['key'] for r in D.parse()]))
if __name__ == '__main__': run(FINAL)
