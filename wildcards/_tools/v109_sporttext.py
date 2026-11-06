"""v109 - words on clothing are always quoted (text rule 1 and 3; user 2026-11-06: jerseys and any sportswear with words).
Lines that mentioned a number, name, name patch or name tape on clothing without saying what it reads now quote it, linked to the
name system (name_jersey_number, name_team, name_first, name_surname, name_town). Two lines that mentioned unquoted words with no
sensible generator are rewritten as pictures."""
import os, re
SUBS = [
 (re.compile(r'with a name patch(?! reading)'), 'with a name patch reading "__name_first__"'),
 (re.compile(r'\b(singlet|jersey|shirt|vest) with a number\b(?! patch)'), r'\1 with the number "__name_jersey_number__"'),
 (re.compile(r'with team number on the chest'), 'with the number "__name_jersey_number__" on the chest'),
 (re.compile(r'\ba number jersey with a helmet'), 'a jersey with the number "__name_jersey_number__" and a helmet'),
 (re.compile(r'with name tape\b'), 'with a name tape reading "__name_surname__"'),
 (re.compile(r'with a number patch'), 'with a patch showing the number "__name_jersey_number__"'),
 (re.compile(r'with the tower name'), 'with the name "__name_town__" printed across it'),
 (re.compile(r'a t-shirt with a rude joke printed in large letters'), 'a t-shirt with a crude cartoon printed large across the front'),
 (re.compile(r'a hi-vis with a name in marker'), 'a hi-vis vest with "__name_first__" written on it in marker'),
 (re.compile(r'bag with a name in marker'), 'bag with "__name_surname__" written on it in marker'),
 (re.compile(r'with a name in marker'), 'with "__name_first__" written on it in marker'),
 (re.compile(r'\ba name in marker'), '"__name_first__" written in marker'),
]
def fix(G, final):
    n_lines = 0
    names = set(G) | {f[:-4] for f in os.listdir(final) if f.endswith('.txt')}
    keys = ('name patch', 'with a number', 'team number', 'number jersey', 'name tape', 'number patch', 'tower name', 'rude joke', 'name in marker')
    for n in sorted(names):
        lines = G.get(n)
        if lines is None:
            with open(os.path.join(final, n + '.txt'), encoding='utf8') as f: raw = f.read()
            if not any(k in raw for k in keys): continue
            lines = raw[:-1].split('\n') if raw.endswith('\n') else raw.split('\n')
        new = []
        for l in lines:
            l2 = l
            for rx, rep in SUBS: l2 = rx.sub(rep, l2)
            if l2 != l: n_lines += 1
            new.append(l2)
        if new != lines: G[n] = new
    print('v109_sporttext', n_lines)
    return G
