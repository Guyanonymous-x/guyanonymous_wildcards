"""Hair layer: hair TYPE (S straight, W wavy, C curly, K coily) is chosen first, then identity line, hairstyle, curl, texture and volume all agree with it.
Ethnic prompt lines are split by the hair type their own wording states; unspecified lines are assigned deterministically from a rough conditional guess."""
import re, zlib, random, collections
from age_model import *
from gender import IS_M
TYPES=['S','W','C','K']; TNAME={'S':'straight','W':'wavy','C':'curly','K':'coily'}
INDEP_SHARE={'S':58,'W':22,'C':12,'K':8}      # rough worldwide guess for the 'independent' (no ethnic line) mode - placeholder
def line_type(line):
    t=line.lower()
    if any(k in t for k in ('coiled','tightly curled','kinky','afro','coily')): return 'K','stated'
    if 'wavy to' in t or 'straight to wavy' in t or 'wavy' in t: return 'W','stated'
    if 'curly' in t or 'curled' in t: return 'C','stated'
    if 'straight' in t: return 'S','stated'
    r=random.Random(zlib.crc32(line.encode())).random()
    if re.search(r'black african|afro-|afro |african ',t): p=(0.02,0.08,0.15,0.75)                       # S,W,C,K  (unspecified hair, African / Afro-descended group label)
    elif re.search(r'(dark|deep|rich) brown skin|ebony|very dark skin',t): p=(0.10,0.15,0.20,0.55)    # unspecified hair + dark skin
    elif re.search(r'blond|light brown|brown hair|light eyes|blue|green|fair|pale',t): p=(0.45,0.40,0.15,0.0)
    else: p=(0.70,0.22,0.08,0.0)
    c=0
    for ty,pp in zip(TYPES,p):
        c+=pp
        if r<=c: return ty,'assigned'
    return 'S','assigned'

# ---- originals: which hair types each original hair_style option is compatible with ----
ORIG_STYLE={ "long layered flowing hair":'SWC',"long straight blunt cut":'S',"side-parted wavy hair":'W',"center-parted sleek hair":'S',"sleek pulled-back hairstyle":'SW',
"neat tight ponytail":'SWCK',"half-up half-down style":'SWCK',"messy high top knot bun":'SWCK',"tight bun at nape":'SWCK',"classic chin-length bob":'SW',"asymmetrical angled bob":'SW',
"layered curtain bangs cut":'SW',"french braid crown":'SWCK',"twin pigtails style":'SWCK',"intricate box braids":'K',"long cornrows braided style":'K',"tight dreadlocks locs":'KC',
"afro puff hairstyle":'K',"short blunt pixie cut":'SWC',"shaggy mullet cut":'SWC',"buzzcut short crop":'SWCK',"undercut with long top":'SWCK',"short messy crop":'SWCK',
"vintage finger waves":'SWK',"wild untamed mop of hair":'WCK',"frizzy uncombed bedhead hair":'WC',"matted tangled hair mass":'WCK',"shaved bald head":'SWCK'}
ORIG_CURL={0:'S',1:'W',2:'W',3:'W',4:'C',5:'C',6:'C',7:'K',8:'K',9:'W',10:'C',11:'S',12:'C',13:'W',14:'C',15:'C',16:'K',17:'W',18:'W',19:'C',20:'K',21:'S',22:'W',23:'C',24:'K',25:'C',26:'W',27:'K'}

# ---- curl: weights for originals (by index) and new natural-language options ----
CURL_NEW={'S':[("naturally straight hair with a gentle bend at the ends",14),("poker-straight fine hair with no wave",10),("straight hair with a slight natural flip at the ends",8),("straight and thick with a heavy smooth fall",16),("straight with a subtle kink from being tied up all day",4),("straight roots with a faint wave through the lengths",8),("silky straight hair that falls flat against the head",6),("blow-dried straight with a smooth rounded finish",8),("flat-ironed pin-straight finish",6),("straight hair with natural cowlicks at the crown",3)],
'W':[("loose natural waves that bend through the lengths",10),("S-shaped waves that start at mid-length",6),("wavy roots with straighter ends",4),("air-dried waves with soft definition",6),("wavy hair with a few loose curls underneath",4)],
'C':[("defined curls with a springy bounce",10),("loose curls that stretch when wet",6),("curls that shrink up toward the root",6),("mixed curl pattern with looser curls at the nape",5),("voluminous curls with a halo of frizz",6)],
'K':[("tight coils with significant shrinkage",8),("defined coil pattern with a soft sheen",6),("stretched coils worn out in a twist-out pattern",4),("fine coily strands with a cotton-soft texture",5),("springy z-pattern coils in tight clusters",6)]}
CURL_ORIG_W={0:14,1:18,2:16,3:10,4:14,5:14,6:8,7:14,8:14,9:2,10:4,11:3,12:2,13:6,14:0.3,15:3,16:8,17:4,18:10,19:8,20:10,21:3,22:6,23:8,24:12,25:3,26:8,27:8}

