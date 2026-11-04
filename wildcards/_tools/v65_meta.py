ONELINE = 'cities and public places: 24 place types in parts, with regional building styles, times, weather and crowds'
BULLETS = ["24 city and public place types in parts: street, market, railway station, airport, harbour, public square, park, bridge, metro platform, shopping arcade, food street, city at night, old town alley, canal, skyline, university campus, library, museum, stadium, festival ground, rooftop terrace, bus stop, building site and residential neighbourhood.",
"Each type has layout, ground surface, detail, activity and signage files, such as `city_market_detail`, assembled by `city_<type>_prompt`. Signage is always generic (painted names, number plates, route numbers) with no brands.",
"Shared files. `city_style` (12 building styles from stone and tile to glass towers), `city_time`, `city_weather` and `city_crowd` suit any place, and times and weather are written so they never contradict each other.",
"Entries. `city_prompt` picks any place, `city_<type>_empty_prompt` leaves people out, `city_frame_prompt` adds the v57 framing for a 1:1 image, and `city_person_prompt` and `city_person_frame_prompt` add a random person to the scene.",
"100 random sample prompts, one per line with no blank lines."]
README = """Guyanonymous' Wildcards v65 - cities and public places
=====================================================
Per type (24)  city_<type>_layout / _surface / _detail / _activity / _sign / _prompt / _empty_prompt / _frame_prompt
Shared         city_style, city_time, city_weather, city_crowd, city_names
Entries        city_prompt, city_empty_prompt, city_frame_prompt, city_person_prompt, city_person_frame_prompt
All Options Once includes all of these except the framed and person prompts.
"""
GEN_ROW = '("city_<type>_*, city_*","24","v65 cities and public places in parts with building styles, times and weather."),'
SAMPLES = [('place', '__city_prompt__', 50), ('empty place', '__city_empty_prompt__', 16), ('place framed 1:1', '__city_frame_prompt__', 16), ('person in place', '__city_person_prompt__', 10), ('person in place framed', '__city_person_frame_prompt__', 8)]
