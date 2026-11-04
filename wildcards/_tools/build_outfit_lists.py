"""Writes the outfit_* attribute files (populated from the vocabulary mined out of YOUR clothing_full_female.txt, see data/outfit_vocab.json),
outfit_cosplay (500+ specific costumes) and the outfit_*_mixed files.   Usage: python build_outfit_lists.py [wildcards_folder]"""
import os, sys, json, random, re
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from paths import wc_dir, DATA
from gender import IS_M
import vocab_clothing_a as VA, vocab_clothing_b as VB
WC = wc_dir(); OUTFIT_NEW = VB.outfit_lists('m' if IS_M else 'f'); V = json.load(open(os.path.join(DATA, 'outfit_vocab.json'), encoding='utf8'))
def alloc(weights, total):
    k = len(weights); spare = max(0, total - k); s = float(sum(weights)); raw = [w / s * spare for w in weights]
    base = [int(r) for r in raw]; left = spare - sum(base)
    for i in sorted(range(k), key=lambda i: raw[i] - base[i], reverse=True)[:left]: base[i] += 1
    return [b + 1 for b in base]
def write(name, lines, seed=1):
    random.Random(seed).shuffle(lines)
    open(os.path.join(WC, name + '.txt'), 'w', encoding='utf8', newline='\n').write('\n'.join(lines) + '\n')
def weighted(name, items, total, seed=1):
    cnt = alloc([w for _, w in items], total); out = []
    for (t, _), c in zip(items, cnt): out += [t] * c
    write(name, out, seed); return len(items)
# ---- supplements and clean-ups applied on top of the mined lists ----
EXTRA = {
 'sexy_top': [("plunging lace bodysuit",2),("satin camisole",2),("halter crop top",2),("low-cut wrap top",2),("strapless bandeau top",2),("backless halter top",2),("cut-out knit top",1.5),("tie-front cropped blouse",1.5),("lace-up front top",1.5),("deep-V ribbed top",1.5),("lace bralette",2),("sheer mesh top over a bralette",1.5)],
 'sexy_bottom': [("micro mini skirt",2),("leather mini skirt",2),("satin shorts",2),("low-rise hot pants",2),("high-slit maxi skirt",2),("thigh-high slit skirt",1.5),("bodycon mini skirt",2),("lace-up side shorts",1.5),("faux leather leggings",2),("tight pencil skirt with a slit",2),("pleated micro skirt",1.5),("short shorts",2)],
 'sexy_full': [("bodycon mini dress",2),("backless satin gown",2),("cutout dress",2),("plunging halter jumpsuit",1.5),("corset mini dress",2),("lace-trimmed slip dress",2),("one-shoulder asymmetric dress",1.5),("bandage dress",2),("sequined mini dress",2),("thigh-high-slit evening gown",2),("two-piece bikini",3),("string bikini",1.5),("strappy cutout one-piece swimsuit",1.5)],
 'lingerie': [("lace bralette and matching briefs",2),("satin chemise",2),("silk slip",2),("lace bodysuit",2),("corset with garter belt",2),("babydoll nightie",1.5),("lace teddy",1.5),("mesh bralette and high-waisted panties",1.5),("satin pajama set",1.5),("bra and panty set",2)],
}
EXCLUDE = {'sexy_bottom': r'board|sport|athletic|padded|tailored|plaid|baby|chequered|^shorts$|polka|high-waisted denim', 'sexy_full': r'only|competitive|utility', 'sexy_top': r'designer brand', 'lingerie': r'^robe$|wizard'}
STRIP = set("stunning breathtaking chic eye-catching sultry daring dramatic striking only competitive fiery bold sensual alluring seductive flirty glamorous versatile practical exotic cozy structured designer brand loungewear tropical-themed bridal-inspired nautical-inspired vintage-inspired".split())
def clean_list(name):
    merged = {}
    for t, w in V[name]:
        if name in ('see_through',): merged[t] = merged.get(t, 0) + w; continue
        t2 = ' '.join(x for x in t.split() if x not in STRIP).strip()
        if not t2 or t2 in ('lingerie', 'top', 'dress'): t2 = t if t in ('dress',) else ''
        if t2: merged[t2] = merged.get(t2, 0) + w
    if name == 'material': merged.pop('sheer organza', None)
    items = list(merged.items())
    if name in EXCLUDE: items = [(t, w) for t, w in items if not re.search(EXCLUDE[name], t)]
    have = {t for t, _ in items}
    items += [(t, w) for t, w in EXTRA.get(name, []) if t not in have]
    # ---- vocabulary expansion (vocab_clothing_a/b): original options keep their weights, new ones join at a typical weight ----
    new = {'color': VA.COLORS, 'material': VA.MATERIALS, 'pattern': VA.PATTERNS}.get(name) or OUTFIT_NEW.get(name) or []
    have = {t.lower() for t, _ in items}; avg = sum(w for _, w in items) / max(1, len(items))
    items += [(t, round(avg * 0.9, 3)) for t in new if t.lower() not in have]
    return items
n = {}
V['color'] = [(t, w) for t, w in V['color'] if t not in ('gray',)]
for name, total in [x for x in [('color', 900), ('material', 300), ('pattern', 220), ('casual_top', 320), ('casual_bottom', 320), ('dress_style', 260), ('uniform_type', 160), ('sexy_top', 160), ('sexy_bottom', 160), ('sexy_full', 170), ('lingerie', 150), ('see_through', 90)] if (not IS_M) or x[0] in ('color', 'material', 'pattern')]:
    _it = clean_list(name); n[name] = weighted('outfit_' + name, _it, max(total, int(len(_it) * 4.5)), seed=len(name))
