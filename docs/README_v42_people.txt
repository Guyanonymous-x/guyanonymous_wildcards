GUYANONYMOUS' WILDCARDS v42: CHARACTER CREATION SYSTEM AND CLEAN-UP

All people are adults (18-120). The create_ prompts describe the person (and clothing, if asked) only. They add no setting, lighting, pose or camera wording.
Use them as  __name__  in a prompt.

NAMES  (prefix + create_random_ + who + mode + clothing state + length + traits)
  prefix        f_  = woman files (she/her)      m_  = man files (he/his)      any_ = neutral files (they/their, no gendered words)
  who           f_create_random_woman   m_create_random_man   any_create_random_person
                fixed identities:  m_create_random_trans_man   f_create_random_trans_woman   m_create_random_intersex_man   f_create_random_intersex_woman
                                   any_create_random_intersex_person   any_create_random_nonbinary_person   any_create_random_androgynous_person
                                   any_create_random_person_in_transition_feminine / _masculine   any_create_random_nonbinary_person_leaning_feminine / _masculine
                any_create_random_person  picks the identity at random (cis men and women weighted 3, every other identity 1)
  mode          (none) = realistic: age drives the look (skin, hair, posture, body type)
                _mismatched = looks 10-30 years older or younger than the stated age, and the prompt says so
                _unlinked = the age number is independent of every other trait (a fit, smooth-skinned 100-year-old; a wrinkled 18-year-old)
  clothing      (none) = person only, no clothing mentioned     _w_clothes = wearing random clothing (age and body type conditioned in realistic mode)
                _nude   _topless (bare-chested, wearing random trousers/skirt/shorts)   _bottomless (wearing a random top, nothing below the waist)
  length        (none) = full description    _short = top-level pools only, about a quarter of the length (for token limits and groups)
  traits        _traits = adds scars / hormone-related traits for the trans, intersex and in-transition identities (files without _traits describe general appearance only)
  Examples:  f_create_random_woman_w_clothes   m_create_random_man_nude_short   any_create_random_person_unlinked   m_create_random_trans_man_w_clothes_traits
  Sexual orientation is never part of these prompts (the older demo_ files that mention it are unchanged and not used by the create_ files).
  any_create_random_person_base*  are the label-free neutral person blocks that the identity files use; they can be called directly too.

AGE
  Numbers alone are weak for most models (older people come out too young). Every create_ prompt states the age as number + age word + visible ageing features, scaled by bracket.
  Brackets 45-54 and older add a short closing line that repeats the ageing (age_closing_<bracket>). _short prompts keep an ageing sentence too.
  Frailty/size words were removed from the age wording so they no longer clash with body type; frailty now comes from the body type only.

OTHER CHANGES
  * Emphasis weights (word:1.5) were converted to plain wording in every file (attractiveness2 is now ordinary-looking ... strikingly attractive).
  * __f_health_conditions__ / __m_health_conditions__ were removed from the random-person templates. The files stay and can be called directly.
  * Blank lines used to make "none" likely (tattoo, eyewear, walking aids, ageing summary, unique features, extras in photo, health conditions, accessory trims/finishes) were replaced with a
    short positive sentence in the same proportion, so tools that strip blank lines keep the intended odds.
  * Openers: "The subject is a woman who is ..." became "A woman, 34 years old, ..." (and "A man", "This person"). Double articles ("an a"), ".." and double spaces were repaired.
  * "Label: text" in the garment piece descriptions ("Piece 1 (...): Front: ...") was rewritten as plain sentences.
  * Bald and shaved hairstyles are now separate templates, so a shaved head no longer gets a curl pattern or hair volume.
  * Hair and eye colours now come only from the colour files (the ethnic background phrases no longer name them).
  * Build words that implied height (petite, tiny, compact) were replaced so they no longer clash with the stature word.
  * Ageing text: a child-sized body wording and "doll-like" were replaced.

CONTRADICTION TEST  (_tools/v42_contra.py [count] [file names])
  Expands the prompts many times and checks for: old age with youthful skin, young age with elderly words, bald with a hairstyle, tall with short, thin with heavy, three hair colours, label colons,
  double articles, stray punctuation, gendered words in any_ output. Before this release 20-28% of realistic full prompts were flagged; after, about 3-7% (several of those hits are false positives).
  The realistic mode is checked on age rules; _mismatched and _unlinked skip the age rules on purpose.
