"""Rewrites the user's 141-line showcase list one-to-one in the v106 layout: 2x3 grids, same person per feature, close-ups of the part, captions."""
import sys, re, random
import body_showcase2 as S
B = S.B
SRC = '/mnt/user-data/attachments/f4f177e0-8597-507c-b7de-4fd3dcc5cfda/2e930e10-attachment.txt'
OD = '/mnt/user-data/outputs/'
SPEC = {sp['key']: sp for sp in B.SPECS}
ORD6 = ['first', 'second', 'third', 'fourth', 'fifth', 'sixth']
HAIRK = ['hair_curly', 'hair_kinky', 'hair_straight', 'hair_wavy']; hair_i = [0]
TURN = S.TURN; GREY = S.GREYBG
def pick(L, sex, frame, c0):
    L = re.sub(r"^(?:the )+(?:woman|man)'s ", '', L.strip()).lower()
    w = sex == B.W
    if L.startswith('adult expressions'): return SPEC['expr_adult_l12']
    if L == 'penis': return SPEC['penis_erect' if 'erect' in c0 else 'penis_flaccid']
    if L.startswith('buttocks'): return SPEC['buttocks_f' if w else 'buttocks_m']
    if L.startswith('anal'): return SPEC['anus_f' if w else 'anus_m']
    if L.startswith('pubic'): return SPEC['pubic_hair_f']
    if L == 'hairstyle':
        k = HAIRK[hair_i[0] % 4]; hair_i[0] += 1; return SPEC[k]
    if L == 'skin colour':
        return SPEC['skin_body' if c0.startswith('bare shoulders') else 'skin_heritage' if 'undertone' in c0 and 'face' in c0 else 'skin_face']
    if L == 'nose': return SPEC['nose_profile' if 'profile' in frame else 'nose']
    for sp in B.SPECS:
        if S.label(sp).lower() == L: return sp
    for sp in B.SPECS:
        if S.label(sp).lower() in L or L in S.label(sp).lower(): return sp
    raise SystemExit('no spec for ' + L)
STRIP = r'^(?:an? )?(?:legs and hips|bare shoulders and upper arms|chest|face|eyes|lips|hands|feet|fingernails|ears|nose|neck|figure|hair) (?:with|that are|that is) '
def fix(c):
    c = S.tidy(c); c = re.sub(STRIP, '', c); c = re.sub(r'^(?:her|his) ', '', c)
    c = re.sub(r'(?:an? )?(?:deep|deeply) (?:central )?cleft(?:ed)?(?: chin)?', 'a small shallow dimple low on the chin tip', c)
    c = re.sub(r'\bchin with a small shallow dimple low on the chin tip', 'chin with a small shallow dimple low on its tip', c)
    return re.sub(r'\s+', ' ', c).strip().rstrip('.').rstrip(',')
def cells_of(l):
    body = l.split('The first panel:', 1)[1]; body = re.split(r'" --steps', body)[0]
    parts = re.split(r' The (?:second|third|fourth|fifth|sixth|seventh|eighth|ninth) panel: ', ' ' + body.strip()); return [p.strip() for p in parts]
