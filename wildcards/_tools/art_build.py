"""Artwork-on-objects (art_*), logos (logo_*) and tattoos (tattoo_*) wildcard systems.  Everything is original descriptive wording: no real brands, characters or trademarks, and no real people's names.
Entry points: run(final) writes the files; export_aoo(out) writes the 'all options once' version.  Deterministic (fixed seeds).

  art_on_object      finished description of an image / pattern / graphic on a product or material (style, subject, technique, layout, colours, feel, placement)
  art_subject*       what the image shows (animals with poses, plants, myth, sky, objects, food, scenes, symbols, abstract, patterns)    art_style  art_technique  art_layout  art_scale  art_feel  art_colourway  art_placement
  logo_mark          finished description of a (fictional) logo or label on an object        logo_type logo_subject logo_style logo_lettering logo_name logo_initials logo_colour logo_treatment logo_placement
  tattoo_set         one to three tattoos with styles, subjects, ink, size, placement, condition;  tattoo_one = a single tattoo       tattoo_style tattoo_subject tattoo_ink tattoo_size tattoo_placement tattoo_condition
  f_prompt_tattooed / m_prompt_tattooed   person prompts with tattoos;   acc_artwork = a sentence a bag/hat/ring/... can carry (used inside the accessory 'extras')"""
import os, sys, re, random, zlib, shutil
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from paths import FINAL
import vocab_art as A, vocab_art2 as B
from vocab_acc_pack import BASE, MODC
PATC = ['{a}', '{a} and {b}', '{a}, {b} and {c}', '{a} with {b} accents', '{a} fading into {b}', '{a} on {b}', '{a} colour-blocked with {b}', 'speckled {a} over {b}', '{a} with {b} stripes', '{a} marbled with {b}', 'mottled {a} and {b}', '{a} dip-dyed to {b}', '{a} with {b} polka dots', 'tie-dyed {a} and {b}', 'gradient from {a} to {b}', '{a} checked with {b}', '{a} with a {b} ombré', '{a}, {b} and {c} in bands', '{a} outlined in {b}', '{a} shaded with {b}']
from vocab_lib import S

def rg(*k): return random.Random(zlib.crc32('|'.join(map(str, k)).encode()))
def cap(s): return s[:1].upper() + s[1:]
def art(w): return ('an ' if w[0].lower() in 'aeiou' else 'a ') + w
def smp(r, x, n): x = list(x); return r.sample(x, min(n, len(x)))
def uniq(l): return sorted(set(x for x in l if x))

def colourway(n, seed):
    r = rg(seed); out = set(); tries = 0
    def pick(): return (r.choice(MODC) + ' ' + r.choice(BASE)) if r.random() < 0.3 else r.choice(BASE)
    while len(out) < n and tries < n * 20:
        tries += 1; a, b, c = pick(), pick(), pick()
        if len({a.split()[-1], b.split()[-1], c.split()[-1]}) < 3: continue
        out.add(r.choice(PATC).format(a=a, b=b, c=c))
    return sorted(out)

def grow(lst, target, seed, joiner=' and '):
    r = rg('grow', seed); base = uniq(lst); out = set(base); tries = 0
    while len(out) < target and tries < target * 30 and len(base) > 1:
        tries += 1; a, b = r.sample(base, 2); out.add(f'{a}{joiner}{b}')
    return sorted(out)