# ---- hairstyle grammar (noun phrases, so they fit "she wears it as ___" / "Her hairstyle is ___") ----
LEN=[('crop',3.0,U(50,12,.3,1.8)),('chin',9.0,P(55,20,.5)),('shoulder',15.0,FLAT),('collar',12.0,FLAT),('mid',24.0,D(55,14,.35)),('waist',9.0,D(48,12,.15)),('hip',2.5,D(42,10,.1))]
LEN_NOUN={'shoulder':'shoulder-length hair','collar':'collarbone-length hair','mid':'mid-back-length hair','waist':'waist-length hair','hip':'hip-length hair'}
CROP=["a pixie cut with wispy tapered sides and a textured fringe","a boyish cut with short sides and a longer swept top","a cropped layered cut with side-swept bangs","a close-cropped cut with a soft tapered nape","a short messy crop with uneven layers","a short tousled cut with a wispy neckline","a very short shaped cut with the ears showing"]
CHIN=["a blunt chin-length bob with a sharp one-length edge","a rounded layered chin-length bob","an A-line bob that is longer at the front","a graduated stacked bob","a soft tapered bob with feathered ends","a jaw-grazing cut with heavy layers","a chin-length bob with curtain bangs and face-framing pieces","a razor-cut bob with textured ends"]
CUT_MID=["with long soft layers","with blunt one-length ends","with feathered layers around the face","with choppy textured layers","with a shaggy layered cut","with a soft graduated shape","with a wolf-style layered cut","with face-framing layers and curtain bangs","with heavy blunt ends and a sharp part"]
CUT_LONG=["with long flowing layers","with blunt one-length ends","with long face-framing layers","with soft U-shaped layers at the back","with a V-shaped cut at the back","with very subtle layers","with thick heavy ends","with wispy feathered ends"]
CUT_CURLY=["with a rounded curly shape and shaped layers","with a tapered cut that keeps volume at the crown","with curl-friendly layers cut for definition","with a curly shag and lots of volume"]
FRINGE=[('',45,FLAT),('blunt full bangs',7,D(50,14,.4)),('wispy see-through bangs',6,D(50,14,.4)),('curtain bangs parted in the middle',9,D(50,14,.4)),('long side-swept bangs',13,FLAT),('short micro bangs',1.5,D(40,12,.2)),('face-framing pieces at the front',12,FLAT),('a soft fringe brushed to one side',6,FLAT)]
STYLING=[ # phrase, min length index, weight, age spec
('worn loose and down',0,40,FLAT),('with a center part',0,14,FLAT),('with a deep side part',0,14,FLAT),('tucked behind the ears',0,7,U(40,25,.7,1.3)),('swept back off the face',1,5,FLAT),
('pulled back into a low ponytail',2,7,FLAT),('pulled up into a high ponytail',2,6,D(35,12,.2)),('twisted into a low bun at the nape',2,5,U(45,15,.4,1.5)),('gathered into a messy top knot',2,4,D(40,14,.2)),
('worn half up with a clip',2,5,D(55,15,.4)),('worn half up, half down',2,6,D(55,15,.4)),('in a single loose braid over one shoulder',3,3.5,FLAT),('in a long braid down the back',3,2.5,FLAT),
('in two plaits',3,1.8,D(32,10,.1)),('in twin pigtails',2,0.5,D(25,8,.05)),('pinned up in a claw-clip updo',2,3,FLAT),('in a sleek low chignon',2,2.5,U(50,14,.3,1.3)),('in a French twist',3,1.5,U(55,12,.2,1.8)),
('held back with a headband',1,3,FLAT),('held back with a silk scarf tied as a headband',1,1,U(40,15,.5,1.3)),('slicked back and tucked behind the ears',1,2,FLAT),
('covered loosely by a headscarf with a few strands showing at the front',1,2.0,U(45,25,.7,1.3)),('windblown and tousled',0,3,D(50,14,.4)),('slightly messy as if freshly woken',0,2,D(40,14,.3))]
STYLING_EXTRA={'W':[('air-dried and loosely tousled',0,5,D(50,14,.4)),('styled in loose beachy movement',0,3,D(45,14,.3))],
 'C':[('worn loose and voluminous',0,14,FLAT),('in a high pineapple bun',2,3,D(45,14,.3)),('pulled into a puffy curly ponytail',2,4,FLAT),('in a braided crown',3,1.5,FLAT),('half up with a scrunchie',2,3,D(50,14,.4)),('pinned back with clips',1,3,FLAT)]}
