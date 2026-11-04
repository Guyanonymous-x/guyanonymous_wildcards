"""Age- and body-conditioned clothing + the completely random clothing mix.
   Writes (into the wildcards folder):
     age<lo>_<hi>_clothing_<archetype>.txt      64 files x 1000 outfit lines  (age bracket x body archetype)
     age<lo>_<hi>_prompt_char_physical_<arch>   character section wired to that archetype
     age<lo>_<hi>_prompt_master_<arch>          full prompt, age/body-conditioned clothing
     age<lo>_<hi>_prompt_master_rc_<arch>       full prompt, RANDOM clothing (not tied to age or body)
     age<lo>_<hi>_prompt_master / _rc           pickers (archetype by share)
     clothing_random_mix, prompt_wardrobe_random, prompt_master_random_clothing, prompt_master_by_age_random_clothing
   Usage: python clothing_build.py [wildcards_folder]"""
import os, sys, re, random, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from paths import wc_dir
from gender import IS_M, pron
from wcbuild import allocate
from age_model import *
from body_model import ARCH, SHARE
WC = wc_dir(); N = 1000
def rl(p): return [l.rstrip('\r\n') for l in open(p, encoding='utf8', errors='replace').read().split('\n')]
def write(name, lines, seed=None):
    if seed is not None: random.Random(seed).shuffle(lines)
    open(os.path.join(WC, name + '.txt'), 'w', encoding='utf8', newline='\n').write('\n'.join(lines) + '\n')
def art(s): return ("an " if s[0].lower() in "aeiou" else "a ") + s
# ---- body-type modifiers on garment tags (multiplicative, deliberately mild except for frailty) ----
MOD = {
 'thin':  {'layered':1.3,'loose':1.2,'crop':0.9,'tight':0.8,'athletic':0.7},
 'slim':  {'crop':1.2,'tight':1.1},
 'avg':   {},
 'athl':  {'athletic':2.0,'tank':1.4,'crop':1.2,'tight':1.2,'loose':0.8,'structured':0.9},
 'curvy': {'wrap':1.4,'aline':1.3,'structured':1.1,'highwaist':1.2,'crop':0.6,'tight':0.8,'mini':0.7},
 'heavy': {'loose':1.3,'aline':1.3,'wrap':1.3,'layered':1.3,'stretch':1.3,'crop':0.4,'tight':0.5,'mini':0.5,'athletic':0.7},
 'musc':  {'athletic':1.7,'tank':1.4,'crop':1.1,'loose':0.9},
 'vheavy': {'loose':1.5,'aline':1.4,'wrap':1.3,'layered':1.3,'stretch':1.5,'comfy':1.6,'crop':0.15,'tight':0.25,'mini':0.25,'athletic':0.4,'heels':0.3},
 'frail': {'layered':1.8,'sleeved':1.6,'loose':1.4,'comfy':2.5,'crop':0.1,'tight':0.2,'heels':0.1,'mini':0.2,'athletic':0.4,'highwaist':1.2},
}
def bmod(arch, tags):
    f = 1.0
    for t in tags.split():
        f *= MOD[arch].get(t, 1.0)
    return f
# ---- colours: (family weight, age spec, shades) ----
COL = [(17,FLAT,["white","bright white","off-white","soft white","cream-white","faded white","slightly yellowed white","crisp white"]),
 (16,FLAT,["black","washed black","faded black","jet black"]),(10,FLAT,["heather grey","light grey","charcoal grey","mid grey","slate grey","marled grey","dove grey"]),
 (7,U(45,25,.6,1.4),["navy","dark navy","midnight blue","ink blue"]),(7,FLAT,["sky blue","powder blue","cobalt blue","royal blue","steel blue","faded blue"]),
 (6,U(45,25,.6,1.4),["beige","sand","oatmeal","cream","ecru","stone","camel"]),(5,FLAT,["red","brick red","tomato red","cherry red","faded red"]),
 (3,U(45,25,.5,1.2),["blush pink","dusty rose","soft pink","faded pink","salmon pink"]),(2.5,D(35,10,.1),["hot pink","fuchsia","bubblegum pink"]),
 (5,FLAT,["forest green","sage green","olive green","emerald green","mint green","khaki green","bottle green"]),(3.5,U(45,25,.6,1.3),["chocolate brown","tan","caramel","rust brown","taupe","mocha"]),
 (2.5,D(45,15,.4),["mustard yellow","butter yellow","pale yellow","golden yellow"]),(2.5,U(40,25,.6,1.3),["burgundy","wine red","maroon","plum"]),(2,FLAT,["lavender","lilac","violet","deep purple","mauve"]),
 (1.5,D(40,15,.4),["burnt orange","terracotta","coral","peach"]),(1.5,FLAT,["teal","turquoise","aqua","petrol blue"]),(0.6,D(35,8,.03),["neon green","electric blue","metallic silver","metallic gold","holographic silver"])]
