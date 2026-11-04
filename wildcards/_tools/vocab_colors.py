"""World-population tables for eye colour and hair colour.
Group totals (percent of adults, before the age model scales hair colour for grey / white):
  eyes : brown ~77, blue ~8.5, hazel ~5, amber ~4.5, green ~2, grey ~0.9, heterochromia ~0.5, very rare / age-related the rest
  hair : black (incl. very dark brown-black) ~76, brown ~12, blonde ~2, red ~1.2, grey / white ~6.8 (the age model scales this up with age), fashion dyes ~2
Within a group the variants split the share (shade words x finish words) so the file has 200+ different, plausible options."""
import itertools

def _table(group_total, shades, mods, shade_w=None):
    """shades: list of shade phrases; mods: list of finish phrases ('' = none); weights spread over shade x mod, shade_w optional per-shade weights"""
    pairs = [(s, m) for s in shades for m in mods]
    sw = shade_w or [1.0] * len(shades)
    w = []
    for s, m in pairs:
        w.append(sw[shades.index(s)])
    tot = sum(w)
    return [(f'{s} {m}'.strip(), group_total * wi / tot) for (s, m), wi in zip(pairs, w)]

# ---------------------------------------------------------------- EYES
def eye_table():
    T = []
    # brown (77): originals kept with their old weights inside the group, new shade x finish variants share the rest
    brown_orig = [("deep chocolate brown irises", 22), ("almost black dark brown irises", 16), ("rich chestnut brown eyes", 12), ("golden honey brown irises", 8), ("dark obsidian irises", 6), ("dull muddy brown irises", 4)]
    brown_new = _table(77 - 0.0, ["dark brown", "very dark brown", "medium brown", "warm brown", "cool dark brown", "black-brown", "light brown", "reddish brown", "golden brown", "honey brown", "chestnut brown", "coffee brown", "espresso brown", "walnut brown", "umber brown", "mahogany brown", "caramel brown", "hazelnut brown", "tea brown", "soft brown"],
        ["irises", "eyes", "irises with a dark outer ring", "eyes with a subtle golden halo near the pupil", "irises with fine radial streaks", "eyes with a glossy depth", "irises that look almost black in low light", "eyes that lighten to amber in sunlight", "irises with a soft even tone", "eyes with a slightly lighter centre"],
        [5, 5, 5, 3, 3, 2, 3, 2, 2.5, 2.5, 2.5, 2, 2, 2, 2, 1.5, 1.5, 1.5, 1.2, 2.5])
    # scale originals into the group: they take 25% of it
    sc_o = 77 * 0.25 / sum(w for _, w in brown_orig); sc_n = 77 * 0.75 / sum(w for _, w in brown_new)
    T += [(n, w * sc_o) for n, w in brown_orig] + [(n, w * sc_n) for n, w in brown_new]
    # amber 4.5
    T += [("rare pale amber irises", 4.5 * 0.2)] + [(n, w * 0.8) for n, w in _table(4.5, ["amber", "golden amber", "copper amber", "light amber", "deep amber", "yellow-gold", "wolf-like amber", "tawny", "burnt-gold", "bronze"], ["irises", "eyes", "irises with a soft inner glow", "eyes with fine brown flecks", "irises with a dark rim"])]
    # hazel 5
    T += [("warm hazel irises with gold flecks", 5 * 0.2), ("warm golden hazel eyes", 5 * 0.1), ("speckled green-brown irises", 5 * 0.1)] + [(n, w * 0.6) for n, w in _table(5, ["hazel", "light hazel", "dark hazel", "green-hazel", "golden hazel", "brown-hazel", "mossy hazel", "amber-hazel", "greyish hazel", "warm hazel"], ["irises", "eyes", "irises that shift between green and brown", "eyes with a starburst of gold", "irises with a dark brown ring", "eyes with a lighter inner ring"])]
    # blue 8.5
    blue_orig = [("striking piercing blue irises", 3), ("pale washed-out light blue eyes", 1.5), ("cool ice blue irises", 1), ("bright sapphire blue eyes", 1.5), ("pale watery blue irises", 1)]
    sc = 8.5 * 0.25 / sum(w for _, w in blue_orig)
    T += [(n, w * sc) for n, w in blue_orig] + [(n, w * 0.75) for n, w in _table(8.5, ["light blue", "pale blue", "mid blue", "deep blue", "steel blue", "cornflower blue", "ice blue", "sky blue", "grey-blue", "green-blue", "navy-edged blue", "denim blue", "azure", "slate blue", "soft blue"], ["irises", "eyes", "irises with a darker limbal ring", "eyes with white flecks near the pupil", "irises with a crisp radial pattern", "eyes with a clear glassy look"])]
    # green 2
    T += [("vibrant emerald green irises", 2 * 0.2), ("olive green irises", 2 * 0.2)] + [(n, w * 0.6) for n, w in _table(2, ["green", "light green", "deep green", "grey-green", "yellow-green", "emerald", "olive", "jade", "sage green", "forest green", "blue-green"], ["irises", "eyes", "irises with golden flecks near the pupil", "eyes with a darker outer ring", "irises with a soft misty look"])]
    # grey 0.9
    T += [("cool dark grey irises", 0.9 * 0.2), ("pale translucent grey eyes", 0.9 * 0.15), ("dark charcoal grey irises", 0.9 * 0.1)] + [(n, w * 0.55) for n, w in _table(0.9, ["silver-grey", "light grey", "steel grey", "storm grey", "blue-grey", "green-grey", "slate grey", "pale grey", "smoky grey"], ["irises", "eyes", "irises with a pale ring", "eyes with a faint blue cast"])]
    # heterochromia and rarities 0.6
    T += [("mismatched blue and brown heterochromia eyes", 0.15), ("clear brilliant cyan eyes", 0.1), ("deep violet-tinged irises", 0.02), ("reddish albino pink irises", 0.01)]
    T += [(n, w) for n, w in _table(0.35, ["central heterochromia with a gold ring", "sectoral heterochromia with a brown patch", "one eye slightly lighter than the other", "complete heterochromia with one blue and one hazel eye", "complete heterochromia with one green and one brown eye", "complete heterochromia with one grey and one blue eye"], ["", "in soft light"])]
    # age-related / rare conditions (kept, tiny; the age model moves the first two to old ages)
    T += [("cloudy milky grey cataract-affected eyes", 0.2), ("faded cloudy aged irises", 0.25), ("yellowish jaundiced hazel eyes", 0.02), ("turbid yellowish eyes", 0.02)]
    # merge duplicates
    d = {}
    for n, w in T: d[n] = d.get(n, 0) + w
    return list(d.items())