KCAT=[("long box braids falling past the shoulders to mid-back",8,FLAT),("waist-length knotless braids with a center part",5,FLAT),("shoulder-length box braids pulled into a half-up bun",3,FLAT),("medium-length goddess braids with curly ends",1.5,D(55,15,.4)),
("Senegalese twists to mid-back",3,FLAT),("chunky passion twists framing the face",1.5,D(45,14,.3)),("straight-back cornrows running from the hairline to the nape",5,FLAT),("intricate patterned cornrows with a swirl design",2.5,D(50,14,.3)),
("feed-in braids pulled into a high ponytail",2,D(50,14,.3)),("two large flat twists on each side",1.5,FLAT),("a defined twist-out falling to the shoulders",4,FLAT),("Bantu knots covering the head",1.5,D(45,14,.3)),
("a rounded full afro shape",5,FLAT),("a tapered natural afro with shaped edges",4,FLAT),("a high afro puff with a silk scarf tied around it",3,FLAT),("a low puff gathered at the nape",2.5,FLAT),
("a short tapered natural cut close to the scalp",6,U(55,14,.3,1.8)),("a very short teeny-weeny afro",3,U(55,14,.3,1.5)),("shoulder-length natural coils worn loose",3,FLAT),("mid-length locs worn loose over the shoulders",3,FLAT),
("long locs pulled into a high bun",2,FLAT),("short starter locs",1,D(40,14,.3)),("faux locs to the waist",1.5,D(45,14,.2)),("a silk-pressed straight style falling to the shoulders",2.5,FLAT),
("a braided updo with sculpted edges",1.5,FLAT),("crochet braids with soft curly texture",1.5,FLAT),("fulani braids with beads at the ends",1.2,FLAT),("a bold printed headwrap with a few coils showing at the front",3,U(45,25,.6,1.4)),
("flat twists pinned into a low bun",1.5,U(50,14,.3,1.3)),("shaved close at the sides with a longer twisted top",1,D(35,12,.2)),("a wash-and-go with defined coils and volume at the crown",3,FLAT),
("two puffs on either side of a center part",1.2,D(30,10,.1)),("a cropped shaped afro with a high curved hairline",1.5,FLAT)]
KSUFFIX=[("",60),(", with edges laid and sculpted",6),(", with gold cuffs on a few strands",3),(", decorated with colorful beads",2),(", with soft face-framing pieces left out",4),(", worn with a thin headband",3)]

def wchoice(rng,items,wfun):
    w=[wfun(i) for i in items]; return rng.choices(items,weights=w,k=1)[0]
def gen_style(T,b,rng):
    kb=lambda sp: Kbracket(sp,b) if b else 1.0
    if T=='K':
        it=wchoice(rng,KCAT,lambda i:i[1]*kb(i[2])); suf=rng.choices(KSUFFIX,weights=[s[1] for s in KSUFFIX],k=1)[0][0]
        return it[0]+suf
    ln=wchoice(rng,LEN,lambda i:i[1]*kb(i[2])); key=ln[0]; idx=[l[0] for l in LEN].index(key)
    if key=='crop': return rng.choice(CROP)
    fr=''
    if key=='chin': base=rng.choice(CHIN)
    else:
        cuts=(CUT_MID if key in('shoulder','collar') else CUT_LONG)+(CUT_CURLY if T=='C' else [])
        base=LEN_NOUN[key]+' '+rng.choice(cuts)
    has_bangs='bangs' in base
    if not has_bangs:
        f=wchoice(rng,FRINGE,lambda i:i[1]*kb(i[2])); fr=f[0]
    sty=[s for s in STYLING+STYLING_EXTRA.get(T,[]) if s[1]<=idx]
    s=wchoice(rng,sty,lambda i:i[2]*kb(i[3]))[0]
    parts=[base]+([fr] if fr else [])+[s]
    return ', '.join(parts)