def build():
    F = {}; r = rg('art')
    def strip(w): return re.sub(r'^(a|an|the) ', '', w)
    # ---------------- subjects
    animal = set(); 
    for x in A.ANIMALS:
        animal.add(art(x))
        for p in smp(r, list(A.POSES), 7): animal.add(f'{art(x)} {p}')
        for m in smp(r, list(A.MODS), 4): animal.add(f'{art(m + " " + x)}')
    plant = set()
    for x in A.PLANTS:
        plant.add(art(x))
        for m in smp(r, list(A.MODS), 6): plant.add(art(m + ' ' + x))
        for p in smp(r, list(A.PLANTS), 3):
            if p != x: plant.add(f'{art(x)} entwined with {art(p)}')
    myth = set()
    for x in A.MYTH:
        myth.add(art(x))
        for p in smp(r, list(A.POSES), 6): myth.add(f'{art(x)} {p}')
        for m in smp(r, list(A.MODS), 4): myth.add(art(m + ' ' + x))
    sky = uniq([art(x) if not x.startswith(('a ', 'an ')) else x for x in A.SKY] + [f'{art(m + " " + strip(x))}' for x in A.SKY[:40] for m in smp(r, list(A.MODS), 3)])
    obj = set()
    for x in list(A.OBJECTS) + list(A.FOOD):
        obj.add(art(x))
        for m in smp(r, list(A.MODS), 5): obj.add(art(m + ' ' + x))
        for p in smp(r, list(A.PLANTS) + list(A.ANIMALS), 3): obj.add(f'{art(x)} with {art(p)} growing from it' if p in A.PLANTS else f'{art(x)} with {art(p)} perched on it')
    scene = uniq(A.SCENES + [f'{art(a)} and {art(b)}' for a, b in zip(smp(r, list(A.ANIMALS), 150), smp(r, list(A.OBJECTS), 150))] + [f'{art(a)} in a field of {b}' for a, b in zip(smp(r, list(A.ANIMALS), 120), smp(r, list(A.PLANTS), 120))] + [f'{art(a)} under {art(b)}' for a, b in zip(smp(r, list(A.MYTH), 60), smp(r, list(A.SKY), 60))])
    sym = uniq([x if x.startswith(('a ', 'an ')) else art(x) for x in A.SYMBOLS] + [f'{art(m + " " + strip(x))}' for x in A.SYMBOLS[:40] for m in smp(r, list(A.MODS), 3)])
    abst = uniq(A.ABSTRACT + [f'{x}, {c}' for x in A.ABSTRACT for c in smp(r, ['in a repeating row', 'fading at one end', 'overlapping itself', 'drawn in a single line', 'with a glow', 'in 3D relief', 'broken into fragments', 'partly erased'], 3)])
    pat = uniq([x for x in A.PATTERNS] + [f'{x}, {c}' for x in A.PATTERNS for c in smp(r, ['tightly repeated', 'blown up large', 'drawn small and dense', 'with irregular spacing', 'warped slightly', 'cut off at the edges', 'in a diagonal layout'], 3)])
    F.update({'art_subject_animal': uniq(animal), 'art_subject_plant': uniq(plant), 'art_subject_myth': uniq(myth), 'art_subject_sky': sky, 'art_subject_object': uniq(obj), 'art_subject_scene': scene, 'art_subject_symbol': sym, 'art_subject_abstract': abst, 'art_subject_pattern': pat})
    F['art_subject'] = [f'__{n}__' for n in ('art_subject_animal', 'art_subject_plant', 'art_subject_myth', 'art_subject_sky', 'art_subject_object', 'art_subject_scene', 'art_subject_symbol', 'art_subject_abstract', 'art_subject_pattern')]
    # ---------------- style etc.
    F['art_style'] = uniq(list(B.ART_STYLES) + [f'{a} meets {b}' for a, b in zip(smp(r, list(B.ART_STYLES), 220), smp(r, list(B.ART_STYLES), 220)) if a != b])
    F['art_technique'] = uniq(list(B.ART_TECH) + [f'{a} and {b}' for a, b in zip(smp(r, list(B.ART_TECH), 150), smp(r, list(B.ART_TECH), 150)) if a != b])
    F['art_layout'] = uniq(list(B.ART_LAYOUT) + [f'{a}, and {b}' for a, b in zip(smp(r, list(B.ART_LAYOUT), 120), smp(r, list(B.ART_LAYOUT), 120)) if a != b])
    F['art_scale'] = uniq(B.ART_SCALE); F['art_feel'] = uniq(list(B.ART_FEEL) + [f'{a} and {b}' for a, b in zip(smp(r, list(B.ART_FEEL), 150), smp(r, list(B.ART_FEEL), 150)) if a != b])
    F['art_colourway'] = colourway(1500, 'art-col')
    PL = "on the front, on the back, across the front panel, on the main surface, on the largest face, along one side, along the top edge, along the bottom edge, around the base, on the flap, on the lid, on the strap, on the handle, on the lining, on the inside, on the underside, on a patch, on a pocket, on the pocket flap, on a tab, across the shoulder, on the sleeve, on the cuff, on the brim, on the crown, on the band, on the toe, on the heel, on the sole, on the tongue, on the collar, on the zipper pull, on the buckle, on a metal plate, on a leather panel, on a fabric panel, on a woven label, on the cover, on the spine, on the face, on the hem, on the corner, in the center, in the corner, on both sides, on one side only, hidden on the inside, wrapped all the way around, running around the edge, repeated on every panel".split(', ')
    F['art_placement'] = uniq(PL + [f'{a}, and {b}' for a, b in zip(smp(r, PL, 80), smp(r, PL, 80)) if a != b])
    # ---------------- templates: finished description
    T = ['__art_scale__ __art_style__ image of __art_subject__, __art_technique__ __art_layout__ __art_placement__, __art_colourway__, __art_feel__',
         '__art_style__ artwork showing __art_subject__, __art_technique__, __art_layout__, in __art_colourway__',
         'a __art_scale__ graphic of __art_subject__ in the style of __art_style__, __art_technique__ __art_placement__, __art_feel__',
         '__art_subject__ rendered in __art_style__, __art_technique__ in __art_colourway__, __art_layout__',
         '__art_style__ pattern of __art_subject__, __art_technique__, __art_layout__, in __art_colourway__',
         'an illustration of __art_subject__ in the style of __art_style__, __art_layout__ __art_placement__, __art_feel__',
         '__art_style__ motif: __art_subject__, __art_technique__ __art_placement__, __art_colourway__',
         'a print of __art_subject__ and __art_subject__ together, __art_style__, __art_technique__, __art_layout__',
         'a __art_scale__ __art_style__ emblem of __art_subject__, __art_technique__ __art_placement__, in __art_colourway__',
         'surface art: __art_subject__, __art_style__, __art_technique__, __art_layout__, __art_colourway__, __art_feel__']
    F['art_on_object'] = T
    F['art_on_object_double'] = ['__art_on_object__. A second image: __art_on_object__', '__art_on_object__, together with __art_on_object__']
    F['art_set'] = ['__art_on_object__'] * 3 + ['__art_on_object_double__'] * 2
    # ---------------- logos
    sy = list(B.SYL); names = set()
    for _ in range(2600): names.add(cap(r.choice(sy) + r.choice(sy)) if r.random() < 0.6 else cap(r.choice(sy) + r.choice(sy) + r.choice(sy)))
    for a in B.ADJ_NAME:
        for n in smp(r, list(B.NOUN_NAME), 14): names.add(f'{a} {n}')
    for n in B.NOUN_NAME:
        for m in smp(r, list(B.NOUN_NAME), 10):
            if n != m: names.add(f'{n} & {m}')
    F['logo_name'] = uniq(names)
    L = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    F['logo_initials'] = uniq([r.choice(L) + r.choice(L) for _ in range(500)] + [r.choice(L) + '.' + r.choice(L) + '.' for _ in range(150)] + [r.choice(L) + r.choice(L) + r.choice(L) for _ in range(500)] + [f'{r.choice(L)}&{r.choice(L)}' for _ in range(150)])
    F['logo_type'] = uniq(B.LOGO_TYPE); F['logo_lettering'] = uniq(list(B.LOGO_LETTER) + [f'{a} with {b}' for a, b in zip(smp(r, list(B.LOGO_LETTER), 200), ['small ornamental swashes', 'a thin underline', 'a drop shadow', 'a double outline', 'a gradient fill', 'worn edges', 'a metallic fill', 'letterspaced wide', 'tight overlapping letters', 'a slanted baseline'] * 20) ])
    FORMS = ['a minimalist', 'a geometric', 'a line-art', 'a flat', 'a bold', 'a detailed engraved', 'a cartoon', 'a woodcut-style', 'a mid-century', 'a vintage', 'a pixel', 'a negative-space', 'a hand-drawn', 'an ornate', 'a monoline', 'a stencil-cut', 'a brush-stroked', 'a symmetrical', 'an abstracted', 'a stylized']
    subj = set(B.LOGO_SUBJ)
    for x in list(A.ANIMALS) + list(A.PLANTS) + list(A.MYTH) + list(A.OBJECTS):
        for f in smp(r, FORMS, 2): subj.add(f'{f} {x}')
    for s in A.SYMBOLS: subj.add(s if s.startswith(('a ', 'an ')) else art(s))
    F['logo_subject'] = uniq(subj)
    F['logo_style'] = uniq(list(B.ART_STYLES) + "flat minimalist, mid-century modern, 1970s retro, 1980s neon, 1990s tech, Y2K chrome, vintage Americana, western saloon, nautical heritage, outdoor-adventure badge, craft-brewery label, farm-stand chalkboard, hand-lettered diner sign, vintage soda label, speakeasy art deco, luxury minimal serif, couture monogram, streetwear block letters, skate-shop sticker, punk band stencil, metal band illegible tangle, hip-hop graffiti tag, K-pop pastel, gothic blackletter, tattoo-parlor flash, barbershop pole, vintage motorcycle club patch, racing team crest, collegiate varsity, military unit patch, scouting badge, fantasy guild sigil, sci-fi corporation, futurist, techno minimal, organic hand-drawn, eco-natural, Scandinavian simple, Japanese minimal, Swiss modernist, brutalist, hand-cut paper, glassmorphism, gradient mesh, sticker bomb, comic-book burst".split(', '))
    F['logo_colour'] = uniq(list(B.LOGO_COLOUR_NOTE) + colourway(1000, 'logo-col'))
    F['logo_treatment'] = uniq(B.LOGO_TREAT); F['logo_placement'] = F['art_placement']
    LT = ['__logo_type__ showing __logo_subject__ with the name "__logo_name__" in __logo_lettering__, __logo_style__, __logo_colour__, __logo_treatment__ __logo_placement__',
          '__logo_type__ of the letters "__logo_initials__" in __logo_lettering__, __logo_style__, __logo_colour__, __logo_treatment__ __logo_placement__',
          '__logo_type__ with __logo_subject__ and no text, __logo_style__, __logo_colour__, __logo_treatment__ __logo_placement__',
          'a logo reading "__logo_name__" in __logo_lettering__ beside __logo_subject__, __logo_style__, __logo_colour__, __logo_treatment__ __logo_placement__',
          '__logo_type__: __logo_subject__ inside a ring with "__logo_name__" lettered around it, __logo_style__, __logo_colour__, __logo_treatment__',
          '__logo_type__ in a __logo_style__ style with __logo_subject__, __logo_treatment__ __logo_placement__, __logo_colour__',
          'the initials "__logo_initials__" in __logo_lettering__ with __logo_subject__ beneath, __logo_style__, __logo_colour__, __logo_treatment__',
          '__logo_type__ in the style of __logo_style__: "__logo_name__" set in __logo_lettering__, __logo_colour__, __logo_treatment__ __logo_placement__']
    F['logo_mark'] = LT
    F['logo_mark_double'] = ['__logo_mark__, with a second smaller mark: __logo_mark__', '__logo_mark__, plus a tiny tag reading "__logo_name__" __logo_placement__']
    F['logo_set'] = ['__logo_mark__'] * 3 + ['__logo_mark_double__'] * 1
    # ---------------- tattoos
    sub = set(B.TATT_RAW)
    for f in ('art_subject_animal', 'art_subject_plant', 'art_subject_myth', 'art_subject_sky', 'art_subject_object', 'art_subject_scene', 'art_subject_symbol', 'art_subject_abstract'):
        for x in smp(r, F[f], min(len(F[f]), 600)): sub.add(x)
    F['tattoo_subject'] = uniq(sub)
    F['tattoo_style'] = uniq(list(B.TATT_STYLE) + [f'{a} blended with {b}' for a, b in zip(smp(r, list(B.TATT_STYLE), 220), smp(r, list(B.TATT_STYLE), 220)) if a != b])
    F['tattoo_ink'] = uniq(list(B.TATT_INK) + [f'in {c}' for c in colourway(600, 'tat-col')])
    F['tattoo_size'] = uniq(list(B.TATT_SIZE) + [f'{a}, {b}' for a, b in zip(smp(r, list(B.TATT_SIZE), 80), smp(r, list(B.TATT_SIZE), 80)) if a != b])
    place = list(B.TATT_PLACE); sides = ['left', 'right']
    pl2 = set(place)
    for p in place:
        for sd in sides:
            m = re.match(r'^on the (inner forearm|outer forearm|upper arm|shoulder|shoulder blade|side of the neck|wrist|collarbone|calf|shin|thigh|outer thigh|ankle|top of the foot|elbow|temple|inner bicep|shoulder cap)$', p)
            if m: pl2.add(f'on the {sd} {m.group(1)}')
    for a, b in zip(smp(r, place, 160), smp(r, place, 160)):
        if a != b: pl2.add(f'{a} and {b}')
    F['tattoo_placement'] = uniq(pl2); F['tattoo_condition'] = uniq(list(B.TATT_COND) + [f'{a}, {b}' for a, b in zip(smp(r, list(B.TATT_COND), 90), smp(r, list(B.TATT_COND), 90)) if a != b])
    TT = ['a __tattoo_size__ __tattoo_style__ tattoo of __tattoo_subject__ __tattoo_ink__ __tattoo_placement__, __tattoo_condition__',
          '__tattoo_placement__: __tattoo_subject__, a __tattoo_style__ tattoo __tattoo_ink__',
          'a tattoo of __tattoo_subject__ __tattoo_placement__, __tattoo_style__, __tattoo_ink__',
          'a __tattoo_style__ tattoo __tattoo_placement__ showing __tattoo_subject__, __tattoo_size__, __tattoo_condition__',
          '__tattoo_subject__ tattooed __tattoo_placement__ in the style of __tattoo_style__, __tattoo_ink__',
          'a __tattoo_size__ tattoo __tattoo_placement__: __tattoo_subject__, __tattoo_style__']
    F['tattoo_one'] = TT
    F['tattoo_two'] = ['__tattoo_one__; also __tattoo_one__', '__tattoo_one__, and elsewhere __tattoo_one__']
    F['tattoo_many'] = ['__tattoo_one__; __tattoo_one__; and __tattoo_one__', '__tattoo_one__; __tattoo_one__; __tattoo_one__; and more']
    F['tattoo_set'] = ['__tattoo_one__'] * 4 + ['__tattoo_two__'] * 3 + ['__tattoo_many__'] * 1
    F['tattoo_cover'] = ['a full sleeve in a consistent __tattoo_style__ theme of __tattoo_subject__, __tattoo_ink__', 'a half sleeve of __tattoo_subject__ flowing into __tattoo_subject__, __tattoo_style__, __tattoo_ink__', 'a full back piece showing __tattoo_subject__, __tattoo_style__, __tattoo_ink__, __tattoo_condition__', 'a leg sleeve of __tattoo_subject__ in __tattoo_style__, __tattoo_ink__', 'hand and finger tattoos of __tattoo_subject__ in __tattoo_style__']
    for k, j in (('art_scale', ', '), ('art_feel', ', and '), ('art_layout', '; also '), ('art_technique', ', then '), ('art_placement', ', also '), ('logo_type', ', combined with '), ('logo_treatment', ' and also '), ('logo_lettering', ' beside '), ('logo_placement', ', also '), ('tattoo_size', ', '), ('tattoo_condition', ', and '), ('tattoo_placement', ' together with '), ('art_subject_sky', ' above '), ('art_subject_symbol', ' beside ')):
        F[k] = grow(F[k], 260, k, j)
    # ---------------- accessory artwork sentence + person bridge
    F['acc_artwork'] = ['Its surface is decorated with __art_on_object__.', 'It carries a decoration of __art_on_object__.', 'It is decorated with __art_on_object__.', 'Its surface is covered with __art_on_object__.', 'It bears a mark of __logo_mark__.', 'It has a design of __logo_mark__.', 'It is marked with __logo_mark__.', 'Its surface shows __art_on_object__, together with __logo_mark__.']
    for g in ('f', 'm'):
        F[f'{g}_prompt_tattooed'] = [f'__{g}_prompt_master_by_age__ Tattoos: __tattoo_set__.', f'__{g}_prompt_master_by_age__ Tattoo detail: __tattoo_cover__.']
    return F

