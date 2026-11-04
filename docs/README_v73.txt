Guyanonymous' Wildcards - v73 changes (2026-11-03)

WHY: the backlog items that were confirmed after the v72 release, plus the checks that stop the same problems coming back.

1. EXPRESSION INTENSITY TIERS (item 54) - _tools/v73_expressions.py, data in _tools/data/expr_tiers.py
   - 68 emotions, each in three tiers (mild, strong, extreme), each tier described physically: mouth, eyes, brows, head or shoulders. The emotion name stays as the label ("a faint amusement, with one corner of the mouth lifted...").
   - facialExpressionsFor_v10 and pose_emotion are rebuilt from the same table (tier weights mild 3, strong 3, extreme 1; 476 lines each, 204 distinct descriptions). The old lists were mostly bare names ("surprised", "cheerful") joined to random modifiers.
   - New manual files: expr_mild, expr_strong, expr_extreme (68 lines each) for choosing the intensity yourself.
2. CONSISTENCY PASS (item 59) - _tools/v73_consistency.py and the check script _tools/check_consistency.py
   - City scenes draw time and weather as consistent pairs (city_conditions, city_night_conditions): no more deep night with a windy day, midday with fog, or a "city at night" lit by bright midday light. "a night market" became "an open-air market".
   - Penguins (animal_penguins) and flightless birds (animal_flightless_birds: cassowary, emu, kiwi, ostrich, rhea, kakapo) have their own groups, behaviours, scenes, close-ups and young lines, so they never fly. Chicks wording was removed from the flying-bird group pools and from the young-waterbird scene.
   - Condition prompts for clothing no longer carry their own random wear state (condw_ copies of the wear prompt chain), so "spotless and pressed" can no longer sit next to "badly broken fastenings".
   - Four fx lines that said "night" while the light was drawn separately were reworded.
   - The check script expands about 88,000 entry-point prompts and flags rule pairs; before the pass it flagged 182, after it flags 0 to 1 per run. Still open: maker style versus genre (a Tata pickup with "tiny four-seat car"), "joint or hinge" on parts that have none.
3. DEPTH AND OCCLUSION FAMILY (item 56) - _tools/v73_depth.py: depth_foreground_clear, depth_foreground_object, depth_person_in_front, depth_behind_furniture, depth_side_by_side, depth_layered, depth_scale_rule, depth_tag and depth_prompt (picks one family). Manual use, positive wording only. The scale rule comes from the 16-person tests (far figures about one third the height of near ones). Not yet tested in images.
4. ANCHORING PHASE 2 - _tools/v73_anchor2.py: 6,568 lines in 448 long-form person piece files now start sentences with "The woman's", "The man's" or "The person's" instead of Her / His / Their, so each attribute is tied to one named person in group scenes.
5. CLEANUP - _tools/v73_cleanup.py, v73_rename_dunder.py, v73_chastity_belt.py
   - 272 file names with a double underscore (for example acc_x_display__material) were renamed to a single underscore and every reference fixed (a __name__ parser can read the old names as two references).
   - mark_tattoo and dem_unique: blank padding lines became single-space "none" lines. Curly quotes, en and em dashes and the stray colon are gone. "School backpack", "school bags by the door" and "school satchel" reworded for the adults-only rule (uniform and costume lines were left).
   - New general chastity_belt group (belt-style devices covering several areas), built from the belt entries of the vagina group, and added to chastity_prompt.
6. TOOLS - _tools/check_build.py is the standing build check (references, symbols, blank lines, pronoun leads, contradictions, bare-name report). _tools/simple_build.py (the All Options Once builder) now finds every export module by itself, builds into a temporary folder, repairs or drops references to missing files, carries over files it cannot regenerate and refuses to replace the real folder if the file count falls by more than 1 percent. The release script keeps the last two released versions.

RUN ORDER after any rebuild (all idempotent, originals in _tools/backup_v70, backup_v71 and backup_v72):
   python _tools/v71_build.py ; python _tools/v72_facial_hair.py ; python _tools/v72_scars.py ; python _tools/v73_cleanup.py ; python _tools/v73_consistency.py ; python _tools/v73_expressions.py ; python _tools/v73_depth.py ; python _tools/v73_chastity_belt.py ; python _tools/v73_anchor2.py ; python _tools/v73_rename_dunder.py ; python _tools/check_build.py
UNDO: add --restore to each (v73_rename_dunder.py also supports --restore).

LEFT FOR LATER: skin tone drift (53) and framing (55) were set aside by request; held props (57) awaits a decision; group wrappers ("They walk together") and the repeated-identity tag are still open.
