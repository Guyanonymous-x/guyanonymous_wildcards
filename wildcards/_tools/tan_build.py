"""Manual tan / sunburn control, realistic for the natural skin tone.
Pick a LEVEL file (skin_tan_<level>) for a mixed set where every line names the natural skin it applies to,
or a LEVEL x TONE file (skin_tan_<level>_<tone>) to match a specific natural skin colour.
Levels: none, faint, light, moderate, deep, maximum (tan); burn_pink, burn_red, burn_blistered (second-degree), burn_peeling.
Tones: very_fair, fair_light, medium_olive, golden_tan, brown, deep_brown."""
import os, re, sys, random, zlib
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from paths import FINAL
def R(*k): return random.Random(zlib.crc32('|'.join(map(str, k)).encode()))
TONES = {'very_fair': 'very fair, pale skin that burns easily', 'fair_light': 'fair to light skin', 'medium_olive': 'light-medium to olive skin',
         'golden_tan': 'golden, tan or caramel skin', 'brown': 'warm to deep brown skin', 'deep_brown': 'very deep brown to dark ebony skin'}
C = {
'none': {'very_fair': 'no tan at all, the skin at its natural pale, cool-pink or ivory shade',
 'fair_light': 'no tan, the skin at its natural fair shade', 'medium_olive': 'no tan, the skin at its natural light-olive shade',
 'golden_tan': 'no extra tan, the skin at its natural golden or caramel shade', 'brown': 'no extra tan, the skin at its natural brown shade', 'deep_brown': 'no extra tan, the skin at its natural deep shade with its usual even richness'},
'faint': {'very_fair': 'a faint warm flush and a few new freckles, with almost no real tan', 'fair_light': 'the first hint of colour, a slight peach-gold warmth on the shoulders and cheeks',
 'medium_olive': 'a slight warm deepening of the olive tone, barely different from the natural shade', 'golden_tan': 'a slightly warmer golden glow on the exposed areas',
 'brown': 'a barely noticeable richer warmth on the exposed areas', 'deep_brown': 'no visible change, only a faint added glow on the cheekbones and shoulders'},
'light': {'very_fair': 'a light peachy-gold tint with extra freckles, uneven and patchy because the skin does not tan evenly', 'fair_light': 'a light golden tan, a clear but gentle shift from the natural shade',
 'medium_olive': 'a light golden-olive tan, a gentle warm shift', 'golden_tan': 'a light caramel-gold tan, a slightly deeper tone on arms and face',
 'brown': 'a slightly richer, warmer brown on exposed skin', 'deep_brown': 'a subtle deepening and richer warmth on the exposed skin, visible mainly beside covered areas'},
'moderate': {'very_fair': 'a soft golden-beige tan with merging freckles, the most this skin tans with careful exposure', 'fair_light': 'a warm golden-beige tan with an even colour',
 'medium_olive': 'a warm golden-olive tan, noticeably deeper than the natural shade', 'golden_tan': 'a rich caramel-bronze tan',
 'brown': 'a clearly deeper chestnut-brown tone on exposed skin', 'deep_brown': 'a clearly deeper, richer tone with a warm undertone on exposed areas'},
'deep': {'very_fair': 'a hard-won warm honey-beige tan, still freckled and still pale beneath clothing; it does not go darker than this', 'fair_light': 'a deep golden-brown tan, a strong shift after long exposure',
 'medium_olive': 'a deep bronze-brown tan', 'golden_tan': 'a deep bronzed mahogany-gold tan',
 'brown': 'a deep espresso-brown tone on exposed areas, glowing and glossy', 'deep_brown': 'a deeper, glossier near-black richness on the exposed areas'},
'maximum': {'very_fair': 'the darkest this skin can go, a warm honey-tan with freckles, with strongly pale covered areas', 'fair_light': 'a dark golden-bronze tan after a long summer, much darker than the covered skin',
 'medium_olive': 'a very dark chestnut-bronze tan after long exposure', 'golden_tan': 'a very dark brown-bronze tan, glossy in the sun',
 'brown': 'a very dark brown with a glossy sheen, strongly different from the covered skin', 'deep_brown': 'the deepest richest dark tone, glossy with sheen, strongly different from the covered skin'},
'burn_pink': {'very_fair': 'light pink skin, tender and warm, the first sign of sunburn', 'fair_light': 'a light pink flush across the shoulders, nose and cheeks, tender',
 'medium_olive': 'a faint reddish-pink flush that fades into tan', 'golden_tan': 'a faint reddish-bronze flush on the shoulders and nose',
 'brown': 'a warm reddish-brown tint, slight tightness and tenderness', 'deep_brown': 'a slightly darker, warm, tight patch of skin that feels tender, with the redness barely visible'},
'burn_red': {'very_fair': 'bright red sunburn, hot and swollen, with sharply pale unburnt strap lines', 'fair_light': 'red sunburned skin, hot and tight, with crisp pale lines where straps and clothes sat',
 'medium_olive': 'reddish-brown sunburn across the exposed skin, hot and tight', 'golden_tan': 'deep red-brown sunburn on the exposed areas, hot and tight',
 'brown': 'dark red-brown to purplish sunburn, shiny, tight and warm to touch', 'deep_brown': 'darker, tight, shiny, dry patches that are hot and tender, with redness visible only as a warm violet-brown tint'},
'burn_blistered': {'very_fair': 'second-degree sunburn, deep red and swollen skin with fluid-filled blisters on the shoulders and nose', 'fair_light': 'second-degree sunburn, deep red skin with raised fluid-filled blisters and swelling',
 'medium_olive': 'second-degree sunburn, deep red-brown swollen skin with raised blisters', 'golden_tan': 'second-degree sunburn, dark red-brown swollen skin with raised fluid-filled blisters',
 'brown': 'second-degree sunburn, dark reddish-brown swollen skin with glossy fluid-filled blisters', 'deep_brown': 'second-degree sunburn, dark, swollen, shiny skin with raised fluid-filled blisters and ashy, weeping patches'},
'burn_peeling': {'very_fair': 'pink new skin showing beneath sheets of peeling, flaking sunburnt skin', 'fair_light': 'pink new skin beneath peeling, flaking sheets of old skin',
 'medium_olive': 'lighter new skin beneath peeling, flaking skin with a patchy tan underneath', 'golden_tan': 'lighter patches of new skin showing under peeling, flaking skin',
 'brown': 'grey-white ashy flakes of peeling skin over lighter, uneven new skin', 'deep_brown': 'ashy grey-white flakes of dry peeling skin over uneven, lighter new patches'},
}
PAT = ['an even all-over tan', 'a clear swimsuit tan line', 'a farmer\'s tan with darker forearms, neck and face', 'a pale band where a watch strap sat', 'pale strap marks from sandals on the feet',
 'a pale mask around the eyes where sunglasses sat', 'a pale band across the forehead where a cap sat', 'a V-shaped darker patch at the neck and chest', 'a pale sock line at the ankles',
 'a darker tan on one arm only, as from a car window', 'patchy colour where sunscreen was missed', 'pale thin lines from bag straps and top straps on the shoulders', 'pale shorts lines across the thighs',
 'a pale ring-finger band', 'darker skin on the shoulders, nose and cheeks only', 'a sharp pale outline of a removed top or swimsuit bottom', 'a tan across the face and hands only']
