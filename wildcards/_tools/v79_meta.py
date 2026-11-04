ONELINE = 'noir, pirate and spy genres, money and metalware collections, and fuller descriptions for named e-reader and phone models'
BULLETS = ["Film noir (about 250 files, `nr_`). 8 visual styles, 16 character types, 22 places, 17 objects and 8 vehicles, plus pair and group scenes. Signs and papers carry their words in quotation marks.",
"Pirates (about 260 files, `pt_`). 8 visual styles, 16 character types, 20 places, 18 objects and 8 ships and boats, plus pair and group scenes.",
"Spy thriller (about 270 files, `sy_`). 8 visual styles, 16 character types, 22 places, 17 objects and 8 vehicles, plus pair and group scenes. Text on screens and boards is spelled out, one quoted line at a time (`sy_screen_text`).",
"Money (about 40 files, `mo_`). Coins, banknotes, purses and wallets, money boxes, cheques and bonds, gaming chips and tokens, account books, counting equipment and bullion, each with type, material, feature, era, invented maker marks, condition and display.",
"Metalware (about 40 files, `mt_`). Brass, copper, pewter, silver, cast iron, tin, locks and keys, hand tools and bronze, with the same pieces of detail and a finish pool.",
"Fixes: the 14 named e-reader models and 13 named phone models now have full physical descriptions instead of a few words, and every screen pool (`ereader_screen`, `phone_screen`, `phone_screen_old`, `phone_screen_future`, and the cyberpunk `cy_screen_text`) gives each line of text in quotation marks.",
"A 40-image prompt showcase for this release, in two sets (1024 and 1408 pixel counts) with varied image ratios, steps 50 and cfg 3.75.",
"100 random sample prompts, one per line with no blank lines."]
README = """Guyanonymous' Wildcards v79 - noir, pirates, spies, money and metalware
=====================================================================
Film noir      nr_prompt, nr_style_prompt, nr_class_prompt, nr_loc_prompt, nr_loc_empty, nr_item_prompt, nr_veh_prompt, nr_pair_prompt, nr_group_prompt
Pirates        pt_prompt (same set of names with the pt_ prefix)
Spy thriller   sy_prompt (same set of names with the sy_ prefix)
Money          mo_prompt, mo_group_prompt, mo_short, mo_<kind>_prompt (coin, note, purse, box, cheque, chip, ledger, till, bar)
Metalware      mt_prompt, mt_group_prompt, mt_short, mt_<kind>_prompt (brass, copper, pewter, silver, iron, tin, lock, tool, bronze)
Fixes          maker_ereader_models, maker_phone_models, ereader_screen, phone_screen*, cy_screen_text
Docs           docs/INDEX_v79.txt, docs/RESEARCH_v79.txt, docs/showcase files
All Options Once includes all of these.
"""
GEN_ROW = '("nr_*, pt_*, sy_*, mo_*, mt_*","925","v79 noir, pirate and spy genres, money and metalware collections."),'
DOCS = ['/home/claude/w/docs/INDEX_v79.txt', '/home/claude/w/docs/RESEARCH_v79.txt']
SAMPLES = [('noir', '__nr_prompt__', 12), ('noir pair', '__nr_pair_prompt__', 3), ('pirate', '__pt_prompt__', 12), ('pirate group', '__pt_group_prompt__', 3), ('spy', '__sy_prompt__', 12), ('spy pair', '__sy_pair_prompt__', 3), ('spy group', '__sy_group_prompt__', 3), ('money', '__mo_prompt__', 20), ('money group', '__mo_group_prompt__', 4), ('metalware', '__mt_prompt__', 20), ('metal group', '__mt_group_prompt__', 4), ('e-reader model', '__maker_ereader_prompt__', 2), ('phone model', '__maker_phone_prompt__', 2)]
