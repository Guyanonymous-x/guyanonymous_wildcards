import re,sys,random
sys.path.insert(0,'.')
import scenes_gen as G
from scenes_gen import *
from scenes_variants import sents,chunk,VERB,NUM,fin
OUTFIT_MAP=[
("a loose sleeveless linen dress in sage green and leather slides","a loose sleeveless linen tunic in sage green over trousers and leather slides"),
("a flowing patterned dress with a wicker bag and sandals","a flowing patterned tunic over trousers with a wicker bag and sandals"),
("a patterned sundress and cardigan with flat shoes","a patterned long tunic and cardigan with trousers and flat shoes"),
("a long printed skirt, plain top and sandals with a headscarf","wide printed trousers, a plain top and sandals with a headscarf"),
("a flowing blue sundress with a straw hat and flat sandals","a flowing blue tunic over trousers with a straw hat and flat sandals"),
("a long flowing indigo dress with a fringed shawl and ankle boots","a long flowing indigo tunic over trousers with a fringed shawl and ankle boots"),
("a long burgundy skirt, white blouse and low heels","wide burgundy trousers, a white shirt and low shoes"),
("a deep red wrap dress with a thin gold necklace and strappy heels","a deep red wrap-front jacket over trousers with a thin gold necklace and smart shoes"),
("a long black dress with a colourful shawl and low heels","a long black tunic coat over trousers with a colourful shawl and low shoes"),
("a long flowing gown in midnight blue with silver stars and a pointed hat","a long flowing robe in midnight blue with silver stars and a pointed hat"),
("a long layered skirt in rainbow stripes with a fitted black top and ankle bells on bare feet","loose rainbow-striped trousers with a fitted black top and ankle bells on bare feet"),
("a long printed wrap skirt in earthy tones with a fitted black top","wide earth-toned printed trousers with a fitted black top"),
("over a long skirt in a block print pattern","over wide block-print trousers"),
("a patterned wrap dress in orange and navy with a flower crown and flat sandals","a patterned wrap tunic in orange and navy over trousers with a flower crown and flat sandals"),
("an emerald dress with a cream cardigan and boots","an emerald tunic with a cream cardigan, trousers and boots"),
("a long printed dress with a denim jacket and sneakers","a long printed tunic with a denim jacket, trousers and sneakers"),
("a long burgundy knit dress with boots and a chunky scarf","a long burgundy knit tunic with trousers, boots and a chunky scarf"),
("a cropped cardigan over a floral dress with ankle boots","a cropped cardigan over a floral tunic and trousers with ankle boots"),
("an olive green shirtdress with a thin belt and block-heeled shoes","a long olive green shirt with a thin belt, trousers and smart shoes"),
("a sparkling embroidered sari-style wrap in deep blue with a woollen shawl and closed sandals","a sparkling embroidered deep blue wrap jacket with a woollen shawl, trousers and closed sandals"),
("a fitted black leotard with a sheer wrap skirt and soft ballet shoes","a fitted black dance top and tights with a sheer wrap layer and soft ballet shoes"),
("pleated midi skirt","pleated wide trousers"),("long skirt and sturdy shoes","wide long trousers and sturdy shoes"),
("long pleated skirt","long pleated trousers"),
("dark skirt and flat shoes","dark trousers and flat shoes"),
("a cream silk blouse tucked into a long burgundy pleated skirt and low suede heels","a cream silk shirt tucked into long burgundy pleated trousers and low suede shoes"),
("a colourful sports bra-style top","a colourful fitted sports top"),
("a bright coral blouse, black skirt and heels","a bright coral shirt, black trousers and shoes"),
("strappy heels","smart shoes"),("block-heeled shoes","smart shoes"),
("blouse","shirt"),("corsage","flower pin on the lapel"),("heels","smart shoes"),
]
def neutral(o):
    for a,b in OUTFIT_MAP: o=o.replace(a,b)
    assert not re.search(r'\b(dress|skirt|gown|sundress|blouse|heels|leotard)\b',o),o
    return o
