import v96_build as _B
ONELINE = 'prompts name what is on a surface instead of denying text: no more "no other words or letters", plain unmarked surfaces, quoted text only where meant'
BULLETS = ["Removed every 'no other words or letters', 'nothing else' and 'no readable text' style negation from the brand styles and the name system (about 5,900 lines). The model notes say negations did not help and that naming words, letters and labels invites lettering; the technical report says training captions quote visible text verbatim, so the prompts now quote the text that should appear and say nothing about text that should not.",
 "Brand styles end with a positive line: the surfaces are plain and unmarked, and the style is carried by colour, shape, material and pattern alone. No label, tag or badge is mentioned, so there is nothing to fill with invented words.",
 "Name-system prompts keep their quoted text, one line each, and no closing denial. The blank-text prompt is now plain unmarked surfaces decorated with shapes and patterns.",
 "A 40-image prompt showcase at 1024 and 1408 pixel counts, steps 50, cfg 3.75, no trailing blank line, and 100 random sample prompts."]
README = """Guyanonymous' Wildcards v96 - positive text wording
Prompts  bs_prompt, name_any_prompt, name_business_card_prompt, name_logo_prompt, name_cap_prompt, name_tshirt_prompt
"""
GEN_ROW = '("maker_bs_*","text wording","v96 positive wording, no text denials."),'
DOCS = ['/home/claude/w/docs/INDEX_v96.txt', '/home/claude/w/docs/NAME_SYSTEM.txt', '/home/claude/w/docs/INDEX_v95.txt']
SAMPLES = [('brand style any', '__bs_prompt__', 45), ('brand named', '__bs_prompt_named__', 25), ('any name prompt', '__name_any_prompt__', 15), ('business card', '__name_business_card_prompt__', 5), ('cap', '__name_cap_prompt__', 4), ('t-shirt', '__name_tshirt_prompt__', 4), ('adult L1', '__adult_l1_full_prompt__', 1), ('pinback', '__pinback_prompt__', 1)]
