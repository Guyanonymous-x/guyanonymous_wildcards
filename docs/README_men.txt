THE MEN'S SET

BUILT FROM THE SAME PIPELINE: bracket (population-weighted for adult men) -> body type -> hair type -> character, clothing, pose, setting, camera, style.
WHAT IS DIFFERENT FOR MEN
  * Brackets (share of adult men): 18-24 14.9 | 25-34 22.9 | 35-44 19.2 | 45-54 16.9 | 55-64 13.7 | 65-74 8.1 | 75-84 3.4 | 85+ 0.9   (approximate; fewer men at older ages)
  * Body-type shares differ (more muscular, fewer obese than women at the same age); m_body_build / m_body_height are rewritten male option lists (V-taper, dad-bod, barrel-chested,
    burly, runner's build ...), m_body_ratio / m_musc_hips / m_musc_legs keep the neutral options of the originals and add male ones.
  * Facial hair: m_facial_hair (about 300 distinct options) conditioned by age - salt-and-pepper / gray / white options rise with age, patchy and sparse options fall.  Since v72 every option is a physical description (where the hair grows, where the skin is bare, length and edge) instead of a style name, and shaved faces use positive wording ("smooth, shiny, hairless skin on the chin, cheeks and upper lip, like freshly shaved skin").  Prompts contain "His lower face has ...".
  * Male-pattern baldness: receding/thinning/bald/comb-over/horseshoe hairstyles and hairlines rise steeply with age (hairstyle share ~15% at 18-24 to ~50% at 75+).
  * Hairstyles are a separate male grammar (fades, tapers, crops, quiffs, pompadours, slick-backs, undercuts, man buns, long hair, shaved heads; coily-hair catalogue with fades,
    waves, cornrows, box braids, twists, locs, afros), age-conditioned and type-aware like the women's.
  * Grooming (m_grooming) replaces makeup; men's jewellery and belts/straps; 1,480 male names from ~60 cultures (m_names).
  * Clothing: outfit lists (m_outfit_casual_top/bottom, outerwear, suit_style, uniform_type, swim_underwear, see_through), m_clothing_full (2,500 lines in the same nested style as
    your female one: casual, layered, suits, uniforms, athletic, outdoor, work, traditional garments from many cultures, vintage, cosplay, a small share of near-nude options),
    63 cosplay archetypes -> 567 distinct costumes, and the age/body conditioned layer (m_age<lo>_<hi>_clothing_<body type>) with men's garments, fits and shoes.
  * Clinical anatomy descriptions (same register as the female files; no template references them): m_body_pecs, m_body_buttocks, m_body_nipples, m_body_genitals, m_pubichair, m_body_chesthair.
  * Health conditions: Turner syndrome (female-only) became Klinefelter syndrome; "twin sister" lines became "twin brother".
  * m_MANprompt / m_character_male_basic are your WOMANprompt / character_female_basic with pronouns swapped, makeup -> grooming, facial hair added and "baby hairs" removed.
    Your <lora:...> tag was NOT carried over (a LoRA trained on a woman would push the result female) - add your own back if you want it.
  * Filtered for men (female-coded options removed): eye_lash ("mascara-coated"), style_photographers_portrait ("feminine elegance"), heightweightdeform/weights/heights lists,
    poses_extended; height and weightkg are shifted to male ranges.
SHARED FILES STILL CONTAIN: background women in scene descriptions (settings10000), "pear-shaped face" (head_shape), stage-makeup mentions in mark_paint.
