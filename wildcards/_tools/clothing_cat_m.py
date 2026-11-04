"""MALE catalogues for the age/body-conditioned clothing layer (imported by clothing_build.py when WC_GENDER=m; replaces the female names)."""
import random
from age_model import *
def art(s): return ("an " if s[0].lower() in "aeiou" else "a ") + s
MOD = {
 'thin':  {'layered':1.3,'loose':1.2,'tight':0.8,'athletic':0.7},
 'slim':  {'tight':1.1},
 'avg':   {},
 'athl':  {'athletic':2.0,'tank':1.4,'tight':1.2,'loose':0.8,'structured':0.9},
 'curvy': {'loose':1.2,'structured':1.1,'tight':0.8,'short':0.9},
 'heavy': {'loose':1.3,'layered':1.2,'stretch':1.3,'tight':0.5,'short':0.7,'athletic':0.7},
 'musc':  {'athletic':1.7,'tank':1.5,'tight':1.3,'loose':0.8},
 'vheavy': {'loose':1.5,'layered':1.3,'stretch':1.5,'comfy':1.6,'tight':0.25,'short':0.4,'athletic':0.4},
 'frail': {'layered':1.8,'sleeved':1.6,'loose':1.4,'comfy':2.5,'tight':0.2,'short':0.3,'athletic':0.4},
}
def bmod(arch, tags):
    f = 1.0
    for t in tags.split(): f *= MOD[arch].get(t, 1.0)
    return f
def kb(spec, b): return 1.0 if b is None else Kbracket(spec, b)
def pick(R, items, b, arch, wi=1, si=2, ti=3):
    w = [it[wi] * kb(it[si], b) * (bmod(arch, it[ti]) if len(it) > ti else 1.0) for it in items]
    return R.choices(items, weights=w, k=1)[0]
COL = [(17,FLAT,["white","bright white","off-white","soft white","cream-white","faded white","crisp white"]),(16,FLAT,["black","washed black","faded black","jet black"]),(10,FLAT,["heather grey","light grey","charcoal grey","mid grey","slate grey","marled grey"]),
 (8,U(45,25,.6,1.4),["navy","dark navy","midnight blue","ink blue"]),(7,FLAT,["sky blue","powder blue","cobalt blue","royal blue","steel blue","faded blue"]),(5,U(45,25,.6,1.4),["beige","sand","oatmeal","stone","camel","khaki"]),
 (4,FLAT,["red","brick red","tomato red","faded red"]),(1.5,D(35,10,.1),["hot pink","salmon pink","bubblegum pink"]),(5,FLAT,["forest green","sage green","olive green","emerald green","army green","bottle green"]),(4,U(45,25,.6,1.3),["chocolate brown","tan","rust brown","taupe","mocha"]),
 (2,D(45,15,.4),["mustard yellow","pale yellow","golden yellow"]),(2.5,U(40,25,.6,1.3),["burgundy","wine red","maroon","plum"]),(1.5,FLAT,["lavender","violet","deep purple"]),(1.5,D(40,15,.4),["burnt orange","terracotta","coral"]),(1.5,FLAT,["teal","turquoise","petrol blue"]),(0.5,D(35,8,.03),["neon green","electric blue","metallic silver","holographic silver"])]
