# v106 - changes from the image tests (released)

Build: `_tools/v106_build.py` (overlays v106 on v105). Released with `finish.py 106`.

## Bulge (v106_bulge.py) - 7 pools
- tight (leggings, compression/cycling shorts): erect = raised line from crotch seam to navel / two fingers below / halfway (size variants), held flat by the fabric, seen from the front only; semi-erect against thigh; flaccid = penis and testicles resting together, fabric following their shape.
- brief (briefs, boxer briefs, thin swim trunks): plain "bulge / erection outline showing through the fabric" wording, no anatomy nouns.
- jock: modest close-fitting pouch, no larger than a hand (no free-standing cup).
- medium (jeans, chinos, trousers): unchanged, it tested well.
- loose: 6 of 8 lines now give a clear tent (about a hand wide, hand and a half long), draping over and around it; 2 stay flat.
- Removed everywhere: "rounded", "swell", "prominent", "subtle", "small" tent, smooth-surface wording.
- male_bulge_clothed now mixes medium + brief + tight erect.

## Panels L1-L4 (v106_panels.py)
- Garment class per outfit (tight / brief / jock / medium / loose) picks the pool.
- Pair postures rewritten with full geometry (who faces where, supports, hands, hips); facing poses carry "torsos turned toward each other" and a three-quarter camera; on-top poses spell out chest, stomach, hips, legs.
- Standing-behind poses put him slightly to one side so the front of his hips shows.
- L2/L3: "His hands stay clear of his groin." / "Neither man's hands are near his own groin."; free arms stated (no pocket hands).
- Two-person same-sex panels state "Both people in this panel are men/women"; the two men never wear the same garment.

## Solo (v106_solo.py)
- L3 solo: topless/shirtless in real bottoms (jeans, shorts, pyjamas, joggers, skirts), hand over the fabric or inside the waistband. All towel, sheet, throw, duvet, robe and held-pillow lines dropped.
- L1/L2 women: hand-on-stomach lines changed to hand on hip or inner thigh.

## Chin (v106_face.py)
- head_chin: every 'deeply cleft' / 'deep central cleft' line replaced. The first fix (a shallow vertical groove) still rendered as a split chin that looked like buttocks, so a cleft is now a small shallow dimple low on the chin tip, about fingernail-sized, no vertical line, outline unbroken.
- Showcase chin grids no longer draw from head_chin: each grid uses six clearly different shapes (sharp pointed, heavy square jutting, receding, soft double chin, small round with a dimple, long narrow) because subtle chin differences were invisible at that camera angle.

## Groups and wrestling (v106_group.py)
- adult_l1..l6_group: 24 new structured three-person scenes per level for L1-L4 (sofa row, shoulder to shoulder, lying together, circle, kissing pair with third behind, seated with one behind) and 2-4 explicit acts for L5/L6 (wwm, wmm, mmm, www); old one-sentence lines kept. Every person introduced once, hands and bodies placed with explicit names (no ambiguous "his"), distinct garments, bulge classes at L2/L3.
- adult_l4/5/6_wrestling_mm created: L4 nude holds with soft penises (6 holds), L5 and L6 explicit wrestling scenes (4 each), L6 with a small semen finish.
- adult_lN_location (v106_location.py): 20 new structured single-person venue scenes per level (sauna, open-air shower, bathhouse edge, hot tub deck, rooftop lounger, lake dock, locker room, hammock, steam room, kitchen counter; woman and man each) with posture geometry, hands, level clothing or nudity, light and camera. Old lines kept.
- Not converted: adult_lN_object lines (old one-sentence style, kept as is).

## Body-feature showcase files (never pushed to git; delivered in chat and to the local !Releases folder as Guyanonymous_Wildcards_v106_bodyfeature_showcase_*)
- V106_showcase_generator.py: 285 grids in the 2x2 layout. One individual per feature (one woman and one man): every grid for that feature shows the same person with the same clothing, light and background. Different features use different people. Close-ups show only the part (chin, one hand, one foot, not the whole head or arm) with the head turned about thirty degrees toward the left of the frame. Age grids keep one person across all panels. Adult pose-scene grids were removed (outside this job).
- convert_list.py: rebuilds the user's 141-line list one to one (133 prompts; the 9 pose-scene lines are left out) in 2x3 grids (3x2 for the portrait-size lines), keeping each line's seed and original option text, tidied (doubled phrases, deep cleft wording).
- Title: each image carries one line of text in its bottom left corner, "[Feature] Variations" (Eye Variations, Pose Variations and so on, singular names), with "Guyanonymous' Wildcards" in smaller text under it. Once per image, never per panel. Titles are in the TITLES table of V106_showcase_generator.py.
- Findings: 2x2 and 2x3 are the largest grids to use; 3x3 and 1x6 drop or duplicate panels.

## Carried from earlier today
- v106_acts.py and v106_positions.py (detailed L5/L6 geometry, 69 variants).

## Not done / needs a decision
- Heavier men: bulge below the belly cannot be set per person (the person token expands later).
- adult_lN_object lines are still in the old one-sentence style.
- Age-system follow-ups, more pose lines, the parked v90/v91 promo files and badge text words are not started.

## Standard showcase
- v106_showcase.py / v106_showcase_out.py: the normal 40-prompt version showcase (panels with bulge classes, groups, wrestling, locations, level 3 solo, kink); group and location picks are limited to the new structured lines (over 500 characters).
