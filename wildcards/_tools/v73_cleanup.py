"""v73 cleanup. Idempotent; --restore. Backups in _tools/backup_v72/cleanup/.
 - 'school backpack' -> 'daypack', 'school bags by the door' -> 'bags by the door', 'school satchel' -> 'leather satchel' (adults-only rule)
 - curly quotes -> straight apostrophes (the double curly quotes, if any, are removed); en and em dashes -> comma or hyphen
 - colons in the two files that had them -> comma (frame_ratio keeps '1:1' style ratio text, which is allowed)
 - legacy blank-padded files (mark_tattoo, dem_unique): blank lines -> a single space line each ('none' option), no trailing blank line
"""
import os, re, sys, shutil
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from paths import FINAL
BK = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'backup_v72', 'cleanup')
if '--restore' in sys.argv:
    for f in os.listdir(BK): shutil.copy(os.path.join(BK, f), os.path.join(FINAL, f))
    print('restored', len(os.listdir(BK))); sys.exit()
os.makedirs(BK, exist_ok=True)
SUBS = [(re.compile(r'\bschool backpacks?\b', re.I), lambda m: 'daypack' + ('s' if m.group(0).lower().endswith('s') else '')),
        (re.compile(r'\bschool bags\b'), 'bags'), (re.compile(r'\bschool bag\b'), 'bag'),
        (re.compile(r'\bschool satchel\b'), 'leather satchel'),
        (re.compile('[‘’]'), "'"), (re.compile('[“”]'), ''),
        (re.compile(r'\s*—\s*'), ', '), (re.compile(r'\s*–\s*'), ' - ')]
changed = {}
for f in sorted(os.listdir(FINAL)):
    if not f.endswith('.txt'): continue
    p = os.path.join(FINAL, f); t = open(p, encoding='utf8').read(); o = t
    for rx, rep in SUBS: t = rx.sub(rep, t)
    if f in ('acc_meritbadge_adulting.txt',): t = re.sub(r'(?<!\d):(?!\d)', ',', t).replace(',,', ',')
    if f in ('mark_tattoo.txt', 'dem_unique.txt'):
        ls = t.split('\n')
        while ls and not ls[-1].strip(): ls.pop()
        t = '\n'.join(' ' if not l.strip() else l for l in ls) + '\n'
    if t != o:
        if not os.path.exists(os.path.join(BK, f)): shutil.copy(p, os.path.join(BK, f))
        open(p, 'w', encoding='utf8', newline='\n').write(t); changed[f] = 1
print('files changed', len(changed))
