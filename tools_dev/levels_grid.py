import sys,random,re
sys.argv=['x']
import body_showcase as B
g=B.g
WC='/home/claude/w/wildcards/'
def rd(n): return [l.strip() for l in open(WC+n+'.txt') if l.strip()]
PL=rd('apose_place'); LT=rd('apose_light')
def distinct(r):
    return r.sample(PL,9), r.sample(LT,9)

def wrap(c,n,solo):
    pre='This panel is a self-contained photograph of %s, taken in its own room under its own light, and nothing from any other panel appears in it. '%('one person alone' if solo else 'exactly two people')
    post=' Each person in this panel has one head, two arms and two legs, and every hand, foot and limb belongs to the person it is described with. Everything outside this panel, including its people, room and light, is different from this one.'
    return pre+c+post
def cast(l):
    t=l.lower()
    if re.match(r'two women',t): return 'ww'
    if re.match(r'two men',t): return 'mm'
    if (re.search(r'\bwoman\b',t) and re.search(r'\bman\b',t)) or 'a man and a woman' in t or 'a woman and a man' in t: return 'wm'
    return None
nk=lambda l: re.sub(r'\s+',' ',re.sub(r'__\w+__,?','',l.lower()).replace(',',''))[:35]
ORD=B.ORD; o1=[];o2=[];b1=[];b2=[]
for L in range(1,7):
    SEED=int.from_bytes(__import__('os').urandom(4),'big'); r=random.Random(SEED)
    pools={k:rd('adult_l%d_panel_%s'%((5 if (L==6 and r.random()<0.6) else L),k)) for k in ('wm','ww','mm')}
    for k in pools: r.shuffle(pools[k])
    mf=rd('adult_l%d_masturbation_f'%L); mm_=rd('adult_l%d_masturbation_m'%L); r.shuffle(mf); r.shuffle(mm_)
    typed=None
    if L>=5:
        T={}
        for k in T: r.shuffle(T[k])
        pass
    order=[('wm',0),('ww',0),('mm',0),('mf',0),('mm_',0),('wm',1),('ww',1),('mm',1),('mf' if L%2 else 'mm_',1)]
    cells=[]; seen=set(); PLS,LTS=distinct(r)
    if L>=5:
        kinds=r.sample(['wm_vaginal','wm_oral','wm_anal','ww_oral','ww_scissor','ww_other','mm_oral','mm_anal','mm_hand','mf','mm_'],9)
        order=[(kk,0) for kk in kinds]
    else:
        while True:
            order=[(r.choice(['wm','ww','mm','mf','mm_','wm','ww','mm']),0) for _ in range(9)]
            ks=[k for k,_ in order]
            if sum(k in ('mf','mm_') for k in ks)<=2 and ks.count('wm')<=3 and ks.count('ww')<=3 and ks.count('mm')<=3 and ks.count('mf')<=1 and ks.count('mm_')<=1: break
        used_solo=set()
    for k,i in order:
        if k=='mf': t=r.choice(mf if not(L==6 and r.random()<0.5) else rd('adult_l5_masturbation_f'))
        elif k=='mm_': t=r.choice(mm_ if not(L==6 and r.random()<0.5) else rd('adult_l5_masturbation_m'))
        elif k in T if L>=5 else False: t=r.choice(T[k]) if k in T else r.choice(rd('adult_l%d_panel_%s'%((5 if (L==6 and r.random()<0.6) else L),k)))
        else:
            if L>=5: t=r.choice(rd('adult_l%d_panel_%s'%((5 if (L==6 and r.random()<0.6) else L),k)))
            else: t=next((x for x in pools[k] if nk(x) not in seen),r.choice(pools[k])); seen.add(nk(t))
        t=t if 'The scene is in' in t or '__apose_place__' in t else t.replace(' The light is',' The scene is in __apose_place__. The light is')
        t=t.replace('__apose_place__',PLS[len(cells)] if len(cells)<9 else PLS[0]).replace('__apose_light__',LTS[len(cells)] if len(cells)<9 else LTS[0]); c=g(t,r).replace(', .','.').replace(',.','.').strip(); c=c[0].upper()+c[1:]; cells.append(wrap(c,len(cells),k in ('mf','mm_'))); continue
    for k,i in []:
        t=mf[i] if k=='mf' else mm_[i] if k=='mm_' else pools[k][i%len(pools[k])]
        t=t.replace('__apose_place__',PLS[len(cells)] if len(cells)<9 else PLS[0]).replace('__apose_light__',LTS[len(cells)] if len(cells)<9 else LTS[0]); c=g(t,r).replace(', .','.').replace(',.','.').strip(); cells.append(c[0].upper()+c[1:])
    head='A grid of 9 equal photographic panels arranged in three rows of three columns, separated by thin plain white gaps. Every panel is a separate scene with its own people, and the people in one panel do not appear in any other panel. '
    t=head+' '.join('The %s panel: %s%s'%(ORD[i],c,'' if c.endswith('.') else '.') for i,c in enumerate(cells))
    assert '__' not in t
    tb=head+' '.join('The %s panel: (%s)'%(ORD[i],c.rstrip('.')+'.') for i,c in enumerate(cells))
    for lst,sz in ((b1,1024),(b2,1408)):
        lst.append('--prompt "%s" --steps 50 --cfg_scale 3.75 --seed %d --width %d --height %d'%(tb,SEED,sz,sz))
    for lst,sz in ((o1,1024),(o2,1408)):
        lst.append('--prompt "%s" --steps 50 --cfg_scale 3.75 --seed %d --width %d --height %d'%(t,SEED,sz,sz))
