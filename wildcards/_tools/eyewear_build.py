"""Builds the eyewear files (5,000 lines each):  acc_glasses (whole population) and age<lo>_<hi>_opt_eyewear (one per age bracket).
Each line is a ready-to-use sentence, or a BLANK line = "nothing visible" (no glasses and no contact lenses).  Shares per age (glasses / sunglasses /
contact lenses / none) are rough estimates of how many adults wear each, and rise with age because of presbyopia.  Exactly 0.5% of the lines are
a monocle and 0.5% are an eyepatch in every file.  Every one of the 28 options of the original acc_glasses.txt is kept at least once.
Run by build_all.py (step 'eyewear'); needs data/acc_glasses_original.txt."""
import os, sys, random, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from paths import wc_dir, DATA, gender
from gender import pron
from age_model import BRACKETS, BRACKET_SHARE, bname, Kbracket, U, D, P, FLAT
from wcbuild import allocate
WC = wc_dir(); N = 5000
ORIG = [l.strip() for l in open(os.path.join(DATA, 'acc_glasses_original.txt'), encoding='utf8') if l.strip()]
ORIG = list(dict.fromkeys(ORIG))
# ---- shares (%) per bracket: prescription/reading glasses, sunglasses, contact lenses  (the rest wears nothing visible) ----
SHARE = {  # glasses, sunglasses, contacts
 0: (22, 6, 16), 1: (27, 6, 16), 2: (32, 6, 12), 3: (45, 6, 7), 4: (60, 6, 4), 5: (68, 6, 2), 6: (72, 5, 1), 7: (72, 4, .5), 8: (68, 3, .2)}
EYEWEAR_SCALE = 0.5   # user request: show eyewear half as often - the lines are replaced by blank (no eyewear) lines
SHARE = {k: tuple(round(x * EYEWEAR_SCALE, 2) for x in v) for k, v in SHARE.items()}
MONO, PATCH = 0.5, 0.5       # percent of lines, every file

# ---- glasses: components (value, weight, age spec) ----
def w(items): return [(v, wt, sp) for v, wt, sp in items]
SHAPE = w([("round", 12, FLAT), ("oval", 10, FLAT), ("rectangular", 14, FLAT), ("square", 8, FLAT), ("cat-eye", 6, D(55, 18, .4)), ("aviator", 6, FLAT), ("browline", 7, FLAT),
  ("hexagonal", 3, D(40, 12, .15)), ("wayfarer", 6, D(50, 16, .3)), ("panto", 4, FLAT), ("oversized butterfly", 3, FLAT), ("half-rim", 5, U(40, 14, .3, 1.6)), ("rimless", 5, U(40, 14, .3, 1.8)),
  ("narrow rectangular", 5, U(45, 14, .3, 1.6)), ("rounded-square", 6, FLAT), ("geometric angular", 3, D(40, 12, .1)), ("teardrop", 2, FLAT), ("clubmaster-style", 3, FLAT), ("octagonal", 2, D(40, 12, .15)),
  ("large round retro", 3, D(45, 14, .2)), ("small oval", 4, U(50, 14, .3, 1.6)), ("heart-shaped", 1, D(30, 8, .05)), ("double-bridge", 2, FLAT), ("cat-eye with upswept corners", 3, FLAT)])
MATERIAL = w([("thin metal", 12, FLAT), ("wire", 8, FLAT), ("titanium", 7, U(35, 14, .3, 1.5)), ("acetate", 14, FLAT), ("horn", 3, U(45, 14, .3, 1.6)),
  ("plastic", 12, FLAT), ("wooden", 1.5, D(45, 14, .3)), ("carbon-fibre", 1.5, D(50, 14, .3)), ("brushed steel", 3, FLAT), ("bamboo", 1, D(45, 14, .4)),
  ("mixed metal-and-acetate", 5, FLAT), ("recycled-plastic", 1.5, D(45, 14, .3)), ("translucent resin", 3, D(40, 12, .15)), ("lightweight flexible", 3, U(55, 14, .3, 1.6))])