PATTERN = [("",74,FLAT),("striped ",8,FLAT),("floral-print ",4,U(45,20,.4,1.8)),("plaid ",2.5,FLAT),("polka-dot ",1.2,U(40,25,.6,1.4)),("tie-dye ",0.5,D(35,8,.03)),("animal-print ",0.7,FLAT),("gingham ",0.9,FLAT),("embroidered ",1.0,U(55,15,.2,2.0)),("lace-trimmed ",1.0,U(50,20,.3,1.4)),("textured ",1.5,FLAT)]
FIT = [("",30,FLAT,''),("relaxed-fit ",25,FLAT,''),("fitted ",20,FLAT,'tight'),("loose ",12,U(55,25,.7,1.3),'loose'),("oversized ",8,D(50,15,.3),'loose'),("cropped ",5,D(35,8,.05),'crop')]
# ---- catalogues: (name, base weight, age spec, tags[, fabrics]) ----
TOPS = [("crew-neck t-shirt",20,FLAT,'',["cotton","soft cotton","jersey cotton","thin cotton"]),("v-neck t-shirt",5,FLAT,'',["cotton","jersey"]),("long-sleeve tee",5,FLAT,'sleeved',["cotton","ribbed cotton"]),
 ("tank top",5,FLAT,'tank',["cotton","ribbed cotton","jersey"]),("button-up shirt",6,FLAT,'structured sleeved',["cotton poplin","oxford cotton","linen","chambray"]),("blouse",7,U(40,25,.5,1.5),'sleeved',["chiffon","crepe","satin","cotton voile","viscose"]),
 ("sweater",6,FLAT,'layered sleeved',["wool","chunky-knit","fine-knit","cashmere-blend","cotton-knit"]),("cardigan",3,U(48,14,.3,2.2),'layered sleeved',["wool","fine-knit","cotton-knit"]),("hoodie",5,D(42,12,.2),'loose sleeved',["fleece","cotton fleece","heavy cotton"]),
 ("sweatshirt",4,D(55,15,.3),'loose sleeved',["fleece","cotton fleece"]),("polo shirt",2,U(50,20,.5,1.3),'',["piqué cotton","cotton"]),("camisole",2,P(30,20,.4),'tight',["satin","silk","cotton"]),
 ("crop top",2,D(35,8,.05),'crop tight',["cotton","ribbed","jersey"]),("turtleneck",2.5,P(45,20,.4),'layered sleeved',["merino wool","ribbed-knit","fine-knit"]),("henley top",1.5,FLAT,'sleeved',["waffle-knit cotton","cotton"]),
 ("tunic top",2,U(48,15,.3,1.8),'loose',["cotton","linen","viscose"]),("off-shoulder top",0.7,D(35,10,.1),'crop',["cotton","knit","chiffon"]),("bodysuit",0.7,D(35,10,.05),'tight',["stretch cotton","ribbed jersey"]),
 ("graphic tee",3,D(38,10,.1),'',["cotton","soft cotton"]),("linen shirt",1.5,U(40,20,.5,1.3),'loose',["linen"]),("embroidered tunic",1.0,U(55,12,.1,2.5),'loose',["cotton","linen"]),
 ("twin-set cardigan and shell top",0.6,U(62,10,.01,4),'layered sleeved',["wool","fine-knit"]),("sleeveless shell top",1.5,U(45,15,.2,1.6),'',["silk","cotton","crepe"]),("knit vest over a collared shirt",1,U(55,12,.1,2),'layered',["wool","cotton-knit"]),
 ("oversized sweater",3,D(50,15,.3),'loose layered sleeved',["chunky-knit","wool","cotton-knit"]),("cable-knit sweater",2,U(40,25,.5,1.4),'layered sleeved',["wool","cotton"]),("wrap top",1.5,P(42,18,.5),'wrap',["jersey","crepe"]),("peplum top",0.8,P(35,15,.3),'structured',["crepe","satin"])]