PATTERN = [("",76,FLAT),("striped ",8,FLAT),("plaid ",5,FLAT),("checked ",2,FLAT),("floral-print ",1,U(45,25,.5,1.4)),("camouflage ",1.2,D(40,16,.3)),("tie-dye ",0.4,D(35,8,.03)),("gingham ",1,FLAT),("embroidered ",0.6,U(55,15,.2,1.8)),("tartan ",1.2,FLAT),("textured ",2,FLAT),("polka-dot ",0.4,FLAT)]
FIT = [("",30,FLAT,''),("relaxed-fit ",25,FLAT,''),("slim-fit ",20,D(45,15,.3),'tight'),("loose ",12,U(55,25,.7,1.3),'loose'),("oversized ",8,D(50,15,.3),'loose'),("boxy ",4,D(40,12,.2),'loose')]
TOPS = [("crew-neck t-shirt",20,FLAT,'',["cotton","soft cotton","jersey cotton","heavy cotton"]),("v-neck t-shirt",3,FLAT,'',["cotton","jersey"]),("graphic tee",5,D(40,12,.1),'',["cotton","soft cotton"]),("henley shirt",2,FLAT,'sleeved',["waffle-knit cotton","cotton"]),
 ("polo shirt",5,U(45,25,.5,1.4),'',["piqué cotton","cotton","performance knit"]),("oxford button-down shirt",6,FLAT,'structured sleeved',["oxford cotton","cotton poplin","chambray"]),("flannel shirt",4,FLAT,'sleeved',["brushed cotton","heavy flannel"]),("denim shirt",2,FLAT,'sleeved',["denim","chambray"]),
 ("linen shirt",2,U(40,20,.5,1.3),'loose',["linen"]),("camp-collar shirt",1.5,D(55,18,.3),'',["rayon","cotton"]),("hoodie",6,D(42,12,.2),'loose sleeved',["fleece","cotton fleece","heavy cotton"]),("zip-up hoodie",3,D(45,14,.2),'loose sleeved',["fleece","cotton fleece"]),
 ("sweatshirt",4,D(55,15,.3),'loose sleeved',["fleece","cotton fleece"]),("crewneck sweater",5,FLAT,'layered sleeved',["wool","lambswool","cotton-knit","merino wool"]),("quarter-zip pullover",3,U(40,20,.4,1.6),'layered sleeved',["merino wool","fleece","fine-knit"]),
 ("cardigan",1.5,U(55,12,.1,3),'layered sleeved',["wool","cotton-knit"]),("turtleneck",1.5,P(45,18,.4),'layered sleeved',["merino wool","ribbed-knit"]),("tank top",3,D(40,14,.2),'tank tight',["cotton","ribbed cotton"]),("sleeveless gym tee",2,D(36,12,.1),'tank athletic tight',["moisture-wicking mesh","jersey"]),
 ("long-sleeve tee",4,FLAT,'sleeved',["cotton","ribbed cotton"]),("baseball tee",1.5,D(40,12,.1),'sleeved',["cotton"]),("thermal waffle shirt",1.5,FLAT,'layered sleeved',["waffle-knit cotton"]),("cable-knit sweater",1.5,U(40,25,.5,1.5),'layered sleeved',["wool","cotton"]),
 ("vest over a collared shirt",1,U(55,14,.1,2.5),'layered',["wool","cotton"]),("Hawaiian shirt",1.5,U(40,25,.5,1.3),'',["rayon","cotton"]),("short-sleeve button-up shirt",3,FLAT,'structured',["cotton","linen blend"])]
JEAN_WASH = [("mid-wash",30,FLAT),("light-wash",20,D(50,18,.4)),("dark indigo",26,U(40,25,.6,1.3)),("faded blue",10,FLAT),("distressed light-wash",4,D(38,10,.08)),("black",8,FLAT),("grey",2,FLAT)]
JEAN_CUT = [("straight-leg",28,FLAT,''),("slim",22,D(40,14,.2),'tight'),("skinny",8,D(32,9,.04),'tight'),("relaxed",14,FLAT,'loose'),("bootcut",5,U(45,18,.3,1.3),''),("tapered",8,FLAT,''),("baggy",5,D(30,9,.05),'loose'),("loose straight",5,U(50,20,.3,1.4),'loose')]
BOTTOMS = [("jeans",30,FLAT,''),("chinos",9,FLAT,''),("khakis",3,U(45,20,.4,1.5),''),("cargo pants",3,D(45,12,.3),'loose'),("cargo shorts",3,D(55,16,.3),'short loose'),("denim shorts",2,D(50,15,.2),'short'),("athletic shorts",4,D(50,15,.3),'short athletic'),
 ("joggers",6,D(50,15,.3),'loose stretch'),("sweatpants",3,FLAT,'loose'),("corduroy pants",2,FLAT,''),("dress trousers",4,P(45,20,.4),'structured'),("pleated trousers",2,U(55,14,.1,2.5),'loose comfy'),("work pants",2,FLAT,''),("track pants",1.5,D(45,15,.3),''),
 ("linen pants",1.5,U(40,22,.4,1.3),'loose'),("elastic-waist trousers",1.5,U(65,10,.02,5),'loose comfy'),("board shorts",1.5,D(45,18,.3),'short')]
