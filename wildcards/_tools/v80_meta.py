ONELINE = 'treasure, card, mineral, sound, screen, art and nature collections'
BULLETS = ["Treasure (about 80 files, `tr_`). Crowns and tiaras, jewellery, goblets and vessels, idols and statuettes, chests and hoards, relics, gemstones, and treasure maps, each fully described.",
"Cards (about 80 files, `cd_`). Playing cards, tarot cards, trading cards, postcards, business cards and labels, board game cards, flash cards and collector packs. Printed captions appear in quotation marks.",
"Minerals and finds (about 80 files, `mn_`). Crystal clusters, polished stones, geodes, ores, fossils, meteorites, cut gemstones and amber, with where each was found and a collector label in quotes.",
"Sound equipment (about 80 files, `sd_`). Record players, radios, tape players, speakers, microphones, headphones, mixing desks and jukeboxes.",
"Screens (about 85 files, `sc_`). Televisions, monitors, laptops, handheld games, arcade cabinets, digital signs, instrument screens and projectors. Each screen has its exact text, one quoted line at a time.",
"Art (about 80 files, `ar_`) and nature finds (about 80 files, `nt_`). Brushes, paints, easels, palettes, sketchbooks, sculpting and printing tools, framed art; shells, feathers, leaves, nests, cones, driftwood, pinned insects and plants.",
"A 40-image prompt showcase for this release, in two sets (1024 and 1408 pixel counts) with varied image ratios, steps 50 and cfg 3.75.",
"100 random sample prompts, one per line with no blank lines."]
README = """Guyanonymous' Wildcards v80 - treasure, cards, minerals, sound, screens, art and nature
======================================================================================
Collections    tr_prompt, cd_prompt, mn_prompt, sd_prompt, sc_prompt, ar_prompt, nt_prompt
Group scenes   <pre>_group_prompt (three pieces together), <pre>_short (one short description)
Kinds          tr_<kind>_prompt (crown, jewel, cup, idol, chest, relic, gem, map), cd_ (deck, tarot, trading, post, index, game, flash, booster), mn_ (cluster, polished, geode, ore, fossil, meteor, gemcut, amber), sd_ (record, radio, tape, speaker, mic, phones, mixer, jukebox), sc_ (tv, monitor, laptop, game, arcade, sign, scope, projector), ar_ (brush, paint, easel, palette, sketch, sculpt, frame, printing), nt_ (shell, feather, leaf, nest, cone, driftwood, insect, plant)
Docs           docs/INDEX_v80.txt, docs/RESEARCH_v80.txt, docs/showcase files
All Options Once includes all of these.
"""
GEN_ROW = '("tr_*, cd_*, mn_*, sd_*, sc_*, ar_*, nt_*","555","v80 treasure, card, mineral, sound, screen, art and nature collections."),'
DOCS = ['/home/claude/w/docs/INDEX_v80.txt', '/home/claude/w/docs/RESEARCH_v80.txt']
SAMPLES = [('treasure', '__tr_prompt__', 14), ('cards', '__cd_prompt__', 14), ('minerals', '__mn_prompt__', 14), ('sound', '__sd_prompt__', 14), ('screens', '__sc_prompt__', 16), ('art', '__ar_prompt__', 8), ('nature', '__nt_prompt__', 8), ('group', '__sc_group_prompt__', 4), ('group', '__mn_group_prompt__', 4), ('group', '__tr_group_prompt__', 4)]
