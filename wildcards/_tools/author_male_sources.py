"""One-time authoring of the male SOURCE files (m_*.txt).  Reads the female canonical workspace (for filtered/converted lists) and writes into the target folder.
   python author_male_sources.py <female_canonical_folder> <target_folder>      (the build_all workflow already contains the result - you only need this to regenerate them)"""
import os, sys, re, random, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from male_names_data import NAMES
SRC, OUT = sys.argv[1], sys.argv[2]; os.makedirs(OUT, exist_ok=True)
R = random.Random(404)
def rd(f): return [l.rstrip('\r\n') for l in open(os.path.join(SRC, f + '.txt'), encoding='utf8', errors='replace').read().split('\n')]
def wr(name, lines): open(os.path.join(OUT, 'm_' + name + '.txt'), 'w', encoding='utf8', newline='\n').write('\n'.join(lines) + '\n')
def uniq_counts(f):
    c = collections.OrderedDict()
    for l in rd(f):
        l = l.strip()
        if l: c[l] = c.get(l, 0) + 1
    return c
FEMCODED = re.compile(r"voluptuous|hourglass|pear-shaped|pear shaped|curvy|petite|cellulite|feminine|boyish|mascara|lipstick|bust\b|breast|cleavage|nipple|girlish|dainty|delicate|bra\b", re.I)
def fill(counts, extras, per_extra=4):
    out = []
    kept = [(o, c) for o, c in counts.items() if not FEMCODED.search(o)]
    for o, c in kept: out += [o] * c
    have = {o for o, _ in kept}
    for e in extras:
        if e not in have: out += [e] * per_extra; have.add(e)
    R.shuffle(out); return out
