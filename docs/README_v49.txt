Guyanonymous' Wildcards v49 - random assembly for every new object
==================================================================
Before: a family file was a list of finished sentences. Now: <family>_prompt (and <family>_random) assembles one description from components.

Per type      <family>_<type>_material      the materials that type really comes in (with __comp_colour__ where the material takes colour)
Shared        comp_colour, comp_fin_wood / metal / plastic / glass / soft / hard, comp_feat_<category> (24 categories), comp_condition
Per family    <family>_random               one line per type that calls the files above
              <family>_prompt               calls <family>_random
              <family>_phrase               same assembly without the condition sentence, for use inside rooms, poses and liquids
Unchanged     <family> (premade lines) and <family>_short
List          v49_families (the 89 families covered), v49_components
Example       __furn_storage_prompt__   __seat_prompt__   __perfume_prompt__   __room_prompt_full__
