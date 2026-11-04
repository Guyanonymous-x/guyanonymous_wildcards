"""v42 people system. Builds the plain-named character creation prompts (all adults 18-120, person only, no setting/pose/lighting):
   {f|m|any}_create_random_{woman|man|person}[_mismatched|_unlinked][_w_clothes|_nude|_topless|_bottomless][_short]
   any_create_random_person...  = mixed identity (cis, trans, intersex, non-binary, androgynous, in transition); optional _traits (scars / hormone-related traits)
   {m|f|any}_create_random_<identity>[_w_clothes|...][_short][_traits]  = fixed identity
Modes: realistic (age drives the look), mismatched (looks 10-30 years off the stated age), unlinked (age independent of every other trait).
The neutral (any_) pools are generated from the f_/m_ pools with they/their wording; no sexual-orientation text is used anywhere here."""
import os, re, sys, random, glob
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from paths import FINAL
BR = ['18_24', '25_34', '35_44', '45_54', '55_64', '65_74', '75_84', '85_94', '95_120']
BT = ['athl', 'avg', 'curvy', 'frail', 'heavy', 'musc', 'slim', 'thin', 'vheavy']
RNG = {'18_24': (18, 24), '25_34': (25, 34), '35_44': (35, 44), '45_54': (45, 54), '55_64': (55, 64), '65_74': (65, 74), '75_84': (75, 84), '85_94': (85, 94), '95_120': (95, 120)}
REF = re.compile(r'__([A-Za-z0-9_\-/]+)__')
WC = FINAL
def rd(n):
    p = os.path.join(WC, n + '.txt')
    return None if not os.path.exists(p) else [l for l in open(p, encoding='utf8').read().split('\n') if l.strip()]
def wr(n, lines): open(os.path.join(WC, n + '.txt'), 'w', encoding='utf8', newline='\n').write('\n'.join(lines) + '\n')
# ---------- gender-neutral conversion ----------
VERBS = {'has': 'have', 'is': 'are', 'was': 'were', 'does': 'do', 'goes': 'go'}
def _verb(m):
    s, w = m.group(1), m.group(2)
    if w in VERBS: w = VERBS[w]
    elif w in ('always', 'this', 'less', 'perhaps', 'its', 'thus'): pass
    elif w.endswith('ies') and len(w) > 4: w = w[:-3] + 'y'
    elif re.search(r'(ss|sh|ch|x|z)es$', w): w = w[:-2]
    elif w.endswith('s') and not w.endswith('ss'): w = w[:-1]
    return s + ' ' + w
def to_they(t):
    t = re.sub(r'\bherself\b|\bhimself\b', 'themselves', t); t = re.sub(r'\bHerself\b|\bHimself\b', 'Themselves', t)
    t = re.sub(r'\b(She|he|He|she)\b', lambda m: 'They' if m.group(1)[0] in 'SH' else 'they', t)
    t = re.sub(r'\b(They|they) ([a-z]+s)\b', _verb, t)
    t = re.sub(r'\b(Her|His)\b', 'Their', t); t = re.sub(r'\b(her|his)\b(?=\s*[,.;:!?]|\s*$|\s+(?:and|to|with|in|on|at|from|by)\b)', 'them', t)
    t = re.sub(r'\b(her|his)\b', 'their', t); t = re.sub(r'\bhim\b', 'them', t)
    t = re.sub(r'\b[Ww]omen\b|\b[Mm]en\b', lambda m: 'People' if m.group(0)[0].isupper() else 'people', t)
    t = re.sub(r'\bA (?:woman|man)\b', 'This person', t)
    t = re.sub(r'\b[Ww]oman\b|\b[Mm]an\b|\b[Gg]irl\b|\b[Bb]oy\b|\b[Ll]ady\b|\b[Gg]entleman\b', lambda m: 'Person' if m.group(0)[0].isupper() else 'person', t)
    return t
