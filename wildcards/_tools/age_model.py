"""Age-conditioning model: turns an option list into per-bracket weights.
Each option gets an age 'affinity' spec (keyword heuristic + explicit overrides). weight(bracket) = base_weight * K(age; spec)."""
import re, math, collections
BRACKETS=[(18,24),(25,34),(35,44),(45,54),(55,64),(65,74),(75,84),(85,94),(95,120)]
# population-share of adult WOMEN per bracket (approx. UN WPP 2022/2023, from memory - verify before relying on it)
BRACKET_SHARE=[14.0,21.8,18.7,16.5,13.8,9.1,4.5,1.55,0.15]
def age_phrase(a):
    """descriptive wording for a single year of age, so a 62-, 78- and 97-year-old do not read alike"""
    names={20:'twenties',30:'thirties',40:'forties',50:'fifties',60:'sixties',70:'seventies',80:'eighties',90:'nineties'}
    pos='early' if a%10<=3 else 'mid' if a%10<=6 else 'late'
    when=f"in {'their' } {pos} {names.get(a//10*10,'')}".strip()
    if a<25: return f"{a} years old, a young adult"
    if a<45: return f"{a} years old, {when}"
    if a<55: return f"{a} years old, {when}, middle-aged with visible signs of aging"
    if a<65: return f"{a} years old, {when}, an older adult well into mid-life aging"
    if a<75: return f"{a} years old, {when}, a senior citizen with clearly aged features"
    if a<85: return f"{a} years old, {when}, elderly and visibly frail with deeply aged features"
    if a<95: return f"{a} years old, {when}, very elderly, shrunken and fragile with extremely aged features"
    if a<100: return f"{a} years old, almost a centenarian, extremely old, frail and deeply wrinkled"
    return f"{a} years old, a centenarian of extraordinary old age, tiny, fragile and ancient-looking"
def bname(b): return f"age{b[0]}_{b[1]}"

OLD={'papery':3,'turkey':3,'frail':2.5,'brittle':1.5,'aging':3,'aged':3,'age spots':3,'age-spot':3,'liver spots':3,'sun spots':1.5,
'sagging':2,'drooping':2,'jowls':2.5,'jowly':2.5,'slack':2,'loose':1.5,'flabby':1.2,'stringy':2,'ptosis':2,'denture-look':0.5,
'missing front teeth':2.5,'partially missing':2.5,'worn down':2,'grinding-worn':1.5,'exposed tooth roots':3,'exposed uneven tooth roots':3,
'receding':1.5,'recessed':1,'thinning':2,'sparse':1.2,'balding':2.5,'wrinkled':2,'creased':1.5,'furrowed':1.5,'etched':1.5,'weathered':1.2,
'weather-etched':3,'leathery':2.5,'leathered':2.5,'carved':3,'sun-aged':3,'sun-damaged':2,'hollow':1,'sunken':1,'gaunt':1,'faded':1.5,
'stiff':1,'rigid':1,'arthritic':3,'trembling':3,'varicose':2.5,'spider':1.2,'bunion-deformed':2,'hammer-toe':2,'hunched':2,'unsteady':2,
'stumbling':2,'grey':2,'cloudy':2,'translucent':0.8,'veiny':0.5,'knobby':2,'indistinct':1,'blurred':1,'fragile':1.5,'dingy':1.5,
'drained':0.5,'thin':0.4,'dry':0.4,'dull':0.4,'lifeless':0.4,'huddled':0.8,'stooped':3,'wiry':0.3,'ridged':1.5,'pigmentation':1,'melasma':0.5}
YOUNG={'youthful':-2.5,'baby-smooth':-3,'smooth':-1,'poreless':-1.5,'firm':-1,'tight':-1,'taut':-1.5,'plump':-1,'dewy':-1,'radiant':-1,
'fresh':-1,'luminous':-1,'glass-skin':-2,'bouncy':-1.5,'buoyant':-1.5,'springy':-2,'light-footed':-2,'lifted':-1.5,'lush':-1,'luscious':-1.5,
'pillow-soft':-1,'rosebud':-1,'acne-prone':-2,'braces':-3,'orthodontic':-3,'clogged':-1,'congested':-1,'oily':-1,'keratosis':-1.5,'chicken-skin':-1.5,
'elastic':-1.5,'sculpted':-1,'toned':-1,'athletic':-1,'chiseled':-1.5,'crisp':-1,'fluttering':-1,'dynamic':-1.5,'running':-2.5,'mid-jump':-3,'airborne':-3,
'dancing':-2,'crouching':-1,'aggressively':-1,'striding':-1,'cosmetic':-0.3,'clear':-0.5,'perfect':-0.3,'lean':-0.5,'rounded cheek':-0.5}
BODY_ONLY={'heavy':0.3,'fat':0.2,'soft':0.15,'fleshy':0.2,'bloated':0.3,'apron':1.5,'stretch-marked':0.5,'protruding':0.15}
ATYPICAL=['severe','swollen','bloodshot','bleeding','inflamed','decayed','deformed','bruised','singed','burnt','burned','jaundiced','petechiae','fungal',
 'injured','missing finger','missing toe','scarred','notched','pockmarked','bulging','gangly','emaciated','vampire','irritated','sore','tender','anaemic','spotted pigmented']
