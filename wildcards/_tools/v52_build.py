"""v52: groups and relationships.
 - any_person_age<b>_w_clothes (+ _short): the random person, restricted to one age bracket (clones of the 15 chain files, rewired)
 - group_<relationship> in four age modes: relationship (default gap rules), any_ages, same_decade, multigenerational
 Everyone is an adult (18-120). Idempotent; run(final) / export_aoo(out)."""
import os, re, sys, random, zlib, functools
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from paths import FINAL
REF = re.compile(r'__([A-Za-z0-9_\-/]+)__'); AGE = re.compile(r'age(\d+_\d+)')
BR = ['18_24', '25_34', '35_44', '45_54', '55_64', '65_74', '75_84', '85_94', '95_120']
LO = [18, 25, 35, 45, 55, 65, 75, 85, 95]; HI = [24, 34, 44, 54, 64, 74, 84, 94, 120]
def _wr(folder, name, lines): open(os.path.join(folder, name + '.txt'), 'w', encoding='utf8', newline='\n').write('\n'.join(lines) + '\n')
def bracket(age): return max(i for i in range(9) if LO[i] <= age)
class Lib:
    def __init__(s, final): s.f = final; s.c = {}
    def rd(s, n):
        if n not in s.c:
            p = os.path.join(s.f, n + '.txt'); s.c[n] = [l for l in open(p, encoding='utf8').read().split('\n') if l.strip()] if os.path.exists(p) else []
        return s.c[n]
    @functools.lru_cache(None)
    def has_age(s, n):
        return any(AGE.search(r) or s.has_age(r) for l in s.rd(n) for r in REF.findall(l))
def clones(final, root, b, suffix):
    """names -> lines for the root restricted to bracket b"""
    L = Lib(final); out = {}; tag = f'{suffix}'
    def cn(n): return f'{n}__age{b}'
    def go(n):
        if cn(n) in out: return True
        out[cn(n)] = []; lines = []
        for l in L.rd(n):
            ages = set(AGE.findall(l)); refs = REF.findall(l)
            if ages and b not in ages: continue
            ok = True
            def sub(m):
                nonlocal ok
                r = m.group(1)
                if AGE.search(r) or not L.has_age(r): return m.group(0)
                if go(r): return '__' + cn(r) + '__'
                ok = False; return m.group(0)
            nl = REF.sub(sub, l)
            if ok: lines.append(nl)
        out[cn(n)] = lines; return bool(lines)
    go(root); return out
# ---- relationships: age rules (return a list of ages) ----
def A(lo, hi, r): return r.randint(lo, hi)
def clip(x): return max(18, min(120, x))
def gap(r, small=8, rare=18, p=0.8):
    g = r.randint(0, small) if r.random() < p else r.randint(small, rare)
    return g if r.random() < .5 else -g
def rel_couple(r): a = A(20, 95, r); return [a, clip(a + gap(r))]
def rel_parent_child(r):
    p = A(40, 105, r); n = r.choice([1, 1, 1, 2]); out = [p]
    for _ in range(n):
        c = p - r.randint(19, 45)
        if c < 18: c = r.randint(18, 24); p = max(p, c + 19); out[0] = p
        out.append(c)
    return out
def rel_three_gen(r):
    g = A(60, 108, r); p = clip(g - r.randint(20, 40)); c = g - r.randint(40, 75)
    c = max(18, min(c, p - 19)); p = max(p, c + 19); g = max(g, p + 19); return [g, p, c]
def rel_siblings(r):
    n = r.choice([2, 2, 3, 3, 4]); a = A(20, 95, r); return [a] + [clip(a + r.randint(-14, 14)) for _ in range(n - 1)]
def rel_friends(r):
    n = r.choice([3, 3, 4, 5]); a = A(19, 90, r); w = r.choice([4, 6, 9, 25]); return [clip(a + r.randint(-w, w)) for _ in range(n)]
def rel_colleagues(r):
    n = r.choice([3, 4, 5, 6]); a = A(24, 62, r); return [clip(a + r.randint(-14, 14)) for _ in range(n)]
def rel_team(r):
    n = r.choice([4, 5, 6, 7, 8]); a = A(21, 60, r); lead = clip(a + r.randint(5, 15)); return [lead] + [clip(a + r.randint(-10, 10)) for _ in range(n - 1)]
def rel_mentor(r): m = A(32, 100, r); return [m, max(18, m - r.randint(12, 38))]
def rel_classmates(r):
    n = r.choice([3, 4, 5, 6]); a = A(18, 70, r); w = r.choice([3, 8, 20]); return [clip(a + r.randint(-w, w)) for _ in range(n)]