COLOUR = w([("black", 20, FLAT), ("tortoiseshell", 12, FLAT), ("gold", 9, U(45, 14, .4, 1.5)), ("silver", 9, U(45, 14, .4, 1.5)), ("rose-gold", 3, D(45, 14, .2)), ("gunmetal grey", 5, FLAT), ("clear", 5, D(45, 14, .3)),
  ("crystal grey", 3, D(45, 14, .3)), ("burgundy", 3, FLAT), ("navy blue", 3, FLAT), ("olive green", 2, FLAT), ("forest green", 2, FLAT), ("brown", 7, FLAT), ("bold red", 3, D(50, 16, .3)),
  ("cobalt blue", 2, D(45, 14, .2)), ("pink", 2, D(40, 12, .15)), ("white", 1.5, D(45, 14, .3)), ("two-tone", 3, FLAT), ("matte black", 5, FLAT), ("copper", 1.5, FLAT), ("lavender", 1, D(40, 12, .1)),
  ("yellow", 1, D(40, 12, .1)), ("tan", 2, FLAT), ("transparent pink", 2, D(40, 12, .1)), ("neon orange", .6, D(32, 8, .05)), ("silver-white", 3, U(65, 12, .3, 1.5))])
LENS = w([("clear prescription lenses", 40, FLAT), ("thick strong lenses that shrink the eyes", 2, U(60, 14, .2, 2.0)), ("thick strong lenses that magnify the eyes", 2, U(60, 14, .2, 2.0)),
  ("thin anti-glare lenses showing a faint reflection", 10, FLAT), ("blue-light filter lenses with a faint blue sheen", 5, D(45, 14, .15)), ("photochromic lenses with a slight grey tint", 4, FLAT),
  ("progressive lenses", 4, U(45, 8, .02, 3.5)), ("bifocal lenses with a visible line", 2, U(60, 10, .02, 3)), ("lenses with a faint gradient tint", 3, FLAT), ("lightly tinted lenses", 3, FLAT),
  ("smudged lenses", 1.5, FLAT), ("scratched lenses", 1, FLAT), ("lenses with a visible edge curve", 3, FLAT)])
STATE = w([("sitting neatly on the nose", 40, FLAT), ("sliding down the nose", 6, FLAT), ("pushed up onto the head", 4, FLAT), ("hanging from a chain around the neck", 2.5, U(60, 12, .1, 3)),
  ("perched low on the nose, looked over", 2.5, U(55, 10, .1, 3)), ("held in one hand", 2, FLAT), ("slightly crooked on the face", 3, FLAT), ("with a hinge repaired by a bit of tape", 1, FLAT),
  ("with a beaded strap behind the head", 1, U(60, 12, .1, 2.5)), ("with a coloured retainer cord", 1.5, U(55, 12, .2, 2)), ("fitted snugly", 10, FLAT), ("worn with a light, slightly fogged edge", 1, FLAT)])
SUN_TINT = w([("dark smoke", 20, FLAT), ("mirrored silver", 9, D(45, 14, .3)), ("mirrored blue", 3, D(40, 12, .15)), ("amber-brown", 10, FLAT), ("green", 8, FLAT), ("gradient grey", 8, FLAT),
  ("rose", 3, D(40, 12, .15)), ("yellow", 2, FLAT), ("polarised dark", 8, FLAT), ("pale blue", 2, D(40, 12, .15)), ("purple", 1, D(35, 10, .1)), ("copper mirrored", 2, FLAT)])
SUN_SHAPE = w([("aviator", 15, FLAT), ("wayfarer", 14, FLAT), ("round", 10, FLAT), ("oversized square", 8, FLAT), ("cat-eye", 8, D(55, 18, .4)), ("sporty wraparound", 8, D(55, 16, .3)), ("shield", 4, D(45, 12, .2)),
  ("narrow rectangular", 5, D(45, 14, .3)), ("oversized round", 5, FLAT), ("pilot", 4, FLAT), ("clip-on flip-up", 2, U(55, 12, .2, 2)), ("wrap-around over prescription glasses", 3, U(60, 12, .1, 3)),
  ("heart-shaped", .6, D(30, 8, .03)), ("tiny round", 2, D(40, 12, .1)), ("hexagonal", 1.5, D(40, 12, .1)), ("browline", 4, FLAT)])
