# Photographic Style Wildcards for Krea 2

A wildcard library of about 4,400 entries that breaks the work of hundreds of history's most renowned photographers into reusable, name-free style descriptions. Combine the pieces to rebuild a recognizable sensibility, or recombine them into styles no single photographer ever made.

No photographer names appear anywhere. Every entry describes **what the photograph looks like and how it was made**, which is what a natural-language model like Krea 2 responds to.

All files live in one folder and every filename starts with `photostyle_`, so the set can sit alongside other wildcard files without clashing.

---

## File groups

The filename after `photostyle_` tells you what the file is:

| Prefix | Role | Files |
|---|---|---|
| `photostyle_master` | Entry point, picks a random mode | `photostyle_master.txt` |
| `photostyle_mode_` | Full prompt templates, 3–5 phrasing variants each | `atomic_bw`, `atomic_color`, `people_scene`, `signature_pure`, `signature_override`, `signature_hybrid`, `chaos` |
| `photostyle_sig_` | 500 anonymized whole-style descriptions, 50 per genre | `street`, `documentary`, `portrait`, `fashion`, `landscape`, `fine_art`, `new_color`, `early_modernist`, `still_life_architecture`, `global`, plus `all` (draws from every genre) |
| `photostyle_subj_` | Subjects | `people`, `places`, `objects`; `photostyle_subject` picks among them |
| `photostyle_gear` | Camera + lens (+ filter) slot to append to any prompt | `photostyle_gear.txt` |
| *(no sub-prefix)* | Atomic style traits, one decision per file | listed below |

### Atomic traits

| Pillar | Files (all `photostyle_…`) |
|---|---|
| **Purpose** (what the image is for) | `purpose` |
| **Gear** | `camera`, `lens`, `lens_filter` |
| **Attraction** (what draws them) | `intent`, plus the `subj_` files |
| **Organisation** (how the frame is built) | `composition`, `placement`, `viewpoint`, `distance`, `visual_strategy`, `staging`, `props`, `gesture` |
| **Experience** (how it should feel) | `lighting`, `atmosphere`, `exposure_key`, `tonality_bw`, `color_palette`, `mood`, `motion`, `focus_dof`, `era` |
| **Treatment** (process, edit, presentation) | `process_bw`, `process_color`, `editing`, `grain_texture`, `artifacts`, `polish`, `finish` |

Each line is a self-contained phrase that slots into a sentence, so any line can be swapped for any other line from the same file.

**`photostyle_purpose`** completes the sentence *"The image should …"*. It covers how the viewer should feel ("make the viewer feel small before the scale of the world"), what they should notice first ("draw the eye first to the hands"), what they should want to do or think ("make the viewer want to visit this place"), and what kind of image it should feel like ("feel like evidence"). Every mode includes it. Use it on its own like this: `The image should __photostyle_purpose__.`

### Entry counts

| File | Entries | File | Entries |
|---|---|---|---|
| lighting | 202 | subj_people | 402 |
| color_palette | 166 | subj_places | 373 |
| mood | 160 | subj_objects | 262 |
| gesture | 165 | props | 216 |
| purpose | 149 | intent | 145 |
| composition | 136 | lens | 106 |
| tonality_bw | 103 | camera | 102 |
| viewpoint | 97 | editing | 97 |
| atmosphere | 89 | finish | 80 |
| process_bw / process_color | 70 each | staging | 69 |
| era | 62 | motion | 60 |
| grain_texture | 58 | artifacts | 57 |
| lens_filter | 53 | visual_strategy | 52 |
| focus_dof | 51 | sig_* (×10) | 50 each |
| exposure_key / placement | 40 each | polish | 30 |
| distance | 25 | | |

Finite categories (distance, polish, placement, exposure key) are kept smaller on purpose: beyond that size the entries would only repeat each other.

### Modes

| Mode | What it does |
|---|---|
| `photostyle_mode_atomic_bw` | Builds a black-and-white style entirely from traits, every slot filled |
| `photostyle_mode_atomic_color` | Same for color, adds palette, editing and optional props |
| `photostyle_mode_people_scene` | People-centred; adds gesture, staging and era; flips between B&W and color |
| `photostyle_mode_signature_pure` | One signature style + subject + camera + lens |
| `photostyle_mode_signature_override` | One signature style with 2–3 of its traits randomly replaced |
| `photostyle_mode_signature_hybrid` | Two signature styles fused, plus new lighting and treatment |
| `photostyle_mode_chaos` | 4–8 random traits from anywhere, plus gear, process and purpose |

`photostyle_master.txt` weights these so hybrids and overrides (the most novel results) come up most often. Duplicate or delete lines in it to change the mix.

---

## Syntax

Standard Dynamic Prompts wildcard syntax:

| Syntax | Meaning |
|---|---|
| `__photostyle_lighting__` | Random line from `photostyle_lighting.txt` |
| `{a\|b\|c}` | Pick one |
| `{2$$a\|b\|c}` | Pick 2, joined with ", " |
| `{2-4$$; $$a\|b\|c\|d}` | Pick 2 to 4, joined with "; " |
| `{text\|}` | Include the text about half the time |

---

## Using it

**With a wildcard tool** (ComfyUI, Forge/A1111 Dynamic Prompts, etc.): drop the `photostyle_*.txt` files into your wildcard folder and use `__photostyle_master__` as the prompt.

**Standalone** (for pasting into Krea 2 directly): keep `photostyle_expand_prompts.py` in the same folder as the `.txt` files. Python 3, no dependencies. It ignores the other files in the folder.

```bash
python photostyle_expand_prompts.py -n 10
python photostyle_expand_prompts.py -n 5 -t "__photostyle_mode_signature_hybrid__"
python photostyle_expand_prompts.py -n 5 --subject "a lighthouse keeper on the stairs"
python photostyle_expand_prompts.py -n 100 --seed 42 -o prompts.txt
```

### Building your own prompts

```
A portrait of my grandmother in her garden. __photostyle_sig_portrait__. __photostyle_gear__
```

```
__photostyle_subj_places__, __photostyle_lighting__, __photostyle_color_palette__, __photostyle_composition__. __photostyle_gear__
```

Pin a genre by using one signature file instead of `all`, e.g. `__photostyle_sig_early_modernist__`.

---

## Tips for Krea 2

- **Labelled slots work well.** The templates use `Camera:`, `Lens:`, `Lighting:` labels, which keep long prompts parseable.
- **Contradictions are part of the design.** A pinhole camera with a 600mm lens, or a daguerreotype in neon, gives strange results. For coherent images use `signature_pure` or the `atomic` modes; for invention use `hybrid` and `chaos`.
- **Trim if results get muddy.** The signature and gear slots carry the most style weight; process, lighting and palette come next.
- **Seed for iteration.** Use `--seed` to reproduce a prompt you like, then swap one file at a time.

## Adding your own entries

One phrase per line; lines starting with `#` are ignored. Write phrases that fit after a label (e.g. after `Lighting:`), and avoid naming real people or brands. If you add a new file, start its name with `photostyle_`.
