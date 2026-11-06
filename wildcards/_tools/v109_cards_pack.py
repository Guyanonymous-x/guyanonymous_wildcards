"""v109 - trading card packaging, extras, storage, displays and condition (user 2026-11-06), added to the v109_cards generator.
Packs (sealed and opened) and boxes of packs (sealed and opened) in the look of each decade; what comes inside a pack (cards, a stick of
bubblegum, a temporary tattoo sheet, a sticker sheet, a checklist card); album pages, sleeves and cases; desk and wall displays;
condition pools for single cards (corners, edges, surface, centring) and for packs and boxes. All printed text is quoted.

Files: tc_pack_<d>_wrapper, tc_pack_wrapper, tc_pack_art, tc_pack_count, tc_pack_condition, tc_box_<d>_look, tc_box_look, tc_box_condition,
       tc_gum, tc_tattoo_sheet, tc_sticker_sheet, tc_checklist, tc_pack_insert,
       tc_pack_sealed_prompt, tc_pack_opened_prompt, tc_box_sealed_prompt, tc_box_opened_prompt, tc_pack_contents_prompt,
       tc_storage_<kind>, tc_storage_prompt, tc_display_desk, tc_display_wall, tc_display_desk_prompt, tc_display_wall_prompt,
       tc_card_corners, tc_card_edges, tc_card_surface, tc_card_centring, tc_card_condition_full, tc_packaging_any_prompt."""
from v109_cards import DECADES

PACK = {
 '1930s': ['a small 1930s paper wrapper folded around the cards and sealed with a dab of glue, printed in two flat colours', 'a slim 1930s envelope of thin printed paper with a scalloped flap'],
 '1950s': ['a 1950s waxed paper wrapper folded at the ends, printed in bright red, yellow and blue, slightly translucent with the shape of the gum showing through', 'a 1950s wax wrapper with a printed cartoon mascot'],
 '1970s': ['a 1970s pack of shiny waxed paper with folded ends, printed with bold colour stripes', 'a 1970s pack of clear crinkly cellophane showing the top card through the wrapper'],
 '1980s': ['a 1980s waxed paper pack with bold diagonal stripes and a star burst, the ends folded and sealed', 'a 1980s hanging pack of three clear plastic pockets of cards on a printed card'],
 '1990s': ['a 1990s shiny foil pack with crimped ends, printed with holographic swirls', 'a 1990s jumbo foil pack, thick and heavy, with metallic lettering'],
 '2000s': ['a 2000s silver foil pack with crimped ends and chrome-effect graphics', 'a 2000s pack in black foil with a gold seal strip'],
 '2020s': ['a 2020s matte foil pack with a minimal design and a tear notch at the top', 'a 2020s clear plastic pack with a cardboard top strip and a hole for hanging on a shop peg'],
}
BOX = {
 '1930s': ['a small 1930s cardboard counter box with a printed lid that folds up into a display'],
 '1950s': ['a 1950s cardboard display box with a printed lid that props up, holding neat rows of waxed paper packs'],
 '1970s': ['a 1970s cardboard display box of 36 waxed paper packs with a bold printed tuck-in lid'],
 '1980s': ['a 1980s display box of 36 waxed paper packs with a pop-up header printed in neon colours'],
 '1990s': ['a 1990s glossy display box of 24 foil packs with holographic printing on the lid'],
 '2000s': ['a 2000s heavy collector\'s box in black card with silver foil lettering, holding 24 packs'],
 '2020s': ['a 2020s compact collector\'s box with a lid held shut by magnets and a matte finish', 'a 2020s shop box with a clear plastic window showing the packs inside'],
}
PACK_ART = ['a cut-out action picture of __tc_sport_basketball_subject_m__', 'a painted picture of __tc_creature_subject__', 'a bold illustration of __tc_superhero_subject__',
            'a picture of __tc_dinosaur_subject__', 'a picture of __tc_vehicle_subject__', 'a collage of film stills', 'a picture of __tc_sport_football_subject_w__', 'a starburst behind a large card back design']
COUNT = ['10 CARDS', '8 CARDS', '12 CARDS + GUM', '5 CARDS', '6 CARDS + 1 STICKER', '15 CARDS']
PACK_COND = ['sealed, crisp and bright as new', 'sealed, the wrapper crinkled all over', 'sealed but badly sun-faded, the colours washed out to pale blue and pink', 'sealed, with one end split open and a card edge poking out',
             'sealed but crushed flat, with deep folds across the wrapper', 'sealed, with a greasy wax stain from the gum spreading across the front', 'sealed, the corners scuffed white and the print rubbed through', 'sealed, water-damaged and rippled']
