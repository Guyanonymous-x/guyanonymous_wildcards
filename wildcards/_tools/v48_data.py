"""v48 data: room-specific gear and room definitions. Rooms describe the space only (no people, no poses)."""
from v40_data_a import E
GEAR = {
'gym_cardio': E("""
treadmill|a long belt on a frame with side rails, a console with buttons and a safety clip|steel and rubber
exercise bike|an upright bike with a heavy flywheel, a padded seat and a small display|steel
rowing machine|a long rail with a sliding seat, a flywheel at the front and a handle on a chain|steel and plastic
elliptical trainer|a machine with two long foot pedals that swing in an oval and two moving handles|steel
stair climber|a machine with two stepping pedals that move up and down|steel
""".replace('\n\n','\n')),
'gym_weights': E("""
squat rack|a heavy steel frame with two uprights, adjustable hooks and safety bars|steel
flat weight bench|a padded flat bench on a steel frame|steel and vinyl
adjustable incline bench|a padded bench with a back that can be set at different angles|steel and vinyl
barbell rack with plates|a tall rack holding long bars and stacks of round weight plates|steel
dumbbell rack|a two-tier rack holding pairs of hex dumbbells in size order|steel and rubber
cable crossover machine|two tall columns with pulley cables, handles and a weight stack|steel
leg press machine|a sloped seat with a large foot plate and weight plates|steel
pull-up frame|a freestanding frame with a high bar and parallel handles|steel
kettlebell shelf|a low rack with kettlebells in rising sizes|steel and iron
""".replace('\n\n','\n')),
'gym_floor': E("""
rubber gym tiles|interlocking black rubber floor tiles with a flecked surface|rubber
wall of mirrors|a full-length mirror wall with a handrail along the bottom|glass
stretching mat area|a long strip of foam mats along one wall|foam
""".replace('\n\n','\n')),
'pool': E("""
lap pool|a long rectangular pool with marked lanes and clear blue water|tile
lane rope|a floating line of discs across the water|plastic
pool ladder|a pair of shiny rails with steps leading down into the water|stainless steel
starting block|a raised platform at the end of a lane with a sloped top|composite
pool lounger|a long reclining chair with slatted back and a towel|plastic; wood
diving board|a long flexible board fixed at one end and jutting over the water|fibreglass
pool steps|wide shallow steps with a handrail at one corner|tile
""".replace('\n\n','\n')),
'yoga': E("""
yoga mat row|several mats laid out in a line on the floor|rubber
yoga block stack|a neat stack of foam blocks|foam
bolster|a long firm cylindrical cushion|cotton
yoga strap|a long strap with a metal ring buckle|cotton
wall-bar rope set|ropes hung from a wall bar for stretching|cotton
singing bowl|a wide metal bowl on a cushion with a striker|bronze
""".replace('\n\n','\n')),
'workshop': E("""
workbench|a heavy bench with a vice at one end and a tool rail|wood and steel
pegboard of tools|a wall board with hooks holding labelled shapes of hand tools|steel and wood
bench grinder|a motor with two grinding wheels on a stand|steel
tool chest|a red metal chest with rolling drawers|steel
""".replace('\n\n','\n')),
'studio': E("""
easel|a wooden tripod holding a canvas|wood
paint table|a table with tubes, jars and brushes|wood
piano|an upright instrument with a lid and a row of keys|wood
music stand|a folding black stand holding sheet music|steel
ballet barre|a long wooden rail fixed to the wall at hip height|wood
""".replace('\n\n','\n')),
'sauna': E("""
sauna bench|wide stepped wooden benches in two tiers|cedar
sauna stove|a metal stove with a basket of stones on top|steel
bucket and ladle|a wooden bucket with a long ladle|wood
""".replace('\n\n','\n')),
'shop': E("""
shop counter|a long counter with a till and a glass front|wood and glass
display shelving|tall shelves with goods in even rows|wood
coffee machine|a large chrome espresso machine with two group heads|steel
bistro table|a small round table with a single central leg|iron
booth seating|a curved padded bench around a table, fixed to the wall|vinyl
""".replace('\n\n','\n')),
'class': E("""
school desk|a small desk with a chair attached|wood and steel
teacher's desk|a larger desk at the front|wood
chalkboard|a big green board with a tray of chalk|slate
reading shelves|shelves of books in rows|wood
""".replace('\n\n','\n')),
'laundry': E("""
washing machine|a front-loading drum with a round glass door|steel
tumble dryer|a front-loading drum dryer|steel
folding table|a counter for folding|laminate
""".replace('\n\n','\n')),
}
SIZE = ['small', 'compact', 'medium-sized', 'spacious', 'large', 'very large and open', 'narrow', 'long and narrow', 'airy', 'high-ceilinged']
FLOOR = ['polished hardwood', 'pale oak boards', 'dark stained planks', 'grey concrete', 'white ceramic tiles', 'terracotta tiles', 'black and white chequered tiles', 'patterned carpet', 'plain grey carpet', 'bamboo flooring', 'woven rush matting', 'speckled stone', 'rubber flooring', 'worn parquet', 'polished marble']
WALLS = ['white painted plaster', 'pale blue paint', 'warm yellow paint', 'exposed red brick', 'wood panelling', 'sage green paint', 'terracotta-coloured plaster', 'wallpaper with a small floral pattern', 'grey concrete', 'white subway tiles', 'deep navy paint', 'whitewashed stone', 'cream paint with a dado rail']
LIGHT = ['large windows letting in soft daylight', 'warm lamplight', 'bright overhead lights', 'a skylight', 'a row of narrow windows', 'dim, warm light from wall lamps', 'low golden evening light through the glass', 'cool white light from long ceiling tubes', 'the soft glow of a single pendant lamp', 'candlelight and one lamp']
COND = ['tidy and well kept', 'lived in, with a few things out of place', 'neglected, with dust and flaking paint', 'newly refurbished', 'cluttered, every surface covered', 'sparse and uncluttered', 'worn but cared for']
STYLE = ['Scandinavian', 'Japanese', 'Mediterranean', 'mid-century modern', 'industrial', 'rustic farmhouse', 'Victorian', 'art-deco', 'contemporary minimalist', 'Moroccan', 'colonial', 'Indian', 'traditional Chinese', 'West African', 'Latin American', 'Middle Eastern']
# key: (label, brief refs, full refs)
R = {
'living_room': ('living room', ['seat_mix_phrase', 'furn_tables_mix_phrase', 'furn_decor_phrase'], ['seat_mix_phrase', 'furn_tables_mix_phrase', 'furn_storage_mix_phrase', 'furn_lighting_mix_phrase', 'furn_decor_phrase']),
'bedroom': ('bedroom', ['furn_beds_mix_phrase', 'furn_storage_mix_phrase'], ['furn_beds_mix_phrase', 'furn_storage_mix_phrase', 'furn_lighting_mix_phrase', 'home_textiles_phrase', 'furn_decor_phrase']),
'kitchen': ('kitchen', ['furn_kitchen_phrase', 'furn_tables_mix_phrase'], ['furn_kitchen_phrase', 'furn_kitchen_phrase', 'home_cookware_phrase', 'home_tableware_phrase', 'furn_tables_mix_phrase']),
'bathroom': ('bathroom', ['furn_bathroom_phrase', 'furn_bathroom_phrase'], ['furn_bathroom_phrase', 'furn_bathroom_phrase', 'furn_bathroom_phrase', 'home_textiles_phrase', 'furn_decor_phrase']),
'dining_room': ('dining room', ['furn_tables_mix_phrase', 'seat_mix_phrase'], ['furn_tables_mix_phrase', 'seat_mix_phrase', 'furn_storage_mix_phrase', 'home_tableware_phrase', 'furn_lighting_mix_phrase']),
'hallway': ('hallway', ['furn_storage_mix_phrase', 'furn_decor_phrase'], ['furn_storage_mix_phrase', 'furn_decor_phrase', 'furn_lighting_mix_phrase', 'furn_decor_phrase']),
'home_office': ('home office', ['furn_office_mix_phrase', 'seat_mix_phrase'], ['furn_office_mix_phrase', 'seat_mix_phrase', 'furn_storage_mix_phrase', 'office_supplies_phrase', 'furn_lighting_mix_phrase']),
'laundry_room': ('laundry room', ['gear_laundry_phrase', 'home_cleaning_phrase'], ['gear_laundry_phrase', 'gear_laundry_phrase', 'home_cleaning_phrase', 'furn_storage_mix_phrase']),
'garage': ('garage', ['gear_workshop_phrase', 'furn_storage_mix_phrase'], ['gear_workshop_phrase', 'gear_workshop_phrase', 'furn_storage_mix_phrase', 'home_cleaning_phrase']),
'attic': ('attic', ['furn_storage_mix_phrase', 'furn_decor_phrase'], ['furn_storage_mix_phrase', 'furn_storage_mix_phrase', 'furn_decor_phrase', 'home_textiles_phrase']),
'basement': ('basement', ['furn_storage_mix_phrase', 'home_cleaning_phrase'], ['furn_storage_mix_phrase', 'home_cleaning_phrase', 'gear_workshop_phrase', 'furn_lighting_mix_phrase']),
'balcony': ('balcony', ['seat_mix_phrase', 'furn_tables_mix_phrase'], ['seat_mix_phrase', 'furn_tables_mix_phrase', 'furn_decor_phrase']),
'conservatory': ('conservatory', ['seat_mix_phrase', 'furn_decor_phrase'], ['seat_mix_phrase', 'furn_tables_mix_phrase', 'furn_decor_phrase', 'furn_lighting_mix_phrase']),
'open_office': ('open-plan office', ['furn_office_mix_phrase', 'furn_office_mix_phrase'], ['furn_office_mix_phrase', 'furn_office_mix_phrase', 'office_supplies_phrase', 'furn_storage_mix_phrase', 'furn_lighting_mix_phrase']),
'meeting_room': ('meeting room', ['furn_office_mix_phrase', 'seat_mix_phrase'], ['furn_office_mix_phrase', 'seat_mix_phrase', 'office_supplies_phrase', 'home_electronics_phrase']),
'reception': ('reception area', ['furn_office_mix_phrase', 'seat_mix_phrase'], ['furn_office_mix_phrase', 'seat_mix_phrase', 'furn_decor_phrase', 'furn_lighting_mix_phrase']),
'break_room': ('staff break room', ['furn_tables_mix_phrase', 'furn_kitchen_phrase'], ['furn_tables_mix_phrase', 'seat_mix_phrase', 'furn_kitchen_phrase', 'home_tableware_phrase']),
'library': ('library', ['furn_storage_mix_phrase', 'furn_tables_mix_phrase'], ['furn_storage_mix_phrase', 'furn_storage_mix_phrase', 'furn_tables_mix_phrase', 'seat_mix_phrase', 'furn_lighting_mix_phrase']),
'cafe': ('café', ['gear_shop_phrase', 'gear_shop_phrase'], ['gear_shop_phrase', 'gear_shop_phrase', 'gear_shop_phrase', 'home_tableware_phrase', 'furn_lighting_mix_phrase']),
'restaurant': ('restaurant dining room', ['furn_tables_mix_phrase', 'seat_mix_phrase'], ['furn_tables_mix_phrase', 'seat_mix_phrase', 'home_tableware_phrase', 'furn_lighting_mix_phrase', 'furn_decor_phrase']),
'bar': ('bar', ['gear_shop_phrase', 'seat_mix_phrase'], ['gear_shop_phrase', 'seat_mix_phrase', 'bottle_phrase', 'furn_lighting_mix_phrase']),
'hotel_room': ('hotel room', ['furn_beds_mix_phrase', 'furn_bathroom_phrase'], ['furn_beds_mix_phrase', 'furn_storage_mix_phrase', 'furn_lighting_mix_phrase', 'home_textiles_phrase', 'furn_decor_phrase']),
'classroom': ('classroom', ['gear_class_phrase', 'gear_class_phrase'], ['gear_class_phrase', 'gear_class_phrase', 'gear_class_phrase', 'furn_lighting_mix_phrase']),
'workshop': ('workshop', ['gear_workshop_phrase', 'gear_workshop_phrase'], ['gear_workshop_phrase', 'gear_workshop_phrase', 'gear_workshop_phrase', 'furn_storage_mix_phrase', 'furn_lighting_mix_phrase']),
'art_studio': ('art studio', ['gear_studio_phrase', 'furn_tables_mix_phrase'], ['gear_studio_phrase', 'gear_studio_phrase', 'furn_tables_mix_phrase', 'furn_lighting_mix_phrase']),
'music_room': ('music practice room', ['gear_studio_phrase', 'seat_mix_phrase'], ['gear_studio_phrase', 'gear_studio_phrase', 'seat_mix_phrase', 'furn_lighting_mix_phrase']),
'dance_studio': ('dance studio', ['gear_studio_phrase', 'gear_gym_floor_phrase'], ['gear_studio_phrase', 'gear_gym_floor_phrase', 'furn_lighting_mix_phrase']),
'gym': ('gym', ['gear_gym_cardio_phrase', 'gear_gym_floor_phrase'], ['gear_gym_cardio_phrase', 'gear_gym_cardio_phrase', 'gear_gym_weights_phrase', 'gear_gym_floor_phrase', 'furn_lighting_mix_phrase']),
'weight_training_gym': ('weight-training gym', ['gear_gym_weights_phrase', 'gear_gym_weights_phrase'], ['gear_gym_weights_phrase', 'gear_gym_weights_phrase', 'gear_gym_weights_phrase', 'gear_gym_floor_phrase', 'furn_lighting_mix_phrase']),
'swimming_pool': ('indoor swimming pool hall', ['gear_pool_phrase', 'gear_pool_phrase'], ['gear_pool_phrase', 'gear_pool_phrase', 'gear_pool_phrase', 'furn_lighting_mix_phrase']),
'yoga_studio': ('yoga studio', ['gear_yoga_phrase', 'gear_gym_floor_phrase'], ['gear_yoga_phrase', 'gear_yoga_phrase', 'gear_gym_floor_phrase', 'furn_lighting_mix_phrase']),
'sauna': ('sauna', ['gear_sauna_phrase', 'gear_sauna_phrase'], ['gear_sauna_phrase', 'gear_sauna_phrase', 'gear_sauna_phrase', 'home_textiles_phrase']),
'spa_treatment_room': ('spa treatment room', ['furn_lighting_mix_phrase', 'home_textiles_phrase'], ['seat_mix_phrase', 'home_textiles_phrase', 'furn_lighting_mix_phrase', 'furn_decor_phrase']),
'shop': ('shop', ['gear_shop_phrase', 'furn_storage_mix_phrase'], ['gear_shop_phrase', 'gear_shop_phrase', 'furn_storage_mix_phrase', 'furn_lighting_mix_phrase']),
'train_carriage': ('train carriage', ['seat_mix_phrase', 'furn_tables_mix_phrase'], ['seat_mix_phrase', 'seat_mix_phrase', 'furn_tables_mix_phrase', 'furn_lighting_mix_phrase']),
}
