import sys, re, json
sys.argv=['x']
import v75_showcase as V
S=V.build(0)
od='/mnt/user-data/outputs/'
lines={0:[],1:[]}; key=['id\ttitle\tratio\tsize_1024eq\tsize_1408eq\tchars\tseed\tcheck']; 
NOTE={'G08':'archetypal figures, no named deities','G05':'nine creatures; long cells','G11':'nine radiators; object details are generic and cell text is long','S19':'square shed scene; verify the odd-item mix reads as a shed','S17':'empty mall; text is plain, no legible writing expected'}
for n,(i,t,ratio,text) in enumerate(S):
    sd=7400+n*11; sz=V.sizes(*ratio)
    chk=[]
    if not text[0].isupper(): chk.append('lowercase start')
    if text.count('"')%2: chk.append('odd quotes')
    if '  ' in text or ' ,' in text: chk.append('spacing')
    if len(text)>7000: chk.append('very long')
    for k in (0,1):
        w,h=sz[k]; lines[k].append('--prompt "%s" --steps 50 --cfg_scale 3.75 --seed %d --width %d --height %d'%(text.replace('"','\\"'),sd,w,h))
    key.append('\t'.join([i,t,'%d:%d'%ratio,'%dx%d'%sz[0],'%dx%d'%sz[1],str(len(text)),str(sd),'; '.join(chk) or 'ok '+NOTE.get(i,'')]))
open(od+'Guyanonymous_Wildcards_v75_showcase_1024.txt','w').write('\n'.join(lines[0])+'\n')
open(od+'Guyanonymous_Wildcards_v75_showcase_1408.txt','w').write('\n'.join(lines[1])+'\n')
open(od+'Guyanonymous_Wildcards_v75_showcase_key.tsv','w').write('\n'.join(key)+'\n')
print('\n'.join(key))
