"""v109 showcase: 40 prompts - the 350-location conversion (scenes, people, eras), era-specific objects, architectural fixtures,
objects with quoted text, trading cards and their packaging and displays, card games, board games, top-down game tables, adventure,
outdoor and workout activities, and quoted sportswear text. The medical scenes are left out of the showcase (their samples are private)."""
import sys, os, random
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import expand as E
from paths import FINAL
from v74_showcase import sizes
files = E.load([FINAL])
OBJ = 'A clear product photograph of %s, standing on a plain wooden table against a soft grey wall, natural window light, sharp focus.'
FIX = 'A clear architectural photograph of %s, seen straight on in soft daylight, sharp focus on the details.'
REFS = [
 ('loc_scene', 4, 3), ('loc_scene', 3, 2), ('loc_scene', 1, 1), ('loc_people', 4, 5), ('loc_people', 3, 2), ('loc_era_scene', 3, 2),
 (OBJ % '__ob_telephone_full__', 1, 1), (OBJ % '__ob_radio_full__', 1, 1), (OBJ % '__ob_camera_full__', 1, 1), (OBJ % '__ob_book_full__', 4, 5), (OBJ % '__ob_newspaper_full__', 3, 2),
 (FIX % '__ob_door_full__', 2, 3), (FIX % '__ob_staircase_full__', 2, 3),
 ('tc_sports_prompt', 2, 3), ('tc_sports_prompt', 2, 3), ('tc_movie_prompt', 2, 3), ('tc_wildlife_prompt', 2, 3), ('tc_pack_opened_prompt', 3, 2), ('tc_box_sealed_prompt', 1, 1), ('tc_display_wall_prompt', 3, 2),
 ('cg_race_aeroplane_card_prompt', 2, 3), ('cg_tarot_stage_prompt', 3, 2), ('cg_stats_play_prompt', 3, 2), ('cg_shed_hand_prompt', 3, 2), ('cg_trick_topdown_prompt', 1, 1), ('cg_hanafuda_topdown_prompt', 1, 1),
 ('bg_city_play_prompt', 3, 2), ('bg_chess_stage_prompt', 1, 1), ('bg_mystery_topdown_prompt', 1, 1), ('bg_hex_settle_topdown_prompt', 1, 1), ('bg_word_tiles_play_prompt', 1, 1), ('bg_stack_tower_stage_prompt', 4, 5),
 ('adv_extreme_prompt', 2, 3), ('adv_extreme_prompt', 3, 2), ('adv_outdoor_prompt', 3, 2), ('adv_outdoor_prompt', 3, 2), ('adv_workout_prompt', 4, 5), ('adv_workout_prompt', 1, 1),
 ('adv_trail_run_prompt', 3, 2), ('adv_motocross_prompt', 3, 2),
]
def build(off=0):
    R = random.Random(1090000 + off); S = []; seen = set()
    for n, (ref, a, b) in enumerate(REFS, 1):
        tpl = ref if ' ' in ref else '__%s__' % ref
        while True:
            text = ' '.join(E.clean(E.expand(files, tpl, R)).split())
            if text not in seen and '__' not in text: break
        seen.add(text)
        text = text[0].upper() + text[1:]
        text = text.replace(', .', '.').replace(',.', '.')
        tag = ref if ' ' not in ref else ref.split('__')[1]
        S.append(('M%02d' % n, tag, (a, b), text))
    return S
if __name__ == '__main__':
    for i, t, ratio, text in build(): print('##', i, t, ratio, len(text)); print(text[:300]); print()
