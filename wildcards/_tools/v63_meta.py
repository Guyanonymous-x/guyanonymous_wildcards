ONELINE = 'global dress and culture: traditional clothing, headwear, adornment, hairstyles, settings and occasions for 30 regions'
BULLETS = ["Regional dress for 30 regions across every inhabited continent (Japan, Korea, China, India, South Asia, South-East Asia, Central Asia, the Middle East, the Arabian Peninsula, Turkey and the Caucasus, North Africa, West, East and Southern Africa, Ethiopia and the Horn, Amazigh regions, Northern, Central, Mediterranean, Eastern and British Isles Europe, the Balkans, Northern Eurasia, the Andes, Mexico and Central America, North America, the Arctic, the Caribbean, the Pacific Islands and Australia).",
"Each region has its own garment, headwear, adornment, hairstyle, setting and occasion files, such as `culture_west_africa_garment`. Every garment is described in full (what it is made of, how it is worn), and every item is neutral about who wears it.",
"Entries. `culture_<region>_prompt` builds a person in the dress of one region, with matching hair, place and occasion. `culture_prompt` picks any region. `culture_frame_prompt` adds the v57 framing so the whole person is in a 1:1 frame.",
"Without a person. `culture_garment_prompt` shows a set of clothing laid out on a plain surface, and `culture_scene_prompt` shows a place and occasion. Mixed lists such as `culture_garment`, `culture_headwear`, `culture_adornment`, `culture_hairstyle`, `culture_setting` and `culture_event` can be mixed with any other file.",
"Everything is described as everyday or festive dress, with no sacred regalia and no stereotyped costume. 100 random sample prompts, one per line with no blank lines."]
README = """Guyanonymous' Wildcards v63 - global dress and culture
=====================================================
Per region (30)  culture_<region>_garment / _head / _adorn / _hair / _setting / _event / _outfit
Region entries   culture_<region>_prompt, _garment_prompt, _scene_prompt, _frame_prompt
Global entries   culture_prompt, culture_frame_prompt, culture_garment_prompt, culture_scene_prompt
Mixed lists      culture_garment, culture_headwear, culture_adornment, culture_hairstyle, culture_setting, culture_event, culture_region, culture_age
All Options Once includes all of these except the framed prompts.
"""
GEN_ROW = '("culture_<region>_*, culture_*","30 regions","v63 regional dress, headwear, adornment, hairstyles, settings and occasions for 30 regions."),'
SAMPLES = [('person in regional dress', '__culture_prompt__', 40), ('person framed 1:1', '__culture_frame_prompt__', 30), ('clothing laid out', '__culture_garment_prompt__', 12), ('scene and occasion', '__culture_scene_prompt__', 12), ('mixed headwear', 'A close portrait of a person wearing __culture_headwear__.', 6)]
