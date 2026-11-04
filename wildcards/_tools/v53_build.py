"""v53: wardrobe by occasion + a no-colon rule.
 - 20 occasions (office, interview, clinical, kitchen, trades, wedding guest, formal evening, funeral, graduation, worship, festival, sports kit, hiking,
   winter, rain, beach, travel, home, stage, night out), each in parts: fabric, top, bottom, one-piece, layer, extra, plus assembled outfits and single-part prompts
 - decolon(): removes ': ' from item text ('Swiss cheese: a cheese ...' -> 'Swiss cheese, which is a cheese ...') across the library
 Idempotent; run(final) / export_aoo(out)."""
import os, re, sys, glob, random, zlib
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from paths import FINAL
import v53_data as D, v53_data2 as B
REF = re.compile(r'__([A-Za-z0-9_\-/]+)__')
def _wr(folder, name, lines): open(os.path.join(folder, name + '.txt'), 'w', encoding='utf8', newline='\n').write('\n'.join(lines) + '\n')
def art(w): return ('an ' if w[:1].lower() in 'aeiou' else 'a ') + w
FABRICW = {'silk', 'satin', 'linen', 'cotton', 'wool', 'fleece', 'flannel', 'denim', 'sequinned', 'canvas', 'nylon', 'velvet', 'faux', 'leather-look', 'leather', 'jersey', 'crepe', 'lycra', 'polyester', 'twill'}
def tidy(item, fabrics):
    drop = {w for f in fabrics for w in re.findall(r'[a-z][a-z\-]{3,}', f)} | FABRICW
    out = ' '.join(w for w in item.split() if w.lower() not in drop)
    return out if len(out.split()) >= 1 and out.strip() else item
PLURAL = {'trousers', 'overalls', 'shorts', 'leggings', 'joggers', 'jeans', 'bottoms', 'dungarees', 'overtrousers', 'chinos', 'gloves', 'tights'}
SLOTS = ['top', 'bottom', 'onepiece', 'layer', 'extra']
def build(final=FINAL):
    G = {}
    col = [l for l in open(os.path.join(final, 'comp_colour.txt'), encoding='utf8').read().split('\n') if l.strip()] if os.path.exists(os.path.join(final, 'comp_colour.txt')) else []
    G['comp_colour_a'] = [art(c) for c in col]
    persons, listing = [], []
    for k, o in D.OCC.items():
        p = f'occasion_{k}_'; r = random.Random(zlib.crc32(k.encode()))
        G[p + 'fabric'] = o['fabric']
        for s in SLOTS:
            G[p + s] = o[s] if s == 'extra' else list(dict.fromkeys(tidy(x, o['fabric']) for x in o[s]))
        ca, cp = '__comp_colour_a__', '__comp_colour__'
        if o.get('colours'): G[p + 'colour_a'] = [art(x) for x in o['colours']]; G[p + 'colour'] = list(o['colours']); ca, cp = f'__{p}colour_a__', f'__{p}colour__'
        def dressed(it, fabs):
            plural = it.split()[-1].lower() in PLURAL
            return [(f'a pair of {cp} {f} {it}' if plural else f'{ca} {f} {it}') for f in fabs]
        for s_ in ('top', 'bottom', 'onepiece', 'layer'): G[f'{p}{s_}_dressed'] = [x for it in G[p + s_] for x in dressed(it, o['fabric'])]
        def item(s): return f'__{p}{s}_dressed__'
        two = f"wearing {item('top')} with {item('bottom')}"; one = f"wearing {item('onepiece')}"
        lay = f"Over this is {item('layer')}."; ext = f"This person also has __{p}extra__."
        head = f"dressed for {o['name']}"
        L = []
        for base in (two, one):
            L += [f'{head}, {base}.', f'{head}, {base}. {lay}', f'{head}, {base}. {ext}', f'{head}, {base}. {lay} {ext}']
        G[p + 'outfit_phrase'] = [l for l in L]
        G[p + 'outfit'] = ['This person is ' + l for l in L]
        G[p + 'outfit_prompt'] = [f'__{p}outfit__']
        for s in SLOTS:
            if s == 'extra': G[f'{p}extra_prompt'] = [f"For {o['name']}, this person also has __{p}extra__."]
            else: G[f'{p}{s}_prompt'] = [f"For {o['name']}, this person wears {item(s)}."]
        persons.append(f'__any_create_random_person_base__ __{p}outfit__'); listing.append(f'__{p}outfit__')
    G['occasion_prompt'] = listing; G['occasion_person_prompt'] = persons; G['occasion_list'] = [f"{k}" for k in D.OCC]
    G.update(badtaste())
    G['v53_entry_points'] = ['__occasion_prompt__', '__occasion_person_prompt__', '__badtaste_prompt__', '__badtaste_person_prompt__', '__badtaste_all_three__']
    return G

