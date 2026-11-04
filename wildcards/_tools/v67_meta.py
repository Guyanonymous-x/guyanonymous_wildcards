ONELINE = 'visual and special effects (real and spectacle tiers) plus extreme weather in sky, land and living layers'
BULLETS = ["Nine effect domains, each with 8 to 10 effects written twice. The real tier is a physically plausible approximation (what could actually be photographed) and the spectacle tier is the film-style version. Both stay photographic, so an illustrative style from v62 translates cleanly. Domains: magic and spellwork, transformation (partial changes with swirling marks), belief-neutral miraculous and mythic events (parted waters, pillar of fire, staff to serpent and others), sacred light and atmosphere, science (arcs, plasma, lasers, bioluminescence, ferrofluid), cultural and secular (fireworks, lanterns, powder, drone shows), stage tricks and illusions, optical illusions, and atmosphere and light physics.",
"Effects are built from parts. `fx_<domain>_real` or `_spectacle` is what, `fx_where_<person|place|sky|object>` is where it sits, `fx_strength` is subtle, moderate or dramatic, `fx_colour_real` and `fx_colour_spectacle` are the light, and `fx_interact_<target>` says how it affects the scene.",
"Entry points. `fx_<domain>_real_prompt` and `fx_<domain>_spectacle_prompt` attach an effect to a ready scene, a person, a place or a stage. `scene_with_effect_prompt` and `fx_prompt` pick any. `fx_real_prompt` and `fx_spectacle_prompt` pick one tier.",
"Photographic effects that apply to a whole image (long exposure, haze, lens flare, motion blur, bokeh, light leaks, double exposure and more) are in `fx_photo_effect`, with `fx_photo_prompt` to use them on a landscape, city or product.",
"Extreme weather in 15 events (tornado, hurricane, blizzard, thunderstorm, hailstorm, flood, wildfire, drought, dust storm, ice storm, avalanche, tsunami, volcanic ash, monsoon, fog). Each event has matching sky, land, people, things, animals, plants and light files, so everything in one prompt belongs to the same storm.",
"Three layers. `wx_<event>_sky_prompt` is the sky and air, `wx_<event>_place_prompt` adds the effect on the land, and `wx_<event>_living_prompt` shows people, things, animals and plants. `wx_<event>_prompt` combines all three, and `wx_severity` gives mild, strong, severe and extreme.",
"Gallery sets. `wx_<event>_gallery_prompt` makes one image of four panels divided by thin white lines, showing the same place at the four severities. `wx_gallery_prompt` picks any event.",
"100 random sample prompts, one per line with no blank lines."]
README = """Guyanonymous' Wildcards v67 - visual and special effects, and extreme weather
=============================================================================
Effects     fx_<domain>_real / _spectacle / _name, fx_where_<person|place|sky|object>, fx_interact_<target>, fx_strength, fx_colour_real, fx_colour_spectacle
            domains: magic transformation miraculous sacred_light scientific cultural tricks optical atmosphere
Entries     fx_<domain>_real_prompt, fx_<domain>_spectacle_prompt, fx_<domain>_prompt, fx_real_prompt, fx_spectacle_prompt, scene_with_effect_prompt, fx_prompt
Photographic fx_photo_effect, fx_photo_prompt
Weather     wx_<event>_sky / _land / _people / _things / _animals / _plants / _light, wx_<event>_sky_prompt / _place_prompt / _living_prompt / _prompt / _gallery_prompt, wx_severity, wx_prompt, wx_sky_prompt, wx_place_prompt, wx_living_prompt, wx_gallery_prompt, wx_names
All Options Once includes all of these.
"""
GEN_ROW = '("fx_*, scene_with_effect_prompt, wx_*","9 domains / 15 events","v67 real and spectacle visual effects and three-layer extreme weather."),'
SAMPLES = [('effect real', '__fx_real_prompt__', 22), ('effect spectacle', '__fx_spectacle_prompt__', 22), ('photographic effect', '__fx_photo_prompt__', 6), ('weather full', '__wx_prompt__', 16), ('weather sky', '__wx_sky_prompt__', 8), ('weather place', '__wx_place_prompt__', 8), ('weather living', '__wx_living_prompt__', 8), ('weather gallery', '__wx_gallery_prompt__', 10)]
