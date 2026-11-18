ACCESSORY SYSTEM (v10): hats, backpacks, purses, wallets, necklaces, bracelets, rings, socks, canes and walking sticks
====================================================================================================================
Built from 9,000 supplied example prompts (1,000 per category). Every example follows one grammar, so the examples were split back into their parts and each
part became its own wildcard file. Recombining the parts gives richly described, fully random objects that nobody wrote. Prices were ignored.

THE GRAMMAR (and the file that supplies each part)
  <lead-in> <grade word> <item type>, made of <material, construction>.        acc_lead, acc_adj_<grade>, acc_<c>_cluster_<grade>, acc_<c>_mat_*_<grade>
  <shape / hardware sentences that belong to that item type>.                  (inside the cluster line, so a roll-top never gets a flap)
  Designed by <tradition>, <palette>; its signature detail is <motif>, <technique>.   acc_<c>_design (48 traditions x their palettes x their motifs), acc_<c>_tech_<grade>
  Practical details ... / Whimsical touches ... / Alongside X it adds Y.        acc_<c>_extras (practical and whimsy pools of 40-100 items each)
  <decoration>  <finish>  <lining>                                             acc_<c>_trim_/finish_/lining_<grade> (blank lines = none)

GRADES (replace the price tiers): basic, practical, standard, fine, luxury, showpiece. They set how fine the material, hardware, technique and decoration are
(acrylic and plastic zippers at "basic", exotic leathers, gold and gemstones at "showpiece"). Price words (affordable, inexpensive, mid-priced ...) are not used.

WHERE TO START
  __acc_prompt__               one full accessory description, any category, any grade
  __acc_<c>_prompt__           one category (c = hat, backpack, purse, wallet, necklace, bracelet, ring, sock, cane)
  __acc_<c>_prompt_<grade>__   one category at one grade, e.g. __acc_ring_prompt_luxury__
  __acc_<c>_short__            a compact phrase, e.g. "a sturdy sling backpack made of waxed canvas, coloured in ..."
  __acc_wear__                 a person wearing or carrying one to three of them;  f_/m_prompt_accessorized = the age-weighted person prompt + accessories
  Build your own: __acc_<c>_cluster_<grade>__, __acc_<c>_design__, __acc_<c>_extras__ ... (all in the table above).

NOTES
- Adult-only: item types and lines for children, babies and toddlers were removed (8% of the examples); "men's" / "women's" were removed from item names.
- Hats use up to 10 material families (a straw hat does not get felt); the other categories use one family.
- Because the person prompts already contain hats, jewellery and bags, f_/m_prompt_accessorized adds a second, richer accessory description; use it instead of the plain master when you want a detailed object.
- Source data: _tools/data/accessories (the prompts without prices, plus type / tradition / material of each); builder: _tools/accessory_build.py (last step of build_all.py).
- The "all options once" set has aoo_acc_* files and aoo_prompt_accessorized.


v12 UPDATE - ACCESSORY EXPANSION
--------------------------------
Every acc_* slot file now has real content; none is blank-only, and every pool file has 200+ distinct lines
(only the small prompt templates acc_<cat>_prompt_<grade> / acc_<cat>_prompt stay short, by design).
- New authored vocabulary (_tools/vocab_acc_a.py, vocab_acc_b.py, acc_expand.py): materials, constructions and makers by
  grade band, technique lines, trim / finish / interior / hardware / carry slots, practical features, whimsy placements,
  ~12 extra item types per category with form sentences, adverb-expanded grade adjectives, 400+ lead-ins with settings.
- New files per category and grade: acc_<cat>_hardware_<grade> (and acc_<cat>_carry_<grade> for backpack, purse, wallet).
  Bracelets and necklaces now have separate metal (mat_all) and bead/cord (mat_bead) material files.
- Prompt templates now have 5 ordering variants per grade.


