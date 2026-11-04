"""Vocabulary expansion for the outfit_*_mixed files: many more assembled-outfit lines (they point at the expanded outfit_* lists)."""
import itertools, random
from vocab_lib import S, sample, seed_of

C = '__outfit_color__'; M = '__outfit_material__'; PAT = '__outfit_pattern__'
TOPADJ = S("oversized, relaxed, fitted, cropped, boxy, soft, lightweight, chunky, layered, slouchy, vintage-style, minimalist, textured")
SHOES_C = S("sneakers, canvas shoes, trainers, ankle boots, chunky boots, sandals, loafers, slip-on shoes, high-top sneakers, platform sneakers, flat shoes, espadrilles, clogs")
TAIL_C = S("casual style, everyday casual look, comfortable casual wear, street casual fashion, relaxed weekend look, easy off-duty style, laid-back outfit, simple everyday outfit, effortless casual look, comfortable day-out outfit, easy errand-running outfit, city-walking outfit")
ACC_C = S("a canvas tote bag, a crossbody bag, a baseball cap, a woven belt, a simple watch, a bandana, sunglasses pushed up on the head, a backpack, a thin scarf, a beanie, a bucket hat, layered necklaces, small hoop earrings, a leather bracelet, no accessories")

def casual(g):
    top = [f'__outfit_casual_top__', f'{C} __outfit_casual_top__', f'{C} {M} __outfit_casual_top__', f'{PAT} __outfit_casual_top__'] + [f'{a} {C} __outfit_casual_top__' for a in TOPADJ]
    bot = [f'__outfit_casual_bottom__', f'{C} __outfit_casual_bottom__', f'{M} __outfit_casual_bottom__', f'{C} {M} __outfit_casual_bottom__', f'{PAT} __outfit_casual_bottom__']
    out = [f'{t}, {b}, {s}, {a}, {tl}' for t in top for b in bot for s in SHOES_C for a in ACC_C[:4] for tl in TAIL_C[:3]]
    if g == 'm':
        out += [f'{C} __outfit_outerwear__ over a {t}, {b}, {s}, {tl}' for t in top for b in bot for s in SHOES_C[:6] for tl in TAIL_C[:3]]
    else:
        out += [f'{C} __outfit_dress_style__, a light cardigan, {s}, {tl}' for s in SHOES_C for tl in TAIL_C] + [f'{p} __outfit_dress_style__, {a}, {s}, {tl}' for p in (C, PAT, f'{C} {M}') for a in ACC_C for s in SHOES_C for tl in TAIL_C[:3]]
    return sample(out, 300, 'mix_casual' + g)

SHOES_F = S("high heels, pointed pumps, block-heeled sandals, strappy heels, kitten heels, polished loafers, ankle boots, ballet flats, slingbacks, platform heels, oxford shoes, wedge heels, mules")
SHOES_FM = S("polished leather shoes, oxford shoes, derby shoes, loafers, brogues, dress boots, patent shoes, monk-strap shoes, suede loafers, chelsea boots")
TAIL_F = S("sophisticated formal wear, polished formal look, elegant evening look, refined business formal, classic formal outfit, high-class formal, professional elegance, dressed for a gala, dressed for the opera, dressed for a wedding, dressed for an awards night, dressed for a black-tie dinner, dressed for a cocktail party, dressed for an important meeting")
ACC_F = S("a clutch bag, statement earrings, a pearl necklace, a thin belt, a silk scarf, a structured handbag, a cocktail ring, a slim watch, a brooch, drop earrings, long gloves, a wrap, a fascinator")
ACC_FM = S("a pocket square, cufflinks and a watch, a silk tie, a bow tie, a tie clip, a waistcoat and pocket watch, a boutonniere, a leather briefcase, a trench coat over the arm, a folded umbrella, a signet ring, a leather belt")

