"""Vocabulary expansion, face / head / neck / ear / eye-detail files.  Options are built from independent 'dimensions'
(one word from each of two or three different dimensions) so they cannot contradict each other, and they carry no colour,
age or gender wording (those belong to other files)."""
import itertools, random
from vocab_lib import S, sample, seed_of, consistent

def dims(noun, dimlists, k, n, name, fmt='{a}, {b} {noun}'):
    """dimension 0 is always the leading adjective; one value from each further chosen dimension follows the noun (pairs, and a triple when 3 dimensions exist)"""
    out = []
    for j in range(1, len(dimlists)):
        for a, b in itertools.product(dimlists[0], dimlists[j]):
            out.append(fmt.format(a=a, b=b, noun=noun))
    if len(dimlists) >= 3 and k >= 2:
        for a, b, c in itertools.product(dimlists[0], dimlists[1], dimlists[2]):
            out.append(fmt.format(a=a, b=f"{b}, {c}", noun=noun))
    out = [o for o in out if consistent(o)]
    return sample(out, n, name)

R = {}   # filename -> function(original_options) -> list of new options

def reg(name, noun, dimlists, k=2, n=320, fmt='{a}, {b} {noun}', extra=None):
    def f(orig, noun=noun, dimlists=dimlists, k=k, n=n, fmt=fmt, extra=extra, name=name):
        out = dims(noun, dimlists, k, n, name, fmt)
        if extra: out += S(extra) if isinstance(extra, str) else list(extra)
        return out
    R[name] = f

# ---------------------------------------------------------------- head
reg('head_shape', 'face shape',
    [S("oval, round, square, oblong, heart-shaped, diamond-shaped, pear-shaped, triangular, rectangular, long, short, wide, narrow, rounded-square, egg-shaped, inverted-triangle, kite-shaped, lantern-shaped, elongated-oval, compact-round"),
     S("with softly contoured planes, with sharply contoured planes, with strongly angular planes, with gently curved lines, with smoothly tapering lines, with evenly proportioned features, with slight asymmetry, with a full lower face, with a lean lower face, with flat planes, with high planes, with a rounded brow line, with a squared brow line"),
     S("with a broad forehead, with a narrow forehead, with prominent cheekbones, with a strong jaw, with a soft jaw, with a pointed chin, with a rounded chin, with a wide jaw, with a tapering chin, with a high hairline, with a low hairline, with a compact lower face")],
    k=2, n=330, fmt='{a} {noun} {b}')

reg('head_chin', 'chin', [S("pointed, rounded, square, cleft, dimpled, receding, prominent, flat, tapered, broad, narrow, small, large, forward-set, squared-off, softly pointed, oval, long, short, heavy"),
    S("with a deep central cleft, with a faint dimple, with a smooth contour, with a defined edge, with a soft underside, with a firm line, with a slight curve, with a pronounced tip, with a gentle taper, with no definition")], k=2, n=260, fmt='{a} {noun} {b}')
reg('head_jaw', 'jawline', [S("sharp, soft, square, angular, rounded, wide, narrow, tapered, strong, delicate, prominent, subtle, broad, squared-off, V-shaped, U-shaped, long, short, curved, straight"),
    S("that is clearly defined, that is softly defined, that is barely defined, that is sculpted, that flows smoothly, that is boldly angled, that is gently angled, that is firmly set, that looks relaxed, that looks tense"),
    S("with a pronounced angle at the corner, with a gentle rise to the ear, with a flat underside, with a curved underside, with visible bone structure, with soft padding, with a slight overbite shadow, with a high jaw angle, with a low jaw angle")], k=2, n=330, fmt='{a} {noun} {b}')
reg('head_cheek', 'cheeks', [S("high, low, flat, rounded, prominent, subtle, full, lean, wide, narrow, sculpted, softly padded, hollowed, broad, angular, curved, dimpled, smooth, plump, tight"),
    S("with prominent cheekbones, with soft apples, with a gentle slope, with defined hollows, with broad cheekbone width, with a flat plane, with a rounded fullness, with a slight asymmetry, with pronounced contours, with delicate contours"),
    S("when relaxed, when smiling, in profile, in three-quarter view, under side light, in soft light")], k=2, n=300, fmt='{a} {noun} {b}')
