# v108 changes (2026-11-05)

Fixes from the hand review of every library file changed on 2026-11-05 (log: LIBRARY_REVIEW_2026-11-05.md), plus the older problems found in that review. All changes are in `_tools/v108_stage.py`; `v108_build.py` applies them on top of v107.

## Adult files
- Level 6 same-sex: every `adult_l6_panel_mm*` (28 lines) and `adult_l6_panel_ww*` (24 lines) now ends with a level-6 ending matched to the pose (semen landing on lips and chin, back, stomach; clear fluid onto the sheet, cushion, chin and chest, stomach). Before, these were identical to level 5.
- Level 1: the "stands bent forward at the hips at a table" pose is removed from `adult_l1_panel_wm`.
- Locations: wet places at level 1 dress him in swim shorts and an open linen shirt and her in a one-piece swimsuit with a sarong; at level 3 swim trunks and bikini bottoms.
- Panels: "in view" sentences removed where the pose hides the body; bulge sentences removed for lying-on-top and lap poses; 69 geometry reworded; the impossible floor position replaced by her astride his lap; camera height fits the furniture.
- Groups: one nude sentence per trio (no "breasts" for three men, no "penises" for three women); duplicate lines removed; cast sentences now read "This scene shows three adults. They are ...".
- Wrestling: "penises and scrotums in view" removed for holds that hide them.
- Fluid: "transparent, not white" becomes "clear and transparent" (`adult_l6_location`, `adult_l6_panel_wm*`, `fluid_scene_squirt`).

## Activities
- `act_*_scene_prompt` (51 files): "__act_X_equip__ can be seen." becomes "The scene includes __act_X_equip__." so no sentence starts in lowercase; "dj" becomes "DJ".
- `act_*_frame_prompt` (51 files): the style slot now uses new `act_frame_style` (six on-location photo styles); the studio-backdrop style no longer appears in a dojo or on a beach.

## Body features
- `f_body_nipples`: each breast described as "<nipple>, set in <areola>".
- `head_chin`: garbled dimple lines and "cleft"/"not a long line" wording fixed.
- New `body_navel` (10 lines).
- Dance, yoga and `f_body_anus` wording fixes.
