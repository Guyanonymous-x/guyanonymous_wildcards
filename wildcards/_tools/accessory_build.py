"""Accessory wildcard system: hats, backpacks, purses, wallets, necklaces, bracelets, rings, socks, canes/walking sticks.

Built from 9,000 supplied example prompts (data/accessories).  Every prompt follows one grammar:
    <grade word> <item type>, made of <material, construction>.  <shape/hardware sentences tied to the type>
    Designed by <tradition>, <palette>, its signature detail is <motif>, <technique>.
    Practical details ... / Whimsical touches ...      <decoration>   <finish>   <lining>
The examples are split back into those parts; every part becomes its own file, so the parts can be recombined at random into prompts nobody wrote.
Prices are ignored (price words are not used; the six "grades" are craft levels: basic, practical, standard, fine, luxury, showpiece).
Lines about children / babies / toddlers are left out and gender words are removed from item names (adult-only library).

Files per category <c> (backpack bracelet cane hat necklace purse ring sock wallet):
    acc_<c>_prompt            one full prompt (picks a grade at random)          acc_<c>_prompt_<grade>   one full prompt of that grade
    acc_<c>_short             one compact phrase: "a sturdy sling backpack made of waxed canvas, coloured in ..."
    acc_<c>_cluster_<grade>   grade word + item type + material + the shape/hardware sentences of that type
    acc_<c>_mat_*_<grade>     material with its construction method          acc_<c>_design    tradition + palette + signature motif
    acc_<c>_tech_<grade>      technique of the motif                         acc_<c>_extras     practical details / whimsical touches (or nothing)
    acc_<c>_practical_pair, acc_<c>_whimsy_pair (pools)                     acc_<c>_trim_/finish_/lining_<grade>
Shared: acc_adj_<grade> (with article), acc_adjbare_<grade>, acc_prompt (any category), acc_short_any, acc_wear (a person wearing/carrying 1-3 of them)
Usage: python accessory_build.py [wildcards_folder]       export_aoo(outdir) feeds simple_build.py
"""
import os, re, sys, csv, random, zlib, collections
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from paths import FINAL, DATA
SRC = os.path.join(DATA, 'accessories')
CATS = ['backpack', 'bracelet', 'cane', 'hat', 'necklace', 'purse', 'ring', 'sock', 'wallet']
import acc_wardrobe as _aw
ALLNEW = list(_aw.NEW)
TIERS = ['economy', 'budget', 'mid', 'premium', 'luxury', 'ludicrous']
GRADE = dict(zip(TIERS, ['basic', 'practical', 'standard', 'fine', 'luxury', 'showpiece']))
GRADES = list(GRADE.values())
# grade words: price wording removed, a few craft words added
PRICE_WORDS = {'affordable', 'inexpensive', 'budget-friendly', 'value-minded', 'mid-priced', 'upscale', 'premium'}
ADD_ADJ = {'basic': ['plain', 'simple', 'mass-produced', 'unfussy'], 'practical': ['hard-wearing', 'serviceable', 'solid'],
           'standard': ['carefully made', 'well-built', 'tasteful'], 'fine': ['elegant', 'high-grade', 'finely made'],
           'luxury': ['bespoke', 'heirloom-quality', 'masterfully made'], 'showpiece': ['collector-grade', 'one-off', 'breathtaking']}
MINOR = re.compile(r"\b(kid|kids|kid's|kids'|child|children|children's|child's|toddler|toddlers|toddler's|baby|babies|infant|infants|junior|youth|school-age|schoolgirl|schoolboy)\b(?! alpaca)", re.I)
GENDER = re.compile(r"\b(men's|women's|ladies'|ladies|gentlemen's|lady's|gentleman's|boys'|girls')\s+", re.I)
SPLIT_S = re.compile(r'(?<=\.) (?=[A-Z])')
FRAMES = {' in': ', coloured in', ', with enamel accents in': ', with enamel accents in', ', finished in': ', finished in', ', in shades of': ', in shades of', ', with accents in': ', with accents in'}
FRAME_RE = re.compile(r'^(, with enamel accents in|, with accents in|, in shades of|, finished in| in)\s+(.*)$')

