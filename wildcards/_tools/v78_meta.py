ONELINE = 'cyberpunk, steampunk and western genres, steampunk phones, and ten home and decorative collections'
BULLETS = ["Cyberpunk (about 270 files, `cy_`). 8 visual styles, 18 character types, 24 places, 18 objects and 8 vehicles, plus pair and group scenes.",
"Steampunk (about 290 files, `sp_`). 8 visual styles, 18 character types, 24 places, 18 objects and 10 vehicles, plus pair and group scenes.",
"Western (about 300 files, `we_`). 8 visual styles, 18 character types, 24 places, 18 objects and 8 vehicles, plus pair and group scenes. Signs and posters carry their words in quotation marks.",
"Steampunk phones (about 40 files, `spp_`). 12 designs from a crank wall phone and candlestick phone to a pocket handset, a wrist communicator and a steam slate, plus a timeline row.",
"Home and decorative collections (about 70 files, `hd_`). Vases and ceramics, lamps, mirrors, picture frames, glassware, rugs, candlesticks, cushions and textiles, wall art and ornaments, each with type, material, feature, era, invented maker marks in quotation marks, condition and display.",
"A 40-image prompt showcase for this release, in two sets (1024 and 1408 pixel counts) with varied image ratios, steps 50 and cfg 3.75.",
"100 random sample prompts, one per line with no blank lines."]
README = """Guyanonymous' Wildcards v78 - cyberpunk, steampunk, western, steampunk phones and home collections
================================================================================================
Cyberpunk      cy_prompt, cy_style_prompt, cy_class_prompt, cy_loc_prompt, cy_loc_empty, cy_item_prompt, cy_veh_prompt, cy_pair_prompt, cy_group_prompt
Steampunk      sp_prompt (same set of names with the sp_ prefix); spp_prompt, spp_timeline_prompt for steampunk phones
Western        we_prompt (same set of names with the we_ prefix)
Home           hd_prompt, hd_group_prompt, hd_short, hd_<kind>_prompt (vase, lamp, mirror, frame, glass, rug, candle, textile, art, ornament)
Docs           docs/INDEX_v78.txt, docs/RESEARCH_v78.txt, docs/showcase files
All Options Once includes all of these.
"""
GEN_ROW = '("cy_*, sp_*, spp_*, we_*, hd_*","962","v78 cyberpunk, steampunk, western, steampunk phones and home and decorative collections."),'
DOCS = ['/home/claude/w/docs/INDEX_v78.txt', '/home/claude/w/docs/RESEARCH_v78.txt']
SAMPLES = [('cyberpunk', '__cy_prompt__', 12), ('cyberpunk pair', '__cy_pair_prompt__', 3), ('steampunk', '__sp_prompt__', 12), ('steampunk group', '__sp_group_prompt__', 3), ('steampunk phone', '__spp_prompt__', 8), ('western', '__we_prompt__', 12), ('western pair', '__we_pair_prompt__', 3), ('western group', '__we_group_prompt__', 3), ('home collection', '__hd_prompt__', 34), ('home group', '__hd_group_prompt__', 8), ('steampunk timeline', '__spp_timeline_prompt__', 2)]