v13 UPDATE - BACKPACKS, EXTRAVAGANCE, FOOTWEAR NAMING
-----------------------------------------------------
BACKPACKS (about 140 shapes, from research on sculptural, artist-made, camping and hauling packs)
- acc_backpack_prompt now mixes three families: conventional (acc_backpack_prompt_<grade>), strange/sculptural (acc_backpack_prompt_odd_<grade>) and utility (acc_backpack_prompt_util_<grade>); odd and utility are weighted two to one over conventional.
- Odd shapes (acc_backpack_cluster_odd_<grade>): prisms, cones, spheres, origami and accordion forms, inflatables, turtle-shell, creature, house, radio, cassette and lantern backpacks, baskets, nets, exoskeleton, jellyfish, and so on, in experimental materials (acc_backpack_mat_odd_<grade>: mushroom leather, inflatable PVC, holographic film, rope, cork, chainmail, glass, carbon fibre ...), with odd features, straps and poses.
- Utility packs (acc_backpack_cluster_util_<grade>): internal-frame, external-frame, hybrid and frameless trekking packs, expedition, canoe-portage (Duluth), pack baskets, wooden pack frames, tumpline packs, military rucksacks, MOLLE, hunting haulers, climbing and ski packs, avalanche packs, dry packs, duffel backpacks, sea bags, haul bags, camera, cooler and tool packs. Files: acc_backpack_frame, acc_backpack_gear (strapped-on camping gear), acc_backpack_utilfeature.
- Colours: acc_backpack_colour (1,500 colour schemes from about 240 colours with modifiers and patterns) is used by acc_backpack_design, so colours no longer repeat; 18 new design traditions (Dada, Bauhaus, Memphis, kinetic, origami engineer, Brutalist ...).
EXTRAVAGANCE (all accessories)
- The luxury and showpiece grades now include ludicrous materials, trims, finishes and linings: gem-covered surfaces, chinchilla/fox/mink fur, ostrich and peacock feathers, leaded stained glass, solid gold sheet, rock crystal, meteorite, opal inlay, Murano glass and more (_tools/vocab_acc_extrav.py).
FOOTWEAR
- Shoe files follow the accessory naming: shoe_<x>_t<n> is now acc_shoe_<x>_<grade> (t1 = basic ... t6 = showpiece), shoe_<x> is acc_shoe_<x>; start with __acc_shoe_prompt__ (= acc_shoe_prompt_master). Shoes are included in acc_prompt, acc_short_any and acc_wear. _tools/shoe_rename.py does the renaming and fixes all references.

v15: novelty and historical hats, funny/novelty socks, and wide-colour designs now cover every accessory category.

v17: socks now include 42 sock styles (22 ankle-height: anklet, ankle, no-show, low-cut, footie, ruffled and lace anklets, sneaker liners ...) and odd, translucent and unusual materials in every grade
(clear vinyl, sheer silk, net and fishnet, tulle, fur, shearling, leather, suede, latex and rubber, metal wire and chainmail, glass-bead fabric, feathers, rope, paper, fibre-optic).
New files: acc_sock_length, acc_sock_length_ankle, acc_sock_oddform, acc_sock_mat_odd_<grade>, acc_sock_cluster_odd_<grade>, acc_sock_cluster_ankle_<grade>, acc_sock_prompt_odd_<grade>, acc_sock_prompt_ankle_<grade>.
v17: 20 thigh-high styles (thigh-high socks and stockings, stay-ups, lace-topped, cable-knit, garter-belt, back-seam, leg warmers, boot socks, toe socks...): acc_sock_length_thigh, acc_sock_cluster_thigh_<grade>, acc_sock_prompt_thigh_<grade>.


v18 additions
-------------
TWENTY-TWO NEW ACCESSORY FAMILIES, built to the same six-grade system and file structure as the first nine (acc_<c>_prompt, _prompt_<grade>, _short, _cluster_<grade>, _mat_all_<grade>, _design, _tech_<grade>, _extras, _trim_/_finish_/_lining_/_hardware_<grade>, _practical, _whimsy, plus _mat_odd_/_cluster_odd_/_prompt_odd_<grade> for unusual materials):
  earring, glove, scarf, tights, cufflink, belt, brooch, watch, necktie, hairpiece, umbrella, fan, apron, bodyjewel, keychain, handkerchief, lanyard, charm, pouch, cigcase (cigarette cases), lighter, contact (contact lenses: colour-changing, cosmetic, costume and novelty).
Every family has 30-50 item types drawn from many cultures and eras (for example jhumka and Maasai disc earrings, falconry gauntlets and Sami mittens, kente stoles and keffiyeh-style wraps, uchiwa and brisé fans, wagasa umbrellas, Zippo-style lighters, cat-eye and sclera-look lenses).
acc_prompt, acc_short_any, acc_wear and acc_wear_one now include all new families.

FOOTWEAR: THREE NEW CLASSES (acc_shoe_*_platform, _novelty, _exotic)
  platform - platform sneakers, boots, sandals, creepers, geta, chopines, disco and glam-rock styles
  novelty  - clown shoes, jester and elf shoes, animal-paw slippers, light-up and roller sneakers, aquarium-heel shoes, winged shoes, costume boots
  exotic   - dancer's stiletto pumps, clear platform heels, pole boots and thigh-high platform boots
They have their own purposes and audiences and are included in acc_shoe_full, acc_shoe_type and the per-grade pickers.
