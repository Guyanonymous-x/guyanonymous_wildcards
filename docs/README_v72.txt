Guyanonymous' Wildcards - v72 changes (released with the v71 anchor pass; applied 2026-11-03)

WHY: Moss tests on 2026-11-03 (10 facial hair images, 18 people-count images, 12 CFG images) showed that named beard styles are weak and that positive physical descriptions work.

1. FACIAL HAIR (backlog item 52) - _tools/v72_facial_hair.py
   - All 303 distinct lines in m_facial_hair, m_age*_facial_hair (9 files) and any_age*_facial_hair (9 files) are rewritten as plain descriptions of where hair grows and where skin is bare (for example the soul patch is "a tiny tuft of hair directly under the lower lip, about the size of a thumbprint, with smooth, hairless skin on the cheeks, chin sides and upper lip").
   - Shaved faces: "smooth, shiny, hairless skin on the chin, cheeks and upper lip, like freshly shaved skin" (tested wording; the 85 year old came out smooth in 6 of 6).
   - Modifiers that contradict a description (connected to the mustache, clean upper lip, rounded bottom and similar) are dropped; the safe ones (neatly groomed, left natural, freshly trimmed, and so on) are kept.
   - Person templates (m_ and any_ age*_prompt_char_face, m_prompt_char_face) now say "His/Their lower face has __..._facial_hair__." instead of "facial hair is", so hair lines and bare-skin lines both read correctly. make_male_templates.py and src_templates_m/prompt_char_face.tpl carry the same sentence.
   - Line counts per file and the age weighting are unchanged (lines were replaced one for one).
   - Open: one 76 year old kept a white beard in every wording; test his other descriptors.
2. SCARS - _tools/v72_scars.py
   - The parametric lines "<adjective> scar on the <place>" in mark_scars (260 lines) and skin_scars (138 lines) become a physical description with colour, relief and length (for example "a thin, pale, slightly raised scar about four centimetres long on the forearm"). Reason: the same words drew a pale raised scar in one image and a deep shadow-filled one in another. Hand-written lines (deep, keloid, surgical, self-harm lines) are untouched.

RUN ORDER after any rebuild (all idempotent, originals in _tools/backup_v70 and _tools/backup_v71):
   python _tools/v71_build.py ; python _tools/v72_facial_hair.py ; python _tools/v72_scars.py
UNDO: add --restore to each.

3. v71 ANCHOR PASS (included in this release) - _tools/v71_build.py
   - Furniture 'It has...' chains merged into 'The <object> has A, B and C'; room openers use the room noun; person templates (m_, f_, any_ create_random files and world_c_ files) are one chained sentence per person with no pronoun-start sentences; ageing summary pieces use 'The man', 'The woman' or 'This person'; 6 bare 'none' furniture options reworded.
   - Not done (phase 2): the long-form piece files (*_prompt_char_face/hair/skin/body/details, about 900 files) still start sentences with Their, His or Her; group wrappers still use 'They walk together'; the identity tag with skin tone needs a variable that repeats one random pick, which plain wildcards cannot do.
