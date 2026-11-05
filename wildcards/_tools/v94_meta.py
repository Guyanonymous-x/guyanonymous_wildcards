import v94_build as _B
ONELINE = 'a fake name system for signs, labels, packaging, business cards, logos, caps and t-shirts, books and comics'
BULLETS = ["A fake name system: invented brand stems (Latin, Nordic, German, tech, Japanese), surnames, first names and trade words, built into company, shop, restaurant, pub, product, person, address, hero, villain, author, book, comic, band, movie and magazine names.",
 "26 business types, each with its own name file and sign prompt (liquor store, bar, pharmacy, bookshop, bakery, cafe, hotel, garage, cinema and more), with a matching extra line such as OPEN or Cold Beer.",
 "Packaging prompts where name, product type, flavour and weight agree: soft drinks, sweets, savoury food, spirits and beer, household goods.",
 "Business cards: eight positioned layouts (corner, centred, split, minimal, corporate, vertical, front and back, trade) with company, website, email, phone and address that agree. Websites end in .example and phones use 555.",
 "Fake logos: a described symbol, style, colour, layout and quoted wordmark, in logo, letterhead, stamp and sign prompts. Baseball caps, t-shirts, hoodies, tote bags and mugs carry defined text or logos.",
 "Older sign, advert and label prompts (about 170 files) now draw from the system through text_brand, text_shop_name, text_pub_name, text_ship_name, text_card_name and text_map_name.",
 "Every text-bearing prompt quotes each line of text and ends with a no-other-words statement, so the image model does not invent words. See docs/NAME_SYSTEM.txt.",
 "A 40-image prompt showcase at 1024 and 1408 pixel counts, steps 50, cfg 3.75, no trailing blank line, and 100 random sample prompts."]
README = """Guyanonymous' Wildcards v94 - fake name system, business cards, logos, caps and t-shirts
Prompts  name_any_prompt, name_business_card_prompt, name_logo_prompt, name_cap_prompt, name_tshirt_prompt, name_business_sign_prompt, name_media_prompt
"""
GEN_ROW = '("name_*","300 new","v94 fake name system."),'
DOCS = ['/home/claude/w/docs/INDEX_v94.txt', '/home/claude/w/docs/NAME_SYSTEM.txt', '/home/claude/w/docs/INDEX_v93.txt']
SAMPLES = [('any name prompt', '__name_any_prompt__', 35), ('business card', '__name_business_card_prompt__', 15), ('logo', '__name_logo_prompt__', 10), ('cap', '__name_cap_prompt__', 8), ('t-shirt', '__name_tshirt_prompt__', 8), ('brand style any', '__bs_prompt__', 12), ('brand named', '__bs_prompt_named__', 8), ('adult L1', '__adult_l1_full_prompt__', 2), ('pinback', '__pinback_prompt__', 2)]
