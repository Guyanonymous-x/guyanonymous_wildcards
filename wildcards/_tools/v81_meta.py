ONELINE = 'robots, gadgets and tech devices'
BULLETS = ["Robots (about 316 files, `rb_`). 25 robot types, each with its own body, head, eyes and sensors, arms, hands, movement and feature lists: tin toy robots, humanoids, androids, helper robots, industrial and laboratory arms, four-legged and many-legged walkers, rovers, tracked robots, drones, giant mechs, snake robots, orbs, cleaners, pets, clockwork automatons, combat robots, underwater and space robots, tiny insect robots, exoskeletons, social robots, warehouse robots and alien machines.",
"Shared robot pools. Colour schemes, wear, markings with quoted names and warnings, places, lighting and camera shots, grouped by style (toy, modern, rugged, antique, strange).",
"Gadgets and tech devices (about 485 files, `gd_`). 42 types covering phones from the early 1980s brick to foldables, smartwatches, bands, rings, glasses, headsets, earbuds, headphones, e-book readers, tablets, organisers, handheld consoles, music players, cameras, pagers, radios, calculators, navigation units, speakers, chargers, mainframes, home computers, towers, all-in-ones, laptops, gaming computers, terminals, server racks, keyboards, monitors, printers, routers and mice.",
"Every device is described by its look (shape, size, screen, controls, material, colour, wear); any text on a screen is written out line by line in quotes.",
"Four reference files `maker_robot_real_models`, `maker_robot_fiction_models`, `maker_gadget_models` and `maker_computer_models` hold the real and fictional names with full descriptions, kept out of the prompts.",
"A 40-image prompt showcase for this release, in two sets (1024 and 1408 pixel counts) with varied image ratios, steps 50 and cfg 3.75.",
"100 random sample prompts, one per line with no blank lines."]
README = """Guyanonymous' Wildcards v81 - robots, gadgets and tech devices
==============================================================
Robots         rb_prompt, rb_group_prompt, rb_short; one type at a time with rb_<type>_prompt
Robot types    tin, human, android, butler, arm, lab, dog, spider, rover, tread, drone, mech, snake, orb, cleaner, pet, clock, war, sub, space, micro, exo, face, warehouse, alien
Robot parts    rb_<type>_body, _head, _eyes, _arms, _hands, _move, _feature; shared rb_colour_<style>, rb_wear_<style>, rb_place_<group>, rb_marks, rb_light, rb_shot
Gadgets        gd_prompt, gd_group_prompt, gd_short; one type at a time with gd_<type>_prompt
Gadget types   brick, candybar, clamshell, slider, qwerty, slab, fold, rugged, watch, band, ring, glasses, vr, earbuds, headphones, ereader, tablet, pda, console, music, camera, pager, radio, calculator, gps, speaker, power, mainframe, homecomp, tower, allinone, laptop, luggable, gamingpc, minipc, terminal, rack, keyboard, monitor, printer, router, mouse
Gadget parts   gd_<type>_era, _body, _screen, _controls, _material, _colour, _feature; shared gd_wear, gd_light, gd_shot, gd_place_<group>, gd_text_<kind>
References     maker_robot_real_models, maker_robot_fiction_models, maker_gadget_models, maker_computer_models
Docs           docs/INDEX_v81.txt, docs/RESEARCH_v81.txt, docs/showcase files
All Options Once includes all of these.
"""
GEN_ROW = '("rb_*, gd_*, maker_robot_*, maker_gadget_*, maker_computer_*","805","v81 robots, gadgets and tech devices."),'
DOCS = ['/home/claude/w/docs/INDEX_v81.txt', '/home/claude/w/docs/RESEARCH_v81.txt', '/home/claude/w/docs/robots_real.txt', '/home/claude/w/docs/robots_fiction.txt', '/home/claude/w/docs/gadgets_handheld.txt', '/home/claude/w/docs/gadgets_computers.txt']
SAMPLES = [('robots', '__rb_prompt__', 34), ('gadgets', '__gd_prompt__', 44), ('screens', '__gd_watch_prompt__', 4), ('screens', '__gd_ereader_prompt__', 4), ('group', '__rb_group_prompt__', 7), ('group', '__gd_group_prompt__', 7)]