def badtaste():
    G = {}; art_ = lambda x: x
    for k, v in B.CLOTH.items(): G[f'badtaste_clothing_{k}'] = v
    for k, v in B.TATT.items(): G[f'badtaste_tattoo_{k}'] = v
    for k, v in B.JEW.items(): G[f'badtaste_jewellery_{k}'] = v
    G['badtaste_colour_clash'] = ['__comp_colour__ and __comp_colour__', '__comp_colour__ with __comp_colour__ and __comp_colour__', 'a mix of __comp_colour__, __comp_colour__ and __comp_colour__']
    C = 'badtaste_clothing_'; cA = '__comp_colour_a__ __badtaste_clothing_fabric__ __badtaste_clothing_garment__'
    G['badtaste_clothing_ugly'] = [f'This person wears {cA} in __badtaste_clothing_ugly_pattern__, {{}}, __badtaste_clothing_ugly_fit__, with __badtaste_clothing_ugly_detail__.'.replace('{}', 'in __badtaste_colour_clash__'), f'This person wears {cA} in __badtaste_clothing_ugly_pattern__, __badtaste_clothing_ugly_fit__.', f'This person wears {cA}, __badtaste_clothing_ugly_fit__, with __badtaste_clothing_ugly_detail__.']
    G['badtaste_clothing_tacky'] = [f'This person wears {cA} with __badtaste_clothing_tacky_detail__.', f'This person wears {cA} with __badtaste_clothing_tacky_theme__.', f'This person wears {cA} with __badtaste_clothing_tacky_detail__ and __badtaste_clothing_tacky_theme__.']
    G['badtaste_clothing_crude'] = ['This person wears __badtaste_clothing_crude_theme__, __badtaste_clothing_crude_context__.', f'This person wears {cA} with __badtaste_clothing_crude_theme__, __badtaste_clothing_crude_context__.', 'This person wears __comp_colour_a__ __badtaste_clothing_crude_item__ printed with __badtaste_clothing_crude_saying__.', 'This person wears __comp_colour_a__ __badtaste_clothing_crude_item__ printed with __badtaste_clothing_crude_saying__, __badtaste_clothing_crude_context__.', 'This person wears __comp_colour_a__ __badtaste_clothing_crude_item__ with __badtaste_clothing_crude_logo__.', 'This person wears __comp_colour_a__ __badtaste_clothing_crude_item__ with __badtaste_clothing_crude_logo__ and __badtaste_clothing_crude_saying__.']
    G['badtaste_clothing_rude_saying_prompt'] = ['This person wears __comp_colour_a__ __badtaste_clothing_crude_item__ printed with __badtaste_clothing_crude_saying__.']
    G['badtaste_clothing_rude_logo_prompt'] = ['This person wears __comp_colour_a__ __badtaste_clothing_crude_item__ with __badtaste_clothing_crude_logo__.']
    G['badtaste_clothing_gross'] = [f'This person wears {cA}, __badtaste_clothing_gross_wear__.', f'This person wears {cA}, __badtaste_clothing_gross_wear__ and __badtaste_clothing_gross_wear__.', f'This person wears {cA} in __badtaste_clothing_ugly_pattern__, __badtaste_clothing_gross_wear__.']
    T = 'badtaste_tattoo_'
    G['badtaste_tattoo_ugly'] = [f'This person has a tattoo of __{T}subject__ __{T}place__, __{T}ugly_flaw__.', f'This person has a tattoo of __{T}subject__ __{T}place__, __{T}ugly_flaw__ and __{T}ugly_flaw__.']
    G['badtaste_tattoo_tacky'] = [f'This person has a tattoo of __{T}subject__ __{T}place__, __{T}tacky_flaw__.', f'This person has a tattoo of __{T}subject__ __{T}place__, __{T}tacky_flaw__, __{T}ugly_flaw__.']
    G['badtaste_tattoo_crude'] = [f'This person has a tattoo of __{T}crude_subject__ __{T}place__.', f'This person has a tattoo of __{T}crude_subject__ __{T}place__, __{T}ugly_flaw__.']
    G['badtaste_tattoo_gross'] = [f'This person has a tattoo of __{T}subject__ __{T}place__, __{T}gross_flaw__.', f'This person has a tattoo of __{T}subject__ __{T}place__, __{T}gross_flaw__ and __{T}ugly_flaw__.']
    J = 'badtaste_jewellery_'
    G['badtaste_jewellery_ugly'] = [f'This person wears __{J}item__ __{J}ugly_flaw__.', f'This person wears __{J}item__ __{J}ugly_flaw__ and __{J}item__ __{J}ugly_flaw__.']
    G['badtaste_jewellery_tacky'] = [f'This person wears __{J}item__ __{J}tacky_flaw__.', f'This person wears __{J}item__ __{J}tacky_flaw__ and __{J}item__ __{J}tacky_flaw__.']
    G['badtaste_jewellery_crude'] = [f'This person wears __{J}item__ __{J}crude_flaw__.', f'This person wears __{J}item__ __{J}crude_flaw__ and __{J}item__ __{J}ugly_flaw__.']
    G['badtaste_jewellery_gross'] = [f'This person wears __{J}item__ __{J}gross_flaw__.', f'This person wears __{J}item__ __{J}gross_flaw__ and __{J}item__ __{J}gross_flaw__.']
    kinds = ['ugly', 'tacky', 'crude', 'gross']
    for what in ('clothing', 'tattoo', 'jewellery'):
        for k in kinds: G[f'badtaste_{what}_{k}_prompt'] = [f'__badtaste_{what}_{k}__']
        G[f'badtaste_{what}_prompt'] = [f'__badtaste_{what}_{k}__' for k in kinds]
    G['badtaste_prompt'] = [f'__badtaste_{w}_prompt__' for w in ('clothing', 'tattoo', 'jewellery')]
    G['badtaste_person_prompt'] = [f'__any_create_random_person_base__ __badtaste_{w}_{k}__' for w in ('clothing', 'tattoo', 'jewellery') for k in kinds]
    G['badtaste_all_three'] = [f'__any_create_random_person_base__ __badtaste_clothing_{k}__ __badtaste_tattoo_{k}__ __badtaste_jewellery_{k}__' for k in kinds]
    return G
