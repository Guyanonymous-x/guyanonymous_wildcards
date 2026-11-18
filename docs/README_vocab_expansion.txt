VOCABULARY EXPANSION (v8)
=========================
Goal: every option file (except those already over 1000 distinct items) brought to at least 200 distinct options, and to 400-700 where the subject allows it.
Result: 1848 of the 3904 files now hold 200+ distinct lines, 336 hold 500+. (Many of the rest are the generated age-bracket / demographic / prompt
template files, which are built from the option files and are not option lists themselves.)

WHAT WAS EXPANDED (each now 200-770 distinct options)
- Clothing: colours (548), materials (434), patterns (455), and the details / fabric / fit / layers / pattern-description lists (about 500 each), plus
  every garment list (tops, bottoms, dresses, uniforms, suits, outerwear, swim/underwear, etc., 200-356 each, both genders).
  The assembled-outfit "mixed" files (casual, formal, uniform, sexy / swim) went from 5-9 lines to about 300 each; they point at the expanded lists.
- Face, head, neck, eyes, brows, lashes, nose, lips/teeth/gums, ears, skin (texture, finish, glow, flush, marks, fuzz, wrinkles), hands/nails, marks (tattoo, piercing,
  scars, paint, cyber), hair shine/volume/hairline/motion/curl/texture, hats, jewellery, straps/bags, make-up, body build/height/ratios, muscle groups.
- Scene: lighting, camera (lens choices are matched to focal range), environment, weather, time, style, medium, poses, expressions, settings (770).
- People: ethnicity / heritage / bone structure / tone, attractiveness (188), facial hair, grooming, curl types per hair type (220 each), K-style hair (260).

EYE AND HAIR COLOUR FOLLOW WORLD POPULATION
- eye_color (531 options): brown ~77%, blue ~8.5%, hazel ~5%, amber ~4.5%, green ~2%, grey ~0.9%, heterochromia and rare ~0.6%, plus a few age-related ones.
- hair_color (553 options): black ~76%, brown ~12%, blonde ~2%, red ~1.2%, grey/white ~6.8% (scaled up with age by the age model), fashion dyes ~2%.
  Within each group the many shades are shared out evenly. The original options are kept inside their groups.

HOW NEW OPTIONS WERE MADE
Options are assembled from lists of leading adjectives and descriptors (combinators) and filtered so that contradictory pairs (e.g. "smooth" + "heavily creased") never occur.
Selection is deterministic (seeded), so rebuilding gives identical files.
- Evenly weighted files: every option appears once.
- Weighted files: the original lines and their proportions stay; the new options share a block that is 25% of the file.
- Blank lines ("none") keep their original share. No { } | characters and no "N::" weights appear in any file.
- The age files for big lists were enlarged (at least 1000 lines, 4 lines per option) so that 300-550 options keep sensible proportions.
- Neutrality rules still hold: no colour words in non-colour files, no age or gender words in feature files.
New modules in _tools: vocab_lib, vocab_face, vocab_body, vocab_scene, vocab_people, vocab_misc, vocab_clothing_a/b, vocab_colors, vocab_apply
(vocab_apply runs first in build_all; use  --no-vocab  to skip it).

NOT EXPANDED (limited possibilities, or deliberately left alone)
- Explicit anatomy: body_labia*, body_vulva, body_clitoris, body_genitals, body_nipples, body_breasts, body_buttocks, body_pecs, pubichair (10-50 options each).
- Numeric lists: f/m_height, f/m_weightkg (37-45 steps), dem_age, attractiveness2 (numeric weights).
- Fixed sets: countries (195), countries_demonyms (193), body_armpithair (4 states), health_conditions (9), countries_ethnic_prompts_C (135).
- Slightly under 200: m_body_chesthair (192), photographer styles (99-100), f/m_heights_all and weights_all (83-149 long descriptive lines).
- Shoe sub-files with few real possibilities (footbed 17, heel material 27, finish 37, lining 41).

THE SEPARATE "ALL OPTIONS ONCE" SET
See the other zip (wildcards_all_options_once_v1.zip): the same material with gender, age and proportion removed.