SPECIAL = w([("heavy safety goggles with a strap", 3, FLAT), ("swimming goggles pushed up on the forehead", 2, D(40, 12, .1)), ("welding goggles", 1, FLAT), ("aviator flying goggles", 1, FLAT), ("ski goggles pushed up", 2, FLAT),
  ("futuristic neon visor glasses", 1, D(40, 10, .05)), ("steampunk brass goggles", 1, D(45, 14, .1)), ("protective lab goggles", 2, FLAT), ("magnifying loupe glasses", 1.5, U(40, 14, .2, 1.5)),
  ("thick round magnifying glasses", 2, U(55, 12, .2, 2)), ("goggles pushed up on forehead", 2, FLAT), ("reading half-glasses on a chain", 2, U(55, 10, .05, 3)), ("pince-nez clamped on the bridge of the nose", .6, FLAT),
  ("a lorgnette on a handle held up to the eyes", .3, U(65, 12, .02, 3)), ("sports goggles with a rubber strap", 2, D(45, 14, .2)), ("blue-lensed gaming glasses", 1, D(35, 10, .05)), ("cracked, taped-together broken glasses", 1.2, FLAT),
  ("dust-covered cracked glasses", .8, FLAT), ("smudged glasses covered in fingerprints", 1.2, FLAT), ("smart glasses with a thick temple", 1, D(45, 14, .15)), ("tinted driving glasses with a yellow tint", 1, FLAT)])
GL_T = ["She wears {a} {shape} pair of {material} glasses with {colour} frames and {lens}, {state}.", "Her eyewear is {a} {shape} pair of {colour} {material} glasses with {lens}, {state}.",
        "She has {a} {shape} {colour} frame, made of {material}, with {lens}, {state}.", "She is wearing {colour} {shape} glasses of {material} with {lens}, {state}.",
        "On her face is {a} {shape} pair of {material} glasses in {colour} with {lens}.", "Her glasses are {shape} and {colour}, made of {material} with {lens}, {state}."]
RD_T = ["She wears {a} {shape} pair of {colour} reading glasses, {state}.", "Her small {shape} {colour} reading glasses are {state}.", "She has {a} {shape} {colour} pair of half-moon reading glasses, {state}."]
SUN_T = ["She wears {a} {sshape} pair of sunglasses with {tint} lenses.", "Her eyes are hidden behind {a} {sshape} pair of {tint} sunglasses.", "She is wearing {tint} {sshape} sunglasses with {fcolour} frames.",
         "She has {tint}-lensed {sshape} sunglasses on, with {fcolour} frames.", "Her {sshape} sunglasses have {fcolour} frames and {tint} lenses."]
SP_T = ["Her eyewear is {s}.", "She wears {s}.", "She has {s}."]
CONTACT = w([("She wears clear contact lenses and no glasses.", 40, FLAT), ("She wears soft contact lenses, faintly visible at the edge of the iris.", 25, FLAT),
  ("She wears daily disposable contact lenses and her eyes show a thin lens edge.", 8, D(40, 12, .1)), ("She wears cosmetic contact lenses that add a subtle ring around her irises.", 8, D(35, 10, .05)),
  ("She wears cosmetic contact lenses that gently enhance her natural eye colour.", 2, D(35, 10, .05)), ("She wears enhancement-tint contact lenses, barely noticeable.", 2, D(35, 10, .05)), ("She wears lightly tinted contact lenses that make her irises look brighter.", 2, D(35, 10, .05)),
  ("She wears cosmetic contact lenses that make her irises look more defined.", 1.5, D(35, 10, .05)), ("She wears cosmetic circle lenses that make her irises look larger.", 1, D(30, 8, .03)), ("She wears circle lenses that make her irises look larger.", 3, D(30, 8, .03)),
  ("She wears contact lenses that slightly deepen her natural eye colour.", 2, D(40, 12, .1)), ("She wears toric contact lenses, with no glasses.", 3, FLAT), ("She wears multifocal contact lenses, with no glasses.", 2, U(50, 8, .02, 3)),
  ("She wears hard gas-permeable contact lenses.", 1.5, FLAT), ("She wears scleral contact lenses that cover the whole front of her eyes.", .8, FLAT),
  ("She wears glossy theatrical cat-eye contact lenses with slit pupils.", .4, D(35, 10, .02)), ("She wears white theatrical contact lenses.", .2, D(35, 10, .02)),
  ("She wears no glasses; her eyes look clear with contact lenses in.", 5, FLAT)])
