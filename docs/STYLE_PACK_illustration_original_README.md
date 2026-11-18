# Illustration style wildcards (flat)

Everything is in this one folder. There are no subfolders.
The pack was built from a taxonomy tested against 1,757 illustrators across 110 genres, plus children's art by age and ability.

- `illustration_<category>_<variable>.txt`: 179 wildcard files with 1,519 values, one per line.
  Call one as `__illustration_<category>_<variable>__`, e.g. `__illustration_color_saturation__`.
- `illustration_childart_*.txt`: children's art by developmental stage (toddler to teen), ability level, conventions and tools.
- `illustration_subject.txt`: 20 sample subjects. Replace `__illustration_subject__` with your own subject.
- `illustration_presets_stress_test_styles.txt`: 31 full style recipes.
- `illustration_presets_signature_devices.txt`: 229 signature devices ("uniquely theirs" traits, no artist names).
- `prompt_*.txt`: 35 prompts. Paste one into your prompt box. Each prompt is also a wildcard, e.g. `__prompt_01_core__`.
- `expand_prompt.py`: prints plain-text versions for tools without wildcard support:
  `python expand_prompt.py prompt_01_core.txt 10`
- `build_wildcards.py`: regenerates the folder. Edit its lists or its GLOSS dictionary, then run it.

## Written for Krea 2 and other LLM-encoder models
Krea 2 reads prompts with a Qwen3-VL language model and truncates at 512 tokens.
The values are written for that:

- **Jargon is glossed in place.** About 250 specialist terms keep their name and add a plain visual description,
  for example "pochoir, crisp hand-stenciled flat watercolor layers" or "Wimmelbuch, a wordless busy picture book teeming with tiny people".
- **No parentheses or brackets.** In ComfyUI and A1111 these change prompt weighting.
- **Length-checked.** Every prompt fits under 512 tokens when expanded (an estimate, since the real tokenizer couldn't be downloaded),
  except `prompt_00_master_all_variables` (~1,300 tokens), which is kept as a reference.
  For Krea 2, use the seven `prompt_00a`–`00g` master parts, which split the same variables into chunks of 170–330 tokens.

## Syntax (Dynamic Prompts)
`__name__` picks one random line from that file · `{a|b}` picks one option · `{8$$, $$a|b|...}` picks 8 options joined by ", ".
ComfyUI Impact Pack supports `__name__` and `{a|b}`, but not the `N$$` form.

## Install
Copy this folder's .txt files into your wildcards folder,
for example `extensions/sd-dynamic-prompts/wildcards/` or ComfyUI's wildcards folder.

## Prompts
| File | What it does | Approx. tokens |
| --- | --- | --- |
| prompt_00_master_all_variables | Every variable. Reference only; too long for Krea 2 | ~1,300 |
| prompt_00a–00g_master_part_* | The master split into 7 parts | 170–330 |
| prompt_01_core | The ~25 variables that matter most. Start here | ~170 |
| prompt_02–16_focus_<category> | Core plus every variable in one category | 190–350 |
| prompt_17–20_spectrum_* | Realistic/hyperdetailed, surreal/insane, abstract, minimal/boring | 80–135 |
| prompt_21/22_random_8/16 | 8 or 16 random variables | 65–165 |
| prompt_23_preset_styles | One of 31 recipes | 45–90 |
| prompt_24_genre_plus_signatures | A genre (69 options) plus two signature devices | 70–95 |
| prompt_25_genre_core | A genre plus the core variables | ~175 |
| prompt_26_child_art | A child's drawing: stage, ability and tool | ~60 |
| prompt_27_child_art_by_stage | Nine complete age stages, 2 to 15, each with matching conventions and tools | ~70 |

## Tips
- Fully random combinations often clash. To lock a style, replace wildcards with literal values, and leave wildcards only where you want variation.
- Put the subject first.
- For child-art prompts, keep other style wildcards out; a "photorealistic" slot will fight a crayon drawing.
