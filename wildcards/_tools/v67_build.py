"""v67 - visual and special effects (real and spectacle tiers) and extreme weather in three layers."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from paths import FINAL
from famlib import P, slug, run_mod, export_aoo_mod
import v67_data as D
LABEL = {'tornado': 'a tornado', 'hurricane': 'a hurricane', 'blizzard': 'a blizzard', 'thunderstorm': 'a thunderstorm', 'hailstorm': 'a hailstorm', 'flood': 'a flood', 'wildfire': 'a wildfire', 'drought': 'a severe drought and heatwave', 'dust_storm': 'a dust storm', 'ice_storm': 'an ice storm', 'avalanche': 'an avalanche', 'tsunami': 'a tsunami', 'volcanic_ash': 'a volcanic ash fall', 'monsoon': 'a monsoon downpour', 'fog': 'a dense fog'}
def build(final=FINAL):
    G = {}
    for t in D.WHERE: G['fx_where_%s' % t] = P(D.WHERE[t]); G['fx_interact_%s' % t] = P(D.INTERACT[t])
    G['fx_strength'] = D.STRENGTH
    for n, s in zip(('subtle', 'moderate', 'dramatic'), D.STRENGTH): G['fx_strength_%s' % n] = [s]
    G['fx_colour_real'] = P(D.COLOUR_REAL); G['fx_colour_spectacle'] = P(D.COLOUR_SPEC)
    allp = {'real': [], 'spectacle': []}
    for dom, items in D.DOM.items():
        G['fx_%s_name' % dom] = [n for n, r, s in items]
        tgt = D.TGT[dom]
        G['fx_subject_%s' % dom] = D.SUBJ[dom]
        for ti, tier in enumerate(('real', 'spectacle')):
            G['fx_%s_%s' % (dom, tier)] = [it[1 + ti] for it in items]
            G['fx_%s_%s_prompt' % (dom, tier)] = ['__fx_subject_%s__ In the scene, there is __fx_%s_%s__, appearing __fx_where_%s__. It is __fx_strength__. The light is __fx_colour_%s__, and it is __fx_interact_%s__.' % (dom, dom, tier, tgt, tier, tgt)]
            allp[tier].append('__fx_%s_%s_prompt__' % (dom, tier))
        G['fx_%s_prompt' % dom] = ['__fx_%s_real_prompt__' % dom, '__fx_%s_spectacle_prompt__' % dom]
    G['fx_real_prompt'] = allp['real']; G['fx_spectacle_prompt'] = allp['spectacle']
    G['scene_with_effect_prompt'] = allp['real'] + allp['spectacle']
    G['fx_prompt'] = list(G['scene_with_effect_prompt'])
    G['fx_photo_effect'] = D.PHOTO
    G['fx_photo_prompt'] = ['__land_prompt__ The photograph has __fx_photo_effect__.', '__city_prompt__ The photograph has __fx_photo_effect__.', '__prod_prompt__ The photograph has __fx_photo_effect__.']
    # weather
    evs = list(D.WX)
    G['wx_severity'] = [D.SEVTXT[s] for s in D.SEV]
    for s in D.SEV: G['wx_severity_%s' % s] = [D.SEVTXT[s]]
    layer = {'sky': ('sky',), 'place': ('land',), 'living': ('people', 'things', 'animals', 'plants')}
    for e in evs:
        w = D.WX[e]; lab = LABEL[e]; pre = 'wx_%s_' % e
        for k in ('sky', 'land', 'people', 'things', 'animals', 'plants', 'light'): G[pre + k] = [w[k]]
        G[pre + 'sky_prompt'] = ['The weather is %s, %s. In the sky there is __%ssky__. The light is __%slight__.' % (lab, '__wx_severity__', pre, pre)]
        G[pre + 'place_prompt'] = ['The weather is %s, %s. The land shows __%sland__. In the sky there is __%ssky__. The light is __%slight__.' % (lab, '__wx_severity__', pre, pre, pre)]
        G[pre + 'living_prompt'] = ['The weather is %s, %s. Seen in the scene is __%speople__. Nearby are __%sthings__. Among the animals, __%sanimals__. The plants show __%splants__. The light is __%slight__.' % (lab, '__wx_severity__', pre, pre, pre, pre, pre)]
        G[pre + 'prompt'] = ['The weather is %s, %s. In the sky there is __%ssky__. The land shows __%sland__. Seen in the scene is __%speople__. Nearby are __%sthings__. Among the animals, __%sanimals__. The plants show __%splants__. The light is __%slight__.' % (lab, '__wx_severity__', pre, pre, pre, pre, pre, pre, pre)]
        G[pre + 'gallery_prompt'] = ['A square image divided into four equal panels by thin white lines, all four showing the same place during %s, with __%sland__ and __%ssky__ as the main features. The top left panel is %s. The top right panel is %s. The bottom left panel is %s. The bottom right panel is %s.' % ((lab, pre, pre) + tuple(D.SEVTXT[s] for s in D.SEV))]
    for key in ('sky', 'place', 'living', 'gallery', ''):
        name = 'wx_%s_prompt' % key if key else 'wx_prompt'
        suffix = ('%s_prompt' % key) if key else 'prompt'
        G[name] = ['__wx_%s_%s__' % (e, suffix) for e in evs]
    G['wx_names'] = [LABEL[e] for e in evs]
    G['v67_entry_points'] = ['fx_prompt', 'fx_real_prompt', 'fx_spectacle_prompt', 'scene_with_effect_prompt', 'fx_photo_prompt', 'wx_prompt', 'wx_sky_prompt', 'wx_place_prompt', 'wx_living_prompt', 'wx_gallery_prompt']
    return G
def run(final): return run_mod(sys.modules[__name__], final)
def export_aoo(out): return export_aoo_mod(build(FINAL), out, skip=())
if __name__ == '__main__': run(FINAL)
