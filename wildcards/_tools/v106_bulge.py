"""v106 - clothed male bulges, written from the image tests.
Findings used: plain 'bulge' wording works; anatomy nouns with size/shape words ('rounded', 'swell', 'ball') are drawn as objects;
tight stretch fabric holds the penis flat against the body and shows it from the front only; medium fabric holds it partway and
softens the outline; loose fabric hangs straight and tents over and around an erect penis only (it needs a clear, not 'subtle', tent);
briefs/jockstraps get outline-through-the-pouch wording, never a free-standing cup; soft penises nestle against the testicles
and the cloth conforms; length is given against the body (crotch seam to navel) so the size reads correctly.
Classes: tight (leggings, compression/cycling shorts), brief (briefs, boxer briefs, thin swim trunks), jock (jockstrap),
medium (jeans, chinos, trousers), loose (boxers, joggers, board shorts, pyjamas), covered (wraps)."""
U = ' the fabric unbroken and fully covering him'
U2 = ', the garment fully covering him'
SIDES = ('left', 'right')
def _t(side, ln):
    return ('a clear bulge in the thin stretch fabric, his erect penis held flat against his lower stomach by the fabric and angled up toward his %s hip, '
            'its outline showing as a raised line from the crotch seam %s, the fuller shape of his testicles below it, seen from the front only' % (side, ln)) + U2
TIGHT = [
 _t('left', 'to about two fingers below his navel'), _t('right', 'to about two fingers below his navel'),
 _t('left', 'to about halfway up his lower stomach'), _t('right', 'to about halfway up his lower stomach'),
 _t('left', 'up to his navel'), _t('right', 'up to his navel'),
 'a visible bulge in the thin stretch fabric, his semi-erect penis held against the top of his left thigh by the fabric, the cloth following its outline and the fuller shape of his testicles at its base' + U2,
 'a visible bulge in the thin stretch fabric, his semi-erect penis held against the top of his right thigh by the fabric, the cloth following its outline and the fuller shape of his testicles at its base' + U2,
 'a soft bulge in the thin stretch fabric, his penis and testicles resting together just below the crotch seam and angled a little toward his left thigh, the stretch fabric following their shape' + U2,
 'a soft bulge in the thin stretch fabric, his penis and testicles resting together just below the crotch seam and angled a little toward his right thigh, the stretch fabric following their shape' + U2,
 'a small soft bulge in the thin stretch fabric, the shape of his penis nestled against his testicles faintly visible through the cloth' + U2]
TIGHT_FLACCID = TIGHT[8:]
TIGHT_ERECT = TIGHT[:6]
BRIEF = [
 'a clear erection outline showing through the fabric, angled up toward his left hip, the cloth following its shape' + U2,
 'a clear erection outline showing through the fabric, angled up toward his right hip, the cloth following its shape' + U2,
 'a visible bulge at the front of the garment, his erect penis pointing up toward his navel under the stretched cloth' + U2,
 'a visible bulge at the front of the garment, his semi-erect penis lying toward his left hip under the cloth' + U2,
 'a small visible bulge at the front of the garment, the soft shape of his penis resting against his testicles under the cloth' + U2,
 'a modest soft bulge at the front of the garment, his relaxed penis and testicles faintly outlined by the cloth' + U2]
JOCK = [
 'a modest, natural-sized pouch at the front, fitting close against his body, the soft outline of his penis and testicles showing through it, no larger than his hand' + U2,
 'a modest pouch at the front fitting close against his body, his semi-erect penis outlined softly through it and angled toward his left hip' + U2,
 'a modest pouch at the front held close against his body, his erect penis outlined through it and angled up toward his right hip, the pouch no wider than his hand' + U2]
MEDIUM = [
 'a small soft bulge in the cloth, the shape of his penis nestled against his testicles faintly visible' + U2,
 'a small soft bulge in the cloth, his penis and testicles resting together and faintly outlined through it' + U2,
 'a visible bulge in the cloth, the soft outline of his erect penis partly held against his body and angled toward his left hip, a little looser near the tip' + U2,
 'a visible bulge in the cloth, the soft outline of his erect penis partly held against his body and angled toward his right hip, a little looser near the tip' + U2,
 'a visible bulge in the cloth, the soft outline of his semi-erect penis lying loosely against the top of his thigh' + U2,
 'a visible bulge in the cloth, the soft outline of his erect penis partly held against his lower stomach and pointing up toward his navel, a little looser near the tip' + U2]
def _l(where):
    return ('his erect penis pushing the loose cloth out into a clear tent %s, about a hand wide and a hand and a half long, '
            'the rest of the loose fabric hanging straight and flat from the waistband and draping lightly over and around the tent, not clinging to it,' % where) + U
LOOSE = [
 'no clear outline, the fabric hanging loose and straight down from the waistband over his groin with only a few small folds at the crotch',
 'no clear outline, the loose cloth hanging straight and flat from the waistband with soft vertical folds',
 _l('angled toward his left hip'), _l('angled toward his right hip'), _l('at the front of his waistband'),
 _l('angled toward his left hip'), _l('angled toward his right hip'), _l('at the front of his waistband')]
BC = [
 'no clear outline, the wrap hanging loose and natural over his groin',
 'only a faint, soft fullness in the wrap where his relaxed penis rests, hardly more than a slight change in the drape',
 'a modest, natural-sized rise in the wrap angled toward his left hip where his erect penis pushes it up, no more than a hand in length, the wrap unbroken and fully covering him',
 'a slight, soft rise in the wrap angled toward his right thigh where his half-hard penis presses against it, the wrap unbroken and fully covering him']
HANDS = ' His hands stay clear of his groin.'
def build(final):
    return {'male_bulge_tight': TIGHT, 'male_bulge_brief': BRIEF, 'male_bulge_jock': JOCK, 'male_bulge_medium': MEDIUM, 'male_bulge_loose': LOOSE,
            'male_bulge_clothed': MEDIUM + BRIEF[:3] + TIGHT_ERECT[:2], 'male_bulge_covered': BC}
