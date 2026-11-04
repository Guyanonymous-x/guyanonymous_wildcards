"""Builds the DEMOGRAPHIC-GROUP prompts (files named demo_*).  Runs AFTER the women's and men's libraries are merged (build_all.py calls it), because it
reuses their finished prompts (f_prompt_master_by_age / m_prompt_master_by_age) as the base character and then adds the group-specific parts.

What it makes
  demo_<identity>_<orientation>    one picker file per combination, e.g.  demo_trans_woman_homosexual, demo_cis_man_asexual, demo_intersex_person_pansexual
  demo_prompt_master               every combination, weighted by (rough) population share      demo_prompt_master_balanced   every combination equally
  demo_prompt_master_<identity>    all orientations of one identity, weighted
  demo_body_<identity>             sentences about the body of that identity group (hormone effects, scars, build, face ...)
  demo_anat_<identity>             clinical, adult anatomy descriptions for the group - NOT referenced by any default prompt (like the other anatomy files)
  demo_ctx_<pronoun>_<partner>     optional neutral context lines (a ring, a photo, a pin) that hint at orientation without relying on stereotypes
Orientation is not visible in a person, so it is stated in the prompt text and hinted with those neutral context lines only; no appearance stereotypes are used.
All subjects are adults (the base prompts only generate ages 18-120).  The numbers in SHARE_* are rough placeholders - edit them to taste."""
import os, sys, random
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from paths import FINAL
WC = sys.argv[1] if len(sys.argv) > 1 and os.path.isdir(sys.argv[1]) else FINAL

# identity: (noun phrase, pronoun key, bases ('f','m'), gender-of-identity m/f/x, population share %)
IDENT = {
 'cis_man': ('a cisgender man', 'he', 'm', 'm', 48.0), 'cis_woman': ('a cisgender woman', 'she', 'f', 'f', 48.6),
 'trans_man': ('a trans man', 'he', 'm', 'm', .30), 'trans_woman': ('a trans woman', 'she', 'f', 'f', .30),
 'trans_man_own_path': ('a trans man who has chosen not to have genital surgery', 'he', 'm', 'm', .25), 'trans_woman_own_path': ('a trans woman who has chosen not to have genital surgery', 'she', 'f', 'f', .25),
 'gradual_fem': ('a person on a gradual transition toward a more feminine presentation', 'she', 'fm', 'x', .08), 'gradual_masc': ('a person on a gradual transition toward a more masculine presentation', 'he', 'fm', 'x', .08),
 'individualized_fem': ('a non-binary person with an individualized transition whose body keeps both masculine and feminine characteristics, leaning feminine', 'they', 'fm', 'x', .05), 'individualized_masc': ('a non-binary person with an individualized transition whose body keeps both masculine and feminine characteristics, leaning masculine', 'they', 'fm', 'x', .05),
 'androgynous': ('an androgynous person', 'they', 'fm', 'x', .55), 'nonbinary': ('a non-binary person', 'they', 'fm', 'x', .45),
 'intersex_man': ('an intersex man', 'he', 'm', 'm', .08), 'intersex_woman': ('an intersex woman', 'she', 'f', 'f', .08), 'intersex_person': ('an intersex person', 'they', 'fm', 'x', .08)}
ATTR = {'opposite': 'opposite-sex partners', 'same': 'same-sex partners', 'both': 'both', 'all': 'all', 'none': 'none'}
SHARE_ATTR = {'opposite': 87, 'same': 4, 'both': 5, 'all': 1.5, 'none': 1.5}
def _orient_raw(gid, attr, noun):
    if attr == 'none': return f"{noun} who is asexual"
    if attr == 'both': return f"{noun} who is bisexual"
    if attr == 'all': return f"{noun} who is pansexual"
    if gid == 'x': return f"{noun} who is attracted to {'men' if attr == 'opposite' else 'women'}" if False else f"{noun} who is {'queer and attracted mainly to men' if attr == 'opposite' else 'queer and attracted mainly to women'}"
    if attr == 'opposite': return f"{noun} who is heterosexual"
    return f"{noun} who is homosexual ({'gay' if gid == 'm' else 'lesbian'})"
def orient_label(gid, attr, noun):
    r = _orient_raw(gid, attr, noun)
    return r[:len(noun)] + ', and' + r[len(noun):] if (' who ' in noun or ' whose ' in noun) else r
