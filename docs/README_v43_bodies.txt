Guyanonymous' Wildcards v43 - bodies, teeth, tattoos
=====================================================
All wording is plain (no weights, no LoRA tags, no camera words). Anatomy wording is clinical and detached. Adults only.

1. LoRA removal
   Every <lora:...> tag and trigger word was removed from the six files that held them (f_WOMANprompt, f_WOMANprompt_ethnic_skin, f_character_female_basic, f_body_vulva, f_body_clitoris, f_body_labia2). f_body_labia2 was deleted.

2. Female anatomy (optional - the create_ prompts leave it out)
   f_body_vulva            a complete clinical description made from the pieces below (160 lines)
   f_body_labia_majora     outer labia, fullness and shape
   f_body_labia            inner labia (unchanged)
   f_body_vulva_tone       skin tone, matched to the person's own skin tone
   f_body_clitoris         unaroused, resting state (the default)
   f_body_clitoris_aroused MANUAL ONLY - never called by another file
   Use: __f_create_random_woman_nude__ __f_body_vulva__

3. Male anatomy
   m_body_genitals         flaccid (the default); near-average sizes weighted (about 50 percent average, rest from small to large); circumcised or not; shaft tone; pubic area; scrotum
   m_body_genitals_erect   MANUAL ONLY - never called by another file
   The hard-coded penis sentences from the old anyone_prompt file are gone; use the create_ files and add __m_body_genitals__ yourself.
   Use: __m_create_random_man_nude__ __m_body_genitals__

4. Teeth
   age{18_24 ... 95_120}_lip_teeth   rewritten: perfect, natural, flawed, stained, missing teeth, dentures and gold caps, with the odds shifting with age (more wear, loss and dentures with age)
   teeth_access_high / _mid / _low   the same range weighted by dental care access (use with a country you pick; high = widespread orthodontic care, low = more decay and missing teeth)
   lip_teeth                         one pool covering everything

5. Tattoos
   tattoo_temporary        stick-on and transfer tattoos (flat colour, glossy film, lifted edges)
   tattoo_henna            henna body art (patterns and stain colours)
   tattoo_bad              badly done tattoos, including misspelled words described in plain words (a letter doubled, swapped, missing)
   tattoo_novelty_random   picks one of the three

6. Sample prompts: Guyanonymous_Wildcards_v43_sample_prompts.txt (96 random prompts) and _labelled.tsv.
