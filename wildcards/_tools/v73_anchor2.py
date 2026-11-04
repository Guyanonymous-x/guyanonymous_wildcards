"""v73 anchoring phase 2: sentence-leading possessive pronouns (Her / His / Their + noun) in the long-form person piece files become a noun
('The woman's face has ...', 'The man's eyes show ...', 'The person's hair ...'), so each attribute is tied to a named person in multi-person scenes.
Files: f_/m_/any_ *prompt_char_(face|hair|hair_C|hair_K|hair_S|hair_W|skin|body|details) and the bt_ body files. Possessives only (no verb changes needed).
Idempotent; --dry counts; --restore puts originals back (backup in _tools/backup_v72/anchor2/). Run LAST, after v71_build.py."""
import os, re, sys, shutil
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from paths import FINAL
BK = os.path.join(HERE, 'backup_v72', 'anchor2')
if '--restore' in sys.argv:
    for f in os.listdir(BK): shutil.copy(os.path.join(BK, f), os.path.join(FINAL, f))
    print('restored', len(os.listdir(BK))); sys.exit()
SEL = re.compile(r'^(f|m|any)_.*prompt_char_(face|hair|hair_[CKSW]|skin|body|details)\.txt$')
NOUN = {'f': "The woman's", 'm': "The man's", 'any': "The person's"}
LEAD = re.compile(r"(^|(?<=[.!?] ))(Her|His|Their) (?=[a-z])")
dry = '--dry' in sys.argv; os.makedirs(BK, exist_ok=True); nf = nl = 0
for f in sorted(os.listdir(FINAL)):
    if not SEL.match(f): continue
    pre = f.split('_')[0]; p = os.path.join(FINAL, f); lines = open(p, encoding='utf8').read().split('\n'); out = []; ch = 0
    for l in lines:
        n = LEAD.sub(lambda m: m.group(1) + NOUN[pre] + ' ', l)
        if n != l: ch += 1
        out.append(n)
    if ch:
        nf += 1; nl += ch
        if not dry:
            if not os.path.exists(os.path.join(BK, f)): shutil.copy(p, os.path.join(BK, f))
            open(p, 'w', encoding='utf8', newline='\n').write('\n'.join(out))
print(('would change' if dry else 'changed'), nf, 'files,', nl, 'lines')