def rng_of(*k): return random.Random(zlib.crc32('|'.join(map(str, k)).encode('utf8')))
def clean(s): return GENDER.sub('', s).strip()

def load():
    meta = collections.defaultdict(list)
    for r in csv.DictReader(open(os.path.join(SRC, 'meta.csv'), encoding='utf8')): meta[r['cat']].append(r)
    out = {}
    for c in CATS:
        L = open(os.path.join(SRC, f'{c}_prompts.txt'), encoding='utf8').read().split('\n')
        rows = []
        for l, r in zip(L, meta[c]):
            if MINOR.search(r['item_type']) or MINOR.search(l.split(' designed by')[0]): continue      # adult-only
            m = re.match(r'^(A pair of |An? )(.+?) ' + re.escape(r['item_type']) + r' designed by (?:an? |the )?' + re.escape(r['design_tradition']) + r', made of (.+?)\.(?= [A-Z]|$)(.*)$', l)
            if not m: continue
            art, adj, rest, tail = m.groups(); mat = r['material']
            if not rest.startswith(mat): continue
            after = rest[len(mat):]; i = after.rfind(', '); con = after[i + 2:]; mid = after[:i]
            if con == 'finished seams' and ', ' in mid: j = mid.rfind(', '); con = mid[j + 2:] + ', ' + con; mid = mid[:j]
            if mid.endswith(', hand-cut') and con.startswith('hand-skived'): con = 'hand-cut, ' + con; mid = mid[:-len(', hand-cut')]
            fm = FRAME_RE.match(mid)
            if not fm: continue
            sents = SPLIT_S.split(tail.strip()) if tail.strip() else []
            rows.append(dict(grade=GRADE[r['tier']], type=clean(r['item_type']), trad=r['design_tradition'], adj=adj, pair=art.startswith('A pair'), mat=mat, con=con,
                             frame=FRAMES[fm.group(1)], pal=fm.group(2), sents=[clean(s) for s in sents]))
        out[c] = rows
    return out

def slot(s, techs):
    if re.match(r'^Practical details include ', s): return 'practical'
    if re.match(r'^Whimsical touches include |^Alongside .* for playfulness\.$|^(It|They) balances? .* with the whimsy of ', s): return 'whimsy'
    if re.match(r'^(It|They) (is|are) (lined|unlined)|^(It|They) (is|are) finished inside|^The (interior|inside) (is|are)|^Inside (is|are)', s): return 'lining'
    if re.match(r'^(Its|Their) signature detail (is|are) |^(It|They) features? ', s):
        body = s.rstrip('.'); k = body.rfind(', ')
        if k > 0 and body[k + 2:] in techs: return 'motif'
    if re.match(r'^(It|They) (is|are) (set|studded|finished|adorned|decorated|trimmed) with|^(It|They) finish(es)? with', s): return 'trim'
    if re.match(r'^(It|They) (has|have) (an?|the) [^.]*(finish|finishes|polish|sheen|patina)\.$|^(It|They) (is|are) (hand-)?(polished|burnished|hand-burnished|hand-polished|finished in)\b', s): return 'finish'
    return 'other'

def split_pair(text, known):
    """'A and B' -> [A, B] using the already known single items"""
    if ' and ' not in text: return [text]
    parts = text.split(' and ')
    for k in range(1, len(parts)):
        a, b = ' and '.join(parts[:k]), ' and '.join(parts[k:])
        if a in known or b in known: return [a, b]
    return None

