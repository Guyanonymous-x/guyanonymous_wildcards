ONELINE = 'animals 2: behaviours, groups, young, close-up details, farm animals and people with animals'
BULLETS = ["Behaviour by animal type. 19 behaviour families (predators, grazers, primates, small mammals, marine mammals, bats, marsupials, raptors, waterbirds, songbirds, parrots, game birds, snakes, reptiles, amphibians, fish, invertebrates, bugs, prehistoric animals) each have their own behaviour, group, young and close-up detail files, such as `ani_raptor_behaviour`, so a bird is never asked to graze and a fish never walks.",
"Animal scenes. `ani2_<class>_prompt` pairs an animal from the v54 lists with a group, a behaviour and a habitat scene from `ani_<family>_scene`. `ani2_prompt` picks any class.",
"Young animals and close-ups. `ani2_young_prompt` shows cubs, chicks, calves and larvae. `ani2_closeup_prompt` shows the eye, paws, feathers, scales or other detail of a named animal.",
"Farm and domestic animals. 14 farm animals each with a full description (`farm_<animal>`), `farm_activity`, and `farm_prompt` for farm scenes.",
"People with animals. `farm_interaction` has ten ways a person can work or bond with an animal. `farm_person_prompt`, `farm_person_frame_prompt` (framed for a full-body 1:1 shot) and `pet_person_prompt` (dogs and cats) combine a random person with an animal.",
"100 random sample prompts, one per line with no blank lines."]
README = """Guyanonymous' Wildcards v61 - animals 2
=======================================
Behaviour   ani_<family>_behaviour / _group / _young / _detail   (18 families)
Entries     ani2_prompt, ani2_young_prompt, ani2_closeup_prompt, ani2_<class>_prompt
Farm        farm_<animal> (14), farm_animal, farm_activity, farm_interaction, farm_prompt
People      farm_person_prompt, farm_person_frame_prompt, pet_person_prompt
All Options Once includes all of these except the framed person prompt.
"""
GEN_ROW = '("ani_<family>_*, ani2_*, farm_*","19 / 14","v61 animal behaviours, groups, young, close-ups, farm animals and people with animals."),'
SAMPLES = [('animal scene', '__ani2_prompt__', 34), ('young animal', '__ani2_young_prompt__', 14), ('animal close-up', '__ani2_closeup_prompt__', 18), ('farm', '__farm_prompt__', 12), ('person with farm animal', '__farm_person_prompt__', 8), ('person with animal framed 1:1', '__farm_person_frame_prompt__', 8), ('person with pet', '__pet_person_prompt__', 6)]
