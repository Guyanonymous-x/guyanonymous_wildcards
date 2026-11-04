"""Stand-alone garment system: any single garment on its own (a shirt, a pair of trousers, a skirt, a dress, a coat ...), free of age and gender.
These files are IN ADDITION to the age/gender-aware clothing files; nothing existing is changed.

Sources: the merged outfit_* lists (both genders, one copy of each name, weights removed, gender/child wording dropped) + vocab_garment.py
Files written (prefix garment_):
  garment_top / bottom / onepiece / outerwear / suit / uniform                   whole categories (every garment of the category once)
  garment_shirt knitwear trousers jeans shorts skirt dress gown jumpsuit coat jacket vest     the sub-types (each 200+ distinct garments)
  garment_base_<type>        plain base names (shirt, blouse, tee ...) to combine with the attribute files
  garment_neckline sleeve length hem waist leg silhouette closure pockets collar lining feature      structure of a garment
  garment_lingerie_sleepwear_swim, garment_sheer, garment_sexy_top/bottom/full, garment_costume       the other adult categories (kept out of garment_prompt)
  garment_prompt_<type>      one fully described garment of that type          garment_prompt_<category>    any type of a category       garment_prompt   any everyday/formal garment
  garment_prompt_intimate    lingerie / sleepwear / swimwear / sheer / sexy    garment_short_<type>   compact "colour material garment" phrase
  garment_outfit             several garments worn together                    f_/m_prompt_master_garments   the person prompt with the wardrobe replaced by garment_outfit
Usage: python garment_build.py [wildcards_folder]      export_aoo(outdir) feeds simple_build.py
"""
import os, re, sys, random, zlib
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from paths import FINAL
import vocab_garment as V

BAD = re.compile(r"\b(woman|women|man|men|girl|girls|boy|boys|female|male|ladies|lady|gentleman|kid|kids|child|children|toddler|baby|infant|junior|teen|teenage|elderly|senior|schoolgirl|schoolboy|men's|women's)\b|[{}|]|__", re.I)
RULES = {
 'top': [('knitwear', r'sweater|jumper|cardigan|pullover|knit|turtleneck|aran|hoodie|sweatshirt|fleece|track top|zip-up|zip up'),
         ('shirt', r't-shirt|\btee\b|henley|jersey|tank|singlet|camisole|\bcami\b|vest top|crop top|bandeau|tube top|halter|bodysuit|muscle|bralette|bustier|blouse|peasant|smock|tunic|wrap top|kimono top|poet|shirt|polo|button')],
 'bottom': [('jeans', r'jean|denim|jegging'), ('shorts', r'short|bermuda|hot pant'), ('skirt', r'skirt|skort|kilt|sarong'), ('trousers', r'.')],
 'onepiece': [('jumpsuit', r'jumpsuit|romper|playsuit|overall|dungaree|catsuit|unitard|boiler suit'), ('gown', r'gown|ball|evening|formal|prom'), ('dress', r'.')],
 'outerwear': [('coat', r'coat|parka|trench|cape\b|cloak|poncho|duffle'), ('vest', r'vest|gilet|shawl|wrap'), ('jacket', r'.')],
}
SRC = {'top': 'outfit_casual_top', 'bottom': 'outfit_casual_bottom', 'onepiece': 'outfit_dress_style', 'outerwear': 'outfit_outerwear'}
OTHER = {'suit': 'outfit_suit_style', 'uniform': 'outfit_uniform_type', 'costume': 'outfit_cosplay', 'sheer': 'outfit_see_through', 'sexy_top': 'outfit_sexy_top', 'sexy_bottom': 'outfit_sexy_bottom', 'sexy_full': 'outfit_sexy_full'}
ATTR = {'shirt': 'neckline sleeve hem closure pockets feature', 'knitwear': 'neckline sleeve hem feature length', 'trousers': 'waist leg closure pockets feature', 'jeans': 'waist leg pockets feature hem',
        'shorts': 'waist length pockets hem', 'skirt': 'silhouette waist length hem closure pockets', 'dress': 'silhouette neckline sleeve waist length hem', 'gown': 'silhouette neckline sleeve waist hem feature',
        'jumpsuit': 'neckline sleeve waist leg closure pockets', 'coat': 'collar closure length pockets lining sleeve', 'jacket': 'collar closure length pockets lining sleeve',
        'vest': 'collar closure length pockets lining', 'suit': 'collar closure pockets lining waist', 'uniform': 'collar closure pockets feature sleeve'}
