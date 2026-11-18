STYLE PACKS: ILLUSTRATION AND PHOTOGRAPHIC STYLE (v9)
=====================================================
Two supplied packs are part of the library now:
- illustration_*  : 179 category files (medium, line, shape, colour, light, texture, dimension, composition, character, environment, typography, mood, lineage, context),
                    presets, 229 signature devices, children's-art-style files (how a child's drawing looks), and 36 illustration prompts (illustration_prompt_*; they were prompt_* in the pack).
- photostyle_*    : about 4,400 anonymised photographic-style entries (traits, 500 whole-style descriptions in sig_*, subjects, gear) and the mode prompts, entry point photostyle_master.
Their original READMEs are in this docs folder (STYLE_PACK_*).

CHANGES MADE WHEN INTEGRATING
- Adult-only: 92 lines that depict a child or teenager (e.g. in photostyle_subj_people, the sig_* files, illustration_subject and the signature devices) were removed.
  Lines about who a picture is for or who made it are kept ("a children's picture book illustration", "a child's drawing", the illustration_childart_* files).
- Gender/relationship lines were removed from the photographic trait files, so they cannot contradict the generated person.
- 2 '#' comment lines were removed (they would have been printed into prompts).
- Every { } | choice and N$$ multi-pick was replaced by small opt_ext_* files (multi-picks became 240 pre-drawn distinct combinations). No { } | remain anywhere.
- The prompt_* files keep their meaning; only the name changed (illustration_prompt_01_core ...).

BRIDGES TO THE PERSON PROMPTS
- style_photo_block / style_illustration_block : one style slot each (lighting, palette, camera, lens ... / medium, line, colour, shape, texture ...).
- f_prompt_photostyled, m_prompt_photostyled   : the normal age-weighted master prompt followed (or preceded) by a photographic style block.
- f_prompt_illustrated, m_prompt_illustrated   : the same person (look, wardrobe, pose, setting) written as an illustration in a random illustration style.
- The packs' own prompts (photostyle_master, illustration_prompt_*) need no person; they describe a subject of their own.
Note: the style packs choose their own colours, lighting and mood, so they can override or duplicate what the person prompts say; use them in place of f_prompt_style / prompt_camera_light for a clean result.

REBUILD
build_all.py runs _tools/style_packs.py as its last step (sources in _tools/data/style_packs). The "all options once" set includes both packs (aoo_illustration_*, aoo_photostyle_*)
with aoo_prompt_photostyled and aoo_prompt_illustrated.