def attr_for(gid, attr):          # who the partner is: 'men' 'women' 'any' 'none'
    if attr == 'none': return 'none'
    if attr in ('both', 'all'): return 'any'
    if gid == 'x': return 'men' if attr == 'opposite' else 'women'
    return ('women' if gid == 'm' else 'men') if attr == 'opposite' else ('men' if gid == 'm' else 'women')
PARTNER = {'men': ["boyfriend", "husband", "male partner", "fiancé"], 'women': ["girlfriend", "wife", "female partner", "fiancée"], 'any': ["partner", "boyfriend", "girlfriend", "spouse"], 'none': ["close friend", "best friend", "roommate", "sister", "colleague"]}
POSS = {'he': ('his', 'he'), 'she': ('her', 'she'), 'they': ('their', 'they')}
CTX = ["{Pp} {w} appears beside {po} in a framed photograph on a nearby shelf.", "{Ps} wears a plain ring on the left hand, a gift from {pp} {w}.", "{Ps} is reading a message from {pp} {w} on a phone.",
       "A second coffee mug, for {pp} {w}, stands next to {pp} own.", "{Ps} keeps a small keepsake from {pp} {w} in a pocket.", "In the background, {pp} {w} waves from across the room.",
       "{Ps} is holding hands with {pp} {w}, only the linked fingers visible.", "A bag with a sticker of {pp} {w}'s favourite band hangs from {pp} shoulder."]
CTX_NONE = ["{Ps} wears a black ring on the right middle finger.", "{Ps} is happily alone, absorbed in a book.", "{Ps} wears a small pin with a purple, grey, white and black stripe design.",
            "{Ps} is surrounded by close friends and treats them as {pp} chosen family.", "{Ps} sits comfortably alone with a hobby project spread out.", "A framed photo of {pp} {w} stands nearby."]
BODY = {   # identity -> list of fragment pools; each line = 'Pronoun body shows: a, b and c.'
 'trans_man': ["a flat, masculine chest from top surgery, with faint horizontal scars", "a chest flattened by a binder", "a deeper-set jaw and a squarer face from testosterone", "growing facial stubble and some chest hair", "broader shoulders and increased muscle definition",
   "a voice that is deep and rough", "a slightly narrow hip line", "short cropped hair with a masculine hairline", "a thickened neck and an Adam's apple that has begun to show"],
 'trans_woman': ["breasts developed through hormone therapy", "softened skin and fat redistributed to the hips and thighs", "slightly broad shoulders", "a feminised face with a smoothed brow after facial feminisation surgery", "a small but visible Adam's apple",
   "smooth, laser-treated facial skin", "long, grown-out hair", "reduced body hair", "a slim waist and rounder hips", "large hands and feet"],
 'gradual_fem': ["small breasts that have begun to grow", "a body in clear transition, with softer features but a visibly masculine frame", "thin patchy remnants of facial hair", "long hair", "a face that reads as ambiguous between masculine and feminine",
   "fat starting to redistribute to the hips", "a barely visible Adam's apple", "broad shoulders with softer arms"],
 'gradual_masc': ["a chest that is flatter than before, with small residual breast tissue", "a body in clear transition, with firmer, more masculine features and a visibly feminine frame", "light stubble across the jaw and chin", "short hair",
   "a face that reads as ambiguous between masculine and feminine", "slightly widened shoulders", "a slim waist with hips beginning to narrow", "deepening facial lines at the jaw"],
 'androgynous': ["a slim, narrow-hipped frame with a flat chest", "fine, even facial features that read as neither clearly male nor female", "a smooth jaw and a soft brow", "medium-length hair worn in an ungendered style", "slender shoulders and a long neck",
   "a soft voice of indeterminate pitch", "a body that shows few gendered contours", "clean, bare skin with no obvious facial hair", "delicate wrists and long fingers"],
 'intersex_person': ["a body that mixes typical male and female traits", "a chest that is slightly developed with a broad frame", "a hairless face with a defined jaw", "narrow hips with a soft chest", "both a broad frame and soft curves", "a clearly androgynous build",
   "a naturally occurring combination of male and female secondary sexual traits", "modest chest development with a deep voice"]}