# ---- texture / volume affinity by hair type ----
TEX_AFF=[(('silky','sleek','smooth','glossy','liquid','velvety'),(1,.8,.4,.15)),(('dense springy','fluffy cloud'),(.1,.35,.9,1)),(('coarse','rough untamed','thick heavy'),(.9,.8,.8,.8)),
 (('frizzy',),(.3,.8,1,.5)),(('thin wispy','fine thinning','brittle breakable','dull lifeless limp','greasy matted limp'),(1,.8,.6,.5)),(('supple bouncy',),(.5,.8,1,.6))]
VOL_AFF=[(('afro volume','massive voluminous','wild expanded','voluminous curly mass','dense thick hair mane','rich dense heavy','dense heavy full','full bouncy high','full buoyant','thick voluminous'),(.3,.6,1,1)),
 (('puffed-up teased','teased retro'),(.7,.8,.8,.6)),(('flat','limp','slicked','compressed','fine thin','thin frail','wispy','lifeless'),(1,.8,.4,.2))]
def aff(table,opt,T):
    t=opt.lower(); i=TYPES.index(T)
    for keys,vec in table:
        if any(k in t for k in keys): return vec[i]
    return 1.0

# ============================ MALE hairstyles (WC_GENDER=m) ============================
FINISH_M = [("",50,FLAT),(", styled with matte clay",8,FLAT),(", slicked with a little pomade",5,D(55,18,.3)),(", air-dried and natural",8,FLAT),(", with a sharp lineup along the forehead",5,D(45,15,.2)),(", neatly combed",6,U(50,20,.5,1.5)),(", tousled and messy",4,D(45,15,.3)),(", with a clean razor-cut neckline",4,FLAT)]
CATS_M = {  # name: (weight, age spec, phrases for S/W, extra phrases for C)
 'buzz':(3.5,FLAT,["a close buzz cut with an even length all over","a very short number-two buzz cut","a military-style high-and-tight buzz","a uniform clipper cut with a faint taper"],[]),
 'crew':(5,FLAT,["a classic crew cut with short tapered sides and a slightly longer top","an ivy league cut with a short side part","a short caesar cut with a straight fringe"],[]),
 'fade':(18,D(55,18,.3),["a low taper fade with a textured top and a side part","a mid skin fade with a swept-back top","a high fade with a short textured quiff","a burst fade blended into a medium-length top","a drop fade with a messy textured fringe","a skin fade with a tidy comb-over top","a taper fade with a slicked-back top","a temple fade with a short pompadour top"],["a mid fade with loose curls on top","a high fade with a curly top","a skin fade with a defined curl crop"]),
 'sidepart':(9,FLAT,["a short side-parted cut with tapered sides","a neat side part with scissor-cut length on top","a classic gentleman's cut with a deep side part","a medium side-swept cut with natural movement"],["a side-parted cut with soft curls on top"]),
 'classic':(8,U(45,25,.5,1.5),["a short back-and-sides cut with a tidy top","a conservative short cut brushed to one side","a neat scissor-cut with short layers","a short business cut with a clean neckline"],["a short tapered curly cut"]),
 'crop':(6,D(50,16,.3),["a textured French crop with a short straight fringe","a messy textured crop with choppy layers","a short cropped cut with a forward-swept fringe"],["a curly crop with a tapered neckline"]),
 'quiff':(4,D(45,15,.2),["a voluminous quiff swept up and back","a high pompadour with tight sides","a rockabilly pompadour with a defined sweep","a textured quiff with a short taper"],["a curly quiff with tapered sides"]),
 'slick':(5,FLAT,["slicked-back hair combed straight back","a long slicked-back style behind the ears","a wet-look combed-back cut with short sides","a combed-back undercut"],["slicked-back curls laid flat"]),
 'medium':(8,D(55,16,.3),["medium-length tousled hair falling over the ears","medium-length hair pushed back from the forehead","a medium-length wavy shag","a jaw-length layered cut with a loose part","ear-length curtains parted in the middle"],["medium-length curls falling over the ears","a medium curly mop top"]),
 'long':(4,D(45,15,.1),["shoulder-length hair worn loose behind the ears","long hair falling past the shoulders","long layered hair with a center part","collarbone-length hair tucked behind the ears"],["shoulder-length curls worn loose","long curly hair falling past the shoulders"]),
 'tied':(2.5,D(50,16,.1),["a messy man bun with shaved sides","long hair tied in a low ponytail","a top knot with a short fade at the sides","hair pulled back into a half-up bun","a neat low bun at the nape"],["curly hair tied in a puffy top knot","a curly ponytail"]),
 'undercut':(3,D(40,12,.1),["a disconnected undercut with long hair on top","a shaved-sides undercut with a swept top","an undercut with a braided section on top"],[]),
 'mullet':(0.7,D(35,10,.05),["a modern textured mullet with short sides","a long mullet falling over the nape"],["a curly mullet"]),
 'shaved':(3,U(40,15,.5,2.5),["a completely shaved head with a smooth scalp","a shaved head with a day of stubble on the scalp","a clean-shaven bald head with a polished shine"],[]),
 'horseshoe':(2,U(40,12,.02,9),["hair only around the sides and back in a thin horseshoe, with a bald crown","a bald crown with short cropped hair at the sides","a thinning top with a short buzzed horseshoe of hair"],[]),
 'combover':(1.5,U(50,12,.05,5),["a comb-over covering a thinning top","long strands swept across a balding crown","a side-swept comb-over with short sides"],[]),
 'thin':(2.5,U(45,12,.05,6),["short hair thinning at the crown and temples","a receding hairline with short hair brushed forward","a short cut with visible thinning on top"],[]),
}
KCAT_M = [("a low fade with a sponge-twist top",6,D(55,18,.3)),("a high-top fade with a flat top",3,D(40,14,.1)),("a taper afro with a sharp lineup",5,FLAT),("a rounded natural afro with shaped edges",4,FLAT),("a low cut with defined 360 waves",5,FLAT),("a short wave cut with a skin fade",4,FLAT),
 ("short straight-back cornrows with a fade at the sides",4,D(50,16,.3)),("long cornrows braided to the back",2.5,D(50,16,.2)),("shoulder-length box braids worn loose",3,D(55,16,.2)),("two-strand twists on top with faded sides",3,D(45,15,.2)),("shoulder-length twists tied back",2,D(50,16,.2)),
 ("short freshly started locs",1.5,D(40,14,.2)),("mid-length locs worn loose over the shoulders",3,FLAT),("long locs tied back into a bun",2,FLAT),("a shaved head with a neat lineup",5,U(40,15,.5,2.5)),("a close-cropped natural cut",6,U(50,18,.4,1.6)),("a very short natural cut with receding temples",3,U(45,12,.05,5)),
 ("a bald crown with a neat horseshoe of tight hair at the sides",2,U(40,12,.02,9)),("a braided ponytail with faded sides",1.5,D(40,14,.1)),("a twist-out falling to the ears",2,D(45,15,.2)),("an afro puff with shaved sides",1.2,D(35,12,.1)),("a taper with a wavy brush-cut top",3,FLAT)]
