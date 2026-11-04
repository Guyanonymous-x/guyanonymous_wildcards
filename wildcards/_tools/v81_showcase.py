"""v81 showcase: 40 prompts built only from wildcard text plus joining words."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from v74_showcase import pull, grid, sizes, cap
def build(off=0):
    S = []; add = lambda i, t, ratio, text: S.append((i, t, ratio, text)); P = lambda ref, s: pull(ref, off + s)
    R = [('tin toy robot', 'rb_tin', (4, 5)), ('humanoid robot', 'rb_human', (4, 5)), ('android', 'rb_android', (4, 5)), ('helper robot', 'rb_butler', (3, 2)), ('industrial arm', 'rb_arm', (3, 2)), ('four-legged robot', 'rb_dog', (3, 2)),
         ('wheeled rover', 'rb_rover', (3, 2)), ('giant mech', 'rb_mech', (4, 5)), ('clockwork automaton', 'rb_clock', (4, 5)), ('pet robot', 'rb_pet', (1, 1)), ('floating orb robot', 'rb_orb', (1, 1)), ('alien machine', 'rb_alien', (3, 2)),
         ('early mobile phone', 'gd_brick', (4, 5)), ('flip phone', 'gd_clamshell', (1, 1)), ('modern phone', 'gd_slab', (4, 5)), ('smartwatch', 'gd_watch', (1, 1)), ('e-book reader', 'gd_ereader', (4, 5)), ('tablet', 'gd_tablet', (3, 2)),
         ('handheld game console', 'gd_console', (3, 2)), ('digital camera', 'gd_camera', (3, 2)), ('home computer', 'gd_homecomp', (3, 2)), ('laptop', 'gd_laptop', (3, 2)), ('computer terminal', 'gd_terminal', (3, 2)), ('gaming computer', 'gd_gamingpc', (4, 5)), ('mainframe', 'gd_mainframe', (3, 2))]
    for n, (t, k, ratio) in enumerate(R, 1): add('S%02d' % n, t, ratio, P('__%s_prompt__' % k, n))
    G = [('tin robots grid', 9, 'tin toy robot', '__rb_tin_short__'), ('humanoid robots grid', 4, 'humanoid robot', '__rb_human_short__'), ('rovers and tracked robots grid', 4, 'rover or tracked robot', ['__rb_rover_short__', '__rb_tread_short__'] * 2),
         ('pet robots grid', 9, 'pet robot', '__rb_pet_short__'), ('drones grid', 4, 'flying robot', '__rb_drone_short__'), ('clockwork robots grid', 4, 'clockwork robot', '__rb_clock_short__'), ('early phones grid', 9, 'early mobile phone', ['__gd_brick_short__', '__gd_candybar_short__', '__gd_clamshell_short__'] * 3),
         ('smartphones grid', 4, 'phone', ['__gd_slab_short__', '__gd_fold_short__'] * 2), ('wearables grid', 4, 'wearable gadget', ['__gd_watch_short__', '__gd_band_short__', '__gd_ring_short__', '__gd_glasses_short__']), ('e-readers grid', 4, 'e-book reader', '__gd_ereader_short__'),
         ('tablets and organisers grid', 4, 'tablet or organiser', ['__gd_tablet_short__', '__gd_pda_short__'] * 2), ('handheld devices grid', 9, 'handheld gadget', ['__gd_console_short__', '__gd_music_short__', '__gd_camera_short__'] * 3), ('home computers grid', 4, 'home computer', '__gd_homecomp_short__'),
         ('laptops grid', 4, 'laptop', ['__gd_laptop_short__', '__gd_luggable_short__'] * 2), ('keyboards and mice grid', 9, 'keyboard or mouse', ['__gd_keyboard_short__', '__gd_mouse_short__', '__gd_monitor_short__'] * 3)]
    for n, (t, c, what, refs) in enumerate(G, 1): add('G%02d' % n, t, (1, 1), grid(c, what, refs, off + 40 + n))
    return S
if __name__ == '__main__':
    for i, t, ratio, text in build(): print('##', i, t, ratio, len(text)); print(text); print()
