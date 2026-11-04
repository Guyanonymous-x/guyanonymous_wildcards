"""Extra options for two under-represented groups, added to the age-bracket and body-type layers (not to the plain source files):
   O2 = old age (65+), O3 = very old age (85+), H2 = obese (BMI 35-39), H3 = severely obese (BMI 40+).
   Wording is gender-neutral so the same list serves the female and male libraries."""
SUPP = {
 'body_build': {
  'O3': ["very aged shrunken frame, noticeably smaller than in youth", "bent, shrunken, spine-curved elderly build", "tiny frail bird-boned very old build", "extremely thin, loosely clothed, stooped ninety-year-old build"],
  'O2': ["aged softened build with a thickened middle and thinner limbs", "stooped older build with rounded shoulders", "stiff, slightly shrunken older build"],
  'H3': ["severely obese very large build with a wide, heavy body", "morbidly obese massive build, rounded in every direction", "very large heavy build with a broad body that fills the frame", "super-sized heavily obese build with deep soft folds"],
  'H2': ["obese large build with a wide soft body and thick limbs", "big, heavily built obese figure with a prominent belly", "very heavy rounded obese build", "obese pear- or apple-shaped build with soft broad hips and belly"]},
 'body_compos': {
  'O3': ["very low muscle and thin skin over a shrunken frame", "sarcopenic depleted muscle with loose skin"],
  'O2': ["age-softened muscle with a fat layer shifted to the middle"],
  'H3': ["extremely high body fat with deep soft layers across the whole body", "very high body fat and heavy soft mass on the torso, hips and thighs"],
  'H2': ["high body fat with soft thick layers across torso and limbs", "obese composition, heavy soft fat with some underlying muscle bulk"]},
 'body_ratio': {
  'O2': ["slightly shortened torso from age compression"], 'O3': ["markedly shortened, compressed torso with a curved upper back"],
  'H3': ["very wide waist exceeding the hips, heavy rounded torso"], 'H2': ["waist as wide as or wider than the hips, rounded torso"]},
 'body_proprtn': {
  'O3': ["shrunken stature with a relatively large head and long-looking arms"], 'O2': ["slightly stooped proportions with a shorter trunk"],
  'H3': ["very wide heavy torso with short-looking limbs", "massively broad trunk and thick limbs"], 'H2': ["wide heavy trunk with thick limbs"]},
 'body_bones': {
  'O3': ["osteoporotic, thin shrunken skeletal frame with a curved spine", "brittle small fragile skeleton showing through loose skin"],
  'O2': ["slightly shrunken skeletal frame, a little stooped"], 'H3': ["large heavy skeletal frame carrying a great deal of weight"], 'H2': ["broad heavy bone structure under soft padding"]},
 'musc_shldr': {
  'O3': ["rounded, hunched, very narrow aged shoulders with a dowager's hump"], 'O2': ["rounded drooping aged shoulders"],
  'H3': ["very broad soft sloping shoulders buried in flesh"], 'H2': ["broad soft rounded shoulders with a padded line"]},
 'musc_arms': {
  'O3': ["thin arms with loose, hanging skin and prominent veins and bones", "spindly arms with wrinkled papery skin"],
  'O2': ["softened aged arms with loose skin at the underarm"], 'H3': ["enormous soft arms with heavy hanging folds", "very thick heavy arms with deep creases at the elbows"], 'H2': ["thick heavy soft arms with hanging upper-arm flesh"]},
 'musc_chest': {
  'O3': ["sunken, narrow chest with visible ribs and loose skin"], 'O2': ["soft, flattened aged chest with loose skin"],
  'H3': ["very heavy soft chest that sags into the belly folds"], 'H2': ["full heavy soft chest merging into a large belly"]},
 'musc_abs': {
  'O3': ["slack hollow belly with loose, wrinkled skin"], 'O2': ["soft, protruding aged belly"],
  'H3': ["huge soft belly that hangs over the waistband in layered folds", "very large overhanging belly with deep skin folds"],
  'H2': ["large rounded protruding belly with a visible fold", "big soft belly that sits over the hips"]},
 'musc_hips': {
  'O3': ["narrow bony hips with loose skin"], 'O2': ["softened, flattened aged hips"], 'H3': ["very wide hips with heavy soft rolls and dimpled skin"], 'H2': ["wide soft hips with a rolled line"]},
 'musc_legs': {
  'O3': ["thin spindly legs with prominent knees and varicose veins"], 'O2': ["slightly thin legs with soft skin and visible veins"],
  'H3': ["massive thick legs with heavy soft folds at the knees"], 'H2': ["thick heavy legs with soft rounded thighs that touch"]},
 'musc_veins': {
  'O3': ["very thin translucent skin with prominent blue veins and age spots"], 'O2': ["visible veins under thin aged skin"],
  'H3': ["veins hidden beneath thick soft skin, with mottled redness on the lower legs"], 'H2': ["few visible veins beneath soft skin"]},
 'neck_length': {'O3': ["short bent neck pushed forward by a curved upper spine"], 'O2': ["neck slightly pushed forward"], 'H3': ["very short thick neck largely hidden by the chin and shoulders"], 'H2': ["short thick neck with a soft double chin"]},
 'neck_muscle': {'O3': ["slack neck with stringy visible cords"], 'O2': ["slackened neck muscles and visible cords"], 'H3': ["thick soft neck with no visible muscle"], 'H2': ["thick neck with soft padding over the muscle"]},
 'neck_clav': {'O3': ["sharp prominent collarbones in deep hollows"], 'O2': ["prominent collarbones with slight hollows"], 'H3': ["collarbones fully hidden by soft tissue"], 'H2': ["collarbones softened by padding"]},
 'neck_crease': {'O3': ["deep turkey-neck folds and loose vertical neck bands"], 'O2': ["horizontal neck creases and sagging skin"], 'H3': ["deep thick neck rolls and a heavy double chin"], 'H2': ["soft double chin and neck rolls"]},
 'head_cheek': {'O3': ["deeply hollow, sunken aged cheeks"], 'O2': ["slightly sunken cheeks with drooping jowls"], 'H3': ["very full round cheeks that merge with the jaw"], 'H2': ["full round soft cheeks"]},
 'head_jaw': {'O3': ["slack, collapsed jawline with heavy jowls"], 'O2': ["softening jawline with jowls"], 'H3': ["jawline lost in a heavy double or triple chin"], 'H2': ["soft jawline with a double chin"]},
 'head_temple': {'O3': ["deeply hollowed temples with visible veins"], 'O2': ["slightly hollowed temples"], 'H3': ["full, rounded temples"], 'H2': ["smooth full temples"]},
 'nose_crease': {'O3': ["deep nasolabial folds reaching the chin"], 'O2': ["deep nasolabial lines"], 'H3': ["deep creases in a full, rounded face"], 'H2': ["soft nasolabial folds in a full face"]},
 'skin_wrinkle': {'O3': ["thousands of fine wrinkles covering the whole face, with deep folds around the mouth and eyes", "heavily creased, papery skin with deep folds and furrows across the forehead"],
  'O2': ["deep, well-established wrinkles around the eyes, mouth and forehead"], 'H3': ["tight, smooth skin in the face stretched over fat, with creases at the neck"], 'H2': ["smoother-than-expected skin on a full face with fine creases"]},
 'skin_texture': {'O3': ["thin, crinkled tissue-paper skin that tears easily", "loose, wrinkled skin hanging in soft folds"], 'O2': ["thin, dry, lax skin with visible texture"],
  'H3': ["thick soft skin with dimpling and stretch marks", "skin stretched over folds with chafed areas"], 'H2': ["thick soft skin with visible dimpling"]},
 'skin_marks': {'O3': ["many large age spots and skin tags across face and hands", "dense liver spots and cherry angiomas"], 'O2': ["scattered age spots and a few skin tags"],
  'H3': ["stretch marks, darkened skin folds and rubbed red patches"], 'H2': ["stretch marks and darkened skin at the folds"]},
 'skin_glow': {'O3': ["dull, thin-looking skin that has lost some of its colour"], 'O2': ["dry, matte aged skin"], 'H3': ["flushed, slightly shiny skin from exertion"], 'H2': ["flushed, rosy skin with a soft sheen"]},
 'eye_lid': {'O3': ["heavy, drooping hooded eyelids that cover most of the upper lid"], 'O2': ["hooded upper lids and baggy under-eyes"], 'H3': ["puffy full lids with soft under-eye bags"], 'H2': ["full soft eyelids"]},
 'eye_brow': {'O3': ["very sparse thin white eyebrows"], 'O2': ["thinning grey eyebrows with stray long hairs"], 'H3': ["full brows above a rounded face"], 'H2': ["full natural brows"]},
 'eye_sclera': {'O3': ["yellowed, cloudy aged whites of the eyes with a pale arcus ring"], 'O2': ["slightly yellowed whites with a faint arcus ring"], 'H3': ["slightly bloodshot, tired whites"], 'H2': ["clear whites with a few veins"]},
 'lip_fullness': {'O3': ["thin, collapsed lips with vertical lines"], 'O2': ["thinning lips with fine vertical lines"], 'H3': ["full lips in a full round face"], 'H2': ["full soft lips"]},
 'lip_corners': {'O3': ["downturned, drooping mouth corners with deep folds"], 'O2': ["slightly downturned mouth corners"], 'H3': ["mouth corners softened by full cheeks"], 'H2': ["soft mouth corners"]},
 'lip_teeth': {'O3': ["few remaining teeth, mostly worn and yellowed", "full dentures with a slightly artificial look"], 'O2': ["worn, yellowed teeth with several gaps"], 'H3': ["slightly crowded teeth"], 'H2': ["slightly yellowed teeth"]},
 'lip_gums': {'O3': ["receded gums and exposed yellowed roots"], 'O2': ["receding gums"], 'H3': ["swollen gums"], 'H2': ["healthy pink gums"]},
 'hair_texture': {'O3': ["very fine, sparse, wispy white hair that lies flat"], 'O2': ["thin, coarse grey-white hair"], 'H3': ["thick coarse hair"], 'H2': ["thick, slightly coarse hair"]},
 'hair_volume': {'O3': ["very little hair, scalp clearly visible through wispy white strands"], 'O2': ["thinning hair with scalp showing"], 'H3': ["full volume"], 'H2': ["full volume"]},
 'hair_line': {'O3': ["hairline far back with a mostly bald crown"], 'O2': ["receded, thinning hairline"], 'H3': ["normal hairline"], 'H2': ["normal hairline"]},
 'hair_shine': {'O3': ["dull, dry chalk-white sheen"], 'O2': ["dull silver-grey sheen"], 'H3': ["slightly oily sheen"], 'H2': ["slightly oily sheen"]},
 'hand_fingers': {'O3': ["thin, bony, spotted, trembling fingers with crooked arthritic joints"], 'O2': ["knobby, slightly crooked fingers with prominent veins"], 'H3': ["short thick puffy fingers with dimpled knuckles"], 'H2': ["thick soft fingers with dimpled knuckles"]},
 'hand_knuckl': {'O3': ["large swollen arthritic knuckles"], 'O2': ["enlarged arthritic joints"], 'H3': ["dimples in place of knuckles"], 'H2': ["dimpled knuckles"]},
 'hand_nails': {'O3': ["thick yellow ridged brittle nails"], 'O2': ["ridged, brittle nails"], 'H3': ["short nails on thick fingers"], 'H2': ["short neat nails"]},
 'hand_feet': {'O3': ["swollen, bunioned, calloused feet with thick toenails"], 'O2': ["bunions and thick nails"], 'H3': ["swollen ankles and puffy feet"], 'H2': ["wide, puffy feet and thick ankles"]},
 'pose_twist': {'O3': ["tilted forward with a rounded upper back and bent knees"], 'O2': ["leaning slightly forward with rounded shoulders"], 'H3': ["body wide and stable, weight over the hips, hips slightly forward"], 'H2': ["slightly swayed, belly leading"]},
 'pose_weight': {'O3': ["leaning on a cane or walker for balance"], 'O2': ["weight on one leg with a hand on something steady"], 'H3': ["weight spread widely, resting against a firm support"], 'H2': ["feet planted wide, weight rocked slightly back"]},
 'body_height': {'O3': ["noticeably shorter than before from age-related spinal compression"], 'O2': ["slightly shortened by age and a bent upper back"], 'H3': ["of average height but looking small against a very large body"], 'H2': ["average height with a very heavy build"]},
}
FAT_OF = {'H3': 0.99, 'H2': 0.88}
def options(f):
    """[(option, tag)] for attribute file f"""
    return [(o, t) for t, os_ in SUPP.get(f, {}).items() for o in os_]
def spec_for_supp(tag, flat=('flat',)):
    return {'O3': ('up', 84, 6, 0.005, 3.5), 'O2': ('up', 68, 8, 0.01, 2.2)}.get(tag, flat)
