WILDCARD LIBRARY - women + men in one folder

  wildcards/          drop-in folder (flat; ~2,180 .txt files) + _tools/ (Python tools - your image tool ignores it)
  docs/               READMEs per layer, naming guide, old->new rename map, sample prompts, change log
  HOW_TO_RUN.txt      how to run the Python tools

NAMING  (details: docs/FILE_NAMING.txt)
  f_xxxx      a FEMALE file          m_xxxx      a MALE file          xxxx (no prefix)   shared by both - identical for women and men
  A file is shared only if it comes out byte-identical for both genders and refers only to shared files; everything else is prefixed, with its __references__ rewritten.
  WARNING: the female files were RENAMED (e.g. prompt_master_by_age -> f_prompt_master_by_age, names_female -> f_names). Replace your old female files with this folder;
  docs/RENAME_MAP_old_to_new.csv lists every old -> new name (663 shared files kept their names, 758 became f_).

NEW IN v42: plain-named character creation prompts, e.g. f_create_random_woman, m_create_random_man_w_clothes_short, any_create_random_person_unlinked - see docs/README_v42_people.txt

ENTRY POINTS  (use as  __name__  in a prompt; swap f_ / m_)
  f_prompt_master_by_age   m_prompt_master_by_age                         age + body conditioned character AND clothing   <- recommended
  f_prompt_master_by_age_random_clothing   m_...                          conditioned character, completely random clothing
  f_prompt_master_random_clothing          m_...                          nothing conditioned, completely random clothing
  f_prompt_master                          m_...                          nothing conditioned, realistic everyday clothing
  f_prompt_master_short                    m_...                          ~120-word version for CLIP-limited models
  Your own big templates: f_WOMANprompt / f_character_female_basic  and  m_MANprompt / m_character_male_basic (the male ones drop your LoRA tag - see docs/README_men.txt).

THE MEN'S SET (details: docs/README_men.txt)
  male body descriptors, build/height tables, facial hair (age-conditioned graying), male-pattern baldness that rises with age, male hairstyles (fades, crops, quiffs, braids, locs, afros...),
  grooming instead of makeup, men's jewellery/belts, 1,480 names, 63 cosplay archetypes -> 567 costumes, male outfit lists + 2,500 outfit lines (m_clothing_full), age/body conditioned clothing,
  clinical anatomy files (m_body_pecs / m_body_nipples / m_body_buttocks / m_body_genitals / m_pubichair / m_body_chesthair) - not referenced by any template, same as the female ones.
  The female library is unchanged: all 1,421 previous files are identical in content (verified) - only the names differ.

WHAT'S NEW IN THIS VERSION (details: docs/README_v3_changes.txt)
  * Eyewear: acc_glasses (whole population) and age<lo>_<hi>_opt_eyewear are now 5,000-line files with realistic shares of no glasses / contact lenses / glasses / sunglasses by age,
    thousands of frame designs, exactly 0.5% monocle and 0.5% eyepatch in every file; all 28 original options kept.
  * Aging and obesity: 9 age brackets (85-94 and 95-120 are separate), single-year age wording ("84 years old, in their mid eighties, elderly and visibly frail ..."), an __aging_summary__ sentence,
    ~150 extra very-old options and a new "severely obese" body type (BMI 35+) with 100 extra options (folds, belly, neck, limbs, skin, posture).
  * Objects: the rubber ducks are gone (2 duck-race lines left of 10,000; was ~107). New obj_* files (furniture, room items, table items, street items, toys, held items), enlarged acc_props / env_props (2,500 lines each).
  * Groups of 2 and 3 people (grp_*): two men / two women / man+woman and MMM, WWW, MMW, MWW; every line has all people actively engaged with each other (positive, in-between or negative).
  * Shoes (shoe_*): six quality tiers (budget to museum-grade, with prices), seven shoe classes (~280 types), purpose, audience, pattern, materials, construction, hardware, soles, extras and price overlay; start from shoe_prompt_master (see docs/SHOES.txt).
  * Demographic groups (demo_*): cisgender, trans, intersex, androgynous, non-binary, midway-in-transition and "stopped partway" identities x heterosexual / homosexual / bisexual / pansexual / asexual.
  * Accessories, mobility aids, settings and poses now follow age and body type (age<lo>_<hi>_aids_<arch>, _settings_<arch>, _pose_*_<arch>, _acc_hats / _acc_jewelry / _acc_props).
  * _tools/prompt_viewer.html: two equal-height scrolling panes (prompt design on the left, sample output on the right).

KNOWN ISSUES
  * Anatomy files body_labia2 / body_vulva / body_clitoris hold your own LoRA tags and have no male counterpart (I cannot invent LoRA names).
  * clothing_full (both genders) keeps your/inherited near-nude options; the age/body conditioned files exclude them. "5::" weight prefixes work in your tool, not in _tools/expand.py.
  * Weights and shares (age brackets, body types, hair types, facial hair, baldness) are estimates - audit CSVs are in wildcards/_tools/audit.
  * Not conditioned for either gender yet: climate, country dress. Beard colour is not linked to hair colour. Facial-hair density is not linked to ancestry.
