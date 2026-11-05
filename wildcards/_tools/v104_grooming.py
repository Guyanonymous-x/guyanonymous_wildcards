"""v104 - beauty and grooming objects and products: female and male hygiene, grooming and beauty items, plus unisex care.
Each item is a full visual description (shape, material, colour, finish). Packaged goods may carry quoted fake-name text."""
import random
R = random.Random(10400)
COL = ['soft white', 'pale pink', 'dusty rose', 'blush pink', 'lilac', 'lavender', 'sky blue', 'navy blue', 'teal', 'mint green', 'sage green', 'forest green', 'cream', 'ivory', 'sand', 'terracotta', 'burgundy', 'charcoal grey', 'matte black', 'slate grey', 'silver', 'gold', 'copper', 'rose gold', 'clear', 'frosted white', 'amber', 'coral', 'mustard yellow', 'olive green']
FIN = ['matte', 'glossy', 'satin', 'brushed', 'frosted', 'soft-touch', 'speckled', 'pearlescent', 'ribbed', 'smooth']
PACK_TEXT = [' On the front, the name "__name_brand__" is printed in large letters on the first line and "__name_variant_household__" on the second line.',
             ' The front reads "__name_brand__" on the first line and "__name_type_household__" on the second line, with "__name_weight_household__" in small letters at the bottom.']
# (name, description with {c} colour and {f} finish, packaged?)
FH = [  # female hygiene
 ('tampon', 'a tampon with a {c} cardboard applicator and a white string, shown beside its {c2} wrapper', 0),
 ('tampon box', 'a small rectangular box of tampons in {c} with a {f} finish, its lid open to show rows of wrapped tampons', 1),
 ('pad', 'a sanitary pad with wings folded back, a white absorbent surface and a {c} backing strip, laid flat', 0),
 ('night pad', 'a long overnight pad with a wide curved back and soft wings, white on top with a {c} wrapper beside it', 0),
 ('panty liner', 'a slim panty liner, white and oval, with its {c} paper backing peeled halfway off', 0),
 ('pad pack', 'a flat plastic bag of sanitary pads in {c} with a {f} finish and a resealable strip', 1),
 ('menstrual cup', 'a bell-shaped menstrual cup of {f} {c} silicone with a short stem and small air holes under the rim, beside a small cotton drawstring pouch', 0),
 ('menstrual disc', 'a flat, round, flexible menstrual disc of {f} {c} silicone with a rim and a small finger loop', 0),
 ('period underwear', 'a pair of {c} cotton period underwear folded flat, with a darker absorbent panel in the gusset visible', 0),
 ('cloth pad', 'a folded reusable cloth pad in {c} cotton with snap-closing wings and a soft flannel top', 0),
 ('intimate wash', 'a {f} {c} plastic bottle of intimate wash with a flip-top lid and a pump on the side', 1),
 ('feminine wipes', 'a soft flat pack of intimate wipes in {c} with a peel-back flap, one wipe pulled partly out', 1),
 ('peri bottle', 'a squeeze bottle with a long curved angled spout in {f} {c} plastic, used for rinsing', 0),
 ('hot water bottle', 'a rubber hot water bottle in {c} with a knitted cover, resting on a bed', 0),
 ('pain relief heat patch', 'a flat rectangular adhesive heat patch in {c} fabric, its paper backing partly peeled away', 1),
 ('razor female', 'a razor with a curved {c} handle, a pivoting head and a {f} finish, with a protective cap beside it', 0),
 ('bikini trimmer', 'a small cordless trimmer in {f} {c} with a slim head, a guard comb beside it', 0),
 ('bag of period products', 'a small zipped pouch in {c} fabric, open to show a tampon, a folded pad and a small bottle of wipes', 0)]
