import v97_build as _B
ONELINE = 'a library-wide text audit: signs, posters, banners, graffiti, labels, tags, badges and lettering rewritten as plain visual nouns, engraved names and initials turned into quoted invented text'
BULLETS = ["Library-wide text audit (STANDING_RULES section 0): about 63,000 lines in 2,587 files mentioned signs, posters, banners, graffiti, labels, tags, badges, logos, lettering, inscriptions or slogans without saying what text appears, so the image model invented words. They now use plain visual nouns (lit panel, picture panel, cloth pennant, spray-painted shapes, tab, patch, motif, stitched border).",
 "Engraved names, stamped initials and monograms in accessory files now carry quoted invented text from the name system, for example the name \"__name_person__\" or the letters \"__name_initial__ __name_initial__\", so a wildcard expands to real quoted text you can edit.",
 "About 150 remaining text denials ('no text', 'no words') were removed.",
 "Not changed on purpose: badge, pin, patch and sticker files (their items are meant to carry defined text), sign_* and text_* files, and the name system.",
 "A 40-image prompt showcase at 1024 and 1408 pixel counts, steps 50, cfg 3.75, no trailing blank line, and 100 random sample prompts."]
README = """Guyanonymous' Wildcards v97 - library-wide text audit
Prompts  every existing prompt family now avoids undefined text; name_* prompts supply quoted text
"""
GEN_ROW = '("text audit","63,000 lines","v97 undefined text rewritten."),'
DOCS = ['/home/claude/w/docs/INDEX_v97.txt', '/home/claude/w/docs/STANDING_RULES.txt', '/home/claude/w/docs/NAME_SYSTEM.txt']
SAMPLES = [('any name prompt', '__name_any_prompt__', 20), ('brand style any', '__bs_prompt__', 20), ('keychain', '__acc_keychain_prompt__', 10), ('glove', '__acc_glove_prompt__', 10), ('outerwear', '__clothing_outerwear_prompt__', 10), ('garment', '__clothing_garment_prompt__', 10), ('drink', '__obj_drink_prompt__', 10), ('business card', '__name_business_card_prompt__', 5), ('adult L1', '__adult_l1_full_prompt__', 3), ('pinback', '__pinback_prompt__', 2)]