BOX_COND = ['still in its tight factory shrink-wrap', 'with the shrink-wrap torn open at one corner and hanging loose', 'with one corner caved in and crushed', 'with the printed lid badly faded by sunlight', 'in near-perfect condition',
            'with the bottom edges worn through to grey cardboard', 'with a brown water stain across the lid and the card warped', 'with old price stickers and tape marks on the lid']
GUM = ['a flat pink stick of bubblegum dusted with white powder', 'a brittle pink slab of bubblegum the size of a card, cracked across the middle', 'a small wrapped piece of bubblegum in waxed paper']
TATTOO = ['a small sheet of temporary tattoos on glossy backing paper, printed with stars, lightning bolts and a flaming ball',
          'a temporary tattoo sheet with tiny coloured pictures of a dragon, a rocket, a crown and a paw print',
          'a strip of temporary tattoos showing small shield-shaped crests in bright colours']
STICKER = ['a small sheet of shiny stickers shaped like stars, shields and balls', 'a sticker sheet of team crests, one reading "__tc_team__" under a bird-shaped emblem',
           'a puffy sticker of a cartoon mascot', 'a holographic sticker of a dragon', 'a sticker sheet with the set name "__tc_set_name__" across the top and small pictures below']
CHECKLIST = ['a checklist card with a printed list headed "CHECKLIST" at the top and small tick boxes down one side']
# Most packs hold only the gum; some hold the gum and one other extra.
INSERT = ['__tc_gum__'] * 6 + ['__tc_gum__ and __tc_tattoo_sheet__', '__tc_gum__ and __tc_sticker_sheet__', '__tc_gum__ and __tc_checklist__']
STORAGE = {
 'album_page': ['a clear plastic nine-pocket album page holding nine cards in three rows', 'a clear plastic four-pocket album page holding four large cards', 'a black-backed album page with clear pockets that make the cards stand out'],
 'sticker_album': ['an open sticker album with printed spaces outlined for each card, some filled and some empty, the page headed "__tc_set_name__"'],
 'binder': ['a thick padded zip binder with a side strap, open to show pages of cards', 'a ring binder with a printed cover, standing on a shelf beside others'],
 'sleeve': ['a thin soft clear plastic sleeve slipped over a card', 'a stiff clear plastic holder open at one end, holding a single card', 'a thick clear plastic case that snaps shut with magnets, holding one card', 'a resealable clear bag holding a stiff plastic card holder'],
 'box': ['a long white cardboard storage box packed with cards in rows, the lid set beside it', 'a small wooden box with a hinged lid, lined with felt and holding a stack of cards', 'a tin with a printed lid holding a thick stack of cards held by an elastic band'],
}
DESK = ['a small clear acrylic block holding one card upright on a desk', 'a wooden stand with a slot cut in the top holding a single card at an angle', 'a small chrome easel holding a graded card case',
        'a row of five cards in clear cases standing in a long acrylic stand on a desk', 'a small glass-domed display holding one card on a wooden base', 'a clear acrylic tiered stand holding three rows of cards in cases']
WALL_ONE = ['a deep black shadow-box frame holding one card behind glass on a white mat', 'a single floating clear acrylic wall holder with one card', 'a small gilt frame holding one graded card case']
WALL = ['a wall frame with a grid of nine cards behind glass', 'a long thin wooden ledge on a wall with a row of cards in cases leaning along it',
        'a glass-fronted wall cabinet with lit shelves of graded cards', 'a large framed display of twenty cards in four rows on a coloured mat', 'a set of floating clear acrylic wall holders, each with one card, arranged in a neat grid']
CORNERS = ['sharp square corners', 'slightly soft corners', 'one rounded corner', 'all four corners worn round', 'a dinged corner']
EDGES = ['clean edges', 'small white flecks along the edges where the coloured border has worn away', 'a rough cut edge', 'one edge slightly frayed']
SURFACE = ['a clean glossy surface', 'a faint scratch across the picture', 'a small dark printing speck on the picture', 'a faint wax stain', 'a light crease across the middle', 'a dent pressed into the surface', 'a sun-faded picture']
CENTRING = ['perfectly centred borders', 'borders a little wider on one side', 'a picture sitting noticeably off-centre', 'a printed frame that sits slightly tilted on the card']

