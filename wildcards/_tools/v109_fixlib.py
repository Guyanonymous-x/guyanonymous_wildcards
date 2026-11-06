"""v109 - two library-wide fixes approved by the user (2026-11-06).
1. Body-build age bands. The bt_<archetype>_<band>_body_build files come in three bands (y 18-44, m 45-64, o 65+; docs/README_body_layer.txt),
   but the v42 person lines (v42_people.py) always used the m band, so young adults could get 'stooped older build' and the old a middle-aged
   one. Every line that names its own age (__ageLO_HI_age_years__) now uses the band for that age. Files built to mismatch on purpose
   (names containing 'mismatched' or 'unlinked') are left alone.
2. The negation 'There are no visible signs of aging on her/his/their face.' (aging_text.py) is rewritten as a positive description."""
import os, re
AGE = re.compile(r'__age(\d+)_\d+_age_years__')
BT = re.compile(r'__([a-z]+)_bt_([a-z]+)_m_body_build__')
NEG = {'There are no visible signs of aging on her face.': 'Her face is smooth and unlined, with the freshness of youth.',
       'There are no visible signs of aging on his face.': 'His face is smooth and unlined, with the freshness of youth.',
       'There are no visible signs of aging on their face.': 'Their face is smooth and unlined, with the freshness of youth.'}
def band(lo): return 'y' if lo < 45 else 'm' if lo < 65 else 'o'
def fix(G, final):
    changed = {'band': 0, 'neg': 0}
    names = set(G) | {f[:-4] for f in os.listdir(final) if f.endswith('.txt')}
    for n in sorted(names):
        if 'mismatched' in n or 'unlinked' in n: continue
        lines = G.get(n)
        if lines is None:
            p = os.path.join(final, n + '.txt')
            with open(p, encoding='utf8') as f: raw = f.read()
            if '_m_body_build__' not in raw and 'no visible signs of aging' not in raw: continue
            lines = raw[:-1].split('\n') if raw.endswith('\n') else raw.split('\n')
        new = []
        for l in lines:
            m = AGE.search(l)
            if m and '_m_body_build__' in l:
                b = band(int(m.group(1)))
                if b != 'm':
                    l2 = BT.sub(lambda x: '__%s_bt_%s_%s_body_build__' % (x.group(1), x.group(2), b), l)
                    if l2 != l: changed['band'] += 1; l = l2
            for a, r in NEG.items():
                if a in l: l = l.replace(a, r); changed['neg'] += 1
            new.append(l)
        if new != lines: G[n] = new
    for n, ls in list(G.items()):
        for l in ls:
            for ref in re.findall(r'__([a-z]+_bt_[a-z]+_[ymo]_body_build)__', l):
                if ref not in G and not os.path.exists(os.path.join(final, ref + '.txt')): raise KeyError('v109_fixlib: missing %s' % ref)
    print('v109_fixlib', changed)
    return G
