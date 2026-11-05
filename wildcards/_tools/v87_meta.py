import re as _re
import v87_build as _B
_G = _B.build()
_n = sum(len(v) for k, v in _G.items() if _re.fullmatch(r'adult_l[1-3]_wrestling_mm', k))
ONELINE = 'male wrestling lines, four brand fixes, deduplicated pinbacks and achievement badges, scene-matched showcase lighting, L1-L5 crowd clean-up'
BULLETS = ["Men-only staged play-fighting for levels 1 to 3 (`adult_wrestling_mm`, `adult_lN_wrestling_mm_prompt`, %d lines): pillows, sauna, mud, oil, gym mat and ring." % _n,
 "Off-White, Bosch Professional, Makita and SodaStream brand styles rewritten as product-neutral essence descriptions.",
 "Pinback and adult achievement files deduplicated: no picture or wording repeated across files.",
 "Levels 1 to 5 cleaned of crowd, audience and spectator mentions, so no scene implies five or more adults.",
 "Showcase lighting now matches the scene (indoor, outdoor, or neutral); place-specific lighting lines are left out.",
 "A 40-image prompt showcase at 1024 and 1408 pixel counts, steps 50, cfg 3.75, no trailing blank line, and 100 random sample prompts."]
README = """Guyanonymous' Wildcards v87 - male wrestling, brand fixes, deduplicated badges
Wrestling (men)  adult_l1..3_wrestling_mm, adult_wrestling_mm, adult_lN_wrestling_mm_prompt
"""
GEN_ROW = '("adult_*_wrestling_mm","%d","v87 men-only wrestling L1-L3."),' % _n
DOCS = ['/home/claude/w/docs/INDEX_v87.txt', '/home/claude/w/docs/INDEX_v86.txt']
SAMPLES = [('male wrestling', '__adult_wrestling_mm__', 20), ('adult L1', '__adult_l1_full_prompt__', 10), ('adult L3', '__adult_l3_full_prompt__', 10), ('adult L5', '__adult_l5_full_prompt__', 10), ('pinback', '__pinback_prompt__', 20), ('insignia', '__insignia_all_prompt__', 10), ('brand style any', '__bs_prompt__', 10), ('brand named', '__bs_prompt_named__', 10)]
