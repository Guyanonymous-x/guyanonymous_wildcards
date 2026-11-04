"""Generate clothing_everyday.txt - natural-language outfits, frequency-weighted by how often they're worn.
Lines are pre-composed (garment x colour shade x fabric x fit) so outfits stay coherent; frequency comes from weighted sampling.
Every item in the rare-tail list (SPECIAL) is forced to appear at least once."""
import random, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from paths import wc_dir
from gender import IS_M
R = random.Random(11)
def pick(table):
    items, w = zip(*table); return R.choices(items, weights=w, k=1)[0]
def art(s): return ("an " if s[0].lower() in "aeiou" else "a ") + s

# ---- colour families: (weight, exact shades). Neutrals dominate real wardrobes; every family gets many shades. ----
COLORS = [
(17, ["white","bright white","off-white","soft white","cream-white","faded white","slightly yellowed white","crisp white"]),
(16, ["black","washed black","faded black","jet black"]),
(10, ["heather grey","light grey","charcoal grey","mid grey","slate grey","marled grey","dove grey"]),
(7,  ["navy","dark navy","midnight blue","ink blue"]),
(7,  ["sky blue","powder blue","cobalt blue","royal blue","steel blue","faded blue"]),
(6,  ["beige","sand","oatmeal","cream","ecru","stone","camel"]),
(5,  ["red","brick red","tomato red","cherry red","faded red"]),
(5,  ["blush pink","dusty rose","soft pink","hot pink","salmon pink","faded pink"]),
(5,  ["forest green","sage green","olive green","emerald green","mint green","khaki green","bottle green"]),
(3.5,["chocolate brown","tan","caramel","rust brown","taupe","mocha"]),
(2.5,["mustard yellow","butter yellow","pale yellow","golden yellow"]),
(2.5,["burgundy","wine red","maroon","plum"]),
(2,  ["lavender","lilac","violet","deep purple","mauve"]),
(1.5,["burnt orange","terracotta","coral","peach"]),
(1.5,["teal","turquoise","aqua","petrol blue"]),
(0.5,["neon green","electric blue","fuchsia","metallic silver","metallic gold","emerald-and-teal"]),
]
def colour(): return R.choice(pick([(c[1], c[0]) for c in COLORS]))
NEUTRAL_OUTER = ["beige","camel","black","navy","olive green","charcoal grey","tan","cream"]
PATTERN = [("",74),("striped ",8),("floral-print ",4),("plaid ",2.5),("polka-dot ",1.2),("tie-dye ",0.5),("animal-print ",0.7),("gingham ",0.9),("embroidered ",1.0),("lace-trimmed ",1.0),("textured ",1.5)]
FIT = [("",30),("relaxed-fit ",25),("fitted ",20),("loose ",12),("oversized ",8),("cropped ",5)]

TOPS = [ # name, weight, fabrics
("crew-neck t-shirt",20,["cotton","soft cotton","jersey cotton","thin cotton"]),
("v-neck t-shirt",5,["cotton","jersey"]),("long-sleeve tee",5,["cotton","ribbed cotton"]),
("tank top",5,["cotton","ribbed cotton","jersey"]),
("button-up shirt",6,["cotton poplin","oxford cotton","linen","chambray"]),
("blouse",7,["chiffon","crepe","satin","cotton voile","viscose"]),
("sweater",6,["wool","chunky-knit","fine-knit","cashmere-blend","cotton-knit"]),
("cardigan",3,["wool","fine-knit","cotton-knit"]),("hoodie",5,["fleece","cotton fleece","heavy cotton"]),
("sweatshirt",4,["fleece","cotton fleece"]),("polo shirt",2,["piqué cotton","cotton"]),
("camisole",2,["satin","silk","cotton"]),("crop top",2,["cotton","ribbed","jersey"]),
("turtleneck",2.5,["merino wool","ribbed-knit","fine-knit"]),("henley top",1.5,["waffle-knit cotton","cotton"]),
("tunic top",2,["cotton","linen","viscose"]),("off-shoulder top",0.7,["cotton","knit","chiffon"]),
("bodysuit",0.7,["stretch cotton","ribbed jersey"]),
]
def make_top():
    name, fabs = pick([((n, f), w) for n, w, f in TOPS])
    pat = pick(PATTERN); fit = pick(FIT); c = colour(); fab = R.choice(fabs)
    if pat == "": return f"{fit}{c} {fab} {name}"
    return f"{fit}{c} {pat}{fab} {name}"

JEAN_WASH = [("mid-wash",30),("light-wash",22),("dark indigo",22),("faded blue",10),("distressed light-wash",6),("black",6),("white",2),("grey",2)]
JEAN_CUT = [("straight-leg",26),("skinny",20),("wide-leg",14),("bootcut",6),("mom",12),("boyfriend",8),("high-waisted",10),("low-rise",4)]
BOTTOMS = [("jeans",24),("leggings",9),("chinos",4),("tailored trousers",3),("wide-leg trousers",3),("cargo pants",2.5),("joggers",5),("sweatpants",2),("denim shorts",5),("cotton shorts",3),("midi skirt",4),("mini skirt",2.5),("maxi skirt",2.5),("pencil skirt",1),("leather trousers",0.3)]
def make_bottom():
    name = pick(BOTTOMS)
    if name == "jeans": return f"{pick(JEAN_WASH)} {pick(JEAN_CUT)} jeans"
    if name == "denim shorts": return f"{pick([('light-wash',3),('mid-wash',3),('white',1),('black',1),('faded blue',1)])} {R.choice(['cut-off ','high-waisted ','bermuda ',''])}denim shorts".replace("  "," ")
    if name == "leggings": return f"{R.choice(['black','black','black','grey','dark navy','charcoal','patterned'])} leggings"
    if name == "leather trousers": return "black leather trousers"
    if name in ("midi skirt","mini skirt"):
        k = R.choice(["denim","pleated","A-line","cotton"]); 
        return f"{R.choice(['light-wash','mid-wash'])} denim {name}" if k == "denim" else f"{colour()} {k} {name}"
    if name == "maxi skirt": return f"{colour()} {R.choice(['flowing','tiered','printed','cotton'])} maxi skirt"
    return f"{colour()} {name}"