_made = {}
def any_of(name):
    """name of an f_ file -> its neutral any_ twin (union of the f_ and m_ pools, they/their wording); built recursively and cached."""
    if not name.startswith('f_'): return name
    core = name[2:]; an = 'any_' + core
    if an in _made: return an
    _made[an] = None
    lines = []
    for src in (name, 'm_' + core):
        L = rd(src)
        if L is None: continue
        for l in L:
            l = to_they(l); l = REF.sub(lambda m: '__' + (any_of(m.group(1)) if m.group(1).startswith('f_') else (any_of('f_' + m.group(1)[2:]) if m.group(1).startswith('m_') else m.group(1))) + '__', l)
            lines.append(l)
    seen = set(); out = []
    for l in lines:
        if l not in seen: seen.add(l); out.append(l)
    wr(an, out or ['']); _made[an] = True
    return an
# ---------- helper files ----------
CLOSE = {'45_54': ["Signs of middle age show across the face and skin.", "The face and skin show the lines of middle age."],
         '55_64': ["The face and skin clearly show an older adult.", "Lines, thinning hair and softened skin show an older adult."],
         '65_74': ["Every detail of the face and skin shows an elderly person.", "The face, hands and posture all show elderly age."],
         '75_84': ["Every detail of the face, hands and posture shows a very elderly person.", "The deep lines, thin skin and slower frame show a very elderly person."],
         '85_94': ["Every detail shows great old age, with deep wrinkles, thin skin and a stooped posture.", "The face, hands and posture show an extremely elderly person."],
         '95_120': ["Every detail shows extreme old age, with heavy wrinkling, translucent thin skin, sparse white hair and a bowed posture.", "The face, hands and body show the oldest possible age, deeply creased."]}
def helpers():
    for b, (lo, hi) in RNG.items():
        wr(f'age_num_{b}', [f'{a} years old' for a in range(lo, hi + 1)])
        wr(f'age_closing_{b}', CLOSE.get(b, [' ']))
    for g in 'fm':      # ageing lines without hair claims (hair is decided by the hair files)
        for b in BR:
            n = f'{g}_age{b}_aging_summary'; L = rd(n)
            if L: wr(n, [l for l in L if not re.search(r'\b(bald|balding|hair|hairless)\b', l, re.I)] or L)
# ---------- line builders ----------
def pron(g):
    return {'f': dict(S='She', P='Her', s='she', p='her', noun='woman', a='A woman', isare='is', have='has', wear='wears', look='looks'),
            'm': dict(S='He', P='His', s='he', p='his', noun='man', a='A man', isare='is', have='has', wear='wears', look='looks'),
            'any': dict(S='They', P='Their', s='they', p='their', noun='person', a='This person', isare='are', have='have', wear='wear', look='look')}[g]
def bts(b): return [t for t in BT if not (t == 'frail' and BR.index(b) < 5)]
def X(g, n): return f'{g}_{n}'
def real_full(g):
    L = []
    for i, b in enumerate(BR):
        for bt in bts(b):
            core = f'age{b}_prompt_char_physical_{bt}'
            L.append(f'__{g}_{core}__' + (f' __age_closing_{b}__' if i >= 3 else ''))
    return L
def comp_line(g, bage, bface, bt, short=False, numstyle='num'):
    """one person built from components: stated age from bracket bage (plain number), everything else from bracket bface."""
    p = pron(g); y = bface
    ident = f"{p['a']}, __age_num_{bage}__, from __countries__. {p['P']} coloring is __age{y}_eye_color__, __age{y}_hair_color__ and __dem_tone__. __{g}_age{y}_aging_summary__"
    if short:
        return f"{ident} {p['S']} {p['have']} {{hair}} and {p['p']} build is __{g}_bt_{bt}_m_body_build__." .replace('{hair}', f'__{g}_age{y}_hairstyle_S__')
    return (f"{ident} __{g}_age{y}_prompt_char_face__ __{g}_age{y}_prompt_char_hair_S__ __{g}_age{y}_prompt_char_skin__ __{g}_bt_{bt}_age{y}_prompt_char_body__ __{g}_age{y}_prompt_char_details__")