CATEGORY = {'top': ['shirt', 'knitwear'], 'bottom': ['trousers', 'jeans', 'shorts', 'skirt'], 'onepiece': ['dress', 'gown', 'jumpsuit'], 'outerwear': ['coat', 'jacket', 'vest'], 'suit': ['suit'], 'uniform': ['uniform']}
LEADS = []

def rd(final, n):
    p = os.path.join(final, n + '.txt')
    return [l.strip() for l in open(p, encoding='utf8')] if os.path.exists(p) else []
def merged(final, base):
    out = []
    for n in (base, 'f_' + base, 'm_' + base): out += rd(final, n)
    seen = set(); res = []
    for l in out:
        if l and not BAD.search(l) and l.lower() not in seen: seen.add(l.lower()); res.append(l)
    return res
def shuf(name, lines): r = random.Random(zlib.crc32(name.encode())); lines = list(lines); r.shuffle(lines); return lines

def build(final):
    F = {}; rep = {}
    groups = {}
    for cat, srcname in SRC.items():
        items = merged(final, srcname); sub = {k: [] for k, _ in RULES[cat]}
        for it in items:
            for k, rx in RULES[cat]:
                if re.search(rx, it, re.I): sub[k].append(it); break
        groups.update(sub)
    for cat, srcname in OTHER.items(): groups[cat] = merged(final, srcname)
    groups['lingerie_sleepwear_swim'] = merged(final, 'outfit_lingerie') + merged(final, 'outfit_swim_underwear')
    for k in list(groups):
        items = list(dict.fromkeys(groups[k]))
        if k in V.BASES or k in V.BASES_SUIT_UNI:
            bases = V.BASES.get(k) or V.BASES_SUIT_UNI[k]
            if len(items) < 220: items += [x for x in V.extra_names(k, bases, None, 260 - len(items)) if x.lower() not in {i.lower() for i in items}]
        F['garment_' + k] = shuf('g_' + k, items)
    # whole categories
    for cat, subs in CATEGORY.items():
        F['garment_' + cat] = shuf('gc_' + cat, [x for s in subs for x in F['garment_' + s]]) if cat not in ('suit', 'uniform') else F['garment_' + cat]
    # bases + attributes
    for k, b in {**V.BASES, **V.BASES_SUIT_UNI}.items(): F['garment_base_' + k] = shuf('b_' + k, list(dict.fromkeys(list(b) + V.base_variants(k, b, 240))))
    F.update({k: shuf(k, v) for k, v in V.attr_files().items()})
    def prompts(k, attrs):
        a = [f'__garment_{x}__' for x in attrs.split()]; a += [a[-1]] * (6 - len(a))
        return [f'__outfit_color__ __outfit_material__ __garment_base_{k}__, {a[0]}, {a[1]}, {a[2]}, __clth_detail__.',
                f'__garment_base_{k}__ in __clth_fabric__, __outfit_color__, {a[0]} and {a[1]}; {a[2]}; __clth_fit__.',
                f'__clth_pattern__ __garment_base_{k}__ in __outfit_color__ and __outfit_color__ with {a[0]}, {a[1]}, {a[3]}.',
                f'__outfit_color__ __garment_base_{k}__ made of __outfit_material__, {a[0]}, {a[1]}, {a[2]}, {a[3]}, __clth_fit__.',
                f'__outfit_pattern__ __outfit_material__ __garment_base_{k}__ with {a[0]} and {a[1]}, {a[4]}, __clth_detail__.',
                f'__outfit_color__ __outfit_material__ __garment_{k}__, __clth_fit__, __clth_detail__.',
                f'__garment_{k}__ in __clth_fabric__, __outfit_color__, __clth_pattern__.',
                f'__outfit_pattern__ __garment_{k}__ in __outfit_color__ __outfit_material__, __clth_detail__.']
    for k, attrs in ATTR.items():
        F['garment_prompt_' + k] = prompts(k, attrs)
        F['garment_short_' + k] = ['__outfit_color__ __outfit_material__ __garment_%s__' % k, '__outfit_color__ __garment_%s__' % k, '__outfit_pattern__ __garment_%s__' % k, '__clth_fabric__ __garment_%s__' % k]
    for cat, subs in CATEGORY.items():
        if cat in ('suit', 'uniform'): continue
        F['garment_prompt_' + cat] = [f'__garment_prompt_{s}__' for s in subs] if len(subs) > 1 else [f'__garment_prompt_{subs[0]}__']
        F['garment_short_' + cat] = [f'__garment_short_{s}__' for s in subs]
    F['garment_prompt'] = [f'__garment_prompt_{c}__' for c in ('top', 'bottom', 'onepiece', 'outerwear', 'top', 'bottom', 'onepiece', 'suit', 'uniform')]
    inti = ['lingerie_sleepwear_swim', 'sheer', 'sexy_top', 'sexy_bottom', 'sexy_full']
    for k in inti + ['costume']:
        F['garment_prompt_' + k] = [f'__outfit_color__ __outfit_material__ __garment_{k}__, __clth_fit__, __clth_detail__.', f'__garment_{k}__ in __clth_fabric__, __outfit_color__, __clth_pattern__.',
                                   f'__outfit_pattern__ __garment_{k}__ in __outfit_color__ __outfit_material__, __clth_detail__.'] if k != 'costume' else [f'__garment_costume__.']
        F['garment_short_' + k] = ['__outfit_color__ __garment_%s__' % k, '__garment_%s__' % k]
    F['garment_prompt_intimate'] = [f'__garment_prompt_{k}__' for k in inti]
    s = lambda c: f'__garment_short_{c}__'
    F['garment_outfit'] = ([f'{s("top")}, {s("bottom")}', f'{s("top")}, {s("bottom")}, {s("outerwear")}', f'{s("onepiece")}', f'{s("onepiece")}, {s("outerwear")}', f'{s("suit")}', f'{s("uniform")}',
                            f'{s("knitwear")}, {s("jeans")}', f'{s("shirt")}, {s("trousers")}', f'{s("shirt")}, {s("skirt")}', f'{s("shirt")}, {s("shorts")}', f'{s("knitwear")}, {s("skirt")}, {s("coat")}',
                            f'{s("shirt")}, {s("jeans")}, {s("jacket")}', f'{s("dress")}, {s("jacket")}', f'{s("gown")}', f'{s("jumpsuit")}', f'{s("shirt")}, {s("trousers")}, {s("vest")}'] * 1)
    # person prompts with the wardrobe replaced by garment_outfit
    for g in ('f', 'm'):
        src = rd(final, f'{g}_prompt_master')
        if src: F[f'{g}_prompt_master_garments'] = [l.replace(f'__{g}_prompt_wardrobe__', 'Wearing __garment_outfit__.') for l in src]
    return F