reg('head_temple', 'temples', [S("flat, gently curved, slightly hollow, full, narrow, broad, smooth, subtly sunken, rounded, bony, padded, recessed, prominent, even, wide-set, tapered, high, low, shallow, deep, long, short, firm, sculpted, dimpled, defined, soft, delicate, squared"),
    S("with faint visible veins, with smooth skin, with soft shading, with a clear bone line, with a gentle dip, with a rounded contour, with a slight bulge, with neat hairline edges, with fine hairs at the edges, with a defined edge")], k=2, n=260, fmt='{a} {noun} {b}')
reg('head_brow', 'forehead', [S("high, low, broad, narrow, rounded, flat, sloping, domed, tall, short, wide, smooth, vertical, gently curved, prominent, squared, heart-shaped, even"),
    S("with a pronounced brow ridge, with a soft brow ridge, with a flat brow line, with a slight bulge above the brows, with defined frontal bones, with smooth skin, with a gentle curve into the hairline, with a widow's-peak hairline, with a straight hairline, with a rounded hairline, with a receding hairline edge, with soft temples"),
    S("catching the light, in soft shadow, in even light")], k=2, n=300, fmt='{a} {noun} {b}')
reg('neck_length', 'neck', [S("long, short, medium-length, slender, thick, thin, broad, narrow, graceful, sturdy, elegant, compact, strong, delicate, tapered, cylindrical, swan-like, stocky, wide-set, tall"),
    S("set high on the shoulders, set low on the shoulders, held upright, held forward, carried tilted, with a straight line, with a slight curve, with visible tendons, with soft contours, with a defined nape, with a smooth line into the shoulders, with a gentle slope to the shoulders"),
    S("in profile, from the front, from behind")], k=2, n=300, fmt='{a} {noun} {b}')
reg('neck_crease', 'neck skin', [S("smooth, softly lined, fine-lined, deeply creased, taut, slack, finely textured, supple, firm, relaxed, dry, hydrated, matte, soft, tight, loose, plump"),
    S("with one horizontal line, with two faint horizontal lines, with a subtle fold at the front, with fine vertical lines, with soft folds when turned, with a visible crease at the base, with creases that deepen when looking down, with gentle skin folds beneath the chin, with a smooth transition to the chest, with a taut surface, with a slightly textured surface, with a soft ripple when turned, with a faint line across the base, with a gentle fold above the collar, with a pronounced centre line, with a smooth glide to the jaw, with a loose drape, with a firm contour")], k=2, n=260, fmt='{a} {noun} {b}')
reg('neck_clav', 'collarbones', [S("prominent, subtle, delicate, strong, broad, narrow, straight, gently curved, sharply defined, softly padded, barely visible, deeply set, horizontal, slightly angled, long, short, visible, symmetrical, slightly asymmetrical"),
    S("with a defined hollow above, with a smooth line to the shoulder, with a soft hollow, with visible bone ends, with a gentle S-curve, with a flat profile, with a pronounced notch at the centre, with a shallow notch, with soft shading beneath, with highlights along the ridge, with a thin soft shadow underneath, with a pronounced upper edge, with a faint outline under the skin, with a flat top, with a rounded top, with a slight upward tilt at the ends, with a wide span, with a narrow span, with a shiny glint on the bone, with a matte surface, with a shallow dip near the shoulder")], k=2, n=260, fmt='{a} {noun} {b}')
