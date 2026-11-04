"""Sentences that say how old the person LOOKS, per age bracket (appended to every identity section as __aging_summary__).
   Written with 'Her/her'; age_build.py converts to 'His/his' for the male library.  Blank lines = nothing added."""
import random
YOUNG = ["Her skin is smooth and unlined, with the freshness of early adulthood.", "She looks every bit her age, youthful and unlined.", "Her face has the soft, firm contours of a young adult.",
         "There are no visible signs of aging on her face.", "Her complexion is clear and taut, with bright youthful eyes.", "Her skin has a youthful bounce and a fresh, even tone."]
EARLY = ["Her face is still smooth, with only faint expression lines.", "Her skin is mostly unlined, with the first light lines at the eyes and mouth.",
         "She looks in her prime, with a few fine lines when she smiles.", "Her features are firm and settled, with a mature look.", "A few fine lines show at the corners of her eyes."]
POOLS = {
 3: dict(lead=["Her face shows the first clear signs of middle age:", "She looks solidly middle-aged:", "She has the weathered but well-kept look of a woman in her early fifties:",
               "Visible middle age shows in her face:", "She is clearly past youth:"],
         skin=["fine lines at the eyes and mouth", "light forehead creases", "faint nasolabial folds", "slightly slack skin at the jaw", "early crow's feet", "some loss of firmness in the cheeks", "a few age spots on the cheeks"],
         hair=["scattered strands of age-lightened hair", "hair that is starting to thin", "slightly thinner hair", "hair showing the first signs of ageing"],
         body=["a slightly softened waistline", "a trace of heaviness in the shoulders", "a middle-aged posture", "a softer jawline"]),
 4: dict(lead=["She looks like an older adult well into her late fifties or sixties:", "Her face shows definite aging:", "She is plainly in the later years of middle age:", "She looks like a woman of around sixty:"],
         skin=["deep lines around her eyes and mouth", "etched forehead wrinkles", "clear jowls beginning to form", "thinner, dry skin", "pronounced nasolabial folds", "age spots across her cheeks and hands", "slackening skin on her neck", "visible crow's feet"],
         hair=["hair that is clearly thinning", "age-lightened hair", "hair thinning at the crown", "fine, thinning hair"],
         body=["a softened, slightly rounded body", "slight stoop in the shoulders", "visible neck lines", "veins visible on her hands"]),
 5: dict(lead=["She looks like a senior citizen in her late sixties or seventies:", "Her face is clearly aged:", "Age is evident in every feature:", "She looks distinctly old, well past retirement age:", "She looks like a woman of around seventy:"],
         skin=["deep wrinkles across her forehead and cheeks", "heavy jowls and a slack jaw", "papery thin skin with many age spots", "deep folds from nose to mouth", "sagging eyelids", "thin, creased lips", "sunken cheeks", "a crepey, wrinkled neck"],
         hair=["thin hair", "hair worn short and thin", "sparse hair", "fine thinning hair"],
         body=["rounded shoulders", "a stooped posture", "age spots on her hands and arms", "slightly trembling hands", "a slower, careful stance"]),
 6: dict(lead=["She looks elderly and frail:", "She is unmistakably elderly:", "Age has deeply marked her:", "She looks like a woman in her late seventies or eighties:", "She has the fragile look of advanced age:"],
         skin=["deeply wrinkled, papery skin", "hollow cheeks and sunken eyes", "heavy drooping eyelids", "a loose, wrinkled neck with hanging skin", "age spots covering her face and hands", "thin lips drawn in over missing teeth", "a network of fine wrinkles over her whole face", "translucent skin with visible veins"],
         hair=["very thin hair", "wispy hair with the scalp visible", "a thin halo of hair", "sparse fine hair"],
         body=["a clearly bent back", "a visible stoop", "frail thin arms", "knobby arthritic hands", "shaky hands", "a slow, hunched posture", "a cane or walker nearby"]),
 7: dict(lead=["She looks very old, in her late eighties or nineties:", "She is extremely elderly and fragile:", "Great age shows in every line:", "She looks ancient, shrunken by age:", "She looks like a woman in her nineties:"],
         skin=["a face covered in deep wrinkles and folds", "translucent paper-thin skin with a map of veins", "cheeks collapsed inward", "heavy hooded eyes with cloudy irises", "a very lined, collapsed mouth", "age spots and skin tags across the face", "a sunken jaw", "loose skin hanging at the throat and arms"],
         hair=["sparse wisps of hair", "very thin hair over a visible scalp", "almost no hair, just a few strands", "a fine fuzz of hair"],
         body=["a bent, shrunken frame", "a pronounced curve in the upper back", "tiny frail limbs", "trembling hands with swollen knuckles", "a small body folded forward", "visible dependence on a cane or a wheelchair"]),
 8: dict(lead=["She looks extraordinarily old, close to or past one hundred:", "She is a centenarian, tiny and fragile:", "She looks ancient, remarkably aged:", "Her extreme old age is unmistakable:", "She looks as old as a person can look:"],
         skin=["skin like crumpled tissue paper, covered in countless fine wrinkles", "deeply sunken eyes and cheeks", "an almost skeletal face with translucent skin", "a very lined face with drooping skin and age spots", "a collapsed jaw and thin lips with deep creases", "a face of deep folds, shrunken and soft"],
         hair=["a few wisps of hair", "nearly bald with fine down", "thin silky hair", "sparse strands of hair"],
         body=["a tiny, severely bent body", "a shrunken, doll-like frame", "bone-thin arms covered in spots", "gnarled arthritic hands", "a deeply stooped back", "a body hardly larger than a child's, folded with age"]),
}
def lines(bi, n):
    R = random.Random(1000 + bi); out = []
    if bi in (0, 1, 2):
        pool = YOUNG if bi == 0 else (YOUNG + EARLY) if bi == 1 else EARLY
        while len(out) < n: out.append(R.choice(pool) if R.random() < .5 else '')
        return out
    P = POOLS[bi]; seen = set()
    for _ in range(40000):
        if len(out) >= n: break
        parts = [R.choice(P['skin'])]
        if R.random() < .85: parts.append(R.choice(P['hair']))
        if R.random() < .75: parts.append(R.choice(P['body']))
        if R.random() < .5: parts.append(R.choice(P['skin']))
        parts = list(dict.fromkeys(parts))
        text = R.choice(P['lead']) + ' ' + ', '.join(parts[:-1]) + (' and ' if len(parts) > 1 else '') + parts[-1] + '.'
        if text not in seen: seen.add(text); out.append(text)
    return out