def build_cat(c, rows):
    F = {}; rep = {}
    # --- techniques per grade: last-comma suffix of signature sentences that repeats often
    suf = collections.Counter()
    for r in rows:
        for s in r['sents']:
            if re.match(r'^(Its|Their) signature detail (is|are) |^(It|They) features? ', s):
                b = s.rstrip('.'); k = b.rfind(', ')
                if k > 0: suf[b[k + 2:]] += 1
    techs = {t for t, n in suf.items() if n >= 6}
    by = collections.defaultdict(lambda: collections.defaultdict(list)); motifs = collections.defaultdict(set); pals = collections.defaultdict(set)
    kp, kw = set(), set(); pr, wh = [], []
    for r in rows:
        g = r['grade']; pals[r['trad']].add((r['frame'], r['pal'])); present = set()
        other = []
        for s in r['sents']:
            sl = slot(s, techs)
            if sl == 'motif':
                b = s.rstrip('.'); k = b.rfind(', '); head, tech = b[:k], b[k + 2:]
                mm = re.match(r'^(?:Its|Their) signature detail (?:is|are) (.+)$', head) or re.match(r'^(?:It|They) features? (.+)$', head)
                motifs[r['trad']].add(mm.group(1)); by[g]['tech'].append(tech); present.add('motif')
            elif sl in ('trim', 'finish', 'lining'): by[g][sl].append(s); present.add(sl)
            elif sl == 'practical': pr.append(s[len('Practical details include '):].rstrip('.')); present.add('practical')
            elif sl == 'whimsy':
                m1 = re.match(r'^Whimsical touches include (.+)\.$', s); m2 = re.match(r'^Alongside (.+?), (?:it|they) adds? (.+) for playfulness\.$', s); m3 = re.match(r'^(?:It|They) balances? (.+?) with the whimsy of (.+)\.$', s)
                if m1: wh.append(('pair', m1.group(1)))
                elif m2: kp.add(m2.group(1)); kw.add(m2.group(2)); present.add('whimsy')
                elif m3: kp.add(m3.group(1)); kw.add(m3.group(2)); present.add('whimsy')
            else: other.append(s)
        r['other'] = other; r['present'] = present; by[g]['n'].append(1)
    # practical / whimsy single-item pools
    pitems, witems = set(kp), set(kw)
    prs = [p for p in pr]; whs = [w for k, w in wh]
    for _ in range(3):
        for p in prs:
            sp = split_pair(p, pitems)
            if sp: pitems.update(sp)
        for w in whs:
            sp = split_pair(w, witems)
            if sp: witems.update(sp)
    pitems = {x for x in pitems if x and not MINOR.search(x)}; witems = {x for x in witems if x and not MINOR.search(x)}
    rep['practical items'] = len(pitems); rep['whimsy items'] = len(witems)
    # --- grade words
    adjs = collections.defaultdict(set)
    for r in rows: adjs[r['grade']].add(r['adj'])
    # --- cluster lines (grade word + type + material ref + type-bound sentences)
    fam = {}
    tm = collections.defaultdict(set)
    for r in rows: tm[r['type']].add(r['mat'])
    sigs = {}
    for t, ms in tm.items(): sigs[t] = tuple(sorted(ms))
    famid = {}
    if c == 'hat':                                     # hats: the material depends on the kind of hat -> merge types with similar material sets into at most 10 families
        groups = [[{t}, set(ms)] for t, ms in tm.items()]
        while len(groups) > 10:
            best = None
            for i in range(len(groups)):
                for j in range(i + 1, len(groups)):
                    a, b = groups[i][1], groups[j][1]; sim = len(a & b) / len(a | b)
                    if best is None or sim > best[0]: best = (sim, i, j)
            _, i, j = best; groups[i][0] |= groups[j][0]; groups[i][1] |= groups[j][1]; del groups[j]
        for n, (ts, ms) in enumerate(sorted(groups, key=lambda g: -len(g[0]))):
            for t in ts: famid[t] = f'f{n + 1}'
    else:
        famid = {t: 'all' for t in tm}
    rep['material families'] = len(set(famid.values()))
    mats = collections.defaultdict(set); tg = collections.defaultdict(list)
    clusters = collections.defaultdict(set)
    for r in rows:
        g = r['grade']; fid = famid[r['type']]
        mats[(fid, g)].add(f"{r['mat']}, {r['con']}")
        lead = 'a pair of __acc_adjbare_%s__' % g if r['pair'] else '__acc_adj_%s__' % g
        line = f"{lead} {r['type']}, made of __acc_{c}_mat_{fid}_{g}__."
        if r['other']: line += ' ' + ' '.join(r['other'])
        clusters[g].add(line)
        tg[(r['type'], g, r['pair'])].append(r['other'])
    for (t, g, pair), lst in tg.items():                      # recombine the type-bound sentences of the same item type and grade, position by position
        r_ = rng_of(c, t, g); lead = 'a pair of __acc_adjbare_%s__' % g if pair else '__acc_adj_%s__' % g; fid = famid[t]
        for _ in range(12):
            base = r_.choice(lst); cur = []
            for k in range(len(base)):
                pool = [x[k] for x in lst if len(x) > k]; cur.append(r_.choice(pool))
            clusters[g].add(f"{lead} {t}, made of __acc_{c}_mat_{fid}_{g}__." + (' ' + ' '.join(cur) if cur else ''))
    # --- write files
    for g in GRADES:
        F[f'acc_{c}_cluster_{g}'] = sorted(clusters[g])
        for fid in sorted(set(famid.values())): F[f'acc_{c}_mat_{fid}_{g}'] = sorted(mats[(fid, g)]) or ['plain fabric, machine-sewn']
        ts = sorted(set(by[g]['tech'])); F[f'acc_{c}_tech_{g}'] = ts or ['executed with care']
        n = len(by[g]['n']) or 1
        for key, nm in (('trim', 'trim'), ('finish', 'finish'), ('lining', 'lining')):
            items = sorted(set(by[g][key])); have = len(by[g][key])
            blanks = int(round(len(items) * max(0, n - have) / max(1, have))) if items else 1
            F[f'acc_{c}_{nm}_{g}'] = items + [''] * blanks
    # design bundles: tradition x palette x motif (cross product, sampled, every observed palette and motif kept)
    design = []
    for t in sorted(motifs):
        pl = sorted(pals[t]); ml = sorted(motifs[t]); r = rng_of(c, t); combos = [(p, m) for p in pl for m in ml]; r.shuffle(combos)
        keep = combos[:max(40, min(len(combos), 60))]
        art = 'an' if t[0].lower() in 'aeiou' else 'a'
        for (fr, pal), m in keep: design.append(f"Designed by {art} {t}{fr} {pal}; its signature detail is {m}")
    F[f'acc_{c}_design'] = design
    # extras
    r = rng_of(c, 'extras'); pl = sorted(pitems); wl = sorted(witems)
    def pairs(items, n):
        out = set(); tries = 0
        while len(out) < n and tries < n * 8 and len(items) > 1:
            tries += 1; a, b = r.sample(items, 2); out.add(f'{a} and {b}')
        return sorted(out)
    F[f'acc_{c}_practical'] = pl; F[f'acc_{c}_whimsy'] = wl
    F[f'acc_{c}_practical_pair'] = pairs(pl, min(400, len(pl) * 4)); F[f'acc_{c}_whimsy_pair'] = pairs(wl, min(400, len(wl) * 4))
    pl_ = (c == 'sock'); he, it_, ad = ('They', 'they', 'add') if pl_ else ('It', 'it', 'adds'); ba = 'balance' if pl_ else 'balances'
    frames = ([f'Practical details include __acc_{c}_practical_pair__.'] * 4 + [f'Whimsical touches include __acc_{c}_whimsy_pair__.'] * 2 +
              [f'Alongside __acc_{c}_practical__, {it_} {ad} __acc_{c}_whimsy__ for playfulness.'] * 2 + [f'{he} {ba} __acc_{c}_practical__ with the whimsy of __acc_{c}_whimsy__.'] * 2 +
              [f'Practical details include __acc_{c}_practical_pair__. Whimsical touches include __acc_{c}_whimsy_pair__.'] * 1 + [''] * 4)
    F[f'acc_{c}_extras'] = frames
    # prompts
    for g in GRADES:
        F[f'acc_{c}_prompt_{g}'] = [f'__acc_{c}_cluster_{g}__ __acc_{c}_design__, __acc_{c}_tech_{g}__. __acc_{c}_extras__ __acc_{c}_trim_{g}__ __acc_{c}_finish_{g}__ __acc_{c}_lining_{g}__']
    F[f'acc_{c}_prompt'] = [f'__acc_{c}_prompt_{g}__' for g in GRADES]
    # short phrases (compact, for adding to a person prompt)
    shorts = set()
    for r in rows:
        aj = r['adj']
        if aj in PRICE_WORDS: aj = rng_of(c, 'short', r['type'], r['pal'], r['mat']).choice(ADD_ADJ[r['grade']])
        lead = ('a pair of ' + aj) if r['pair'] else (('an ' if aj[0] in 'aeiou' else 'a ') + aj)
        shorts.add(f"{lead} {r['type']} made of {r['mat']}{r['frame']} {r['pal']}")
    F[f'acc_{c}_short'] = sorted(shorts)
    import acc_expand; acc_expand.expand_cat(c, F, tg, famid, pitems, witems)
    if c == 'backpack':
        import acc_pack; acc_pack.run(F)
    import acc_novelty; acc_novelty.run(F, c)
    rep['types'] = len({r['type'] for r in rows}); rep['prompts used'] = len(rows); rep['design lines'] = len(design)
    return F, rep

