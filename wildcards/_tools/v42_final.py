"""v42 final pass (idempotent). (1) emphasis weights (word:N) -> plain wording. (2) __f_/m_health_conditions__ removed from the random-person templates (the files stay).
(3) 'The subject is a woman who is ...' style openers -> 'A woman, <age>, ...'. (4) punctuation / article repairs. (5) blank-line weighting: blank lines used to make 'none' likely are replaced by a short
positive sentence in the same proportion (tools that strip blank lines then keep the intended odds). (6) child-coded phrase in ageing text replaced."""
import os, re, sys, glob, random
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from paths import FINAL

# ---------- (1) weights ----------
W = re.compile(r'\(([^()\n]{1,120}?)\s*:\s*(-?\d*\.?\d+)\)')
ATTR = [(0.35, 'ordinary-looking'), (0.65, 'pleasant-looking'), (0.95, 'good-looking'), (1.05, 'attractive'), (1.35, 'quite attractive'), (1.75, 'very attractive'), (2.5, 'extremely attractive'), (99, 'strikingly attractive')]
LIT = {'red eyes': 'vivid red eyes', 'fangs': 'visible fangs'}
def wconv(m):
    inner, w = m.group(1).strip(), float(m.group(2))
    if inner == 'attractive':
        for lim, word in ATTR:
            if w <= lim: return word
    if w >= 1.4 and inner in LIT: return LIT[inner]
    if w == 1.2 and inner in LIT: return LIT[inner]
    return inner
def weights_text(t): return W.sub(wconv, t)
# ---------- (2) health conditions ----------
HC = re.compile(r'[ \t]*__[fm]?_?health_conditions__[ \t]*')
HCFILE = re.compile(r'^(?:[fm]_)?health_conditions\.txt$')
def health_text(t): return HC.sub(' ', t)
# ---------- (3) openers ----------
A = r'(?:__[A-Za-z0-9_]*age[A-Za-z0-9_]*__)'
B = r'(?m)(^|__ |\. )'
def openers_text(t):
    t = re.sub(B + r'(?:The subject is a|A) (woman|man) who is (' + A + r') and holds ([^,\n]+?) nationality', r'\1A \2, \3, who holds \4 nationality', t)
    t = re.sub(B + r'(?:The subject is a|A) (woman|man) who is (' + A + r') from ', r'\1A \2, \3, from ', t)
    t = re.sub(B + r'(?:The subject is a|A) (woman|man) of ([^.\n]+?) nationality who is (' + A + r')', r'\1A \2 of \3 nationality, \4,', t)
    t = re.sub(B + r'(?:The subject is a|A) (woman|man) who is (' + A + r')', r'\1A \2, \3,', t)
    t = re.sub(B + r'This (woman|man), (' + A + r'), is from ', r'\1A \2, \3, from ', t)
    t = re.sub(B + r'(A (?:woman|man)(?: of [^.\n]+? nationality)?, ' + A + r'),(?=\.)', r'\1\2', t)
    t = re.sub(B + r'(A (?:woman|man), ' + A + r'),,', r'\1\2,', t)
    t = re.sub(r'The subject is (an?) ', lambda m: m.group(1).capitalize() + ' ', t)
    return t
ORD = {'1': 'first', '2': 'second', '3': 'third'}
def pieces_text(t):
    if 'Piece 1 (' not in t: return t
    t = re.sub(r'Piece (\d) \(([^()]*)\): ', lambda m: 'The ' + ORD.get(m.group(1), 'next') + ' piece is ' + m.group(2) + '. ', t)
    t = t.replace(' -- ', '. ')
    t = re.sub(r'(?m)^([^:\n]{3,90}): (?=The first piece)', r'\1. ', t)
    return t.replace('Front: ', 'At the front, ')
# ---------- (4) punctuation ----------
def vow(w): return 'an' if w[:1].lower() in 'aeiou' else 'a'
def punct_text(t):
    t = re.sub(r'\b(?:a|an) (?:a|an) (?=(\w))', lambda m: vow(m.group(1)) + ' ', t)
    t = re.sub(r'(?<!\.)\.\.(?!\.)', '.', t)
    t = re.sub(r',\s*,', ',', t)
    t = re.sub(r'(?m)(?<=\S)[ \t]{2,}(?=\S)', ' ', t)
    t = re.sub(r' +([,.;])', r'\1', t)
    t = re.sub(r'(?<![-\w])-- ?', '', t) if False else t
    return t
# ---------- (6) child-coded ----------
CH = [("a body hardly larger than a child's", 'a very small, light frame'), ("hardly larger than a child's", 'very small and light')]
def child_text(t):
    for a, b in CH: t = t.replace(a, b)
    return t
# ---------- (5) blank-line weighting ----------
def pron(f):
    if f.startswith('f_'): return {'S': 'She', 'P': 'Her', 's': 'she', 'p': 'her', 'r': 'herself'}
    if f.startswith('m_'): return {'S': 'He', 'P': 'His', 's': 'he', 'p': 'his', 'r': 'himself'}
    return None
