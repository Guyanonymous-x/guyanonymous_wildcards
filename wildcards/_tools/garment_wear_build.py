"""One-piece garments (coveralls, boiler suits, zip jumpsuits and flight suits, one-piece zipper leisure suits, bodysuits/catsuits/unitards, overalls and dungarees long and short, rompers, union suits)
and dance / performance / wrestling wear (leotards, singlets, wrestling outfits and costumes, ballet, ballroom and Latin, folk and world dance, stage dance, burlesque and cabaret, exotic-dancer and pole-dance wear, themed dance costumes)
as stand-alone clothing wildcards in the garment_ system.  Adult wording, no gendered words, no brands; nothing existing is changed.
Files per family <k>:  garment_<k> (names), garment_base_<k>, garment_feat_<k>, garment_mat_<k>, garment_prompt_<k>, garment_short_<k>
Groups: garment_onepiece_wear / garment_dance_wear (all names), garment_prompt_onepiece_wear / garment_prompt_dance_wear / garment_prompt_wear, garment_outfit_wear
Usage: python garment_wear_build.py [wildcards_folder]; export_aoo(outdir) feeds simple_build.py"""
import os, re, sys, random, zlib
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from paths import FINAL
from garment_wear_data import F as FAM
from garment_culture_data import C as CULTF
from garment_reveal_data import R as REVF
from garment_swim_data import W as SWF
from swim_detail import swim_detail
from garment_detail import detail as gdetail
SWIM = list(SWF)
FAM = dict(FAM); FAM.update(CULTF); FAM.update(REVF); FAM.update(SWF); CULT = list(CULTF); REV = list(REVF)
ONE = ['coverall', 'zipsuit', 'leisure_onepiece', 'bodysuit', 'overalls', 'romper', 'unionsuit']
NIGHT = ['nightshirt', 'nightgown', 'negligee', 'pajamas', 'robe', 'robe_smoking', 'robe_world', 'robe_sexy']
UNDER = ['bra', 'underwear', 'shapewear', 'slip', 'lingerie', 'garterwear', 'sexy_underwear']
DANCE = ['leotard', 'singlet', 'wrestling', 'ballet', 'ballroom', 'folkdance', 'stagedance', 'burlesque', 'stripper', 'poledance', 'themeddance']
def rg(*k): return random.Random(zlib.crc32('|'.join(map(str, k)).encode()))
def names(k, d, n=300):
    R = rg('gw', k); out = set(d['types'])
    T, Fe, M, A = d['types'], d['feats'], d['mats'], d['adjs']
    tries = 0
    while len(out) < n and tries < 40000:
        tries += 1; t = R.choice(T); f = R.choice(Fe); m = R.choice(M); a = R.choice(A); c = R.randrange(6)
        out.add([f'{m} {t}', f'{t} with {f}', f'{a} {t}', f'{a} {t} with {f}', f'{m} {t} with {f}', f'{a} {m} {t}'][c])
    out = sorted(out); R.shuffle(out); return out