# ---- body descriptors: keep non-female-coded options, add male ones ----
wr('body_ratio', fill(uniq_counts('body_ratio'), ["broad shoulders tapering to a narrow waist (V-taper)","shoulders and hips of equal width in a straight rectangular torso","wide muscular shoulders over a thick solid waist","narrow sloping shoulders with a soft rounded midsection","broad chest narrowing to slim hips","narrow shoulders with a wide lower body","long torso with shorter legs","long legs with a shorter torso","barrel chest above a thick waist","wide rib cage and narrow hips","pronounced shoulder-to-waist ratio with a lean waist","thick neck and heavy trapezius slope over a boxy torso","narrow frame with minimal shoulder width","wide-set shoulders with a heavy belly and slim legs"]))
wr('musc_hips', fill(uniq_counts('musc_hips'), ["narrow slim hips","narrow straight hips with a flat rear","toned athletic hips with firm glutes","heavy soft love handles at the waist","broad sturdy pelvic frame","sagging loose skin at the hips","slender narrow hips under a lean waist","thick solid hips above powerful thighs"]))
wr('musc_legs', fill(uniq_counts('musc_legs'), ["lean sinewy runner's legs","thick heavily muscled quadriceps and calves","skinny narrow legs with prominent knees","heavy thick soft legs with fleshy calves","hairy muscular legs with defined calves","bowed legs with a pronounced outward curve"]))
# ---- accessories ----
J = ["heavy gold chain necklace and rings","simple leather cord necklace","classic steel wristwatch on a metal bracelet","stacked leather and beaded bracelets","silver signet ring","single stud earring","thick silver chain bracelet","dog tags on a ball chain","worn leather-strap watch","rugged titanium sports watch","plain wedding band only","cufflinks and a tie pin","turquoise ring and a leather cuff","gold hoop earring and a thin chain","puka shell necklace","several chunky rings on different fingers","black rubber digital watch","wooden bead bracelet","dive watch with a rotating bezel","pocket watch chain across a vest","silver pendant on a long cord","braided leather wristband","antique gold pinky ring","sleek minimalist smart watch","religious pendant on a fine chain","diamond stud earrings","vintage chronograph watch","friendship bracelets worn on one wrist"]
wr('acc_jewelry', J * 3 + R.sample(J, 16))
S = ["plain brown leather belt with a metal buckle","black leather belt with a silver buckle","woven canvas web belt","braided leather belt","suspenders over a shirt","messenger bag strap across the chest","backpack straps on both shoulders","leather camera strap around the neck","tool belt hung with pouches","utility belt with a holstered multi-tool","ornate rodeo belt buckle","wide leather weightlifting belt","bandolier-style crossbody strap","lanyard with an ID card around the neck","gun-belt style leather rig","rope belt knotted at the waist","military web belt with a brass buckle","ratchet ratcheting belt with no visible holes","fanny pack worn across the chest","guitar strap over one shoulder","duffel bag strap on one shoulder","leather watch strap peeking from a cuff","bike messenger bag with a chest clip","fishing vest straps and clips","climbing harness straps at the waist","sling bag strap across the torso","golf bag strap over the shoulder","leather satchel strap diagonally across the body"]
wr('acc_straps', S * 3 + R.sample(S, 16))
# ---- grooming (replaces the makeup files in male prompts) ----
GROOM = ["a clean skincare finish with a natural matte look","a light concealer on small blemishes","neatly tidied eyebrows","a touch of lip balm","bare skin with no products at all","hair styled with matte clay","hair slicked with shiny pomade","a freshly shaved glossy jaw","beard oil giving the beard a healthy sheen","a light stage powder to reduce shine","subtle tinted moisturizer evening the skin tone","a well-kept barbered look with a crisp neckline","sun-weathered skin with no grooming products","a faint sweat sheen from heat","light cologne-ready polished grooming","sunscreen leaving a faint sheen","a barber-fresh edge-up along the hairline","trimmed nose and ear hair, clean nails, tidy overall grooming","light eyeliner worn for a stage look","dramatic stage makeup with contoured cheekbones","guyliner and dark eyeshadow in a rock-style look","painted black nails","clear nail polish on neat nails","an unkempt, hurried morning look","exhausted, unshaven, uncombed grooming","hair freshly cut with a crisp part","a post-workout flush with damp hair","skin lightly bronzed by the sun","a tidy mustache with waxed tips","a carefully lined-up beard edge","minimal grooming with natural eyebrows and dry lips","oil-slicked skin from a long working day"]
wr('grooming', GROOM * 2 + R.sample(GROOM, 8))
# ---- facial hair: duplicates in the file encode base likelihood ----
FH = [("a clean-shaven smooth jaw",14),("a freshly shaved face with a faint shadow",9),("a clean-shaven face with a defined jawline",8),("a smooth shaved chin and upper lip",5),
 ("light stubble across the jaw",8),("a heavy five o'clock shadow",5),("a rugged three-day stubble",5),("patchy stubble with uneven growth",1.5),("sculpted designer stubble with a clean neckline",2),("gray stubble",1.5),
 ("a thin pencil mustache",0.8),("a thick bushy mustache",1.5),("a classic horseshoe mustache",0.8),("a waxed handlebar mustache",0.5),("a neatly trimmed mustache",2),("a walrus mustache hanging over the lip",0.5),("a wispy sparse mustache",0.8),("a white mustache",0.4),
 ("a short goatee",2),("a full goatee with a connected mustache",2),("a Van Dyke with a pointed chin beard",0.7),("a soul patch under the lower lip",0.8),("a chin strap beard along the jawline",0.6),("a circle beard of connected mustache and goatee",1.2),("a graying goatee",0.6),
 ("a short boxed beard",4),("a closely trimmed short beard",6),("a well-groomed medium beard",5),("a full thick beard",5),("a long full beard reaching the chest",1.2),("a rounded full beard with a shaped cheek line",2),("a patchy sparse beard",1.2),("a scruffy untamed beard",1.5),
 ("a Garibaldi beard with a rounded bottom",0.6),("a neatly sculpted beard with sharp cheek lines",2.5),("an anchor beard tracing the jaw and chin",0.6),("a braided beard",0.2),("mutton-chop sideburns",0.4),("long sideburns with a shaved chin",0.5),
 ("a short salt-and-pepper beard",2),("a full gray beard",1.5),("a full white beard",1),("a trimmed white beard",0.8),("a long white beard",0.3),("a neat salt-and-pepper goatee",0.8),("a salt-and-pepper mustache",0.6)]
