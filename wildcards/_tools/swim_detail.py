"""Builds a full clear description (front, back, what is covered and uncovered, cut) for every swimwear name, so no swimsuit relies on its name alone."""
import re, zlib
WET = ["When wet, the thin fabric turns translucent, so the skin and the shapes beneath show through", "Once soaked, the light-weight fabric becomes see-through and clings, showing what lies under it", "Wet, the material goes translucent and reveals the skin underneath, especially across the lined-free areas", "The unlined fabric turns sheer when it gets wet, letting the body show through the colour"]
def has(n, *w): return any(x in n for x in w)
def swim_detail(k, name):
    n = name.lower(); f = []; b = []; cv = []; un = []
    if k == 'swim_dive':
        if has(n, 'shorty', 'springsuit'): cv.append('the torso and the tops of the thighs and upper arms'); un.append('the lower arms and lower legs')
        elif has(n, 'rash guard', 'shirt', 'vest', 'jacket', 'poncho', 'robe'): cv.append('the torso and arms' if has(n, 'long', 'shirt', 'rash') else 'the torso'); un.append('the legs')
        elif has(n, 'booties', 'gloves', 'hood', 'mask'): cv.append('the hands, feet or head'); un.append('the rest of the body')
        else: cv.append('the whole body from the neck to the ankles and wrists'); un.append('the head, hands and feet')
        f.append('a close, smooth-skinned front with a zip or neck seal' if has(n, 'zip', 'suit', 'drysuit') else 'a smooth snug front'); b.append('a back zip or chest zip closure and taped seams' if has(n, 'zip', 'suit') else 'a smooth back with flat seams')
        return desc(f, b, cv, un, name=name, fit='snug, stretchy and body-hugging')
    if k == 'swim_cover':
        f.append('a loose open or wrapped front'); b.append('a flowing back'); cv.append('the body over a swimsuit, to the hips, thighs or ankles'); un.append('the arms and lower legs')
        if has(n, 'sheer', 'mesh', 'net', 'gauze', 'crochet', 'transparent'): un.append('the swimsuit beneath, seen through the sheer fabric')
        return desc(f, b, cv, un, name=name, fit='loose, light and draped')
    if k == 'swim_trunks':
        f.append('a waistband with a drawstring or elastic'); cv.append('the hips and part of the thighs')
        L = 'above the knee' if has(n, 'short-cut', 'short-short', 'retro') else 'to the mid-thigh' if has(n, 'mid-thigh', 'jammer') else 'to the knee' if has(n, 'knee', 'long') else 'to the upper thigh'
        b.append('a full seat that reaches ' + L); un.append('the legs below the hem and the torso')
        if has(n, 'sheer'): un.append('the skin seen through the sheer lining')
        return desc(f, b, cv, un, name=name, fit=f'a straight leg cut {L}')
    if k == 'swim_brief':
        f.append('a contoured pouch front on a waistband' if has(n, 'pouch', 'contoured', 'jock') else 'a small front panel on a waistband'); cv.append('the groin and the front of the hips')
        if has(n, 'thong', 'g-string', 'string', 'micro', 'jockstrap'): b.append('a thong back with a narrow strap between the buttocks'); un.append('the buttocks and the upper thighs')
        elif has(n, 'brazilian', 'cheeky'): b.append('a scooped back that shows part of the buttocks'); un.append('the lower part of the buttocks')
        else: b.append('a full back covering the buttocks'); un.append('the thighs')
        if has(n, 'sheer', 'mesh'): un.append('the skin seen through the sheer or mesh fabric')
        return desc(f, b, cv, un, name=name, fit='a low or high leg cut, snug' + (', with narrow side straps' if has(n, 'side', 'string', 'tie') else ''))
    if k == 'swim_retro':
        f.append('a modest fitted front in the style of its period'); b.append('a back that is closed or lightly scooped to match the period'); cv.append('the torso and hips, and often the thighs or upper legs'); un.append('the arms and lower legs' if has(n, 'wool', 'sailor', 'bloomers', 'gown') else 'the arms, the legs and the midriff where the style is two-piece')
        if has(n, 'bikini', 'thong', 'string'): cv = ['the chest and the hips']; un = ['the midriff, the back and a good part of the buttocks']
        return desc(f, b, cv, un, name=name, fit='fitted, with period shaping' + (' and a skirt' if has(n, 'skirt') else ''))
    # one-piece, bikini, extreme, novelty
    one = k == 'swim_onepiece' or has(n, 'one-piece', 'monokini', 'sling', 'suspender', 'pretzel', 'swimsuit')
    if has(n, 'sling', 'suspender', 'slingshot'):
        f.append('a small front panel whose two side straps rise up over the chest and across both shoulders, joining behind the neck'); b.append('the straps meet at the nape and run down the middle of the back into a thong'); cv.append('only the nipples and the pubic area'); un.append('the sides of the torso, the back and the buttocks')
        return desc(f, b, cv, un, name=name, fit='one-piece, strap-held and very minimal')
    if has(n, 'pretzel'):
        f.append('a small chest panel with a strap looped around the neck and a second set of straps circling the midriff'); b.append('an open back with the midriff straps tied at the spine'); cv.append('the nipples and the pubic area'); un.append('the rest of the torso and the back')
        return desc(f, b, cv, un, name=name, fit='strap-based and minimal')
    if has(n, 'monokini', 'pubikini'):
        f.append('a high-waisted bottom linked to two straps that rise to a halter neck, leaving the chest bare' if not has(n, 'chain', 'mesh', 'link') else 'a bikini top and bottom joined down the centre by chains or a sheer mesh panel'); b.append('a low open back with a tie at the neck and the waist'); cv.append('the hips and the stomach'); un.append('the chest and the back' if not has(n, 'chain', 'mesh', 'link') else 'the sides of the torso')
        return desc(f, b, cv, un, name=name, fit='one-piece, halter-held')
    if has(n, 'micro', 'g-string', 'string bikini', 'invisible', 'peek', 'crotchless', 'seekini', 'teardrop', 'hikini') or (has(n, 'sheer') and 'when wet' not in n and 'when soaked' not in n and not one and not has(n, 'brief', 'shorts', 'sarong')):
        f.append('tiny triangle cups on thin strings and a very small front piece'); b.append('a string or thong back with very little fabric'); cv.append('the nipples and the pubic area'); un.append('the sides of the chest, the hips and the buttocks')
        if has(n, 'crotchless', 'peek'): un.append('the genital area through an open slit')
        if has(n, 'sheer', 'seekini', 'invisible'): un.append('the skin seen through the sheer or clear-look fabric')
        return desc(f, b, cv, un, name=name, fit='extremely small, tied at the neck and hips')
    if one:
        f.append('a one-piece front from neckline to leg opening'); b.append('a closed back' if not has(n, 'backless', 'open-back', 'open back', 'low', 'plunging lace-up', 'halter', 'strappy') else 'a low open back showing most of the back'); cv.append('the chest, stomach and hips'); un.append('the arms and legs')
        if has(n, 'plunging', 'deep v', 'v-neck'): f.append('a plunging neckline down to the navel'); un.append('the upper chest and the centre of the chest')
        if has(n, 'cut-out', 'window', 'side', 'monokini'): un.append('skin at the sides and the stomach through cut-outs')
        if has(n, 'thong'): b.append('a thong seat'); un.append('the buttocks')
        elif has(n, 'high-cut', 'bikini-cut', 'brief-leg'): b.append('high-cut leg openings over the hips'); un.append('the upper thighs and hips')
        if has(n, 'long-sleeved'): cv.append('the arms'); un = [u for u in un if u != 'the arms and legs'] + ['the legs']
        if has(n, 'sheer', 'mesh'): un.append('the skin seen through the sheer panels')
        return desc(f, b, cv, un, name=name, fit='snug and body-fitting')
    f.append('two small cups or triangles for the chest and a separate bottom'); cv.append('the nipple area and the pubic area at least')
    if has(n, 'bandeau'): f[-1] = 'a straight strapless band across the chest and a separate bottom'
    if has(n, 'halter'): f[-1] = 'cups held by a halter strap around the neck and a separate bottom'
    if has(n, 'underwire', 'push-up', 'balconette'): f[-1] = 'underwire or padded cups lifting the chest and a separate bottom'
    if has(n, 'tankini', 'camikini'): f[-1] = 'a tank or camisole top reaching the midriff and a separate bikini bottom'; cv.append('the chest and midriff')
    if has(n, 'thong'): b.append('a thong back with a narrow strap between the buttocks'); un.append('the buttocks')
    elif has(n, 'cheeky', 'scrunch', 'brazilian'): b.append('a scooped or ruched back that shows part of the buttocks'); un.append('the lower buttocks')
    elif has(n, 'high-waist', 'high waist', 'retro', 'boy'): b.append('a full back covering the buttocks'); un.append('the midriff above the waist')
    else: b.append('a back with a low-cut bottom covering most of the buttocks'); un.append('the midriff, the back and the sides of the hips')
    b.append('a tied or hooked strap across the back')
    if has(n, 'sheer', 'mesh'): un.append('the skin seen through the sheer fabric')
    if has(n, 'lace-up', 'tie'): b.append('tied or laced sides')
    return desc(f, b, cv, un, name=name, fit='low-rise and snug' + (', with tie sides' if has(n, 'tie') else ''))
def jn(x):
    x = list(dict.fromkeys(x)); return x[0] if len(x) == 1 else ', '.join(x[:-1]) + ' and ' + x[-1]
def desc(f, b, cv, un, fit, name=''):
    wet = ''
    if name and zlib.crc32(name.encode()) % 100 < 45 and not has(name.lower(), 'wetsuit', 'neoprene', 'drysuit', 'poncho', 'robe', 'terry'): wet = '. ' + WET[zlib.crc32(name.encode()) % len(WET)]
    return f"Front: {'; '.join(f)}. Back: {'; '.join(b)}. It covers {jn(cv)}, and leaves {jn(un)} uncovered. Cut and fit: {fit}{wet}"