def build():
    G = {}
    for k, d in FAM.items():
        G[f'garment_{k}'] = names(k, d)
        G[f'garment_base_{k}'] = sorted(dict.fromkeys(d['types']))
        G[f'garment_feat_{k}'] = sorted(dict.fromkeys(d['feats'])); G[f'garment_mat_{k}'] = sorted(dict.fromkeys(d['mats']))
        G[f'garment_prompt_{k}'] = [f'__outfit_color__ __outfit_material__ __garment_{k}__, __clth_fit__, __clth_detail__.', f'__garment_{k}__ in __clth_fabric__, __outfit_color__, __clth_pattern__.',
            f'__outfit_pattern__ __garment_{k}__ in __outfit_color__ __outfit_material__, __clth_detail__.', f'__outfit_color__ __garment_base_{k}__ made of __garment_mat_{k}__ with __garment_feat_{k}__, __clth_fit__.',
            f'__garment_base_{k}__ in __garment_mat_{k}__ and __outfit_color__, with __garment_feat_{k}__ and __garment_feat_{k}__.', f'__outfit_pattern__ __garment_base_{k}__ in __outfit_color__, __garment_feat_{k}__, __clth_detail__.']
        G[f'garment_short_{k}'] = [f'__outfit_color__ __garment_{k}__', f'__outfit_color__ __outfit_material__ __garment_{k}__', f'__garment_{k}__']
    for k in FAM:
        if k in SWIM: continue
        G[f'garment_{k}_detail'] = [f'{x}: {gdetail(x)}' for x in G[f'garment_{k}']]
        G[f'garment_prompt_{k}_detail'] = [f'__outfit_color__ __garment_{k}_detail__.', f'__garment_{k}_detail__, __clth_fit__, __clth_detail__.']
    for k in SWIM:
        G[f'garment_{k}'] = [f'{x} ({swim_detail(k, x)})' for x in G[f'garment_{k}']]
        G[f'garment_base_{k}'] = [f'{x} ({swim_detail(k, x)})' for x in G[f'garment_base_{k}']]
    G['garment_onepiece_wear'] = sorted({x for k in ONE for x in G[f'garment_{k}']}); G['garment_dance_wear'] = sorted({x for k in DANCE for x in G[f'garment_{k}']})
    G['garment_night_wear'] = sorted({x for k in NIGHT for x in G[f'garment_{k}']}); G['garment_under_wear'] = sorted({x for k in UNDER for x in G[f'garment_{k}']})
    for nm, ks in (('onepiece_wear', ONE), ('dance_wear', DANCE), ('night_wear', NIGHT), ('under_wear', UNDER)):
        G[f'garment_prompt_{nm}'] = [f'__garment_prompt_{k}__' for k in ks]; G[f'garment_short_{nm}'] = [f'__garment_short_{k}__' for k in ks]
    G['garment_reveal_wear'] = sorted({x for k in ('seductive', 'mishap') for x in G[f'garment_{k}']}); G['garment_modest_wear'] = G['garment_modest']
    G['garment_prompt_reveal_wear'] = ['__garment_prompt_seductive__', '__garment_prompt_mishap__']; G['garment_prompt_modest_wear'] = ['__garment_prompt_modest__']
    G['garment_swim_wear'] = sorted({x for k in SWIM for x in G[f'garment_{k}']}); G['garment_prompt_swim_wear'] = [f'__garment_prompt_{k}__' for k in SWIM]; G['garment_short_swim_wear'] = [f'__garment_short_{k}__' for k in SWIM]
    G['garment_culture_wear'] = sorted({x for k in CULT for x in G[f'garment_{k}']}); G['garment_prompt_culture_wear'] = [f'__garment_prompt_{k}__' for k in CULT]; G['garment_short_culture_wear'] = [f'__garment_short_{k}__' for k in CULT]
    for d in ('1920s', '1930s', '1940s', '1950s', '1960s', '1970s', '1980s', '1990s', '2000s', '2010s', '2020s'):
        G[f'garment_culture_{d}'] = sorted({x for k in CULT for x in G[f'garment_{k}'] if d in x}) or G['garment_culture_wear'][:1]
    G['garment_prompt_wear'] = ['__garment_prompt_onepiece_wear__', '__garment_prompt_dance_wear__', '__garment_prompt_culture_wear__', '__garment_prompt_swim_wear__']; G['garment_prompt_intimate_wear'] = ['__garment_prompt_night_wear__', '__garment_prompt_under_wear__']
    s = lambda k: f'__garment_short_{k}__'
    G['garment_outfit_wear'] = [s('nightshirt'), s('nightgown'), s('negligee'), s('pajamas'), s('robe'), f"{s('robe_smoking')}, {s('pajamas')}", f"{s('robe_sexy')}, {s('lingerie')}", f"{s('robe')}, {s('nightgown')}", s('lingerie'), s('bra'), f"{s('bra')}, {s('underwear')}", s('shapewear'), f"{s('slip')}, {s('garterwear')}", s('sexy_underwear'), s('coverall'), s('zipsuit'), s('leisure_onepiece'), s('overalls'), f'{s("overalls")}, __garment_short_shirt__' if False else s('romper'), s('unionsuit'), f'{s("bodysuit")}, {s("overalls")}', s('leotard'), f'{s("leotard")}, {s("ballet")}', s('singlet'), s('wrestling'), s('ballet'), s('ballroom'), s('folkdance'), s('stagedance'), s('burlesque'), s('stripper'), s('poledance'), s('themeddance'), f'{s("bodysuit")}, {s("stagedance")}']
    return G
def run(final):
    G = build()
    for n, l in G.items():
        assert l and all(l) and not any(re.search(r'[{}|]', x) for x in l), n
        open(os.path.join(final, n + '.txt'), 'w', encoding='utf8', newline='\n').write('\n'.join(l) + '\n')
    for g in ('f', 'm'):
        sp = os.path.join(final, f'{g}_prompt_master.txt')
        if os.path.exists(sp):
            src = [l.rstrip('\n') for l in open(sp, encoding='utf8') if l.strip()]
            lines = [l.replace(f'__{g}_prompt_wardrobe__', 'Wearing __garment_prompt_wear__.') for l in src]
            if lines != src: open(os.path.join(final, f'{g}_prompt_master_garments_wear.txt'), 'w', encoding='utf8', newline='\n').write('\n'.join(lines) + '\n')
    print('garment wear:', len(G), 'files;', sum(len(G[f'garment_{k}']) for k in FAM), 'names'); return G
def export_aoo(out, prefix='aoo_'):
    G = build(); names_ = set(G); ren = {'outfit_color': 'clothing_color', 'outfit_material': 'clothing_material', 'outfit_pattern': 'clothing_pattern', 'clth_detail': 'clothing_detail', 'clth_fabric': 'clothing_fabric', 'clth_fit': 'clothing_fit', 'clth_pattern': 'clothing_pattern_description'}
    ref = re.compile(r'__([A-Za-z0-9_\-/]+)__'); n = 0
    for name, lines in G.items():
        keep = list(dict.fromkeys(l for l in lines if l.strip()))
        keep = [ref.sub(lambda m: '__' + prefix + ren.get(m.group(1), m.group(1)) + '__' if (m.group(1) in names_ or m.group(1) in ren) else m.group(0), l) for l in keep]
        if not name.startswith(('garment_prompt', 'garment_short', 'garment_outfit')): random.Random(zlib.crc32(name.encode())).shuffle(keep)
        open(os.path.join(out, prefix + name + '.txt'), 'w', encoding='utf8', newline='\n').write('\n'.join(keep) + '\n'); n += 1
    return n
if __name__ == '__main__':
    a = [x for x in sys.argv[1:] if os.path.isdir(x)]; run(os.path.abspath(a[0]) if a else FINAL)
