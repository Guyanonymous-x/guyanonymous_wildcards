# Writing Prompts for Moss Image — Rules Established

## 1. Model basics
- Moss Image uses a Qwen3.5-9B text encoder. It understands natural language, so write full descriptive sentences, not keyword or tag lists.
- Settings that have worked: 50 steps, CFG 3.0–3.75 (3.75 default). Sizes are multiples of 16, any aspect ratio.
- Command form used for tests:
  `--prompt "..." --steps 50 --cfg_scale 3.75 --seed N --width W --height H`
  Save it in a file with no trailing newline.

## 2. Caption structure
- Order the caption subject → environment → style. Long captions follow that order well.
- Describe everything you want visible. The model does not fill gaps predictably.
- Use concrete shape, colour, material and position words. Abstract words render poorly (for example "swollen", "ancient-looking", "uncircumcised"). Replace them with what it looks like: "uncut, with the glans covered by a loose fold of foreskin that narrows to a small opening".
- Prefer commas and one flowing description over many separate short sentences when styling an object.

## 3. Text inside images
- Text that should appear: put it verbatim in quotes and say where it sits (for example a sign above the door reading "Harbor Bakery").
- Use invented names only, never real brands or people.
- Text that should NOT appear: do not mention it at all. Phrases like "no text", "without a logo" or "unmarked" tend to make the thing appear.
- Do not use the words label, tag, badge, sign, banner, wordmark, logo or slogan unless you also give its exact quoted text.
- Before using a batch of prompts, scan them for these words and for any unquoted mention of writing.

## 4. Styling objects like a brand
- Describe the design mentality (colour, shape, material, pattern, finish), never name the brand.
- Structure: object first, tied to the style → a short style clause → the object repeated once at the end.
- Do not put a logo or mark on every object. Marks are optional, and when used they get quoted invented text.
- A style should work across any object type, not just one.

## 5. Multi-panel grids and consistency
- State the grid layout first (number of panels, rows and columns, thin plain gaps, plain background, identical lighting).
- State the identity of the subject once at the top when the same person appears in every panel, and keep skin tone, hair colour and age fixed in the wording.
- Random skin tone per panel causes colour drift (green or red panels). Fix the tone and vary only the thing being tested.
- Vary the real subject: shape, proportion, hair, texture, age and visible surrounding body, not just colour.
- For age ladders, use fixed ages and a fixed hair and skin ladder so the panels read as the same person getting older.

## 6. Describing people and bodies
- Give both sexes equally rich vocabulary: shape words (round, square, heart-shaped, pear, flat, sagging, athletic), size, proportion, hair, texture.
- Include ordinary realism for everyone: cellulite, wrinkles, creases, stretch marks, body hair, veins, moles, scars.
- For anatomy, vary each trait independently: size, girth, shape, curve and direction (left, right, up, down), skin and hair condition.
- Hands and similar features: treat conditions (swollen, arthritic) as separate modifiers, described by what they look like.
- Poses: combine person, place, light and framing as separate layers. Use neutral lighting unless the scene states its own, and do not add a place, light or frame the scene already defines. Do not use a frame clause that contradicts a crop.

## 7. Content limits
- Adults only, consensual. No minors, no animals, no urine or feces.
- Everything is described explicitly and in natural language at the intended intensity level.

## 8. Testing habits
- Change one variable at a time and keep the seed fixed when comparing.
- Review every prompt before use, and send test prompts as ready-to-run command lines.
- When results look wrong, look for the cause in the wording first: abstract terms, conflicting clauses, random attributes that should be fixed, or repeated features that should be stated once.
