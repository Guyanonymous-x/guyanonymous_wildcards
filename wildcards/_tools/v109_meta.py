import v109_build as _B
ONELINE = "350-location conversion, every object kind with its own wildcards, era objects and architectural fixtures, trading cards, card and board games, adventure and workout activities, medical scenes and quoted sportswear text"
BULLETS = [
 "Locations: the 350 Locations inventory (1,422 places in 20 groups, from homes and workplaces to hospitals, transport and odd places) converted into per-place pools (`loc_<group>_<place>_*`) with scene, people, time, era and regional prompts. Real brand names are replaced by descriptions of their look (and added to the brand styles), child-related places are never sexual, and measurements are left out.",
 "Objects: every object kind named in the inventory (about 930 new builders, `ob_<object>_*`) with its own forms, materials, wear, details and quoted text where text belongs (labels, books, tickets, signs); city sign lines now quote names from the name generators.",
 "Era objects: 230 objects that changed over time (phones, radios, cookers, furniture, clothing, tools, toys, fixtures and more) have period descriptions from before 1800 to today (`ob_<object>_era_<period>`, `ob_<object>_period`).",
 "Architectural fixtures: 79 new builders for doors, windows, walls, floors, ceilings, staircases, lifts, escalators, roofs, fireplaces and more, with quoted house and floor numbers where they belong.",
 "Trading cards (`tc_`): sports (invented teams with quoted names and numbers on the shirts), film, artist and musician, superhero, creature, wildlife, dinosaur, vehicle, space and game cards in seven decade styles; five grades of card condition; graded cases; card backs; packs and boxes sealed and opened with gum and inserts; albums, sleeves and storage; desk and wall displays.",
 "Card games (`cg_`): 20 kinds of special-deck card games, unbranded and described by look and rules (four-suit trick game, road-race game in five themes, tarot, playing cards, picture, stats, shedding, party, collectible battle, flower cards and more), with every text area on the cards quoted, boxes, parts and score pads, and games shown dealing, dealt, in play and finished.",
 "Board and tabletop games (`bg_`): a property-trading game in seven themes plus 35 more family games (chess, draughts, backgammon, word tiles, mystery, conquest, trains, mahjong, dominoes, jigsaws, bingo and more) with boards, pieces, cards, boxes, stages and top-down views.",
 "Activities (`adv_`): 71 adventure, extreme, solo outdoor and workout activities, each named and described in plain words, with outfits, equipment, poses for women and men, freely mixed places with matching light, weather and camera views.",
 "Medical scenes (`med_`): clinical, nonsexual examinations, treatments and surgery for the health locations, with draping and chaperones for intimate examinations, in seven decades from the 1700s to the 2010s.",
 "Library fixes: body builds now follow the age of the person, 'no visible signs of aging' rewritten positively, and every number, name or name tape on sportswear and uniforms is quoted.",
 "Showcase files (40 prompts at 1024 and 1408 pixel counts, steps 50, cfg 3.75) and 100 sample prompts are included.",
]
README = """Guyanonymous' Wildcards v109 - 350-location conversion, object builders, era objects, fixtures, trading cards, card and board games, activities, medical scenes
Prompts  loc_scene, loc_people, loc_era_scene, tc_any_prompt, tc_packaging_any_prompt, cg_any_prompt, cg_topdown_any_prompt, bg_all_any_prompt, bg_topdown_any_prompt, adv_any_prompt, med_scene_any, med_scene_decade_any
"""
GEN_ROW = '("locations, objects, games, activities v109","features","v109 350-location conversion, object builders, era objects, fixtures, trading cards, card and board games, activities, medical scenes."),'
DOCS = ['/home/claude/w/docs/INDEX_v109.txt', '/home/claude/w/docs/STANDING_RULES.txt', '/home/claude/w/docs/NAME_SYSTEM.txt']
SAMPLES = [('location scene', '__loc_scene__', 4), ('location people', '__loc_people__', 2), ('trading card', '__tc_any_prompt__', 4), ('trading card packaging', '__tc_packaging_any_prompt__', 2),
           ('card game', '__cg_any_prompt__', 3), ('board game', '__bg_all_any_prompt__', 3), ('activity', '__adv_any_prompt__', 4), ('object', '__ob_any_full__', 3),
           ('any name prompt', '__name_any_prompt__', 4), ('brand style any', '__bs_prompt__', 6), ('adult L1', '__adult_l1_full_prompt__', 3), ('garment', '__clothing_garment_prompt__', 4), ('drink', '__obj_drink_prompt__', 3)]