ACT_MAP={"dances at the centre with a skirt gathered in both hands and a joyful expression":"dances at the centre with a loose trouser leg lifted and a joyful expression","stands behind the sofa at the centre-left with a hand on the back of it":"stands beside the sofa at the centre-left with a hand resting on the sofa back",
"stands behind the bar at the far left shaking a cocktail shaker over one shoulder":"stands at the end of the bar at the far left shaking a cocktail shaker over one shoulder",
"stands at the far left behind a stall weighing vegetables on a scale":"stands at the far left beside a stall weighing vegetables on a scale",
"sits at the centre behind a pile of fabric rolls":"sits at the centre beside a pile of fabric rolls",
"stands behind their chair at the left":"stands beside their chair at the left"}
def act(a):
    for k,v in ACT_MAP.items(): a=a.replace(k,v)
    return a
EXTRA={
(2,0):"A butcher-block worktop holds a wooden board of sliced vegetables, a copper pot steams on a gas hob, open shelves display ceramic bowls and jars of dried herbs, and a window above the sink shows a leafy yard.",
(2,1):"The bridge has a curved iron railing painted dark green, a walkway of worn stone slabs, old lamp posts with round glass globes, and a wide river below reflecting the lights of the city.",
(2,2):"Tall oak bookshelves rise behind a long reading table of dark wood, with brass-shaded green lamps, leather-bound volumes, a rolling ladder on a rail and a worn patterned rug on the floor.",
(2,3):"A heavy timber workbench holds clamps, chisels, a vice and curled wood shavings, pegboard walls display hand tools in rows, and unfinished chairs and planks lean against the back wall.",
(2,4):"Two facing bench seats upholstered in patterned blue fabric flank a narrow fold-down table, luggage racks hold bags above, and large windows show fields and hills moving past.",
(3,0):"A low wooden coffee table holds a board game, mugs and a bowl of snacks, a deep fabric sofa and floor cushions surround it, a bookcase and a floor lamp stand against the wall, and a rug covers the floorboards.",
(3,1):"Wooden market stalls under striped canvas awnings display crates of oranges, tomatoes, leafy greens and cut flowers, with hand-lettered price tags, hanging scales and woven baskets stacked beside them.",
(3,2):"A full-length mirror covers the long wall, a wooden barre runs along the opposite side, speakers sit in the corner, and the sprung wooden floor shows faint scuff marks from practice.",
(3,3):"A narrow trail of packed earth runs along a ridge with scattered boulders, low shrubs and wildflowers, and a wooden signpost, with a wide valley and layered hills stretching behind.",
(3,4):"A round table with a white cloth is set with wine glasses, small plates, candles in glass holders and a bread basket, with leather chairs around it and a dark wooden bar glowing in the background.",
(4,0):"Rows of wooden desks with chairs face a whiteboard, shelves hold craft supplies, paper models and plants, wall displays show maps and project posters, and tall windows run along one side.",
(4,1):"A wide paved plaza of pale stone has a central stone fountain, wooden benches, small potted trees and café tables, with tall historic buildings with arched windows around the edges.",
(4,2):"A long dark wooden dining table is set with white plates, serving dishes of roast meat, vegetables, bread and bowls of rice, candles and a floral centrepiece, under a glass chandelier with a sideboard behind.",
(4,3):"Rows of food stalls with steaming woks, charcoal grills and glass cases of dumplings and skewers, plastic stools, strings of lanterns and bulbs overhead, and narrow lanes of wet pavement reflecting the lights.",
(4,4):"A lakeshore of pebbles and grass has a green dome tent, a small gas stove on a flat stone, folding chairs, backpacks and a coiled rope, with tall pines along the far bank and mountains beyond.",
(5,0):"White desks with monitors, plants and notice boards fill the floor, with a glass-walled meeting corner, a wall chart of sticky notes, and a window wall with a view of city rooftops.",
(5,1):"Colourful bunting and paper lanterns hang between lamp posts, food carts sell grilled corn and sweets, and painted wooden stages and long trestle tables line a wide street closed to traffic.",
(5,2):"A long glossy table is surrounded by padded chairs, with printed charts, laptops and glasses of water spread across it, a wall-mounted screen at one end and a whiteboard covered in diagrams.",
(5,3):"A wide green lawn has scattered mature trees, a gravel path curving along one side, a wooden bench, a picnic blanket with bags and water bottles, and a pond in the distance.",
(5,4):"Two small wooden tables pushed together hold cups, plates of pastries and phones, with a long counter, an espresso machine, shelves of ceramic mugs and hanging plants in the background.",
(6,0):"A rubber-matted floor holds rows of folded exercise mats, racks of dumbbells and kettlebells line one wall, with a long mirror, climbing ropes at the back and tall windows.",
(6,1):"A covered platform has yellow safety lines at its edge, steel benches, a large departure board, a timetable sign, a bin and a vending machine, with rail tracks and a signal beyond.",
(6,2):"A long wooden bar with a brass foot rail and rows of bottles on lit glass shelves, high stools, small round tables, exposed brick walls and hanging pendant lamps with warm filament bulbs.",
(6,3):"A stone quay has iron bollards, stacked fish crates and coiled ropes, weathered fishing boats are moored alongside, nets hang over rails, and seabirds sit on posts above the grey-green harbour.",
(6,4):"Wooden easels hold canvases in progress, long tables carry brushes, paint tubes and jars, a clay sculpture sits on a turntable, finished paintings lean on the walls and a large skylight is overhead.",
(7,0):"A very long table has a white tablecloth, candles in glass holders, wine bottles and glasses, platters of shared dishes and baskets of bread, in a restaurant with wood panelling, framed pictures and warm pendant lamps.",
(7,1):"Long folding tables carry covered dishes and pitchers, a barbecue sends up smoke, balloons are tied to fence posts, chalk drawings cover the road, and a row of terraced houses with small front gardens lines the street.",
(7,2):"Rows of wooden desks, shelves stacked with finished posters and cardboard models, a large world map on the wall, a whiteboard at the front and tall windows with green blinds.",
(7,3):"A rocky lookout platform of flat stone has a low wooden rail, tough grass, scattered boulders and a signpost, with a wide valley, a winding river and ridges fading into haze.",
(7,4):"A small makeshift stage of wooden pallets is draped with fabric, with painted backdrops, a trunk of props, hanging colourful flags, and a grassy festival field with tents and food stalls behind.",
(8,0):"Sliding shoji screens with pale paper panels line one wall, a low wooden table holds a layered white birthday cake, a wide patterned carpet covers the floor with floor cushions, a long cream sofa and plain bunting flags hung overhead.",
(8,1):"A high covered market hall has an iron roof and skylights, wooden stalls piled with fruit, vegetables, cheese and flowers, hanging lamps, crates and chalkboard price signs.",
(8,2):"Floor-to-ceiling bookshelves with ladders, a long reading table, leather armchairs arranged in a loose circle, brass reading lamps, a patterned carpet and arched windows.",
(8,3):"Rows of concrete stands with plastic seats, painted railings, hanging team banners and a pitch of bright green grass far below, with a stadium roof overhead.",
(8,4):"A bright studio has a polished wooden floor, mats in two rows, a wall of mirrors, bamboo blinds, plants, folded blankets and blocks stacked in a corner.",
}
NAMES=["Kavuz","Rilom","Domex","Zenku","Tulap","Bexil","Narvu","Gokel"]
def clean_desc(t):
    ss=sents(t)
    ss=[s for s in ss if not re.search(r'hair is moving|hair moving',s)]
    return ' '.join(ss)