BODY['trans_man_own_path'] = BODY['trans_man']; BODY['trans_woman_own_path'] = BODY['trans_woman']; BODY['individualized_fem'] = BODY['gradual_fem']; BODY['individualized_masc'] = BODY['gradual_masc']; BODY['nonbinary'] = BODY['androgynous']
BODY['intersex_man'] = BODY['intersex_person'] + ["a masculine build with some breast tissue", "broad shoulders and a deep chest with softer hips"]; BODY['intersex_woman'] = BODY['intersex_person'] + ["a feminine build with a deeper voice and some facial hair shadow", "curved hips and modest breasts with a broad jaw"]
BODY['cis_man'] = ["a typical masculine build"]; BODY['cis_woman'] = ["a typical feminine build"]
ANAT = {   # clinical, adult, non-explicit descriptions of sex characteristics - kept in their own files, referenced by no default prompt
 'trans_man': ["a surgically constructed phallus after phalloplasty", "a metoidioplasty-enlarged clitoris that functions as a small phallus", "a vulva with a clitoris enlarged by testosterone", "a vulva, with the uterus and ovaries intact", "a vulva with the uterus and ovaries removed"],
 'trans_woman': ["a surgically constructed vulva and vagina after vaginoplasty", "a penis and testes, reduced in size by hormone therapy, together with breasts", "a vulva constructed from penile tissue, with a shortened urethra", "a penis, with orchiectomy completed"],
 'trans_man_own_path': ["a vulva, with a clitoris enlarged by testosterone and no genital surgery", "a vulva and a flat chest, with only top surgery", "a vulva and a masculine body with body hair, on testosterone"],
 'trans_woman_own_path': ["a penis and testes together with hormone-developed breasts", "a penis and testes, softened by anti-androgens, with breasts", "a penis with orchiectomy completed and no vaginoplasty, together with breasts"],
 'gradual_fem': ["a penis and testes together with small developing breasts", "a penis with testes, with the first signs of breast development", "a body mixing male genitals with early female secondary characteristics"],
 'gradual_masc': ["a vulva and a clitoris enlarged by testosterone, with a flattened chest", "a vulva together with a flat chest and facial stubble", "a body mixing female genitals with early male secondary characteristics"],
 'individualized_fem': ["a penis and testes with fully developed breasts", "a penis and testes with moderately developed breasts, by their own choice of surgeries and hormones", "feminine breasts and masculine genitals in one body, a deliberately blended body"],
 'individualized_masc': ["a vulva with a flat chest after top surgery, by their own choice", "a vulva and a clitoris enlarged by testosterone, on a hormone plan of their own choosing", "male-pattern body hair and a deepened voice with a vulva, by their own choice of hormones"],
 'androgynous': ["typical male anatomy, hidden under a unisex wardrobe", "typical female anatomy, hidden under a unisex wardrobe"],
 'intersex_person': ["a vulva and an enlarged clitoris resembling a small phallus", "a small penis with a divided scrotum and undescended testes", "ovotesticular tissue with both ovarian and testicular tissue", "both a vagina and a small penis", "a vulva with internal testes (androgen insensitivity)", "hypospadias with a small penis and a partially fused scrotum", "ambiguous external genitals, neither clearly male nor female", "a penis and testes with an additional uterus and cervix (persistent Müllerian duct syndrome)", "a vulva with a deep vagina and internal testes", "a penis with testes and a XXY chromosomal pattern with small testes"]}
for k in ('nonbinary',): ANAT[k] = ANAT['androgynous']
ANAT['intersex_man'] = [a for a in ANAT['intersex_person'] if 'penis' in a or 'testes' in a]; ANAT['intersex_woman'] = [a for a in ANAT['intersex_person'] if 'vulva' in a or 'vagina' in a]
ANAT['cis_man'] = ["a penis and testes"]; ANAT['cis_woman'] = ["a vulva and vagina"]
WARD_X = {'androgynous': ["wearing a plain unisex outfit of loose trousers and a boxy shirt", "wearing a tailored suit with a soft silk blouse", "wearing an oversized sweater and straight jeans", "wearing a long tunic over wide trousers"],
          'gradual_fem': ["wearing a loose shirt over a soft top", "wearing a mix of masculine trousers and a feminine blouse"], 'gradual_masc': ["wearing a plain button shirt and a tight undershirt", "wearing a mix of masculine trousers and a fitted top"]}

def w(name, lines):
    open(os.path.join(WC, name + '.txt'), 'w', encoding='utf8', newline='\n').write('\n'.join(lines) + '\n')
