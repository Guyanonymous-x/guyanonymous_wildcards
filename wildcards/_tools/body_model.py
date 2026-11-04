"""Body-type (archetype) conditioning. Each option is placed on three axes from its wording:
   fat (0 very lean .. 1 very heavy), muscle (0 weak .. 1 very strong), frailty (0 robust .. 1 frail)   (None = option doesn't say)
An archetype is a target region on those axes; weight(option, archetype, age band) = base x archetype_kernel x age_kernel."""
import re, math
from age_model import *
ARCH = ['thin','slim','avg','athl','curvy','heavy','vheavy','musc','frail']
ARCH_LABEL = {'thin':'thin / underweight','slim':'slim','avg':'average','athl':'athletic / toned','curvy':'curvy / overweight','heavy':'heavy / obese (BMI 30-34)','vheavy':'severely obese (BMI 35+)','musc':'muscular / strong','frail':'frail (mostly elderly)'}
CENTER = {'thin':(.12,.15,.45),'slim':(.25,.30,.0),'avg':(.45,.35,.05),'athl':(.22,.80,.0),'curvy':(.65,.35,.0),'heavy':(.90,.30,.0),'vheavy':(1.0,.22,.05),'musc':(.35,.95,.0),'frail':(.15,.10,.95)}
SIG = (.20,.22,.30)
# archetype share (%) of adult women per age bracket (rough, from WHO/NCD-RisC-style BMI patterns; placeholders to be verified)
_SHARE8 = {
 (18,24):[8,28,28,12,12,9,2.5,0.5],(25,34):[6,22,28,11,15,15,2.5,0.5],(35,44):[4,14,26,7,22,24,2.5,0.5],(45,54):[3,11,24,5,25,29,2,1],
 (55,64):[3,10,23,4,26,31,1.5,1.5],(65,74):[3,9,22,3,26,30,1,6],(75,84):[4,9,22,2,24,24,0.5,14.5],(85,120):[5,9,20,1,20,17,0.3,27.7]}
_SHARE8M = {(18,24):[6,26,30,14,10,6,7,1],(25,34):[4,18,28,13,17,10,9,1],(35,44):[3,12,26,11,24,15,8,1],(45,54):[3,10,24,8,27,19,7,2],
             (55,64):[3,10,24,7,28,20,5,3],(65,74):[3,10,25,5,28,18,4,7],(75,84):[4,11,26,3,24,12,2,18],(85,120):[5,12,25,2,19,8,1,28]}
def _split(t):
    """[thin,slim,avg,athl,curvy,heavy,musc,frail] -> 9 values; 'heavy' becomes 68% heavy / 32% severely obese"""
    out = {}
    for k, v in t.items():
        v = list(v); h = v[5]; out[k] = v[:5] + [h * .68, h * .32] + v[6:]
    out[(85, 94)] = out[(85, 120)]; out[(95, 120)] = out[(85, 120)]; del out[(85, 120)]
    return out
SHARE = _split(_SHARE8)
from gender import IS_M
if IS_M: SHARE = _split(_SHARE8M)
BAND_OF = {(18,24):'y',(25,34):'y',(35,44):'y',(45,54):'m',(55,64):'m',(65,74):'o',(75,84):'o',(85,94):'o',(95,120):'o'}
BANDS = {'y':(18,44),'m':(45,64),'o':(65,105)}

