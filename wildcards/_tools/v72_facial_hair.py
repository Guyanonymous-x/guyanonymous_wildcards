#!/usr/bin/env python3
"""v72 facial hair pass (backlog item 52).

Tested 2026-11-03 on Moss (10 images): named beard styles are weak, positive physical
descriptions work. Every named style becomes a plain description of where the hair grows
and where the skin is bare; shaved faces use positive wording ("smooth, shiny, hairless
... like freshly shaved skin"). Modifiers that contradict the description are dropped.
The template sentence "His/Their facial hair is X." becomes "His/Their lower face has X."
so both hair and bare-skin lines read correctly.

Usage:  python _tools/v72_facial_hair.py [--dry] [--restore]
Run it LAST after any rebuild (like v71_build.py); it is idempotent.
Originals are saved in _tools/backup_v71/ the first time it runs.
"""
import glob, os, re, shutil, sys, collections

HERE = os.path.dirname(os.path.abspath(__file__))
LIB = os.path.dirname(HERE)
BK = os.path.join(HERE, 'backup_v71')
DRY = '--dry' in sys.argv

BARE = "smooth, hairless cheeks"
S = "smooth, hairless"

# (regex for the head of the line, description, modifier class)
HEADS = [
 # ---- shaved and bare faces
 (r'(a )?clean-shaven face with a defined jawline', 'smooth, shiny, hairless skin on the chin, cheeks and upper lip, like freshly shaved skin, with a defined jawline', 'NONE'),
 (r'(a )?clean-shaven smooth jaw', 'smooth, shiny, hairless skin on the chin, cheeks and upper lip, like freshly shaved skin', 'NONE'),
 (r'clean-shaven face', 'smooth, shiny, hairless skin on the chin, cheeks and upper lip, like freshly shaved skin', 'SHAVED'),
 (r'(a )?smooth shaved chin and upper lip', 'smooth, shiny, hairless skin on the chin, cheeks and upper lip, like freshly shaved skin', 'NONE'),
 (r'(a )?freshly shaved face with a faint shadow', 'smooth, hairless skin on the cheeks and upper lip, with only a faint dark shadow along the jaw and chin', 'NONE'),
 (r'nearly clean-shaven face with a shadow', 'smooth, hairless skin on the cheeks and upper lip, with only a faint dark shadow along the jaw and chin', 'SHAVED'),
 (r'beardless chin with a mustache', 'a neat mustache on the upper lip, with smooth, shiny, hairless skin on the chin and cheeks', 'SHAVED'),
 (r'long sideburns with a shaved chin', 'long sideburns running down both sides of the face to the jaw, with smooth, shiny, hairless skin on the chin, cheeks and upper lip', 'NONE'),
 # ---- sideburn styles
 (r'mutton[- ]chops?(-sideburns)?|mutton-chop sideburns', 'thick sideburns that widen down the cheeks to the jaw, with smooth, hairless skin on the chin and upper lip', 'SMALL'),
 (r'sideburns only', 'long sideburns running down both sides of the face to the jaw, with smooth, shiny, hairless skin on the chin, cheeks and upper lip', 'SMALL'),
 # ---- small chin styles
 (r'(a )?soul patch( under the lower lip)?', 'a tiny tuft of hair directly under the lower lip, about the size of a thumbprint, with smooth, hairless skin on the cheeks, chin sides and upper lip', 'NONE'),
 (r'(a )?full goatee with a connected mustache', 'a mustache joined to a rounded beard on the chin, forming a ring around the mouth, with smooth, hairless cheeks', 'SMALL'),
 (r'(a )?circle beard( of connected mustache and goatee)?', 'a mustache joined to a rounded beard on the chin, forming a ring around the mouth, with smooth, hairless cheeks', 'SMALL'),
 (r'(a )?(short |neat )?(hair-coloured )?goatee', 'a small rounded patch of hair on the chin about the width of the mouth, with smooth, hairless cheeks', 'SMALL'),
 (r'(a )?Van Dyke( with a pointed chin beard)?', 'a pointed beard on the chin with a separate thin mustache above it, and smooth, hairless cheeks', 'SMALL'),
 (r'an? anchor beard( tracing the jaw and chin)?', 'a pointed chin beard joined to a thin line of hair tracing the jaw, with a thin mustache and smooth cheeks', 'SMALL'),
 (r'(a )?chin ?strap beard( along the jawline)?', 'a narrow band of beard running along the jawline from ear to ear around the chin, with smooth, hairless cheeks above it', 'SMALL'),
 (r'(a )?chinstrap with a mustache', 'a narrow band of beard running along the jawline from ear to ear around the chin, joined by a mustache, with smooth, hairless cheeks', 'SMALL'),
 (r'(a )?balbo beard', 'a full mustache joined to a rounded chin beard, with smooth, hairless cheeks', 'SMALL'),
 (r'(a )?(French )?fork(ed)? beard', 'a long chin beard that splits in the middle into two points, with smooth, hairless cheeks', 'SMALL'),
 (r'(a )?ducktail beard', 'a full beard on the chin and jaw that narrows to a point at the bottom, like the tail of a duck', 'BIG'),
 (r'(a )?braided beard', 'a long chin beard woven into one or more thin braids', 'SMALL'),
 (r'(a )?[Gg]aribaldi beard( with a rounded bottom)?', 'a broad, full beard on the chin and jaw, with a rounded bottom and a mustache blended into it', 'BIG'),
 # ---- mustaches
 (r'(a )?toothbrush mustache', 'a short, narrow mustache about the width of the nose on the upper lip, with smooth, hairless skin on the chin and cheeks', 'MUST'),
 (r'(a )?(thin )?pencil mustache', 'a very thin, narrow mustache in a neat line along the upper lip, with smooth, hairless skin on the chin and cheeks', 'SMALL'),
 (r'(a )?(waxed )?handlebar mustache', 'a long mustache whose ends are waxed and curled upward, with smooth, hairless skin on the chin and cheeks', 'MUST'),
 (r'(a )?(classic )?horseshoe mustache', 'a thick mustache with two straight strips of hair falling down past the corners of the mouth to the jaw, with smooth, hairless cheeks', 'MUST'),
 (r'(a )?walrus mustache( hanging over the lip)?', 'a very thick, broad mustache that hangs down over the upper lip and the corners of the mouth, with smooth, hairless skin on the chin and cheeks', 'MUST'),
 (r'(a )?Fu Manchu mustache', 'a long mustache whose ends grow down in thin strips well below the chin, with smooth, hairless cheeks', 'MUST'),
 (r'an? imperial mustache', 'a mustache whose ends curve upward, with a small tuft of hair on the chin and smooth, hairless cheeks', 'MUST'),
 (r'(a )?(wispy sparse|neatly trimmed|thick bushy|hair-coloured) mustache', None, 'MUST'),  # filled below
 # ---- stubble
 (r'(a )?heavy five o.clock shadow', 'dense, very short, dark growth across the cheeks, jaw, chin and upper lip', 'STUB'),
 (r'(a )?rugged three-day stubble', 'rough, short stubble about three days long across the cheeks, jaw, chin and upper lip', 'STUB'),
 (r'(a )?(sculpted )?designer stubble( with a clean neckline)?', 'short, evenly trimmed stubble kept to the same length across the cheeks, jaw and chin, with a sharp line along the neck', 'STUB'),
 (r'patchy stubble with uneven growth', 'short stubble that grows unevenly, thicker in some places and bare in others, across the cheeks, jaw and chin', 'STUB'),
 (r'heavy stubble', 'thick, dense stubble across the cheeks, jaw, chin and upper lip', 'STUB'),
 (r'faint stubble across the jaw', 'a faint, very short shadow of hair across the jaw and chin, with smooth skin elsewhere', 'STUB'),
 (r'faint stubble', 'a faint, very short shadow of hair across the jaw and chin, with smooth skin elsewhere', 'STUB'),
 (r'(hair-coloured )?stubble', 'short stubble across the cheeks, jaw, chin and upper lip', 'STUB'),
 # ---- beards
 (r'(a )?long full beard reaching the chest', 'a long, full beard covering the cheeks, chin and jaw and hanging down to the chest', 'BIG'),
 (r'(a )?long (hair-coloured )?beard', 'a long, full beard covering the cheeks, chin and jaw and hanging well below the chin', 'BIG'),
 (r'(a )?(lumberjack|mountain-man|mountain-person) beard', 'a thick, bushy, untrimmed beard covering the cheeks, chin and jaw and hanging down to the chest', 'BIG'),
 (r'(a )?wispy beard', 'a thin, sparse beard of fine, scattered hairs on the chin and jaw, with bare skin showing through', 'BIG'),
 (r'(a )?patchy( sparse)? beard', 'an uneven beard with bare patches of skin between clumps of hair on the cheeks, chin and jaw', 'BIG'),
 (r'(a )?scruffy untamed beard', 'a scruffy, untrimmed beard with stray hairs, covering the cheeks, chin and jaw', 'BIG'),
 (r'(a )?short boxed beard', 'a short, full beard of even length on the cheeks, chin and jaw, trimmed to square edges', 'BIG'),
 (r'(a )?soft natural beard', 'a soft, natural, medium-length beard covering the cheeks, chin and jaw', 'BIG'),
 (r'(a )?trimmed beard with a sharp neckline', 'a short, trimmed beard on the cheeks, chin and jaw with a sharp, straight line along the neck', 'BIG'),
 (r'(a )?neatly sculpted beard with sharp cheek lines', 'a short, neatly sculpted beard on the chin and jaw with crisp, straight lines along the cheeks and neck', 'BIG'),
 (r'(a )?rounded full beard with a shaped cheek line', 'a full, rounded beard on the chin and jaw with a clean, curved line along the cheeks', 'BIG'),
 (r'(a )?closely trimmed (short )?(hair-coloured )?beard|(a )?short hair-coloured beard|(a )?trimmed hair-coloured beard', 'a short, closely trimmed beard covering the cheeks, chin and jaw', 'BIG'),
 (r'(a )?well-groomed medium beard', 'a medium-length, well-groomed beard covering the cheeks, chin and jaw', 'BIG'),
 (r'(a )?full (thick |hair-coloured )?beard', 'a full, thick beard covering the cheeks, chin and jaw, with a mustache', 'BIG'),
]
MUSTACHE_TEXT = {
 'wispy sparse': 'a thin, sparse mustache of fine, scattered hairs on the upper lip, with smooth, hairless skin on the chin and cheeks',
 'neatly trimmed': 'a neatly trimmed mustache on the upper lip, with smooth, hairless skin on the chin and cheeks',
 'thick bushy': 'a thick, bushy mustache covering the upper lip, with smooth, hairless skin on the chin and cheeks',
 'hair-coloured': 'a mustache on the upper lip, with smooth, hairless skin on the chin and cheeks',
}
OK = {
 'NONE': set(),
 'SHAVED': {'with a crisp neckline': 'with a crisp neckline',
            'with a defined jawline': 'with a defined jawline',
            'freshly shaved': 'freshly shaved',
            'with smooth even skin': 'with smooth, even skin',
            'with a faint shadow along the jaw': 'with only a faint dark shadow along the jaw'},
 'SMALL': {'neatly groomed': 'neatly groomed', 'slightly unkempt': 'slightly unkempt', 'left natural': 'left natural',
           'freshly trimmed': 'freshly trimmed', 'lightly combed': 'lightly combed', 'oiled and glossy': 'oiled and glossy'},
 'MUST': {'neatly groomed': 'neatly groomed', 'slightly unkempt': 'slightly unkempt', 'left natural': 'left natural',
          'freshly trimmed': 'freshly trimmed', 'lightly combed': 'lightly combed', 'oiled and glossy': 'oiled and glossy',
          'shaped with sharp edges': 'with sharply shaped edges', 'even all over': 'even all over'},
 'STUB': {'neatly groomed': 'neatly groomed', 'left natural': 'left natural', 'slightly unkempt': 'slightly unkempt',
          'shaped with sharp edges': 'with sharply shaped edges', 'with a defined neckline': 'with a defined line along the neck',
          'even all over': 'even all over', 'denser along the jaw': 'denser along the jaw', 'thick and full': 'thick and dense',
          'thin and patchy': 'thin and patchy'},
 'BIG': {'neatly groomed': 'neatly groomed', 'slightly unkempt': 'slightly unkempt', 'left natural': 'left natural',
         'freshly trimmed': 'freshly trimmed', 'lightly combed': 'lightly combed', 'oiled and glossy': 'oiled and glossy',
         'shaped with sharp edges': 'with sharply shaped edges', 'even all over': 'even all over',
         'thick and full': 'thick and full', 'thin and patchy': 'thin and patchy',
         'with a defined neckline': 'with a defined line along the neck', 'denser along the jaw': 'denser along the jaw'},
}
COMPILED = [(re.compile(r'^(' + h + r')(?=$|,| )'), d, k) for h, d, k in HEADS]
DESCS = {d for _, d, _ in HEADS if d} | set(MUSTACHE_TEXT.values())

