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

## 9. Learnings from the v106 image tests
- Grids: 2x2 and 2x3 render reliably; 3x3 and 1x6 drop or duplicate panels. Wrap each panel in its own bracketed, self-contained description.
- Colours and props that are named are followed. Hands go into pockets when hand placement is not stated, so state hands and free arms.
- Two-person scenes: say "Both people in this panel are men" (or women), otherwise a man and woman appear. Facing poses need "Their torsos are turned toward each other and not toward the camera, and the camera sees them in three-quarter view from one side." Named positions fail unless the geometry is spelled out.
- Clothed bulges depend on fabric. Anatomy nouns with size or shape words (rounded, swell, prominent, subtle tent) are drawn as objects; use plain "bulge" or "outline showing through the fabric". Tight stretch fabric holds the penis flat against the belly and shows it from the front only; briefs outline it; a jockstrap is a modest close pouch no larger than a hand; medium fabric (linen, jeans) softens the outline; loose fabric needs a clear tent about a hand wide and a hand and a half long. Give length against the body (crotch seam to navel).
- Chin: a "deep cleft" splits the chin into two lobes and runs toward the lip, and even a shallow vertical groove looked like buttocks. Use a small shallow dimple low on the chin tip, outline unbroken.
- Feature showcases: one person per feature, close-up of only the part, subtle options (chin shapes) need clearly different shapes to show at all, and one quoted title per image gives readable text.

## 10. v107 learnings
- Body-part grids must say the person is completely nude in every panel; leaving clothing unstated or naming a t-shirt or underwear puts clothes on feature grids.
- Size ranges need numbers to show: areolas are written as a ladder from thumbnail-wide to about seven centimetres across.
- Face-shape grids: four mild sub-features per panel (shape; cheeks; jaw; chin) and "the same face in every panel" give six near-identical faces. Use one shape word plus a plain proportion clause ("clearly taller than it is wide", "almost as wide as it is tall", "narrows sharply to a small pointed chin") with a matching neck, and spread each grid across round, gaunt, heart, long, square and oval/triangular.
- Body-feature grid audit (v107): the same fix applies to eyes, nose, nose profile, lips, cheeks and jaw, and hands. Keep only the core phrase of each part, add one plain visual clause per class, and pick one panel per class. Never tell the model a changing attribute stays the same: eye grids must not say "same eye colour", and skin grids must not say "same skin colour". Hair-texture grids must name the texture (curly, coily, wavy, straight) in every panel. Pubic-hair panels must describe hair. Vulva grids must not repeat an inner-labia line.
- Eye grids: changing eye colour, lashes or adding makeup swamps the shape. Fix eye colour, lashes and bare lids in the header; vary only shape and lids (hooded, monolid, puffy under-eye bags, deep-set, downturned, upturned, large round).
- Leading each panel with the changing feature and stating the shared person once in the header makes differences far more visible than repeating ~90 words of "same person" text per panel.
- A gaunt face clause ages the person unless "still young, smooth young skin" is added.
- Small facial features (eyes, lashes, brows, nose, lips, teeth, ears, chin): 'tight close-up' plus hair and 'nude, plain background' gives whole faces. Use 'extreme close-up ... filling the whole panel edge to edge: the frame runs from X to Y', drop hair and nudity/background text for those grids.
- Full-length nude grids: the model covers the groin with clasped hands and smooths genitals away unless told: 'Both arms hang straight down at the sides... the groin fully uncovered. His penis and testicles hang clearly visible.' Nails/feet need dramatic types (stiletto red, bitten to the quick, clawed toes with bunion, cracked calluses), not short/medium/average.