JEAN_WASH = [("mid-wash",30,FLAT),("light-wash",22,D(50,18,.4)),("dark indigo",22,U(40,25,.6,1.3)),("faded blue",10,FLAT),("distressed light-wash",6,D(38,10,.08)),("black",6,FLAT),("white",2,D(45,18,.3)),("grey",2,FLAT)]
JEAN_CUT = [("straight-leg",26,FLAT,''),("skinny",20,D(40,12,.15),'tight'),("wide-leg",14,D(55,15,.4),'loose'),("bootcut",6,U(40,15,.3,1.3),''),("mom",12,D(40,10,.1),'highwaist'),("boyfriend",8,D(40,10,.2),'loose'),("high-waisted",10,FLAT,'highwaist'),("low-rise",4,D(30,8,.03),'tight crop'),("relaxed tapered",3,U(45,20,.4,1.3),'loose')]
BOTTOMS = [("jeans",24,FLAT,''),("leggings",9,D(60,20,.5),'tight stretch'),("chinos",4,FLAT,''),("tailored trousers",3,P(48,20,.4),'structured'),("wide-leg trousers",3,FLAT,'loose'),("cargo pants",2.5,D(45,12,.3),'loose'),
 ("joggers",5,D(50,15,.3),'loose stretch'),("sweatpants",2,FLAT,'loose'),("denim shorts",5,D(55,15,.2),'short'),("cotton shorts",3,D(55,15,.3),'short'),("midi skirt",4,FLAT,'aline'),("mini skirt",2.5,D(33,8,.04),'mini short'),
 ("maxi skirt",2.5,FLAT,'loose'),("pencil skirt",1,P(40,15,.3),'tight structured'),("leather trousers",0.3,D(40,15,.1),'tight'),("elastic-waist trousers",2,U(65,10,.02,5),'loose comfy'),("pull-on slacks",1.5,U(60,12,.02,4),'loose comfy stretch'),
 ("capri pants",1.5,U(50,14,.3,1.8),''),("wide-leg linen pants",1.5,U(45,18,.4,1.4),'loose'),("denim skirt",1.5,D(45,15,.3),'aline'),("pleated skirt",2,D(40,15,.3),'aline'),("culottes",1,U(45,15,.3,1.5),'loose'),("paperbag trousers",1,P(35,15,.3),'highwaist')]
DRESSES = [("sundress",6,FLAT,'loose'),("shirt dress",3,U(40,20,.5,1.3),''),("wrap dress",3,P(42,18,.5),'wrap'),("maxi dress",5,FLAT,'loose'),("midi dress",5,FLAT,'aline'),("t-shirt dress",3,D(45,18,.3),'loose'),("slip dress",1.5,D(35,10,.1),'tight'),
 ("sweater dress",2,FLAT,'layered sleeved'),("denim dress",1,D(42,14,.3),''),("little black dress",2,P(35,20,.4),'structured'),("pinafore dress",1,D(40,12,.2),'aline'),("shift dress",2,U(45,15,.3,1.4),'structured'),("bodycon dress",1.5,D(34,8,.05),'tight'),
 ("kaftan",1,U(50,18,.3,1.6),'loose'),("tea dress",1,U(55,15,.2,1.6),'aline'),("house dress",0.8,U(72,8,.01,6),'loose comfy'),("knit midi dress",1,U(45,20,.3,1.4),'aline sleeved'),("skater dress",1.5,D(36,10,.1),'aline')]
