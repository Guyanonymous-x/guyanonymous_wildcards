import v108_build as _B
ONELINE = "review fixes across the adult, body-feature and activity files, level-6 endings for same-sex panels, place-friendly activity photo styles, and a new navel file"
BULLETS = [
 "Level 6 same-sex panels: every `adult_l6_panel_mm*` and `adult_l6_panel_ww*` line now has a level-6 ending (semen for men, clear fluid for women) that fits the pose, so level 6 differs from level 5.",
 "Level 1: the bent-forward-at-a-table pose is removed from `adult_l1_panel_wm` (it stays at level 2 and above).",
 "Locations: level 1 and level 3 scenes at wet places (shower, steam room, sauna, plunge pool, hot tub, lake dock) now dress people in swimwear.",
 "Panels and groups: hidden-body wording removed where the pose covers it, 69 geometry tidied, impossible floor position replaced, three-person nude sentences matched to who is in the scene, and duplicate group lines removed.",
 "Fluid wording: 'not white' negations replaced with 'clear and transparent' in `adult_l6_location`, `adult_l6_panel_wm` and `fluid_scene_squirt`.",
 "Activities: all 51 `act_*_scene_prompt` files start each sentence with a capital ('The scene includes ...'); `act_*_frame_prompt` uses the new `act_frame_style` (six on-location photo styles) so a studio backdrop no longer clashes with the place.",
 "Body features: `f_body_nipples` reworded per breast, `head_chin` garbled and 'cleft' lines fixed, new `body_navel` (10 navel shapes).",
 "Showcase files (40 prompts at 1024 and 1408 pixel counts, steps 50, cfg 3.75) and 100 sample prompts are included.",
]
README = """Guyanonymous' Wildcards v108 - review fixes, level-6 same-sex endings, place-friendly activity styles, navel file
Prompts  adult_l6_panel_mm, adult_l6_panel_ww, act_*_frame_prompt, act_*_scene_prompt; features body_navel, act_frame_style
"""
GEN_ROW = '("review fixes v108","features","v108 review fixes, level-6 same-sex endings, activity photo styles, navel file."),'
DOCS = ['/home/claude/w/docs/INDEX_v108.txt', '/home/claude/w/docs/STANDING_RULES.txt', '/home/claude/w/docs/NAME_SYSTEM.txt']
SAMPLES = [('adult L6 mm', '__adult_l6_panel_mm__', 2), ('adult L6 ww', '__adult_l6_panel_ww__', 2), ('activity frame', '__act_archery_frame_prompt__', 2), ('activity scene', '__act_beekeeping_scene_prompt__', 2), ('kink panel', '__kink_panel_wm__', 2), ('grooming object', '__groom_prompt__', 4), ('masturbation scene', '__adult_l4_masturbation_f__', 2), ('any name prompt', '__name_any_prompt__', 10), ('brand marks', '__bs_marked_prompt__', 10), ('adult pose scene', '__adult_l1_pose_scene__', 3), ('brand style any', '__bs_prompt__', 10), ('keychain', '__acc_keychain_prompt__', 8), ('glove', '__acc_glove_prompt__', 8), ('outerwear', '__clothing_outerwear_prompt__', 8), ('garment', '__clothing_garment_prompt__', 8), ('drink', '__obj_drink_prompt__', 8), ('business card', '__name_business_card_prompt__', 5), ('adult L1', '__adult_l1_full_prompt__', 3), ('pinback', '__pinback_prompt__', 3)]