OUTER = [("denim jacket",7,D(55,20,.3),''),("leather jacket",5,D(55,18,.3),''),("bomber jacket",4,D(40,12,.1),''),("varsity jacket",1.5,D(30,9,.03),''),("field jacket",3,FLAT,'layered'),("blazer",6,P(45,20,.4),'structured'),("sport coat",2,U(50,18,.3,1.6),'structured'),
 ("puffer jacket",9,FLAT,'layered'),("parka",5,FLAT,'layered'),("trench coat",3,FLAT,'layered'),("wool overcoat",5,U(45,20,.4,1.5),'layered'),("windbreaker",4,FLAT,''),("fleece jacket",5,U(40,25,.6,1.3),'layered'),("rain jacket",5,FLAT,''),
 ("cardigan",2,U(55,12,.1,3),'layered'),("quilted vest",2,U(50,18,.3,1.8),'layered'),("peacoat",3,FLAT,'layered'),("shearling-lined jacket",1.5,FLAT,'layered'),("hooded anorak",2,FLAT,'')]
SHOES = [("white sneakers",16,FLAT,'athletic'),("black sneakers",10,FLAT,'athletic'),("canvas sneakers",6,D(50,18,.3),''),("running shoes",8,FLAT,'athletic'),("leather boots",7,FLAT,''),("work boots",5,FLAT,''),("chelsea boots",3,D(55,18,.3),''),("loafers",3,FLAT,''),
 ("sandals",3,D(50,18,.3),''),("slides",2,D(45,16,.3),''),("hiking boots",2,FLAT,'athletic'),("high-top sneakers",3,D(40,12,.1),''),("boat shoes",1.5,U(40,25,.5,1.3),''),("slip-on shoes",3,U(40,25,.6,1.4),'comfy'),("comfortable walking shoes",2,U(62,10,.03,4.5),'comfy'),("orthopedic-style supportive shoes",0.7,U(78,8,.01,8),'comfy'),("cushioned sneakers",3,U(55,15,.3,1.8),'comfy')]
