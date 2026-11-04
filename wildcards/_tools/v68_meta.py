ONELINE = 'patch release: condition parts that fit every subject, sessile sea animals, world place wording'
BULLETS = ["Condition parts fixed. The part lists for buildings, vehicles, furniture, clothing and statues in the v62 condition system were too specific (a bridge could get a damaged front door, a glove could get damaged sleeves). They now name parts that exist on every subject of that kind, such as entrance, stonework, wheels or running gear, legs or base, main fabric and plinth.",
"Sea animals fixed. Jellyfish, corals, anemones, starfish and urchins now have their own behaviour family (drifting with the current, waving tentacles, clinging to a rock) instead of sharing one with crabs and shellfish, so a jellyfish is never asked to burrow into sand.",
"Object condition prompts fixed. They now use tools only, because machines such as tractors belong to the vehicle kind and were being given handles.",
"World place prompts fixed. `world_<name>_place_prompt` now reads \"Visible nearby are ...\" so the sentence always starts correctly.",
"Also included: the full v57 to v67 gallery of 200 sample prompts, organised in groups, as a separate download."]
README = """Guyanonymous' Wildcards v68 - patch release
===========================================
Fixed  cond_building_*, cond_vehicle_*, cond_furniture_*, cond_clothing_*, cond_statue_* (part lists)
Fixed  ani_sessile_* (new family for jellyfish, corals, anemones, starfish, urchins), ani2_* for those classes
Fixed  world_<name>_place_prompt wording
Fixed  object condition prompts now use hand and power tools only (machines such as tractors are covered by the vehicle kind)
No new entry points. Everything from v67 is unchanged.
"""
GEN_ROW = '("cond_*, ani_sessile_*","patch","v68 fixes to condition parts, sea animal behaviours and world place wording."),'
SAMPLES = [('condition', '__condition_prompt__', 40), ('condition heavy', '__condition_ruined_prompt__', 14), ('sea animal', '__ani2_jellyfish_corals_and_anemones_prompt__', 12), ('starfish', '__ani2_starfish_and_urchins_prompt__', 8), ('world place', '__world_place_prompt__', 16), ('animal scene', '__ani2_prompt__', 10)]
