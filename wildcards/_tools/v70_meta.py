ONELINE = 'real-world manufacturer styles by decade for cars, trucks, motorcycles, bicycles, boats, aircraft, spacecraft, trains and skates'
BULLETS = ["104 real manufacturers and makers across 10 categories (43 car makers, 15 motorcycle makers, 11 truck, bus and tractor makers, 9 aircraft makers, 8 bicycle makers, 5 skateboard and skate styles, 4 boat builders, 4 rail and bus styles, 3 space programmes, 2 scooter makers), with 213 decade descriptions from the 1930s to the 2020s.",
"This is the one part of the library that uses real brand names on purpose, as you asked. Each style is also described in plain visual terms (grille shape, roofline, lamps, fins, stripes, tank shape and so on), so it works even when a model does not know the name.",
"Per maker: `maker_<maker>_<decade>` (one decade), `maker_<maker>_style` (any decade), `maker_<maker>_genre` (the vehicle genres it makes, taken from the v69 genres and described without a random paint job so the maker's own look decides the colours and details), and the entries `maker_<maker>_prompt`, `maker_<maker>_scene_prompt` (with a pose and camera angle) and `maker_<maker>_person_prompt` (with a person). `maker_<maker>_<decade>_prompt` pins a decade.",
"Mix and entry files. `maker_prompt`, `maker_scene_prompt` and `maker_person_prompt` pick any maker. `maker_<category>_prompt` picks within cars, trucks, motorcycles, scooters, bicycles, boats, aircraft, spacecraft, rail or skates. `maker_decade_<decade>_prompt` and `maker_decade_prompt` pick by decade. `maker_blend_prompt` blends two makers' styles on a random real vehicle, and `maker_style_any` can be dropped into any vehicle prompt.",
"The index `docs/MAKERS_v70.txt` lists every maker, the genres it applies to and the decades covered.",
"100 random sample prompts, one per line with no blank lines."]
README = """Guyanonymous' Wildcards v70 - manufacturer styles
=================================================
Per maker (104)  maker_<maker>_<decade>, maker_<maker>_<decade>_prompt, maker_<maker>_style, maker_<maker>_genre, maker_<maker>_prompt, maker_<maker>_scene_prompt, maker_<maker>_person_prompt
Entries          maker_prompt, maker_scene_prompt, maker_person_prompt, maker_blend_prompt, maker_decade_prompt, maker_decade_<decade>_prompt, maker_<category>_prompt / _scene_prompt / _person_prompt / _names / _style
Mixes            maker_style_any, maker_names, maker_decades
Docs             docs/MAKERS_v70.txt
Real brand names are used only in the maker_* files. All Options Once includes all of these.
"""
GEN_ROW = '("maker_<maker>_*, maker_*","104","v70 real-world manufacturer styles by decade for cars, trucks, motorcycles, bicycles, boats, aircraft, spacecraft, trains and skates."),'
DOCS = ['/home/claude/w/docs/MAKERS_v70.txt']
SAMPLES = [('any maker', '__maker_prompt__', 24), ('car maker', '__maker_car_prompt__', 14), ('truck maker', '__maker_truck_prompt__', 6), ('motorcycle maker', '__maker_motorbike_prompt__', 8), ('scooter maker', '__maker_scooter_prompt__', 3), ('bicycle maker', '__maker_bicycle_prompt__', 6), ('boat maker', '__maker_boat_prompt__', 4), ('aircraft maker', '__maker_air_prompt__', 6), ('space programme', '__maker_space_prompt__', 4), ('rail', '__maker_rail_prompt__', 3), ('skates', '__maker_skate_prompt__', 4), ('with pose', '__maker_scene_prompt__', 8), ('with person', '__maker_person_prompt__', 6), ('blend', '__maker_blend_prompt__', 4)]
