Guyanonymous' Wildcards v48 - rooms and locations
==================================================
Rooms describe the space only: no people, no poses. They call furniture (furn_*), household (home_*), office, bottle and gear (gear_*) files by reference.

All rooms       room_prompt_brief, room_prompt_full
One room        room_<type>_prompt_brief / room_<type>_prompt_full
Types           living_room bedroom kitchen bathroom dining_room hallway home_office laundry_room garage attic basement balcony conservatory open_office meeting_room reception break_room library cafe restaurant bar hotel_room classroom workshop art_studio music_room dance_studio gym weight_training_gym swimming_pool yoga_studio sauna spa_treatment_room shop train_carriage
Modifiers       room_size room_floor room_walls room_light room_condition room_style
Gear            gear_gym_cardio gear_gym_weights gear_gym_floor gear_pool gear_yoga gear_sauna gear_workshop gear_studio gear_shop gear_class gear_laundry (each _prompt and _phrase)
Entry points    v48_entry_points
Example         __any_create_random_person_w_clothes__ __pose_prompt__ __room_gym_prompt_full__