DRESSES = [("sundress",6),("shirt dress",3),("wrap dress",3),("maxi dress",5),("midi dress",5),("t-shirt dress",3),("slip dress",1.5),("sweater dress",2),("denim dress",1),("little black dress",2),("pinafore dress",1),("shift dress",2),("bodycon dress",1.5)]
def make_dress():
    d = pick(DRESSES)
    if d == "little black dress": return d
    if d == "denim dress": return f"{R.choice(['light-wash','mid-wash'])} denim dress"
    return f"{colour()} {pick(PATTERN)}{d}"
def make_outer():
    o = pick([("denim jacket",8),("puffer jacket",9),("wool coat",6),("trench coat",5),("blazer",6),("leather jacket",4),("parka",5),("windbreaker",4),("fleece jacket",5),("rain jacket",5),("bomber jacket",3),("cardigan",5),("quilted jacket",3),("shawl",2),("duster coat",1),("poncho",0.8)])
    if o == "denim jacket": return f"{R.choice(['light-wash','mid-wash','black','faded blue'])} denim jacket"
    if o == "leather jacket": return f"{R.choice(['black','black','brown','tan'])} leather jacket"
    if o in ("trench coat","wool coat","duster coat","parka"): return f"{R.choice(NEUTRAL_OUTER)} {o}"
    return f"{colour()} {o}"

SHOES_CASUAL = [("white sneakers",16),("black sneakers",9),("canvas sneakers",7),("running shoes",8),("leather ankle boots",8),("flat sandals",8),("ballet flats",6),("loafers",4),("black leather boots",4),("flip-flops",4),("sports sandals",2),("rain boots",1.5),("hiking boots",1.5),("platform sneakers",2),("slip-on shoes",3),("mules",1.5)]
SHOES_DRESS = [("white sneakers",14),("flat sandals",14),("ballet flats",10),("leather ankle boots",9),("block-heel sandals",8),("low heels",7),("high heels",4),("loafers",5),("espadrilles",4),("black sneakers",5),("mules",3),("platform sneakers",3),("knee-high boots",3)]
ACTIVE = ["a matching grey athletic set of leggings and sports top","a black sports bra with high-waisted yoga leggings","loose running shorts and a technical tee","a navy tracksuit with white stripes","cycling shorts with a loose tee","a fitted sleeveless gym top with black training tights"]
SPECIAL = ["a satin evening gown","a sequined cocktail dress","a tailored two-piece trouser suit","a black tie formal dress","a one-piece swimsuit",
 "a two-piece bikini","a sarong over a swimsuit","an emerald and teal sequined slingshot-style bikini","a silk kimono-style robe",
 "a traditional-style wrap blouse and long skirt","denim overalls over a striped tee","a jumpsuit","boiler-suit style coveralls","a sequined top with black trousers"]
SPECIAL_W = [0.5,0.5,1.2,0.2,1.2,1.0,0.3,0.03,0.3,0.5,0.8,1.5,0.4,0.4]

def outfit():
    r = R.random()
    if r < 0.57:
        s = f"{art(make_top())} with {make_bottom()}"
        if R.random() < 0.33: s += f" under {art(make_outer())}"
        shoe = pick(SHOES_CASUAL)
    elif r < 0.77:
        s = art(make_dress())
        if R.random() < 0.30: s += f" with {art(make_outer())}"
        shoe = pick(SHOES_DRESS)
    elif r < 0.85:
        s = R.choice(ACTIVE); shoe = R.choice(["white running shoes","black training shoes","grey sneakers"])
    else:
        s = R.choices(SPECIAL, weights=SPECIAL_W, k=1)[0]
        if any(k in s for k in ("bikini","swimsuit","sarong")): return s
        shoe = pick(SHOES_DRESS)
    return s + (f" and {shoe}" if R.random() < 0.9 else "")

def main(N=2500, out=None):
    out = out or os.path.join(wc_dir(), 'clothing_everyday.txt')
    if IS_M:                       # men: age-neutral outfits from the male catalogue
        import clothing_cat_m as M
        Rm = random.Random(11); lines = [M.outfit(Rm, None, 'avg') for _ in range(N)]
    else:
        lines = [outfit() for _ in range(N)]
    for sp in (SPECIAL if not IS_M else []):      # guarantee every rare-tail item at least once (female list only)
        if not any(sp in l for l in lines): lines[R.randrange(N)] = sp
    open(out, 'w', encoding='utf8', newline='\n').write('\n'.join(lines) + '\n'); return lines
if __name__ == '__main__':
    L = main(); N = len(L)
    if IS_M: print(N, 'male outfits written'); raise SystemExit
    print(N, 'lines', len(set(L)), 'unique')
    for l in L[:12]: print(' ', l)
    sh = lambda k: sum(1 for l in L if k in l) / N * 100
    print('t-shirts %.1f%% | white-family tops %.1f%% | jeans %.1f%% | dresses %.1f%% | sequin %.2f%% | slingshot lines %d' % (
        sh('t-shirt'), sum(1 for l in L if ('t-shirt' in l or 'tee' in l) and ('white' in l or 'cream' in l)) / N * 100, sh('jeans'), sh('dress'), sh('sequin'), sum(1 for l in L if 'slingshot' in l)))
