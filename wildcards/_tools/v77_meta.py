ONELINE = 'fantasy and horror, people interacting in pairs and groups, toys, dolls, plush, playsets, games, toy packaging and die-cast models'
BULLETS = ["Fantasy (about 500 files, `fa_`). 12 visual styles, 24 folk from elves to beast-kin, 20 character types, 30 places and 20 objects, plus party and duel scenes.",
"Horror (about 400 files, `ho_`). 11 styles from gothic to folk horror, 24 entities, 16 survivor types, 30 places and 20 objects, described by looks and mood only, with no gore.",
"People interacting (about 200 files, `pi_`). 46 adult pair actions (handing over, dancing, swordfights, chases, heists, arguments, embraces and more) and 14 group scenes of 4 to 6 people, with positions given left to right and people drawn from the existing person pools.",
"Toys and models (about 300 files, `toy_`, `dc_`). Action figures, fashion, porcelain and rag dolls, wooden toys, plush animals and creatures, resin statues, 16 playsets, eight kinds of boxed games and small toys, 13 kinds of toy packaging by era and condition, and die-cast models of cars, trucks, aircraft, ships, trains, buildings, figures and miniatures.",
"A 40-image prompt showcase for this release, in two sets (1024 and 1408 pixel counts) with varied image ratios, steps 50 and cfg 3.75.",
"100 random sample prompts, one per line with no blank lines."]
README = """Guyanonymous' Wildcards v77 - fantasy, horror, people interaction, toys and die-cast
====================================================================================
Fantasy        fa_prompt, fa_style_prompt, fa_folk_prompt, fa_class_prompt, fa_loc_prompt, fa_item_prompt, fa_party_prompt, fa_duel_prompt
Horror         ho_prompt, ho_style_prompt, ho_ent_prompt, ho_ent_alone, ho_class_prompt, ho_loc_prompt, ho_item_prompt
People         pi_prompt, pi_pair_prompt, pi_group_prompt, pi_<action>_prompt
Toys           toy_prompt, toy_figure_prompt, toy_lineup_prompt, toy_play_prompt, toy_play_scene, toy_game_prompt, toy_pack_prompt
Die-cast       dc_prompt, dc_boxed, dc_collection_prompt, dc_<kind>_prompt
Docs           docs/INDEX_v77.txt, docs/RESEARCH_v77.txt, docs/showcase files
All Options Once includes all of these except the person-based pi_ files, which need the person generator files.
"""
GEN_ROW = '("fa_*, ho_*, pi_*, toy_*, dc_*","1336","v77 fantasy, horror, people interaction, toys and die-cast models."),'
DOCS = ['/home/claude/w/docs/INDEX_v77.txt', '/home/claude/w/docs/RESEARCH_v77.txt']
SAMPLES = [('fantasy', '__fa_prompt__', 14), ('fantasy party', '__fa_party_prompt__', 3), ('horror', '__ho_prompt__', 14), ('horror alone', '__ho_ent_alone__', 4), ('people pair', '__pi_pair_prompt__', 14), ('people group', '__pi_group_prompt__', 6), ('toy', '__toy_prompt__', 14), ('toy lineup', '__toy_lineup_prompt__', 3), ('play scene', '__toy_play_scene__', 4), ('die-cast', '__dc_prompt__', 8), ('die-cast boxed', '__dc_boxed__', 6), ('die-cast shelf', '__dc_collection_prompt__', 4), ('packaging', '__toy_pack_prompt__', 6)]