FAM = [  # (regex on file base without f_/m_/age prefix, template) ; {S} She/He, {P} Her/His, {p} her/his
    (r'opt_tattoo$', '{P} skin is unadorned.'), (r'aids(_[a-z]+)?$', '{S} stands unaided.'), (r'opt_eyewear$|acc_glasses$', '{P} eyes are uncovered.'),
    (r'aging_summary$', '{S} looks {p} age.'), (r'opt_unique$', '{S} has an ordinary look.'), (r'extrasinphoto$', '{S} is alone.'), (r'health_conditions$', '{S} is healthy.')]
NEUT = [(r'^acc_.*_trim_', 'It has a simple, plain edge.'), (r'^acc_.*_finish_', 'It has a simple, plain surface.'), (r'^acc_.*_hardware_', 'It has plain, simple fittings.'), (r'^acc_.*_lining_', 'Inside it has a plain, simple lining.')]
def blank_fix(final):
    n = 0; left = {}
    for f in sorted(glob.glob(os.path.join(final, '*.txt'))):
        base = os.path.basename(f)[:-4]; t = open(f, encoding='utf8').read(); L = t.split('\n')
        tail = L[-1] == ''
        body = L[:-1] if tail else L
        if not any(not l.strip() for l in body): continue
        pr = pron(base); core = re.sub(r'^(f|m|any)_', '', base); core = re.sub(r'^(bt_[a-z]+_)?age\d+_\d+_', '', core); core = re.sub(r'^bt_[a-z]+_', '', core)
        rep = None
        if pr:
            for rx, tpl in FAM:
                if re.search(rx, core): rep = tpl.format(**pr); break
        else:
            for rx, s in NEUT:
                if re.search(rx, base): rep = s; break
        if rep is None: left[core] = left.get(core, 0) + 1; continue
        body = [rep if not l.strip() else l for l in body]
        open(f, 'w', encoding='utf8', newline='\n').write('\n'.join(body + ([''] if tail else []))); n += 1
    return n, left

# ---------- (7) age / size consistency ----------
AGE_FIX = [(", tiny, fragile and ancient-looking", ", ancient-looking"), (", frail and deeply wrinkled", " and deeply wrinkled"), ("elderly and visibly frail with deeply aged", "elderly with deeply aged"),
           ("very elderly, shrunken and fragile with extremely aged", "very elderly with extremely aged"), ("a shrunken, doll-like frame", "a deeply bent frame"), ("a very small, light frame", "a deeply bent frame"),
           ("a tiny, severely bent body", "a severely bent back"), ("She is a centenarian, tiny and fragile:", "She is a centenarian:"), ("He is a centenarian, tiny and fragile:", "He is a centenarian:"),
           ("is extremely elderly and fragile", "is extremely elderly"), ("shrunken by age:", "marked by age:"), ("shrunken and soft", "soft and deeply folded"), ("the fragile look of advanced age", "the look of advanced age"),
           ("frail thin arms", "thin arms"), ("a small body folded forward", "a body folded forward"), ("doll-like", "delicate"), ("She is a centenarian: ", "She is a centenarian, "), ("He is a centenarian: ", "He is a centenarian, "), ("marked by age:", "marked by age,")]
SIZE_FIX = [(r'\bpetite\b', 'delicate'), (r'\btiny\b', 'small-framed'), (r'\bcompact\b', 'sturdy')]
AGED = re.compile(r'wrinkled|sagging|crepe|crepey|leathery|deep furrow|age spot', re.I)
YOUNG = re.compile(r'unwrinkled|youthful|unlined|smooth skin', re.I)
def agesize_fix(final):
    n = 0
    for f in glob.glob(os.path.join(final, '*.txt')):
        base = os.path.basename(f)[:-4]; core = re.sub(r'^(f_|m_|any_)', '', base)
        if not (re.search(r'age_years$|aging_summary$', core) or re.search(r'body_build|body_ratio', core) or re.match(r'age(18|25|35|45|55|65|75|85|95)_\d+_skin_wrinkle$', core)): continue
        t = open(f, encoding='utf8').read(); u = t
        if re.search(r'age_years$|aging_summary$', core):
            for a, b in AGE_FIX: u = u.replace(a, b)
        if re.search(r'body_build|body_ratio', core):
            for a, b in SIZE_FIX: u = re.sub(a, b, u)
        if re.match(r'age(18|25|35)_\d+_skin_wrinkle$', core):
            L = u.split('\n'); good = [l for l in L if l.strip() and not AGED.search(l)]
            if good:
                R = random.Random(6); u = '\n'.join(l if (not l.strip() or not AGED.search(l)) else R.choice(good) for l in L)
        if re.match(r'age(55|65|75|85|95)_\d+_skin_wrinkle$', core):
            L = u.split('\n'); good = [l for l in L if l.strip() and not YOUNG.search(l)]
            if good:
                R = random.Random(5); u = '\n'.join(l if (not l.strip() or not YOUNG.search(l)) else R.choice(good) for l in L)
        if u != t: open(f, 'w', encoding='utf8', newline='\n').write(u); n += 1
    return n

