import v95_build as _B
ONELINE = 'brand styles now define every word that can appear on the object, so no trigger word or real brand name is printed'
BULLETS = ["Fixed brand-style prompts printing the sharpness trigger word or the real brand name on the object. Image metadata showed the trigger word was sitting in front of the prompt and the model printed it wherever a wordmark, label or tag was described but not defined.",
 "Every brand style ends with a defined text line: any label, tag, badge, packaging or sign is small, and the only words on it are an invented brand name from the new name system, with no other words or letters anywhere.",
 "Brand styles describe the object, not a logo: wordmark, lettering, slogan and text clauses were removed from the style descriptions, and the prompt no longer says 'In the style of <Brand>'. The file name is the brand (maker_bs_heinz), so the prompt holds only the detailed design description. The _named files now hold the same text as the plain ones.",
 "No logo front and centre: every style says the main surfaces carry colour, shape, material and pattern, and any label, tag, badge or sign is small and discreet.",
 "Brand-style files now draw that invented name from name_brand_invented, so each image gets a different fake name. Edit the quoted text in the expanded prompt to use your own.",
 "A 40-image prompt showcase at 1024 and 1408 pixel counts, steps 50, cfg 3.75, no trailing blank line, and 100 random sample prompts."]
README = """Guyanonymous' Wildcards v95 - brand styles with defined text
Prompts  bs_prompt, bs_prompt_named, bs_building_prompt, bs_accessory_prompt, bs_madeup_vehicle_prompt, name_any_prompt
"""
GEN_ROW = '("maker_bs_*","text fix","v95 brand styles define their text."),'
DOCS = ['/home/claude/w/docs/INDEX_v95.txt', '/home/claude/w/docs/NAME_SYSTEM.txt', '/home/claude/w/docs/INDEX_v94.txt']
SAMPLES = [('brand style any', '__bs_prompt__', 45), ('brand named', '__bs_prompt_named__', 35), ('any name prompt', '__name_any_prompt__', 10), ('business card', '__name_business_card_prompt__', 5), ('adult L1', '__adult_l1_full_prompt__', 3), ('pinback', '__pinback_prompt__', 2)]