SHOES_DRESS = [("polished oxford shoes",9,FLAT,''),("derby shoes",6,FLAT,''),("leather loafers",6,FLAT,''),("brogues",3,U(40,20,.4,1.4),''),("dress boots",4,FLAT,''),("monk-strap shoes",2,D(50,18,.3),''),("clean white sneakers",5,D(55,18,.3),'athletic'),("suede chukka boots",3,FLAT,''),("comfortable dress shoes",2,U(60,12,.03,4),'comfy')]
ACTIVE = [("a fitted athletic t-shirt with training shorts",3),("a compression top and joggers",2),("a navy tracksuit with white stripes",1.5),("a running vest and short split shorts",1),("a basketball jersey and baggy shorts",1.5),("cycling bib shorts with a jersey",1),("a gym tank and sweatpants",2),("a zip-up training jacket over a tee and joggers",2),("a hooded performance top with running tights",1)]
WORK = ["a high-visibility vest over a work shirt and rugged work pants","a mechanic's coveralls with a name patch","a chef's white double-breasted jacket with checked trousers","a lab coat over a shirt and tie","hospital scrubs with a stethoscope around the neck","a canvas apron over a flannel shirt and jeans","a carpenter's tool belt over a tee and work pants","a button-down shirt with a loosened tie and dress trousers","a security guard uniform with a utility belt","a delivery uniform polo with cargo shorts"]
SUITS = [("a navy two-piece suit",7),("a charcoal suit",6),("a black suit",4),("a light grey suit",3),("a tan summer suit",2),("a brown tweed suit",1.5),("a pinstripe suit",2),("a three-piece suit with a waistcoat",1.5),("a double-breasted suit",1.5),("a sport coat with contrasting trousers",3)]
SHIRTS = ["a crisp white dress shirt","a light blue dress shirt","a pale pink dress shirt","a striped dress shirt","a checked dress shirt","a white shirt with an open collar"]
TIES = ["a solid silk tie","a striped tie","a knit tie","a patterned tie with a tie clip","a bow tie","no tie, collar open","a pocket square and no tie"]
SPECIAL = [("a classic black tuxedo with a bow tie",.5,P(40,20,.5)),("swim trunks and a loose open shirt",1.2,D(45,20,.4)),("board shorts and a rash guard",.8,D(40,18,.3)),("a traditional kurta with fitted trousers",.5,FLAT),("a linen guayabera and trousers",.5,U(45,18,.3,1.6)),
 ("a jumpsuit-style coverall",.4,D(45,15,.2)),("denim overalls over a plain tee",.6,D(45,15,.2)),("a seersucker suit with a straw hat",.4,U(55,15,.1,2.5)),("a formal dark suit with a black tie for a funeral",.4,U(55,15,.05,2.0)),("a dinner jacket with a silk scarf",.3,U(55,15,.05,2.0))]
TYPES = [('tb',66,FLAT),('suit',8,P(42,18,.3)),('active',9,D(52,16,.25)),('work',8,P(40,18,.3)),('special',3.5,P(40,20,.5))]
TYPE_MOD = {'athl':{'active':2.0},'musc':{'active':1.8},'frail':{'active':0.25,'special':1.2,'suit':0.8},'heavy':{'active':0.8}}
OUT_PROB = 0.33
def colour(R, b):
    fam = R.choices(COL, weights=[c[0] * kb(c[1], b) for c in COL], k=1)[0]; return R.choice(fam[2])
def make_top(R, b, a):
    t = pick(R, TOPS, b, a); name, fabs = t[0], t[4]
    pat = R.choices(PATTERN, weights=[p[1] * kb(p[2], b) for p in PATTERN], k=1)[0][0]
    fit = R.choices(FIT, weights=[f[1] * kb(f[2], b) * bmod(a, f[3]) for f in FIT], k=1)[0][0]
    c = colour(R, b); fab = R.choice(fabs)
    if name == 'graphic tee': return f"{fit}{c} {fab} graphic tee with a printed design"
    return f"{fit}{c} {pat}{fab} {name}"
def make_bottom(R, b, a):
    it = pick(R, BOTTOMS, b, a); name = it[0]
    if name == "jeans":
        wash = R.choices(JEAN_WASH, weights=[x[1] * kb(x[2], b) for x in JEAN_WASH], k=1)[0][0]
        cut = R.choices(JEAN_CUT, weights=[x[1] * kb(x[2], b) * bmod(a, x[3]) for x in JEAN_CUT], k=1)[0][0]
        return f"{wash} {cut} jeans"
    if name == "denim shorts": return f"{R.choice(['light-wash','mid-wash','black','faded blue'])} denim shorts"
    return f"{colour(R, b)} {name}"
