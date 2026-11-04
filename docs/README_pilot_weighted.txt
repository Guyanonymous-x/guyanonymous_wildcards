NOTE: file names in this README are the women's base names; in the combined folder they carry an f_ prefix (men: m_). See FILE_NAMING.txt.
PILOT v2 - frequency-weighted wildcards
wildcards/   drop-in replacements (same filenames) for: eye_color, hair_color, hair_style, hair_texture, dem_tone,
             body_build, body_height, skin_wrinkle, dem_unique, mark_tattoo
             + NEW clothing_everyday_female.txt (natural-language outfits, 2500 lines)
scripts/     wcbuild.py (generic builder), pilot_body.py (the weight tables - edit and re-run), clothing_everyday.py (generator)
Rules: every original option kept >= 1 time; <= 2500 lines; blank lines = "none" (dem_unique 65%, mark_tattoo 88%).
Weights are rough worldwide-adult-woman estimates, NOT yet cited or conditioned on country/age/ethnicity.

REBUILD: python _tools/build_all.py --only weights     (run from the wildcards folder; see HOW_TO_RUN.txt)