def rel_neighbours(r):
    n = r.choice([2, 3, 4]); return [A(20, 100, r) for _ in range(n)]
RELS = {  # name: (age fn, intro sentences, interaction lines)
 'couple': (rel_couple, ['A couple together.', 'Two partners together.', 'A pair of partners.'], ['They stand close, relaxed together.', 'One has an arm around the other.', 'They look at each other and laugh.', 'They hold hands.', 'They sit side by side, shoulders touching.']),
 'parent_child': (rel_parent_child, ['A parent with their adult child.', 'A parent with their adult children.', 'An older parent and a grown child.'], ['They stand together in an easy, familiar way.', 'They share a joke, leaning towards each other.', 'The parent looks on proudly while the younger person talks.', 'They sit together, comfortable in silence.']),
 'three_generations': (rel_three_gen, ['Three generations of one family, with a grandparent, their adult child and a grown grandchild.', 'A family across three generations.'], ['They pose close together, with the eldest in the middle.', 'They sit together with the eldest in a chair at the centre.', 'They walk side by side, sharing a story.']),
 'siblings': (rel_siblings, ['Adult siblings together.', 'A group of brothers, sisters and siblings.', 'Siblings who have grown up together.'], ['They tease each other and laugh.', 'They stand close, with the easy habit of people who grew up together.', 'They sit around together, talking over each other.']),
 'friends': (rel_friends, ['A group of friends.', 'Friends out together.', 'A close group of friends.'], ['They laugh together, talking at once.', 'They stand in a loose cluster, clearly at ease.', 'They sit close together, sharing a moment.', 'They walk together in a relaxed line.']),
 'colleagues': (rel_colleagues, ['A group of colleagues.', 'Work colleagues together.', 'People who work together.'], ['They stand in a casual cluster, mid-conversation.', 'They sit around a shared table, talking.', 'They walk together, discussing something.']),
 'team': (rel_team, ['A team with their lead.', 'A working team together.', 'A group on the same team, their lead standing at the front.'], ['They stand in a tidy group, the lead slightly in front.', 'They gather around the lead, who is explaining something.', 'They pose together as a team.']),
 'mentor_mentee': (rel_mentor, ['An experienced mentor with a younger mentee.', 'A mentor and the person they are guiding.'], ['The mentor explains while the other listens closely.', 'They look at something together, the mentor pointing.', 'They stand together, talking seriously.']),
 'classmates': (rel_classmates, ['Classmates on an adult education course.', 'Fellow students in an evening class.', 'A group of classmates.'], ['They gather around a table, sharing notes.', 'They stand in a group after class, talking.', 'They sit together, comparing work.']),
 'neighbours': (rel_neighbours, ['Neighbours chatting together.', 'A few neighbours who have known each other for years.'], ['They chat across a low fence.', 'They stand together on the pavement, talking.', 'They gather on a doorstep.'])}
MODES = ['relationship', 'any_ages', 'same_decade', 'multigenerational']
def ages_for(rel, mode, r):
    fn = RELS[rel][0]; base = fn(r); n = len(base)
    if mode == 'relationship': return base
    if mode == 'any_ages': return [A(18, 110, r) for _ in range(n)]
    if mode == 'same_decade': b = r.randint(0, 8); return [r.randint(LO[b], HI[b]) for _ in range(n)]
    # multigenerational: spread across at least three brackets, youngest to oldest
    while True:
        a = sorted(A(18, 110, r) for _ in range(n)); 
        if n >= 3 and len({bracket(x) for x in a}) >= 3 or n == 2 and a[1] - a[0] >= 25: return a
ARR = ['standing in a row, from left to right', 'sitting in a loose group, from left to right', 'gathered in a close cluster, from left to right', 'standing in two staggered rows, from left to right', 'walking together side by side, from left to right']
THEME = ['', '', 'They are dressed in clearly different styles.', 'Their clothes coordinate loosely in colour.', 'Their outfits are casual and mixed.', 'They are dressed for the same occasion.']
ORD = ['first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh', 'eighth']
def line(rel, mode, r):
    ages = ages_for(rel, mode, r); n = len(ages); short = '_short'
    r2 = random.Random(r.random()); order = ages[:] if mode != 'multigenerational' else r2.sample(ages, n)
    if mode == 'relationship' and rel in ('parent_child', 'three_generations', 'mentor_mentee', 'team'): order = r2.sample(ages, n)
    intro = r.choice(RELS[rel][1]); inter = r.choice(RELS[rel][2]); th = r.choice(THEME)
    persons = ' '.join(f'{ORD[i].capitalize()} person. __any_person_age{BR[bracket(a)]}_w_clothes{short}__' for i, a in enumerate(order))
    head = f'{intro} {n} people, described from left to right. {inter}' + (' ' + th if th else '')
    return f'{head} {persons}'