OUTER = [("denim jacket",8,D(55,20,.3),''),("puffer jacket",9,FLAT,'layered'),("wool coat",6,U(45,20,.4,1.5),'layered'),("trench coat",5,FLAT,'layered'),("blazer",6,P(45,20,.4),'structured'),("leather jacket",4,D(52,16,.3),''),
 ("parka",5,FLAT,'layered'),("windbreaker",4,FLAT,''),("fleece jacket",5,U(40,25,.6,1.3),'layered'),("rain jacket",5,FLAT,''),("bomber jacket",3,D(40,12,.1),''),("cardigan",5,U(48,14,.3,2.2),'layered'),("quilted jacket",3,U(50,20,.4,1.5),'layered'),
 ("shawl",2,U(60,12,.05,3),'layered'),("duster coat",1,FLAT,'layered'),("poncho",0.8,U(50,20,.3,1.4),'layered'),("long lightweight cardigan",2,U(48,15,.3,2),'layered'),("quilted vest",1.5,U(55,14,.2,1.8),'layered')]
SHOES = [("white sneakers",16,FLAT,'athletic'),("black sneakers",9,FLAT,'athletic'),("canvas sneakers",7,D(50,18,.3),''),("running shoes",8,FLAT,'athletic'),("leather ankle boots",8,FLAT,''),("flat sandals",8,FLAT,''),("ballet flats",6,FLAT,''),
 ("loafers",4,FLAT,''),("black leather boots",4,FLAT,''),("flip-flops",4,D(45,15,.3),''),("sports sandals",2,FLAT,'athletic'),("rain boots",1.5,FLAT,''),("hiking boots",1.5,FLAT,'athletic'),("platform sneakers",2,D(30,8,.05),''),
 ("slip-on shoes",3,U(40,25,.6,1.4),'comfy'),("mules",1.5,D(50,18,.3),''),("comfortable walking shoes",2,U(62,10,.03,4.5),'comfy'),("orthopedic-style supportive shoes",0.7,U(78,8,.01,8),'comfy'),("cushioned sneakers",3,U(55,15,.3,1.8),'comfy'),("wedge sandals",1.5,U(40,20,.4,1.3),'')]
SHOES_DRESS = [("white sneakers",14,FLAT,'athletic'),("flat sandals",14,FLAT,''),("ballet flats",10,FLAT,''),("leather ankle boots",9,FLAT,''),("block-heel sandals",8,D(50,15,.2),'heels'),("low heels",7,FLAT,'heels'),("high heels",4,D(38,10,.05),'heels'),
 ("loafers",5,FLAT,''),("espadrilles",4,FLAT,''),("black sneakers",5,FLAT,'athletic'),("mules",3,D(50,18,.3),''),("platform sneakers",3,D(30,8,.05),''),("knee-high boots",3,FLAT,''),("comfortable low-heel shoes",2,U(60,12,.03,4),'comfy'),("wedge sandals",2,U(40,20,.4,1.3),'')]
ACTIVE = [("a matching grey athletic set of leggings and sports top",3),("a black sports bra with high-waisted yoga leggings",3),("loose running shorts and a technical tee",1.5),("a navy tracksuit with white stripes",1.5),("cycling shorts with a loose tee",1),("a fitted sleeveless gym top with black training tights",1.5),("a comfortable velour tracksuit",1),("a lightweight zip-up training jacket over a tank top and leggings",1.5)]
WORK = ["a tailored two-piece trouser suit with a crisp blouse","a knee-length pencil skirt suit with a silk blouse","a fitted blazer over a shell top and tailored trousers","a smart shirt dress with a belt and a structured blazer","a pleated midi skirt with a tucked-in blouse and a cardigan","a collared shirt under a knit vest with chinos"]
SPECIAL = [("a satin evening gown",.5,P(40,20,.5)),("a sequined cocktail dress",.5,D(42,15,.2)),("a black tie formal dress",.2,FLAT),("a one-piece swimsuit",1.2,D(45,20,.4)),("a two-piece bikini",1.0,D(40,15,.2)),("a sarong over a swimsuit",.3,FLAT),
 ("a silk kimono-style robe",.3,FLAT),("a traditional-style wrap blouse and long skirt",.5,FLAT),("denim overalls over a striped tee",.8,D(45,15,.2)),("a jumpsuit",1.5,FLAT),("boiler-suit style coveralls",.4,D(45,15,.2)),("a sequined top with black trousers",.4,FLAT),
 ("a formal two-piece skirt suit with a hat for a special occasion",.5,U(55,15,.05,2.5)),("a lace-trimmed evening dress with a matching jacket",.5,U(55,15,.05,2.5))]
