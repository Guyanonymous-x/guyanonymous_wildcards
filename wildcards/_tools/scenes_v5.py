import json,re
OPEN="Sharp, clean, high-resolution photograph with crisp focus, fine detail, accurate natural colour and a clear, high-quality finish."
SCENE=("A square 1:1 group photograph of exactly eight people in a long, narrow Japanese-style living room in the evening, taken from chest height looking slightly down with a 24mm lens so that every person is shown fully from head to toe inside the frame, with a small margin around the group. "
"Sliding shoji screens with pale paper panels line the left wall, a long cream sofa stands against the back wall, floor cushions and a wide patterned carpet cover the floor, and a low wooden table in the centre holds a layered white cake with lit candles. A string of plain, blank cream triangular flags hangs overhead. "
"Warm lamplight, evening window light and candle glow give soft golden highlights on faces and gentle shadows. The mood is a warm, candid family party with natural expressions.")
P=[
("Far left, standing on open floor with both feet visible","a 40-year-old man with tan Syrian Arab skin, a messy textured drop fade of wavy dark hair and a soul patch","a pale blue shirt, grey trousers and slippers","smiling and holding a cake knife"),
("Left of centre, sitting on the sofa","a 77-year-old person with tan skin, collarbone-length shaggy silver-brown hair tucked behind the ears and a thick balbo beard","a patterned long tunic and cardigan with trousers and flat shoes","clapping and laughing"),
("Centre-left, sitting on a floor cushion at the front","a 48-year-old Samoan woman with bronze brown skin and long wavy dark hair tucked behind the ears","a bright red jumper, dark jeans and socks","arms crossed over her knees, looking at the cake"),
("Just left of the middle, standing beside the sofa with feet visible","an 18-year-old young person with a masculine presentation, golden brown skin and loose wavy mid-back-length hair","a smart waistcoat over a white shirt, dark trousers and polished shoes","one hand resting on the back of the sofa"),
("Just right of the middle, sitting at the centre of the sofa","a 31-year-old Zimbabwean woman with medium golden-tan skin and black shoulder-length hair with long side-swept bangs under a headscarf","wide printed trousers, a plain top and sandals","holding a wrapped gift in both hands"),
("Centre-right, sitting on the arm of the sofa","a 22-year-old non-binary Tanzanian person with olive skin and hip-length, perfectly straight espresso-brown hair","a plain green hooded top with no print, plain grey joggers and white trainers","grinning"),
("Right of centre, standing on open floor with both feet visible","an 85-year-old man with medium beige skin, a shaved head, a shaved chin, deep wrinkles and a slightly stooped posture","a cream silk shirt with a small flower pin on the lapel, trousers and smart shoes","lifting a glass"),
("Far right, sitting cross-legged on the floor","a 76-year-old Libyan man with very deep brown skin, ash grey wavy hair, a clean-shaven face, thin aged skin and a hunched posture","a faded band t-shirt, jeans and sneakers","holding a party hat"),
]
# boxes in 1024 canvas, absolute x1,y1,x2,y2 then converted to centred yxyx
BX=[(20,90,200,960),(190,300,390,700),(110,480,420,960),(330,200,520,760),(520,330,690,700),(670,330,830,800),(780,150,1000,860),(740,430,1004,900)]
def cb(x1,y1,x2,y2): return [y1-512,x1-512,y2-512,x2-512]
def short():
    t=[OPEN,SCENE]
    for i,(pos,who,out,act) in enumerate(P): t.append("%s, %s, wearing %s, %s."%(pos,who,out,act))
    t.append("The eight people are different individuals fully inside the square frame, with natural hands and relaxed body language, and there are exactly eight people in the image.")
    return ' '.join(t)
def layout():
    items=[]
    for (pos,who,out,act),b in zip(P,BX):
        items.append({"label":"person","caption":"%s, %s, wearing %s, %s."%(pos,who,out,act),"bbox":cb(*b)})
    items+= [
     {"label":"object","caption":"A low wooden table with a layered white cake with lit candles on top.","bbox":cb(380,560,680,860)},
     {"label":"object","caption":"A long cream sofa against the back wall.","bbox":cb(180,320,880,760)},
     {"label":"object","caption":"Sliding shoji screens with pale paper panels on the left wall.","bbox":cb(0,0,380,420)},
     {"label":"object","caption":"A string of plain, blank cream triangular flags hanging overhead.","bbox":cb(100,40,1000,190)}]
    d={"summary":{"meta":["photo"],"canvas":"single","caption":OPEN+" "+SCENE+" Exactly eight people are shown, each fully inside the frame."},"items":items,"bbox_coord_space":"abs_centralized","bbox_format":"yxyx"}
    return json.dumps(d,ensure_ascii=False)
S=short(); J=layout()
assert '\n' not in S and '\n' not in J and '\\' not in J.replace('\\"','')
out='/mnt/user-data/outputs/'
open(out+'Guyanonymous_Wildcards_party_8people_v5_short_and_layout_plain.txt','w').write(S+'\n'+J)
esc=lambda s:s.replace('\\','\\\\').replace('"','\\"')
flags=[]
for name,txt in (('short',S),('layout',J)):
    for st in (50,80):
        for c in (3.25,3.5,3.75): flags.append('--prompt "%s" --steps %d --cfg_scale %s --seed 7800'%(esc(txt),st,c))
open(out+'Guyanonymous_Wildcards_party_8people_v5_short_and_layout_batch_flags.txt','w').write('\n'.join(flags))
print(len(S)//4,len(J)//4,len(flags))
json.loads(J); print(J[:600])