CONTACT_EXTRA = ["", ", with a thin lens edge just visible", ", giving her eyes a slightly glossy look", ", her eyes looking bright and unobstructed", ", with no frames on her face", ", with a faint reflection on the lens surface",
  ", with her eyes slightly reddened from wear", ", the lenses almost invisible", ", leaving her whole face open and unframed", ", with eyes that look sharp and clear", ", with a natural, unframed look",
  ", with a faint ring at the edge of the iris", ", and her eyes are slightly moist", ", with a subtle sheen across the pupils"]
MONOCLE = ["She wears a gold-rimmed monocle over her left eye, on a thin chain.", "She wears a monocle over her right eye, held by the muscles around the socket.", "A round silver monocle sits in her left eye.",
  "She has a black-rimmed monocle in her right eye, with a ribbon tucked into her collar.", "She wears a horn-rimmed monocle over one eye.", "A Victorian brass monocle with a short chain hangs from her left eye.",
  "She wears a tinted monocle in her left eye.", "She has a thin wire monocle clipped over her right eye.", "She wears a magnifying monocle that enlarges one eye.", "She wears an engraved gold monocle with a fine chain over her left eye.",
  "Her eyewear is a monocle over one eye."]
EYEPATCH = ["She wears a black fabric eyepatch over her left eye with a thin strap around her head.", "A black leather eyepatch covers her right eye, held by a cord.", "She has a white medical eye patch taped over her left eye.",
  "She wears a gauze eye pad taped over her right eye.", "A dark brown stitched leather eyepatch covers her left eye.", "She wears a clear plastic eye shield over her right eye.",
  "A black satin eyepatch embroidered in gold covers her left eye.", "She wears a plain skin-tone eyepatch over her right eye.", "She has a velvet eyepatch with a jewelled edge over her left eye.",
  "She wears a worn canvas eyepatch over her right eye, with a frayed strap.", "She wears a black pirate-style eyepatch over one eye.", "A soft padded eyepatch with an elastic band covers her left eye, with scarring visible around it."]
NONE_LINES = ["She has clear vision and wears no glasses.", "She wears no glasses at all."]      # kept so the original 'no glasses' option stays represented

def art(s): return "an" if s[0].lower() in "aeiou" else "a"
def pick(R, items, b):
    wt = [x[1] * Kbracket(x[2], b) for x in items]; return R.choices(items, weights=wt, k=1)[0][0]
def glasses_line(R, b):
    r = R.random()
    if r < .07: return R.choice(SP_T).format(s=pick(R, SPECIAL, b))
    if r < .15:
        shape = pick(R, SHAPE, b); colour = pick(R, COLOUR, b)
        return R.choice(RD_T).format(a=art(shape), shape=shape, colour=colour, state=pick(R, STATE, b))
    shape = pick(R, SHAPE, b); mat = pick(R, MATERIAL, b); col = pick(R, COLOUR, b)
    return R.choice(GL_T).format(a=art(shape), shape=shape, material=mat, colour=col, lens=pick(R, LENS, b), state=pick(R, STATE, b))
def sun_line(R, b):
    sh = pick(R, SUN_SHAPE, b); t = pick(R, SUN_TINT, b)
    return R.choice(SUN_T).format(a=art(sh), sshape=sh, tint=t, fcolour=pick(R, COLOUR, b))
def orig_sentence(o):
    if o == 'monocle over one eye': return None
    if o.startswith('no glasses'): return NONE_LINES[0]
    return R_orig(o)
def R_orig(o):
    if 'goggles' in o: return f"She has {o}."
    return f"Her eyewear is {o}."
