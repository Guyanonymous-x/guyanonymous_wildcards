"""Generic condition descriptors, applicable to ANY item (garment, accessory, object, vehicle, building ...).
Ladder: condition_01_pristine ... condition_09_ruined; aspect pools; combined condition_any; condition_prompt."""
import os, re, sys, random, zlib
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from paths import FINAL
def S(x): return [i.strip() for i in x.split(';') if i.strip()]
def R(*k): return random.Random(zlib.crc32('|'.join(map(str, k)).encode()))
LADDER = {
 '01_pristine': (S("perfect and brand new; pristine and flawless; factory-fresh; showroom perfect; unused and untouched; absolutely immaculate; mint, with every surface unmarked; brand new, still crisp and sharp; fresh from the maker with no trace of handling"),
   S("crisp edges and a flawless surface; no marks, scratches or creases anywhere; colours at full strength; a clean, even finish; tags or protective wrapping still attached; the smell of newness; perfectly even stitching or joins; a flawless shine")),
 '02_like_new': (S("like new; hardly used; barely touched; almost perfect; very well kept; carefully looked after; lightly handled; in excellent condition; cleaned and cared for"),
   S("only the faintest signs of handling; a few barely visible marks; edges still sharp; colours still bright; a surface that still gleams; slight softening at the creases; one or two tiny scuffs that are hard to find")),
 '03_good': (S("in good condition; in good shape with light use; clean and tidy; gently used; well maintained; lightly worn in; neat with minor signs of age; sound and presentable"),
   S("small scuffs on the corners; very light creasing; a faint dulling of the finish; a couple of tiny marks; slightly softened edges; fine surface scratches that catch the light; colours a touch less vivid than new")),
 '04_used': (S("clearly used; in everyday condition; lived-in; used regularly; showing ordinary wear; middle-aged and serviceable; used but still dependable; broken in"),
   S("scuffs and light scratches across the surface; soft creases at the bends; darkened edges where it is handled; slightly dulled colour; minor rubbed patches; a few small stains; a loosened thread or small chip; visible signs of handling")),
 '05_worn': (S("worn; well worn; noticeably worn down; heavily used; showing years of use; tired; worn thin in places; weathered; scuffed all over"),
   S("rubbed bare at the high points; faded colour; creased deeply along the folds; frayed edges; scratches that run in many directions; shiny patches from repeated touching; sagging shape; dull, tired surfaces; small chips along the edges")),
 '06_shabby': (S("shabby; scruffy; beaten up; run-down; battered; tatty; rough and neglected; scuffed and stained; grubby"),
   S("stains that have set into the surface; ragged edges and loose threads; dents and deep scratches; patches rubbed through to the layer beneath; mismatched repairs; grime in the seams; peeling or flaking finish; missing small parts; a sagging, distorted shape")),
 '07_damaged': (S("damaged; broken in places; torn; cracked; split; badly knocked about; in poor condition; badly marked; falling apart at the seams"),
   S("a long crack or tear; a dent that has changed its shape; a missing piece; holes worn through; deep gouges; burn or scorch marks; heavy stains and discolouration; broken fastenings or hardware; large patches of peeling, rust or mould; repairs held together with tape or glue")),
 '08_decayed': (S("old and decayed; rotting; corroded; mouldering; ancient and crumbling; rusted solid; moth-eaten; sun-rotted; deteriorated beyond use"),
   S("rust that has eaten holes through the metal; mould in dark, fuzzy patches; fabric or material that is brittle and crumbling; thick dust and cobwebs; colours bleached to grey; warped or sagging parts; stains soaked right through; a surface that flakes away when touched")),
 '09_ruined': (S("ruined; wrecked; destroyed; completely worn out; beyond repair; in tatters; a total wreck; burnt out; shattered"),
   S("pieces missing or scattered; large burnt or melted areas; shredded fabric or collapsed structure; deeply crushed or bent out of shape; heavy soot, mud or grime over everything; only fragments left of the original; no original finish remaining; held together by a few remaining joins")),
}
ASPECT = {
 'stain': S("coffee stains; wine stains; grease marks; oil stains; ink blots; mud splashes; food stains; sweat marks; rust stains; water rings; paint splashes; grass stains; sauce drips; tea stains; soot smudges; a yellowed patch; a faded patch from bleach; blood-coloured stains; dark marks from heavy handling"),
 'mark': S("scratches; scuffs; dents; creases; fingerprints; pen marks; scribbles; stickers half peeled off; label residue; tape marks; scorch marks; cigarette burns; hair or lint clinging to it; teeth marks; glue marks; chalk marks; pressure marks; bite-sized chips"),
 'wear': S("worn thin; rubbed bare; frayed edges; pilling; shiny patches; faded colour; loose threads; peeling paint; cracked finish; worn-through holes; softened corners; stretched out of shape; flattened pile; polished smooth by handling; thinning at the knees, elbows or corners"),
 'dirt': S("a coating of dust; dried mud; ingrained dirt; sand in the seams; cobwebs; grime in the creases; a layer of soot; oil and dirt on the edges; dried salt marks; pollen dust; dog or cat hair; ash; a film of grease"),
 'age': S("a soft patina; yellowing; a faded, sun-bleached look; brittle with age; spots of age; foxing; tarnish; cracked varnish; crazed paint; dulled lustre; old repairs; a musty, stored-away look; discoloured with time"),
 'damage': S("a tear; a split seam; a missing button or part; a broken zip or clasp; a crack; a chip; a bent frame; a hole; a burn hole; a snapped strap; a dent; a missing piece; a loose hinge; a crushed corner; a warped shape; a broken lock"),
 'repair': S("a neat darn; a mismatched patch; visible stitches; glue lines; tape wrapped around a break; a replaced part in a different colour; a welded seam; a safety pin holding it together; a rivet or staple; a darned heel or elbow; a handmade repair"),
 'finish': S("a high gloss shine; a clean matte finish; a satin sheen; a polished, mirror-like surface; an even, unmarked coat; a soft lustre; a crisp, clean surface"),
 'finish_poor': S("a dull, lifeless surface; a scuffed shine; a sticky film; a flaking coat; a bubbled coating; an uneven finish; a cloudy surface; a cracked glaze"),
}
def mk():
    G = {}; alll = []
    for k, (heads, details) in LADDER.items():
        n = f'condition_{k}'
        G[n + '_head'] = heads; G[n + '_detail'] = details
        G[n] = sorted({f"It is {h}: {d}" for h in heads for d in details if R('c', k, h, d).random() < .55})
        alll += G[n]
    for a, l in ASPECT.items(): G[f'condition_{a}'] = l
    G['condition_any'] = sorted(set(alll))
    G['condition_ladder'] = [f'__condition_{k}__' for k in LADDER]
    G['condition_good'] = [f'__condition_{k}__' for k in ('01_pristine', '02_like_new', '03_good')]
    G['condition_poor'] = [f'__condition_{k}__' for k in ('05_worn', '06_shabby', '07_damaged', '08_decayed', '09_ruined')]
    G['condition_aspect_prompt'] = [f"Details: __condition_{a}__." for a in ASPECT]
    G['condition_prompt'] = ['__condition_01_pristine__.', '__condition_02_like_new__. Finish: __condition_finish__.', '__condition_03_good__. Marks: __condition_mark__.',
        '__condition_04_used__. Marks: __condition_mark__; dirt: __condition_dirt__.', '__condition_05_worn__. Wear: __condition_wear__; age: __condition_age__.',
        '__condition_06_shabby__. Stains: __condition_stain__; wear: __condition_wear__; repairs: __condition_repair__.', '__condition_07_damaged__. Damage: __condition_damage__; repairs: __condition_repair__; stains: __condition_stain__.',
        '__condition_08_decayed__. Age: __condition_age__; dirt: __condition_dirt__; damage: __condition_damage__.', '__condition_09_ruined__. Damage: __condition_damage__; dirt: __condition_dirt__.']
    return G
def build(): return mk()
def run(final):
    G = build()
    for n, l in G.items():
        assert l and all(l) and not any(c in x for x in l for c in '{}|'), n
        open(os.path.join(final, n + '.txt'), 'w', encoding='utf8', newline='\n').write('\n'.join(dict.fromkeys(l)) + '\n')
    print('condition:', len(G), 'files'); return G
def export_aoo(out, prefix='aoo_'):
    G = build(); nm = set(G); ref = re.compile(r'__([A-Za-z0-9_\-/]+)__'); n = 0
    for name, lines in G.items():
        keep = list(dict.fromkeys(ref.sub(lambda m: '__' + prefix + m.group(1) + '__' if m.group(1) in nm else m.group(0), l) for l in lines))
        if not (name.endswith('prompt') or name.startswith('condition_ladder') or name in ('condition_good', 'condition_poor')): random.Random(zlib.crc32(name.encode())).shuffle(keep)
        open(os.path.join(out, prefix + name + '.txt'), 'w', encoding='utf8', newline='\n').write('\n'.join(keep) + '\n'); n += 1
    return n
if __name__ == '__main__':
    a = [x for x in sys.argv[1:] if os.path.isdir(x)]; run(os.path.abspath(a[0]) if a else FINAL)
