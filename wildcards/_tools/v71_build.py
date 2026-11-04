"""v71: anchor pass (pronoun-start sentences replaced by named or chained wording), applied to the finished wildcard files.
   python _tools/v71_build.py            -> apply (originals are copied once to _tools/backup_v70/)
   python _tools/v71_build.py --dry      -> count what would change, write nothing
   python _tools/v71_build.py --restore  -> put the originals back
 Run it LAST after any rebuild (build_all.py, v42_people.py, v48/v50_build.py write the old wording again).  It is idempotent.
 1. furniture  furn_*.txt   'It has A. It has B. Its material is C.'  ->  'The X has A and B, and its material is C.'
 2. rooms      room_*_prompt_full.txt   'The room is a bedroom. It is large ...' -> 'The room is a bedroom. The bedroom is large ...'
 3. people     lines with 'A man|A woman|This person, <age>, from __countries__.'  ->  one chained sentence per person
               ('A man, 40 years old, from Syria, has eyes, hair and skin, has a build described as X, and is wearing Y.');
               aging_summary pieces and stray 'He/She/They is wearing' sentences get a noun instead of a pronoun."""
import os, re, sys, glob, shutil
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from paths import FINAL
BACKUP = os.path.join(HERE, 'backup_v70')
REF = r'__[A-Za-z0-9_\-/]+__'
SPLIT = re.compile(r'(?<=[a-z_\}\.])\.\s+(?=[A-Z_])')

# ------------------------------------------------------------------ 1. furniture
def noun_of(first):
    m = re.match(r'^(?:an? )?([a-z][a-z \-]*?)\.$', first.strip())
    if m: return m.group(1)
    m = re.match(r'^The ([a-z][a-z \-]*?) (?:has|is|stands|sits|hangs|features|comes)\b', first)
    return m.group(1) if m else None
def anchor_furn(line):
    ss = SPLIT.split(line.strip()); ss = [s if s.endswith('.') else s + '.' for s in ss]
    if not any(re.match(r'^(It|Its|It also|Inside it) ', s) for s in ss): return line
    noun = None
    for s in ss:
        noun = noun_of(s)
        if noun: break
    if not noun:
        m = re.search(r'__furn_([a-z0-9_]+?)_(?:shape|type|length|size|finish|colour|material|feet|taps|fabric|blades|panels|frame|top|body|seat|base|heading|rail|controls|pattern|pile)', line)
        if m: noun = m.group(1).replace('_', ' ')
    if not noun: return line
    The = 'The ' + noun
    out = []; has = []; tails = []
    def flush():
        nonlocal has, tails
        if has or tails:
            tl = ['its %s is %s' % (a, v) for a, v in tails]
            tj = (', '.join(tl[:-1]) + ' and ' + tl[-1]) if len(tl) > 1 else (tl[0] if tl else '')
            if has:
                body = (', '.join(has[:-1]) + ' and ' + has[-1]) if len(has) > 1 else has[0]
                out.append('%s has %s%s.' % (The, body, (', and ' + tj) if tj else ''))
            else:
                a0, v0 = tails[0]; rest = tl[1:]
                rj = (', '.join(rest[:-1]) + ' and ' + rest[-1]) if len(rest) > 1 else (rest[0] if rest else '')
                out.append("%s's %s is %s%s." % (The, a0, v0, (', ' + rj) if rj else ''))
        has = []; tails = []
    for s in ss:
        s0 = s.rstrip('.')
        m = re.match(r'^%s has (.*)$' % re.escape(The), s0)
        if m and not has: has.append(m.group(1)); continue
        m = re.match(r'^(?:It|It also) has (.*)$', s0)
        if m and (has or out or tails): has.append(m.group(1)); continue
        m = re.match(r'^Its (\w+) is (.*)$', s0)
        if m: tails.append((m.group(1), m.group(2))); continue
        m = re.match(r'^(Inside )?[Ii]t (stands|sits|rests|hangs|is|looks|has) (.*)$', s0)
        if m and m.group(1):
            flush(); out.append('Inside, %s %s %s.' % (The.lower(), m.group(2), m.group(3))); continue
        if m:
            flush(); out.append('%s %s %s.' % (The, m.group(2), m.group(3))); continue
        flush(); out.append(s)
    flush()
    return ' '.join(out)
