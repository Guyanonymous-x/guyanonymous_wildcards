ONELINE = 'art and media styles, unbranded product and packaging, signage helpers, and the condition (appearance modifier) system'
BULLETS = ["Art and media styles. `medium_name` has 38 fully described media (oil, watercolour, woodblock, mosaic, stained glass, embroidery, paper cut, clay, marble, pixel art, comic, technical drawing and more) with `medium_palette`, `medium_finish`, `medium_subject` and the entry `medium_prompt`.",
"Product and packaging shots with no brands. `prod_item` (30 described products), `pack_type` (20 described packages), `pack_label` (plain, hand-written or stamped labels), plus set, light and angle files, in `prod_prompt` and `pack_prompt`.",
"Signage helpers. `sign_type`, `sign_lettering`, `sign_message` (30 neutral words) and `sign_prompt` give readable signs with chosen wording.",
"The condition system. Eight subject kinds (building, vehicle, furniture, clothing, object, sign, book, statue) each have ten condition families (damage, missing pieces, wear, dirt, decay, graffiti, repair, fine quality, cheap quality, faded, burnt) at three strengths (light, moderate, heavy). Each file names real parts of that kind of thing, such as `cond_vehicle_decay_heavy` (doors, windscreen, mudguards).",
"Using it. `modify_<kind>` picks any condition, `cond_<kind>_<family>` picks a strength, `cond_<kind>_<strength>` picks a family. `condition_<kind>_prompt` adds it to a ready subject, and `condition_prompt` and `condition_ruined_prompt` pick any kind.",
"100 random sample prompts, one per line with no blank lines."]
README = """Guyanonymous' Wildcards v62 - art, media and condition
======================================================
Styles      medium_name, medium_palette, medium_finish, medium_subject, medium_prompt
Product     prod_item, prod_set, prod_light, prod_angle, prod_prompt; pack_type, pack_label, pack_finish, pack_prompt
Signs       sign_type, sign_lettering, sign_message, sign_prompt
Condition   cond_<kind>_<family>_<light|moderate|heavy>, cond_<kind>_<family>, cond_<kind>_<strength>, modify_<kind>
            kinds: building vehicle furniture clothing object sign book statue
            families: damage missing wear dirt graffiti faded burnt decay repair fine cheap
Entries     condition_<kind>_prompt, condition_<kind>_<strength>_prompt, condition_<kind>_good_prompt, condition_prompt, condition_ruined_prompt
All Options Once includes all of these except the framed medium prompt.
"""
GEN_ROW = '("medium_*, prod_*, pack_*, sign_*, cond_*, modify_*","38 / 8 kinds","v62 art and media styles, product and packaging shots, signs and the condition modifier system."),'
SAMPLES = [('art medium', '__medium_prompt__', 14), ('product', '__prod_prompt__', 10), ('packaging', '__pack_prompt__', 8), ('sign', '__sign_prompt__', 8), ('condition mixed', '__condition_prompt__', 30), ('condition ruined', '__condition_ruined_prompt__', 8), ('building condition', '__condition_building_prompt__', 6), ('vehicle condition', '__condition_vehicle_prompt__', 6), ('excellent condition', '__condition_furniture_good_prompt__', 4), ('modifier only', '__modify_clothing__', 6)]