TYPES = [('tb',57,FLAT),('dress',20,FLAT),('active',8,D(52,16,.2)),('work',5,P(42,16,.3)),('special',4,P(36,20,.5))]
TYPE_MOD = {'athl':{'active':2.0},'musc':{'active':1.8},'frail':{'active':0.25,'special':1.2},'heavy':{'dress':1.1},'thin':{}}
OUT_PROB = 0.33
def kb(spec, b): return Kbracket(spec, b)
def pick(R, items, b, arch, wi=1, si=2, ti=3):
    w = [it[wi] * kb(it[si], b) * (bmod(arch, it[ti]) if len(it) > ti else 1.0) for it in items]
    return R.choices(items, weights=w, k=1)[0]
def colour(R, b):
    fam = R.choices(COL, weights=[c[0] * kb(c[1], b) for c in COL], k=1)[0]; return R.choice(fam[2])
def make_top(R, b, a):
    t = pick(R, TOPS, b, a); name, fabs = t[0], t[4]
    pat = R.choices(PATTERN, weights=[p[1] * kb(p[2], b) for p in PATTERN], k=1)[0][0]
    fit = R.choices(FIT, weights=[f[1] * kb(f[2], b) * bmod(a, f[3]) for f in FIT], k=1)[0][0]
    c = colour(R, b); fab = R.choice(fabs)
    if name == 'graphic tee': return f"{fit}{c} {fab} graphic tee with a small print"
    return f"{fit}{c} {pat}{fab} {name}"
def make_bottom(R, b, a):
    it = pick(R, BOTTOMS, b, a); name = it[0]
    if name == "jeans":
        wash = R.choices(JEAN_WASH, weights=[x[1] * kb(x[2], b) for x in JEAN_WASH], k=1)[0][0]
        cut = R.choices(JEAN_CUT, weights=[x[1] * kb(x[2], b) * bmod(a, x[3]) for x in JEAN_CUT], k=1)[0][0]
        return f"{wash} {cut} jeans"
    if name == "denim shorts": return f"{R.choice(['light-wash','mid-wash','white','black','faded blue'])} {R.choice(['cut-off ','high-waisted ','bermuda ',''])}denim shorts".replace("  ", " ")
    if name == "denim skirt": return f"{R.choice(['light-wash','mid-wash','dark indigo'])} denim skirt"
    if name == "leggings": return f"{R.choice(['black','black','black','grey','dark navy','charcoal'])} leggings"
    if name == "leather trousers": return "black leather trousers"
    return f"{colour(R, b)} {name}"
def make_dress(R, b, a):
    d = pick(R, DRESSES, b, a)[0]
    if d == "little black dress": return d
    if d == "denim dress": return f"{R.choice(['light-wash', 'mid-wash'])} denim dress"
    pat = R.choices(PATTERN, weights=[p[1] * kb(p[2], b) for p in PATTERN], k=1)[0][0]
    return f"{colour(R, b)} {pat}{d}"
def make_outer(R, b, a):
    o = pick(R, OUTER, b, a)[0]
    if o == "denim jacket": return f"{R.choice(['light-wash','mid-wash','black','faded blue'])} denim jacket"
    if o == "leather jacket": return f"{R.choice(['black','black','brown','tan'])} leather jacket"
    if o in ("trench coat","wool coat","duster coat","parka"): return f"{R.choice(['beige','camel','black','navy','olive green','charcoal grey','tan','cream'])} {o}"
    return f"{colour(R, b)} {o}"
