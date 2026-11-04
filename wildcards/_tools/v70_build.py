"""v70 - real-world manufacturer styles by decade (names used deliberately); influence files for cars, trucks, motorcycles, scooters, bicycles, boats, aircraft, spacecraft, rail, tractors and skates."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from paths import FINAL
from famlib import P, slug, run_mod, export_aoo_mod
import v70_data as D, v69_data as A, v69_data2 as X
CATLAB = {'car': 'cars', 'truck': 'trucks, buses and tractors', 'motorbike': 'motorcycles', 'scooter': 'scooters', 'bicycle': 'bicycles', 'boat': 'boats', 'air': 'aircraft', 'space': 'spacecraft', 'rail': 'trains and buses', 'skate': 'skateboards and skates'}
def build(final=FINAL):
    G = {}; R = D.parse(); bycat = {}; bydec = {}
    for r in A.parse():
        g = r['key']; pre = 'vx_%s_' % g; c = X.CLASS_OF[g]; lab = r['label'][0].upper() + r['label'][1:]
        G[pre + 'base_prompt'] = ['%s, which is %s. Its shape is __%sform__, with __%sfeature__. The location is __%ssetting__.' % (lab, r['desc'], pre, pre, pre)]
        G[pre + 'base_scene_prompt'] = ['__%sbase_prompt__ The vehicle is __%sstate__, seen from __vs_%s_camera__.' % (pre, pre, c)]
        G[pre + 'base_person_prompt'] = ['__%sbase_scene_prompt__ A person __culture_age__ is __vs_%s_person__.' % (pre, c)]
    for r in R:
        k = r['key']; pre = 'maker_%s_' % k; bycat.setdefault(r['cat'], []).append(k)
        for d, t in r['eras']:
            G[pre + d] = ['the design style of %s in the %s, with %s' % (r['name'], d, t)]
            G[pre + d + '_prompt'] = ['__%sgenre__ Design influence, __%s%s__.' % (pre, pre, d)]
            bydec.setdefault(d, []).append('__%s%s_prompt__' % (pre, d))
        G[pre + 'style'] = ['__%s%s__' % (pre, d) for d, t in r['eras']]
        G[pre + 'genre'] = ['__vx_%s_base_prompt__' % g for g in r['genres']]
        G[pre + 'scene_genre'] = ['__vx_%s_base_scene_prompt__' % g for g in r['genres']]
        G[pre + 'person_genre'] = ['__vx_%s_base_person_prompt__' % g for g in r['genres']]
        G[pre + 'prompt'] = ['__%sgenre__ Design influence, __%sstyle__.' % (pre, pre)]
        G[pre + 'scene_prompt'] = ['__%sscene_genre__ Design influence, __%sstyle__.' % (pre, pre)]
        G[pre + 'person_prompt'] = ['__%sperson_genre__ Design influence, __%sstyle__.' % (pre, pre)]
    for c, ks in bycat.items():
        G['maker_%s_prompt' % c] = ['__maker_%s_prompt__' % k for k in ks]
        G['maker_%s_scene_prompt' % c] = ['__maker_%s_scene_prompt__' % k for k in ks]
        G['maker_%s_person_prompt' % c] = ['__maker_%s_person_prompt__' % k for k in ks]
        G['maker_%s_names' % c] = [r['name'] for r in R if r['cat'] == c]
        G['maker_%s_style' % c] = ['__maker_%s_style__' % k for k in ks]
    allk = [r['key'] for r in R]
    G['maker_prompt'] = ['__maker_%s_prompt__' % k for k in allk]
    G['maker_scene_prompt'] = ['__maker_%s_scene_prompt__' % k for k in allk]
    G['maker_person_prompt'] = ['__maker_%s_person_prompt__' % k for k in allk]
    G['maker_names'] = [r['name'] for r in R]
    G['maker_style_any'] = ['__maker_%s_style__' % k for k in allk]
    G['maker_blend_prompt'] = ['__vx_real_prompt__ Design influence, a blend of __maker_style_any__ and __maker_style_any__.']
    for d, refs in bydec.items(): G['maker_decade_%s_prompt' % d] = refs
    G['maker_decade_prompt'] = ['__maker_decade_%s_prompt__' % d for d in sorted(bydec)]
    G['maker_decades'] = sorted(bydec)
    G['v70_entry_points'] = ['maker_prompt', 'maker_scene_prompt', 'maker_person_prompt', 'maker_blend_prompt', 'maker_decade_prompt'] + ['maker_%s_prompt' % c for c in bycat]
    return G
def run(final): return run_mod(sys.modules[__name__], final)
def export_aoo(out): return export_aoo_mod(build(FINAL), out, skip=())
if __name__ == '__main__': run(FINAL)