# ---------- (8) hair / eye colour only in the colour files; bald styles in their own templates ----------
HC_ = r'(?:dark brown|light brown|black|dark|brown|blond|blonde|reddish|red|auburn|gray|grey|light)'
def ethnic_text(t):
    t = re.sub(r' and (?:' + HC_ + r' )+hair\b', '', t)
    t = re.sub(r'\b' + HC_ + r'\b ?(?=(?:[a-z\-]+ ){0,2}hair\b)', '', t)
    t = re.sub(r' and (?:' + HC_ + r'|blue or green|blue|green|hazel)(?: (?:' + HC_ + r'|blue or green))* eyes\b', '', t)
    t = re.sub(r'\b(almond shaped|almond|large) (?:dark brown |dark |light )(?=eyes)', r'\1 ', t)
    t = re.sub(r'\b(almond shaped|large) (?:dark brown |dark |light )(eyes)', r'\1 \2', t)
    return re.sub(r'  +', ' ', t)
def ethnic_fix(final):
    n = 0
    for f in glob.glob(os.path.join(final, 'countries_ethnic_prompts*.txt')):
        t = open(f, encoding='utf8').read(); u = ethnic_text(t)
        if u != t: open(f, 'w', encoding='utf8', newline='\n').write(u); n += 1
    return n
BALDRX = re.compile(r'\b(bald|balding|shaved head|shaved scalp|hairless|smooth scalp|shaved bald|clean-shaven head)\b', re.I)
def hair_fix(final):
    n = 0
    for f in glob.glob(os.path.join(final, '*_age*_hairstyle_[SWCK].txt')) + glob.glob(os.path.join(final, '[fm]_hairstyle_[SWCK].txt')):
        base = os.path.basename(f)[:-4]
        if base.endswith('_bald'): continue
        L = [l for l in open(f, encoding='utf8').read().split('\n') if l.strip()]
        bald = [l for l in L if BALDRX.search(l)]
        if not bald: continue
        hairy = [l for l in L if not BALDRX.search(l)]
        if not hairy: continue
        R = random.Random(9); p = len(bald) / len(L)
        out = hairy[:] + [R.choice(hairy) for _ in range(len(bald))]
        open(f, 'w', encoding='utf8', newline='\n').write('\n'.join(out) + '\n')
        open(f[:-4] + '_bald.txt', 'w', encoding='utf8', newline='\n').write('\n'.join(bald) + '\n')
        tpl = f.replace('hairstyle', 'prompt_char_hair')
        if os.path.exists(tpl):
            T = [l for l in open(tpl, encoding='utf8').read().split('\n') if l.strip()]
            if not any('_bald__' in l for l in T):
                P = 'Her' if os.path.basename(f).startswith('f_') else ('His' if os.path.basename(f).startswith('m_') else 'Their')
                k = max(1, round(60 * p / (1 - p))) if p < 1 else 60
                U = T * (60 // max(1, len(T))) + [f'{P} hairstyle is __' + base + '_bald__.'] * k
                open(tpl, 'w', encoding='utf8', newline='\n').write('\n'.join(U) + '\n')
        n += 1
    return n
# ---------- driver ----------
def clean_text(t, health=True):
    t = weights_text(t); t = child_text(t); t = openers_text(t); t = pieces_text(t)
    if health: t = health_text(t)
    return punct_text(t)
def run(final, verbose=True):
    ch = 0
    for f in glob.glob(os.path.join(final, '*.txt')):
        base = os.path.basename(f)
        t = open(f, encoding='utf8').read(); u = clean_text(t, health=not HCFILE.match(base))
        if u != t: open(f, 'w', encoding='utf8', newline='\n').write(u); ch += 1
    nb, left = blank_fix(final); agesize_fix(final); ethnic_fix(final); hair_fix(final)
    if verbose: print('v42 final: text rewritten in', ch, 'files; blank lines made explicit in', nb, 'files; families left unchanged:', {k: v for k, v in sorted(left.items(), key=lambda x: -x[1])[:8]})
    return ch + nb
def export_aoo(out, prefix='aoo_'):
    for f in glob.glob(os.path.join(out, '*.txt')):
        t = open(f, encoding='utf8').read(); u = clean_text(t, health=False)
        if u != t: open(f, 'w', encoding='utf8', newline='\n').write(u)
    return 0
if __name__ == '__main__':
    a = [x for x in sys.argv[1:] if os.path.isdir(x)]; run(os.path.abspath(a[0]) if a else FINAL)
