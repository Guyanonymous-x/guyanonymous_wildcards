# v109 changes (in progress, not released)

## Negations removed from framing and style files (v109_stage.py)
- frame_clarity (all 4 lines) no longer end "and no blur, haze, noise or compression artefacts"; MOSS_IMAGE_NOTES line 48 found Moss training captions annotate exactly those defects.
- frame_person_full, frame_group_full, frame_room, frame_landscape, frame_animal_quad_prompt: "nothing cropped", "nobody cropped", "no people in frame" and similar now say what is there.
- Negated quality defects (blur, haze, noise, grain, softness, "noiseless", "grainless") rewritten positively in lite_volum, illustration_texture_edge_texture, illustration_texture_overall_texture, illustration_texture_surface_texture, illustration_medium_digital_tool, photostyle_grain_texture, photostyle_era, photostyle_process_bw, photostyle_process_color, photostyle_sig_early_modernist.
- Shared object detail pools from v75 that implied printed text: ob_glass_detail ("a printed measuring scale"), ob_metal_detail ("a stamped maker's plate"), ob_paper_detail ("a stamped date", "a rubber-stamped mark").

## City signage with defined text (v109_signs.py)
- The 24 city_<type>_sign files (v65; made text-free by the v97 audit as "lit panel" wording) complete "Signage is ..." in every city_<type>_prompt, which mentioned signage without saying what it read (text rule 3). Each line keeps its sign type and gives quoted text from the matching name generator (name_ship for boat names, name_cafe, name_shop, name_town, text_menu_item, text_street and so on), one line each with its position.

