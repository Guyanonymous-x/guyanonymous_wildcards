ONELINE = 'fantasy, sci-fi and history worlds, plus consolidation (full index, model guide, small fixes to v63 and v64)'
BULLETS = ["31 worlds in three groups. 16 historical settings (ancient Egypt, Greece, Rome, early medieval northern Europe, medieval Europe, Heian Japan, Tang China, Mughal India, pre-1500s Mesoamerica, Renaissance, age of sail, Victorian Britain, the American frontier, the 1920s, 1950s and 1970s), 8 fantasy settings (kingdom, woodland realm, mountain halls, gothic realm, pirate sea, desert kingdom, fairy tale cottage, wizard's tower) and 7 science fiction settings (starship crew, space station, alien world, neon megacity, ruined wasteland, retro-futurist city, robot workshop).",
"Each world has dress, props, setting and action files, such as `world_renaissance_props`, with every garment and object described in plain words. All are original archetypes with no named characters, franchises or brands.",
"Entries. `world_<name>_prompt` puts a random person in a world. `world_prompt` picks any, and `world_history_prompt`, `world_fantasy_prompt` and `world_scifi_prompt` pick within a group. `world_place_prompt` shows a place with no person, and `world_frame_prompt` adds the v57 framing for a 1:1 image.",
"Consolidation. A full index (`docs/INDEX_v66.txt`) lists every family and every version's entry points, and a model guide (`docs/MODEL_GUIDE_v66.txt`) says which file to start from for each kind of image.",
"Fixes. Region names in v63 now read correctly in the middle of a sentence (\"of the Arctic\"), and v64 activity prompts say \"Equipment nearby includes\" so fixtures like a barre no longer read as something carried.",
"100 random sample prompts, one per line with no blank lines."]
README = """Guyanonymous' Wildcards v66 - fantasy, sci-fi and history, and consolidation
============================================================================
Per world (31)  world_<name>_dress / _props / _setting / _action / _prompt / _place_prompt / _frame_prompt
Entries         world_prompt, world_history_prompt, world_fantasy_prompt, world_scifi_prompt, world_place_prompt, world_frame_prompt, world_names
Docs            docs/INDEX_v66.txt (full index), docs/MODEL_GUIDE_v66.txt (where to start)
All Options Once includes all of these except the framed prompts.
"""
GEN_ROW = '("world_<name>_*, world_*","31","v66 history, fantasy and science fiction worlds with dress, props, settings and actions."),'
DOCS = ['/home/claude/w/docs/INDEX_v66.txt', '/home/claude/w/docs/MODEL_GUIDE_v66.txt']
SAMPLES = [('history', '__world_history_prompt__', 24), ('fantasy', '__world_fantasy_prompt__', 18), ('science fiction', '__world_scifi_prompt__', 16), ('framed 1:1', '__world_frame_prompt__', 24), ('place', '__world_place_prompt__', 18)]