def exists(n): return os.path.exists(os.path.join(WC, n + '.txt'))
def poss(p): return POSS[p][0]
def body_lines(gid, pron, R, n=120):
    lead = {"he": "He has", "she": "She has", "they": "This person has"}[pron]
    pool = BODY[gid]; out = set(); k = 0
    P = {'he': 'He', 'she': 'She', 'they': 'They'}[pron]; Ps = {'he': 'His', 'she': 'Her', 'they': 'Their'}[pron]
    while len(out) < n and k < n * 40:
        k += 1; a = R.sample(pool, min(len(pool), R.choice([2, 3, 3, 4])))
        out.add(f"{lead} {a[0]}." if len(a) == 1 else f"{lead} {', '.join(a[:-1])} and {a[-1]}.")
    return sorted(out)
def build():
    R = random.Random(2024); combos = []
    for gid_, (noun, pron, base, gid, share) in IDENT.items():
        pron = pron if len(base) == 1 else 'they'
        w(f'demo_body_{gid_}', body_lines(gid_, pron, R)); w(f'demo_anat_{gid_}', [f"{ {'he':'His','she':'Her','they':'Their'}[pron]} anatomy: {a}." for a in ANAT[gid_]])
    for pron in ('he', 'she', 'they'):
        for pt in ('men', 'women', 'any', 'none'):
            lines = []
            Ps = {'he': 'He', 'she': 'She', 'they': 'They'}[pron]; Pp = {'he': 'His', 'she': 'Her', 'they': 'Their'}[pron]; pp = Pp.lower(); po = {'he': 'him', 'she': 'her', 'they': 'them'}[pron]
            lines = [c.format(Ps=Ps, Pp=Pp, pp=pp, po=po, w=w_) for c in (CTX_NONE if pt == 'none' else CTX) for w_ in PARTNER[pt]]
            w(f'demo_ctx_{pron}_{pt}', sorted(set(lines)))
    for gid_, (noun, pron, base, gid, share) in IDENT.items():
        bases = [b for b in base] if base != 'fm' else ['f', 'm']
        pron = pron if len(base) == 1 else 'they'
        for attr in ATTR:
            pt = attr_for(gid, attr); label = orient_label(gid, attr, noun)
            lines = []
            for b in bases:
                bm = f"{b}_prompt_master_by_age"
                if not exists(bm): sys.exit(f'{bm} not found - build the libraries first')
                lines.append(f"Subject: {label}. __demo_body_{gid_}__ __{bm}__ __demo_ctx_{pron}_{pt}__")
                lines.append(f"__{bm}__ The subject is {label}. __demo_body_{gid_}__ __demo_ctx_{pron}_{pt}__")
                lines.append(f"A portrait of {label}. __{bm}__ __demo_body_{gid_}__")
                lines.append(f"{label[0].upper() + label[1:]}. __{bm}__ __demo_ctx_{pron}_{pt}__")
            w(f'demo_{gid_}_{attr_name(attr, gid)}', lines)
            combos.append((gid_, attr, share * SHARE_ATTR[attr] / 100))
    tot = sum(c[2] for c in combos)
    from wcbuild import allocate
    cnt = allocate([c[2] for c in combos], 2000)
    lines = []
    for (g, a, _), k in zip(combos, cnt): lines += [f"__demo_{g}_{attr_name(a, IDENT[g][3])}__"] * k
    random.Random(1).shuffle(lines); w('demo_prompt_master', lines)
    w('demo_prompt_master_balanced', [f"__demo_{g}_{attr_name(a, IDENT[g][3])}__" for g, a, _ in combos])
    for gid_ in IDENT:
        w(f'demo_prompt_master_{gid_}', [f"__demo_{gid_}_{attr_name(a, IDENT[gid_][3])}__" for a in ATTR for _ in range(max(1, round(SHARE_ATTR[a] / 3)))])
    print('demographic files:', len(combos), 'combinations')
def attr_name(attr, gid):
    if attr == 'none': return 'asexual'
    if attr == 'both': return 'bisexual'
    if attr == 'all': return 'pansexual'
    if gid == 'x': return 'attracted_to_men' if attr == 'opposite' else 'attracted_to_women'
    return 'heterosexual' if attr == 'opposite' else 'homosexual'
if __name__ == '__main__': build()