def kw_score(file,opt):
    t=opt.lower(); s=0.0
    for d in (OLD,YOUNG):
        for k,v in d.items():
            if re.search(r'(?<![\w-])'+re.escape(k),t): s+=v
    if file.startswith(('body_','musc_','hand_')):
        for k,v in BODY_ONLY.items():
            if k in t: s+=v
    return max(-3,min(3,s))
def spec_from_s(s):
    if abs(s)<0.2: return ('flat',)
    fl=0.01+0.5*math.exp(-1.0*(abs(s)-0.25))
    return ('up',48+10*s,9,fl,1.0) if s>0 else ('down',52+8*s,9,fl,1.0)
def logi(x): return 1/(1+math.exp(-x))
def K(spec,age):
    t=spec[0]
    if t=='flat': return 1.0
    if t=='up':   _,m,w,fl,amp=spec; return fl+(amp-fl)*logi((age-m)/w)
    if t=='down': _,m,w,fl,amp=spec; return fl+(amp-fl)*logi((m-age)/w)
    if t=='peak': _,mu,sg,fl=spec; return fl+(1-fl)*math.exp(-0.5*((age-mu)/sg)**2)
def Kbracket(spec,b): return sum(K(spec,a) for a in range(b[0],min(b[1],105)+1))/(min(b[1],105)-b[0]+1)