def real_short(g):
    L = []; p = pron(g)
    for i, b in enumerate(BR):
        for bt in bts(b):
            L.append(f"{p['a']}, __age{b}_age_years__, from __countries__. {p['S']} {p['have']} __age{b}_eye_color__ and __age{b}_hair_color__, styled as __{g}_age{b}_hairstyle_S__, and __dem_tone__. __{g}_age{b}_aging_summary__ {p['P']} build is __{g}_bt_{bt}_m_body_build__.")
    return L
def years_off(a, b):
    d = abs(RNG[a][0] + RNG[a][1] - RNG[b][0] - RNG[b][1]) // 2
    return 'ten' if d < 15 else 'twenty' if d < 25 else 'thirty' if d < 35 else 'forty'
def mismatched(g, short, n=360, seed=7):
    R = random.Random(seed + (1 if short else 0) + ord(g[0])); L = []; p = pron(g)
    k = 0
    while len(L) < n and k < n * 30:
        k += 1
        a = R.choice(BR); i = BR.index(a); cands = [BR[j] for j in range(len(BR)) if 1 <= abs(j - i) <= 3]
        y = R.choice(cands); bt = R.choice(bts(y)); older = BR.index(y) > i
        line = comp_line(g, a, y, bt, short) + f" {p['S']} {p['look']} about {years_off(a, y)} years {'older' if older else 'younger'} than {p['p']} stated age."
        if line not in L: L.append(line)
    return L
def unlinked(g, short, n=360, seed=11):
    R = random.Random(seed + (1 if short else 0) + ord(g[0])); L = []
    while len(L) < n:
        a = R.choice(BR); y = R.choice(BR); bt = R.choice(BT)
        line = comp_line(g, a, y, bt, short)
        if line not in L: L.append(line)
    return L
def clothes_tok(g, mode, line_i, b=None, bt=None):
    h = 'm' if (g == 'any' and line_i % 2) else ('f' if g == 'any' else g)
    return f'__{h}_clothing_random_mix__'
STATES = ['', '_w_clothes', '_nude', '_topless', '_bottomless']
def with_state(g, lines, state, realistic=False):
    p = pron(g); out = []
    for i, l in enumerate(lines):
        h = 'm' if (g == 'any' and i % 2) else ('f' if g == 'any' else g)
        if state == '': out.append(l)
        elif state == '_w_clothes':
            m = re.search(r'age(\d+_\d+)_prompt_char_physical_([a-z]+)__', l)
            tok = f'__{h}_age{m.group(1)}_clothing_{m.group(2)}__' if (realistic and m and g != 'any') else f'__{h}_clothing_random_mix__'
            out.append(f"{l} {p['S']} {p['isare']} wearing {tok}.")
        elif state == '_nude': out.append(f"{l} {p['S']} {p['isare']} nude.")
        elif state == '_topless': out.append(f"{l} {p['S']} {p['isare']} bare-chested and {p['isare']} wearing __{h}_outfit_casual_bottom__.")
        elif state == '_bottomless': out.append(f"{l} {p['S']} {p['isare']} wearing __{h}_outfit_casual_top__ and nothing below the waist.")
    return out
# ---------- identities ----------
IDEN = {  # id: (label, base gender g, name suffix, bodies from demo_body_<id>)
 'trans_man': ('A trans man', 'm', 'trans_man'), 'trans_woman': ('A trans woman', 'f', 'trans_woman'), 'intersex_man': ('An intersex man', 'm', 'intersex_man'),
 'intersex_woman': ('An intersex woman', 'f', 'intersex_woman'), 'intersex_person': ('An intersex person', 'any', 'intersex_person'), 'nonbinary': ('A non-binary person', 'any', 'nonbinary_person'),
 'androgynous': ('An androgynous person', 'any', 'androgynous_person'), 'gradual_fem': ('A person in transition toward a more feminine presentation', 'any', 'person_in_transition_feminine'),
 'gradual_masc': ('A person in transition toward a more masculine presentation', 'any', 'person_in_transition_masculine'),
 'individualized_fem': ('A non-binary person with a blended body leaning feminine', 'any', 'nonbinary_person_leaning_feminine'), 'individualized_masc': ('A non-binary person with a blended body leaning masculine', 'any', 'nonbinary_person_leaning_masculine')}
