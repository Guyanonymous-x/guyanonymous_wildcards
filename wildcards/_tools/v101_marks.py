"""v101 - optional brand-style marks: small marks built from random choices with fake names/logos from the name system."""
def P(x): return [i.strip() for i in x.split(';') if i.strip()]
def build(final=None):
    G = {}
    G['bs_simple_shape'] = P('circle; triangle; diamond; crescent; square; cross; hexagon; teardrop; arch; semicircle; oval; star; zigzag line; wave; heart; plus sign; ring; half moon; leaf; arrow')
    G['bs_mark_shape'] = P('round; oval; shield-shaped; rounded-rectangle; diamond-shaped; pill-shaped; six-sided; square; arch-topped; kite-shaped; tall narrow; wide flat; teardrop-shaped')
    G['bs_mark_material'] = P('leather; rubber-like; woven cloth; enamel; printed; metal; embroidered; moulded plastic; stitched canvas; stamped paper')
    G['bs_mark_outline'] = P('with a stitched border; with a thin ring around the edge; with a double line around the edge; with a plain clean edge; with a raised rim; with a dashed line around the edge; with softly rounded corners; with a bold thick edge')
    G['bs_mark_size'] = P('small; very small; neat and small; modest')
    G['bs_mark_place'] = P('on one side; near the lower edge; off-centre on the front; near an upper corner; low on the back; at a lower corner; beside a seam; in the middle of a plain panel')
    G['bs_mark'] = [
        'A __bs_mark_size__ __bs_mark_shape__ __bs_mark_material__ mark __bs_mark_outline__ sits __bs_mark_place__, carrying __name_logo_description__.',
        'Placed __bs_mark_place__ is a __bs_mark_size__ __bs_mark_shape__ __bs_mark_material__ mark __bs_mark_outline__, showing __name_logo_description__.',
        'A __bs_mark_size__ __bs_mark_material__ mark, __bs_mark_shape__ and __bs_mark_outline__, sits __bs_mark_place__, with __name_logo_description__.']
    G['maker_bs_converse_mark'] = ['A small round rubber-like mark with a thin ring and a stitched border sits __bs_mark_place__, carrying __name_logo_description__.',
        'A small round leather mark with a double line around the edge sits __bs_mark_place__, carrying __name_logo_description__.',
        'A small oval woven cloth mark with a stitched border sits __bs_mark_place__, carrying __name_logo_description__.']
    G['v101_marks_entry_points'] = ['bs_mark', 'bs_simple_shape', 'maker_bs_converse_mark']
    return G
