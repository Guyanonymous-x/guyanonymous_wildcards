PROMPT TEMPLATES v1  (unified wildcard prompts)

HOW IT NESTS
  prompt_master            -> picks one of 3 section orders
    prompt_style           -> photo / documentary / (rarely) stylized medium
    prompt_char_physical   -> anchored (ethnic line supplies skin/hair/eye basics) OR independent (weighted colour files)
      prompt_char_identity_anchored | prompt_char_identity_independent
      prompt_char_face / _hair / _skin / _body / _details
    prompt_wardrobe        -> clothing_pool (95% clothing_everyday_female, 5% clothing_full_female) + optional accessories
    prompt_pose_expression -> pose_* / facialExpressionsFor_v10 / poses_female / poses
    prompt_setting         -> settings10000 (80%) or env_* (20%)
    prompt_camera_light    -> cam_* + lite_*
  prompt_master_short + prompt_char_physical_short: compact versions (~120 words) for CLIP-limited models.

CONVENTIONS
  * Files of noun phrases (head_*, eye_*, hair_*, body_* ...) are placed mid-sentence:  "Her jaw is __head_jaw__".
  * OPTIONAL-trait files are sentence-ready ("She has a ...") so a blank line prints nothing: opt_unique, opt_tattoo, health_conditions.
  * {text __file__|||} = inline optional: 1 chance in 4 that the text appears (N pipes = 1 in N+1).
  * Nested wildcard lines (clothing_pool.txt) give weighted mixing without tool-specific weight syntax.
  * "woman"/"her" are hard-coded: every body, clothing and pose file is currently female. A dem_gender file needs male/neutral file sets first.
  * Anatomy-specific files (body_breasts, body_nipples, body_ass_female, body_labia ...) are intentionally NOT referenced here.

REQUIRES your existing wildcard files (109 are referenced). Works best with the pilot_v2 weighted files, but runs without.
tools/expand.py : test expander. Example:  python tools/expand.py wildcards <your_wildcard_folder> -- prompt_master 3 42
