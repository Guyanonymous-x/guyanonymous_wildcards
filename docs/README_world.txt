Guyanonymous' Wildcards - World-proportional random person (v17)
=================================================================
Adults only (18-120). Built to show the whole world's people in roughly the proportions they live in, with no region as the default.

ENTRY POINTS (use either; the odds are the same)
  __world_person__              BROAD: picks one of 14 world regions by adult population, then a country in that region, then a full person.
  __world_person_by_country__   FINE: picks any of 193 countries directly by adult population, then a full person.
Pick a region yourself:  __world_r_<region>_person__     Pick a country yourself:  __world_c_<country>_person__
Lists of the shares used: world_region_list.txt, world_country_list.txt. Ethnic-background lines by hair group: world_c_<country>_<W|K|S|C>.txt.

WHAT IS RANDOMISED
  - ancestry/background and hair group: from the chosen country's own background lines (10 per country, in the existing countries_ethnic_prompts files)
  - sex and age: age bands by the country's age profile (young / young-middle / middle / older), with a sex ratio that tilts female in old age
  - gender identity and sex characteristics: world shares from demo_build.py (cis, trans, non-binary, androgynous, intersex, gradual and individualized transitions)
  - physical body: the existing weighted body tables, with a regional factor on heavier builds
  - face, hair, skin, details, clothing, pose and setting from the existing age/body files.  No photographic style or camera tokens are included.

HONEST LIMITS
  - All numbers are rough best estimates (UN-style 2024 populations, region adult shares, age profiles). Edit _tools/world_data.py and re-run world_build.py.
  - Inside a country the mix of backgrounds follows that country's 10 lines, not a census. Multi-ethnic countries (for example the USA, Brazil, India, Nigeria)
    are only roughly proportional. Diaspora communities and mixed heritage are represented by country lines such as "Canadian Black African".
  - Identity shares are small and approximate; adjust IDENT in demo_build.py.
  - Earlier note: the existing age masters already include ethnicity (dem_ethnicity, countries_ethnic_prompts_*) but weight groups roughly equally; this layer replaces that with population weights.

REGION SHARES USED (adults)
  East Asia: about 23.7% of the world's adults
  South Asia: about 23.3% of the world's adults
  Southeast Asia: about 8.6% of the world's adults
  Central Asia and the Caucasus: about 1.1% of the world's adults
  the Middle East: about 4.4% of the world's adults
  Western, Northern and Southern Europe: about 6.2% of the world's adults
  North Africa: about 3.1% of the world's adults
  West Africa: about 3.9% of the world's adults
  East Africa and the Horn: about 3.5% of the world's adults
  Central and Southern Africa: about 3.3% of the world's adults
  Eastern Europe, Russia and the Balkans: about 4.5% of the world's adults
  North America: about 5.2% of the world's adults
  Latin America and the Caribbean: about 8.5% of the world's adults
  Oceania and the Pacific: about 0.6% of the world's adults
