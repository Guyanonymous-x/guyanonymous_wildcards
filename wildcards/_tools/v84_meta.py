import v84_build as _B, v83_bs as _S
_G = _B.build(); _nb = len(_S.load())

import re as _re
_nlines = sum(len(v) for k, v in _G.items() if _re.fullmatch(r'adult_l[1-5]_(pose|body|setting|object|group|location)', k))
_moved = sum(1 for k in _G if k.startswith('adult_acc_') or k.startswith('adult_chastity_'))
ONELINE = 'adult update: five explicitness levels across six genres, sex/BDSM/fetish files under adult_, brand styles rewritten as design essence'
BULLETS = ["Adult content (adults only, consensual): `adult_l1` to `adult_l5` x pose, body, setting, object, group, location (%d lines in 30 files). L1 suggestive, L2 sensual, L3 partial nudity, L4 explicit nudity, L5 explicit acts in clinical wording." % _nlines,
 "Mixed sets `adult_<genre>` (all five levels), and prompts `adult_l1_prompt` to `adult_l5_prompt`, `adult_solo_prompt`, `adult_group_prompt`, `adult_prompt`.",
 "Objects split by visibility, for example worn under clothing with the shape visible through fabric versus uncovered.",
 "%d existing sex, BDSM and fetish object files moved under the `adult_` prefix (normal clothing and underwear stay put)." % _moved,
 "Brand styles (%d) rewritten as transferable design essence: mood, shape language, materials, colour and lettering, applicable to any subject (no exact products or parts)." % _nb,
 "Brand naming: `maker_bs_<brand>` is the style only, with the brand name left out (use it in a prompt like 'A __maker_bs_jeep__ typewriter' or after the subject). `maker_bs_<brand>_named` starts 'In the style of <Brand>,'. The same pairing exists for `maker_brand_style*` (all, group, region, era, industry), `bs_cell_<brand>[_named]` and `bs_prompt[_named]`.",
 "A 40-image prompt showcase (8 per level) at 1024 and 1408 pixel counts, steps 50, cfg 3.75, plus a list of open questions for review.",
 "100 random sample prompts, one per line with no blank lines."]
README = """Guyanonymous' Wildcards v84 - adult levels, adult_ prefix, brand style essence
Adult (adults only)  adult_l1..l5_<pose|body|setting|object|group|location>, adult_<genre>, adult_lN_prompt, adult_prompt
Moved                adult_acc_*, adult_chastity_*
Brand styles         maker_bs_<brand> = style only (no name), maker_bs_<brand>_named = with name; maker_brand_style*, bs_cell_*, bs_prompt have _named twins
Docs                 docs/INDEX_v84.txt, docs/RESEARCH_v84.txt, docs/ADULT_QUESTIONS_v84.txt
"""
GEN_ROW = '("adult_*","%d","v84 adult levels, prompts and moved adult objects."),' % sum(1 for k in _G if k.startswith('adult_'))
DOCS = ['/home/claude/w/docs/INDEX_v84.txt', '/home/claude/w/docs/RESEARCH_v84.txt', '/home/claude/w/docs/ADULT_QUESTIONS_v84.txt']
SAMPLES = [('adult any', '__adult_prompt__', 40), ('adult L1', '__adult_l1_prompt__', 10), ('adult L2', '__adult_l2_prompt__', 10), ('adult L3', '__adult_l3_prompt__', 10), ('adult L4', '__adult_l4_prompt__', 10), ('adult L5', '__adult_l5_prompt__', 10), ('brand style any', '__bs_prompt__', 6), ('brand style named', '__bs_prompt_named__', 4)]
