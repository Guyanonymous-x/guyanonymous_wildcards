# guyanonymous_wildcards

A slightly extensive wildcard system for generating text prompts for txt2img generation, written in plain sentences for natural-language models such as Krea 2 and Moss Image.

**Current version: v104**

**Contents:** [Introduction](#introduction) · [What's New in v104](#whats-new-in-v104) · [Features](#features) · [Getting Started](#getting-started) · [Using the Features](#using-the-features) · [Full Changelog](#full-changelog)

## Introduction

Guyanonymous' Wildcards is a library of about 41,600 wildcard text files (41585 `.txt` files in [`wildcards/`](wildcards/) at v104, plus 1280 build and check files in [`wildcards/_tools/`](wildcards/_tools/)). Each file holds one option per line. When a prompt says `__name__`, your image tool replaces it with a random line from `name.txt`. Many files refer to other files, so one reference can build a whole description: a person, an outfit, a room, an animal, a vehicle, a street sign, a book cover and so on.

The library is for people who make images with text-to-image tools and want varied, detailed prompts that still make sense. Lines are full descriptive sentences, not tag lists. There are no emphasis weights, LoRA tags or negative prompts. That is why it suits natural-language models such as Krea 2 and MOSS-Image. The docs also cover tag-style and token-limited models (see [Model-specific guidance](#model-specific-guidance)).

People files describe adults aged 18 to 120. Some families are adult-themed: clinical anatomy descriptions, adult accessories, chastity devices and a "bad taste" set. These sit in their own files and the default person templates do not call them, so you only get them if you reference them yourself. Real brand names appear only in the `maker_*` files. All other names (authors, shops, brands, teams, people) are invented.

Each release gets a `release/vNN` branch (v74 is the first version tracked in git; each release also updates this README). Release zips and the "All Options Once" export are built from this tree and are not stored here.

## What's New in v104

Penis stages and modifiers, physical fluid wording, masturbation by level and beauty and grooming objects ([docs/INDEX_v104.txt](docs/INDEX_v104.txt), research notes in [docs/RESEARCH_v104.txt](docs/RESEARCH_v104.txt)). Since v103 it adds:

- Penis stages: semi-erect and just-after-ejaculation forms, plus a separate circumcision modifier with physical foreskin wording and independent length, girth, shape, curve and lean pools.
- Ejaculation modifier (look, amount, after) and squirting described physically with single-stream and spray forms; structured scenes that keep every body part tied to its owner.
- Pubic hair stubble, patchy and shaved shapes; masturbation pools for levels 1 to 6.
- New Beauty and Grooming section: female and male hygiene, grooming, beauty and unisex care objects, about 575 descriptions.
- **Showcase and sample files:** the showcase files (40 prompts at 1024 and 1408 sizes, plus a key file) highlight what is new or changed in this version, while the 100 sample prompts are representative of everything the model can do. Both are in [docs/showcase/](docs/showcase/), built by `_tools/v104_showcase.py`.

The full list of v104 entry points is in `wildcards/v104_entry_points.txt`.

## What's New in v103

Adult poses now describe distinct people, places and light, and the age pools and hand and pubic hair wildcards are improved. ([docs/INDEX_v103.txt](docs/INDEX_v103.txt), research notes in [docs/RESEARCH_v103.txt](docs/RESEARCH_v103.txt)). Since v102 it adds:

- Adult poses get a person layer (`__adult_l1_pose_person__` to `__adult_l6_pose_person__`; 1,600 women and 1,600 men with age, heritage, skin, build and hair) and a scene layer (`__adult_l1_pose_scene__` to `__adult_l6_pose_scene__`) with place, light and framing.
- Vague device phrases were rewritten as concrete shapes and colours.
- Age pools cleaned of wrong-age entries; new graded ladders `__age_step1_body_skin__` to `__age_step9_body_skin__` and `__age_step1_hand_skin__` to `__age_step9_hand_skin__`.
- Hand joint conditions are an optional modifier (`__hand_condition_mild__`, `__hand_condition_marked__`); the base hand pools no longer say swollen or arthritic.
- Pubic hair: new stubble and patchy pools, a `__pubic_hair_shape__` modifier (heart, arrow, line, triangle and more), and `__f_pubichair_all__` / `__m_pubichair_all__`.
- **Showcase:** 40 prompts at 1024 and 1408 sizes, a key file and 100 sample prompts in [docs/showcase/](docs/showcase/), built by `_tools/v103_showcase.py`.

The full list of v103 entry points is in `wildcards/v103_entry_points.txt`.

## Features

- **Large drop-in library.** One flat folder of 32,712 `.txt` files using the common `__name__` wildcard syntax. You need no Python to use it.
- **Women and men in one folder.** `f_` files are female, `m_` files are male and unprefixed files are shared. `any_` files are gender-neutral (they/their). At v74 there are 1,466 `f_`, 1,457 `m_` and 1,246 `any_` files.
- **Character creation system (v42).** `f_create_random_woman`, `m_create_random_man`, `any_create_random_person` and fixed identities (trans, intersex, non-binary, androgynous, in transition). It has three age modes (realistic, mismatched, unlinked), clothing states (none, `_w_clothes`, `_nude`, `_topless`, `_bottomless`), `_short` versions and an optional `_traits` suffix.
- **Conditioned layers.** In the master prompts the age bracket is chosen first. Body type, hair type, clothing, accessories, mobility aids, settings and poses then follow from it:
  - age layer: 9 brackets, 18–24 to 95–120
  - body-type layer: 8 archetypes plus severely obese
  - hair-type layer: straight, wavy, curly, coily
  - age and body conditioned clothing
  - frequency-weighted eye, hair and skin files
  - the men's set: facial hair, baldness that rises with age, grooming
- **Prompt templates.** These are nested master prompts (`f_/m_prompt_master_by_age`, `_random_clothing`, `_short`) and ready-made entry points for people, groups, outfits, places, animals, objects and food.
- **Subject families.** Each has its own entry points:
  - groups and relationships
  - occasions
  - shoes
  - accessories and wardrobe
  - adult-only accessories
  - poses, settings and interactions
  - furniture and household objects
  - containers and liquids
  - rooms
  - food and tableware
  - animals (by class, behaviour and farm animals)
  - plants and landscapes
  - architecture (`arch_`, `bld_`)
  - vehicles (`veh_`, `vx_`, interiors, paint and damage)
  - 104 manufacturer styles
  - 120 jobs
  - hobbies, music and sport
  - 30 world regions of dress and culture
  - 24 city types
  - 31 fantasy, sci-fi and history worlds
  - visual effects and extreme weather
  - art media, product shots and packaging
  - condition and damage
  - expressions in three intensity tiers
  - depth and occlusion
  - reading matter, signage and ads
  - creatures and powers
  - paper and print collections
- **Framing pack (v57).** `frame_*` files wrap any subject in a clarity opener, a square 1:1 frame and a composition that keeps the subject whole.
- **Model profiles.** Usage notes for natural-language, tag-style and token-limited models, plus test notes for MOSS-Image.
- **Python tools (optional).** `wildcards/_tools/` holds builders that regenerate the weighted layers, a test expander, a reference checker, consistency and contradiction checkers, the All Options Once builder and a browser-based prompt viewer. They need Python 3.8+ and no extra packages.
- **Release editions.** Each release is built as flat and folder editions (the folder edition uses `__family/name__`). Each also comes as an "All Options Once" (not proportional) edition, where every option appears once. The zips are not stored in this repository.

## Getting Started

### Requirements

- **An image tool that supports `__name__` wildcards.** The docs say only "your image tool" or "your front end". They do not name one specific extension. Put the folder wherever your tool reads wildcard files. The library uses only plain `__name__` references. In the current library no file uses `{a|b}` inline choices, `N::` weight prefixes or tool-specific syntax, and `_tools/check_build.py` treats pipes outside `{a|b}` and `(word:1.5)` weights as errors. Your tool reads only `.txt` files, so it ignores `_tools/`.
- **A text-to-image model.** The library targets natural-language models (Krea 2, MOSS-Image and similar). The project's MOSS-Image tests ([docs/MOSS_IMAGE_NOTES.txt](docs/MOSS_IMAGE_NOTES.txt)) were run in Forge, and the notes say MOSS-Image also runs in ComfyUI 0.42.0+.
- **Python 3.8 or newer: optional.** You need it only to rebuild generated files or run the checkers ([docs/HOW_TO_RUN.txt](docs/HOW_TO_RUN.txt)). On Windows, tick "Add python.exe to PATH" when you install it.

### Install

1. Get the files. Either clone this repository (`git clone https://github.com/Guyanonymous-x/guyanonymous_wildcards`) or download it as a ZIP from GitHub. `main` always holds the latest version. Each release also has a `release/vNN` branch (for example `release/v74`), so older git-tracked versions can be recovered.
2. Copy the contents of `wildcards/` into your image tool's wildcards folder. If you are upgrading from a release before the men's set, replace your old female files: they were renamed with an `f_` prefix. [docs/RENAME_MAP_old_to_new.csv](docs/RENAME_MAP_old_to_new.csv) lists every old to new name.
3. Leave `docs/` wherever is convenient. It is reference material only.

### Your first prompt

From [docs/QUICK_START_v55.txt](docs/QUICK_START_v55.txt):

1. Write `__file_name__` in a prompt. The tool replaces it with one random line from that file.
2. Start with a ready-made prompt file:

   | Subject | Try |
   |---|---|
   | A person | `__any_person_age35_44_w_clothes__` (bands 18_24, 25_34 … 95_120) or `__f_prompt_master_by_age__` / `__m_prompt_master_by_age__` |
   | A group | `__group_prompt__` |
   | An outfit | `__occasion_wedding_guest_outfit_prompt__` |
   | A place | `__setting_prompt__`, `__room_living_room_prompt_brief__`, `__city_prompt__`, `__land_prompt__` |
   | An animal | `__animal_prompt__`, `__animal_dogs_prompt__`, `__animal_aquatic_salt_prompt__` |
   | An object | `__obj_kitchen_prompt__`, `__tool_prompt__`, `__veh_prompt__`, `__arch_prompt__` |
   | Food | `__food_prompt__`, `__food_dish_prompt__`, `__table_setting_prompt__` |
   | New in v74 | `__reading_prompt__`, `__signage_prompt__`, `__cb_prompt__`, `__bld_prompt__` |

3. Build your own line from parts, for example:
   `__any_person_age45_54_w_clothes__ __pose_prompt__ __setting_prompt__ __food_drink_prompt__`
4. Add your own style or LoRA tags and negative prompt outside these files. The library never writes them.
5. If your tool reports a missing file, check the name against the index files. Names are lower case with underscores.

## Using the Features

### Wildcard syntax

- `__name__` is replaced by one random line from `name.txt`. Lines may contain further `__name__` references, so templates nest.
- The folder edition (shipped since v56) groups files into family folders: people, clothing, accessories, body, pose_camera_style, places, groups, objects, animals, nature_buildings_vehicles, food_tableware and other. References there are written `__family/name__`, for example `__animals/animal_dogs_prompt__`. Use the flat edition (this repository) if your tool does not support folder paths.
- Text meant to appear in the image is inside double quotation marks. `_fill` files hold quoted placeholders for you to replace.
- Since v73, file names no longer contain double underscores (`acc_x_display__material` became `acc_x_display_material`). A `__name__` parser could read the old names as two references.

### Folder layout and naming

```
wildcards/          the library: one .txt per wildcard (flat)
wildcards/_tools/   Python build and check tools, data, source templates (ignored by image tools)
docs/               per-version notes, indexes, layer READMEs, model notes, samples, showcase
```

Naming rules, from [docs/FILE_NAMING.txt](docs/FILE_NAMING.txt):

| Prefix | Meaning |
|---|---|
| `f_<name>` | female file (she/her) |
| `m_<name>` | male file (he/his) |
| `<name>` (no prefix) | shared: identical for both genders |
| `any_<name>` | neutral file (they/their, no gendered words) |

- Every layer is built twice, once for women and once for men. A file is kept once under its plain name only if both builds are byte-identical and it refers only to shared files. Otherwise it becomes `f_` and `m_` files, and each one's references point at its own gender. A gendered file therefore never silently serves the wrong gender.
- **Women-only:** makeup (`f_make_*`), `f_hair_baby`, female anatomy and `f_outfit_dress_style`.
- **Men-only:** `m_grooming` (replaces makeup), `m_facial_hair`, male anatomy and `m_outfit_suit_style`.
- **Common suffixes:**
  - `_prompt`: a whole assembled description
  - `_short` / `_brief`: compact versions
  - `_full`: long versions
  - `_phrase`: for use inside other sentences
  - `_random`: a per-type assembly
  - `_names`: lists of names
  - `_frame_prompt`: framed versions (see the framing pack)
  - `_fill`: editable placeholder text
- **Family prefixes:** these follow each version's notes, for example `furn_`, `room_`, `animal_`, `ani2_`, `vx_`, `maker_`, `job_`, `act_`, `culture_`, `city_`, `world_`, `fx_`, `wx_`, `cond_`, `frame_`, `book_`, `sign_`, `bld_`, `cb_` and `pw_`. See [docs/INDEX_v74.txt](docs/INDEX_v74.txt), [docs/INDEX_v66.txt](docs/INDEX_v66.txt) and [docs/INDEX_v55.txt](docs/INDEX_v55.txt).

### Prompt templates

[docs/README_prompt_templates.txt](docs/README_prompt_templates.txt) explains how the master prompts nest:

```
prompt_master            -> picks one of 3 section orders
  prompt_style           -> photo / documentary / (rarely) stylized medium
  prompt_char_physical   -> anchored (ethnic line supplies skin/hair/eye basics) or independent
    prompt_char_identity_*, prompt_char_face / _hair / _skin / _body / _details
  prompt_wardrobe        -> clothing pool + optional accessories
  prompt_pose_expression -> pose_* / facial expressions / poses
  prompt_setting         -> settings or env_*
  prompt_camera_light    -> cam_* + lite_*
```

**Person entry points** (swap `f_` for `m_`):

| File | What you get |
|---|---|
| `f_prompt_master_by_age` | Character and clothing conditioned on age and body. **Recommended.** |
| `f_prompt_master_by_age_random_clothing` | Conditioned character with completely random clothing |
| `f_prompt_master_random_clothing` | Nothing conditioned, random clothing |
| `f_prompt_master` | Nothing conditioned, realistic everyday clothing |
| `f_prompt_master_short` | About 120 words, for CLIP-limited models |

You can also use your own big templates: `f_WOMANprompt` / `f_character_female_basic` and `m_MANprompt` / `m_character_male_basic`. All LoRA tags were removed from these in v43.

**Character creation names** ([docs/README_v42_people.txt](docs/README_v42_people.txt)) are built as prefix + `create_random_` + who + mode + clothing + length + traits:

- **Mode:**
  - none: realistic, age drives the look
  - `_mismatched`: looks 10–30 years older or younger than the stated age
  - `_unlinked`: the age is independent of every other trait
- **Clothing:** none, `_w_clothes`, `_nude`, `_topless`, `_bottomless`.
- **Length:** full, or `_short` (about a quarter of the length).
- **Examples:** `f_create_random_woman_w_clothes`, `m_create_random_man_nude_short`, `any_create_random_person_unlinked`, `m_create_random_trans_man_w_clothes_traits`.
- `any_create_random_person` picks the identity at random. Cis men and women are weighted 3, every other identity 1.
- Ages are stated as number + age word + visible ageing features, because models tend to render older people too young.

**Other people entry points:**

- `any_person_age<band>_w_clothes` (+ `_short`) gives one age band.
- `group_<relationship>` and `group_prompt` (with `_any_ages`, `_same_decade` and `_multigenerational` variants) give groups. Relationships include couple, parent_child, three_generations, siblings, friends, colleagues, team, mentor_mentee, classmates and neighbours.
- The older group set is `grp_prompt_master`, `grp_prompt_master_2`, `grp_prompt_master_3` and `grp_2_mm` … `grp_3_mww`.
- Demographic prompts are `demo_prompt_master`, `demo_prompt_master_balanced` and `demo_<identity>_<orientation>`.

**Person, setting and pose are separate (v46).** Person files describe only the person and object files only the object. You combine them yourself. Examples:

- `__any_create_random_person_short__ __pose_sitting_w_seat__ __setting_prompt__`
- `__any_create_random_person_w_clothes__ __pose_prompt__ __room_gym_prompt_full__`

**Objects built from parts (v49–v50).** `<family>_prompt` assembles one description from components: material, colour, finish, features and condition. Every part is its own file and can be used alone. For example, `__furn_bed_built__` is a whole bed and `__furn_bed_headboard_prompt__` is just the headboard. To fix one detail, use that part file and leave the rest random.

**Entry point lists.** Most versions from v38 to v74 have a `vNN_entry_points` file in the library (for example `v47_entry_points` and `v74_entry_points`), and v49 has `v49_families`. [docs/MODEL_GUIDE_v66.txt](docs/MODEL_GUIDE_v66.txt) groups the main entry points by subject.

### Layers

Each layer has its own README in `docs/`. Those READMEs use the women's base names, so add `f_` (or `m_` for men) in the combined folder.

- **Age layer** ([docs/README_age_layer.txt](docs/README_age_layer.txt)):
  - The age bracket is picked first, weighted by population share.
  - Every age-linked attribute is then drawn from that bracket's own files, named `age<lo>_<hi>_<attribute>`: skin, face, eyes, lips, hair colour and texture, body, muscles, hands, pose, tattoo and eyewear.
  - Each option's weight is its base weight times an age kernel ("up", "down", "peak" or "flat").
  - The brackets are 18–24, 25–34, 35–44, 45–54, 55–64, 65–74, 75–84, 85–94 and 95–120.
- **Body layer** ([docs/README_body_layer.txt](docs/README_body_layer.txt)):
  - The age bracket picks a body archetype: thin, slim, avg, athl, curvy, heavy, musc or frail, plus vheavy for severely obese (added in v3).
  - Every body slot then comes from that archetype's files, `bt_<archetype>_<y|m|o>_<attribute>`.
  - This removed clashes such as "heavily overweight" with "chiseled abs".
- **Hair layer** ([docs/README_hair_layer.txt](docs/README_hair_layer.txt)):
  - Hair type (S straight, W wavy, C curly, K coily) is chosen once per prompt.
  - The type feeds both the ethnic identity line (`countries_ethnic_prompts_S/W/C/K`) and the hair paragraph (`hair_curl_<T>`, `hairtex_<T>`, `hairvol_<T>`, `hairstyle_<T>`, with age-bracket versions).
- **Clothing layer** ([docs/README_clothing_layer.txt](docs/README_clothing_layer.txt)):
  - `outfit_*` attribute lists, `outfit_cosplay` (630 costumes for women, 567 for men) and `age<lo>_<hi>_clothing_<archetype>`, which follows both age and body type.
  - `f_/m_clothing_random_mix` is completely random clothing.
  - The age and body conditioned files exclude near-nude options. `clothing_full` keeps them.
- **Men's set** ([docs/README_men.txt](docs/README_men.txt)):
  - The same pipeline as for women, with men's population shares.
  - Male build and height lists.
  - `m_facial_hair`, which follows age. Since v72 it uses plain physical descriptions, and prompts read "His lower face has …".
  - Male-pattern baldness that rises with age.
  - A separate male hairstyle grammar.
  - `m_grooming`.
  - 1,480 names in `m_names`.
  - Men's clothing lists and 2,500 outfit lines in `m_clothing_full`.
- **People system (v42) and bodies (v43)** ([docs/README_v42_people.txt](docs/README_v42_people.txt), [docs/README_v43_bodies.txt](docs/README_v43_bodies.txt)):
  - The `create_` prompts, described above.
  - Teeth by age and by dental-care access (`teeth_access_high/_mid/_low`).
  - Novelty tattoos (`tattoo_temporary`, `tattoo_henna`, `tattoo_bad`).
  - Optional clinical anatomy files. The `create_` prompts leave these out; you add them yourself, for example `__f_create_random_woman_nude__ __f_body_vulva__`. Files marked MANUAL ONLY are never called by another file.
- **Shoes** ([docs/SHOES.txt](docs/SHOES.txt)):
  - Six quality tiers, shoe classes, materials, construction and prices.
  - The footwear files now use the accessory naming `acc_shoe_*`, with tier names basic, practical, standard, fine, luxury and showpiece (renamed by `_tools/shoe_rename.py`).
  - Start from `acc_shoe_prompt_master` or `acc_shoe_prompt`.
- **Manufacturer styles** ([docs/MAKERS_v70.txt](docs/MAKERS_v70.txt)): 104 makers, each with decade, style, genre, prompt, scene and person files.

### Weighted files

- Likelihood is set by **repeating lines**, not by tool-specific weight syntax ([docs/README_pilot_weighted.txt](docs/README_pilot_weighted.txt)). For example, `eye_color` has 2,500 lines, and common colours appear many more times than rare ones. Every original option is kept at least once.
- Nested pointer files give weighted mixing. For example, a clothing pool can be 95% everyday outfits and 5% the full list.
- "None" options are not blank lines. Since v42 they are short positive sentences in the same proportion, and since v73 some are single-space lines. Tools that strip blank lines therefore keep the intended odds.
- The shares (age brackets, body types, hair types, facial hair, baldness, eyewear) are rough estimates, not cited data.
- The rebuild writes audit CSVs listing every option's weight to `_tools/audit/`. That folder is not committed to git.
- If you want every option equally likely, use the **All Options Once** edition, built by `_tools/simple_build.py`. Every distinct option appears once there, gendered and age-specific files are merged, and it has simple `aoo_prompt_*` templates.

### The `_tools` scripts

You do not need any tool to *use* the wildcards. Run them from the wildcards folder with Python 3.8+. They take no required arguments. On Windows use `py _tools\name.py`; on Mac or Linux use `python3 _tools/name.py`.

| Script | What it does |
|---|---|
| `build_all.py` | Rebuilds the generated layers for both genders and merges them. Each gender is built in its own workspace (`_tools/work/f`, `_tools/work/m`). Files identical for both stay shared and the rest become `f_`/`m_`. It ends with a reference check and takes about 1–2 minutes. **Back up first:** it rewrites every generated file. Options: `--list`, `--only age,body`, `--from hair`, `--gender m`, or a folder path. |
| `expand.py` | Test expander. `expand.py m_prompt_master_by_age` gives 3 samples. `expand.py f_prompt_master_by_age 5 42` gives 5 samples with seed 42. `expand.py --check` verifies that every `__reference__` resolves. |
| `check_build.py` | Standing pre-release check. It covers references, forbidden symbols (curly quotes, dashes, LoRA tags, weights, stray colons), blank lines, pronoun-led sentences, contradictions and a bare-name report. `--fail` sets the exit code. |
| `check_consistency.py` | Expands entry points many times and flags rule clashes, such as night with day wording, snow with summer or flightless birds flying. Usage: `check_consistency.py 200 7`, plus `--fail`. |
| `v51_check.py`, `v42_contra.py` | Contradiction and grammar samplers for entry points and for the `create_` prompts. |
| `check_vocab.py` | Option counts, forbidden characters and sample resolved prompts. |
| `simple_build.py` | Builds the All Options Once package. |
| `sample_prompts.py`, `v74_showcase.py` | Sample and showcase prompt generators. |
| `prompt_viewer.html` | Open it in a browser and click "Load wildcards folder". Type a start file name and press Generate. The prompt design appears in the left pane and sample output in the right. |
| `vNN_build.py` / `vNN_data.py` / `vNN_meta.py` | The build stages for each version's families (v40 to v74). |
| `v71_build.py`, `v72_*.py`, `v73_*.py` | Post-build passes that must be re-run after any rebuild, in order (see below). Each one takes `--restore` to undo. |
| `extern/` | Builders and expanders for the illustration and photostyle style packs. |

**What to edit for what** ([docs/HOW_TO_RUN.txt](docs/HOW_TO_RUN.txt)). Run the step in brackets afterwards.

| To change | Edit | Then run |
|---|---|---|
| Likelihood weights | `_tools/pilot_body.py` | `--only weights` |
| Women's clothing vocabulary | `_tools/data/outfit_vocab.json` | `--only outfits` |
| Men's clothing vocabulary | `_tools/male_outfits.py` | `--only outfits` |
| Cosplay | `cosplay_data_a/b/c.py` (women), `cosplay_data_m1/m2/m3.py` (men) | `--only outfits` |
| Conditioned clothing | `clothing_build.py` (women), `clothing_cat_m.py` (men) | `--only clothing` |
| Age curves, baldness and beard graying | `age_model.py` | `--from age` |
| Body types and shares | `body_model.py` | `--from body` |
| Hair types and hairstyles | `hair_model.py` | `--from hair` |
| Prompt wording | `_tools/data/src_templates/*.tpl` (women), `src_templates_m/*.tpl` (men) | `--from templates` |

**Run order after any rebuild** ([docs/README_v73.txt](docs/README_v73.txt)). All of these can be run more than once safely:

```
python _tools/v71_build.py ; python _tools/v72_facial_hair.py ; python _tools/v72_scars.py ;
python _tools/v73_cleanup.py ; python _tools/v73_consistency.py ; python _tools/v73_expressions.py ;
python _tools/v73_depth.py ; python _tools/v73_chastity_belt.py ; python _tools/v73_anchor2.py ;
python _tools/v73_rename_dunder.py ; python _tools/check_build.py
```

Maintainer's local working folder: `D:\!!!!!!!Dave's Apps - Wildcards\Guyanonymous' Wildcards`.

### Model-specific guidance

From [docs/MODEL_NOTES_v55.txt](docs/MODEL_NOTES_v55.txt), [docs/MODEL_PROFILES_v57.txt](docs/MODEL_PROFILES_v57.txt), [docs/MODEL_GUIDE_v66.txt](docs/MODEL_GUIDE_v66.txt) and [docs/MOSS_IMAGE_NOTES.txt](docs/MOSS_IMAGE_NOTES.txt):

- **Natural-language models (Krea 2, MOSS and similar):**
  - Use the full `_prompt` / `_full` files, or `frame_prompt` / `frame_<kind>_prompt` as they are.
  - Put the setting and light after the subject.
  - Keep one subject per line.
  - For groups, keep the "First person … Second person …" order.
- **Tag-style or short-prompt models:**
  - Use `_short` / `_brief` files, or join single part files with commas.
  - Add one line from `frame_person_full` or `frame_product`.
- **Token-limited models (about 75 tokens):**
  - Use `_short` files and `frame_person_prompt_short` / `frame_person_age<N>_prompt`.
  - Full person prompts can run over 1,000 characters.
- **Models that read the first words most strongly:** put the main subject first.
- **Framing:**
  - `frame_ratio` is square 1:1. Edit it for other ratios.
  - Full-body lines ask for head to toe with a margin on every side. If a model still crops, repeat the line or use a `_short` prompt.
  - `frame_animal_quad_prompt` and `frame_feature_grid_prompt` make four-panel images.
- **MOSS-Image test notes** (single seeds, not conclusive):
  - **Model:** a 5B diffusion transformer with a Qwen3.5-9B text encoder. It accepts prompts up to about 4,000 tokens.
  - **Settings:** CFG 3.0 is usually enough for long prompts. 50 steps showed no visible loss compared with 80. 1024×1024 and 1408×1408 (1.98M pixels) sit inside the recommended 2M.
  - **Wording:** use positive wording. Negations such as "no readable lettering" did not help, and words like "banner" invite lettering. Put text to render in quotation marks.
  - **Groups:** ordinal and position anchors bind outfits and actions to the right person, and an explicit count line held the people count. Skin tone can drift between scenes.
- **Known limits:** about 0.5% of random person prompts mix age words with build or hair words that do not fit. Re-roll those.
- **Krea 2:** the docs do not give model-specific settings, beyond listing it as a natural-language model.

## Full Changelog

Summarised from the notes in [docs/](docs/), newest first. Dates are shown only where the notes give one. All git commit dates (2026-11-04) are import dates, not release dates.

### v104
Penis stages (semi-erect and post-ejaculation), circumcision as a separate modifier, physical wording for ejaculation and squirting, masturbation by level, and a Beauty and Grooming object section. See [What's New in v104](#whats-new-in-v104).

### v103
v103: adult poses with people, places and light; age ladders and cleaner age pools; hand-condition and pubic-hair modifiers. See [What's New in v104](#whats-new-in-v104).

### v102
v102: commas inside object-first style text, randomised quiet motifs replace brand marks, extended marks. See [What's New in v104](#whats-new-in-v104).

### v101
v101: object-first brand styles, optional brand marks, object-neutral styles and samples of everything. See [What's New in v104](#whats-new-in-v104).

### v100
polish See [What's New in v104](#whats-new-in-v104).

### v99
brands of the past See [What's New in v104](#whats-new-in-v104).

### v98
unnamed brand cells, quoted badge text See [What's New in v104](#whats-new-in-v104).

### v97
library-wide text audit See [What's New in v104](#whats-new-in-v104).

### v96
positive text wording, no text denials See [What's New in v104](#whats-new-in-v104).

### v95
brand styles describe the object, no logos or brand names in prompts See [What's New in v104](#whats-new-in-v104).

### v94
fake name system, business cards, logos, caps and t-shirts See [What's New in v104](#whats-new-in-v104).

### v93
150 more image-checked brand styles, wider subjects, defined label text See [What's New in v104](#whats-new-in-v104).

### v92
object-only brand styles, 100 more brands See [What's New in v104](#whats-new-in-v104).

### v89
Vans, Converse, Land Rover product-neutral See [What's New in v104](#whats-new-in-v104).

### v88
25 more image-checked brand styles See [What's New in v104](#whats-new-in-v104).

### v87
male wrestling, brand fixes, deduplicated badges, lighting fit See [What's New in v104](#whats-new-in-v104).

### v86
pinback buttons, insignia, adult achievements, kilts, pony, torn clothing See [What's New in v104](#whats-new-in-v104).

### v85
v85: adult L6, modifiers, messy, wrestling, gear, kilts and tailoring, top brands image-checked See [What's New in v104](#whats-new-in-v104).

### v85
v85: adult L6, modifiers (scene-neutral), messy, wrestling, gear, kilts and tailoring, top brands image-checked See [What's New in v104](#whats-new-in-v104).

### v84
v84: adult levels and adult_ prefix, brand styles as design essence (style-only plus _named) See [What's New in v104](#whats-new-in-v104).

### v83
v83: 746 global brand styles across all eras and regions; richer illustration and photography style lists (59 files) See [What's New in v104](#whats-new-in-v104).

### v82
v82: art forms that are neither illustration nor photography: sculpture, craft, fibre and render/installation (96 forms, 1,158 files) See [What's New in v104](#whats-new-in-v104).

### v81
v81: robots (25 types), gadgets and tech devices (42 types) and maker reference files (801 new files) See [What's New in v104](#whats-new-in-v104).

### v80
v80: treasure, card, mineral, sound, screen, art and nature collections (571 new files) See [What's New in v104](#whats-new-in-v104).

### v79
Noir (`nr_`), pirate (`pt_`) and spy (`sy_`) genres, money (`mo_`) and metalware (`mt_`) collections, full descriptions for named e-reader and phone models, and screen text given in quotation marks. See [What's New in v104](#whats-new-in-v104).

### v78
Cyberpunk (`cy_`), steampunk (`sp_`) and western (`we_`) genres, steampunk phones (`spp_`) and home and decorative collections (`hd_`). See [What's New in v104](#whats-new-in-v104).

### v77
Fantasy (`fa_`), horror (`ho_`), people interacting (`pi_`), toys (`toy_`) and die-cast models (`dc_`). See [What's New in v104](#whats-new-in-v104).

### v76
Science fiction (`sf_`), e-reader and phone timelines, and eight timekeeping and instrument collections (`col_`). Showcase prompts and sample prompts in `docs/showcase/`. See [What's New in v76](#whats-new-in-v76).

### v75
Legendary creatures (`leg_`), sacred figure archetypes, the pilot conversion of 325 Location Inventory records (`loc_`) with tag indexes and anywhere pools, and 66 object builders (`ob_`). Showcase prompts and sample prompts for the release are in `docs/showcase/`. See [What's New in v76](#whats-new-in-v76).

### v74
"Foundation release": reading matter, signage and lettering engine, ads and labelled containers, vehicle interiors (`vint2_`), architecture upgrade (`bld_`), creature body-plan and hybrid builders, powers, paper and print collections, and `_fill` placeholder files. Also the showcase prompts and the first git-tracked version. See [What's New in v76](#whats-new-in-v76).

### v73 (2026-11-03)
- **Expression intensity tiers:** 68 emotions × mild, strong and extreme, each described physically. `facialExpressionsFor_v10` and `pose_emotion` were rebuilt, and `expr_mild` / `expr_strong` / `expr_extreme` were added.
- **Consistency pass:**
  - City time and weather are drawn as consistent pairs.
  - Penguins and flightless birds got their own groups and never fly.
  - Clothing condition prompts no longer carry their own wear state.
  - The new `check_consistency.py` went from 182 flags to 0–1 per run.
- **Depth and occlusion family:** `depth_*`, `depth_prompt`.
- **Anchoring phase 2:** 6,568 lines in 448 person piece files now start with "The woman's", "The man's" or "The person's".
- **Cleanup:** 272 double-underscore file names were renamed. Blank padding became single-space lines, curly quotes and dashes were removed, and a new `chastity_belt` group was added.
- **Tools:** `check_build.py` is the standing build check. `simple_build.py` now builds into a temporary folder and refuses to finish if the file count falls by more than 1%.

### v72 (applied 2026-11-03)
- **Facial hair:** all 303 lines in `m_facial_hair` and the age files were rewritten as plain descriptions of where hair grows and where skin is bare, after tests showed named beard styles are weak. Person templates now say "His/Their lower face has …".
- **Scars:** the parametric scar lines in `mark_scars` and `skin_scars` became physical descriptions with colour, relief and length.
- Released together with the v71 anchor pass.

### v71 (2026-11-03)
No separate notes file. The anchor pass is described in README_v72:
- furniture "It has…" chains were merged
- room openers use the room noun
- person templates became one chained sentence per person
- ageing summaries use "The man", "The woman" or "This person"

### v70
Manufacturer styles: 104 makers × decade, style, genre, prompt, scene and person files, plus the mixes `maker_style_any`, `maker_names` and `maker_decades`. Real brand names are used only in `maker_*`.

### v69
Vehicles:
- 157 genres (`vx_<genre>_*`)
- vehicle poses (`vs_*`)
- paint (`vpaint_*`)
- damage (`vdmg_*`, `vxd_*`)
- interiors (`vint_*`)
- entry points `vx_prompt` and `vxs_prompt`

### v68
Patch release with no new entry points:
- fixed condition part lists
- new `ani_sessile_*` family for jellyfish, corals and similar
- reworded `world_<name>_place_prompt`
- object condition prompts limited to hand and power tools

### v67
Visual and special effects in nine domains (`fx_*`), photographic effects (`fx_photo_*`) and extreme weather (`wx_*`) with sky, land, people, things, animals, plants and light parts.

### v66
Fantasy, sci-fi and history worlds: 31 worlds × dress, props, setting and action (`world_*`). Added [INDEX_v66.txt](docs/INDEX_v66.txt) and [MODEL_GUIDE_v66.txt](docs/MODEL_GUIDE_v66.txt).

### v65
Cities and public places: 24 city types × layout, surface, detail, activity and sign, plus shared style, time, weather and crowd files (`city_*`).

### v64
Hobbies, music and sport: per-activity clothes, equipment, setting and action (`act_*`).

### v63
Global dress and culture: 30 regions × garment, headwear, adornment, hair, setting, event and outfit (`culture_*`).

### v62
- **Art media:** `medium_*`.
- **Product shots and packaging:** `prod_*`, `pack_*`.
- **Signs:** `sign_*`.
- **Condition system:** `cond_<kind>_<family>_<strength>` for buildings, vehicles, furniture, clothing, objects, signs, books and statues, with `condition_*_prompt` entry points.

### v61
Animals 2:
- behaviour, group, young and detail pools for 18 families (`ani_*`, `ani2_*`)
- 14 farm animals (`farm_*`)
- `farm_person_prompt` and `pet_person_prompt`

### v60
Nature and landscapes: 28 landscape types in parts (`land_*`), flora by 8 biomes (`flora_*`), and shared season, time, sky and water files.

### v59
Professions and roles: 120 jobs × outfit, tool, workplace and action (`job_*`), grouped by sector.

### v58
- Outerwear and accessories built from parts: `wear_*`, 58 types across outerwear, hats, bags, scarves, gloves and belts.
- `frame_animal_quad_prompt` rewritten.

### v57
Framing and clarity pack: `frame_*` files and entry points, plus [MODEL_PROFILES_v57.txt](docs/MODEL_PROFILES_v57.txt).

### v56
- **Grammar pass:** a/an corrected in 4,093 lines across 712 files.
- **First folder edition:** 12 family folders, with references written `__family/name__`.

### v55
- **Food:** `food_*` for cheese, fruit, vegetable, bread, dessert, dish, drink and snack.
- **Tableware:** `ware_*`.
- **Table settings:** `table_*`, `meal_prompt`.
- **Docs:** added [INDEX_v55.txt](docs/INDEX_v55.txt), [QUICK_START_v55.txt](docs/QUICK_START_v55.txt) and [MODEL_NOTES_v55.txt](docs/MODEL_NOTES_v55.txt).

### v54
- **Animals:** 36 classes, insects, and salt and fresh water animals (`animal_*`).
- **Nature:** plants and `nature_prompt`.
- **Buildings:** 9 building types (`arch_*`).
- **Vehicles:** 12 vehicle types (`veh_*`, `machinery_prompt`).

### v53
- **Wardrobe by occasion:** 20 occasions × parts (`occasion_*`).
- **Bad-taste set:** clothing, tattoos and jewellery in ugly, tacky, crude and gross variants (`badtaste_*`).
- **New rule:** item descriptions no longer contain `: `.

### v52
- **Groups and relationships:** `group_<relationship>` with age-gap modes.
- **One age band per prompt:** `any_person_age<bracket>_w_clothes`.
- **Consistent settings:** `setting_exterior`, plus hot and cold variants. Everyone is 18 to 120.

### v51
- **Prompt-quality checker:** `v51_check.py`.
- **Build pass:** `v51_build.py` removes repeated words, fixes a/an and removes baldness/styled-hair clashes.
- **Tool assemblies:** `tool_<trade>_random` / `_phrase`.
- **Room wording fixes.**

### v50
Furniture and appliances built from parts (`furn_<item>_built`, `furn_<item>_<part>`), matching bed boards, shared part materials and group mix phrases.

### v49
Random assembly for every new object family: `<family>_prompt` / `_random` / `_phrase`, built from shared `comp_*` components, covering 89 families.

### v48
Rooms and locations: 35 room types (`room_<type>_prompt_brief` / `_full`), room modifiers and `gear_*` files. Rooms describe the space only.

### v47
Furniture, household and office objects, containers (bottles, closures, perfume) and liquids (`furn_*`, `home_*`, `bottle_*`, `liquid_*`).

### v46
Setting, pose and interaction were split into separate files:
- poses with and without supports
- seats, surfaces and lean supports
- two- and three-person interactions
- place/light/weather settings

### v45
Adult-only accessories, each described as an object only:
- chastity devices split by anatomy
- merkins and pasties
- adult toys

### v44
Accessories and wardrobe:
- eyewear and wraps
- wearable tech (retro to far future)
- pins and patches
- earrings
- plastic and novelty ranges
- costume teeth
- balls and sport equipment
- garment-fit files

### v43
- **LoRA tags removed** from all files.
- **Clinical anatomy files:** optional, never called by the `create_` prompts.
- **Teeth:** follow age and dental-care access.
- **Novelty tattoos:** temporary, henna and badly done.

### v42
- **Character creation system:** the `create_random_*` names, identities, age modes, clothing states and `_short`.
- **Weights to wording:** emphasis weights became plain wording.
- **Blank lines:** blank "none" lines became positive sentences.
- **Hair:** bald styles were separated from other hairstyles.
- **Checker:** a contradiction checker (`v42_contra.py`) cut the flag rate from 20–28% to about 3–7%.

### v4–v41
No release notes exist in `docs/`. (`_tools/NEXT_ROUND.txt` mentions some v38–v41 work items, and `_tools/` has build scripts from v40 and v41.)

### v3
From [README_v3_changes.txt](docs/README_v3_changes.txt):
- **Eyewear:** 5,000-line eyewear files with age-based shares.
- **Ages and bodies:** 9 age brackets and a "severely obese" body type.
- **Objects:** new `obj_*` objects; rubber ducks reduced.
- **Groups:** groups of 2 and 3 (`grp_*`).
- **Demographics:** demographic identity files (`demo_*`).
- **Shoes:** the shoe system (`shoe_*`, now `acc_shoe_*`).
- **Age and body conditioning:** accessories, aids, settings and poses now follow age and body type.
- **Wording fixes:** colour-neutral skin modifiers, and plain-word hair curls replacing the 1A–4C codes.
- **Viewer:** `prompt_viewer.html`.

### Undated foundation builds (before the numbered notes)
[CHANGELOG_cleanup.txt](docs/CHANGELOG_cleanup.txt) and the layer READMEs record the early builds:
- **Cleanup:** removed ages under 18, and removed child and gender nouns from the ethnic lines.
- **Weighting and templates:** the frequency-weighted pilot and the unified prompt templates.
- **Layers:** the age, body-type, hair and clothing layers.
- **Men's build:** added male files, with female files renamed `f_` and shared files kept plain (see [RENAME_MAP_old_to_new.csv](docs/RENAME_MAP_old_to_new.csv)).
- **Tools:** moved into `wildcards/_tools` with `build_all.py`.

## Credits

Guyanonymous' Wildcards by Guyanonymous. The repository includes no license file.