FAT = {'dad-bod':.6,'barrel-chested':.55,'burly':.7,'powerlifter':.55,'v-taper':.22,'lanky':.2,'runner':.15,'swimmer':.22,'laborer':.4,'obese':.97,'very high body fat':.97,'apron':.97,'hanging':.9,'fat belly':.92,'buried':.92,'hidden':.85,'heavily overweight':.95,'flabby':.82,'bloated':.78,'distended':.78,
 'heavy':.82,'fleshy':.74,'plump':.7,'chubby':.7,'soft':.62,'rounded':.6,'voluptuous':.68,'curvy':.64,'full-figured':.78,'pear':.64,'thick':.62,'stocky':.55,'padded':.65,'covered':.65,
 'cellulite':.72,'love handles':.72,'stretch-marked':.6,'rolls':.78,'roll':.72,'folds':.75,'fold':.7,'puffy':.65,'wide':.55,'broad':.52,'thick-set':.75,'heavy-set':.78,'high body fat':.85,'sagging fat':.85,
 'slender':.25,'slim':.22,'lean':.2,'delicate':.22,'petite':.27,'narrow':.37,'toned':.22,'athletic':.25,'sculpted':.2,'chiseled':.1,'flat':.27,'firm':.28,'skinny':.1,'thin':.13,'gaunt':.05,
 'bony':.06,'emaciated':.02,'frail':.08,'underweight':.04,'sunken':.07,'stick':.05,'hollow':.09,'wiry':.18,'low body fat':.15,'compact':.4,'average':.45,'medium':.45,'balanced':.45,'moderate':.45,'hourglass':.5,'ribcage':.1,'hip bone':.1,'hip and rib':.1,'shoulder blades':.15,'iliac':.1,'ribs':.1}
MUSC = {'powerlifter':.85,'burly':.6,'dad-bod':.3,'v-taper':.8,'swimmer':.7,'runner':.5,'laborer':.6,'barrel-chested':.55,'bodybuilder':1.0,'muscular':.85,'sculpted':.85,'chiseled':.95,'carved':.9,'vascular':.85,'athletic':.72,'toned':.68,'defined':.7,'strong':.8,'solid':.6,'firm':.58,'powerful':.85,'wiry':.5,'lean':.5,
 'high muscle':.9,'muscle definition':.85,'dense muscular':.85,'pectoral':.8,'deltoid':.8,'trapezius':.8,'quadriceps':.85,'calf muscle':.7,
 'frail':.08,'weak':.1,'thin':.22,'skinny':.18,'unmuscled':.08,'flabby':.15,'soft':.25,'plump':.3,'drooping':.2,'sagging':.2,'gaunt':.15,'bony':.2,'untoned':.15,'emaciated':.05,'depleted':.06,'low muscle':.08}
FRAIL = {'frail':.95,'emaciated':.95,'gaunt':.8,'brittle':.9,'fragile':.85,'weak':.7,'severely':.9,'bony':.65,'skinny':.3,'stick':.7,'sunken':.6,'depleted':.9,'skin and bone':.9,'underweight':.8,'hollow':.5,'jutting':.45,'narrow compressed':.5,'ribcage':.45,'hip bone':.45,'hip and rib':.45,'iliac':.45,'shoulder blades':.35,'ribs':.45}
def _hits(d,t): return [v for k,v in d.items() if re.search(r'(?<![\w-])'+re.escape(k),t)]
def _combine(vals,base):
    if not vals: return None
    devs=sorted([v-base for v in vals],key=abs,reverse=True)
    x=base+devs[0]+0.3*sum(devs[1:]); return max(0.0,min(1.0,x))
def coords(opt,file=None):
    t=opt.lower()
    if file=='neck_crease' and not any(k in t for k in ('fleshy','rolls','double chin','puffy','heavy')): return None
    f=_combine(_hits(FAT,t),.45); m=_combine(_hits(MUSC,t),.4)
    fr=_hits(FRAIL,t); r=max(fr) if fr else None
    if f is None and m is None and r is None: return None
    return (f,m,0.0 if r is None else r)
def arch_kernel(c,a,floor=0.008):
    if c is None: return 1.0
    ctr=CENTER[a]; d2=0.0
    for i in range(3):
        if c[i] is not None: d2+=((c[i]-ctr[i])/SIG[i])**2
    return floor+(1-floor)*math.exp(-0.5*d2)
def Kband(spec,band):
    lo,hi=BANDS[band]; return sum(K(spec,a) for a in range(lo,hi+1))/(hi-lo+1)

def supp_coords(f,opt):
    """body coordinates for a supplement option (None for old-age options: those are driven by the age kernel)"""
    import supplements as S
    for tag in ('H3','H2'):
        if opt in S.SUPP.get(f,{}).get(tag,[]): return (S.FAT_OF[tag],None,0.0)
    for tag,fr in (('O3',.7),('O2',.3)):
        if opt in S.SUPP.get(f,{}).get(tag,[]): return (None,None,fr)
    return None