reg('neck_muscle', 'neck muscles', [S("defined, soft, lean, strong, relaxed, flexed, prominent, subtle, athletic, slim, thick, rounded, tendon-forward, smooth, sculpted, broad, tight, ropy, long, short, firm, delicate, solid, wiry, pronounced, understated, toned, compact, powerful"),
    S("with visible sternocleidomastoid lines, with a clear trapezius slope, with a soft transition to the shoulders, with a V-shaped dip at the base, with relaxed tendons, with tension on one side, with a strong jaw-to-collarbone line, with a smooth surface, with visible cords when turning, with a gentle slope")], k=2, n=260, fmt='{a} {noun} {b}')

# ---------------------------------------------------------------- eyes (shape and surroundings)
reg('eye_shape', 'eyes', [S("almond-shaped, round, narrow, wide, deep-set, hooded, upturned, downturned, monolid, prominent, sleepy, wide-set, close-set, large, small, oval, slanted, cat-like, doe-like, protruding, level, angled, soft, sharp"),
    S("with a defined crease, with a hidden crease, with a double eyelid fold, with a single eyelid, with a gentle upward tilt, with a gentle downward tilt, with a long outer corner, with a rounded inner corner, with a pointed inner corner, with a visible tear duct, with a heavy upper lid, with a lifted outer corner, with a soft lower lid line, with an almond outline"),
    S("under straight brows, under arched brows, under a prominent brow ridge, under a smooth brow, framed by long lashes, framed by short lashes, in a relaxed gaze, in an alert gaze, in a soft gaze")], k=2, n=340, fmt='{a} {noun}, {b}')
reg('eye_spacing', 'eye spacing', [S("wide, narrow, average, very wide, slightly wide, slightly narrow, balanced, close, generous, tight, even, symmetrical, slightly uneven"),
    S("with a broad nose bridge, with a narrow nose bridge, with a low nose bridge, with a high nose bridge, with a flat bridge between them, with prominent inner corners, with soft inner corners, with a gap about one eye wide, with a gap narrower than one eye, with a gap wider than one eye"),
    S("giving a calm look, giving an open look, giving an intense look, giving a gentle look, giving a focused look, giving a wide-eyed look")], k=2, n=280, fmt='{a} {noun}, {b}')
reg('eye_lid', 'eyelids', [S("smooth, creased, hooded, heavy, light, thin, thick, double-fold, single-fold, deep-creased, shallow-creased, defined, soft, firm, translucent, full, narrow, tapered, puffy, tight"),
    S("with a crisp crease line, with a crease that disappears at the outer edge, with a slight droop at the outer corner, with a visible lash line, with hidden lash roots, with a soft fold above, with a high crease, with a low crease, with a tapered fold, with a parallel fold, with visible fine veins, with a faintly shadowed lid"),
    S("when the eyes are open wide, when the eyes are relaxed, when looking down, when looking up, when looking sideways")], k=2, n=300, fmt='{a} {noun}, {b}')
reg('eye_brow', 'eyebrows', [S("thick, thin, bushy, full, sparse, arched, straight, rounded, angular, soft, bold, feathery, tapered, flat, high-arched, low-set, high-set, wide-set, close-set, neat, unruly, groomed, natural, sleek, fluffy, defined, faint, strong, elongated, short"),
    S("with a gentle arch, with a sharp peak, with a flat line, with a rounded arch, with a long tail, with a short tail, with a soft front edge, with a blunt front edge, with hairs growing upward, with hairs combed flat, with hairs growing in different directions, with a clean lower edge, with a slight gap in the middle, with a gentle upward slant, with a gentle downward slant, with a slight asymmetry")], k=2, n=320, fmt='{a} {noun} {b}')
reg('eye_sclera', 'sclera', [S("clear, bright, clean, soft, slightly veined, finely veined, glossy, matte, moist, dry, calm, pale, smooth, evenly toned, translucent, lightly tinted, softly shaded, slightly speckled, healthy, natural"),
    S("with a thin visible vessel at the corners, with soft shading near the upper lid, with a gentle pigment line at the edge, with fine capillaries, with a crisp limbal edge, with a soft limbal ring, with no visible vessels, with a faint tear film shine, with moisture at the lower lid, with pronounced whites around the iris, with whites only partly showing")], k=2, n=260, fmt='{a} {noun} {b}')
