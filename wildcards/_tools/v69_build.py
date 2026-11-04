"""v69 - vehicles: 157 genres (real and imagined) in parts, plus poses and states, people with vehicles, paint, damage and interiors."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from paths import FINAL
from famlib import P, slug, run_mod, export_aoo_mod
import v69_data as D, v69_data2 as X
PAINT_IMAG = P("glowing neon blue lines on a dark body; polished brass with copper rivets; a pearl white with soft glowing panels; weathered scrap metal with patched plates; a gleaming chrome with a rainbow sheen; a deep purple with gold trim; a matt black with a single red light strip; sun-bleached canvas and wood")
DOMLABEL = {'road': 'cars', 'truck': 'trucks', 'two_wheel': 'two-wheelers and skates', 'rail': 'trains', 'utility': 'working and leisure vehicles', 'water': 'watercraft', 'air': 'aircraft', 'space': 'spacecraft', 'imagined': 'imagined vehicles'}
CLASSES = ['car', 'cart', 'truck', 'motorbike', 'bicycle', 'skate', 'rail', 'boat', 'ship', 'air', 'space', 'imagined']
def build(final=FINAL):
    G = {}; by = {}; R = D.parse(); cls = X.CLASS_OF
    G['vpaint_colour'] = X.PAINT_COLOUR; G['vpaint_finish'] = X.PAINT_FINISH; G['vpaint_effect'] = X.PAINT_EFFECT; G['vx_paint_imagined'] = PAINT_IMAG
    G['vpaint_prompt'] = ['__vpaint_colour__, with __vpaint_finish__ and __vpaint_effect__']
    G['vpaint_scene_prompt'] = ['The paintwork is __vpaint_prompt__.']
    for c in CLASSES:
        G['vs_%s_state' % c] = X.STATE[c]; G['vs_%s_camera' % c] = X.CAMERA[c]; G['vs_%s_person' % c] = X.PERSON[c]; G['vs_%s_group' % c] = X.GROUP[c]
    for k, v in X.SPECIAL.items(): G['vs_special_%s' % k] = v
    for r in R:
        k = r['key']; pre = 'vx_%s_' % k; c = cls[k]; by.setdefault(r['dom'], []).append(r)
        G[pre + 'form'] = r['forms']; G[pre + 'feature'] = r['feats']; G[pre + 'setting'] = r['sets']
        paint = '__vx_paint_imagined__' if r['dom'] == 'imagined' else '__vpaint_prompt__'
        lab = r['label'][0].upper() + r['label'][1:]
        G[pre + 'prompt'] = ['%s, which is %s. Its shape is __%sform__, with __%sfeature__. The paintwork is %s. The location is __%ssetting__.' % (lab, r['desc'], pre, pre, paint, pre)]
        G[pre + 'frame_prompt'] = ['__frame_clarity__ __frame_ratio__ __%sprompt__ __frame_vehicle__' % pre]
        st = ['__vs_special_%s__' % k] * 3 + ['__vs_%s_state__' % c] if k in X.SPECIAL else ['__vs_%s_state__' % c]
        G[pre + 'state'] = st
        G[pre + 'scene_prompt'] = ['__%sprompt__ The vehicle is __%sstate__, seen from __vs_%s_camera__.' % (pre, pre, c)]
        G[pre + 'person_prompt'] = ['__%sscene_prompt__ A person __culture_age__ is __vs_%s_person__.' % (pre, c)]
        G[pre + 'group_prompt'] = ['__%sscene_prompt__ Around it are %s.' % (pre, '__vs_%s_group__' % c)]
        G[pre + 'person_frame_prompt'] = ['__frame_clarity__ __frame_ratio__ __%sperson_prompt__ __frame_person_style__, __frame_person_full__ Lighting is __frame_light__.' % pre]
    for dom, rs in by.items():
        G['vx_%s_prompt' % dom] = ['__vx_%s_prompt__' % r['key'] for r in rs]
        G['vx_%s_names' % dom] = [r['label'] for r in rs]
        G['vx_%s_frame_prompt' % dom] = ['__vx_%s_frame_prompt__' % r['key'] for r in rs]
    for c in CLASSES:
        ks = [r['key'] for r in R if cls[r['key']] == c]
        for suf in ('scene_prompt', 'person_prompt', 'group_prompt', 'person_frame_prompt'):
            G['vxs_%s_%s' % (c, suf)] = ['__vx_%s_%s__' % (k, suf) for k in ks]
        # damage
        if c in X.DMG:
            for i, s in enumerate(X.VSTRENGTH): G['vdmg_%s_%s' % (c, s)] = X.DMG[c][i].split('; ') if False else [X.DMG[c][i]]
            G['vdmg_%s' % c] = ['__vdmg_%s_%s__' % (c, s) for s in X.VSTRENGTH]
            G['vxd_%s_prompt' % c] = ['__vxs_%s_scene_prompt__ Damage and wear shows %s.' % (c, '__vdmg_%s__' % c)]
            for s in X.VSTRENGTH: G['vxd_%s_%s_prompt' % (c, s)] = ['__vxs_%s_scene_prompt__ Damage and wear shows __vdmg_%s_%s__.' % (c, c, s)]
        # interiors
        iv = dict(X.VINT.get(c, {}))
        if c == 'truck': iv = {k: v for k, v in X.VINT['car'].items() if k != 'trunk'}
        if iv:
            views = []
            for part, lines in iv.items():
                if part == 'trim': G['vint_%s_trim' % c] = lines
                else: G['vint_%s_%s' % (c, part)] = lines; views.append('__vint_%s_%s__' % (c, part))
            G['vint_%s_view' % c] = views
            names = [r['label'] for r in R if cls[r['key']] == c and (c != 'car' or r['dom'] == 'road')]
            G['vint_%s_subject' % c] = names
            G['vint_%s_prompt' % c] = ['A detail and interior photograph of %s. The view shows __vint_%s_view__. The trim and materials are __vint_%s_trim__.' % ('__vint_%s_subject__' % c, c, c)]
    allk = [r['key'] for r in R]; real = [r['key'] for r in R if r['dom'] != 'imagined']
    G['vx_prompt'] = ['__vx_%s_prompt__' % k for k in allk]
    G['vx_real_prompt'] = ['__vx_%s_prompt__' % k for k in real]
    G['vx_frame_prompt'] = ['__vx_%s_frame_prompt__' % k for k in allk]
    G['vxs_prompt'] = ['__vx_%s_scene_prompt__' % k for k in allk]
    G['vxs_person_prompt'] = ['__vx_%s_person_prompt__' % k for k in allk]
    G['vxs_group_prompt'] = ['__vx_%s_group_prompt__' % k for k in allk]
    G['vxs_person_frame_prompt'] = ['__vx_%s_person_frame_prompt__' % k for k in allk]
    G['vxd_prompt'] = ['__vxd_%s_prompt__' % c for c in CLASSES if c in X.DMG]
    G['vxd_ruined_prompt'] = ['__vxd_%s_heavy_prompt__' % c for c in CLASSES if c in X.DMG]
    G['vint_prompt'] = ['__vint_%s_prompt__' % c for c in CLASSES if ('vint_%s_prompt' % c) in G]
    G['vx_names'] = [r['label'] for r in R]; G['vx_domains'] = list(DOMLABEL.values())
    G['vx_condition_prompt'] = ['__vx_real_prompt__ Its condition shows __modify_vehicle__.']
    G['v69_entry_points'] = ['vx_prompt', 'vx_real_prompt', 'vxs_prompt', 'vxs_person_prompt', 'vxs_group_prompt', 'vxs_person_frame_prompt', 'vxd_prompt', 'vxd_ruined_prompt', 'vint_prompt', 'vpaint_scene_prompt', 'vx_frame_prompt', 'vx_condition_prompt'] + ['vx_%s_prompt' % d for d in by]
    return G
def run(final): return run_mod(sys.modules[__name__], final)
def skipset():
    sk = ['vx_frame_prompt', 'vxs_person_frame_prompt']
    sk += ['vx_%s_frame_prompt' % d for d in DOMLABEL] + ['vx_%s_frame_prompt' % r['key'] for r in D.parse()] + ['vx_%s_person_frame_prompt' % r['key'] for r in D.parse()] + ['vxs_%s_person_frame_prompt' % c for c in CLASSES]
    return tuple(sk)
def export_aoo(out): return export_aoo_mod(build(FINAL), out, skip=skipset())
if __name__ == '__main__': run(FINAL)