def shared():
    F = {}
    src = collections.defaultdict(set)
    for r in load_cache: src[r['grade']].add((r['adj']))
    for g in GRADES:
        a = sorted({x for x in src[g] if x not in PRICE_WORDS} | set(ADD_ADJ[g]))
        import acc_expand; a = sorted(set(a) | set(acc_expand.adj_files()[g]))
        F[f'acc_adjbare_{g}'] = a
        F[f'acc_adj_{g}'] = [('an ' if x[0].lower() in 'aeiou' else 'a ') + x for x in a]
    return F

def person_bridge():
    F = {}
    verbs = {'backpack': ['carrying {}', 'wearing {} on the back', 'with {} slung over one shoulder', 'carrying {} by its top handle', 'wearing {} on both shoulders', 'with {} resting against the back'],
             'bracelet': ['wearing {} on the wrist', 'with {} around one wrist', 'showing {} on the forearm', 'wearing {} loosely at the wrist', 'with {} stacked on the arm'],
             'cane': ['holding {}', 'leaning on {}', 'walking with {}', 'resting a hand on {}', 'carrying {} at the side', 'gripping {} firmly'],
             'hat': ['wearing {}', 'with {} tilted slightly', 'wearing {} low over the brow', 'wearing {} pushed back on the head', 'holding {} in one hand', 'with {} set squarely on the head'],
             'necklace': ['wearing {} around the neck', 'with {} resting on the collarbone', 'wearing {} at the throat', 'with {} hanging at the chest', 'touching {} with one hand'],
             'purse': ['carrying {}', 'holding {} at the side', 'with {} over one shoulder', 'carrying {} on the forearm', 'holding {} close to the body', 'with {} hanging from the crook of the arm'],
             'ring': ['wearing {} on a finger', 'showing {} on the left hand', 'with {} on the right hand', 'wearing {} on the index finger', 'with {} on the ring finger', 'holding up one hand to show {}'],
             'sock': ['wearing {}', 'with feet in {}', 'showing {} above the shoes', 'wearing {} pulled up', 'wearing {} with the cuffs folded down'],
             'wallet': ['holding {}', 'with {} in a hand', 'taking {} from a pocket', 'holding {} open', 'carrying {} in a back pocket', 'with {} tucked under one arm']}
    import acc_wardrobe; verbs.update(acc_wardrobe.verbs())
    one = []
    if not SKIP_SHOE: verbs['shoe'] = ['wearing {}']
    CC = CATS + ALLNEW + ([] if SKIP_SHOE else ['shoe'])
    for c in CC:
        for v in verbs[c]: one.append(v.format(f'__acc_shoe_worn__' if c == 'shoe' else f'__acc_{c}_short__'))
    F['acc_short_any'] = [f'__acc_{c}_short__' for c in CATS + ALLNEW] + ([] if SKIP_SHOE else ['__acc_shoe_worn__'])
    F['acc_wear_one'] = one
    import acc_expand; rw = acc_expand.rngk('wear'); ws = set(one)
    while len(ws) < 520:
        k = rw.choice((2, 2, 3)); ws.add(', '.join(rw.sample(one, k)))
    F['acc_wear'] = sorted(ws)
    import acc_pack as _ap; F['acc_colour'] = _ap.colour_lines()
    F['acc_prompt'] = [f'__acc_{c}_prompt__' for c in CATS + ALLNEW] + ([] if SKIP_SHOE else ['__acc_shoe_prompt__'])
    for g in ('f', 'm'):
        F[f'{g}_prompt_accessorized'] = [f'__{g}_prompt_master_by_age__ Accessories: __acc_wear__.', f'__{g}_prompt_master_by_age__ Accessory detail: __acc_wear_one__.']
    return F