# ---- cosplay: >= 500 distinct, specifically described costumes from the archetype catalogue ----
if IS_M:
    import cosplay_data_m3 as cd
else:
    import cosplay_data_c as cd
PALETTES = ["midnight navy and silver","crimson and black","emerald green and gold","ivory and rose gold","charcoal grey and electric blue","burgundy and bronze","forest green and brown","royal purple and gold","teal and copper","white and pale blue","obsidian black and violet","burnt orange and cream","sage green and cream","scarlet and ivory","slate blue and silver","mustard yellow and brown","deep plum and rose pink","pearl white and gold","bottle green and black","rust red and tan","ice blue and white","dusty pink and grey","turquoise and gold","copper and charcoal","cream and navy","blood red and bone white","lavender and silver","olive drab and black","coral and teal","gunmetal and neon green","black and hot pink","chocolate brown and gold","sky blue and white","amber and deep brown","silver and black","magenta and indigo"]
def cap(s): return s[0].upper() + s[1:]
rng = random.Random(2024); costumes = []; seen = set()
for title, G, H, D, P in cd.ARCH:
    combos = [(g, h, d, p) for g in range(len(G)) for h in range(len(H)) for d in range(len(D)) for p in range(len(P))]
    rng.shuffle(combos); pal = PALETTES[:]; rng.shuffle(pal); k = 0
    for g, h, d, p in combos:
        if k >= 9: break
        line = f"{cap(title)} costume with {pal[k]} accents: {G[g]}, {H[h]}, {D[d]}, and {P[p]}"
        if line not in seen: seen.add(line); costumes.append(line); k += 1
write('outfit_cosplay', costumes, seed=5)
# ---- mixed pointer targets (nested wildcards) ----
if not IS_M: write('outfit_sexy_mixed', ["__outfit_color__ __outfit_sexy_top__, __outfit_color__ __outfit_sexy_bottom__"] * 4 + ["__outfit_color__ __outfit_material__ __outfit_sexy_top__, __outfit_sexy_bottom__"] * 2 + ["__outfit_color__ __outfit_sexy_full__"] * 4 + ["__outfit_color__ __outfit_lingerie__"] * 2 + ["__outfit_see_through__"] * 2)
if not IS_M: write('outfit_uniform_mixed', ["__outfit_color__ __outfit_uniform_type__", "classic __outfit_color__ __outfit_uniform_type__, matching accessories", "{cute|strict|smart|neat} __outfit_color__ __outfit_uniform_type__, highly detailed outfit", "__outfit_color__ and __outfit_color__ __outfit_uniform_type__, professional appearance", "__outfit_uniform_type__ in __outfit_color__, neat and tidy look"])
if not IS_M: write('outfit_formal_mixed', ["elegant __outfit_color__ __outfit_material__ __outfit_dress_style__, high heels, sophisticated formal wear", "tailored __outfit_color__ business suit, crisp white shirt, formal office attire", "smart casual __outfit_color__ blazer, neat trousers, modern formal", "luxurious __outfit_color__ __outfit_material__ evening gown, expensive jewelry, high-class formal", "__outfit_color__ __outfit_material__ cocktail dress, clutch bag, polished formal look", "formal __outfit_color__ pencil skirt suit with a silk blouse, professional elegance"])
if not IS_M: write('outfit_casual_mixed', ["__outfit_pattern__ __outfit_casual_top__, __outfit_material__ __outfit_casual_bottom__, comfortable casual wear", "oversized __outfit_color__ __outfit_casual_top__, ripped __outfit_color__ jeans, street casual fashion", "__outfit_color__ __outfit_material__ __outfit_casual_top__, __outfit_color__ __outfit_casual_bottom__, sneakers, casual style", "{5::__outfit_pattern__|5::__outfit_color__} __outfit_dress_style__, light cardigan, casual breezy style", "relaxed __outfit_color__ __outfit_casual_top__ with __outfit_casual_bottom__, everyday casual look"])
if IS_M:
    import male_outfits as mo
    for _k, _items in mo.LISTS.items():
        _items = list(_items); _have = {t.lower() for t, _ in _items}; _avg = sum(w for _, w in _items) / max(1, len(_items))
        _items += [(t, round(_avg * 0.9, 3)) for t in OUTFIT_NEW.get(_k, []) if t.lower() not in _have]
        n[_k] = weighted('outfit_' + _k, _items, max(200, int(len(_items) * 4.5)), seed=len(_k))
    for _k, _lines in mo.MIXED.items(): write('outfit_' + _k, list(_lines))
import vocab_misc as _vm
for _kind in (['casual', 'formal', 'uniform', 'sexy'] if not IS_M else ['casual', 'formal', 'uniform', 'swim']):
    _fn = os.path.join(WC, 'outfit_' + _kind + '_mixed.txt') if not IS_M or _kind != 'swim' else os.path.join(WC, 'outfit_swim_mixed.txt')
    if IS_M and _kind in ('casual', 'formal', 'uniform', 'swim'): _fn = os.path.join(WC, 'outfit_' + _kind + '_mixed.txt')
    _old = [l for l in open(_fn, encoding='utf8').read().split('\n') if l.strip()] if os.path.exists(_fn) else []
    _new = [x for x in _vm.mixed_lines('m' if IS_M else 'f', _kind) if x not in _old]
    write('outfit_' + _kind + '_mixed', _old + _new, seed=11)
print('outfit lists written:', {k: v for k, v in n.items()}, '| cosplay costumes:', len(costumes), 'distinct:', len(set(costumes)))
