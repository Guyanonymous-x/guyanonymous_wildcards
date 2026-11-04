"""v80 showcase: 40 prompts built only from wildcard text plus joining words."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from v74_showcase import pull, grid, sizes, cap
def build(off=0):
    S = []; add = lambda i, t, ratio, text: S.append((i, t, ratio, text)); P = lambda ref, s: pull(ref, off + s)
    R = [('crown', 'tr_crown', (3, 2)), ('treasure chest', 'tr_chest', (3, 2)), ('relic', 'tr_relic', (4, 5)), ('tarot cards', 'cd_tarot', (3, 2)), ('playing cards', 'cd_deck', (3, 2)), ('trading cards', 'cd_trading', (4, 5)), ('postcard', 'cd_post', (3, 2)),
         ('crystal cluster', 'mn_cluster', (1, 1)), ('geode', 'mn_geode', (3, 2)), ('fossil', 'mn_fossil', (4, 5)), ('amber', 'mn_amber', (1, 1)), ('record player', 'sd_record', (3, 2)), ('radio', 'sd_radio', (4, 5)), ('tape player', 'sd_tape', (3, 2)), ('jukebox', 'sd_jukebox', (4, 5)),
         ('television', 'sc_tv', (3, 2)), ('computer monitor', 'sc_monitor', (3, 2)), ('handheld game', 'sc_game', (4, 5)), ('arcade cabinet', 'sc_arcade', (4, 5)), ('projector', 'sc_projector', (3, 2)), ('paint brush', 'ar_brush', (3, 2)), ('easel and canvas', 'ar_easel', (4, 5)), ('framed artwork', 'ar_frame', (3, 2)), ('shell', 'nt_shell', (1, 1)), ('nest and egg', 'nt_nest', (3, 2))]
    for n, (t, k, ratio) in enumerate(R, 1): add('S%02d' % n, t, ratio, P('__%s_prompt__' % k, n))
    G = [('treasure jewellery grid', 9, 'piece of treasure jewellery', '__tr_jewel_short__'), ('goblets and vessels grid', 4, 'goblet or vessel', '__tr_cup_short__'), ('tarot cards grid', 4, 'tarot card', '__cd_tarot_short__'), ('trading cards grid', 4, 'trading card', '__cd_trading_short__'),
         ('polished stones grid', 9, 'polished stone', '__mn_polished_short__'), ('cut gemstones grid', 4, 'cut gemstone', '__mn_gemcut_short__'), ('fossils grid', 4, 'fossil', '__mn_fossil_short__'), ('radios grid', 9, 'radio', '__sd_radio_short__'),
         ('microphones and headphones grid', 4, 'microphone or pair of headphones', ['__sd_mic_short__', '__sd_phones_short__'] * 2), ('televisions grid', 4, 'television', '__sc_tv_short__'), ('monitors and laptops grid', 4, 'computer monitor or laptop', ['__sc_monitor_short__', '__sc_laptop_short__'] * 2),
         ('handheld games grid', 4, 'handheld game', '__sc_game_short__'), ('brushes and paints grid', 9, 'art tool or paint', ['__ar_brush_short__', '__ar_paint_short__', '__ar_palette_short__'] * 3), ('shells grid', 9, 'shell', '__nt_shell_short__'), ('feathers and leaves grid', 4, 'feather or leaf', ['__nt_feather_short__', '__nt_leaf_short__'] * 2)]
    for n, (t, c, what, refs) in enumerate(G, 1): add('G%02d' % n, t, (1, 1), grid(c, what, refs, off + 40 + n))
    return S
if __name__ == '__main__':
    for i, t, ratio, text in build(): print('##', i, t, ratio, len(text)); print(text); print()