R['eye_lash'] = None   # handled in vocab_face2 (gendered files)

# ---------------------------------------------------------------- nose
reg('nose_bridge', 'nose bridge', [S("high, low, narrow, wide, straight, concave, convex, flat, rounded, sharp, soft, prominent, subtle, long, short, delicate, strong, slightly bent, smooth, bony, refined, broad, gently humped, scooped, arched"),
    S("with a gentle dip below the brow, with a slight bump, with a defined edge, with a smooth line to the tip, with a gentle slope, with a straight profile, with a subtle curve, with a visible bone ridge, with soft sides, with a slight lean to one side, with a wide base, with a narrow base"),
    S("in profile, from the front, in three-quarter view")], k=2, n=300, fmt='{a} {noun} {b}')
reg('nose_tip', 'nose tip', [S("rounded, pointed, upturned, downturned, bulbous, narrow, wide, soft, defined, flat, button-like, refined, fleshy, slim, projected, drooping, bifid, heart-shaped, boxy, broad, small, tiny, large, blunt, teardrop-shaped"),
    S("with a slight upward tilt, with a slight downward tilt, with soft cartilage, with firm cartilage, with a faint dimple, with a visible dividing line, with a gentle projection, with little projection, with a rounded base, with a defined edge, with a delicate outline, with a slightly off-centre point, with smooth skin, with visible pores"),
    S("in profile, from the front, from below")], k=2, n=300, fmt='{a} {noun} {b}')
reg('nose_nostril', 'nostrils', [S("narrow, wide, round, oval, teardrop-shaped, slit-like, flared, tucked, small, large, symmetrical, slightly asymmetrical, visible, hidden, high-set, flat, elongated, pinched, open, delicate, thick-walled, thin-walled"),
    S("with a neat outline, with a soft inner curve, with a visible rim, with gentle flare when breathing, with a slim alar edge, with a rounded alar edge, with a pronounced alar groove, with a faint crease at the base, with a slim columella, with a broad columella, with a hanging columella, with a retracted columella")], k=2, n=260, fmt='{a} {noun} {b}')
reg('nose_crease', 'nasolabial lines', [S("faint, deep, shallow, soft, sharp, long, short, curved, straight, symmetrical, asymmetrical, subtle, defined, smooth, gentle, pronounced, delicate, wide, narrow"),
    S("that deepen when smiling, that stay visible at rest, that curve around the mouth, that run straight down, that end at the mouth corner, that continue below the mouth, that are barely visible, that are clearly visible in side light, that soften with the cheeks, that frame the mouth, that fade toward the chin, that begin near the nostril wing, that start high on the cheek, that start low near the mouth, that look softer in even light, that look sharper in side light, that disappear when relaxed, that appear only when laughing, that run parallel to the lips")], k=2, n=240, fmt='{a} {noun} {b}')
reg('nose_philtr', 'philtrum', [S("short, long, deep, shallow, narrow, wide, defined, smooth, flat, curved, straight, subtle, pronounced, soft, sharp-edged, concave, convex, symmetrical, slightly asymmetrical"),
    S("with clear ridges, with soft ridges, with a gentle groove, with a deep groove, with a smooth surface, with fine downy hair, with a defined arch at the top, with a wide base, with a narrow base, with a slight shadow, with a gentle curve into the lip")], k=2, n=240, fmt='{a} {noun} {b}')

# ---------------------------------------------------------------- mouth
reg('lip_fullness', 'lips', [S("full, thin, plump, medium, wide, narrow, pillowy, balanced, soft, firm, heavy, delicate, generous, small, large, subtle, defined, even, uneven, bow-shaped, flat"),
    S("with a fuller lower lip, with a fuller upper lip, with equal upper and lower lips, with a defined centre peak, with soft edges, with a sharp outline, with a gentle curve, with a straight line, with a slight downturn, with a slight upturn, with a visible lip line, with a gentle pout, with a relaxed closure, with the lips slightly parted, with the lips pressed together"),
    S("in a neutral expression, in a soft smile, in a calm expression")], k=2, n=320, fmt='{a} {noun} {b}')
