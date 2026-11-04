NOTE: file names in this README are the women's base names; in the combined folder they carry an f_ prefix (men: m_). See FILE_NAMING.txt.
HAIR LAYER v1

PROBLEM: the ethnic identity line stated a hair type ("tightly coiled black hair") while hair_curl, hair_style, hair_texture and hair_volume were rolled independently.
In a 3,000-prompt test the curl pattern agreed with the ethnic line only 43% of the time. Hair styles were also a flat list of 28 options with no length/age/texture logic.

NOW: hair type T (S straight, W wavy, C curly, K coily) is chosen once per prompt, inside prompt_char_physical, and passed to both the identity line and the hair paragraph.
  - countries_ethnic_prompts is split into countries_ethnic_prompts_S/W/C/K by the hair wording in each line (1,297 of 1,950 lines state it; 653 are assigned
    deterministically from a rough guess - see docs/hair_type_audit.csv and correct any you disagree with in hair_model.py: line_type()).
    Because the type is picked in proportion to the number of lines of that type and the line is then drawn uniformly inside it, the joint distribution of your ethnic
    lines is unchanged.  Anchored type shares: straight 32.6 | wavy 32.2 | curly 7.8 | coily 27.4 (countries are weighted equally in your file, hence the high coily share).
  - Independent mode (no ethnic line) uses placeholder worldwide shares: straight 58 | wavy 22 | curly 12 | coily 8.
  - hair_curl_<T>: your 28 curl options sorted by type + new natural-language options.
  - hairtex_<T>[_age bracket], hairvol_<T>[_age bracket]: your 28 texture/volume options re-weighted by type fit and age; every option kept at least once.
  - hairstyle_<T> and age<lo>_<hi>_hairstyle_<T>: noun-phrase styles from a grammar (length x cut x fringe x styling; a separate catalogue for coily hair: braids, twists,
    locs, afros, puffs, wraps ...). Lengths shorten and updos/pixie cuts rise with age; ponytails/pigtails/top knots fall. All 28 original styles are kept at least once in
    every file where they are compatible with the type. A loosely draped headscarf style is included at ~2%.
  - hair_style.txt (global) is rebuilt: 2,500 lines mixing all types and brackets; all 28 originals kept.
  - prompt_char_hair, prompt_char_physical, prompt_char_physical_short (and the age<lo>_<hi>_ versions) are type-aware; hair paragraph wording rewritten so styles read cleanly.

LIMITS: hair COLOUR is still independent of ancestry in independent mode; baby hairs / edges / hairline are not type-linked; style weights are my estimates, not data.

REBUILD: python _tools/build_all.py --only hair     (run from the wildcards folder; see HOW_TO_RUN.txt)