NONE_FIX = {'furn_blanket_chest_hardware': ('none', 'no metal hardware'), 'furn_blanket_chest_feet': ('none', 'no feet, resting flat on the floor'), 'furn_conference_table_extras': ('none', 'no extra fittings'), 'furn_kitchen_island_extras': ('none', 'no extra fittings'), 'furn_reception_desk_extras': ('none', 'no extra fittings'), 'furn_shoe_rack_extras': ('none', 'no extra fittings')}

# ------------------------------------------------------------------ 2. room openers
def opener_fix(l):
    m = re.match(r'^The room is (an?) ([^.]+)\. It is (.*?)\. (.*)$', l)
    if not m: return l
    art, n = m.group(1), m.group(2)
    return 'The room is %s %s. The %s is %s. %s' % (art, n, n, m.group(3), m.group(4).replace('It contains', 'The %s contains' % n, 1))

# ------------------------------------------------------------------ 3. people
NOUN = {'He': 'The man', 'She': 'The woman', 'They': 'This person'}
POSN = {'His': 'The man', 'Her': 'The woman', 'Their': 'This person'}
def third(v):
    if v in ('are', 'is'): return 'is'
    if v in ('have', 'has'): return 'has'
    if v in ('do', 'does'): return 'does'
    if re.search(r'(sh|ch|ss|x|o)$', v): return v + 'es'
    if re.search(r'[^aeiou]y$', v): return v[:-1] + 'ies'
    return v if v.endswith('s') and v not in ('look',) else v + 's'
def anchor_pron(text):
    """sentence-initial He/She/They/His/Her/Their -> noun; verbs made singular. Mid-sentence pronouns are left alone."""
    parts = re.split(r'(?<=\.)(\s+)', text); out = []
    for p in parts:
        m = re.match(r'^(He|She|They) (\w+)(.*)$', p, re.S)
        if m:
            n = NOUN[m.group(1)]; v = m.group(2)
            p = '%s %s%s' % (n, third(v) if m.group(1) == 'They' else v, m.group(3))
        else:
            m = re.match(r"^(His|Her|Their) (.*)$", p, re.S)
            if m: p = "%s's %s" % (POSN[m.group(1)], m.group(2))
        out.append(p)
    return ''.join(out)
HDR = re.compile(r'(A man|A woman|This person), (%s), from (__countries__)\. ' % REF)
PRO = r'(?:He|She|They)'; POS = r'(?:His|Her|Their|his|her|their)'
BG1 = re.compile(r'(A man|A woman|This person), (%s)\. (?:His|Her|Their) background (?:is|are) (%s)\.' % (REF, REF))
BG2 = re.compile(r'(?:He|She|They) (?:is|are) a (believable, real-looking (?:man|woman|person)) who (?:is|are) (%s), and (?:his|her|their) background (?:is|are) (%s)\.' % (REF, REF))
def person_line(line):
    l2 = BG2.sub(lambda m: 'A %s, %s, whose background is %s.' % (m.group(1), m.group(2), m.group(3)), BG1.sub(r'\1, \2, whose background is \3.', line))
    if l2 != line: return anchor_pron_tail(l2)
    m = HDR.search(line)
    if not m: return line
    pre = line[:m.start()]; subj, age, country = m.groups(); rest = line[m.end():]
    sentences = re.split(r'(?<=\.)\s+', rest.strip()); preds = []; others = []
    for s in sentences:
        lead = re.match(r'^((?:%s\s*)+)(.*)$' % REF, s)
        if lead: others.append(lead.group(1).strip()); s = lead.group(2)
        if not s: continue
        s0 = s.rstrip('.')
        if m2 := re.match(r'^%s coloring (?:is|are) (.+)$' % POS, s0): preds.append('has ' + m2.group(1)); continue
        if m2 := re.match(r'^%s (?:has|have) (.+, styled as .+)$' % PRO, s0): preds.append('has ' + m2.group(1)); continue
        if m2 := re.match(r'^%s (?:has|have) (.+?) and %s build (?:is|are) (.+)$' % (PRO, POS), s0): preds += ['has ' + m2.group(1), 'has a build described as ' + m2.group(2)]; continue
        if m2 := re.match(r'^%s build (?:is|are) (.+)$' % POS, s0): preds.append('has a build described as ' + m2.group(1)); continue
        if m2 := re.match(r'^%s looks? about (\w+) years (older|younger) than %s stated age$' % (PRO, POS), s0): preds.append('looks about %s years %s than the stated age' % (m2.group(1), m2.group(2))); continue
        if m2 := re.match(r'^%s (?:is|are) bare-chested and (?:is|are) wearing (.+)$' % PRO, s0): preds.append('is bare-chested and wearing ' + m2.group(1)); continue
        if m2 := re.match(r'^%s (?:is|are) wearing (.+)$' % PRO, s0): preds.append('is wearing ' + m2.group(1)); continue
        if re.match(r'^%s (?:is|are) nude$' % PRO, s0): preds.append('is nude'); continue
        others.append(anchor_pron(s if s.endswith('.') else s + '.')) if re.match(r'^(He|She|They|His|Her|Their) ', s) else others.append(s)
    if not preds: return line
    chain = preds[0] if len(preds) == 1 else ', '.join(preds[:-1]) + ', and ' + preds[-1]
    return '%s%s, %s, from %s, %s.%s' % (pre, subj, age, country, chain, (' ' + ' '.join(others)) if others else '')