reg('lip_cupid', "Cupid's bow", [S("defined, soft, sharp, flat, wide, narrow, deep, shallow, high-peaked, low-peaked, rounded, symmetrical, asymmetrical, subtle, dramatic, gentle, pronounced, double-peaked, smooth, angular"),
    S("with a distinct dip, with a barely visible dip, with a curved top line, with a straight top line, with peaks close together, with peaks far apart, with soft peaks, with sharp peaks, with a crisp outline, with a blurred outline, with a shallow center dip, with a deeper center dip")], k=2, n=240, fmt='{a} {noun} {b}')
reg('lip_corners', 'mouth corners', [S("upturned, downturned, level, neutral, soft, sharp, tucked, relaxed, tense, deep-set, defined, turned up slightly, turned down slightly, curved, straight, symmetrical, asymmetrical, lifted, drooping, smiling, firm"),
    S("with a small dimple, with a faint line, with a shadow at the edge, with a smooth edge, with a visible fold, with gentle creases when smiling, with a slight uplift on one side, with a neat finish, with a soft finish, with no creases")], k=2, n=240, fmt='{a} {noun} {b}')
reg('lip_teeth', 'teeth', [S("straight, slightly crooked, evenly spaced, gapped, crowded, small, large, prominent, uniform, natural-looking, neat, irregular, slightly overlapping, protruding, aligned, rounded-edged, square-edged, pointed canines, long front, short front, broad front"),
    S("with a gap between the front teeth, with slightly overlapping incisors, with a slight overbite, with a slight underbite, with a visible lower row, with an upper row only showing, with the tips of the lower teeth visible, with a straight bite, with a wide smile arc, with a narrow smile arc, with an even edge line, with natural translucency at the edges, with a small chip, with a sharp canine, with a slight twist in one tooth"),
    S("in a closed-mouth smile, in a wide smile, in a slight smile, when talking, when laughing")], k=2, n=300, fmt='{a} {noun} {b}')
reg('lip_gums', 'gum line', [S("low, high, even, uneven, shallow, neat, defined, smooth, visible, hidden, symmetrical, asymmetrical, soft, firm, thin, thick, scalloped, straight, subtle, pronounced"),
    S("showing when smiling widely, showing only a little when smiling, hidden when smiling, showing above the upper teeth, showing slightly on one side, with a smooth outline, with a scalloped outline, with a thin pink band above the teeth, with healthy contours, with a neat margin, with papillae filling the gaps, with a slight gummy smile")], k=2, n=240, fmt='{a} {noun} {b}')

# ---------------------------------------------------------------- ears
reg('ear_shape', 'ears', [S("small, large, round, oval, pointed, narrow, wide, protruding, flat against the head, folded, lobed, long, short, high-set, low-set, symmetrical, asymmetrical, prominent, subtle, tucked, upright, cupped, angular, soft-edged, sharp-edged"),
    S("with a defined helix, with a soft helix, with a prominent antihelix, with a flat antihelix, with a pronounced curl at the top, with a Darwin's tubercle, with a smooth outer rim, with a folded rim, with a deep concha, with a shallow concha, with a pronounced tragus, with a delicate shape, with a thick rim, with a thin rim, with a slight outward tilt, with an upright set"),
    S("partly covered by hair, fully visible, in profile, from behind")], k=2, n=300, fmt='{a} {noun}, {b}')
reg('ear_lobe', 'earlobes', [S("long, short, round, pointed, attached, detached, free-hanging, small, large, thick, thin, soft, firm, plump, delicate, heavy, flat, curved, tapering, creased, smooth"),
    S("with a pierced hole, with several piercings, with no piercings, with a small stud, with a faint crease, with a visible ridge, with a notch, with a sagging weight, with a neat edge, with a slight curl, with a soft outline, with a firm edge")], k=2, n=240, fmt='{a} {noun} {b}')
