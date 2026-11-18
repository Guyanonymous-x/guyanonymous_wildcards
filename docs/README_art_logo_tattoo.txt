ARTWORK-ON-OBJECTS, LOGOS AND TATTOOS  (new in v13)
====================================================
Three separate wildcard systems for the "images, marks and designs" that appear on products, materials and skin.  Everything is original descriptive wording: no real brands, characters, trademarks or people.

1) ARTWORK ON AN OBJECT  - start with  __art_on_object__  (or __art_set__ for one or two images)
   art_subject (picks from art_subject_animal / plant / myth / sky / object / scene / symbol / abstract / pattern: about 10,000 subjects, animals with poses, hybrids, scenes)
   art_style (about 380 styles and blends: ukiyo-e, mud-cloth, risograph, vaporwave, folk art, scientific plate, pixel art ...)
   art_technique (screen-printed, hand-embroidered, tooled, enamelled, inlaid ... and pairs)
   art_layout, art_scale, art_feel, art_placement, art_colourway (1,500 colour schemes)
2) LOGOS  - start with  __logo_mark__  (or __logo_set__)
   logo_type, logo_subject (about 1,200), logo_style (about 250), logo_lettering, logo_name (about 3,000 invented names - check them for accidental matches with real brands before commercial use), logo_initials, logo_colour, logo_treatment (embossed, woven label, enamel pin ...), logo_placement
3) TATTOOS  - start with  __tattoo_set__  (one to many tattoos),  __tattoo_one__  (a single one) or  __tattoo_cover__  (sleeves, back pieces)
   tattoo_style (about 215), tattoo_subject (about 3,600), tattoo_ink, tattoo_size, tattoo_placement (arms, hands, neck, back, legs, feet and head; no intimate areas), tattoo_condition
   Person prompts:  f_prompt_tattooed and m_prompt_tattooed  (adult prompt + tattoos)

Links:  every accessory 'extras' slot can now add  __acc_artwork__  (a sentence with artwork or a logo), so bags, hats, rings and so on pick up images and marks.
Build:  _tools/art_build.py  (vocabulary in _tools/vocab_art.py, vocab_art2.py).  The all-options-once set has the same lists as aoo_art_*, aoo_logo_*, aoo_tattoo_*.
