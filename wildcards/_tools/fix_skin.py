"""One-time (already applied): makes skin_flush, skin_glow, skin_marks, skin_finish colour-neutral, so they never contradict the ethnicity / dem_tone skin colour.
Colour words are replaced by RELATIVE wording ("a shade deeper than the base skin tone", "darker than the surrounding skin").  Applied to the root files and to age_model.py / supplements.py."""
import os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(HERE)
M = {
 # flush
 'blotchy inflamed red patches': 'blotchy inflamed patches, deeper than the surrounding skin',
 'blotchy stress-red skin': 'blotchy stress-flushed skin',
 'blushing red neck and chest': 'blushing neck and chest, a shade deeper than the face',
 'blushing warm red cheeks': 'blushing warm cheeks, a shade deeper than the base skin tone',
 'cold pale blue-tinted skin': 'cold drained skin with a cool undertone',
 'feverish bright red flush': 'feverish intense flush, much deeper than the base skin tone',
 'flush red nose and cheeks': 'flushed nose and cheeks',
 'healthy rosy flush': 'healthy warm flush',
 'heavy rosacea redness across nose': 'heavy rosacea flushing across the nose',
 'intense red facial flush': 'intense facial flush, much deeper than the base skin tone',
 'mottled red and pale skin': 'mottled skin with patches deeper and lighter than the base skin tone',
 'pale ashen skin with dark eye rings': 'drained skin with shadowed eye rings',
 'pale bloodless ghostly skin': 'drained, bloodless-looking skin that has lost some of its natural colour',
 'pale cold ghostly skin tone': 'drained cold skin that has lost some of its natural colour',
 'pale drained complexion': 'drained complexion, a shade lighter than the natural skin tone',
 'pale sallow drained skin': 'drained, tired skin that has lost some of its natural colour',
 'pale sickly skin tone': 'sickly skin that has lost some of its natural colour',
 'red inflamed rosacea patches': 'inflamed rosacea patches, deeper than the surrounding skin',
 'rosy pink flushed cheeks': 'warmly flushed cheeks, a shade deeper than the base skin tone',
 'ruddy wind-burned red face': 'ruddy wind-burned face, flushed deeper than the natural skin tone',
 'soft pink apple cheeks': 'soft flushed apple cheeks',
 'subtle warm pink skin flush': 'subtle warm skin flush',
 'sunburnt bright red skin': 'sunburnt, visibly inflamed skin, deeper than the natural skin tone',
 'uneven blotchy red skin patches': 'uneven blotchy skin patches, deeper than the base skin tone',
 'vibrant rosy skin bloom': 'vibrant healthy skin bloom',
 'wind-chafed red cheeks': 'wind-chafed flushed cheeks',
 # glow
 'ashen grey dull skin': 'dull lifeless skin that has lost its natural colour',
 'bronzed sun-kissed glowing skin': 'sun-kissed glowing skin, a shade deeper than the natural skin tone',
 'dull sallow lifeless skin tone': 'dull lifeless skin tone that has lost its natural colour',
 'dull, pale, thin-looking skin': 'dull, thin-looking skin that has lost some of its colour',
 'healthy rosy luminous skin': 'healthy luminous skin with a warm flush',
 'muddy dull skin tone': 'dull skin tone with no vibrancy',
 'pale cold translucent skin': 'cool translucent-looking skin, lighter than the natural skin tone',
 'pale sickly waxy skin': 'sickly waxy skin that has lost its natural colour',
 'pale translucent skin with visible veins': 'thin translucent-looking skin with visible veins',
 'sickly pale ash-grey skin': 'sickly drained skin that has lost its natural colour',
 'translucent porcelain skin glow': 'translucent delicate skin glow',
 'translucent porcelain': 'translucent delicate',
 # marks
 'cluster of small dark moles': 'cluster of small moles, darker than the surrounding skin',
 'dark mole near eye': 'mole near the eye, darker than the surrounding skin',
 'dark pigment spots on jaw': 'pigment spots on the jaw, darker than the surrounding skin',
 'faded brownish birthmark': 'faded birthmark, slightly darker than the surrounding skin',
 'freckled pale skin': 'lightly freckled skin',
 'hyper-pigmented dark skin patches': 'hyper-pigmented skin patches, darker than the surrounding skin',
 'melasma dark patches on forehead': 'melasma patches on the forehead, darker than the surrounding skin',
 'pale freckles across bridge of nose': 'faint freckles across the bridge of the nose',
 'prominent dark facial mole': 'prominent facial mole, darker than the surrounding skin',
 'prominent dark port-wine birthmark': 'prominent port-wine birthmark, deeper in colour than the surrounding skin',
 'red strawberry birthmark on skin': 'raised strawberry birthmark, deeper in colour than the surrounding skin',
 'scattered dark beauty marks': 'scattered beauty marks, darker than the surrounding skin',
 'singular sharp dark mole': 'singular sharp mole, darker than the surrounding skin',
 'small red cherry angioma spots': 'small cherry angioma spots, deeper in colour than the surrounding skin',
 'subtle pale beauty mark on cheek': 'subtle beauty mark on the cheek, slightly lighter than the surrounding skin',
 # finish
 'chalky pale skin finish': 'chalky powdery skin finish',
}
n = 0
for f in ('skin_flush', 'skin_glow', 'skin_marks', 'skin_finish'):
    p = os.path.join(ROOT, f + '.txt'); lines = open(p, encoding='utf8').read().split('\n')
    out = [M.get(l.strip(), l) for l in lines]; n += sum(a != b for a, b in zip(lines, out)); open(p, 'w', encoding='utf8', newline='\n').write('\n'.join(out))
for fn in ('age_model.py', 'supplements.py'):
    p = os.path.join(HERE, fn); s = open(p, encoding='utf8').read(); o = s
    for k in sorted(M, key=len, reverse=True): s = s.replace('"' + k + '"', '"' + M[k] + '"').replace("'" + k + "'", "'" + M[k] + "'")
    if s != o: open(p, 'w', encoding='utf8').write(s); print('patched', fn)
print('root lines changed:', n)