lines = []; tot = sum(w for _, w in FH)
for o, w in FH: lines += [o] * max(1, round(w / tot * 1000))
R.shuffle(lines); wr('facial_hair', lines)
# ---- names ----
nm = list(dict.fromkeys(x.replace('_', ' ') for x in NAMES.split())); R.shuffle(nm); wr('names', nm)
# ---- clinical anatomy descriptions (adult; same descriptive register as the female files; no templates reference them) ----
def combos(n, builder):
    out = []; tries = 0
    while len(out) < n and tries < 5000:
        s = builder(); tries += 1
        if s not in out: out.append(s)
    return out
def pecs():
    b = R.choice(["flat and narrow","broad and flat","lightly defined","firmly muscular","heavily muscular with a pronounced upper chest","thick and barrel-shaped","soft and rounded","soft with mild fullness at the chest","narrow and slightly concave","lean with the ribs faintly visible","covered in a soft layer of fat"])
    h = R.choice(["no chest hair","sparse light chest hair","a moderate patch of chest hair","dense dark chest hair","chest hair going gray","a thin trail of hair along the sternum","a full covering of curly chest hair"])
    f = R.choice(["visible collarbones","a defined groove along the sternum","smooth even skin","scattered freckles across the skin","faint stretch marks at the sides","a few visible veins across the upper chest","a faint old scar line","a small mole near the sternum"])
    return f"His chest is {b}, with {h} and {f}."
def butt():
    b = R.choice(["flat and narrow","small and firm","round and muscular","compact and athletic","broad and soft","low-set and soft","high and tight","square and solid","slightly sagging","flat with little definition","wide and heavy"])
    s = R.choice(["smooth skin","a light dusting of hair","faint dimples at the sides","a few stretch marks","a slightly darker skin tone than the thighs","visible muscle definition when standing","soft skin that moves slightly with the body"])
    return f"His buttocks are {b}, with {s}."
def nip():
    sz = R.choice(["small","medium-sized","large","wide"]); c = R.choice(["pale pink","light brown","medium brown","dark brown","deep brown-black","tan"])
    sh = R.choice(["flat against the chest","slightly raised","round","oval","softly puffy"]); hh = R.choice(["bare","with a few fine hairs around the areola","with coarse dark hairs around the areola"])
    return f"His nipples are {sz} and {c}, {sh}, {hh}."
def gen():
    sz = R.choice(["small","average-sized","above-average","large"]); st = R.choice(["when flaccid"]); circ = R.choice(["circumcised with a smooth exposed glans","uncircumcised with the foreskin covering the glans","uncircumcised with a partly retracted foreskin","circumcised with a visible scar line"])
    sk = R.choice(["even coloring along the shaft","shaft skin slightly darker than the surrounding skin","a few faint veins along the shaft","a pronounced vein pattern along the shaft"])
    sc = R.choice(["a tight compact scrotum","a relaxed hanging scrotum","a lightly haired scrotum","a smooth shaved scrotum","a heavily wrinkled scrotum"]); ph = R.choice(["groomed trimmed pubic hair","a natural untrimmed pubic area","a fully shaved pubic area","a neat narrow strip of pubic hair"])
    return f"His penis is {sz} {st}, {circ}, with {sk}, below {ph}, with {sc}."
