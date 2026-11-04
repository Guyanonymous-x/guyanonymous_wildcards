ONELINE = 'nature and landscapes: 28 landscape types in parts, flora by biome, rock formations, water features, sky'
BULLETS = ["Landscapes in parts. 28 landscape types (mountain range, alpine lake, desert dunes, rocky desert, rocky and tropical coast, temperate forest, rainforest, savanna, steppe, tundra, glacier, volcano, canyon, waterfall, river valley and delta, wetland, farmland, rolling hills, moorland, fjord, island archipelago, salt flat, geyser field, cave, bamboo grove, vineyard valley, dune coast). Each has its own feature, vegetation, water, foreground and scale files, such as `land_tundra_feature`, assembled by `land_<type>_prompt`.",
"Shared parts. `land_season`, `land_time`, `land_sky`, `land_clouds` and `land_night_sky` work with any landscape. Seasons, times and skies are chosen to suit the scene, and a cave is lit by a lamp instead of the sky.",
"Flora by biome. Eight biomes (alpine, desert, tropical, temperate, grassland, wetland, coastal, arctic) each have about eight fully described plants and trees, in `flora_<biome>`, with `flora_prompt` choosing a group of plants in a season.",
"Rock formations and water features. `land_rock_formation` (arches, columns, hoodoos, mesas, slot canyons and more) and `land_water_feature` (waterfalls, rapids, hot springs, tarns and more) can be added to any scene. `land_close_prompt` and `land_night_prompt` use them on their own.",
"Entries. `land_prompt` picks any landscape, `land_<type>_prompt` makes one type, and `land_frame_prompt` frames a landscape for a 1:1 image with the v57 framing files.",
"100 random sample prompts, one per line with no blank lines, show every landscape type, flora, rock formations, water features and night skies."]
README = """Guyanonymous' Wildcards v60 - nature and landscapes
===================================================
Landscapes  land_<type>_feature / _vegetation / _water / _foreground / _scale / _prompt   (28 types)
Shared      land_season, land_time, land_sky, land_clouds, land_night_sky, land_rock_formation, land_water_feature
Flora       flora_<biome> (8 biomes), flora_prompt, flora_biomes
Entries     land_prompt, land_names, land_close_prompt, land_night_prompt, land_frame_prompt
All Options Once includes all of these.
"""
GEN_ROW = '("land_<type>_*, flora_<biome>, land_prompt","28 / 8","v60 nature and landscapes in parts, with flora by biome, rock formations, water features and skies."),'
SAMPLES = [('landscape', '__land_prompt__', 44), ('landscape framed 1:1', '__land_frame_prompt__', 10), ('flora', '__flora_prompt__', 14), ('rock formation or water', '__land_close_prompt__', 12), ('night sky', '__land_night_prompt__', 6), ('clouds', 'A wide view of __land_clouds__ over __land_prompt__', 6), ('plants', '__plant_prompt__', 8)]
