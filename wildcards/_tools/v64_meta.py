ONELINE = 'hobbies, music and sport: 51 activities with clothing, equipment, settings and actions'
BULLETS = ["51 activities in three groups. 18 hobbies (gardening, pottery, knitting, sewing, painting, woodworking, baking, birdwatching, photography, fishing, camping, chess, reading, model building, calligraphy, beekeeping, dance classes, stargazing), 21 sports (football, basketball, running, swimming, cycling, tennis, climbing, skiing, surfing, boxing, gymnastics, rowing, archery, cricket, yoga, skateboarding, martial arts, sailing and more) and 12 kinds of music making (violin, guitar, piano, drums, woodwinds, brass, choir, folk instruments, DJ, orchestra, busking, bagpipes).",
"Each activity has clothes, equipment, setting and action files, such as `act_rock_climbing_equip`, with every piece of equipment described in plain words.",
"Entries. `act_<activity>_prompt` places a random person in an activity. `act_prompt` picks any, and `act_hobby_prompt`, `act_sport_prompt` and `act_music_prompt` pick within a group. `act_frame_prompt` adds the v57 framing for a full-body 1:1 shot.",
"Without a person. `act_gear_prompt` lays equipment out on a plain surface and `act_scene_prompt` shows the place for the activity.",
"100 random sample prompts, one per line with no blank lines."]
README = """Guyanonymous' Wildcards v64 - hobbies, music and sport
======================================================
Per activity  act_<activity>_clothes / _equip / _setting / _action / _prompt / _gear_prompt / _scene_prompt / _frame_prompt
Entries       act_prompt, act_hobby_prompt, act_sport_prompt, act_music_prompt, act_frame_prompt, act_gear_prompt, act_scene_prompt, act_names, act_age
All Options Once includes all of these except the framed prompts.
"""
GEN_ROW = '("act_<activity>_*, act_*","51","v64 hobbies, sport and music activities with clothing, equipment, settings and actions."),'
SAMPLES = [('hobby', '__act_hobby_prompt__', 22), ('sport', '__act_sport_prompt__', 24), ('music', '__act_music_prompt__', 16), ('framed 1:1', '__act_frame_prompt__', 24), ('equipment', '__act_gear_prompt__', 8), ('place', '__act_scene_prompt__', 6)]
