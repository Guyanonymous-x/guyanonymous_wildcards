import v99_build as _B
ONELINE = 'brands of the past: 70 defunct and historic brands (cars, airlines, shops, radios, toys, sweets, cameras, computers) as object styles, with no brand name, logo or text in the prompts'
BULLETS = ["70 new brand styles of defunct or historic brands, from Saab and Pontiac to Pan Am, Braniff, Biba, Dansette, Trabant, Sinclair, Agfa and Woolworths, each written as an object style: colours, forms, materials and patterns only.",
 "The file name carries the brand (for example maker_bs_trabant); the prompt never names it and contains no logo or text.",
 "They join bs_prompt, maker_brand_style and the new bs_past_prompt, with the same plain-surface wording as every other brand style.",
 "A 40-image prompt showcase focused on the new styles at 1024 and 1408 pixel counts, steps 50, cfg 3.75, and 100 random sample prompts."]
README = """Guyanonymous' Wildcards v99 - brands of the past
Prompts  bs_past_prompt styles objects like defunct brands
"""
GEN_ROW = '("brands of the past","70 styles","v99 defunct brands as object styles."),'
DOCS = ['/home/claude/w/docs/INDEX_v99.txt', '/home/claude/w/docs/STANDING_RULES.txt', '/home/claude/w/docs/NAME_SYSTEM.txt']
SAMPLES = [('any name prompt', '__name_any_prompt__', 10), ('brands of the past', '__bs_past_prompt__', 10), ('brand style any', '__bs_prompt__', 20), ('keychain', '__acc_keychain_prompt__', 10), ('glove', '__acc_glove_prompt__', 10), ('outerwear', '__clothing_outerwear_prompt__', 10), ('garment', '__clothing_garment_prompt__', 10), ('drink', '__obj_drink_prompt__', 10), ('business card', '__name_business_card_prompt__', 5), ('adult L1', '__adult_l1_full_prompt__', 3), ('pinback', '__pinback_prompt__', 2)]
