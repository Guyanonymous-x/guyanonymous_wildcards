import v92_build as _B
ONELINE = '80 more image-checked brand styles, object design only'
BULLETS = ["80 more brand styles rewritten after checking image grids, as object design language only (no photography, advertising, settings or people): Carhartt, Puma, Uniqlo, Vivienne Westwood, Swatch, Marimekko, Hunter, Stetson, New Balance, The North Face, Supreme, Salomon, Yeti, Victorinox, Columbia Sportswear, Canada Goose, Playmobil, Hot Wheels, Barbie house style, Mattel, Fisher-Price, Sanrio, Aardman, Hanna-Barbera, Taschen, Blue Note Records, Heineken, Cadbury, Toblerone, Haribo, Heinz, Campbell, Tabasco, Marmite, Hershey, Nescafe, Kikkoman, Milo, Bang & Olufsen, Leica, Polaroid, Canon, Casio, Seiko, Omega, Dyson, Smeg, KitchenAid, Fender, Gibson, Marshall Amplification, Samsung, Ducati, Vespa, Royal Enfield, Pan Am, British Airways, Lufthansa, Emirates, NASA, London Underground posters, Routemaster, Shinkansen, Herman Miller, Knoll, Vitra, Alessi, Kartell, Le Creuset, Wedgwood, Meissen, Lalique, Georg Jensen, Iittala, Anglepoise, Liberty, Morris and Co, Pyrex, Tupperware, Chevrolet.",
 "Each brand has `maker_bs_<brand>` (style only), `maker_bs_<brand>_named` and the research notes are in docs/RESEARCH_v92_brands_batch4.txt.",
 "A 40-image prompt showcase at 1024 and 1408 pixel counts, steps 50, cfg 3.75, no trailing blank line, and 100 random sample prompts."]
README = """Guyanonymous' Wildcards v92 - 80 more image-checked brand styles
Brands  maker_bs_<brand>, maker_bs_<brand>_named, bs_prompt, bs_prompt_named
"""
GEN_ROW = '("maker_bs_*","80 updated","v92 image-checked brand styles."),'
DOCS = ['/home/claude/w/docs/INDEX_v92.txt', '/home/claude/w/docs/RESEARCH_v92_brands_batch4.txt', '/home/claude/w/docs/INDEX_v91.txt']
SAMPLES = [('brand style any', '__bs_prompt__', 45), ('brand named', '__bs_prompt_named__', 45), ('adult L1', '__adult_l1_full_prompt__', 5), ('pinback', '__pinback_prompt__', 5)]
