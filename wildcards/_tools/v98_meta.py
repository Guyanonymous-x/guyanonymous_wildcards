import v98_build as _B
ONELINE = 'brand styles that no longer name their brand, plus quoted badge and medal text: every bs_cell file is now unnamed, the text-word filter also covers badge, tag, label, sign and banner words, and about 6,000 unquoted "the words X" phrases in badge, medal and pin files are now in quotes'
BULLETS = ["The 746 bs_cell_*_named files no longer say 'in the style of <Brand>'; they carry the same design-language text as the plain cell files (the file name carries the brand).",
 "Brand style descriptions drop clauses mentioning badges, tags, labels, signs, banners, emblems, crests, stamps and similar, so no undefined text or marks appear.",
 "About 6,000 unquoted phrases such as the words Steamy Car Windows in badge, medal, pin and insignia files are now quoted.",
 "A 40-image prompt showcase at 1024 and 1408 pixel counts, steps 50, cfg 3.75, no trailing blank line, and 100 random sample prompts."]
README = """Guyanonymous' Wildcards v98 - unnamed brand cells, quoted badge text
Prompts  brand-style prompts never name a brand; badge and medal text is quoted
"""
GEN_ROW = '("brand cells","746 files","v98 unnamed, badge text quoted."),'
DOCS = ['/home/claude/w/docs/INDEX_v98.txt', '/home/claude/w/docs/STANDING_RULES.txt', '/home/claude/w/docs/NAME_SYSTEM.txt']
SAMPLES = [('any name prompt', '__name_any_prompt__', 20), ('brand style any', '__bs_prompt__', 20), ('keychain', '__acc_keychain_prompt__', 10), ('glove', '__acc_glove_prompt__', 10), ('outerwear', '__clothing_outerwear_prompt__', 10), ('garment', '__clothing_garment_prompt__', 10), ('drink', '__obj_drink_prompt__', 10), ('business card', '__name_business_card_prompt__', 5), ('adult L1', '__adult_l1_full_prompt__', 3), ('pinback', '__pinback_prompt__', 2)]