def outfit(R, b, a):
    tw = [t[1] * kb(t[2], b) * TYPE_MOD.get(a, {}).get(t[0], 1.0) for t in TYPES]; kind = R.choices(TYPES, weights=tw, k=1)[0][0]
    out_p = min(0.9, OUT_PROB * kb(U(50, 25, .7, 1.5), b) * bmod(a, 'layered') ** 0.5)
    if kind == 'tb':
        s = f"{art(make_top(R, b, a))} with {make_bottom(R, b, a)}"; shoe = pick(R, SHOES, b, a)[0]
        if R.random() < out_p: s += f" under {art(make_outer(R, b, a))}"
    elif kind == 'dress':
        s = art(make_dress(R, b, a)); shoe = pick(R, SHOES_DRESS, b, a)[0]
        if R.random() < out_p * 0.9: s += f" with {art(make_outer(R, b, a))}"
    elif kind == 'active':
        s = R.choices(ACTIVE, weights=[x[1] for x in ACTIVE], k=1)[0][0]; shoe = R.choice(["white running shoes", "black training shoes", "grey sneakers"] if a != 'frail' else ["comfortable walking shoes", "cushioned sneakers"])
    elif kind == 'work':
        s = R.choice(WORK); shoe = R.choice(["low heels", "loafers", "ballet flats", "leather ankle boots"] if a != 'frail' else ["comfortable low-heel shoes", "loafers", "ballet flats"])
    else:
        sp = R.choices(SPECIAL, weights=[x[1] * kb(x[2], b) for x in SPECIAL], k=1)[0][0]; s = sp; shoe = pick(R, SHOES_DRESS, b, a)[0]
        if any(k in sp for k in ("bikini", "swimsuit", "sarong")): return s
    return s + (f" and {shoe}" if R.random() < 0.9 else "")
# ---- the stylized pool (YOUR clothing_full list), weighted by keyword age/body fit ----
YOUNGW = {'mini':-1.2,'micro':-2,'crop':-1,'cheer':-1.5,'school':-1.5,'sailor':-1.2,'bikini':-0.8,'festival':-1.5,'neon':-1.5,'holographic':-1.5,'rave':-2,'idol':-1.5,'lolita':-1.5,'cute':-1,'kawaii':-1.5,'magical':-1.5,'playful':-0.5,'denim shorts':-1,'tube top':-1.5,'streetwear':-1,'graffiti':-1.5}
OLDW = {'elegant':0.8,'shawl':2,'pantsuit':2,'modest':1.5,'long-sleeved':1,'tweed':2,'brooch':1.5,'cardigan':1,'pearl':1,'tailored':0.5,'sophisticated':0.7,'classic':0.7,'traditional':0.6,'kimono':0.5,'sari':0.8,'gown':0.6}
TIGHTW = ('bodycon','crop','micro','bikini','corset','lingerie','tight','figure-hugging','mini','sheer','strapless')
def style_score(l):
    t = l.lower(); s = 0.0
    for d in (YOUNGW, OLDW):
        for k, v in d.items():
            if k in t: s += v
    return max(-3, min(3, s))
STYLE_SHARE = [8, 7, 5, 4, 3, 2, 2, 1, 1]
POOL_EXCLUDE = r"^only\b|^no clothing|^nude|pussy|vagina|nipple|breasts|^body paint|g-string|thong|^a (large )?towel|washcloth|bedsheet|^ripped and torn cloth|bad home-made|reflection"
RANDOM_MIX = ["__clothing_everyday__"] * 20 + ["__clothing_full__"] * 30 + ["__outfit_cosplay__"] * 12 + ["__outfit_casual_mixed__"] * 8 + ["__outfit_formal_mixed__"] * 7 + ["__outfit_uniform_mixed__"] * 6 + ["__outfit_sexy_mixed__"] * 7 + ["__outfit_see_through__"] * 4 + ["__outfit_color__ __outfit_lingerie__"] * 3 + ["__outfit_color__ __outfit_material__ __outfit_dress_style__"] * 3
if IS_M:      # men: replace the catalogues, outfit builder, keyword weights, pool filter and random mix with the male versions
    from clothing_cat_m import *
raw = [l for l in rl(os.path.join(WC, 'clothing_full.txt')) if l.strip()]
pool = []
for l in raw:
    l = re.sub(r'^\d+::', '', l.strip()).strip()
    if not l or re.search(POOL_EXCLUDE, l.lower()): continue
    pool.append((l, spec_from_s(style_score(l)), any(k in l.lower() for k in TIGHTW)))