def fix(G, final=None):
    for d in DECADES:
        G['tc_pack_%s_wrapper' % d] = PACK[d]; G['tc_box_%s_look' % d] = BOX[d]
    G['tc_pack_wrapper'] = ['__tc_pack_%s_wrapper__' % d for d in DECADES]; G['tc_box_look'] = ['__tc_box_%s_look__' % d for d in DECADES]
    G['tc_pack_art'] = PACK_ART; G['tc_pack_count'] = COUNT; G['tc_pack_condition'] = PACK_COND; G['tc_box_condition'] = BOX_COND
    G['tc_photo_item'] = ['Sharp product photograph with true colours and fine detail of the print and materials.', 'Clean studio photograph with soft shadows and crisp focus.', 'Natural light photograph with a shallow depth of field.']
    G['tc_gum'] = GUM; G['tc_tattoo_sheet'] = TATTOO; G['tc_sticker_sheet'] = STICKER; G['tc_checklist'] = CHECKLIST; G['tc_pack_insert'] = INSERT
    G['tc_card_corners'] = CORNERS; G['tc_card_edges'] = EDGES; G['tc_card_surface'] = SURFACE; G['tc_card_centring'] = CENTRING
    G['tc_card_condition_full'] = ['__tc_card_corners__, __tc_card_edges__, __tc_card_surface__ and __tc_card_centring__']
    text = 'The front of the wrapper is printed with the set name "__tc_set_name__" across the top and "__tc_pack_count__" in one corner, with %s.' % '__tc_pack_art__'
    G['tc_pack_sealed_prompt'] = ['A single unopened trading card pack lying on a wooden table. It is %s. %s The pack is %s. __tc_photo_item__' % ('__tc_pack_%s_wrapper__' % d, text, '__tc_pack_condition__') for d in DECADES]
    G['tc_pack_opened_prompt'] = ['A trading card pack just torn open on a table, the wrapper peeled back and the cards fanned out beside it. The pack is %s. %s Spilled out with the cards is __tc_pack_insert__. The top card is __tc_any_short__. __tc_photo_item__' % ('__tc_pack_%s_wrapper__' % d, text) for d in DECADES]
    G['tc_pack_contents_prompt'] = ['The contents of one opened trading card pack laid out neatly on a white table and photographed from above, showing a fanned stack of cards with the top one being __tc_any_short__, and __tc_pack_insert__, with the torn wrapper, __tc_pack_wrapper__, lying beside them. __tc_photo_item__']
    G['tc_box_sealed_prompt'] = ['A sealed box of trading card packs standing on a shop counter. It is %s, %s. The lid is printed with the set name "__tc_set_name__" in large letters. __tc_photo_item__' % ('__tc_box_%s_look__' % d, '__tc_box_condition__') for d in DECADES]
    G['tc_box_opened_prompt'] = ['An opened box of trading card packs on a table, %s, with the lid folded back to show rows of packs standing on end, each one %s, a few already taken out and lying beside the box. The lid is printed with the set name "__tc_set_name__". __tc_photo_item__' % ('__tc_box_%s_look__' % d, '__tc_pack_%s_wrapper__' % d) for d in DECADES]
    for k, v in STORAGE.items(): G['tc_storage_%s' % k] = v
    G['tc_storage'] = ['__tc_storage_%s__' % k for k in STORAGE]
    G['tc_storage_prompt'] = ['A trading card collection kept in %s, lying on a desk. The cards include __tc_any_short__ and __tc_any_short__. __tc_photo_item__' % ('__tc_storage_%s__' % k) for k in STORAGE]
    G['tc_display_desk'] = DESK; G['tc_display_wall'] = WALL
    G['tc_display_desk_prompt'] = ['A collector\'s desk with __tc_display_desk__, showing __tc_any_short__, beside a lamp and a mug. __tc_photo_item__']
    G['tc_display_wall_one'] = WALL_ONE
    G['tc_display_wall_prompt'] = ['A room wall with __tc_display_wall__, the cards including __tc_any_short__ and __tc_any_short__, lit by a soft spotlight. Interior photograph with true colours.',
                                   'A room wall with __tc_display_wall_one__, the card being __tc_any_short__, lit by a soft spotlight. Interior photograph with true colours.']
    G['tc_packaging_any_prompt'] = ['__tc_pack_sealed_prompt__', '__tc_pack_opened_prompt__', '__tc_pack_contents_prompt__', '__tc_box_sealed_prompt__', '__tc_box_opened_prompt__',
                                    '__tc_storage_prompt__', '__tc_display_desk_prompt__', '__tc_display_wall_prompt__']
    return G