load_cache = []
SKIP_SHOE = False
def run(final):
    global load_cache
    data = load(); load_cache = [r for rows in data.values() for r in rows]
    files = {}; reps = {}
    for c in CATS:
        F, rep = build_cat(c, data[c]); files.update(F); reps[c] = rep
    import acc_wardrobe; files.update(acc_wardrobe.build_all())
    files.update(shared()); files.update(person_bridge())
    for n, lines in files.items():
        lines = [l for l in lines]
        assert not any(re.search(r'[{}|]', l) for l in lines), n
        open(os.path.join(final, n + '.txt'), 'w', encoding='utf8', newline='\n').write('\n'.join(lines) + '\n')
    print(f'accessories: {len(files)} files;', {c: (r["prompts used"], r["types"], r["design lines"]) for c, r in reps.items()})
    return files

def export_aoo(out, prefix='aoo_'):
    import shutil
    global SKIP_SHOE
    SKIP_SHOE = True
    tmp = os.path.join(out, '_acc_tmp'); os.makedirs(tmp, exist_ok=True); files = run(tmp); shutil.rmtree(tmp); SKIP_SHOE = False
    names = set(files) | {'acc_artwork'}; ref = re.compile(r'__([A-Za-z0-9_\-/]+)__'); n = 0
    for name, lines in files.items():
        if name.startswith(('f_', 'm_')): continue
        seen = set(); keep = []
        for l in lines:
            if not l.strip() or l in seen: continue
            seen.add(l); keep.append(ref.sub(lambda m: '__' + prefix + m.group(1) + '__' if m.group(1) in names else m.group(0), l))
        if not (name.endswith(tuple('_prompt_' + g for g in GRADES)) or name.endswith('_prompt') or name == 'acc_prompt'): random.Random(zlib.crc32(name.encode())).shuffle(keep)
        open(os.path.join(out, prefix + name + '.txt'), 'w', encoding='utf8', newline='\n').write('\n'.join(keep) + '\n'); n += 1
    p = lambda t: f'__{prefix}{t}__'
    open(os.path.join(out, prefix + 'prompt_accessorized.txt'), 'w', encoding='utf8').write(f'{p("prompt_full")} Accessories: {p("acc_wear")}.\n')
    return n + 1

if __name__ == '__main__':
    a = [x for x in sys.argv[1:] if os.path.isdir(x)]
    run(os.path.abspath(a[0]) if a else FINAL)