def run(final):
    files = build()
    for n, lines in files.items():
        assert not any(re.search(r'[{}|]', l) for l in lines), (n, [l for l in lines if re.search(r'[{}|]', l)][:2])
        open(os.path.join(final, n + '.txt'), 'w', encoding='utf8', newline='\n').write('\n'.join(lines) + '\n')
    print('art/logo/tattoo:', len(files), 'files;', {k: len(files[k]) for k in ('art_subject_animal', 'art_style', 'art_colourway', 'logo_name', 'logo_subject', 'tattoo_subject', 'tattoo_style', 'tattoo_placement')})
    return files

TEMPL = re.compile(r'(prompt|_mark$|_one$|_two$|_many$|_set$|_cover$|on_object|_double$)')
def export_aoo(out, prefix='aoo_'):
    tmp = os.path.join(out, '_art_tmp'); os.makedirs(tmp, exist_ok=True); files = run(tmp); shutil.rmtree(tmp)
    names = set(files); ref = re.compile(r'__([A-Za-z0-9_\-/]+)__'); n = 0
    for name, lines in files.items():
        if name.startswith(('f_', 'm_')): continue
        seen = set(); keep = []
        for l in lines:
            if not l.strip() or l in seen: continue
            seen.add(l); keep.append(ref.sub(lambda m: '__' + prefix + m.group(1) + '__' if m.group(1) in names else m.group(0), l))
        if not TEMPL.search(name): random.Random(zlib.crc32(name.encode())).shuffle(keep)
        open(os.path.join(out, prefix + name + '.txt'), 'w', encoding='utf8', newline='\n').write('\n'.join(keep) + '\n'); n += 1
    open(os.path.join(out, prefix + 'prompt_tattooed.txt'), 'w', encoding='utf8').write(f'__{prefix}prompt_full__ Tattoos: __{prefix}tattoo_set__.\n')
    return n + 1

if __name__ == '__main__':
    a = [x for x in sys.argv[1:] if os.path.isdir(x)]; run(os.path.abspath(a[0]) if a else FINAL)
