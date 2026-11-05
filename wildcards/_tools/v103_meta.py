import v103_build as _B
ONELINE = 'adult poses with people, places and light; age ladders and cleaner age pools'
BULLETS = ["Adult poses now come with people: `__adult_l1_pose_person__` ... `__adult_l6_pose_person__` give every pose line a distinct adult (age 20s-70s, heritage, skin, build, hair, facial hair) from `__apose_person_f__` and `__apose_person_m__` (1,600 each).",
 "`__adult_l1_pose_scene__` ... `__adult_l6_pose_scene__` add a place, a light and a framing clause (`__apose_place__`, `__apose_light__`, `__apose_frame__`), so the grids no longer look like one warm lamp-lit room.",
 "Vague device phrases ('a small remote', 'a buzzing tube', 'a ring that buzzes') were rewritten as concrete shapes and colours so the model draws them as intended.",
 "Age pools cleaned: young skin, glow, hair colour and strenuous poses removed from the 65+ brackets, aged skin removed from the youngest brackets.",
 "Age ladders: `__age_step1_body_skin__` ... `__age_step9_body_skin__` and `__age_step1_hand_skin__` ... `__age_step9_hand_skin__` give an evenly graded body and hand ageing for age grids.",
 "Hand pools no longer bake in 'swollen', 'knobby' or 'arthritic' (the model drew these as round balls). Joint conditions are now an optional modifier: `__hand_condition_mild__`, `__hand_condition_marked__` or `__hand_condition__`, described by concrete shapes, to add to any hand prompt.",
 "Pubic hair: new `__pubic_hair_stubble__` and `__pubic_hair_patchy__` pools, and a separate `__pubic_hair_shape__` modifier for hair shaved or trimmed into shapes (heart, arrow, line, triangle, diamond, star, lightning bolt and more). `__f_pubichair_all__` and `__m_pubichair_all__` combine them with the existing pools.",
 "A 40-image prompt showcase at 1024 and 1408 pixel counts, steps 50, cfg 3.75, and 100 sample prompts."]
README = """Guyanonymous' Wildcards v103 - adult pose people and scenes
Prompts  bs_marked_prompt adds a random small mark
"""
GEN_ROW = '("adult pose scenes","people, places and light","v103 adult pose people, scenes and age ladders."),'
DOCS = ['/home/claude/w/docs/INDEX_v103.txt', '/home/claude/w/docs/STANDING_RULES.txt', '/home/claude/w/docs/NAME_SYSTEM.txt']
SAMPLES = [('any name prompt', '__name_any_prompt__', 10), ('brand marks', '__bs_marked_prompt__', 10), ('adult pose scene', '__adult_l1_pose_scene__', 3), ('brand style any', '__bs_prompt__', 20), ('keychain', '__acc_keychain_prompt__', 10), ('glove', '__acc_glove_prompt__', 10), ('outerwear', '__clothing_outerwear_prompt__', 10), ('garment', '__clothing_garment_prompt__', 10), ('drink', '__obj_drink_prompt__', 10), ('business card', '__name_business_card_prompt__', 5), ('adult L1', '__adult_l1_full_prompt__', 3), ('pinback', '__pinback_prompt__', 2)]
