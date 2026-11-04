"""v73: general chastity_belt group (user decision 2026-11-02, item 38): belt-style devices that cover several areas (front shield plus rear strap).
Built from the belt-type lines already in the chastity_vagina group (full text, phrase, random, short files), reusing the same material files.
Creates chastity_belt, chastity_belt_phrase, chastity_belt_random, chastity_belt_short, chastity_belt_prompt and adds __chastity_belt_prompt__ to chastity_prompt. --restore removes them."""
import os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from paths import FINAL
P = lambda n: os.path.join(FINAL, n + '.txt')
rd = lambda n: [l.rstrip('\n') for l in open(P(n), encoding='utf8') if l.strip()]
if '--restore' in sys.argv:
    for n in ('chastity_belt', 'chastity_belt_phrase', 'chastity_belt_random', 'chastity_belt_short', 'chastity_belt_prompt'):
        if os.path.exists(P(n)): os.remove(P(n))
    ls = [l for l in rd('chastity_prompt') if l != '__chastity_belt_prompt__']; open(P('chastity_prompt'), 'w', newline='\n').write('\n'.join(ls) + '\n'); sys.exit()
belt = re.compile(r'chastity belt', re.I)
for src, dst in (('chastity_vagina', 'chastity_belt'), ('chastity_vagina_phrase', 'chastity_belt_phrase'), ('chastity_vagina_random', 'chastity_belt_random'), ('chastity_vagina_short', 'chastity_belt_short')):
    ls = [l.replace('chastity_vagina_', 'chastity_vagina_') for l in rd(src) if belt.search(l)]
    open(P(dst), 'w', encoding='utf8', newline='\n').write('\n'.join(ls) + '\n'); print(dst, len(ls))
open(P('chastity_belt_prompt'), 'w', newline='\n').write('__chastity_belt_random__\n')
ls = rd('chastity_prompt')
if '__chastity_belt_prompt__' not in ls: open(P('chastity_prompt'), 'w', newline='\n').write('\n'.join(ls + ['__chastity_belt_prompt__']) + '\n')
