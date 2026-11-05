import re as _re, glob as _g, os as _os
import v85_build as _B, v83_bs as _S
_G = _B.build(); _nb = len(_S.load())
_cnt = lambda pat: sum(len(v) for k, v in _G.items() if _re.fullmatch(pat, k))
_n6 = _cnt(r'adult_l6_(pose|body|setting|object|group|location)')
_nmod = _cnt(r'adult_l[1-6]_(expression|bodychange)')
_nmw = _cnt(r'adult_l[1-6]_(messy|wrestling)')
_ngear = _cnt(r'adult_gear_.*')
ONELINE = 'adult level 6, expression and body-change modifiers, messy play, wrestling, gear, kilts and tailoring; 20 top brands image-checked'
BULLETS = ["Adult level 6 (`adult_l6_<pose|body|setting|object|group|location>`, %d lines): ejaculate, squirting described plainly, and groups of five or more adults. Levels 1 to 5 stay at four adults or fewer." % _n6,
 "Optional modifiers for every level, L1 to L6: `adult_lN_expression` and `adult_lN_bodychange` (%d lines) - faces, flushing, sweat, trembling, calm or tolerant looks, intensity within consensual play." % _nmod,
 "Messy play and staged play-fighting: `adult_lN_messy` and `adult_lN_wrestling` for L1 to L6 (%d lines), plus per-level prompts." % _nmw,
 "Gear (%d lines): `adult_gear_materials`, `_garments`, `_uniforms`, `_kilts`, `_tailoring`, `_pony`, `_furniture`, `_roleplay`, `_fetish_focus`, all in `adult_gear`." % _ngear,
 "Existing L1-L5 adult lines audited: jargon replaced with plain visual descriptions, ejaculate and large-group lines moved to L6, urine, school, sleeping or drunk partner lines removed.",
 "20 top brand styles rewritten after checking product images (Jeep, Nike, Adidas, Coca-Cola, Apple, Sony, Levi Strauss, Chanel, Burberry, Porsche, Ferrari, Studio Ghibli, Disney classic, Pixar, Patagonia, Barbour, Zippo, Muji, Olivetti, IKEA).",
 "A 40-image prompt showcase at 1024 and 1408 pixel counts, steps 50, cfg 3.75, no trailing blank line, and 100 random sample prompts.",
 "A list of open questions for review: docs/ADULT_QUESTIONS_v85.txt."]
README = """Guyanonymous' Wildcards v85 - adult L6, modifiers, messy, wrestling, gear, kilts and tailoring
Adult L6       adult_l6_<genre>, adult_l6_prompt
Modifiers      adult_lN_expression, adult_lN_bodychange (L1-L6)
Messy/wrestle  adult_lN_messy, adult_lN_wrestling, adult_lN_messy_prompt, adult_lN_wrestling_prompt
Gear           adult_gear_* , adult_gear
Full prompts   adult_lN_full_prompt (scene + expression + body change)
Docs           docs/INDEX_v85.txt, docs/RESEARCH_v85_adult_gear.txt, docs/RESEARCH_v85_brands_top25.txt, docs/ADULT_QUESTIONS_v85.txt
"""
GEN_ROW = '("adult_*","%d","v85 adult L6, modifiers, messy, wrestling, gear and prompts."),' % sum(1 for k in _G if k.startswith('adult_'))
DOCS = ['/home/claude/w/docs/INDEX_v85.txt', '/home/claude/w/docs/RESEARCH_v85_adult_gear.txt', '/home/claude/w/docs/RESEARCH_v85_brands_top25.txt', '/home/claude/w/docs/ADULT_QUESTIONS_v85.txt', '/home/claude/w/docs/BRIEF_v85_adult.txt']
SAMPLES = [('adult L6', '__adult_l6_full_prompt__', 12), ('adult L1', '__adult_l1_full_prompt__', 8), ('adult L2', '__adult_l2_full_prompt__', 8), ('adult L3', '__adult_l3_full_prompt__', 8), ('adult L4', '__adult_l4_full_prompt__', 8), ('adult L5', '__adult_l5_full_prompt__', 8), ('messy', '__adult_l3_messy_prompt__', 8), ('wrestling', '__adult_l2_wrestling_prompt__', 8), ('gear', '__adult_gear__', 12), ('brand style any', '__bs_prompt__', 10), ('brand named', '__bs_prompt_named__', 10)]