# ---------------------------------------------------------------- HAIR
def hair_table():
    T = []
    FIN = ["", "with a natural gloss", "with a soft matte finish", "with faint lighter highlights in sunlight", "with a healthy sheen", "with a slightly lighter top layer", "with subtle depth of tone"]
    # black ~76
    black_orig = [("jet black dark shiny hair", 22), ("dark raven black hair", 14), ("jet black with blue sheen", 3)]
    sc = 76 * 0.3 / sum(w for _, w in black_orig)
    T += [(n, w * sc) for n, w in black_orig]
    T += [(n, w * 0.7) for n, w in _table(76, ["jet black hair", "soft black hair", "natural black hair", "blue-black hair", "deep black hair", "raven black hair", "true black hair", "off-black hair", "brownish-black hair", "warm black hair", "cool black hair", "ink black hair", "darkest brown-black hair", "black-brown hair"], FIN, [4, 4, 5, 2, 3, 3, 3, 2, 3, 2, 2, 2, 2, 3])]
    # brown ~12
    brown_orig = [("rich chocolate brown hair", 12), ("dark brown with dark roots", 1.5), ("golden chestnut brown hair", 3.5), ("warm hazelnut brown hair", 3), ("ash brown dull hair", 3)]
    sc = 12 * 0.3 / sum(w for _, w in brown_orig)
    T += [(n, w * sc) for n, w in brown_orig]
    T += [(n, w * 0.7) for n, w in _table(12, ["dark brown hair", "medium brown hair", "light brown hair", "chestnut brown hair", "chocolate brown hair", "espresso brown hair", "ash brown hair", "golden brown hair", "mousy brown hair", "warm brown hair", "cool brown hair", "reddish brown hair", "walnut brown hair", "caramel brown hair", "mahogany brown hair", "coffee brown hair", "toffee brown hair", "chestnut hair with golden tones"], FIN, [5, 5, 3, 3, 3, 2, 2, 2, 2, 2, 2, 2, 1.5, 1.5, 1.5, 1.5, 1, 1.5])]
    # blonde ~2
    blonde_orig = [("natural honey blonde hair", 1.2), ("dirty blonde hair", 1.5), ("light ash blonde hair", 0.8), ("golden wheat blonde hair", 0.8), ("natural strawberry blonde hair", 0.3)]
    sc = 2 * 0.3 / sum(w for _, w in blonde_orig)
    T += [(n, w * sc) for n, w in blonde_orig]
    T += [(n, w * 0.7) for n, w in _table(2, ["dark blonde hair", "golden blonde hair", "honey blonde hair", "ash blonde hair", "light blonde hair", "sandy blonde hair", "dirty blonde hair", "wheat blonde hair", "platinum blonde hair", "flaxen blonde hair", "butter blonde hair", "champagne blonde hair", "straw blonde hair", "strawberry blonde hair"], FIN[:6])]
    # red ~1.2
    red_orig = [("copper red hair", 0.6), ("vibrant fiery red auburn hair", 0.6), ("bright orange-red hair", 0.2)]
    sc = 1.2 * 0.3 / sum(w for _, w in red_orig)
    T += [(n, w * sc) for n, w in red_orig]
    T += [(n, w * 0.7) for n, w in _table(1.2, ["ginger red hair", "copper red hair", "auburn hair", "deep auburn hair", "light copper hair", "russet red hair", "burnt orange hair", "bright natural red hair", "dark red hair", "rust red hair", "cinnamon red hair", "red-gold hair"], FIN[:6])]
    # grey / white 6.8 (age model scales it)
    grey_orig = [("salt-and-pepper grey mixed hair", 4), ("silver grey aging hair", 4), ("pure snowy white hair", 2), ("mottled grey-brown hair", 1.5), ("dull greyish brown hair", 1.2)]
    sc = 6.8 * 0.3 / sum(w for _, w in grey_orig)
    T += [(n, w * sc) for n, w in grey_orig]
    T += [(n, w * 0.7) for n, w in _table(6.8, ["salt-and-pepper grey hair", "silver grey hair", "steel grey hair", "light grey hair", "dark grey hair", "pewter grey hair", "ash grey hair", "snowy white hair", "silvery white hair", "cream-white hair", "grey hair with dark streaks", "grey hair with a few dark strands", "white hair with grey patches", "white-streaked dark hair", "grey at the temples"], ["", "with a soft sheen", "with a coarse wiry texture", "with a smooth silky look", "with a yellowish tint at the ends"])]
    # fashion dyes ~2
    dye_orig = [("bright neon dyed magenta hair", 0.1), ("faded pink pastel hair", 0.2), ("faded dye green-tinted hair", 0.05), ("vibrant royal blue dyed hair", 0.1), ("platinum blonde bleached hair", 1.5), ("bleached brassy yellow hair", 0.8), ("deep burgundy red hair", 1.0)]
    sc = 2.0 * 0.35 / sum(w for _, w in dye_orig)
    T += [(n, w * sc) for n, w in dye_orig]
    T += [(n, w * 0.65) for n, w in _table(2.0, ["pastel pink dyed hair", "pastel blue dyed hair", "pastel lilac dyed hair", "pastel mint dyed hair", "pastel peach dyed hair", "neon pink dyed hair", "neon blue dyed hair", "neon green dyed hair", "neon orange dyed hair", "vivid purple dyed hair", "vivid teal dyed hair", "vivid red dyed hair", "vivid magenta dyed hair", "electric blue dyed hair", "silver-lavender dyed hair", "rose gold dyed hair", "copper-pink dyed hair", "burgundy dyed hair", "plum dyed hair", "jet black dyed hair", "bleached white dyed hair", "ombre dyed hair fading from dark to light", "two-tone dyed hair with a bright underlayer", "rainbow-streaked dyed hair"], ["", "with a glossy finish", "with visible regrowth at the roots"])]
    d = {}
    for n, w in T: d[n] = d.get(n, 0) + w
    return list(d.items())

if __name__ == '__main__':
    for name, t in (('eye', eye_table()), ('hair', hair_table())):
        tot = sum(w for _, w in t)
        print(name, len(t), 'options; total weight', round(tot, 1))