# ---------------- no-colon rule ----------------
def decolon_line(l):
    if ': ' not in l: return l
    refs = []
    def mask(m): refs.append(m.group(0)); return f'\x00{len(refs) - 1}\x00'
    t = REF.sub(mask, l)
    if ': ' not in t: return l
    t = re.sub(r'\bFront: (?=an? |the |[a-z])', 'At the front, ', t); t = re.sub(r'\bBack: (?=an? |the |[a-z])', 'At the back, ', t)
    m = re.match(r'^([^:.]{2,120}): (\S+)', t)
    if m:
        label, nxt = m.group(1), m.group(2)
        if nxt[:1].isupper() or nxt[:1].isdigit(): sep = '. ' if nxt[:1].isupper() else ', '
        elif nxt.lower() in ('a', 'an', 'the') and len(label) <= 60 and ',' not in label: sep = ', which is '
        elif nxt.lower() in ('a', 'an', 'the', 'one', 'two', 'three'): sep = ', with '
        else: sep = ', '
        t = label + sep + t[m.end() - len(nxt):]
    def rest(m):
        nxt = m.group(1)
        if nxt[:1].isupper(): return '. ' + nxt
        if nxt.lower() in ('a', 'an', 'the', 'one', 'two', 'three', 'four'): return ', with ' + nxt
        return ', ' + nxt
    t = re.sub(r': (\S+)', rest, t)
    return re.sub(r'\x00(\d+)\x00', lambda m: refs[int(m.group(1))], t)
def decolon(folder):
    n = lines = 0
    for p in glob.glob(os.path.join(folder, '*.txt')):
        if os.path.basename(p) in ('README.txt', 'CHANGELOG.txt', 'HOW_TO_RUN.txt'): continue
        t = open(p, encoding='utf8', errors='replace').read()
        if ': ' not in t: continue
        old = t.split('\n'); new = [decolon_line(l) for l in old]; c = sum(a != b for a, b in zip(old, new))
        if c: open(p, 'w', encoding='utf8', newline='\n').write('\n'.join(new)); n += 1; lines += c
    return n, lines
def run(final):
    G = build(final)
    for n, l in G.items(): _wr(final, n, l)
    print('v53:', len(G), 'files'); print('no-colon rule:', decolon(final)); return G
def export_aoo(out, prefix='aoo_'):
    G = {k: v for k, v in build(FINAL).items() if k not in ('occasion_person_prompt', 'v53_entry_points', 'badtaste_person_prompt', 'badtaste_all_three')}; names_ = set(G); n = 0   # the person prompt needs the people system
    for name, lines in G.items():
        keep = list(dict.fromkeys(REF.sub(lambda m: '__' + prefix + m.group(1) + '__' if (m.group(1) in names_ or os.path.exists(os.path.join(out, prefix + m.group(1) + '.txt'))) else m.group(0), l) for l in lines))
        _wr(out, prefix + name, keep); n += 1
    decolon(out); return n
if __name__ == '__main__':
    a = [x for x in sys.argv[1:] if os.path.isdir(x)]; run(os.path.abspath(a[0]) if a else FINAL)
