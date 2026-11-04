import sys, re, math
import photo50 as I
import illus50
sys.path.insert(0, '.')
from v74_showcase import sizes
S = I.build(); od = '/mnt/user-data/outputs/'
lines = {0: [], 1: []}; key = ['id\tstyle\tratio\tsize_1024eq\tsize_1408eq\tchars\tseed\tcheck']
KIDS = re.compile(r'\b(child|children|kid|kids|boy|girl|teen|teenage|baby|toddler|student)\b', re.I)
for n, (i, t, ratio, text) in enumerate(S):
    sd = 9300 + n * 7; sz = sizes(*ratio); chk = []
    if KIDS.search(text): chk.append('minor word')
    if illus50.LB.search(text): chk.append('nudity word')
    if text.count('"') % 2: chk.append('odd quotes')
    if '  ' in text or ' ,' in text: chk.append('spacing')
    if len(text) > 4400: chk.append('long')
    for k in (0, 1):
        w, h = sz[k]; lines[k].append('--prompt "%s" --steps 50 --cfg_scale 3.75 --seed %d --width %d --height %d' % (text.replace('"', '\\"'), sd, w, h))
    key.append('\t'.join([i, t, '%d:%d' % ratio, '%dx%d' % sz[0], '%dx%d' % sz[1], str(len(text)), str(sd), '; '.join(chk) or 'ok']))
open(od + 'Guyanonymous_Wildcards_photography50_1024.txt', 'w').write('\n'.join(lines[0]) + '\n')
open(od + 'Guyanonymous_Wildcards_photography50_1408.txt', 'w').write('\n'.join(lines[1]) + '\n')
open(od + 'Guyanonymous_Wildcards_photography50_key.tsv', 'w').write('\n'.join(key) + '\n')
print('\n'.join(key))