MIXW = {'cis_man': 3, 'cis_woman': 3, 'trans_man': 1, 'trans_woman': 1, 'intersex_man': 1, 'intersex_woman': 1, 'intersex_person': 1, 'nonbinary': 1, 'androgynous': 1, 'gradual_fem': 1, 'gradual_masc': 1, 'individualized_fem': 1, 'individualized_masc': 1}
def with_identity(lines, label, bodyid=None):
    return [f"{label}. {l}" + (f" __demo_body_{bodyid}__" if bodyid else '') for l in lines]
def build():
    helpers(); made = 0
    for g in ('f', 'm', 'any'):
        noun = pron(g)['noun']
        base_full = real_full(g); base_short = real_short(g)
        if g == 'any':
            for l in base_full + base_short:
                for r in REF.findall(l): pass
            base_full = [REF.sub(lambda m: '__' + any_of('f_' + m.group(1)[4:]) + '__' if m.group(1).startswith('any_') else m.group(0), l) for l in base_full]
            base_short = [REF.sub(lambda m: '__' + any_of('f_' + m.group(1)[4:]) + '__' if m.group(1).startswith('any_') else m.group(0), l) for l in base_short]
        modes = {'': (base_full, base_short), '_mismatched': (mismatched(g, False), mismatched(g, True)), '_unlinked': (unlinked(g, False), unlinked(g, True))}
        for mname, (full, short) in modes.items():
            if g == 'any' and mname:
                full = [REF.sub(lambda m: '__' + any_of('f_' + m.group(1)[4:]) + '__' if m.group(1).startswith('any_') else m.group(0), l) for l in full]
                short = [REF.sub(lambda m: '__' + any_of('f_' + m.group(1)[4:]) + '__' if m.group(1).startswith('any_') else m.group(0), l) for l in short]
            for st in STATES:
                for sh, lines in (('', full), ('_short', short)):
                    L = with_state(g, lines, st, realistic=(mname == '' and sh == ''))
                    if g == 'any':    # mixed identity: label (+ optional traits) per line
                        wr(f'any_create_random_person_base{mname}{st}{sh}', L); made += 1
                        for tr in ('', '_traits'):
                            out = []
                            for gid, wgt in MIXW.items():
                                label = {'cis_man': 'A man', 'cis_woman': 'A woman'}.get(gid) or IDEN[gid][0]
                                if gid in ('cis_man', 'cis_woman'):
                                    if tr: continue
                                    h = 'm' if gid == 'cis_man' else 'f'
                                    out += [f'__{h}_create_random_{"man" if h == "m" else "woman"}{mname}{st}{sh}__'] * wgt * 4
                                else:
                                    out += [f'__{IDEN[gid][1]}_create_random_{IDEN[gid][2]}{mname}{st}{sh}{tr}__'] * wgt * 4
                            if tr == '' or True: wr(f'any_create_random_person{mname}{st}{sh}{tr}', out); made += 1
                    else:
                        wr(f'{g}_create_random_{noun}{mname}{st}{sh}' if g != 'any' else f'any_create_random_person_base{mname}{st}{sh}', L); made += 1
    # fixed identities (all modes share the realistic/unlinked/mismatched person blocks of their base)
    for gid, (label, g, nm) in IDEN.items():
        for mname in ('', '_mismatched', '_unlinked'):
            for st in STATES:
                for sh in ('', '_short'):
                    src = f'{g}_create_random_{pron(g)["noun"]}{mname}{st}{sh}' if g != 'any' else f'any_create_random_person_base{mname}{st}{sh}'
                    base = rd(src)
                    if base is None: continue
                    for tr in ('', '_traits'):
                        wr(f'{g}_create_random_{nm}{mname}{st}{sh}{tr}', [f"{label}. __{src}__" + (f" __demo_body_{gid}__" if tr else '')]); made += 1
    print('v42 people: files written', made, '; neutral any_ twins', len(_made))
    return made
def run(final):
    global WC; WC = final; return build()
if __name__ == '__main__':
    a = [x for x in sys.argv[1:] if os.path.isdir(x)]; run(os.path.abspath(a[0]) if a else FINAL)