# ---- consistent settings: outdoor places only, weather/time/season that agree ----
IND = re.compile(r'foyer|corridor|aisle|garage|cinema|bowling|salon|laborator|\bbath\b|nightclub|supermarket|store|\bshop\b|mall|library|\bgym|kitchen|office|lobby|lounge|restaurant|caf[eé]|\bbar\b|theatre|theater|museum|gallery|classroom|workshop|factory|warehouse|hawker|trade-show|booth|rink|studio|clinic|hospital|laundr|bakery|tea house|chapel|cathedral|church|auditorium|stage|arcade|casino|hotel|bedroom|bathroom|living room|attic|basement|cellar|cloister|greenhouse|elevator|stairwell|subway|metro|carriage|aquarium|\bhall\b|boutique|pharmacy|barber|parlou?r|\bspa\b|sauna|dojo|\btent\b|queue|barn|community centre|conservatory|diner|dorm|\bclub\b|penthouse|staircase|barracks|planetarium|power-plant floor|\bpub\b(?! garden)|stable|tunnel|crypt|swimming pool(?!.*deck)|taxi|wardrobe|lodge', re.I)
HOTP = re.compile(r'desert|dune|salt flat|rainforest|mangrove|rice terrace', re.I); COLDP = re.compile(r'glacier|snow|\bski\b|frozen|\bice\b|tundra', re.I)
TIMES_DAY = ['at dawn', 'early in the morning', 'in the mid-morning', 'at midday', 'in the early afternoon', 'in the late afternoon', 'at golden hour', 'at sunset', 'at dusk', 'at twilight']
TIMES_NIGHT = ['at night', 'late at night', 'before dawn', 'in the blue hour before sunrise']
# weather: (text, allowed seasons, day?, night?)  seasons: S summer, W winter, M mild (spring/autumn)
WEA = [('under a clear sky', 'SWM', 1, 0, 6), ('under a clear starry sky', 'SWM', 0, 1, 6), ('under a bright full moon', 'SWM', 0, 1, 2), ('with a few scattered clouds', 'SWM', 1, 1, 4), ('under an even grey overcast', 'SWM', 1, 1, 3),
 ('in light drizzle', 'SWM', 1, 1, 2), ('in steady rain', 'SWM', 1, 1, 2), ('in heavy rain', 'SWM', 1, 1, 1), ('during a thunderstorm', 'SM', 1, 1, 1), ('in thick fog', 'WM', 1, 1, 2), ('in light mist', 'SWM', 1, 1, 2),
 ('just after rain, with wet ground and puddles', 'SWM', 1, 1, 2), ('just after rain, with a rainbow in the sky', 'SM', 1, 0, 1), ('in a strong breeze', 'SWM', 1, 1, 2), ('in a heat haze', 'S', 1, 0, 2), ('in warm, humid air', 'S', 1, 1, 2),
 ('in falling snow', 'W', 1, 1, 3), ('with fresh snow on the ground', 'W', 1, 1, 2), ('in freezing air, with frost on every surface', 'W', 1, 1, 2), ('in cold, still air', 'W', 1, 1, 2), ('in cool, crisp air', 'M', 1, 1, 2), ('in mild, calm weather', 'M', 1, 1, 2)]
SEAS = {'S': ['in summer', 'on a hot summer day', 'in high summer'], 'W': ['in winter', 'on a cold winter day', 'in midwinter'], 'M': ['in spring', 'in autumn', 'on an early autumn day', 'on a spring day']}
def conditions(allowed):
    out = []
    for seas in allowed:
        for text, ok, day, night, w in WEA:
            if seas not in ok: continue
            for t in (TIMES_DAY if day else []) + (TIMES_NIGHT if night else []):
                if day and not night and t in TIMES_NIGHT: continue
                if night and not day and t in TIMES_DAY: continue
                if 'rainbow' in text and t in ('at dusk', 'at twilight', 'at sunset', 'at dawn'): continue
                if 'golden' in t and ('overcast' in text or 'fog' in text or 'heavy' in text or 'thunder' in text or 'steady rain' in text): continue
                if t == 'at sunset' and 'clear sky' not in text and 'scattered' not in text: continue
                out.append((f'{t[0].upper() + t[1:]}, {random.Random(zlib.crc32((seas + text + t).encode())).choice(SEAS[seas])}, {text}.', w))
    return out
