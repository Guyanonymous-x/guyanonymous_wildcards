import sys, re, json
sys.argv=['x']
import v79_showcase as V
S=V.build(0)
od='/mnt/user-data/outputs/'
lines={0:[],1:[]}; key=['id\ttitle\tratio\tsize_1024eq\tsize_1408eq\tchars\tseed\tcheck']; 
NOTE={'S04':'check the lettering M. HALE, INVESTIGATIONS renders','S07':'check THE BLUE ROOM renders','S14':'check LOG OF THE SEA WOLF renders','S21':'check TOP SECRET renders','G14':'four e-reader designs, check each differs','G15':'four phone designs, check each differs'}
for n,(i,t,ratio,text) in enumerate(S):
    sd=7900+n*11; sz=V.sizes(*ratio)
    chk=[]
    if not text[0].isupper(): chk.append('lowercase start')
    if text.count('"')%2: chk.append('odd quotes')
    if '  ' in text or ' ,' in text: chk.append('spacing')
    if len(text)>7000: chk.append('very long')
    for k in (0,1):
        w,h=sz[k]; lines[k].append('--prompt "%s" --steps 50 --cfg_scale 3.75 --seed %d --width %d --height %d'%(text.replace('"','\\"'),sd,w,h))
    key.append('\t'.join([i,t,'%d:%d'%ratio,'%dx%d'%sz[0],'%dx%d'%sz[1],str(len(text)),str(sd),'; '.join(chk) or 'ok '+NOTE.get(i,'')]))
open(od+'Guyanonymous_Wildcards_v79_showcase_1024.txt','w').write('\n'.join(lines[0])+'\n')
open(od+'Guyanonymous_Wildcards_v79_showcase_1408.txt','w').write('\n'.join(lines[1])+'\n')
open(od+'Guyanonymous_Wildcards_v79_showcase_key.tsv','w').write('\n'.join(key)+'\n')
print('\n'.join(key))
