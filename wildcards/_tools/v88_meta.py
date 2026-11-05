import v88_build as _B
ONELINE = '25 more brand styles image-checked and rewritten as product-neutral essence descriptions'
BULLETS = ["25 more brand styles rewritten after checking image grids: Rolls-Royce, Mini, Land Rover, Volkswagen, BMW, Mercedes-Benz, Toyota, Tesla, Louis Vuitton, Gucci, Hermes, Ralph Lauren, Lacoste, Tiffany and Co, Lego, Vans, Converse, Pepsi, Guinness, Starbucks, McDonalds, Braun, Nintendo, Rolex, Harley-Davidson.",
 "Each style describes transferable design language (shapes, materials, finish, palette, lettering, photography) usable on any product, with no named parts or models.",
 "Default `maker_bs_<brand>` gives the style only; `_named` adds the name. Research notes are in docs/RESEARCH_v88_brands_batch2.txt.",
 "A 40-image prompt showcase at 1024 and 1408 pixel counts, steps 50, cfg 3.75, no trailing blank line, and 100 random sample prompts."]
README = """Guyanonymous' Wildcards v88 - 25 more image-checked brand styles
Brands  maker_bs_<brand>, maker_bs_<brand>_named, bs_prompt, bs_prompt_named
"""
GEN_ROW = '("maker_bs_*","25 updated","v88 image-checked brand styles."),'
DOCS = ['/home/claude/w/docs/INDEX_v88.txt', '/home/claude/w/docs/RESEARCH_v88_brands_batch2.txt', '/home/claude/w/docs/RESEARCH_v85_brands_top25.txt']
SAMPLES = [('brand style any', '__bs_prompt__', 40), ('brand named', '__bs_prompt_named__', 40), ('adult L1', '__adult_l1_full_prompt__', 10), ('pinback', '__pinback_prompt__', 10)]