# seventh grid: kink
r=random.Random(int.from_bytes(__import__('os').urandom(4),'big'))
K={k:rd('kink_panel_'+k) for k in ('wm','ww','mm','f','m')}
for k in K: r.shuffle(K[k])
seq=[('wm',0),('ww',0),('mm',0),('f',0),('wm',1),('m',0),('ww',1),('mm',1),('wm',2)]
cells=[]; PLS,LTS=distinct(r)
for n_,(k,i) in enumerate(seq):
    c=g(K[k][i].replace('__apose_place__',PLS[n_]).replace('__apose_light__',LTS[n_]),r).replace(', .','.').replace(',.','.').strip(); c=re.sub(r'([.,;]) (a|an) (man|woman|second)',lambda m:m.group(1)+' '+m.group(2).capitalize()+' '+m.group(3),c) if False else re.sub(r'\. (a) (man|woman)',lambda m:'. A '+m.group(2),c); cells.append(wrap(c[0].upper()+c[1:],n_,k in ('f','m')))
t=head+' '.join('The %s panel: %s%s'%(ORD[i],c,'' if c.endswith('.') else '.') for i,c in enumerate(cells))
assert '__' not in t
ks=r.randrange(10**6); tb=head+' '.join('The %s panel: (%s)'%(ORD[i],c.rstrip('.')+'.') for i,c in enumerate(cells))
b1.append('--prompt "%s" --steps 50 --cfg_scale 3.75 --seed %d --width 1024 --height 1024'%(tb,r.randrange(10**6))); b2.append(b1[-1].replace('--width 1024 --height 1024','--width 1408 --height 1408'))
o1.append('--prompt "%s" --steps 50 --cfg_scale 3.75 --seed %d --width 1024 --height 1024'%(t,ks))
o2.append('--prompt "%s" --steps 50 --cfg_scale 3.75 --seed %d --width 1408 --height 1408'%(t,ks))
KINK=1
open('/mnt/user-data/outputs/Guyanonymous_Wildcards_adult_levels_grid_1024.txt','w').write('\n'.join(o1))
open('/mnt/user-data/outputs/Guyanonymous_Wildcards_adult_levels_grid_1408.txt','w').write('\n'.join(o2))
print([len(x) for x in o1]); print(re.findall(r'semen[^.]{0,120}',o1[5])[:2]); print(re.findall(r'The fifth panel: .{0,500}',o1[5])[0])

open('/mnt/user-data/outputs/Guyanonymous_Wildcards_adult_levels_grid_bracketed_1024.txt','w').write('\n'.join(b1))
open('/mnt/user-data/outputs/Guyanonymous_Wildcards_adult_levels_grid_bracketed_1408.txt','w').write('\n'.join(b2))
