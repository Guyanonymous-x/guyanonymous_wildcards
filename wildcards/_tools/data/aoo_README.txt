GUYANONYMOUS' WILDCARDS - ALL OPTIONS ONCE
==========================================
A simplified wildcard set, separate from the main library.
- Every option file (prefix aoo_) lists each distinct option exactly once, in random order: no repeated lines, so every option is equally likely.
- No gender, age or population-proportion distinctions: gendered and age-specific files are merged into one list per topic, and any line that names a gender is dropped (age wording is dropped in the human-feature files).
- Clothing, hair, poses, footwear, face, body, make-up, lighting, camera, scenes and so on each have one file.
- Five ready-made templates: aoo_prompt_full, aoo_prompt_outfit, aoo_prompt_face_and_hair, aoo_prompt_pose_and_scene, aoo_prompt_footwear. Use them as, e.g., __aoo_prompt_full__.
- _counts.json lists the number of options in every file.
Eye and hair colour are listed once each, so rare colours are as likely as common ones (use the main library for realistic proportions).
Built by _tools/simple_build.py from the main library; no { } | characters are used.
Style packs: aoo_illustration_* (illustration styles, 179 category files + presets) and aoo_photostyle_* (photographic style traits and 500 whole-style descriptions)
are included once each. Ready-made: aoo_prompt_photostyled, aoo_prompt_illustrated, aoo_style_photo_block, aoo_style_illustration_block.
Accessories: aoo_acc_* (hats, backpacks, purses, wallets, necklaces, bracelets, rings, socks, canes) - parts of rich accessory descriptions, one per file; aoo_acc_prompt picks any accessory, aoo_prompt_accessorized adds them to a person.
Garments: aoo_garment_* - any single garment on its own (shirt, trousers, skirt, dress, coat ...); aoo_garment_prompt gives one fully described garment, aoo_garment_outfit a combination.
