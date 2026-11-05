"""v102 (from v101) - optional brand-style marks: small marks built from random choices with fake names/logos from the name system."""
def P(x): return [i.strip() for i in x.split(';') if i.strip()]
def build(final=None):
    G = {}
    G['bs_simple_shape'] = P('circle; triangle; diamond; crescent; square; cross; hexagon; teardrop; arch; semicircle; oval; star; zigzag line; wave; heart; plus sign; ring; half moon; leaf; arrow')
    G['bs_mark_shape'] = P('round; oval; shield-shaped; rounded-rectangle; diamond-shaped; pill-shaped; six-sided; square; arch-topped; kite-shaped; tall narrow; wide flat; teardrop-shaped')
    G['bs_mark_material'] = P('stamped leather; embossed leather; debossed rubber-like; woven cloth; embroidered cloth; enamelled metal; stamped metal; engraved metal; etched metal; low-relief cast metal; printed paper; printed canvas; stitched canvas; moulded plastic; inlaid wood; printed card')
    G['bs_mark_initials'] = P('KV; MR; TSL; AB; NOH; PW; DEL; RJ; CLM; HQ; OTA; BV; SGN; FR; WLK; YD; ZEM; GP; IRO; UX; JNB; LTC; XAV; EK; QMS; VHD; ARC; BNT; DRW; FLM; GHT; HLS; JKO; LMV; NPQ; RST; TUW; VXY; CDE; FGH')
    G['bs_motif_kind'] = P('stamped into the surface; embossed in low relief; printed in a single colour; engraved in fine lines; etched lightly into the surface; picked out in a contrasting colour; raised in low relief; inlaid in a contrasting colour; pressed into the surface; painted in a single colour')
    G['bs_motif'] = ['A small simple __bs_simple_shape__ motif, __bs_motif_kind__, recurs as a quiet accent', 'A small __bs_simple_shape__ shape, __bs_motif_kind__, appears now and then as a discreet accent', 'A single small __bs_simple_shape__ motif, __bs_motif_kind__, sits quietly to one side', 'A tiny __bs_simple_shape__ motif, __bs_motif_kind__, is repeated sparingly as a quiet accent']
    G['bs_motif_c'] = [x[0].lower() + x[1:] for x in G['bs_motif']]
    G['bs_mark_outline'] = P('with a stitched border; with a thin ring around the edge; with a double line around the edge; with a plain clean edge; with a raised rim; with a dashed line around the edge; with softly rounded corners; with a bold thick edge')
    G['bs_mark_size'] = P('small; very small; neat and small; modest')
    G['bs_mark_place'] = P('on one side; near the lower edge; off-centre on the front; near an upper corner; low on the back; at a lower corner; beside a seam; in the middle of a plain panel')
    G['bs_mark'] = [
        'A __bs_mark_size__ __bs_mark_shape__ __bs_mark_material__ mark __bs_mark_outline__ sits __bs_mark_place__, carrying __name_logo_description__.',
        'A __bs_mark_size__ __bs_mark_shape__ __bs_mark_material__ mark __bs_mark_outline__ sits __bs_mark_place__, showing the capital letters "__bs_mark_initials__" in __name_logo_font__.',
        'Placed __bs_mark_place__ is a __bs_mark_size__ __bs_mark_shape__ __bs_mark_material__ mark __bs_mark_outline__, showing __name_logo_description__.',
        'A __bs_mark_size__ __bs_mark_material__ mark, __bs_mark_shape__ and __bs_mark_outline__, sits __bs_mark_place__, with __name_logo_description__.',
        'A __bs_mark_size__ __bs_mark_material__ mark, __bs_mark_shape__ and __bs_mark_outline__, sits __bs_mark_place__, showing the capital letters "__bs_mark_initials__" in __name_logo_font__.']
    G['maker_bs_converse_mark'] = ['A small round rubber-like mark with a thin ring and a stitched border sits __bs_mark_place__, carrying __name_logo_description__.',
        'A small round leather mark with a double line around the edge sits __bs_mark_place__, carrying __name_logo_description__.',
        'A small oval woven cloth mark with a stitched border sits __bs_mark_place__, carrying __name_logo_description__.']
    G['v102_marks_entry_points'] = ['bs_mark', 'bs_motif', 'bs_simple_shape', 'maker_bs_converse_mark']
    return G