def build(seed, b, bi=None, shares=None):
    R = random.Random(seed)
    g, s, c = shares
    n_m = round(N * MONO / 100); n_p = round(N * PATCH / 100)
    n_g = round(N * g / 100); n_s = round(N * s / 100); n_c = round(N * c / 100)
    n_none = N - n_m - n_p - n_g - n_s - n_c
    lines = []
    cw = [x[1] * Kbracket(x[2], b) for x in CONTACT]; cnt = allocate(cw, max(n_c, len(CONTACT)))
    for (t, _, _), k in zip(CONTACT, cnt):
        for j in range(k):
            tt = t if j == 0 else t[:-1] + R.choice(CONTACT_EXTRA) + '.'
            lines.append(tt)
    lines = lines[:max(n_c, 0)] if n_c >= len(CONTACT) else lines
    orig = [orig_sentence(o) for o in ORIG]; orig = [o for o in orig if o]
    glass = list(orig); seen = set(glass)
    while len(glass) < n_g:
        for _ in range(30):
            x = glasses_line(R, b)
            if x not in seen: break
        seen.add(x); glass.append(x)
    glass = glass[:max(n_g, len(orig))]
    sun = []; seen = set()
    while len(sun) < n_s:
        for _ in range(30):
            x = sun_line(R, b)
            if x not in seen: break
        seen.add(x); sun.append(x)
    mono = [MONOCLE[i % len(MONOCLE)] for i in range(n_m)]; patch = [EYEPATCH[i % len(EYEPATCH)] for i in range(n_p)]
    none = [NONE_LINES[1]] * min(2, n_none) + [''] * (n_none - min(2, n_none))
    allv = lines + glass + sun + mono + patch + none
    if len(allv) > N: allv = allv[:N] if False else allv
    # trim/pad with blanks so the file is exactly N lines
    while len(allv) > N:
        if '' in allv: allv.remove('')
        else: allv.pop()
    allv += [''] * (N - len(allv))
    R.shuffle(allv); return [pron(x) for x in allv]
def nog(l):    # contact-lens lines must not mention glasses at all (the word primes image models to draw them)
    if 'contact lens' not in l: return l
    l = l.replace(' and no glasses', '').replace(', with no glasses', '').replace('She wears no glasses; her eyes look clear with contact lenses in.', 'Her eyes look clear with contact lenses in.')
    return l
def write(name, lines): lines = [nog(l) for l in lines]; open(os.path.join(WC, name + '.txt'), 'w', encoding='utf8', newline='\n').write('\n'.join(lines) + '\n')
if __name__ == '__main__':
    for bi, b in enumerate(BRACKETS): write(f"{bname(b)}_opt_eyewear", build(500 + bi, b, bi, SHARE[bi]))
    # whole-population file: weighted mix of the brackets' shares
    tot = sum(BRACKET_SHARE); g = sum(SHARE[i][0] * BRACKET_SHARE[i] for i in range(len(BRACKETS))) / tot
    s = sum(SHARE[i][1] * BRACKET_SHARE[i] for i in range(len(BRACKETS))) / tot; c = sum(SHARE[i][2] * BRACKET_SHARE[i] for i in range(len(BRACKETS))) / tot
    R = random.Random(777); mix = []
    cnt = allocate(BRACKET_SHARE, 6000)
    # sample proportionally from the bracket files that were just written
    pool = []
    for b, k in zip(BRACKETS, cnt):
        pool += [(l, k) for l in [x for x in open(os.path.join(WC, bname(b) + '_opt_eyewear.txt'), encoding='utf8').read().split('\n')[:-1]]]
    # pick N lines, weighting each by bracket share / N; keep monocle+eyepatch at exactly 0.5% each by building those separately
    base = [x for x in pool if not any(m in x[0] for m in ('monocle', 'eyepatch', 'eye patch', 'eye pad', 'eye shield'))]
    lines = R.choices([x[0] for x in base], weights=[x[1] for x in base], k=N - 2 * round(N * .005))
    lines += [pron(MONOCLE[i % len(MONOCLE)]) for i in range(round(N * .005))] + [pron(EYEPATCH[i % len(EYEPATCH)]) for i in range(round(N * .005))]
    # guarantee all original options appear at least once
    need = [pron(orig_sentence(o)) for o in ORIG if orig_sentence(o)]
    for i, t in enumerate(need):
        if t not in lines: lines[i] = t
    R.shuffle(lines); write('acc_glasses', lines)
    print('eyewear files written')
