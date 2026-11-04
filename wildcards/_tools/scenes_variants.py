import re,random,sys
sys.path.insert(0,'.')
import scenes_gen as G
from scenes_gen import *
NUM=["two","three","four","five","six","seven","eight"]
LET="ABCDEFGH"
VERB={'have':'has','are':'is','look':'looks','wear':'wears','show':'shows','carry':'carries','keep':'keeps','sit':'sits','stand':'stands','appear':'appears','seem':'seems','do':'does','get':'gets','hold':'holds','hide':'hides','bear':'bears','display':'displays','were':'was','don\'t':'doesn\'t','add':'adds','come':'comes','give':'gives','use':'uses','move':'moves','stay':'stays','tend':'tends'}
def sents(t): return re.split(r'(?<=\.)\s+',t.strip())
def chunk(ss,maxw=50):
    out=[];cur=[]
    for s in ss:
        s=s.strip()
        if not s: continue
        if cur and sum(len(x.split()) for x in cur)+len(s.split())>maxw:
            out.append(cur);cur=[]
        cur.append(s)
    if cur: out.append(cur)
    res=[]
    for c in out:
        parts=[c[0].rstrip('.')]+[x[0].lower()+x[1:] if not re.match(r'^[A-Z]{2,}',x) else x for x in [y.rstrip('.') for y in c[1:]]]
        res.append(', '.join(parts)+'.')
    return res
def label(sentence,L):
    s=sentence
    m=re.match(r'^They (\S+)',s)
    if m:
        v=m.group(1); nv=VERB.get(v,v if v.endswith('s') else v+'s')
        s=re.sub(r'^They \S+',L+' '+nv,s,1)
    s=re.sub(r'^(She|He)\b',L,s)
    s=re.sub(r'^(Her|His|Their)\b',L+"'s",s)
    s=re.sub(r'^This person\b',L,s)
    s=re.sub(r', and (she|he) ',', and '+L+' ',s)
    s=re.sub(r', and they (\S+)',lambda m:', and '+L+' '+VERB.get(m.group(1),m.group(1)+'s'),s)
    s=re.sub(r"\b(she|he)\b",L,s)
    s=re.sub(r"\b(her|his|their)\b(?=\s+[a-z])",L+"'s",s)
    s=re.sub(r"\bthey (\S+)",lambda m:L+' '+VERB.get(m.group(1),m.group(1)),s)
    return s
def struct(N,i,spec,seed):
    rng,E=mk(seed)
    st,narr,sty,light,cam,ppl=spec
    sett=setting(rng,E,st)
    fixed=2600+N*480
    per=(MAXC-len(sett)-len(narr)-fixed)//N
    per=min(per,3500)
    P=[]
    for pp in ppl:
        o,a=pp.split('|'); P.append((person(rng,E,per),o,a))
    return dict(N=N,narr=narr,sty=STY[sty],light=light,cam=CAM[cam],sett=sett,P=P)
def head(d,sett):
    N=d['N']
    return [OPENER,"Square 1:1 frame.","A fully detailed group scene with exactly %s people, all clearly visible and complete from the top of the head to the soles of the feet, standing or seated within the square frame with nothing cropped by the edges, a little space around the group, and every person's face, hands and feet fully shown."%NUM[N-2],d['narr'],d['sty'],d['cam'],d['light'],"The setting, described in detail, follows. "+sett]
def tail(N,named=False):
    t="Together the group fills the square frame in a balanced composition, with natural overlap in depth where people stand close, no one hidden behind another so that each full body is readable, consistent proportions and anatomy for every person, natural hands with five fingers each, and relaxed, believable body language. All %d people are different individuals with different ages, backgrounds, builds and styles, rendered with the same sharp focus, true colours and fine detail from head to toe."%N
    return [t,"Keep the same square 1:1 aspect ratio and keep every person entirely inside the frame."]
def vA(d):
    N=d['N'];parts=[]
    for j,(desc,o,a) in enumerate(d['P']):
        an="The %s person, %s,"%(ORD[j],POS[N][j])
        parts.append("%s is described as follows. %s %s is dressed in %s. %s %s."%(an,desc,an,o,an,a))
    return head(d,d['sett'])+["The people are now described one by one from left to right across the frame."]+parts+tail(N)
def vB(d):
    N=d['N'];parts=[]
    sett=' '.join(chunk(sents(d['sett']),45))
    for j,(desc,o,a) in enumerate(d['P']):
        an="The %s person, %s,"%(ORD[j],POS[N][j])
        ss=sents(desc)
        first=ss[0]
        blk=[an+" is described as follows. "+first]+chunk(ss[1:],50)
        blk.append("%s is dressed in %s, and %s."%(an,o,a))
        parts.append(' '.join(blk))
    return head(d,sett)+["The people are now described one by one from left to right across the frame."]+parts+tail(N)
def vC(d):
    N=d['N'];parts=[]
    names=', '.join('Person '+LET[k] for k in range(N))
    for j,(desc,o,a) in enumerate(d['P']):
        L='Person '+LET[j]
        ss=[label(x,L) for x in sents(desc)]
        parts.append("%s is the person %s. %s %s is dressed in %s. %s %s."%(L,POS[N][j],' '.join(ss),L,o,L,a))
    intro="The people are named %s from left to right across the frame, and each name is used for everything described about that person."%names
    return head(d,d['sett'])+[intro]+parts+tail(N)
def fin(parts):
    t=' '.join(parts); t=re.sub(r'\s+',' ',t).replace('..','.').replace(' ,',',').replace(',,',',')
    return t
if __name__=='__main__':
    ALL={2:S2,3:S3,4:S4,5:S5,6:S6,7:S7,8:S8}
    out='/mnt/user-data/outputs';tsv=[]
    for N,L in ALL.items():
        lines=[]
        for i,sp in enumerate(L):
            d=struct(N,i,sp,N*100+i)
            for v,fn in (('A',vA),('B',vB),('C',vC)):
                t=fin(fn(d)); lines.append(t); tsv.append('%d\t%d\t%s\t%s'%(N,i+1,v,t))
                assert len(t)//4<3900,(N,i,v,len(t))
        open(f'{out}/Guyanonymous_Wildcards_scenes_{N}_people_variants.txt','w').write('\n'.join(lines))
        print(N,[len(l)//4 for l in lines])
    open(f'{out}/Guyanonymous_Wildcards_scenes_variants_labelled.tsv','w').write('people\tprompt\tversion\ttext\n'+'\n'.join(tsv))