PATB = ['across the shoulders and upper back', 'across the nose and cheeks', 'on the chest and upper arms', 'on the tops of the feet and shins', 'in sharp bands where straps and clothing sat', 'on the back of the neck and ears', 'across the whole back', 'on the nose, forehead and shoulders, with pale lines where a cap and straps sat', 'on the thighs and knees', 'on the face and forearms only', 'on one side of the body only']
def mk():
    G = {}
    for lv, d in C.items():
        mixed = []
        for t, txt in d.items():
            L = [f"{TONES[t]}: {txt}" for _ in [0]] if lv == 'none' else ([f"{TONES[t]}: {txt}, {p}" for p in PATB] if lv.startswith('burn') else [f"{TONES[t]}: {txt}, with {p}" for p in PAT])
            G[f'skin_tan_{lv}_{t}'] = L; mixed += L
        G[f'skin_tan_{lv}'] = mixed
    G['skin_tan_level'] = [f'__skin_tan_{lv}__' for lv in C]
    G['skin_tan_tan_levels'] = [f'__skin_tan_{lv}__' for lv in ('faint', 'light', 'moderate', 'deep', 'maximum')]
    G['skin_tan_burn_levels'] = [f'__skin_tan_{lv}__' for lv in ('burn_pink', 'burn_red', 'burn_blistered', 'burn_peeling')]
    G['skin_tan_pattern'] = PAT; G['skin_tan_burn_pattern'] = PATB; G['skin_tan_tone'] = list(TONES.values())
    return G
def build(): return mk()
def run(final):
    G = build()
    for n, l in G.items():
        assert l and all(l) and not any(c in x for x in l for c in '{}|'), n
        open(os.path.join(final, n + '.txt'), 'w', encoding='utf8', newline='\n').write('\n'.join(dict.fromkeys(l)) + '\n')
    print('tan:', len(G), 'files'); return G
def export_aoo(out, prefix='aoo_'):
    G = build(); nm = set(G); ref = re.compile(r'__([A-Za-z0-9_\-/]+)__'); n = 0
    for name, lines in G.items():
        keep = list(dict.fromkeys(ref.sub(lambda m: '__' + prefix + m.group(1) + '__' if m.group(1) in nm else m.group(0), l) for l in lines))
        if name not in ('skin_tan_level', 'skin_tan_tan_levels', 'skin_tan_burn_levels'): random.Random(zlib.crc32(name.encode())).shuffle(keep)
        open(os.path.join(out, prefix + name + '.txt'), 'w', encoding='utf8', newline='\n').write('\n'.join(keep) + '\n'); n += 1
    return n
if __name__ == '__main__':
    a = [x for x in sys.argv[1:] if os.path.isdir(x)]; run(os.path.abspath(a[0]) if a else FINAL)