MH = [  # male hygiene
 ('deodorant stick', 'a {f} {c} deodorant stick in a cylinder, its cap off and the white stick twisted out', 1),
 ('body wash', 'a tall squeezable bottle of body wash in {f} {c} plastic with a flip cap', 1),
 ('soap bar', 'a rectangular bar of soap in {c} with rounded edges and a faintly {f} surface, resting on a ceramic dish', 0),
 ('shower gel pouch', 'a flat refill pouch of shower gel in {c} with a spout at the top', 1),
 ('intimate wash men', 'a {f} {c} bottle of men\'s intimate wash with a pump top', 1),
 ('foot powder', 'a shaker tin of foot powder in {f} {c} metal with a perforated cap', 1),
 ('body powder', 'a round tin of body powder in {c} with a puff resting beside it and fine white powder dusted around it', 1),
 ('body groomer', 'a cordless body groomer in {f} {c} with a narrow trimmer head and a guard comb beside it', 0),
 ('nose trimmer', 'a slim handheld nose and ear hair trimmer in {f} {c} with a small round head', 0),
 ('nail clippers', 'a pair of steel nail clippers with a lever, and a small {c} leather case beside them', 0),
 ('toothbrush male', 'a toothbrush with a thick {c} handle and firm bristles, in a ceramic cup', 0),
 ('shaving gel', 'a squeezable tube of shaving gel in {f} {c} with a screw cap', 1),
 ('sports towel', 'a folded {c} towel with a woven stripe at one end, on a gym bench', 0),
 ('antiperspirant spray', 'a tall {f} {c} aerosol can of antiperspirant with a button cap', 1)]
MG = [  # male grooming / beauty
 ('safety razor', 'a double-edge safety razor with a {f} {c} handle and a chrome head, a fresh blade beside it', 0),
 ('cartridge razor', 'a cartridge razor with a ribbed {c} handle and a pivoting head with five blades', 0),
 ('straight razor', 'a straight razor with a folding blade and a {c} handle, lying open beside a leather strop', 0),
 ('electric shaver', 'an electric foil shaver in {f} {c} with a small display and a charging stand', 0),
 ('shaving brush', 'a shaving brush with a {c} handle and a full, soft badger-hair knot, its tips damp with lather', 0),
 ('shaving bowl', 'a wide ceramic shaving bowl in {c} filled with thick white lather and a brush resting across it', 0),
 ('shaving soap', 'a round puck of shaving soap in a wooden bowl, {c} and slightly {f}, with lather swirled across the top', 0),
 ('aftershave balm', 'a {f} {c} bottle of aftershave balm with a pump top', 1),
 ('aftershave splash', 'a glass bottle of aftershave in {c} liquid with a heavy {f} cap and a square base', 1),
 ('beard trimmer', 'a cordless beard trimmer in {f} {c} with an adjustable guard comb and a small oil bottle beside it', 0),
 ('beard oil', 'a small glass dropper bottle of golden beard oil with a {c} cap, a bead of oil on the tip of the dropper', 1),
 ('beard balm', 'a small round tin of beard balm in {c}, its lid off and a thick waxy balm inside', 1),
 ('beard comb', 'a fine-toothed wooden beard comb in {c} with a rounded handle, a few strands of hair caught in it', 0),
 ('beard brush', 'a boar-bristle beard brush with a rounded {c} wooden handle', 0),
 ('moustache wax', 'a tiny round tin of moustache wax in {c} with a small comb beside it', 1),
 ('pomade', 'a round {f} {c} tin of hair pomade, the lid off and a smooth glossy surface with a comb mark in it', 1),
 ('hair clay', 'a wide plastic jar of matte hair clay in {c} with a screw lid placed beside it', 1),
 ('barber scissors', 'a pair of steel barber scissors with a finger rest and a {c} handle, on a folded towel', 0),
 ('hair clipper', 'a hair clipper in {f} {c} with a set of guard combs in a row beside it', 0),
 ('styptic pencil', 'a short white styptic pencil in a {c} case, damp at its tip', 0),
 ('cologne', 'a rectangular glass bottle of cologne with {c} liquid, a {f} cap and a spray nozzle', 1),
 ('men skincare', 'a {f} {c} tube of men\'s face moisturiser, squeezed to leave a small white dab on a counter', 1),
 ('tinted moisturiser', 'a small {f} {c} squeeze tube of tinted moisturiser with a dab of beige cream smeared beside it', 1),
 ('brow gel', 'a slim {f} {c} tube of clear brow gel with a small spiral brush wand', 1),
 ('eyeliner men', 'a black kohl pencil with a {c} barrel, freshly sharpened', 0),
 ('lip balm men', 'a small {f} {c} tube of lip balm, twisted up to show a pale waxy stick', 1),
 ('wash bag', 'a {c} zippered leather wash bag, open to show a razor, a brush and a bottle inside', 0)]