def build():
    src = open(SRC, encoding='utf8').read().split('\n'); out = []
    for ln, l in enumerate(src, 1):
        if not l.strip(): continue
        lora = '<lora' in l; seed = int(re.search(r'--seed (\d+)', l).group(1)); portrait = '--width 832' in l
        hdr = l.split('The first panel:')[0]
        if 'separate photographic scene' in hdr: continue
        raw = cells_of(l); r = random.Random(seed)
        sex = B.W if re.search(r'adult woman|adult women|women', hdr.split('Every panel is', 1)[1][:300]) and 'adult man' not in hdr[:600] else B.M
        who = 'woman' if sex == B.W else 'man'
        cells = []; seen = set(); caplab = None
        if 'separate photographic scene' in hdr:
            caplab = 'Pose scene'
            for c in raw:
                t = S.cap(re.sub(r'\s+', ' ', c).strip().rstrip('.')) + '.'
                if t in seen: continue
                seen.add(t); n = 'one person' if re.match(r'^(A|An) (man|woman|nonbinary adult|person)\b', t) and not re.search(r'\b(second|another|two|each other|partner)\b', t) else 'the people described'
                cells.append(S.wrap(t + ' Each person in this panel has one head, two arms and two legs, and every hand, foot and limb belongs to the person it is described with.', n_people=n))
        else:
            m = re.search(r'Every panel is (.+) of a different (adult (?:woman|man)(?: in (?:her|his) [a-z ]+)?)', hdr)
            frame, subj = (m.group(1), 'an ' + m.group(2)) if m else ('', 'an adult ' + who)
            if 'sportswear' in hdr:
                caplab = 'Pose'; ident = S.pid(who, r, key='pose_' + who); col = S.PCOL.setdefault(('pose_' + who, who), random.Random(seed).choice(S.COL))
                for c in raw:
                    c = re.sub(r'\s+', ' ', c).strip().rstrip('.'); c0 = c
                    if c in seen: continue
                    seen.add(c); cells.append(S.pan(ident, 'A full-length view in plain fitted %s sportswear, %s. The pose: %s.' % (col, TURN, c), S.LIMB, 'pose'))
            elif 'bare skin on a different' in hdr:
                caplab = 'Skin marks'; ident = S.pid(who, r, hair=False, key='skin_marks')
                for c in raw:
                    c = re.sub(r'^a close-up showing ', '', re.sub(r'\s+', ' ', c)).strip().rstrip('.')
                    if c in seen: continue
                    seen.add(c); cells.append(S.pan(ident, 'A close-up of the bare skin where the mark is, %s. The skin mark: %s.' % (TURN, c), '', 'skin mark'))
            elif 'showing the tattoo' in hdr:
                caplab = 'Tattoos'; ident = S.pid(who, r, hair=False, key='tattoo')
                for c in raw:
                    c = re.sub(r'\s+', ' ', c).strip().rstrip('.')
                    if c in seen: continue
                    seen.add(c); cells.append(S.pan(ident, 'A close-up of the tattooed area of bare skin, %s. The tattoo: %s.' % (TURN, c), '', 'tattoo'))
            elif re.search(r'and the makeup fills', hdr):
                caplab = 'Makeup'; ident = S.pid(who, r, key='makeup')
                for c in raw:
                    c = re.sub(r'^Special makeup, ', '', re.sub(r'\s+', ' ', c), flags=re.I).strip().rstrip('.')
                    if c in seen: continue
                    seen.add(c); cells.append(S.pan(ident, 'A tight close-up of the face with the head turned about thirty degrees toward the left side of the frame, so that the front of the face and a little of its side are both in view. The makeup: %s.' % c, '', 'makeup'))
            else:
                mm = re.search(r'and the (.+?) fills the whole panel', hdr) or re.search(r'with its own (\w+)\.', hdr)
                if not mm: raise SystemExit('line %d: no label' % ln)
                sp = pick(mm.group(1), sex, frame, raw[0]); lab = S.label(sp); caplab = lab
                ident = S.identity(sp, sex, r)
                if frame.startswith(('a close-up of', 'an extreme close-up of')) and 'clinical' not in frame:
                    fr = re.sub(r'bare forearm and hand', 'one hand', frame)
                    v = S.cap(fr) + ', ' + ('with the head turned about thirty degrees toward the left side of the frame so that the front and a little of the side are both in view' if sp['key'] in S.HEADK or 'eye' in fr else TURN)
                elif 'behind' in frame and sp['key'].startswith('hair'):
                    v = 'A head and shoulders view from behind, with the head turned about thirty degrees toward the left side of the frame so that the back and a little of the side of the hair are both in view'
                else:
                    v = S.view(sp, frame)
                if v is None: v = S.cap(S.frame_phrase(frame, re.sub(r'^an adult', 'the same adult', subj)))
                ex = S.LIMB if sp['key'] in S.LIMBKEYS else ' The hand has five fingers and belongs to one arm.' if sp['key'] in ('hands', 'nails') else ' The foot has five toes.' if sp['key'] == 'feet' else ''
                for c in raw:
                    c = fix(c)
                    if not c or c in seen: continue
                    seen.add(c)
                    cells.append('(This panel is a photograph of exactly one person, the same %s, %s, and nothing else from any other panel appears in it. %s. %s: %s.%s Everything about this person other than the feature listed under %s is identical to the other panels.)' % (ident, S.GREYBG, v, lab, c, ex, lab))
        cells = cells[:6]
        if len(cells) < 6: print('line', ln, 'only', len(cells), 'cells')
        cl = ' In the bottom left corner of this panel there is small plain white text reading “%s”.' % caplab
        lay = 'three rows of two columns' if portrait else 'two rows of three columns'
        focus = 'feature' if caplab not in ('Pose scene',) else ''
        if caplab == 'Pose scene': head = 'A grid of 6 equal photographic panels arranged in %s, separated by thin plain white gaps. Every panel is a separate scene with its own person or people, and nothing is shared between panels.' % lay
        else: head = 'A grid of 6 equal photographic panels arranged in %s, separated by thin plain white gaps. Every panel shows the same person in the same light against the same background; only the feature listed under %s changes from panel to panel.' % (lay, caplab)
        t = ' '.join((head + ' ' + ' '.join('The %s panel: %s' % (ORD6[i], c) for i, c in enumerate(cells))).split())
        t += S.tail(caplab)
        out.append((ln, seed, lora, portrait, caplab, t))
    return out
if __name__ == '__main__':
    out = build(); rows = {0: [], 1: []}; key = ['old_line\tseed\tcaption\tchars\tcheck']
    for ln, seed, lora, portrait, cl, t in out:
        sz = B.sizes(2, 3) if portrait else B.sizes(3, 2)
        for k in (0, 1):
            w, h = sz[k]; rows[k].append('--prompt "%s%s" --steps 50 --cfg_scale 3.75 --seed %d --width %d --height %d' % ('<lora:MOSSwSh4rpD3tails:0.5> ' if lora else '', t.replace('"', '\\"'), seed, w, h))
        chk = [x for x, bad in (('token', '__' in t or '@@' in t), ('spacing', '  ' in t), ('cleft', 'cleft' in t.lower() and 'chin' in t.lower())) if bad]
        key.append('%d\t%d\t%s\t%d\t%s' % (ln, seed, cl, len(t), ';'.join(chk) or 'ok'))
    for k, n in ((0, '1024'), (1, '1408')): open(OD + 'Guyanonymous_Wildcards_v106_showcase_list_%s.txt' % n, 'w', encoding='utf8').write('\n'.join(rows[k]))
    open(OD + 'Guyanonymous_Wildcards_v106_showcase_list_key.tsv', 'w').write('\n'.join(key)); print(len(out), 'prompts')
