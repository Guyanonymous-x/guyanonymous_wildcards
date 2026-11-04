"""v82 showcase: 40 prompts built only from wildcard text plus joining words."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from v74_showcase import pull, grid, sizes, cap
def build(off=0):
    S = []; add = lambda i, t, ratio, text: S.append((i, t, ratio, text)); P = lambda ref, s: pull(ref, off + s)
    R = [('marble statue', 'sculpt_marble', (4, 5)), ('bronze figure', 'sculpt_bronze', (4, 5)), ('chainsaw carving', 'sculpt_chainsaw', (4, 5)), ('ice carving', 'sculpt_ice', (4, 5)), ('wire sculpture', 'sculpt_wire', (3, 2)),
         ('stoneware pottery', 'craft_stoneware', (1, 1)), ('kintsugi bowl', 'craft_kintsugi', (1, 1)), ('blown glass vessel', 'craft_glassvessel', (4, 5)), ('glass mosaic', 'craft_glassmosaic', (3, 2)), ('marquetry panel', 'craft_marquetry', (3, 2)), ('lacquerware', 'craft_lacquer', (3, 2)),
         ('woven tapestry', 'fibre_tapestry', (3, 2)), ('patchwork quilt', 'fibre_quilt', (3, 2)), ('felted wool art', 'fibre_felted', (1, 1)), ('crochet toy', 'fibre_amigurumi', (4, 5)), ('origami', 'fibre_origami', (1, 1)), ('paper cutting', 'fibre_papercut', (4, 5)), ('diorama', 'fibre_diorama', (3, 2)), ('ship in a bottle', 'fibre_ship_in_bottle', (3, 2)),
         ('clay render', 'render_clay_render', (1, 1)), ('low-poly render', 'render_low_poly_render', (3, 2)), ('claymation scene', 'render_claymation_scene', (3, 2)), ('neon sign', 'render_neon_sign', (4, 5)), ('mirrored room', 'render_infinity_mirror_room', (3, 2)), ('sand mandala', 'render_sand_mandala', (1, 1))]
    for n, (t, k, ratio) in enumerate(R, 1): add('S%02d' % n, t, ratio, P('__af_%s_prompt__' % k, n))
    G = [('marble and granite grid', 4, 'carved stone sculpture', ['__af_sculpt_marble_short__', '__af_sculpt_granite_short__'] * 2), ('bronze and steel grid', 4, 'metal sculpture', ['__af_sculpt_bronze_short__', '__af_sculpt_steel_short__'] * 2), ('wood carvings grid', 4, 'wood carving', ['__af_sculpt_wood_short__', '__af_sculpt_totem_short__'] * 2),
         ('pottery grid', 9, 'piece of pottery', ['__af_craft_stoneware_short__', '__af_craft_raku_short__', '__af_craft_celadon_short__'] * 3), ('glass grid', 4, 'piece of glasswork', ['__af_craft_glassvessel_short__', '__af_craft_lampwork_short__'] * 2), ('tile and mosaic grid', 4, 'tile or mosaic panel', ['__af_craft_azulejo_short__', '__af_craft_glassmosaic_short__'] * 2),
         ('embroidery grid', 4, 'piece of embroidery', ['__af_fibre_crewel_short__', '__af_fibre_cross_stitch_short__', '__af_fibre_sashiko_short__', '__af_fibre_goldwork_short__']), ('quilts and tapestries grid', 4, 'quilt or tapestry', ['__af_fibre_quilt_short__', '__af_fibre_tapestry_short__'] * 2),
         ('paper art grid', 9, 'piece of paper art', ['__af_fibre_origami_short__', '__af_fibre_quilling_short__', '__af_fibre_papercut_short__'] * 3), ('puppets grid', 4, 'puppet', ['__af_fibre_shadow_puppet_short__', '__af_fibre_marionette_short__'] * 2),
         ('toy renders grid', 4, 'toy-like 3D object', ['__af_render_vinyl_toy_short__', '__af_render_brick_build_short__', '__af_render_action_figure_short__', '__af_render_resin_figurine_short__']), ('3D render looks grid', 4, '3D render', ['__af_render_clay_render_short__', '__af_render_low_poly_render_short__', '__af_render_voxel_art_short__', '__af_render_wireframe_render_short__']),
         ('light installations grid', 4, 'light installation', ['__af_render_neon_sign_short__', '__af_render_led_installation_short__'] * 2), ('food and flower art grid', 4, 'piece of edible or floral art', ['__af_render_sugar_sculpture_short__', '__af_render_fruit_carving_short__', '__af_render_floral_arrangement_short__', '__af_render_balloon_sculpture_short__']),
         ('mixed art forms grid', 9, 'art object', ['__af_sculpt_relief_short__', '__af_craft_lacquer_short__', '__af_fibre_lace_short__'] * 3)]
    for n, (t, c, what, refs) in enumerate(G, 1): add('G%02d' % n, t, (1, 1), grid(c, what, refs, off + 40 + n))
    return S
if __name__ == '__main__':
    for i, t, ratio, text in build(): print('##', i, t, ratio, len(text)); print(text); print()
