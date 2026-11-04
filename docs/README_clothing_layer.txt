NOTE: file names in this README are the women's base names; in the combined folder they carry an f_ prefix (men: m_). See FILE_NAMING.txt.
CLOTHING LAYER v1  (+ outfit lists, 630 cosplay costumes, random clothing mix)

1. OUTFIT ATTRIBUTE LISTS (outfit_color, _material, _pattern, _casual_top, _casual_bottom, _dress_style, _uniform_type, _sexy_top, _sexy_bottom, _sexy_full, _see_through, _lingerie)
   The files your clothing_full_female.txt expected were not in any of the zips you uploaded (all three uploads are byte-identical: same MD5, 144 files, no outfit/ folder),
   so they are populated from YOUR OWN vocabulary: _tools/data/outfit_vocab.json was mined from the 2,600 outfit lines in clothing_full_female.txt (colour / material / pattern word
   frequencies, garment and uniform phrases with colours, patterns and filler adjectives stripped, sheer outfits copied from your own lines) plus supplements for coverage.
   Weights follow how often each term appears in your file. If you still have your originals, just overwrite the outfit_*.txt files with them - nothing else needs to change.
2. outfit_cosplay: 630 distinct, specifically described costumes (70 original archetypes x 9 variants: fantasy, sci-fi, historical, gothic/horror, steampunk, anime-inspired, folklore/myth,
   original superheroes). No named copyrighted characters. Source: _tools/cosplay_data_a/b/c.py (add archetypes there, then python _tools/build_all.py --only outfits).
3. outfit_sexy_mixed / uniform_mixed / formal_mixed / casual_mixed: the corrected targets of the 5 pointer lines in clothing_full_female.txt.
4. AGE + BODY CONDITIONED CLOTHING: age<lo>_<hi>_clothing_<archetype> (8 brackets x 8 body types, 1,000 outfits each).
   Garments, colours, patterns, fits and shoes follow age curves (crop tops, mini skirts, neon, hoodies fall with age; cardigans, shawls, elastic-waist trousers and cushioned shoes rise);
   body type nudges fit and coverage (loose/wrap/A-line up and crop/tight down for heavier builds; athletic/active wear up for athletic and muscular builds; layers, long sleeves, comfort shoes up
   and heels down for frail builds). 1-8% (by age) of each file is drawn from your clothing_full_female.txt lines, age-weighted, excluding its nude / near-nude / anatomy lines.
   Within a prompt the character body and the clothing use the SAME body archetype (age<lo>_<hi>_prompt_master_<archetype>).
5. COMPLETELY RANDOM CLOTHING (not tied to age or body): clothing_random_mix = everyday outfits 20 | your full list 30 | cosplay 12 | casual 8 | formal 7 | uniform 6 | sexy 7 | see-through 4 | lingerie 3 | colour+material+dress 3.
   prompt_wardrobe_random uses it.  Entry points:
     __prompt_master_by_age__                    age + body conditioned character AND clothing   (recommended)
     __prompt_master_by_age_random_clothing__    age + body conditioned character, completely random clothing
     __prompt_master_random_clothing__           nothing conditioned, random clothing
     __prompt_master__                           nothing conditioned, realistic everyday clothing (clothing_pool)
NOT CONDITIONED YET: accessories (hats/jewellery/bags), makeup, pose, setting. Climate/season and country dress are not modelled.