# ---- explicit overrides: (file, option) -> spec ; or file -> {keyword: spec} applied by substring ----
def U(m,w=9,fl=0.01,amp=1.0): return ('up',m,w,fl,amp)
def D(m,w=9,fl=0.2,amp=1.0): return ('down',m,w,fl,amp)
def P(mu,sg=14,fl=0.3): return ('peak',mu,sg,fl)
FLAT=('flat',)
SUB={ # file -> list of (substring, spec) ; first match wins; evaluated before keyword scoring
'skin_wrinkle':[('faint subtle expression',P(33,13,.15)),('soft faint facial',P(34,13,.15)),('subtle laugh',P(38,13,.15)),('fine smile lines',P(40,13,.15)),
  ('fine dry skin lines',P(46,14,.2)),('worry lines',U(58,9,.01,1)),('crinkled under-eye',U(56,9,.01,1)),("crow's feet",U(58,9,.01,1)),('marionette',U(66,9,.01,1)),
  ('smoker',U(62,10,.01,1)),('fine papery',U(70,8,.02,1)),('smooth tight unblemished',D(36,9,.04,1)),('smooth firm skin',D(40,9,.04,1)),('smooth unwrinkled',D(40,10,.03,1))],
'hair_color':[('salt-and-pepper',U(52,8,.01,4)),('silver grey',U(66,8,.01,8)),('snowy white',U(78,7,.01,10)),('mottled grey-brown',U(58,9,.01,4)),('dull greyish brown',U(52,10,.15,2)),
  ('dark brown with dark roots',D(45,15,.3)),('neon',D(30,8,.03)),('pastel',D(32,8,.03)),('green-tinted',D(32,8,.03)),('royal blue',D(32,8,.03)),
  ('platinum',D(50,14,.2)),('brassy',D(50,14,.2)),('burgundy',P(50,22,.5)),('auburn',P(48,22,.5)),('copper red',P(48,22,.5)),('orange-red',P(40,22,.4)),
  ('dyed',D(32,9,.04)),('ombre',D(32,9,.04)),('rainbow',D(30,8,.03)),('white',U(74,8,.01,8)),('silver',U(66,8,.01,8)),('grey',U(60,9,.01,6)),('rose gold',D(34,9,.04)),
  ('black',D(62,14,.12)),('brown',D(62,14,.12)),('blonde',D(55,14,.12))],
'hair_texture':[('wiry grey',U(60,10,.05,3)),('thin wispy',U(62,12,.2,2.5)),('fine thinning',U(60,12,.15,3)),('brittle breakable',U(62,12,.2,2.5)),('dull lifeless limp',U(55,15,.5,1.6)),
  ('glossy healthy',D(48,12,.3)),('smooth polished glossy',D(48,12,.3)),('supple bouncy',D(45,12,.25)),('soft velvety',D(48,14,.35)),('silky shiny',D(48,12,.3)),
  ('damaged bleached',P(32,14,.4)),('chemically treated',P(42,15,.4)),('rough weather-beaten',U(60,12,.3,1.5))],
'eye_color':[('cataract',U(76,7,.01,8)),('faded cloudy aged',U(70,8,.01,8)),('jaundiced',FLAT),('turbid',FLAT)],
'body_build':[('severely underweight',U(80,8,.15,3)),('bony emaciated',U(82,8,.1,3)),('tall gaunt',U(80,8,.1,3)),('skinny bony',U(74,12,.4,2)),('delicate frail',U(78,10,.2,3)),
  ('bodybuilder',P(30,10,.25)),('obese',P(60,16,.5)),('plump',P(55,18,.55)),('chubby',P(50,18,.55)),('rounded',P(55,18,.55)),('voluptuous',P(45,18,.6)),('heavy',P(58,16,.5)),('thick-set',P(58,16,.5)),
  ('full-figured',P(55,16,.5)),('pear',P(48,18,.6)),('slender',D(52,14,.45)),('petite',D(60,18,.7)),('lean wiry',D(52,14,.45)),('athletic',D(50,14,.35)),('toned',D(52,14,.4)),('hourglass',D(46,14,.5))],
'body_height':[('diminished',U(80,8,.05,12)),('petite',FLAT),('tall',D(70,22,.65)),('towering',D(70,22,.65))],
'pose_action':[('sitting casually',U(40,25,.6,1.3)),('sitting cross',D(45,14,.3)),('sitting upright formal',U(55,18,.5,1.6)),('sitting forward',U(55,18,.5,1.5)),('lounging',FLAT),
  ('slouched tired',U(60,15,.3,1.2)),('huddled',U(66,10,.2,1.3)),('stumbling',U(78,8,.02,3)),('cowering',FLAT),('walking forward',FLAT),('walking away',FLAT),('leaning',FLAT),
  ('standing',FLAT),('kneeling',D(55,10,.15)),('perched',D(40,10,.1)),('lying down',FLAT),('sprawled',D(45,12,.3)),('crouching',D(48,12,.1)),('dancing',D(48,14,.1)),('running',D(42,10,.03)),('mid-jump',D(38,8,.02)),('striding',D(55,14,.2)),('power pose',FLAT)],
'pose_twist':[('slouched',U(58,14,.3,1.5)),('hunched',U(62,12,.25,1.8)),('rigid',U(66,12,.2,1.5)),('huddled',U(66,12,.2,1.4)),('extreme',D(38,8,.03)),('dynamic',D(40,9,.05)),('dramatic backward',D(36,8,.03)),
  ('arched back',D(46,12,.15)),('athletic spine',D(48,12,.15)),('graceful',D(55,14,.3)),('spiraling',D(38,8,.04)),('sharply away',D(42,9,.1))],
'pose_weight':[('unsteady',U(78,8,.02,3)),('stumbling',U(78,8,.02,3)),('staggering',U(76,8,.01,2)),('heavy tired',U(62,14,.3,1.5)),('heavy slouched',U(60,14,.3,1.4)),('slouched',U(60,14,.3,1.3)),
  ('light-footed',D(50,12,.1)),('light springy',D(40,10,.05)),('upright lifted',D(52,14,.2)),('athletic stance',D(50,12,.15)),('aggressive',D(45,12,.15)),('rigid',U(64,12,.25,1.5)),('leaning heavily',U(62,12,.3,1.5))],
'hair_volume':[('thinning',U(55,10,.1,3)),('sparse',U(58,10,.1,2.5)),('balding',U(60,10,.05,3)),('wispy',U(52,14,.3,1.6)),('thin frail',U(62,12,.15,2.5)),('fine thin',U(48,14,.3,1.5)),('bouncy',D(45,12,.2)),('buoyant',D(45,12,.2))],
'hair_line':[('receding',U(52,12,.15,2)),('thinning',U(55,10,.1,2.5)),('sparse',U(55,10,.1,2.5)),('widely receded',U(62,10,.05,3)),('deeply receded',U(64,10,.05,3)),('fuzz-covered',D(32,10,.1)),('fuzzy soft',D(34,10,.2))],
}