def person2(rng,E,budget):
    for _ in range(60):
        g=rng.choice(['__any_create_random_person_w_clothes__']+['__any_person_age%s_w_clothes__'%b for b in BANDS])
        t=E(g)
        if 'bald' in t.lower() and re.search(r'styled as|ponytail|bob|braid|curl',t): continue
        ss=sents(t)
        if re.search(r'\bwear',ss[-1]) and not re.search(r'hair|makeup',ss[-1]): ss=ss[:-1]
        ss=[s for s in ss if not re.search(r'hair is moving|hair moving',s)]
        if not re.search(r'\d+ years old',' '.join(ss)): continue
        prot=lambda x:bool(re.search(r'years old|nationality|background',x))
        L=lambda: sum(len(s)+1 for s in ss)
        for pat in DROP:
            if L()<=budget: break
            ss=[s for k,s in enumerate(ss) if prot(s) or k==0 or not re.search(pat,s)]
        while L()>budget:
            c=[k for k,x in enumerate(ss) if k>0 and not prot(x) and not re.search(r'hair|build|skin|Overall',x)]
            if not c: c=[k for k,x in enumerate(ss) if k>0 and not prot(x) and not re.search(r'hair|build',x)]
            if not c: break
            ss.pop(max(c,key=lambda k:len(ss[k])))
        if L()>budget: continue
        return ' '.join(ss)
    raise SystemExit('no fit')
