"""v78 stage B - steampunk phones (spp_) and home and decorative collections (hd_): vases and ceramics, lamps, mirrors, frames, glassware, rugs, candlesticks, textiles, wall art, ornaments."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from famlib import P
def A(l): return 'an' if l[0].lower() in 'aeio' else 'a'
SPP = """candlestick|candlestick phone|a tall brass candlestick telephone with a clockwork dial, an exposed gear train and a trumpet earpiece on a hook
wall_crank|crank phone|a wooden wall phone with a brass crank, twin bells, a speaking horn and riveted copper plates
pocket_phone|pocket handset|a palm-sized brass handset that opens like a pocket watch to show a tiny glowing screen and turning gears
gear_flip|gear flip phone|a flip phone with a copper and leather case, visible gears at the hinge and brass keys
tube_phone|speaking tube phone|a brass pipe terminal with a mouthpiece, a pressure dial and a coiled hose
desk_phone|desk phone|a heavy oak desk phone with brass dials, a glass tube display and a cloth-covered cord
smart_slate|steam slate|a thin slate of dark glass in a riveted brass frame with a leather back and tiny pipe vents
wrist_phone|wrist communicator|a wide leather cuff with a brass phone face, small dials and a coiled antenna
radio_phone|aether radio phone|a boxy phone with a copper coil antenna, glowing glass valves and a brass handset
rotary_phone|rotary phone|a black enamel and brass rotary phone with a gear-ringed dial and a bell on top
bell_pager|clockwork pager|a small brass box with a bell, a winding key and a paper scroll window
cane_phone|gadget cane phone|a cane whose brass head opens to a small earpiece, dial and mouthpiece""".split('\n')
SPP_MAT = P("polished brass; aged copper; dark leather and brass; oak and brass; riveted iron; verdigris-coated copper; mother-of-pearl and brass")
SPP_DET = P("a row of tiny gears showing through glass; a pressure gauge on the side; green patina in the corners; engraved scrollwork; a leather strap; a hanging brass key; a small steam vent; a cracked glass dial")
COND = P("in mint condition with its original box; lightly used with a soft patina; worn bright on every edge; scratched and dull; stained with age spots; missing a small part; cracked and repaired with glue; freshly restored to a high shine; dusty from years in an attic; heavily used and dented; covered in the marks of a workshop")
DISPLAY = P("in a glass-topped display case; on a velvet tray; on a shelf among other pieces; on a stand under a lamp; on a sideboard; on a market stall table; on a mantelpiece; on a windowsill; in a collector's cabinet; on a wooden table beside a lamp; in a shop window")
SERVICE = P("a handwritten price label; a repair tag tied on with string; a scratched owner's initials; a faded paper label; a dated inscription; a worn serial number; a chip on one edge; a tiny stamp underneath")
COLOUR = P("white; cream; deep blue; forest green; dusty rose; mustard yellow; black; terracotta; turquoise; pale grey; burgundy; sage green; gold; two-tone blue and white")
# name|types|materials|features|eras|marks
C = {
 'vase': ('vase or ceramic', "a tall narrow vase; a round squat vase; a pair of mantel vases; a bud vase; a lidded ginger jar; a storage jar; a decorated bowl; a jug with a handle; a planter pot; a bottle vase with a long neck; a trumpet vase; a rustic pitcher",
  "glazed earthenware; white porcelain; stoneware; painted ceramic; cobalt glass; terracotta; speckled stoneware", "a hand-painted flower band; a drip glaze; a crackle finish; a raised pattern; gilded edges; a pair of loop handles; a twisted neck; a plain matte surface",
  "from the 1900s; from the 1930s; from the 1950s; from the 1960s; from the 1970s; from the 1980s; of a current design", "foot"),
 'lamp': ('table lamp', "a ceramic base table lamp with a fabric shade; a brass desk lamp; a glass-shaded banker's lamp; a ribbed glass lamp; a lava lamp; a tripod floor lamp; a mushroom-shaped lamp; a bedside lamp with a pleated shade; a hanging pendant lamp; a tiffany-style stained glass lamp; an oil lamp converted for electricity",
  "brass; chrome; painted metal; ceramic; frosted glass; walnut wood; chrome and plastic", "a pleated fabric shade; a pull chain; a twisted cord; a stained glass shade; a dimmer dial; a white globe; an adjustable arm; a fringed shade",
  "from the 1900s; from the 1930s; from the 1950s; from the 1960s; from the 1970s; from the 1980s; of a current design", "base"),
 'mirror': ('mirror', "a round gilded wall mirror; a sunburst mirror; a tall oval floor mirror; a hand mirror; a dressing table mirror on a stand; a beveled rectangular mirror; an arched window mirror; a small shaving mirror; a rope-framed mirror; a mirror in a carved wooden frame",
  "gilded wood; carved oak; brass; painted metal; chrome; rattan; plain beveled glass", "a foxed silvered back; a beveled edge; spots of age on the glass; a hanging chain; a stand on the back; a carved crest at the top; a plain narrow frame; rays of gold spikes",
  "from the 1800s; from the 1900s; from the 1930s; from the 1950s; from the 1970s; of a current design", "frame"),
 'frame': ('picture frame', "a carved wooden picture frame; a hinged double frame; a silver table frame; a gilded gallery frame; a plain black frame with a white mount; a brass easel frame; a shadow box frame; a multi-photo wall frame; a painted folk-art frame; a tortoiseshell-style frame",
  "carved walnut; silver plate; gilded plaster; painted wood; black lacquer; brass; resin", "an oval cut-out; a velvet-backed stand; a ribbon on the top; an engraved corner; a peeling gold edge; a card mount; a cracked glass; a faded photograph inside",
  "from the 1880s; from the 1920s; from the 1950s; from the 1970s; from the 1990s; of a current design", "corner"),
 'glass': ('glassware', "a cut-glass decanter; a set of wine glasses; a bowl of pressed glass; a punch bowl on a stand; a carnival glass bowl; a set of tumblers; a cake stand; a lidded sugar bowl; a glass pitcher; a paperweight with an air bubble flower; a stemmed cordial glass",
  "clear cut crystal; amber pressed glass; green depression glass; blue glass; opalescent glass; iridescent glass; milk glass", "a diamond-cut pattern; a gilded rim; a frosted band; a stopper on a chain; tiny bubbles in the glass; an etched flower; a moulded fruit pattern; a chipped foot",
  "from the 1880s; from the 1920s; from the 1930s; from the 1950s; from the 1970s; of a current design", "base"),
 'rug': ('rug or carpet', "a hand-knotted wool rug; a braided oval rug; a runner for a hallway; a flat-woven kilim; a fringed Persian-style rug; a shag rug; a round jute rug; a hooked rug; a geometric 1960s rug; a rag rug",
  "wool; cotton; jute; braided rags; silk blend; synthetic pile", "a medallion pattern; a border of stripes; frayed fringe; a worn path down the middle; faded colours; a bold geometric repeat; a floral pattern; a stain in one corner",
  "from the 1900s; from the 1930s; from the 1950s; from the 1960s; from the 1970s; from the 1980s; of a current design", "back"),
 'candle': ('candlestick', "a pair of brass candlesticks; a tall silver candelabra; a glass hurricane candle holder; a wrought iron floor candle stand; a wooden candle block; a stubby ceramic holder with a handle; a tiered chandelier; a taper holder; a lantern for a tea light",
  "polished brass; silver plate; wrought iron; carved wood; pewter; coloured glass; ceramic", "a drip tray; a half-melted candle; a twisted stem; a wide base; a curved handle; stains of old wax; a snuffer on a chain; a bobeche catching wax",
  "from the 1700s; from the 1800s; from the 1900s; from the 1950s; from the 1970s; of a current design", "base"),
 'textile': ('cushion or textile', "a patchwork quilt; a knitted throw; an embroidered cushion; a crocheted doily; a woven wall hanging; a tasselled bolster; a set of linen tea towels; a velvet cushion; a macrame hanger; a tablecloth with lace edging",
  "cotton; wool; linen; velvet; lace; patchwork scraps; jute", "a floral embroidered pattern; a faded stripe; hand-stitched edges; a worn patch; a fringe along the edge; a darned corner; a small stain; bold geometric blocks",
  "from the 1900s; from the 1930s; from the 1950s; from the 1970s; from the 1980s; of a current design", "label"),
 'art': ('wall art', "a framed oil landscape; a set of botanical prints; a brass wall plate; a woven tapestry; a relief plaque; a framed embroidery sampler; a wooden mask; a pair of ceramic wall plates; a framed map; a macramé wall panel; a mirror mosaic; a framed black and white photograph",
  "oil on canvas; ink on paper; carved wood; fired clay; woven wool; brass; stitched cotton", "a dark varnish; a gold frame; a hanging wire; a small signature in a corner; a faded colour; foxed paper; a raised surface; a hand-lettered caption",
  "from the 1800s; from the 1900s; from the 1930s; from the 1950s; from the 1970s; of a current design", "corner"),
 'ornament': ('ornament', "a porcelain shepherdess figurine; a pair of china dogs; a brass owl; a glass animal; a painted wooden bird; a ceramic cat; a music box; a snow globe; a pair of bookends; a resin garden gnome; a brass bell; a miniature ceramic cottage",
  "painted porcelain; brass; cast iron; blown glass; carved wood; glazed ceramic; resin", "a gilded edge; delicate painted detail; a chipped ear; a worn base; a felt pad underneath; a tiny crack; a faded smile; a painted flower",
  "from the 1900s; from the 1930s; from the 1950s; from the 1960s; from the 1980s; of a current design", "base"),
}
DISP = {'rug': "on a polished wooden floor; hung over a wooden rail; rolled up against a wall; spread in a sunlit hallway; in a market stall pile",
 'mirror': "hung on a papered wall; leaning against a wall; on a dressing table; above a fireplace; in a shop with other mirrors",
 'art': "hung on a papered wall; above a fireplace; leaning against a wall; in a gallery row; in a shop window",
 'frame': "on a sideboard; on a mantelpiece; hung on a papered wall; on a bedside table; among other frames on a wall",
 'textile': "folded on a bed; draped over a chair; hung from a rail; on a wooden table; in a market stall pile",
 'lamp': "on a bedside table; on a sideboard; on a wooden desk; on a shop shelf; in a window"}
def build(final=None):
    G = {}
    sk = []
    for row in SPP:
        k, label, look = row.split('|')
        G['spp_%s_look' % k] = ['%s %s, %s' % (A(label), label, look)]
        G['spp_%s_prompt' % k] = ['A steampunk telephone, __spp_%s_look__, made of __spp_material__, with __spp_detail__. It is __spp_cond__, and it is __spp_display__.' % k]
        G['spp_%s_short' % k] = ['__spp_%s_look__.' % k]
        sk.append(k)
    G['spp_material'] = SPP_MAT; G['spp_detail'] = SPP_DET; G['spp_cond'] = COND; G['spp_display'] = DISPLAY
    for s_ in ('look', 'prompt', 'short'): G['spp_' + s_] = ['__spp_%s_%s__' % (k, s_) for k in sk]
    G['spp_timeline_prompt'] = ['A row of steampunk telephones, from the oldest design at the left to the newest at the right. They are ' + ', then '.join('__spp_%s_look__' % k for k in ('wall_crank', 'candlestick', 'desk_phone', 'rotary_phone', 'gear_flip', 'smart_slate')) + '. They are __spp_display__.']
    allp = []
    G['hd_condition'] = COND; G['hd_display'] = DISPLAY; G['hd_service'] = SERVICE; G['hd_colour'] = COLOUR
    for k, (noun, types, mats, feats, eras, mk) in C.items():
        G['hd_%s_type' % k] = P(types); G['hd_%s_material' % k] = P(mats); G['hd_%s_feature' % k] = P(feats); G['hd_%s_era' % k] = P(eras)
        G['hd_%s_marks' % k] = ['with the maker name __text_brand__ stamped on the %s' % mk, 'with the maker name __text_brand__ painted on the %s and a small mark of __text_logo_emblem__' % mk, 'with a paper label on the %s reading __text_brand__' % mk, 'with no marks at all']
        G['hd_%s_look' % k] = ['__hd_%s_type__, __hd_%s_era__, in __hd_colour__ with __hd_%s_feature__, made of __hd_%s_material__, __hd_%s_marks__' % (k, k, k, k, k)]
        G['hd_%s_display' % k] = P(DISP[k]) if k in DISP else ['__hd_display__']
        G['hd_%s_prompt' % k] = ['A home decoration, %s, __hd_%s_look__. It is __hd_condition__, with __hd_service__, and it is __hd_%s_display__.' % (noun, k, k)]
        G['hd_%s_short' % k] = ['__hd_%s_type__, __hd_%s_era__, in __hd_colour__.' % (k, k)]
        G['hd_%s_group_prompt' % k] = ['Three pieces of %s are shown together. The first is __hd_%s_short__ The second is __hd_%s_short__ The third is __hd_%s_short__ They are all __hd_condition__, and they are __hd_%s_display__.' % (noun, k, k, k, k)]
        allp.append(k)
    for s_ in ('prompt', 'group_prompt', 'short'): G['hd_' + s_] = ['__hd_%s_%s__' % (k, s_) for k in allp]
    G['v78_coll_entry_points'] = ['spp_prompt', 'spp_timeline_prompt', 'hd_prompt', 'hd_group_prompt', 'hd_short'] + ['hd_%s_prompt' % k for k in allp]
    return G
if __name__ == '__main__': print(len(build()))
