import sys,random,re,os
sys.path.insert(0,'.')
from expand import load, expand, clean
from scenes_data import *
from scenes_data2 import *
from scenes_data3 import *
files=load(['/home/claude/w/wildcards'])
OPENER="Ultra-sharp, high-resolution image with crisp focus throughout, fine detail, clean edges, accurate natural colour and no blur, haze, noise or compression artefacts."
MAXC=14300
BANDS=['18_24','25_34','35_44','45_54','55_64','65_74','75_84','85_94','95_120']
POS={2:["on the left side of the frame","on the right side of the frame"],
3:["at the left of the frame","at the centre of the frame","at the right of the frame"],
4:["at the far left of the frame","left of centre","right of centre","at the far right of the frame"],
5:["at the far left of the frame","left of centre","at the centre of the frame","right of centre","at the far right of the frame"],
6:["at the far left of the frame","left of centre, towards the left","at the centre-left","at the centre-right","right of centre","at the far right of the frame"],
7:["at the far left of the frame","left of centre","at the centre-left","at the centre of the frame","at the centre-right","right of centre","at the far right of the frame"],
8:["at the far left of the frame","left of centre","at the centre-left","just left of the middle","just right of the middle","at the centre-right","right of centre","at the far right of the frame"]}
ORD=["first","second","third","fourth","fifth","sixth","seventh","eighth"]
DROP=[r'hands show|hands are|hands have',r'Above the torso',r'At the forehead',r'Up close',r'There are faint|There are subtle',r'The nose shows',r'mouth has|mouth shows|mouth is',r'proportions',r'Her torso|His torso|Their torso|torso shows',r'Around the eyes',r'build and']
def mk(seed):
    rng=random.Random(seed)
    E=lambda t:' '.join(clean(expand(files,t,rng)).split())
    return rng,E
def person(rng,E,budget):
    for _ in range(40):
        g=rng.choice(['__any_create_random_person_w_clothes__']+['__any_person_age%s_w_clothes__'%b for b in BANDS])
        t=E(g)
        if 'bald' in t.lower() and re.search(r'styled as|ponytail|bob|braid|curl',t): continue
        sents=re.split(r'(?<=\.)\s+',t)
        if re.search(r'\bwear',sents[-1]) and not re.search(r'hair|makeup',sents[-1]): sents=sents[:-1]
        for pat in DROP:
            if sum(len(s)+1 for s in sents)<=budget: break
            sents=[s for s in sents if not re.search(pat,s)]
        while sum(len(s)+1 for s in sents)>budget:
            c=[k for k,x in enumerate(sents) if k>0 and not re.search(r'hair|build|skin|Overall',x)]
            if not c: c=[k for k,x in enumerate(sents) if k>0 and not re.search(r'hair|build',x)]
            if not c: break
            sents.pop(max(c,key=lambda k:len(sents[k])))
        if sum(len(s)+1 for s in sents)>budget: continue
        return ' '.join(sents)
    raise SystemExit('no person fit')
def setting(rng,E,spec):
    k,key=spec
    t=E({'room':'__room_%s_prompt_full__'%key if key else '','city':'__city_%s_empty_prompt__'%key if key else '','land':'__land_prompt__'}[k])
    if k=='room': t=re.split(r' It contains ',t)[0]
    t=' '.join(x for x in re.split(r'(?<=\.)\s+',t) if not re.match(r'(No people are visible|The light comes from|The light is)',x))
    return t
def build(N,i,spec,seed):
    rng,E=mk(seed)
    st,narr,sty,light,cam,ppl=spec
    assert len(ppl)==N,(N,i,len(ppl))
    sett=setting(rng,E,st)
    head=[OPENER,"Square 1:1 frame.",
      "A fully detailed group scene with exactly %s people, all clearly visible and complete from the top of the head to the soles of the feet, standing or seated within the square frame with nothing cropped by the edges, a little space around the group, and every person's face, hands and feet fully shown."%(["two","three","four","five","six","seven","eight"][N-2]),
      narr, STY[sty], CAM[cam], light,
      "The setting, described in detail, follows. "+sett,
      "The people are now described one by one from left to right across the frame."]
    tail=["Together the group fills the square frame in a balanced composition, with natural overlap in depth where people stand close, no one hidden behind another so that each full body is readable, consistent proportions and anatomy for every person, natural hands with five fingers each, and relaxed, believable body language. All %d people are different individuals with different ages, backgrounds, builds and styles, rendered with the same sharp focus, true colours and fine detail from head to toe."%N,
      "Keep the same square 1:1 aspect ratio and keep every person entirely inside the frame."]
    fixed=sum(len(x)+1 for x in head+tail)+N*420
    per=(MAXC-fixed)//N
    parts=[]
    for j,pp in enumerate(ppl):
        outfit,action=pp.split('|')
        d=person(rng,E,per)
        a="The %s person, %s,"%(ORD[j],POS[N][j])
        parts.append("%s is described as follows. %s %s is dressed in %s. %s %s."%(a,d,a,outfit,a,action))
    txt=' '.join(head+parts+tail)
    txt=re.sub(r'\s+',' ',txt).replace('..','.').replace(' ,',',')
    return txt
if __name__=='__main__':
    out='/mnt/user-data/outputs'
    ALL={2:S2,3:S3,4:S4,5:S5,6:S6,7:S7,8:S8}
    for N,L in ALL.items():
        assert len(L)==5,N
        lines=[build(N,i,s,N*100+i) for i,s in enumerate(L)]
        for l in lines:
            assert '\n' not in l and '__' not in l and not re.search(r'[{}|]',l),(N,l[:80])
        open(f'{out}/Guyanonymous_Wildcards_scenes_{N}_people.txt','w').write('\n'.join(lines))
        print(N,[len(l) for l in lines],[len(l)//4 for l in lines])