FB = [  # female beauty
 ('lipstick', 'a {f} {c} lipstick tube twisted up to show a rich, rounded bullet of colour', 0),
 ('lip gloss', 'a slim tube of glossy lip gloss with a {c} cap and a soft doe-foot applicator, a streak of colour beside it', 0),
 ('lip liner', 'a sharpened lip liner pencil with a {c} barrel and a thin line drawn beside it', 0),
 ('mascara', 'a slim {f} {c} mascara tube with its wand pulled out, the bristles dark and coated', 1),
 ('eyeliner', 'a liquid eyeliner pen with a {c} barrel and a fine brush tip, a thin black line drawn beside it', 1),
 ('eyeshadow palette', 'a rectangular {f} {c} eyeshadow palette with a mirror in the lid, twelve pans in a soft gradient, a fluffy brush beside it', 1),
 ('blush compact', 'a round {f} {c} compact with the lid open to show a pressed pink blush and a small mirror', 1),
 ('foundation bottle', 'a glass bottle of foundation with a {c} pump top and a {f} body, a swatch of beige liquid smeared beside it', 1),
 ('concealer', 'a slim squeeze tube of concealer with a {c} sponge-tip applicator', 1),
 ('setting powder', 'a round jar of loose setting powder in {c} with a sifter lid and a large soft brush beside it', 1),
 ('highlighter', 'a flat pressed highlighter pan in {c} with a shimmering {f} surface and a small brush', 1),
 ('makeup brush set', 'a set of makeup brushes with {c} handles and soft rounded heads standing in a ceramic cup', 0),
 ('beauty sponge', 'a damp teardrop-shaped makeup sponge in {c} beside a smear of foundation', 0),
 ('nail polish', 'a small glass bottle of nail polish in {c} with a black cap and a {f} finish, a painted swatch beside it', 1),
 ('nail file', 'a slim emery nail file in {c} with a curved shape and a {f} grip', 0),
 ('nail kit', 'a manicure set in a zipped {c} case, open to show clippers, a file, tweezers and a cuticle pusher', 0),
 ('tweezers', 'a pair of slanted steel tweezers with a {c} grip, next to a magnifying mirror', 0),
 ('eyelash curler', 'a metal eyelash curler with {c} rubber pads and a looped handle, held open', 0),
 ('false lashes', 'a pair of false lashes in a clear plastic tray with a small tube of {c} glue', 1),
 ('perfume bottle', 'a faceted glass perfume bottle with {c} liquid, a gold collar and a spray nozzle', 1),
 ('face serum', 'a small glass serum bottle with a {c} rubber dropper and a {f} cap', 1),
 ('moisturiser jar', 'a wide round jar of face cream in {f} {c} glass with the lid beside it and a smooth white swirl of cream inside', 1),
 ('sheet mask', 'a folded sheet mask in a {c} foil sachet, one corner peeled open to show a damp white mask', 1),
 ('facial roller', 'a facial roller with a smooth {c} stone head and a slim {f} handle', 0),
 ('hair dryer', 'a hair dryer in {f} {c} with a long nozzle and a coiled cord', 0),
 ('curling iron', 'a {f} {c} curling iron with a heat-proof tip and a coiled cord', 0),
 ('hair straightener', 'a slim hair straightener in {f} {c} with ceramic plates, clamped shut', 0),
 ('paddle brush', 'a wide paddle hairbrush with a {c} cushioned pad, flexible pins and a long handle', 0),
 ('hair clips', 'a handful of hair clips in {c} metal and {f} plastic spread on a vanity tray', 0),
 ('scrunchies', 'a stack of scrunchies in {c} silk', 0),
 ('vanity mirror', 'a round makeup mirror on a {f} {c} stand with a ring of small lights', 0),
 ('makeup bag', 'a quilted {c} makeup bag, unzipped to show lipsticks, brushes and a compact inside', 0)]
