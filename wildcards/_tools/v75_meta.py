ONELINE = 'legendary creatures from around the world, archetypal sacred figures, the first 325 converted locations, and 66 object builders'
BULLETS = ["Legendary creatures (about 1,000 files, `leg_`). 121 creatures from folklore on every continent, described by looks only: dragons, griffins, trolls, kitsune, djinn, thunderbirds and many more. Each has a look, habitat, prompt, scene with time and weather, encounter with a small witness, and an art version (painting, relief, tapestry). Regional mix files and a two-beings face-off file.",
"Archetypal sacred and divine figures (18, `leg_sacred_`). Sun-lord, sea-mother, storm-father, trickster, underworld queen and others, with no named deities, shown with poses, offerings and surroundings.",
"Locations (about 3,800 files, `loc_`). The Location Inventory pilot: 325 places (home interiors and exteriors, workplaces, circulation spaces, bathrooms, food and hospitality, unusual places), each with item, furniture, installed feature, signature detail, material, palette, light, human trace and condition pools, a clean scene, a full scene and a scene that adds items from the shared anywhere pools. Tag indexes list scenes by era, light, scale and more.",
"Object builders (about 560 files, `ob_`). 66 everyday objects found in the locations that had no builder: tickets, lockers, napkins, radiators, fridges, jars, trolleys, microphones, projectors and more, each built from type, colour, material, era, wear and detail.",
"A 40-image prompt showcase for this release, in two sets (1024 and 1408 pixel counts) with varied image ratios, steps 50 and cfg 3.75. Every description in it comes from the wildcard files.",
"100 random sample prompts, one per line with no blank lines."]
README = """Guyanonymous' Wildcards v75 - legendary creatures, locations and objects
=======================================================================
Legends        leg_prompt, leg_scene, leg_encounter, leg_art, leg_short, leg_pair_prompt, leg_<region>_*, leg_<key>_*, leg_sacred_prompt, leg_sacred_art
Locations      loc_scene, loc_scene_plus, loc_clean, loc_<category>_scene, loc_<category>_scene_plus, loc_tag_*, loc_<id>_*, loc_anywhere_*
Objects        ob_any_full, ob_any_short, ob_any_phrase, ob_<name>_*
Docs           docs/INDEX_v75.txt, docs/SHOWCASE_v75 files
All Options Once includes all of these.
"""
GEN_ROW = '("leg_*, loc_*, ob_*","5,201","v75 legendary creatures, sacred figures, 325 converted locations and 66 object builders."),'
DOCS = ['/home/claude/w/docs/INDEX_v75.txt']
SAMPLES = [('legend', '__leg_prompt__', 14), ('legend encounter', '__leg_encounter__', 8), ('legend art', '__leg_art__', 6), ('face-off', '__leg_pair_prompt__', 4), ('sacred figure', '__leg_sacred_prompt__', 8), ('location', '__loc_scene_plus__', 30), ('location clean', '__loc_clean__', 8), ('object', '__ob_any_full__', 22)]