def gen_style_m(T,b,rng):
    kb=lambda sp: Kbracket(sp,b) if b else 1.0
    if T=='K':
        it=wchoice(rng,KCAT_M,lambda i:i[1]*kb(i[2])); fin=wchoice(rng,FINISH_M,lambda i:i[1]*kb(i[2]))[0]
        return it[0]+(fin if fin and 'shaved' not in it[0] else '')
    names=list(CATS_M); cname=rng.choices(names,weights=[CATS_M[n][0]*kb(CATS_M[n][1]) for n in names],k=1)[0]
    w,sp,base,curly=CATS_M[cname]; pool=(base+curly*2) if T=='C' and curly else base
    phrase=rng.choice(pool)
    if cname in ('shaved','horseshoe','combover','thin','buzz'): return phrase
    fin=wchoice(rng,FINISH_M,lambda i:i[1]*kb(i[2]))[0]
    return phrase+fin
_gs_f=gen_style
def gen_style(T,b,rng): return gen_style_m(T,b,rng) if IS_M else _gs_f(T,b,rng)
if IS_M: ORIG_STYLE={}

try:   # vocabulary expansion: many more coily-hair styles (keeps the original ones)
    import vocab_people as _vp
    KCAT += _vp.k_styles('f'); KCAT_M += _vp.k_styles('m')
except ImportError:
    pass
