VERSION 3 CHANGES
=================
1. EYEWEAR  (_tools/eyewear_build.py)
   Files: acc_glasses -> f_acc_glasses / m_acc_glasses (whole population), age<lo>_<hi>_opt_eyewear (per age bracket, f_ / m_). 5,000 lines each. Blank line = nothing visible.
   Shares BEFORE the x0.5 scale (EYEWEAR_SCALE in eyewear_build.py halves all of them): 18-24 22/6/16 | 25-34 27/6/16 | 35-44 32/6/12 | 45-54 45/6/7 | 55-64 60/6/4 | 65-74 68/6/2 | 75-84 72/5/1 | 85-94 72/4/.5 | 95+ 68/3/.2 ; the rest wear nothing visible.
   (rough estimates - edit SHARE in eyewear_build.py). Monocle 25 lines and eyepatch 25 lines (0.5% each) in every file. The 28 original acc_glasses options are kept (data/acc_glasses_original.txt).
2. AGING / OBESITY  (age_model.py, body_model.py, supplements.py, aging_text.py)
   Brackets: 18-24 25-34 35-44 45-54 55-64 65-74 75-84 85-94 95-120. New body type "vheavy" = severely obese. supplements.py holds the extra options (O2/O3 = old / very old, H2/H3 = obese).
   __aging_summary__ is appended to each identity paragraph and says how old the person LOOKS.
3. OBJECTS  (objects_data.py, objects_build.py, fix_settings.py)
   settings10000.txt was edited once by fix_settings.py: whimsical tail clauses reduced to 12 lines each, rubber-duck races reduced to 2 lines (other river events added).
   New: obj_furniture obj_room_items obj_table_items obj_outdoor_items obj_toys obj_held_items obj_scene_interior obj_scene_exterior; acc_props and env_props regenerated (originals kept once).
   prompt_setting has two new lines (indoors / outdoors) and there are prompt_setting_interior / prompt_setting_exterior.
4. GROUPS  (group_build.py)  start from  grp_prompt_master (all), grp_prompt_master_2, grp_prompt_master_3  or one of  grp_2_mm grp_2_ww grp_2_mw grp_3_mmm grp_3_www grp_3_mmw grp_3_mww.
   Pieces for your own templates: grp_person_f, grp_person_m, grp_interact_2_<positive|mixed|negative>, grp_interact_3_<...>, grp_expression_2_/3_<tone>, grp_relation_<tone>.
5. DEMOGRAPHIC GROUPS  (demo_build.py)  demo_prompt_master (population-weighted), demo_prompt_master_balanced (every combination equally), demo_prompt_master_<identity>,
   demo_<identity>_<orientation> (e.g. demo_trans_woman_homosexual, demo_cis_man_asexual, demo_intersex_person_pansexual), demo_body_<identity> (body wording), demo_ctx_<pronoun>_<partner> (neutral context cues),
   demo_anat_<identity> (clinical anatomy, adults only, referenced by NO default prompt). Orientation is stated in text and hinted only with neutral cues (a ring, a photograph); there are no appearance stereotypes.
   Identities: cis_man cis_woman trans_man trans_woman trans_man_nonop trans_woman_nonop halfway_mtf halfway_ftm halted_mtf halted_ftm androgynous nonbinary intersex_man intersex_woman intersex_person.
   The base character comes from the existing f_/m_ age masters, so a person who is androgynous or midway in transition may carry "she"/"he" wording from that base; the demo_body lines use neutral "This person has ..." there.
6. ACCESSORIES / AIDS / SETTINGS / POSES BY AGE AND BODY TYPE  (access_build.py, clothing_build.py)
   The per-age, per-body-type master prompts (age..._prompt_master_<arch>) now use age..._aids_<arch>, age..._prompt_setting_<arch>, age..._prompt_pose_expression_<arch> and age..._acc_hats/jewelry/props.
7. VIEWER  _tools/prompt_viewer.html  - open in a browser, click "Load wildcards folder", type a start file name (e.g. f_prompt_master_by_age), press Generate. Both panes have the same height and scroll.
8. SKIN-TONE WORDING  (fix_ethnic.py, applied once)  every line of countries_ethnic_prompts now names a specific skin colour (no more "light" / "fair" alone) and the 28 dem_tone options name colour + undertone.
   NOTE: skin_flush / skin_glow / skin_marks / skin_finish / dem_unique can still describe a colour that disagrees with the ethnicity line (e.g. "rosy flush" on very dark skin); a fix is still open.
9. HAIR CODES REMOVED  hair_curl no longer contains the (1A)-(4C) style codes; each option now describes the curl in plain words (e.g. "tight defined spiral curls, bouncy ringlets about the width of a pencil").
   Order/indices are unchanged, so the weights in hair_model.py still line up.
8b. SKIN MODIFIERS NOW COLOUR-NEUTRAL (fix_skin.py, applied once)  skin_flush / skin_glow / skin_marks / skin_finish (and their age versions) no longer name colours; they say "a shade deeper than the base skin tone",
   "darker than the surrounding skin", "has lost some of its natural colour" etc., so they cannot contradict the ethnicity / dem_tone line.
8c. EYEWEAR HALVED  eyewear_build.py EYEWEAR_SCALE = 0.5 halves every glasses / sunglasses / contacts share (more blank lines = nothing worn); contact-lens lines no longer say "no glasses".
8d. CROSS-FILE NEUTRALITY  (neutralize.py)  colour / age / gender wording that contradicted the controlling files was removed or made relative; see docs/CROSS_FILE_AUDIT.txt.
10. SHOES  (shoe_build.py, shoe_data.py, shoe_data2.py, data/shoe_vocab.json)  see docs/SHOES.txt.
Run order (build_all.py): weights, everyday, objects, templates, outfits, age, eyewear, body, access, hair, clothing, then merge, demo_build, group_build, shoe_build and the reference check.
