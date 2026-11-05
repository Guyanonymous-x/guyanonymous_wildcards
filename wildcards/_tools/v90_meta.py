import v90_build as _B
ONELINE = 'brand styles now apply to the object only, not the whole scene'
BULLETS = ["Brand style files (`maker_bs_<brand>` and `_named`) now hold only object design language: shape, material, finish, palette, pattern, lettering, emblem. Photography, advertising and setting sentences moved to new `maker_bs_<brand>_mood` files (203 brands).",
 "Every brand style ends with a line saying it applies to the object itself and not to its surroundings.",
 "Brand prompts (`bs_prompt`, `bs_prompt_named` and per-group) now ask for the object to be styled with the setting kept plain and neutral, and subject lists no longer include people, rooms, streets or other scenes.",
 "A 40-image prompt showcase at 1024 and 1408 pixel counts, steps 50, cfg 3.75, no trailing blank line, and 100 random sample prompts."]
README = """Guyanonymous' Wildcards v90 - brand styles scoped to the object
Style      maker_bs_<brand> (object design only), maker_bs_<brand>_named, maker_bs_<brand>_mood (photography and setting)
Prompts    bs_prompt, bs_prompt_named
"""
GEN_ROW = '("maker_bs_*_mood","203","v90 photography and setting sentences split out of brand styles."),'
DOCS = ['/home/claude/w/docs/INDEX_v90.txt', '/home/claude/w/docs/INDEX_v89.txt']
SAMPLES = [('brand style any', '__bs_prompt__', 45), ('brand named', '__bs_prompt_named__', 45), ('adult L1', '__adult_l1_full_prompt__', 5), ('pinback', '__pinback_prompt__', 5)]