def run(final):
    F = build(final)
    for n, lines in F.items():
        assert not any(re.search(r'[{}|]', l) for l in lines), n
        open(os.path.join(final, n + '.txt'), 'w', encoding='utf8', newline='\n').write('\n'.join(lines) + '\n')
    small = sorted((len({l for l in v if l}), k) for k, v in F.items() if k.startswith('garment_') and not k.startswith(('garment_prompt', 'garment_short', 'garment_outfit')) and len({l for l in v if l}) < 200)
    print(f'garments: {len(F)} files; under 200: {small}')
    return F

def export_aoo(out, prefix='aoo_'):
    import shutil
    tmp = os.path.join(out, '_g_tmp'); os.makedirs(tmp, exist_ok=True)
    F = build(FINAL); names = set(F); ren = {'outfit_color': 'clothing_color', 'outfit_material': 'clothing_material', 'outfit_pattern': 'clothing_pattern', 'clth_detail': 'clothing_detail', 'clth_fabric': 'clothing_fabric', 'clth_fit': 'clothing_fit', 'clth_pattern': 'clothing_pattern_description'}; ref = re.compile(r'__([A-Za-z0-9_\-/]+)__'); n = 0
    tm = lambda k: k.startswith(('garment_prompt', 'garment_short', 'garment_outfit'))
    for name, lines in F.items():
        if name.startswith(('f_', 'm_')): continue
        keep = []; seen = set()
        for l in lines:
            if not l.strip() or l in seen: continue
            seen.add(l); keep.append(ref.sub(lambda m: '__' + prefix + ren.get(m.group(1), m.group(1)) + '__' if (m.group(1) in names or m.group(1) in ren) else m.group(0), l))
        if not tm(name): random.Random(zlib.crc32(name.encode())).shuffle(keep)
        open(os.path.join(out, prefix + name + '.txt'), 'w', encoding='utf8', newline='\n').write('\n'.join(keep) + '\n'); n += 1
    shutil.rmtree(tmp, ignore_errors=True)
    # outfit_color / material / pattern and the clth_* files are already in the aoo set under other names -> alias references
    return n

if __name__ == '__main__':
    a = [x for x in sys.argv[1:] if os.path.isdir(x)]
    run(os.path.abspath(a[0]) if a else FINAL)