UN = [  # unisex care
 ('toothbrush', 'a toothbrush with a slim {c} handle and soft bristles, standing in a glass', 0),
 ('toothpaste', 'a flattened tube of toothpaste in {c} with a screw cap and a ribbon of white paste on a brush', 1),
 ('dental floss', 'a small {c} dispenser of dental floss with a thread pulled out', 1),
 ('mouthwash', 'a tall {f} {c} bottle of mouthwash with a measuring cap', 1),
 ('shampoo', 'a tall bottle of shampoo in {f} {c} plastic with a pump top', 1),
 ('conditioner', 'a bottle of conditioner in {f} {c} with a flip cap, placed on a shower shelf', 1),
 ('hair mask', 'a wide jar of hair mask in {c} with a scoop of creamy mask resting on the lid', 1),
 ('hair brush', 'a round {c} wooden hairbrush with natural bristles', 0),
 ('comb', 'a {c} plastic comb with fine and wide teeth', 0),
 ('loofah', 'a natural {c} loofah on a cord, hung from a shower hook', 0),
 ('bath sponge', 'a soft {c} bath sponge, damp and dripping', 0),
 ('hand cream', 'a squeeze tube of hand cream in {c} with a {f} finish and a flip cap', 1),
 ('sunscreen', 'a squeeze bottle of sunscreen in {c} with a flip cap', 1),
 ('lip balm', 'a small tube of lip balm in {c} twisted up to show a pale stick', 1),
 ('cotton pads', 'a round tub of cotton pads in {c} with the lid off and pads spilling out', 0),
 ('cotton swabs', 'a small box of cotton swabs in {c} with a few swabs standing in a glass', 0),
 ('bath towel', 'a thick folded bath towel in {c} cotton with a woven border', 0),
 ('shower cap', 'a clear plastic shower cap with a {c} elastic edge', 0),
 ('razor blade pack', 'a flat pack of razor cartridges in {c} with a {f} finish', 1),
 ('bath bomb', 'a round bath bomb in {c} with a {f} surface, fizzing slightly at the edge of a full bathtub', 0),
 ('body lotion', 'a tall pump bottle of body lotion in {f} {c} plastic', 1),
 ('face wash', 'a squeeze tube of face wash in {c} with a flip cap, a swirl of cleanser on a damp palm beside it', 1),
 ('talcum powder', 'a round tin of talcum powder in {c} with a shaker top', 1),
 ('hand soap pump', 'a refillable glass pump bottle of hand soap in {c} on a sink edge', 1)]
GROUPS = {'f_hygiene': FH, 'm_hygiene': MH, 'm_grooming': MG, 'f_beauty': FB, 'unisex_care': UN}
SURF = ['a white marble bathroom counter', 'a wooden bathroom shelf', 'a pale tiled windowsill', 'a glass vanity tray', 'a woven basket on a bathroom shelf', 'a folded white towel', 'a grey stone countertop', 'a dressing table beside a mirror', 'a medicine cabinet shelf', 'a clean ceramic basin edge', 'a bedside table', 'a gym locker bench']
LIGHT = ['soft diffused daylight from a frosted window', 'bright even bathroom light', 'warm lamplight', 'clean white studio light', 'soft morning sunlight', 'cool overhead light']
FRAME = ['A close view from slightly above.', 'A close view at eye level.', 'A medium close-up with the surface visible around the object.', 'A tight view filling the frame with the object.']
def lines(items, packaged=True):
    out = []
    for name, d, pk in items:
        cs = R.sample(COL, 5)
        for i, c in enumerate(cs):
            f = R.choice(FIN); c2 = R.choice(COL)
            t = d.format(c=c, f=f, c2=c2)
            t = t[0].upper() + t[1:] + '.'
            if pk and i % 2 == 0: t += R.choice(PACK_TEXT)
            out.append(t)
    return out
def build(final):
    G = {}; ep = []
    for k, items in GROUPS.items():
        G['groom_item_' + k] = lines(items)
        G['groom_%s_prompt' % k] = ['__groom_item_%s__ It sits on __groom_surface__. The light is __groom_light__. __groom_frame__' % k]
        ep.append('groom_%s_prompt' % k); ep.append('groom_item_' + k)
    G['groom_surface'] = SURF; G['groom_light'] = LIGHT; G['groom_frame'] = FRAME
    G['groom_item_female'] = ['__groom_item_f_hygiene__', '__groom_item_f_beauty__']
    G['groom_item_male'] = ['__groom_item_m_hygiene__', '__groom_item_m_grooming__']
    G['groom_item_any'] = ['__groom_item_f_hygiene__', '__groom_item_f_beauty__', '__groom_item_m_hygiene__', '__groom_item_m_grooming__', '__groom_item_unisex_care__']
    G['groom_prompt'] = ['__groom_item_any__ It sits on __groom_surface__. The light is __groom_light__. __groom_frame__']
    G['groom_female_prompt'] = ['__groom_item_female__ It sits on __groom_surface__. The light is __groom_light__. __groom_frame__']
    G['groom_male_prompt'] = ['__groom_item_male__ It sits on __groom_surface__. The light is __groom_light__. __groom_frame__']
    ep += ['groom_prompt', 'groom_female_prompt', 'groom_male_prompt', 'groom_item_female', 'groom_item_male', 'groom_item_any']
    G['v104_grooming_entry_points'] = ep
    return G
