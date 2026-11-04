ONELINE = 'science fiction (styles, aliens, locations, vehicles, robots, suits), e-reader and phone timelines, and eight timekeeping and instrument collections'
BULLETS = ["Science fiction (about 615 files, `sf_`). 15 visual styles (space opera, retro-futurism, biopunk, solarpunk, space western and more), 52 alien species, 48 locations from ring stations to alien jungles, 32 vehicles, 16 robots and 10 spacesuits, each described by looks only.",
"E-reader and phone timelines (about 120 files). 18 e-reader generations from the late 1990s to a 2026 foldable e-ink book, and 31 phone generations from the 1983 brick to rollable and future designs. Real device names are in `maker_ereader_` and `maker_phone_` files only.",
"Timekeeping and instrument collections (about 110 files, `col_`). Watches, clocks, scientific instruments, cameras, typewriters, radios and early electronics, telephones and musical instruments, each with type, material, feature, era, invented maker names in quotation marks, condition and display.",
"A 40-image prompt showcase for this release, in two sets (1024 and 1408 pixel counts) with varied image ratios, steps 50 and cfg 3.75.",
"100 random sample prompts, one per line with no blank lines."]
README = """Guyanonymous' Wildcards v76 - science fiction, device timelines and collections
===============================================================================
Sci-fi         sf_prompt, sf_style_prompt, sf_alien_prompt, sf_alien_pair_prompt, sf_loc_prompt, sf_veh_prompt, sf_robot_prompt, sf_suit_prompt, sf_<kind>_<key>_*
Devices        ereader_prompt, ereader_timeline, phone_prompt, phone_timeline, maker_ereader_prompt, maker_phone_prompt
Collections    col_prompt, col_prompt_fill, col_group_prompt, col_short, col_<name>_prompt (watch, clock, instrument, camera, typewriter, radio, telephone, music)
Docs           docs/INDEX_v76.txt, docs/RESEARCH_v76.txt, docs/showcase files
All Options Once includes all of these.
"""
GEN_ROW = '("sf_*, ereader_*, phone_*, maker_ereader_*, maker_phone_*, col_*","839","v76 science fiction, e-reader and phone timelines, timekeeping and instrument collections."),'
DOCS = ['/home/claude/w/docs/INDEX_v76.txt', '/home/claude/w/docs/RESEARCH_v76.txt']
SAMPLES = [('sci-fi style', '__sf_style_prompt__', 8), ('alien', '__sf_alien_prompt__', 14), ('sci-fi location', '__sf_loc_prompt__', 10), ('vehicle', '__sf_veh_prompt__', 10), ('robot', '__sf_robot_prompt__', 6), ('spacesuit', '__sf_suit_prompt__', 4), ('e-reader', '__ereader_prompt__', 8), ('phone', '__phone_prompt__', 10), ('real device', '__maker_phone_prompt__', 4), ('collection', '__col_prompt__', 20), ('collection group', '__col_group_prompt__', 6)]