def formal(g):
    if g == 'f':
        out = [f'{a} {C} {M} __outfit_dress_style__, {s}, {ac}, {tl}' for a in S("elegant, luxurious, tailored, understated, striking, classic, graceful, polished") for s in SHOES_F for ac in ACC_F for tl in TAIL_F[:5]]
        out += [f'tailored {C} business suit, crisp shirt, {s}, {ac}, formal office attire' for s in SHOES_F for ac in ACC_F]
        out += [f'smart casual {C} blazer, neat trousers, {s}, {ac}, modern formal' for s in SHOES_F for ac in ACC_F]
    else:
        out = [f'{a} {C} __outfit_suit_style__, crisp shirt, {s}, {ac}, {tl}' for a in S("tailored, sharp, classic, luxurious, understated, modern, distinguished, slim-cut") for s in SHOES_FM for ac in ACC_FM for tl in TAIL_F[:5]]
        out += [f'{C} {M} __outfit_suit_style__, {s}, {ac}, high-class formal' for s in SHOES_FM for ac in ACC_FM]
        out += [f'smart casual {C} blazer, white shirt, neat trousers, {s}, {ac}, modern formal' for s in SHOES_FM for ac in ACC_FM]
    return sample(out, 300, 'mix_formal' + g)

ADJ_U = S("neat, crisp, worn, practical, regulation, standard-issue, freshly pressed, well-used, ceremonial, tidy, rugged, sharp, classic, modern")
TAIL_U = S("highly detailed outfit, neat and tidy look, professional appearance, worn and practical look, matching accessories, ready for the shift, ready for inspection, ready for a long day, with a name badge, with a lanyard, with polished buttons, with sensible shoes")
def uniform(g):
    out = [f'{a} {C} __outfit_uniform_type__, {t}' for a in ADJ_U for t in TAIL_U] + [f'__outfit_uniform_type__ in {C}, {t}' for t in TAIL_U] + [f'{C} and {C} __outfit_uniform_type__, {t}' for t in TAIL_U]
    out += [f'{a} {C} {M} __outfit_uniform_type__, {t}' for a in ADJ_U for t in TAIL_U]
    return sample(out, 260, 'mix_uniform' + g)

def sexy(g):
    TAIL = S("evening-out look, party look, date-night look, confident look, glamorous look, summer-night look, club-night look, holiday look, resort look")
    out = []
    if g == 'f':
        for t in TAIL:
            out += [f'{C} __outfit_sexy_top__, {C} __outfit_sexy_bottom__, {t}', f'{C} {M} __outfit_sexy_top__, __outfit_sexy_bottom__, {t}', f'{C} __outfit_sexy_full__, {t}', f'{C} {M} __outfit_sexy_full__, {t}', f'{C} __outfit_lingerie__, {t}', f'__outfit_see_through__, {t}', f'{PAT} __outfit_sexy_top__, {C} __outfit_sexy_bottom__, {t}']
        out += [f'{C} __outfit_sexy_top__, {C} __outfit_sexy_bottom__, {s}' for s in S("heels, strappy sandals, platform boots, ankle boots, sneakers, knee-high boots, barefoot")]
        out += [f'{C} __outfit_sexy_full__, {s}, {a}' for s in S("heels, strappy sandals, platform boots, ankle boots, barefoot") for a in S("a clutch bag, statement earrings, layered necklaces, a body chain, a choker, bangles, no jewellery")]
    return sample(out, 200, 'mix_sexy' + g) if out else ['__outfit_see_through__']

def swim(g):
    TAIL = S("beach look, poolside look, summer look, seaside look, holiday look, lazy-day look, resort look, surf-day look")
    ACC = S("sunglasses, a straw hat, a beach towel over the shoulder, sandals, flip-flops, a bucket hat, a rash guard, a long open shirt, a sarong, a snorkel mask pushed up")
    out = [f'{C} __outfit_swim_underwear__, {a}, {t}' for a in ACC for t in TAIL] + [f'{C} {M} __outfit_swim_underwear__, {a}, {t}' for a in ACC for t in TAIL] + [f'__outfit_swim_underwear__ with a loose open shirt, {t}' for t in TAIL] + [f'__outfit_see_through__, {t}' for t in TAIL[:3]]
    return sample(out, 200, 'mix_swim' + g)

def mixed_lines(g, kind):
    return {'casual': casual, 'formal': formal, 'uniform': uniform, 'sexy': sexy, 'swim': swim}[kind](g)

# --- register the clothing-detail composers into the shared registry ---
try:
    import vocab_clothing_b as _VB
    from vocab_face import R as _R
    for _n in ('clth_detail', 'clth_fabric', 'clth_fit', 'clth_layers', 'clth_pattern'):
        _R[_n] = getattr(_VB, _n)
except ImportError:
    pass
