NOTE: file names in this README are the women's base names; in the combined folder they carry an f_ prefix (men: m_). See FILE_NAMING.txt.
AGE LAYER v1 - age-bracket conditioned wildcards

WHY: previously every attribute was rolled independently, so a 19-year-old could get "papery crinkled skin" and an 87-year-old "jet black hair".
Now the age bracket is chosen FIRST (inside prompt_master_by_age) and every age-linked attribute for that prompt is drawn from that bracket's own file.

BRACKETS (adult women, population-weighted): 18-24 14.0% | 25-34 21.8% | 35-44 18.7% | 45-54 16.5% | 55-64 13.8% | 65-74 9.1% | 75-84 4.5% | 85-120 1.7%
  (shares are my approximation of UN WPP figures - verify before relying on them)

USE:  __prompt_master_by_age__            (replaces __prompt_master__; needs the prompts_v1 + pilot_v2 files too)

FILES (457, all prefixed age<lo>_<hi>_):
  _age_years              single-year ages in the bracket (85-120 decays to 120, every age kept at least once)
  _<attribute>            43 age-linked attributes: skin_wrinkle/texture/glow/marks, head_cheek/jaw/temple, nose_crease, eye_lid/lash/brow/sclera/color,
                          neck_crease/muscle, lip_* (5), hair_color/texture/volume/line/shine, body_build/height/compos/bones, musc_* (7),
                          hand_* (4), pose_action/twist/weight   (every original option is still present at least once - 1000 lines each)
  _opt_tattoo, _opt_eyewear   sentence-ready, blank = none; tattoo prevalence peaks 25-44, eyewear rises with age (rough estimates)
  _prompt_* (11)          the section templates re-pointed at the bracket's files, plus _prompt_master
  prompt_master_by_age    picks the bracket by population share

HOW THE CONNECTION WORKS: weight(option, bracket) = base weight x age kernel. Kernels: 'up' (more likely with age), 'down', 'peak', 'flat'.
  Tags come from a keyword heuristic + explicit overrides (_tools/age_model.py). age_affinity_audit.csv lists every option's tag and its final

NOT YET AGE-CONDITIONED: clothing, hair style, makeup, face shape, nose/ear shape, body_ratio/proprtn, health_conditions, settings.
Base weights outside the 6 pilot-weighted files are placeholders (1.0, atypical options 0.3).

REBUILD: python _tools/build_all.py --only age     (run from the wildcards folder; see HOW_TO_RUN.txt)