## Full Location Inventory conversion (v109_locparse.py, v109_loc.py, v109_locbrands.py)
- Source: docs/location_inventory/Location_Inventory_complete.md, a pandoc export of the 350 Locations document (22 tabs). The document itself is not edited; every fix is in the converter (user 2026-11-06).
- All 1,422 records: home, ext, work, bath, food, circ, retail, culture, civic, transport, outdoor, health, odd, vehicle, depot, dwelling, secret, vice, wealth, edu. The first tab's 350 short records are skipped because each has a full-depth version later.
- The v75 pilot (325 records) is rebuilt with its IDs kept (9 retitled records mapped by ALIAS in v109_locparse). Pilot pools the full conversion no longer makes are retired; at release, remove from git every wildcards/*.txt file that is in the git clone but not in the working library (git rm), and check the count.
- Per location loc_<cat>_<name>_: items, incidental, furniture, installed, signature, materials, palette, light, traces, condition, time, region, sign (+ _a/_b halves for long pools) and prompts _clean, _scene, _scene_plus, _time_scene, _era_scene, _region_scene, _people.
- Entry points: loc_scene, loc_clean, loc_scene_plus, loc_people, loc_time_scene, loc_era_scene, loc_region_scene, and loc_<cat>_* for every category; loc_tag_<tag>_<value> indexes.
- Text rules: phrases naming printed or written things are dropped; where a record has signage, a _sign pool gives quoted name-system text matched to the business. Negated phrases are dropped or have the negated clause cut. Measurements (Dimensions & fit and any number with a unit) are never used (user 2026-11-06). The document's notes about itself are dropped.
- Real brands and organisations (text rule 6) are replaced in place by a description of their look (v109_locbrands.SUBST), e.g. "converted Airstream" -> "a converted riveted polished-aluminium travel trailer with rounded ends".
- People: adults in casual or formal outfits, one neutral action (loc_person_action), full-length framing.
- Child-related places (Education tab plus titles naming children, nurseries, playgrounds, schools; 80 records): not walled off (user 2026-11-06), but people there are adults aged 25 and over (loc_woman/man_adult25) in modest workwear filtered from the everyday clothing files (loc_outfit_modest_f/m); their scene_plus draws only on filtered anywhere pools; no phrase anywhere in the location pools puts a child in a scene (children's belongings stay); child_safe_check fails the build if adult vocabulary reaches any of these files; no adult_ file references any loc_ file.

## Brand styles added (v83_bs_transport.py, v83_bs_heritage.py, v83_bs_modern_misc.py, rows marked "v109 additions")
- 18 brands and organisations named in the Location Inventory: Airstream, Amtrak, London Underground, Caledonian Sleeper, Wagons-Lits, Nightjet, RNLI lifeboat, ADAC roadside rescue, Rega Swiss air rescue, US Coast Guard, Trinity House, Royal Navy, St John Ambulance (transport); Royal Crown Derby, Steenbeck, Lamson pneumatic tubes, Madame Tussauds (heritage); NHS (modern_misc). Written from general knowledge; not yet image-checked.

## Object builders (v109_obj.py)
- 51 new ob_<name>_* builders for the commonest location objects with no object wildcard (mug, flask, stove, curtain, key, pen, dispenser, jug, pump, piano, hose, padlock, handset, couch, tarpaulin, whiteboard, meter, soap, dish, broom, urn, trough, dehumidifier, hairbrush, rucksack, shovel, mop, hairgrip, extinguisher, detector, barrel, bollard, shutter, hairband, comb, boiler, headphones, parcel, brazier, pillow, decanter, sandwich, timer, scuttle, straw, tent, alarm, controller, carrier, trap, coil). ob_any_short / _phrase / _full cover v75 and v109 objects.

## Object builders for every object kind in the Location Inventory (v109_objall.py, data/v109_objall_review.tsv)
- All 5,737 head nouns of the location object fields were read by hand: 1,021 are real kinds of object (the rest are phrasing words, places, materials, living things, food or abstract nouns). 928 new ob_<noun>_* builders (objects with a v75 or v109_obj builder keep it).
- _type holds the forms of the object only (work glove, gardening glove, fingerless glove), from the words directly in front of the noun; materials, colours, sizes, conditions and locations are stripped. _material holds materials the document puts directly on that object (ceramic for a mug), with the class pool as a fallback (user 2026-11-06).
- 92 objects carry text and link to the name system in quotes: signs, labels, product packaging (brand and weight), books, newspapers (masthead and headline), magazines, posters, tickets, receipts, menus, cards, badges, certificates, maps, calendars, records, plaques, notices, covers, scoreboards.
- ob_any_short / _phrase / _full include the new builders. Keys that clash with shared pool names are renamed (paper -> paper_sheet, glass -> drinking_glass).
- Shared v75 class pools fixed: lines implying writing, stickers or sound (a hand-written tab, a sticker with a service number, covered in magnets and notes, thin newsprint, a hum and a faint light, a plaque) replaced with plain visual details.
- Smell, taste and sound descriptors are dropped from location and object pools unless tied to something visible (user 2026-11-06).

## Art styles (v109_art.py)
- illustration_style_scribble_line_mild: the polished looping-scribble pen portrait look from the user's first scribble-portrait tests, saved as an art style at the user's request (user 2026-11-06); also added to illustration_presets_signature_devices.

## Found, not changed (for the user to decide)
- maker_prompt lines name real brands ("the design style of Audi") - text rule 5.
- adult_l2_group and adult_l3_group: 48 structured trio lines say "No one has a hand near a groin." (v106) - negation.
- An aging-summary line "There are no visible signs of aging"; a culture line "with no headwear"; 63 m_clothing_everyday lines "... and no tie" - negations.
- "lit panel" from the v97 audit remains in about 634 files; some read badly ("a lit seatbelt lit panel").
- Stray ",." after person references in some adult_l5_panel_wm lines; ".," in adult_lN_messy_prompt.

## Era objects (v109_era.py, v109_era_data*.py)
216 era-sensitive objects (appliances, electronics, communication, lighting, transport, furniture, kitchenware, bathroom fittings, clothing, tools, office and paper goods, medical, toys, sport, street objects). Each has ob_<k>_era_<period> for the periods it existed in (before_1800, 1800s, 1900_1945, 1946_1979, 1980_1999, 2000_present), ob_<k>_period (random period) and an era-matched ob_<k>_full. Paper, cloth and leather goods use ob_era_condition_soft. New quoted text pools for newspaper, ticket and cassette.

## Medical scenes (v109_med.py, v109_med_era.py)
47 examinations and treatments (GP checks, specialist tests, imaging, screening including cervical screening, breast, prostate, rectal and testicular checks with a chaperone and draping, pregnancy care, dental, physio, dialysis, chemotherapy, emergency care, historic wards) and 17 operations, linked to the health locations. Clinician and patient poses, equipment, draping, light and camera pools. Every scene also exists per decade (1700s, 1880s, 1920s, 1950s, 1970s, 1990s, 2010s) with that decade's room, equipment, clothing, light and photographic look: med_exam_<k>_<decade>_scene, med_exam_<k>_decade_scene, med_scene_decade_any.
Clinical and nonsexual; adult patients only (pregnancy patients 18-44); no child-related places; nothing referenced from adult_ files. Clinician and patient clothing is gender-matched. Builds for patients under 65 exclude elderly build lines.
Also: location titles now take "an" before x-ray, MRI, ECG and similar (v109_loc.article).

## Library fixes (v109_fixlib.py)
- Body-build age bands: 1,562 person lines that named an age under 45 or over 64 used the 45-64 build files (v42_people.py always wrote _m_); they now use the y (18-44) or o (65+) band. Files built to mismatch on purpose (mismatched, unlinked) are untouched.
- 'There are no visible signs of aging on her/his/their face.' (90 lines) now reads 'Her/His/Their face is smooth and unlined, with the freshness of youth.'

## Architectural fixtures (v109_fixtures.py, v109_era_data_g.py)
79 fixtures that had no builder: doors and door hardware, windows and glazing, walls, floors, ceilings and their finishes (cornice, ceiling rose, skirting, architrave, dado and picture rails, panelling, wallpaper, tiling, mosaic, parquet, linoleum, terrazzo), worktops, splashbacks, kitchen islands, partitions, staircases, banisters, balustrades, newel posts, landings, lifts, escalators, fire escapes, beams, rafters, trusses, pillars, pilasters, arches, alcoves, niches, lintels, sills, thresholds, porches, verandas, balconies, parapets, roofs, gutters, chimneys, mantelpieces, hearths, window seats, shower screens, ceiling fans, fuse boxes, light switches, domes, vaults, conservatories, pergolas, cladding and gateposts. Same file set as other objects; quoted house numbers, floor numbers and carved names where text belongs; 14 have period descriptions. Fixed fittings use ob_era_condition_fixed.

## Trading cards (v109_cards.py)
tc_ generator: 15 sports (invented towns, teams and leagues), movie character, scene and poster cards (invented films and studios), painter, musician and dancer cards, superheroes, fantasy creatures, wildlife, dinosaurs, vehicles, space explorers and video game characters. Card design by decade (1930s, 1950s, 1970s, 1980s, 1990s, 2000s, 2020s), finishes, insert features (rookie and all-star badges, serial numbers, signature, fabric swatch window, first edition stamp), condition, presentation (desk, hand, sleeve, stand, opened pack, graded case), card backs with quoted stats, and binder pages. Names on cards match the pictured person's gender. Entry points: tc_any_prompt, tc_sports_prompt, tc_movie_prompt, tc_artist_prompt, tc_any_back_prompt, tc_any_decade_<decade>_prompt, tc_binder_prompt.
Packaging and storage (v109_cards_pack.py): sealed and opened packs and boxes of packs in the look of each decade; pack extras (bubblegum, temporary tattoo sheets, sticker sheets, checklist cards); album pages, sticker albums, binders, sleeves, toploaders, magnetic cases and storage boxes; desk and wall displays; card condition by corners, edges, surface and centring, plus pack and box condition. Entry points: tc_pack_sealed_prompt, tc_pack_opened_prompt, tc_pack_contents_prompt, tc_box_sealed_prompt, tc_box_opened_prompt, tc_storage_prompt, tc_display_desk_prompt, tc_display_wall_prompt, tc_packaging_any_prompt.

## Trading card condition and plain wording
Card condition is now its own sentence right after the card design, in five grades with visible damage words (perfect, almost perfect, handled and worn, heavily worn, damaged), weighted towards used cards. Graded cases only hold perfect or almost-perfect cards, with a matching grade on the label. Loose cards are photographed in light that shows wear. Pack and box condition pools are stronger (crushed, split, sun-faded, water-damaged, caved-in corners). Collector terms were replaced with plain descriptions (refractor, parallel, cracked ice, full-bleed, die-cut, hobby and blaster boxes, rack, cello and wax packs, penny sleeves, toploaders).

## Words on clothing (v109_sporttext.py)
Every line that mentioned a number, name, name patch or name tape on clothing, or a name written in marker, now quotes it from the name system (name_jersey_number, name_team, name_first, name_surname, name_town); 2,500+ lines. Sports card kits carry the team name and number on the shirt. New shared name pools: name_team, name_team_mascot, name_jersey_number.

## Activities (v109_adv.py, v109_adv_data.py)
71 activities: 39 extreme and adventure sports, 14 solo outdoor activities and 18 workouts. Each has a label with a plain description, outfits, equipment, poses for women and men, several kinds of place (so activity and place mix freely), light that follows the place, weather outdoors and camera views. Ages suit the activity (18-44, 18-64 or 18-74). Also gear flat-lay and empty-place prompts. Entry points: adv_any_prompt, adv_extreme_prompt, adv_outdoor_prompt, adv_workout_prompt, adv_pose_any, adv_any_gear_prompt.

## Card games (v109_cardgames.py)
Unbranded generators for a four-suit trick-taking game with a bird card, a road-race game of distance, hazard, remedy and safety cards, a fishing game of picture sets, a stats comparison game (cars, dinosaurs, aircraft, monsters, ships) with quoted numbers, a colour-matching shedding game with number and action cards, happy families, snap and ordinary playing cards. Single cards, hands, games in play, boxes; decade looks and condition. Entry point cg_any_prompt.
Card games, added: full decks (the trick game's 57 cards, all 52 playing cards and two jokers, a 78-card tarot deck with the 22 titled trump cards and four suits of fourteen), the road-race game in five themes going back over a century (motorcars, bicycle racing, aeroplanes, horse-drawn coaches, motorbikes) each with distance, hazard, remedy and safety cards, a 1910s look, boxes and packaging (tuck boxes, cellophane-sealed decks, tins, lidded boxes with trays, window boxes, worn boxes) and game parts (score pads with quoted headings, rules leaflets, card trays, tarot booklet and cloth, poker chips).

## Property-trading board game (v109_boardgame.py)
Unbranded board game creator in seven themes (city, seaside, space colony, medieval kingdom, wild west, underwater city, fantasy realm): boards of 40 spaces with quoted corner squares and invented street names, title deed cards with quoted prices and rents, two decks of event cards with quoted text, play money with quoted values, metal tokens, houses and hotels, dice, boxes (closed and open with tray), the whole contents laid out, and games in progress. Decade looks and condition. Entry point bg_any_prompt.

Top-down views: every card game and board game has a natural-language top-down prompt (cg_<game>_topdown_prompt, bg_<game>_topdown_prompt, cg_topdown_any_prompt, bg_topdown_any_prompt). Layout JSON versions were made and tested but are not part of the library (user decision); the method is kept in claude/LAYOUT_JSON_NOTES.md.
