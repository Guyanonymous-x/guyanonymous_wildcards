STAND-ALONE GARMENTS (v11)
==========================
Any single piece of clothing on its own, with no age and no gender built in. These 104 garment_* files are IN ADDITION to the existing age/gender-aware clothing
files and prompts; nothing existing was changed.

WHERE TO START
  __garment_prompt__            one fully described garment of any everyday/formal type
  __garment_prompt_shirt__      shirts, blouses, tees, tanks, tunics        __garment_prompt_knitwear__   sweaters, cardigans, hoodies, sweatshirts
  __garment_prompt_trousers__   trousers, chinos, joggers, leggings         __garment_prompt_jeans__      jeans and denim            __garment_prompt_shorts__
  __garment_prompt_skirt__      __garment_prompt_dress__   __garment_prompt_gown__   __garment_prompt_jumpsuit__
  __garment_prompt_coat__       __garment_prompt_jacket__  __garment_prompt_vest__   __garment_prompt_suit__   __garment_prompt_uniform__
  __garment_prompt_top__ / _bottom__ / _onepiece__ / _outerwear__   any type of that category
  __garment_prompt_intimate__   lingerie, sleepwear, swimwear, sheer and sexy pieces (kept out of clothing_garment_prompt on purpose)     __garment_prompt_costume__
  __garment_outfit__            several garments worn together (top + bottom, dress + jacket, suit ...)
  __garment_short_<type>__      compact phrase, e.g. "saffron linen A-line skirt", for building your own prompts
  f_prompt_master_garments / m_prompt_master_garments   the usual person prompt, with the wardrobe replaced by clothing_garment_outfit

THE PARTS (mix them yourself)
  garment_<type>               200-600 distinct garments per type, e.g. "pleated linen wrap skirt with a button front" (both genders merged, one copy each, weights removed)
  garment_base_<type>          plain base names (shirt, tee, skirt, parka ...), 240 each, to combine with the structure files:
  clothing_garment_neckline, sleeve, length, hem, waist, leg, silhouette, closure, pockets, collar, lining, feature      (150-450 each)
  Colour, material, pattern, fabric, fit and detail come from the existing clothing_outfit_color, clothing_outfit_material, clothing_outfit_pattern, clothing_part_fabric, clothing_part_fit, clothing_part_detail, clothing_part_pattern.

Two ways of describing a garment are mixed in every prompt: a ready-made named garment (richly described already, so only fit/detail/colour are added) and
a plain base garment built up from the structure files (neckline, sleeves, hem, closure, pockets ...), which gives garments nobody listed.

NOTES
- Gender and child wording was removed from garment names. The structure files contain no colours, genders or ages.
- Small sub-types (skirts, shorts, jumpsuits, gowns, vests) were enlarged to about 260 names with modifier combinations.
- Source of names: the merged outfit_* lists; builder _tools/garment_build.py (last step of build_all.py), words in _tools/vocab_garment.py.
- The "all options once" set has aoo_garment_* with the same prompts.