def person_file(name, lines):
    out = []
    for l in lines:
        n = person_line(l)
        if n == l and re.search(r'(^|\.\s|\s)(He|She|They) (is|are) (wearing|nude|bare-chested)', l) and not HDR.search(l): n = anchor_pron_tail(l)
        out.append(n)
    return out
def anchor_pron_tail(l):
    # lines made of piece references followed by a pronoun sentence: anchor only the sentences that start with a pronoun
    return re.sub(r'(?<=[\.\s])(He|She|They) (is|are) ', lambda m: '%s is ' % NOUN[m.group(1)], l)

# ------------------------------------------------------------------ driver
def read(p): return [l.rstrip('\r\n') for l in open(p, encoding='utf8', errors='replace')]
def write(p, lines): open(p, 'w', encoding='utf8', newline='\n').write('\n'.join(lines) + '\n')
def main():
    dry = '--dry' in sys.argv
    if '--restore' in sys.argv:
        for f in glob.glob(os.path.join(BACKUP, '*.txt')): shutil.copy2(f, os.path.join(FINAL, os.path.basename(f)))
        print('restored', len(glob.glob(os.path.join(BACKUP, '*.txt'))), 'files'); return
    stats = {'furn': [0, 0], 'room': [0, 0], 'person': [0, 0], 'aging': [0, 0]}
    for p in sorted(glob.glob(os.path.join(FINAL, '*.txt'))):
        name = os.path.basename(p)[:-4]; L = read(p); new = None; kind = None
        if name.startswith('furn_'):
            kind = 'furn'; new = [anchor_furn(l) if re.search(r'(^|\.\s)(It|Its|It also|Inside it) ', l) else l for l in L]
            if name in NONE_FIX: a, b = NONE_FIX[name]; new = [b if l.strip() == a else l for l in new]
        elif re.match(r'^room_.*_prompt_full$', name): kind = 'room'; new = [opener_fix(l) for l in L]
        elif re.search(r'aging_summary', name): kind = 'aging'; new = [anchor_pron(l) for l in L]
        elif any('from __countries__.' in l or 'background is' in l or re.search(r'(^|\.\s|\s)(He|She|They) (is|are) (wearing|nude|bare-chested)', l) for l in L) and re.search(r'create_random|person|prompt_char|demo', name):
            kind = 'person'; new = person_file(name, L)
        if new is None: continue
        stats[kind][0] += 1
        if new != L:
            stats[kind][1] += sum(a != b for a, b in zip(L, new))
            if not dry:
                os.makedirs(BACKUP, exist_ok=True)
                b = os.path.join(BACKUP, name + '.txt')
                if not os.path.exists(b): shutil.copy2(p, b)
                write(p, new)
    print('files scanned / lines changed', stats)
if __name__ == '__main__': main()