def make_outer(R, b, a):
    o = pick(R, OUTER, b, a)[0]
    if o == "denim jacket": return f"{R.choice(['light-wash','mid-wash','black','faded blue'])} denim jacket"
    if o == "leather jacket": return f"{R.choice(['black','black','brown','tan'])} leather jacket"
    if o in ("wool overcoat","trench coat","peacoat","parka"): return f"{R.choice(['black','navy','charcoal grey','camel','olive green','tan'])} {o}"
    return f"{colour(R, b)} {o}"
def outfit(R, b, a):
    tw = [t[1] * kb(t[2], b) * TYPE_MOD.get(a, {}).get(t[0], 1.0) for t in TYPES]; kind = R.choices(TYPES, weights=tw, k=1)[0][0]
    out_p = min(0.9, OUT_PROB * kb(U(50, 25, .7, 1.5), b) * bmod(a, 'layered') ** 0.5)
    if kind == 'tb':
        s = f"{art(make_top(R, b, a))} with {make_bottom(R, b, a)}"; shoe = pick(R, SHOES, b, a)[0]
        if R.random() < out_p: s += f" under {art(make_outer(R, b, a))}"
    elif kind == 'suit':
        suit = R.choices(SUITS, weights=[x[1] for x in SUITS], k=1)[0][0]; shirt = R.choice(SHIRTS); tie = R.choice(TIES)
        s = f"{suit} with {shirt} and {tie}"; shoe = pick(R, SHOES_DRESS, b, a)[0]
        if R.random() < out_p * 0.6: s += f" under {art(R.choice(['black','navy','charcoal grey','camel'])+' '+R.choice(['wool overcoat','trench coat','peacoat']))}"
    elif kind == 'active':
        s = R.choices(ACTIVE, weights=[x[1] for x in ACTIVE], k=1)[0][0]; shoe = R.choice(["white running shoes", "black training shoes", "grey sneakers"] if a != 'frail' else ["comfortable walking shoes", "cushioned sneakers"])
    elif kind == 'work':
        s = R.choice(WORK); shoe = R.choice(["steel-toe work boots", "leather work boots", "black non-slip shoes"] if a != 'frail' else ["comfortable walking shoes", "slip-on shoes"])
    else:
        sp = R.choices(SPECIAL, weights=[x[1] * kb(x[2], b) for x in SPECIAL], k=1)[0][0]; s = sp; shoe = pick(R, SHOES_DRESS, b, a)[0]
        if any(k in sp for k in ("swim trunks", "board shorts")): return s
    return s + (f" and {shoe}" if R.random() < 0.9 else "")
YOUNGW = {'streetwear':-1.5,'graffiti':-1.5,'oversized':-1,'hoodie':-0.8,'neon':-1.5,'festival':-1.5,'rave':-2,'skater':-1.5,'graphic':-0.8,'tank':-0.8,'sneaker':-0.5,'cyber':-1.2}
OLDW = {'tweed':2,'classic':0.7,'blazer':0.7,'traditional':0.6,'cardigan':1.5,'suit':0.6,'tailored':0.7,'formal':0.5,'wool':0.4,'vest':0.6,'overcoat':0.8,'pensioner':2}
TIGHTW = ('tight','fitted','compression','speedo','briefs','shirtless','sleeveless','tank')
POOL_EXCLUDE = r"^only\b|^no clothing|^nude|penis|genital|testic|^shirtless|underwear|boxer|briefs|jockstrap|g-string|thong|^a (large )?towel|washcloth|bedsheet|bad home-made|reflection|swim|^naked"
RANDOM_MIX = ["__clothing_everyday__"] * 20 + ["__clothing_full__"] * 30 + ["__outfit_cosplay__"] * 12 + ["__outfit_casual_mixed__"] * 8 + ["__outfit_formal_mixed__"] * 7 + ["__outfit_uniform_mixed__"] * 6 + ["__outfit_swim_mixed__"] * 7 + ["__outfit_see_through__"] * 4 + ["__outfit_color__ __outfit_swim_underwear__"] * 3 + ["__outfit_color__ __outfit_material__ __outfit_suit_style__"] * 3
