import v102_build as _B
ONELINE = 'comma-joined brand styles and randomised quiet motifs'
BULLETS = ["Object-first brand-style prompts now use commas instead of periods inside the style text, so the style reads as one unified description (your A/B tests favoured commas).",
 "Brand logos, nameplates, hallmarks and monograms inside style texts are replaced by a random quiet motif (__bs_motif__): a random simple shape in a random kind of mark (stamped, embossed, engraved, etched, printed, woven, stitched, enamelled and more).",
 "__bs_mark__ now pairs a mark kind with its material (stamped leather, enamelled metal, woven cloth ...) and can show short capital-letter initials.",
 "The 'plain and unmarked' wording was removed from style texts (text rule: do not mention what should not appear).",
 "A 40-image prompt showcase at 1024 and 1408 pixel counts, steps 50, cfg 3.75, and 100 sample prompts."]
README = """Guyanonymous' Wildcards v102 - brand marks
Prompts  bs_marked_prompt adds a random small mark
"""
GEN_ROW = '("brand marks","random marks and motifs","v102 comma-joined styles, randomised motifs."),'
DOCS = ['/home/claude/w/docs/INDEX_v102.txt', '/home/claude/w/docs/STANDING_RULES.txt', '/home/claude/w/docs/NAME_SYSTEM.txt']
SAMPLES = [('any name prompt', '__name_any_prompt__', 10), ('brand marks', '__bs_marked_prompt__', 10), ('brand style any', '__bs_prompt__', 20), ('keychain', '__acc_keychain_prompt__', 10), ('glove', '__acc_glove_prompt__', 10), ('outerwear', '__clothing_outerwear_prompt__', 10), ('garment', '__clothing_garment_prompt__', 10), ('drink', '__obj_drink_prompt__', 10), ('business card', '__name_business_card_prompt__', 5), ('adult L1', '__adult_l1_full_prompt__', 3), ('pinback', '__pinback_prompt__', 2)]