wr('body_pecs', combos(50, pecs)); wr('body_buttocks', combos(50, butt)); wr('body_nipples', combos(50, nip)); wr('body_genitals', combos(40, gen))
wr('pubichair', ["a fully shaved pubic area","a neatly trimmed natural pubic patch","a thick untrimmed natural bush","a narrow groomed strip","a closely clipped even covering","a lightly trimmed triangle","a sparse natural covering","dense dark curly pubic hair","fine light pubic hair","graying pubic hair","a shaved pubic area with light regrowth","a groomed pubic area with a trimmed line along the hip crease"] * 2)
wr('body_chesthair', ["a completely smooth hairless chest","a faint scattering of fine chest hair","a moderate natural covering of chest hair","thick dark chest hair spreading to the shoulders","a thin vertical line of hair along the sternum","gray-flecked chest hair","a trimmed neat chest hair pattern","a dense curly mat of chest hair","patchy uneven chest hair","white chest hair on an older chest","a freshly shaved chest with light stubble","fine blond chest hair that is barely visible"] * 2)
# ---- converted originals ----
def pro(t):
    for a, b in [(r'\bshe she\b', 'he'), (r'\bShe\b', 'He'), (r'\bshe\b', 'he'), (r'\bHer\b', 'His'), (r'\bher\b', 'his'), (r'\bherself\b', 'himself'), (r'\bwoman\b', 'man'), (r'\bsisters\b', 'brothers'), (r'\bsister\b', 'brother')]: t = re.sub(a, b, t)
    return t
hc = [pro(l.strip()) for l in rd('health_conditions')]
hc = [l.replace('Turner Syndrome and has a short stature, a wide neck with visible lateral skin folds (webbed neck), a broad chest structure, and a low hairline at the back of the neck', 'Klinefelter Syndrome and has a tall slender frame with long legs, sparse facial hair, mildly enlarged breast tissue, and a narrower shoulder structure') for l in hc]
wr('health_conditions', hc)
wr('extrasinphoto', [pro(l.strip()) if l.strip() else '' for l in rd('extrasinphoto')])
def keep(f, out=None):
    L = rd(f); k = [pro(l) for l in L if not FEMCODED.search(l) and not re.search(r'\b(skirt|dress|heels)\b', l, re.I)]
    wr(out or f, k)
def keep2(f, rx):
    L = rd(f); k = [pro(l) for l in L if not re.search(rx, l, re.I)]; wr(f, k); print('  ', f, len(L), '->', len(k))
keep2('eye_lash', r'mascara|lash extensions'); keep2('style_photographers_portrait', r'feminine|women|woman|girl|lipstick|bridal')
keep('heightweightdeform10000'); keep('weights_all'); keep('heights_all'); keep('poses_extended')
h = [float(l) for l in rd('height') if l.strip()]; w = [float(l) for l in rd('weightkg') if l.strip()]
wr('height', [str(round(v + 13) if v >= 140 else round(v * 1.04)) for v in h]); wr('weightkg', [str(round(v * 1.17)) for v in w])
# ---- the user's own prompt templates, converted ----
def man_prompt(t):
    t = pro(t); t = re.sub(r'(?<=__)she\b', 'he', t)
    t = t.replace('clothing_full_female', 'clothing_full')
    t = t.replace('__hair_baby__, ', '').replace('__hair_shine__, and __hair_motion__', '__hair_shine__, and __hair_motion__ with __facial_hair__ on his face')
    t = re.sub(r'Enhanced by __make_base__, __make_hlite__, __make_blush__, __make_eyes__, and __make_lips__, he wears', 'Groomed with __grooming__, he wears', t)
    t = re.sub(r'<lora:[^>]*>,?', '', t)          # the user's LoRA tag is not carried over to the male templates
    return t
for src, dst in [('WOMANprompt', 'MANprompt'), ('character_female_basic', 'character_male_basic')]:
    wr(dst, [man_prompt(l) for l in rd(src)])
import male_outfits as _mo
wr('clothing_full', _mo.clothing_full_lines(2500))
print('male sources written to', OUT, len(os.listdir(OUT)), 'files')