def tag(desc):
    ss=sents(desc); age=re.search(r'(\d+) years old',desc)
    g=None
    m=re.match(r'^(?:A|An) ([^.]{3,70})\.$',ss[0])
    if m and not re.search(r'years old|nationality',ss[0]): g=m.group(1)
    if not g:
        m=re.search(r'\b(woman|man|person)\b',ss[0]); g=m.group(1) if m else 'person'
    g=re.sub(r'^(a|an) ','',g)
    VOC=set("very light medium deep dark pale fair warm cool rich golden ruddy olive bronze tan brown beige ebony ivory tawny honey mahogany pink porcelain ashen copper caramel espresso cocoa sandy".split())
    sk=None
    for m in re.finditer(r"([a-z]+(?:[- ][a-z]+){0,3}) skin\b",desc):
        ws=re.split(r"[- ]",m.group(1))
        k=len(ws)
        while k>0 and ws[k-1] in VOC: k-=1
        ph=m.group(1).split(' ')
        good=[w for w in re.split(r"(?<= )",m.group(1))]
        tail=[w for w in re.split(r"[- ]",m.group(1))]
        # keep trailing run of vocabulary words
        words=m.group(1).split(' ')
        run=[]
        for w in reversed(words):
            if all(p in VOC for p in w.split('-')): run.insert(0,w)
            else: break
        if run: sk=' '.join(run)+' skin'; break
    if sk: g=g+(' and ' if ' with ' in g else ' with ')+sk
    n=age.group(1) if age else ''
    art='an' if re.match(r'(8|11|18)',n) else 'a'
    return ('%s %s-year-old %s'%(art,n,g)) if age else 'a '+g