def transform(line):
    s = line.strip()
    if not s: return line
    if any(s.startswith(d) for d in DESCS): return line      # already converted
    for rx, d, k in COMPILED:
        m = rx.match(s)
        if not m: continue
        if d is None:
            d = next(v for key, v in MUSTACHE_TEXT.items() if key in m.group(0))
        rest = s[m.end():]
        mod = rest[2:] if rest.startswith(', ') else ''
        out = d
        if mod in OK[k]: out = d + ', ' + OK[k][mod]
        return out
    return None

def main():
    pool = sorted(glob.glob(os.path.join(LIB, 'm_age*_facial_hair.txt')) + glob.glob(os.path.join(LIB, 'any_age*_facial_hair.txt')) + [os.path.join(LIB, 'm_facial_hair.txt')])
    tmpl = sorted(glob.glob(os.path.join(LIB, 'm_age*_prompt_char_face.txt')) + glob.glob(os.path.join(LIB, 'any_age*_prompt_char_face.txt')) + [os.path.join(LIB, 'm_prompt_char_face.txt')])
    if '--restore' in sys.argv:
        for f in glob.glob(os.path.join(BK, '*')):
            shutil.copy2(f, os.path.join(LIB, os.path.basename(f)))
        print('restored from', BK); return
    if not DRY: os.makedirs(BK, exist_ok=True)
    changed = unmatched = 0; miss = collections.Counter()
    for f in pool:
        lines = open(f, encoding='utf-8').read().split('\n')
        out = []
        for l in lines:
            t = transform(l)
            if t is None: miss[l] += 1; out.append(l); continue
            out.append(t)
        if out != lines:
            changed += 1
            if not DRY:
                b = os.path.join(BK, os.path.basename(f))
                if not os.path.exists(b): shutil.copy2(f, b)
                open(f, 'w', encoding='utf-8', newline='\n').write('\n'.join(out))
    tchanged = 0
    for f in tmpl:
        txt = open(f, encoding='utf-8').read()
        new = re.sub(r'\b(His|Their) facial hair is __', r'\1 lower face has __', txt)
        if new != txt:
            tchanged += 1
            if not DRY:
                b = os.path.join(BK, os.path.basename(f))
                if not os.path.exists(b): shutil.copy2(f, b)
                open(f, 'w', encoding='utf-8', newline='\n').write(new)
    # source template and generator, so a rebuild keeps the sentence
    for p, a, b in [(os.path.join(HERE, 'make_male_templates.py'), "' His facial hair is __facial_hair__.'", "' His lower face has __facial_hair__.'"),
                    (os.path.join(HERE, 'data', 'src_templates_m', 'prompt_char_face.tpl'), 'His facial hair is __', 'His lower face has __')]:
        if os.path.exists(p):
            t = open(p, encoding='utf-8').read()
            if a in t and not DRY: open(p, 'w', encoding='utf-8', newline='\n').write(t.replace(a, b))
    print(('DRY ' if DRY else '') + f'pool files changed {changed}, template files changed {tchanged}, unmatched distinct lines {len(miss)}')
    for l, n in miss.most_common(40): print('  UNMATCHED', n, l)

if __name__ == '__main__':
    main()