SUB.update({
'musc_abs':[('deeply carved',D(32,9,.05)),('chiseled',D(32,9,.05))]+SUB.get('musc_abs',[]),
'skin_glow':[('translucent delicate',D(42,12,.4))]+SUB.get('skin_glow',[]),
'eye_color':SUB['eye_color']+[('grey',FLAT),('cyan',FLAT),('muddy',FLAT)],
'eye_sclera':[('bloodshot',FLAT),('red',FLAT),('translucent',FLAT),('yellow-tinged aged',U(72,9,.01,6)),('cloudy dull greyish',U(75,8,.01,5)),('dingy',U(65,10,.1,2))],
'hand_nails':[('bitten',D(35,10,.3))],
'body_compos':[('low body fat',D(40,10,.2)),('moderate healthy',FLAT),('balanced healthy',FLAT),('skinny-fat',FLAT),
  ('very high body fat',P(58,16,.5)),('high body fat',P(55,18,.55)),('heavy body fat',P(55,18,.55)),('heavy plump',P(55,18,.55)),('plump heavy',P(55,18,.55)),
  ('soft chubby',P(50,18,.55)),('chubby soft',P(50,18,.55)),('soft fleshy',P(55,18,.55)),('soft rounded',P(55,18,.55)),('heavy solid bulky',P(50,18,.6)),('bulky heavy',P(50,18,.6)),
  ('frail depleted',U(80,8,.05,6)),('frail thin skin',U(82,8,.05,6)),('frail low muscle',U(82,8,.05,6))],
})

def spec_for(file,opt):
    for sub,sp in SUB.get(file,[]):
        if sub in opt.lower(): return sp,'override'
    return spec_from_s(kw_score(file,opt)),'keyword'
def base_weight(file,opt,pilot_counts):
    if pilot_counts and opt in pilot_counts: return float(pilot_counts[opt])
    return 0.3 if any(k in opt.lower() for k in ATYPICAL) else 1.0

# ---------------- male overrides (WC_GENDER=m) ----------------
from gender import IS_M
if IS_M:
    BRACKET_SHARE = [14.9, 22.9, 19.2, 16.9, 13.7, 8.1, 3.4, 0.85, 0.05]       # adult men per bracket (approx. UN WPP; fewer men at older ages)
    SUB['hair_line'] = [('widely receded',U(46,10,.02,7)),('deeply receded',U(48,10,.02,7)),('receding',U(34,12,.08,4)),('thinning',U(34,12,.06,4.5)),('sparse',U(38,12,.06,3.5)),('fuzz-covered',D(32,10,.1)),('fuzzy soft',D(34,10,.2))]
    SUB['hair_volume'] = [('thinning',U(34,12,.06,4)),('sparse',U(38,12,.06,3.5)),('balding',U(45,12,.03,5)),('wispy',U(40,14,.2,2)),('thin frail',U(58,12,.1,3)),('fine thin',U(40,14,.3,1.8)),('bouncy',D(45,12,.2)),('buoyant',D(45,12,.2))]
    SUB['body_build'] = [('dad-bod',P(48,16,.5)),('barrel-chested',P(55,16,.5)),('burly',P(50,16,.5)),('stocky',P(50,18,.55)),('powerlifter',P(34,12,.3)),('compact muscular',D(52,16,.4)),('swimmer',D(42,12,.3)),('runner',D(48,14,.4)),('laborer',U(40,25,.6,1.2)),('lanky',D(50,15,.4)),('lean athletic',D(50,14,.35))] + SUB['body_build']
    SUB['facial_hair'] = [('salt-and-pepper',U(52,9,.01,5)),('white',U(70,8,.01,6)),('gray',U(58,9,.01,5)),('graying',U(55,9,.01,4)),('patchy',D(30,9,.1)),('sparse',D(30,9,.1)),('wispy',D(32,10,.1)),('long full beard',P(42,16,.3)),('braided',P(34,12,.2)),('designer',D(38,12,.15)),('handlebar',P(40,14,.3)),('clean',FLAT),('shaved',FLAT),('smooth',FLAT)]