def struct(N,i,spec,seed):
    rng,E=mk(seed)
    st,narr,sty,light,cam,ppl=spec
    sett=setting(rng,E,st)+' '+EXTRA[(N,i)]
    fixed=3300+N*520+len(sett)+len(narr)
    per=min((MAXC-fixed)//N,3300)
    P=[]
    for pp in ppl:
        o,a=pp.split('|'); d=person2(rng,E,per); P.append((d,neutral(o),act(a),tag(d)))
    return dict(N=N,narr=narr,sty=STY[sty],light=light,cam=CAM[cam],sett=sett,P=P)
def head(d,sett,N):
    return [OPENER,"Square 1:1 frame.","A fully detailed group scene with exactly %s people, all clearly visible and complete from the top of the head to the soles of the feet, standing or seated within the square frame with nothing cropped by the edges, a little space around the group, and every person's face, hands and feet fully shown."%NUM[N-2],d['narr'],d['sty'],d['cam'],d['light'],"The setting, described in detail, follows. "+sett,"Any banners and decorations are blank, plain bunting flags and simple shapes with smooth, unmarked surfaces."]
def tail(N):
    return ["Together the group fills the square frame in a balanced composition, with natural overlap in depth where people stand close, no one hidden behind another so that each full body is readable, consistent proportions and anatomy for every person, natural hands with five fingers each, and relaxed, believable body language. All %d people are different individuals with different ages, backgrounds, builds and styles, rendered with the same sharp focus, true colours and fine detail from head to toe."%N,
 "There are exactly %s people in the image, no more and no fewer, and no other person, mannequin, reflection or portrait of a person appears anywhere."%NUM[N-2],
 "Leave a clear margin of floor and wall between the outer people and the edges of the frame, and keep the same square 1:1 aspect ratio with every person entirely inside the frame."]
def pos(N,j): return "The %s person, %s,"%(ORD[j],POS[N][j])
def vA(d):
    N=d['N'];p=[]
    for j,(desc,o,a,t) in enumerate(d['P']):
        an=pos(N,j)
        p.append("%s is described as follows. %s %s %s, is dressed in %s. %s %s."%(an,desc,an,t,o,an,a))
    return head(d,d['sett'],N)+["The people are now described one by one from left to right across the frame."]+p+tail(N)
def vB(d):
    N=d['N'];p=[]
    sett=' '.join(chunk(sents(d['sett']),45))
    for j,(desc,o,a,t) in enumerate(d['P']):
        an=pos(N,j); ss=sents(desc)
        blk=[an+" is described as follows. "+ss[0]]+chunk(ss[1:],50)
        blk.append("%s %s, is dressed in %s, and %s."%(an,t,o,a))
        p.append(' '.join(blk))
    return head(d,sett,N)+["The people are now described one by one from left to right across the frame."]+p+tail(N)
def lab(s,L):
    m=re.match(r'^They (\S+)',s)
    if m:
        v=m.group(1); s=re.sub(r'^They \S+',L+' '+VERB.get(v,v if v.endswith('s') else v+'s'),s,count=1)
    s=re.sub(r'^(She|He)\b',L,s); s=re.sub(r'^(Her|His|Their)\b',L+"'s",s); s=re.sub(r'^This person\b',L,s)
    s=re.sub(r', and (she|he) ',', and '+L+' ',s)
    s=re.sub(r', and they (\S+)',lambda m:', and '+L+' '+VERB.get(m.group(1),m.group(1)+'s'),s)
    s=re.sub(r"\b(she|he)\b",L,s); s=re.sub(r"\b(her|his|their)\b(?=\s+[a-z])",L+"'s",s)
    s=re.sub(r"\bthey (\S+)",lambda m:L+' '+VERB.get(m.group(1),m.group(1)),s)
    return s
def named(d,labels,intro_fmt,pre):
    N=d['N'];p=[]
    for j,(desc,o,a,t) in enumerate(d['P']):
        L=pre+labels[j]
        ss=[lab(x,L) for x in sents(desc)]
        p.append("%s is the person %s. %s %s, %s, is dressed in %s. %s %s."%(L,POS[N][j],' '.join(ss),L,t,o,L,a))
    names=', '.join(pre+labels[k] for k in range(N))
    return head(d,d['sett'],N)+[intro_fmt%names]+p+tail(N)
def vC(d): return named(d,list("ABCDEFGH"),"The people are named %s from left to right across the frame, and each name is used for everything described about that person.","Person ")
def vD(d): return named(d,NAMES,"The people are named %s from left to right across the frame, and each name is used for everything described about that person.","")
LORA="<lora:MOSSwSh4rpD3tails:1>, Sh4rpD3tails. "
STEPS=[50,75]; CFGS=[3,3.25,3.5,4]
if __name__=='__main__':
    ALL={2:S2,3:S3,4:S4,5:S5,6:S6,7:S7,8:S8}
    out='/mnt/user-data/outputs'; tsv=[];mx=0
    for N,L in ALL.items():
        plain=[];flag=[]
        for i,sp in enumerate(L):
            d=struct(N,i,sp,N*100+i); seed=7000+N*100+i*10
            for v,fn in (('A',vA),('B',vB),('C',vC),('D',vD)):
                t=fin(fn(d)); assert '"' not in t and ' --' not in t and '\n' not in t
                mx=max(mx,len(t)); assert len(t)+len(LORA)<15200,(N,i,v,len(t))
                plain.append(t)
                for s in STEPS:
                    for c in CFGS:
                        flag.append('--prompt "%s%s" --steps %d --cfg_scale %s --seed %d'%(LORA,t,s,c,seed))
                        tsv.append('%d\t%d\t%s\t%d\t%s\t%d'%(N,i+1,v,s,c,seed))
        open(f'{out}/Guyanonymous_Wildcards_scenes_{N}_people_v2_plain_4versions.txt','w').write('\n'.join(plain))
        open(f'{out}/Guyanonymous_Wildcards_scenes_{N}_people_v2_batch_flags.txt','w').write('\n'.join(flag))
        print(N,len(plain),len(flag))
    open(f'{out}/Guyanonymous_Wildcards_scenes_v2_batch_index.tsv','w').write('people\tprompt\tversion\tsteps\tcfg\tseed\n'+'\n'.join(tsv))
    print('max chars',mx,'est tokens',(mx+len(LORA))//4)
