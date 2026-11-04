ONELINE = 'outerwear, hats, bags, scarves, gloves and belts built from parts; quad-panel prompt fix'
BULLETS = ["Outerwear, hats, bags, scarves, gloves and belts are now built from parts. 16 outerwear types (trench coat, parka, peacoat, puffer, bomber, denim and leather jackets, overcoat, rain poncho, cloak, anorak, windbreaker, duffle coat, quilted vest, blazer, kimono-style jacket), 12 hats, 11 bags, 7 scarves and wraps, 6 gloves and 6 belts.",
"Each item is fully described. A fixed description of the shape, then a material, colour, pattern, lining, closure, pockets, collar, cuffs, hardware and a condition are chosen separately, so every result is different. Shared pools sit in `wear_<category>_<part>` and special cases (a poncho has no cuffs, a suitcase has wheels, a turban has no band) have their own files.",
"Use them whole or by part. `wear_prompt` picks anything, `wear_outerwear_prompt`, `wear_hats_prompt`, `wear_bags_prompt`, `wear_scarves_prompt`, `wear_gloves_prompt` and `wear_belts_prompt` pick one category, and `wear_<category>_<type>_prompt` makes one type (for example `wear_outerwear_trench_coat_prompt`). `wear_colour`, `wear_pattern` and `wear_condition` can be used on their own.",
"Fix. `frame_animal_quad_prompt` now reads naturally (each panel is introduced by its corner and then the full animal prompt).",
"100 random sample prompts, one per line with no blank lines, show every category of wearable item, products and framing."]
README = """Guyanonymous' Wildcards v58 - outerwear and accessories from parts
==================================================================
Items       wear_outerwear / wear_hats / wear_bags / wear_scarves / wear_gloves / wear_belts   (58 types)
Parts       wear_<category>_<part>, wear_<category>_<type>_<part> (special cases), wear_colour, wear_pattern, wear_condition
Prompts     wear_prompt, wear_<category>_prompt, wear_<category>_<type>_prompt, wear_<category>_names
Fix         frame_animal_quad_prompt rewritten
All Options Once includes all of these.
"""
GEN_ROW = '("wear_<category>_<type>_*, wear_prompt","58 types / 6 categories","v58 outerwear, hats, bags, scarves, gloves and belts built from parts, with a different material, colour, pattern, closure and condition every time."),'
SAMPLES = [('wearable item', '__wear_prompt__', 28), ('outerwear', '__wear_outerwear_prompt__', 14), ('hat', '__wear_hats_prompt__', 8), ('bag', '__wear_bags_prompt__', 8), ('scarf', '__wear_scarves_prompt__', 6), ('gloves', '__wear_gloves_prompt__', 5), ('belt', '__wear_belts_prompt__', 5), ('product shot', '__frame_accessory_prompt__', 4), ('quad animals', '__frame_animal_quad_prompt__', 3),
 ('person in a coat', '__frame_person_prompt_short__ Wearing __wear_outerwear_prompt__', 8), ('person with bag', '__frame_person_prompt_short__ Carrying __wear_bags_prompt__', 6), ('person in hat', '__frame_person_prompt_short__ Wearing __wear_hats_prompt__', 5)]
