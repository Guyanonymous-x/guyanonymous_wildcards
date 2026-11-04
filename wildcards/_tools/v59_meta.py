ONELINE = '120 professions and roles, including spiritual and ritual roles from many traditions, built from parts'
BULLETS = ["Professions and roles. 120 jobs in 7 sectors: health and care, trades, farming and food, public service and transport, office and professional, creative and performing, service and hospitality, and spiritual and ritual roles. Each has its own parts, `job_<name>_outfit`, `_tool`, `_workplace` and `_action`, and an assembled `job_<name>_prompt`.",
"Spiritual and ritual roles from many traditions, described neutrally and respectfully as jobs, with their clothing, tools, places and actions. They include a rabbi, cantor, Anglican, Catholic, Orthodox and Protestant clergy, Methodist preacher, imam, muezzin, Buddhist monk, Zen priest, Tibetan lama, Hindu priest, Sikh granthi, Shinto and Taoist priests, druid, shaman, nun, pagan priestess, vodou priest, Sufi mystic, yogi, pilgrim and church organist.",
"Pick by job or by sector. `job_prompt` picks any profession, `job_sector_<sector>_prompt` picks one sector (for example `job_sector_spiritual_prompt`), and `job_<name>_prompt` makes one job. `job_names` and `job_sector_<sector>_names` list the jobs.",
"Put a person in the role. `job_person_prompt` adds a short person description to a random job, and `job_frame_prompt` also frames it as a whole-body 1:1 image with the v57 framing files.",
"100 random sample prompts, one per line with no blank lines, show professions from every sector, including the spiritual roles, with and without people."]
README = """Guyanonymous' Wildcards v59 - professions and roles
===================================================
Jobs        job_<name>_outfit / _tool / _workplace / _action / _prompt     120 jobs
Pickers     job_prompt, job_sector_<sector>_prompt, job_names, job_sector_<sector>_names
            sectors: health, trades, public, office, creative, service, spiritual
With people job_person_prompt, job_frame_prompt
All Options Once includes the jobs (not the person prompts).
"""
GEN_ROW = '("job_<name>_*, job_prompt, job_sector_<sector>_prompt","120 / 7","v59 professions and roles in 7 sectors, including spiritual and ritual roles from many traditions, built from outfit, tool, workplace and action parts."),'
SAMPLES = [('any profession', '__job_prompt__', 24), ('health', '__job_sector_health_prompt__', 6), ('trades', '__job_sector_trades_prompt__', 6), ('public service', '__job_sector_public_prompt__', 5), ('office', '__job_sector_office_prompt__', 5), ('creative', '__job_sector_creative_prompt__', 6), ('service', '__job_sector_service_prompt__', 5), ('spiritual roles', '__job_sector_spiritual_prompt__', 14),
 ('person in the role', '__job_person_prompt__', 12), ('framed whole-body image', '__job_frame_prompt__', 17)]
