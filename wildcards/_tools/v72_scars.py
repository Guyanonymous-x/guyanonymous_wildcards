#!/usr/bin/env python3
"""v72 scar pass: '<adjective> scar on the <place>' lines in mark_scars and skin_scars become
physical descriptions (colour, relief, length). Reason: Moss drew 'a short scar on the forearm'
as a deep recessed gash in one image and a pale raised line in another; a fixed look removes the
spread. Usage: python _tools/v72_scars.py [--dry] [--restore]. Run LAST after any rebuild; idempotent.
Originals go to _tools/backup_v71/."""
import os, re, shutil, sys
HERE = os.path.dirname(os.path.abspath(__file__)); LIB = os.path.dirname(HERE); BK = os.path.join(HERE, 'backup_v71')
FILES = ['mark_scars.txt', 'skin_scars.txt']
L4 = 'about four centimetres long'
D = {
 'thin': f'a thin, pale, slightly raised scar {L4}', 'wide': 'a wide, flat, pale scar about two centimetres across and four centimetres long',
 'faint': f'a faint, pale, barely raised scar {L4}', 'raised': f'a raised, slightly pink scar ridge {L4}',
 'flat': f'a flat, smooth, pale scar {L4}', 'straight': f'a straight, thin, pale scar {L4}',
 'curved': f'a thin, pale, gently curved scar {L4}', 'zigzag': f'a thin, pale zigzag scar {L4}',
 'short': 'a short, thin, pale scar about two centimetres long', 'long': 'a long, thin, pale scar about eight centimetres long',
 'healed': f'a fully healed, flat, pale scar {L4}', 'old': f'an old, flat, silvery-pale scar {L4}',
 'neat': f'a neat, thin, straight, pale scar {L4}', 'silvery': f'a thin, silvery, slightly shiny scar {L4}',
 'pale': f'a pale, thin, flat scar {L4}', 'puckered': f'a pale, slightly raised scar {L4} with the skin gathered along its edges',
 'linear': f'a thin, straight, pale scar {L4}', 'diagonal': f'a thin, pale scar {L4} running diagonally',
 'vertical': f'a thin, pale scar {L4} running up and down', 'horizontal': f'a thin, pale scar {L4} running sideways',
}
RX = re.compile(r'^(' + '|'.join(D) + r') scar (on the [a-z ]+)$')
def conv(l):
    m = RX.match(l.strip())
    return f'{D[m.group(1)]} {m.group(2)}' if m else l
if '--restore' in sys.argv:
    for f in FILES:
        if os.path.exists(os.path.join(BK, f)): shutil.copy2(os.path.join(BK, f), os.path.join(LIB, f))
    sys.exit(print('restored'))
for f in FILES:
    p = os.path.join(LIB, f); lines = open(p, encoding='utf-8').read().split('\n'); out = [conv(l) for l in lines]
    n = sum(a != b for a, b in zip(lines, out)); print(f, 'lines changed', n)
    if n and '--dry' not in sys.argv:
        os.makedirs(BK, exist_ok=True)
        if not os.path.exists(os.path.join(BK, f)): shutil.copy2(p, os.path.join(BK, f))
        open(p, 'w', encoding='utf-8', newline='\n').write('\n'.join(out))