if __name__ == '__main__':
    for bi, b in enumerate(BRACKETS):
        for ai, a in enumerate(ARCH):
            R = random.Random(bi * 100 + ai); n_sty = round(N * STYLE_SHARE[bi] / 100)
            lines = [outfit(R, b, a) for _ in range(N - n_sty)]
            w = [kb(sp, b) * ((bmod(a, 'tight crop mini') if tight else 1.0)) for _, sp, tight in pool]
            lines += R.choices([p[0] for p in pool], weights=w, k=n_sty)
            write(f"{bname(b)}_clothing_{a}", lines, seed=bi * 100 + ai)
    # ---- templates ----
    WARD = ["She is wearing {C}. __acc_glasses__{ Her jewelry includes __acc_jewelry__.||}{ On her head she has __acc_hats__.||||}{ She carries __acc_props__.|||}",
            "Her outfit is {C}.{ Her jewelry includes __acc_jewelry__.||} __acc_glasses__{ Around her waist she has __acc_straps__.||||}",
            "She is dressed in {C}.{ On her head she has __acc_hats__.||||}{ She has __acc_jewelry__.||} __acc_glasses__"]
    WARD = [pron(w) for w in WARD]; EYE = pron(' __acc_glasses__')
    write('clothing_random_mix', RANDOM_MIX, seed=1)
    write('prompt_wardrobe_random', [w.replace('{C}', '__clothing_random_mix__') for w in WARD])
    base = {'1': "__prompt_style__ {PHYS} {WARD} {POSE} __prompt_setting__ __prompt_camera_light__", '2': "{PHYS} {WARD} {POSE} __prompt_setting__ __prompt_camera_light__ __prompt_style__", '3': "__prompt_setting__ {PHYS} {WARD} {POSE} __prompt_camera_light__ __prompt_style__"}
    write('prompt_master_random_clothing', [v.replace('{PHYS}', '__prompt_char_physical__').replace('{WARD}', '__prompt_wardrobe_random__').replace('{POSE}', '__prompt_pose_expression__') for v in base.values()])
    pick_rc = []
    for bi, b in enumerate(BRACKETS):
        p = bname(b)
        phys_src = [l for l in rl(os.path.join(WC, f"{p}_prompt_char_physical.txt")) if l.strip()]
        cnt = collections.Counter(phys_src); tot = sum(cnt.values()); keys = list(cnt)
        ncount = allocate([cnt[k] for k in keys], 240)            # compress 1000 repeated lines to ~240 keeping every distinct variant
        for a in ARCH:
            plines = []
            for k, c in zip(keys, ncount): plines += [k.replace(f"__{p}_prompt_char_body__", f"__bt_{a}_{p}_prompt_char_body__")] * c
            write(f"{p}_prompt_char_physical_{a}", plines, seed=bi + 7)
            ml, mr = [], []
            for w in WARD:
                for v in base.values():
                    ph = f"__{p}_prompt_char_physical_{a}__"; po = f"__{p}_prompt_pose_expression_{a}__"
                    ward = w.replace('{C}', f"__{p}_clothing_{a}__").replace(EYE, f" __{p}_opt_eyewear__")
                    for acc in ('hats', 'jewelry', 'props'): ward = ward.replace(f"__acc_{acc}__", f"__{p}_acc_{acc}__")
                    ward += f" __{p}_aids_{a}__"
                    st = lambda s_: s_.replace('__prompt_setting__', f"__{p}_prompt_setting_{a}__")
                    ml.append(st(v.replace('{PHYS}', ph).replace('{WARD}', ward).replace('{POSE}', po)))
                    mr.append(st(v.replace('{PHYS}', ph).replace('{WARD}', "__prompt_wardrobe_random__").replace('{POSE}', po)))
            write(f"{p}_prompt_master_{a}", ml); write(f"{p}_prompt_master_rc_{a}", mr)
        cnt2 = allocate(SHARE[b], 1000); pm, pr = [], []
        for a, c in zip(ARCH, cnt2): pm += [f"__{p}_prompt_master_{a}__"] * c; pr += [f"__{p}_prompt_master_rc_{a}__"] * c
        write(f"{p}_prompt_master", pm, seed=3); write(f"{p}_prompt_master_rc", pr, seed=4)
    share = allocate(BRACKET_SHARE, 1000)
    write('prompt_master_by_age', [f"__{bname(b)}_prompt_master__" for b, c in zip(BRACKETS, share) for _ in range(c)], seed=9)
    write('prompt_master_by_age_random_clothing', [f"__{bname(b)}_prompt_master_rc__" for b, c in zip(BRACKETS, share) for _ in range(c)], seed=10)
    print('clothing layer written to', WC)
