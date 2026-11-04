"""ONE-TIME maintenance script (already applied to the delivered files):  python _tools/fix_ethnic.py
 1. countries_ethnic_prompts.txt - the vague skin words "light", "fair" and "fair to light" become specific colours (several variants, chosen deterministically per line).
 2. dem_tone.txt (+ the table in pilot_body.py) - every option now names a skin colour AND an undertone (it used to give only an undertone)."""
import os, re, zlib, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from paths import FINAL
VAR = {'light': ["light beige", "light peachy-beige", "light warm ivory", "light pinkish-beige", "light neutral beige", "light creamy-beige"],
       'fair': ["fair peachy-cream", "fair pinkish-ivory", "fair cool ivory", "fair porcelain-pink", "fair neutral cream", "fair warm cream"],
       'fair to light': ["fair to light peachy-beige", "fair to light pinkish-ivory", "fair to light warm beige", "fair to light cream-beige", "fair to light neutral ivory"]}
p = os.path.join(FINAL, 'countries_ethnic_prompts.txt'); n = 0; out = []
for l in open(p, encoding='utf8').read().split('\n'):
    m = re.search(r'with (light|fair to light|fair) skin\b', l)
    if m:
        v = VAR[m.group(1)]; new = v[zlib.crc32(l.encode('utf8')) % len(v)]
        l = l[:m.start()] + f'with {new} skin' + l[m.end():]; n += 1
    out.append(l)
open(p, 'w', encoding='utf8', newline='\n').write('\n'.join(out)); print('ethnic lines rewritten:', n)
TONE = {"warm golden undertones": "medium golden-tan skin with warm golden undertones", "neutral balanced undertones": "medium beige skin with neutral balanced undertones", "olive greenish undertones": "olive skin with greenish undertones",
 "cool pinkish undertones": "light pink-beige skin with cool pinkish undertones", "peach undertones": "light peach skin with peach undertones", "tan golden undertones": "tan skin with golden undertones",
 "earthy brown undertones": "medium brown skin with earthy brown undertones", "bronze undertones": "bronze skin with warm bronze undertones", "copper undertones": "copper-brown skin with copper undertones",
 "rich ebony undertones": "deep ebony-brown skin with rich ebony undertones", "deep mahogany undertones": "deep mahogany-brown skin with reddish undertones", "deep red undertones": "deep reddish-brown skin with deep red undertones",
 "cool bluish undertones": "dark brown skin with cool bluish undertones", "pale porcelain undertones": "pale porcelain-white skin with faint pale undertones", "pale alabaster undertones": "pale alabaster-white skin with faint undertones",
 "ivory cool undertones": "ivory skin with cool undertones", "ashy neutral undertones": "light grey-beige skin with ashy neutral undertones", "flush ruddy undertones": "fair skin with a flushed ruddy-red undertone",
 "ashen grey undertones": "ashen grey-pale skin with grey undertones", "weathered bronze undertones": "weathered bronze-brown skin with bronze undertones", "sallow yellowish undertones": "sallow yellow-beige skin with yellowish undertones",
 "sunburned red undertones": "sunburned red-pink skin over a fair base", "sanguine rosy undertones": "fair rosy-pink skin with sanguine undertones", "dull pale undertones": "dull pale beige skin with muted undertones",
 "hyperpigmented uneven undertones": "medium brown skin with uneven hyperpigmented patches", "jaundiced warm undertones": "yellow-tinged jaundiced skin with warm undertones", "cyanotic cool undertones": "bluish-pale cyanotic skin with cool undertones",
 "pale sickly undertones": "pale sickly greenish-white skin with cool undertones"}
for fn in (os.path.join(FINAL, 'dem_tone.txt'), os.path.join(HERE := os.path.dirname(os.path.abspath(__file__)), 'pilot_body.py')):
    s = open(fn, encoding='utf8').read()
    for a, b in TONE.items(): s = s.replace(f'"{a}"', f'"{b}"') if fn.endswith('.py') else s
    if fn.endswith('.txt'): s = '\n'.join(TONE.get(l.strip(), l) for l in s.split('\n'))
    open(fn, 'w', encoding='utf8', newline='\n').write(s)
print('dem_tone options rewritten:', len(TONE))
