# Library review of every file changed v105 -> v107 (105 files)

Status per batch; FIX = to apply; OK = read and fine; PRE = pre-existing issue, not caused today.

## Batch 1 - act_yoga/dance/martial (12 files, v107)
- OK: all 12 read in full; no duplicates; no skin colour; tenses agree with "The person is ...".
- FIX act_dance_classes_action: "mid-spin with a skirt flared out" -> "mid-spin with the hair flying out" (most outfits have no skirt).
- FIX act_dance_classes_equip: "a sprung wooden floor" -> "a stack of exercise mats" (template says "Equipment nearby includes").
- FIX act_yoga_action: "lying in a final rest with the arms open" -> "lying flat on the back in a final rest pose with the arms open at the sides".
- PRE act_*_scene_prompt (all activities): "__act_X_equip__ can be seen." gives a lowercase sentence start ("... at dawn. a rolled mat can be seen."). Fix for yoga/dance/martial: "There is __act_X_equip__ in view."
- PRE act_*_frame_prompt: frame style can say "studio-lit fashion photograph on a seamless backdrop" while the place is a dojo or beach; and the style fragment starts lowercase. Not changed today; listed for a later fix.

## Batch 2 - f_body_nipples, f_body_anus, m_body_anus, head_chin
- FIX f_body_nipples (35 new v107 lines): grammar ("her breasts have a tiny flat nipple that barely rises set in ..."; "puffy nipple with the areola rising in a soft dome set in a ... areola"). Reword as "each breast has <nipple>, set in <areola>, the areola <surface>"; puffy folded into the areola text. Old 50 lines OK.
- FIX f_body_anus line 9: "a rosette with a slightly darker ring around it than the surrounding skin" -> "a rosette ringed by skin slightly darker than the skin around it".
- NOTE f_body_anus / m_body_anus are not referenced by any template yet (showcase only).
- FIX head_chin (v106): lines 132-139 garbled ("chin with a faint small dimple in the middle of the tip and a faint dimple"); remove. Remove the word "cleft" and the negation "not a long line" from all dimple lines: "X chin with a small, shallow dimple in the middle of its tip". Repeated lines at the top are the file's original weighting (OK).

## Batch 3 - male_bulge_* (7 files), kink_panel_wm
- OK: all read. Bulge lines are anatomically clear, always "fully covering him", left/right variants balanced. male_bulge_loose repeats its tent lines on purpose (source list weights tents 3:1 over flat) - not a bug.
- OK kink_panel_wm: 8 scenes, adults, consensual framing, positions and hands stated.

## APPLIED (working library, and in _tools/v108_stage.py for the next build)
- adult_l1..l6_group: duplicate lines removed (cause: v106 capitalises new lines after its duplicate check, so a rebuild re-added them). Files now identical to v106.
- head_chin, f_body_nipples, f_body_anus, act_* fixes from batches 1 and 2.

## Batch 4 - adult_l1..l3_panel_wm/ww/mm (9 files)
- FIX "Both people in this panel are women/men." (84 lines, L1-L4 ww/mm) -> "Both people are women/men." ("panel" invites a comic-panel layout when the line is used as a single image).
- FIX bulge sentence removed where the partner's body hides his groin (woman lying on top of him; woman sitting on his thighs facing him; man lying on top of the other man).
- ASK user: L1 (clothed) includes "woman bent forward at a table, man behind holding her hips" - keep at L1?
- OK otherwise: hand placement, camera and clothing consistent; L2 underwear, L3 topless with bottoms, matching bulge class per garment.

## Batch 5 - adult_l4_panel_wm/ww/mm
- FIX L4 wm: "her vulva ... his penis ... in view" in poses that hide them: woman lying on top (now "Their bodies are pressed together from chest to hips."), woman straddling his lap ("Her breasts are in view from the side."), woman bent at a table seen from the side ("Her breasts hang in view, and his penis ... beside her hips").
- FIX L4 mm: man lying on top - "their bodies pressed together from chest to hips".
- OK: standing, sitting side by side, kneeling and behind-the-partner poses (designed so both fronts show).

## Batch 6 - adult_l5/l6_panel_wm/mm/ww + 18 act files (24 files)
- OK: all L5 lines read; positions, hands and camera agree; adults, consensual.
- FIX 69 lines: "with the first man's head is level with ..." / "her head is level with his hips and his head is level ..." -> "head level with" (12 lines in 12 files).
- OK: the 18 act files (anal/oral/vaginal/hand/scissor/other) contain only lines from their main panel file, each in the right act.
- OK L6 wm: same as L5 plus small semen or clear squirting endings, landing where the pose allows.
- PRE (not caused today, same in v105): L6 mm and ww panels are identical to L5 - no level-6 endings for same-sex couples.

## Batch 7 - adult_l5/l6_position_* (22 files)
- FIX camera "at mattress height" on positions with no bed (wall, table, chair, armchair, standing) -> "at hip height".
- FIX three-person lines said "showing both bodies" -> "showing all three bodies".
- FIX impossible position ("sits on the edge of a bed ... she lies back on the floor between his thighs ... inside her") replaced with her astride his lap facing him, knees on the mattress.
- OK: all other positions read; geometry, hands and acts agree; sub-files are subsets of position_all.

## Batch 8 - adult_l1..l6_location (new v106 lines, 20 per level)
- FIX L1 and L3: clothing was picked regardless of setting (suit jacket under a beach shower, sweater in a steam room, jumper with legs in a plunge pool). Wet or hot places now: L1 swim shorts and an open linen shirt / one-piece swimsuit with a sarong; L3 swim trunks (medium bulge) / bikini bottoms.
- OK L2 (underwear by design), L4 nude, L5 and L6 masturbation and endings: poses, hands and cameras agree.

## Batch 9 - adult_l1..l3_masturbation_f/m, adult_l3_pose_person/scene
- FIX L3 poses: "nude" beside a garment (kneeling nude ... in boxer briefs; on all fours, nude ... in cotton briefs; recline nude ... a thong on each; only stockings, a thong on) and "in low-slung jeans ... bare thigh and buttock exposed" - now say only what is worn.
- FIX L2 solo: "swim trunks ... inside the front of his underwear" -> "his swim trunks"; "mesh bodysuit ... her underwear" -> "her bodysuit".
- OK L1 (clothed, hands over clothing), L3 solo (topless with bottoms, hands over or inside the waistband).

## Batch 10 - adult_l4..l6_wrestling_mm
- FIX L4: "penises and scrotums in view" removed from the four holds that hide them (on his chest with legs locked round the waist, face down, legs scissored round the waist, chest to chest against a wall).
- OK L5/L6: acts and endings agree with the holds; semen lands where the pose allows.

## Batch 11 - adult_l1..l6_group (new v106 lines)
- FIX L4: "Everyone is nude, with breasts and penises and scrotums in view" was used for every trio, including three men and three women. Now per trio (three men / three women / woman and two men / two women and a man).
- OK L1-L3 (clothing correct for each person's gender, bulge class per garment), L5-L6 acts and endings.

## Batch 12 - v106_entry_points, v107_entry_points, package README
- OK: 344 + 6 names, every one is a real file, no duplicates.
- FIX package README.txt carried the v107 line three times (finish.py was run three times). Removed; finish.py now adds the version line only once. The released v107 zips contain the triple line.

## SUMMARY
All 105 changed files read. Fixes are in the working library and in _tools/v108_stage.py (applied by the next build); nothing is released yet.
