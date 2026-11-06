import v106_build as _B
ONELINE = "clothed bulges by fabric class, structured three-person and location scenes, wrestling at levels 4 to 6, solo scenes in real bottoms, a shallow chin dimple instead of a deep cleft"
BULLETS = [
 "Clothed men: `male_bulge_tight`, `_brief`, `_jock`, `_medium`, `_loose`, `_clothed` and `_covered`, written from image tests. Tight stretch fabric holds the penis flat against the belly; briefs outline it; a jockstrap has a modest close pouch; medium fabric softens the outline; loose fabric only tents over an erect penis. Length is given against the body.",
 "Level panels `adult_lN_panel_wm/_ww/_mm` rewritten with full geometry: who faces whom, torsos turned toward each other, three-quarter camera, hands placed, and both people stated as men or women where needed.",
 "Group scenes: structured three-person scenes at levels 1 to 6 (`adult_lN_group`), with explicit acts at levels 5 and 6.",
 "Wrestling: new `adult_l4_wrestling_mm`, `adult_l5_wrestling_mm`, `adult_l6_wrestling_mm`.",
 "Location scenes: ten venues for a woman and a man at every level (`adult_lN_location`), each stating position, hands, place, light and camera.",
 "Solo scenes at level 3 use topless or shirtless in real bottoms; hand-on-stomach lines for women at levels 1 and 2 changed to hand on hip or inner thigh.",
 "Chin: `head_chin` no longer has a deep cleft, which rendered as a split chin. A cleft is now a small shallow dimple low on the chin tip, with the outline unbroken.",
 "Showcase files (40 prompts at 1024 and 1408 pixel counts, steps 50, cfg 3.75) highlight what is new or changed in this version: level panels with the clothed bulge classes, structured group, wrestling, location and solo scenes. The 100 sample prompts are representative of everything the model can do.",
 "Body-feature showcase (kept outside the package): grids of 2x2 or 2x3 panels with one person per feature, close-ups of just the part and one title per image such as Eye Variations with Guyanonymous' Wildcards in smaller text beneath it. Generators V106_showcase_generator.py and convert_list.py are in the tools folder."]
README = """Guyanonymous' Wildcards v106 - bulge classes, structured scenes, wrestling, chin fix
Prompts  male_bulge_*, adult_lN_panel_*, adult_lN_group, adult_l4/5/6_wrestling_mm, adult_lN_location
"""
GEN_ROW = '("adult scenes v106","panels","v106 bulge classes, structured group and location scenes, wrestling."),'
DOCS = ['/home/claude/w/docs/INDEX_v106.txt', '/home/claude/w/docs/STANDING_RULES.txt', '/home/claude/w/docs/NAME_SYSTEM.txt']
SAMPLES = [('kink panel', '__kink_panel_wm__', 2), ('adult L5 act', '__adult_l5_panel_ww_scissor__', 1), ('grooming object', '__groom_prompt__', 4), ('masturbation scene', '__adult_l4_masturbation_f__', 2), ('penis semi-erect', '__m_body_genitals_semi_v2__', 2), ('penis after climax', '__m_body_genitals_post_v2__', 2), ('any name prompt', '__name_any_prompt__', 10), ('brand marks', '__bs_marked_prompt__', 10), ('adult pose scene', '__adult_l1_pose_scene__', 3), ('penis modifier', '__m_body_genitals_mod__', 3), ('brand style any', '__bs_prompt__', 20), ('keychain', '__acc_keychain_prompt__', 10), ('glove', '__acc_glove_prompt__', 10), ('outerwear', '__clothing_outerwear_prompt__', 10), ('garment', '__clothing_garment_prompt__', 10), ('drink', '__obj_drink_prompt__', 10), ('business card', '__name_business_card_prompt__', 5), ('adult L1', '__adult_l1_full_prompt__', 3), ('pinback', '__pinback_prompt__', 2)]
