import v101_build as _B
ONELINE = 'object-first brand styles, optional brand marks, object-neutral styles and samples of everything'
BULLETS = ["New __bs_mark__ add-on: a small mark built from random shape, material, outline, size and position, carrying a fake logo and name from the name system. Add it by hand to any prompt or use bs_marked_prompt for a random one.",
 "Brand styles are about design mentality, not one object: sentences naming shoes, cars, bags, shops and other objects were removed from 122 styles (84 styles that are only about one kind of object are unchanged).",
 "Converse rewritten as linework, curves, materials and palette, with a random simple shape as its motif.",
 "Brand-style prompts now start with the object tied to the style ('A wallet done in a design language of ...'), give the short style, and repeat the object once at the end, so the style and the object stay connected.",
 "Subject lists no longer contain shops, kiosks, stations, posters or signs that invite garbled text.",
 "Sample files now draw one prompt from every family of the package (about 90 families), so they show everything it can do; the showcase files show what is new in this version.",
 "A 40-image prompt showcase at 1024 and 1408 pixel counts, steps 50, cfg 3.75, and 100 sample prompts."]
README = """Guyanonymous' Wildcards v101 - brand marks
Prompts  bs_marked_prompt adds a random small mark
"""
GEN_ROW = '("brand marks","random marks","v101 optional marks, object-neutral styles."),'
DOCS = ['/home/claude/w/docs/INDEX_v101.txt', '/home/claude/w/docs/STANDING_RULES.txt', '/home/claude/w/docs/NAME_SYSTEM.txt']
SAMPLES = [('any name prompt', '__name_any_prompt__', 10), ('brand marks', '__bs_marked_prompt__', 10), ('brand style any', '__bs_prompt__', 20), ('keychain', '__acc_keychain_prompt__', 10), ('glove', '__acc_glove_prompt__', 10), ('outerwear', '__clothing_outerwear_prompt__', 10), ('garment', '__clothing_garment_prompt__', 10), ('drink', '__obj_drink_prompt__', 10), ('business card', '__name_business_card_prompt__', 5), ('adult L1', '__adult_l1_full_prompt__', 3), ('pinback', '__pinback_prompt__', 2)]