WETW = re.compile(r'\b(rain-swept|foggy|post-storm|flooded|storm-lashed|misty|stormy|waterlogged)\s+', re.I)
def unweather(l):
    if not WETW.search(l): return l
    t = WETW.sub('', l)
    m = re.match(r'^(an?)\s+(.*)$', t, re.I)
    return (('an ' if m.group(2)[:1].lower() in 'aeiou' else 'a ') + m.group(2)) if m else t
def settings(final):
    G = {}; rd = lambda n: [l for l in open(os.path.join(final, n + '.txt'), encoding='utf8').read().split('\n') if l.strip()]
    ex, ins = rd('setting_exterior_place'), rd('setting_interior_place')
    keep = [unweather(re.sub(r'^(an?) (dimly lit|sunlit) ', r'\1 ', l)) for l in ex if not IND.search(l)]
    moved = [unweather(re.sub(r'^(an?) (dimly lit|sunlit) ', r'\1 ', l)) for l in ex if IND.search(l)]
    G['setting_exterior_place'] = list(dict.fromkeys(keep)); G['setting_interior_place'] = list(dict.fromkeys(ins + moved))
    G['setting_exterior_place_hot'] = [l for l in G['setting_exterior_place'] if HOTP.search(l)]; G['setting_exterior_place_cold'] = [l for l in G['setting_exterior_place'] if COLDP.search(l)]
    G['setting_exterior_place_any'] = [l for l in G['setting_exterior_place'] if not HOTP.search(l) and not COLDP.search(l)]
    for nm, al in (('any', 'SWM'), ('hot', 'S'), ('cold', 'W')):
        cs = conditions(al); G['setting_conditions_' + nm] = [t for t, w in cs for _ in range(w)]
    G['setting_conditions'] = ['__setting_conditions_any__']
    G['setting_exterior'] = ['The setting is __setting_exterior_place_any__. __setting_conditions_any__'] * 14 + ['The setting is __setting_exterior_place_hot__. __setting_conditions_hot__'] * 2 + ['The setting is __setting_exterior_place_cold__. __setting_conditions_cold__'] * 2
    return G

def build(final=FINAL, N=120):
    G = {}
    for root, suf in (('any_create_random_person_w_clothes', ''), ('any_create_random_person_w_clothes_short', '_short')):
        for b in BR:
            cl = clones(final, root, b, suf)
            for k, v in cl.items():
                G[k] = v
    for root, suf in (('any_create_random_person_w_clothes', ''), ('any_create_random_person_w_clothes_short', '_short')):
        for b in BR: G[f'any_person_age{b}_w_clothes{suf}'] = [f'__{root}__age{b}__']
    for rel in RELS:
        for mode in MODES:
            r = random.Random(zlib.crc32(f'{rel}{mode}'.encode()))
            G[f'group_{rel}' + ('' if mode == 'relationship' else '_' + mode)] = list(dict.fromkeys(line(rel, mode, r) for _ in range(N * 3)))[:N]
    for mode in MODES:
        sfx = '' if mode == 'relationship' else '_' + mode
        G['group_prompt' + sfx] = [f'__group_{rel}{sfx}__' for rel in RELS]
    G['group_relationships'] = [f'__group_{rel}__' for rel in RELS]; G['group_age_modes'] = [f'__group_prompt{"" if m == "relationship" else "_" + m}__' for m in MODES]
    G.update(settings(final))
    G['v52_entry_points'] = ['__group_prompt__', '__group_prompt_any_ages__', '__group_prompt_same_decade__', '__group_prompt_multigenerational__', '__setting_exterior__']
    return G
def run(final):
    G = build(final)
    for n, l in G.items(): _wr(final, n, l)
    print('v52:', len(G), 'files'); return G
def export_aoo(out, prefix='aoo_'):
    G = {k: v for k, v in build(FINAL).items() if k.startswith('setting_')}; names_ = set(G); n = 0   # the people system is not part of All Options Once
    for name, lines in G.items():
        keep = list(dict.fromkeys(REF.sub(lambda m: '__' + prefix + m.group(1) + '__' if (m.group(1) in names_ or os.path.exists(os.path.join(out, prefix + m.group(1) + '.txt'))) else m.group(0), l) for l in lines))
        _wr(out, prefix + name, keep); n += 1
    return n
if __name__ == '__main__':
    a = [x for x in sys.argv[1:] if os.path.isdir(x)]; run(os.path.abspath(a[0]) if a else FINAL)
