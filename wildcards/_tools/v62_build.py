"""v62 - art and media styles, unbranded product and packaging, signage helpers, and the condition (appearance modifier) system."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from paths import FINAL
from famlib import P, slug, run_mod, export_aoo_mod

MEDIUM = P("an oil painting, which is thick layered paint with visible brush strokes and rich blended colour; a watercolour painting, which is soft translucent washes of colour that bleed at the edges on textured paper; a gouache painting, which is flat, matte, opaque colour with clean edges; an acrylic painting, which is bold saturated colour with a smooth satin surface; a pencil drawing, which is fine graphite lines and soft shading on cream paper; a charcoal drawing, which is deep smudged blacks and soft greys on rough paper; an ink drawing, which is confident black pen lines with cross-hatched shading; a pastel drawing, which is soft chalky colour layered with visible strokes; a woodblock print, which is bold flat colour areas with carved lines and a slightly uneven ink texture; a linocut print, which is thick black outlines and a few flat colours with a rough carved look; a screen print, which is flat layered colour with crisp edges and a slight misregistration; a risograph print, which is grainy overlapping ink colours with a soft speckled texture; a stencil artwork, which is sprayed flat colour with sharp cut edges and soft fading at the borders; a mosaic, which is small square tiles of coloured stone and glass set with thin grout lines; a stained glass panel, which is bright translucent colour held in dark lead lines, lit from behind; an embroidery, which is dense coloured thread stitches on woven cloth with a raised texture; a paper cut artwork, which is layered sheets of coloured paper with soft shadows between the layers; a collage, which is torn and cut paper, fabric and printed scraps layered together; a clay sculpture, which is hand-modelled earthenware with visible finger marks and a matte glaze; a marble carving, which is smooth polished stone with fine chisel detail; a bronze casting, which is dark metal with a warm patina and sharp detail; a wire sculpture, which is a drawing in space made from bent metal wire; a digital painting, which is smooth blended colour with crisp lighting and fine detail; a vector illustration, which is flat clean shapes with solid colour and sharp edges; a pixel art picture, which is a low resolution grid of square coloured blocks with a limited palette; a comic book illustration, which is bold black outlines, flat colour and halftone dot shading; a children's picture book illustration, which is soft rounded shapes in gentle colour with a hand-painted look; a botanical illustration, which is precise fine line drawing with delicate watercolour colour on white paper; a technical drawing, which is precise thin lines, dimensions and light blue-line shading on white paper; an architectural sketch, which is quick confident pen lines with light colour wash; a fashion illustration, which is long elegant lines and loose colour washes; a tattoo flash drawing, which is bold black outlines and bright flat colour on cream paper; a paper marbling, which is swirling veins of colour floating on a pale ground; an ink wash painting, which is flowing black ink in many shades of grey on pale paper with plenty of empty space; a fresco, which is soft matte pigment painted into plaster with a slightly cracked surface; an illuminated manuscript page, which is fine ink lettering with gold leaf and small bright painted details; a papercraft diorama, which is folded and layered paper forms in a small lit box; a felt and fabric artwork, which is soft stitched wool shapes with a fuzzy texture; a neon sign artwork, which is glowing coloured glass tubes bent into shapes against a dark wall")
PALETTE = P("a warm earthy palette; a cool blue and grey palette; a bright primary colour palette; soft pastel colours; deep jewel colours; a limited palette of three colours; black and white with one bright accent; rich autumn colours; muted faded colours; high contrast saturated colours; a monochrome palette in one hue; fresh spring greens and yellows")
FINISH = P("a rough textured surface; a smooth clean finish; visible brush or pen marks; a slightly aged and yellowed finish; a glossy varnished finish; a matte chalky finish; fine paper grain showing through; a worn edge with small stains; a crisp new finish")
SUBJ_FOR_ART = P("a quiet harbour at dawn; a crowded street market; a single flower in a jar; a mountain valley in autumn; a person reading by a window; a pair of old boots; a bowl of fruit on a table; a lighthouse in a storm; a cat asleep on a chair; a busy kitchen; a field of tall grass in the wind; a bridge over a river; a night sky over a small village; a person walking a dog in the rain")

PROD = P("a ceramic mug, which is a rounded cup with a thick handle and a glazed finish; a glass bottle, which is a clear tall bottle with a narrow neck and a metal cap; a leather wallet, which is a folded rectangle of stitched brown leather; a wooden chopping board, which is a thick rectangle of pale wood with a hanging hole; a stainless steel water flask, which is a slim brushed-metal bottle with a screw lid; a pair of sunglasses, which are dark round lenses in a thin metal frame; a wristwatch, which is a round dial with a leather strap and a steel case; a canvas backpack, which is a roomy cloth bag with leather straps and metal buckles; a scented candle, which is wax in a thick glass jar with a cotton wick; a notebook, which is a thick stitched book with a soft cloth cover; a fountain pen, which is a slim lacquered barrel with a gold nib; a pair of leather gloves, which are fitted stitched gloves with a soft lining; a woven basket, which is a deep round basket of natural cane with two handles; a ceramic vase, which is a tall glazed vase with a narrow neck; a wool blanket, which is a thick folded blanket with woven stripes; a pair of headphones, which are cushioned ear cups on a padded metal band; a handheld mirror, which is a round glass mirror in a carved wooden frame; a bar of soap, which is a rectangular bar of cream soap pressed with a simple pattern; a tin of tea, which is a round metal tin with a tight lid; a jar of honey, which is a glass jar of golden honey with a wooden dipper; a metal kettle, which is a rounded kettle with a long spout and a curved handle; a pair of scissors, which are steel blades with orange handles; a tool roll, which is a canvas roll holding steel hand tools; a bicycle bell, which is a small chrome dome with a lever; a desk lamp, which is a jointed metal arm with a round shade; a travel mug, which is a tall insulated cup with a sealed lid; a plant pot, which is a terracotta pot with a saucer; a pair of binoculars, which are two black barrels with a central focus wheel; a hand-bound journal, which is a thick cream book with a leather strap; a rolled yoga mat, which is a thick rolled mat tied with a strap")
PSET = P("on a plain seamless white surface; on a plain seamless soft-grey surface; on a pale wooden table; on a slab of dark stone; on a folded linen cloth; on a pedestal in a bright room; in the middle of a clean concrete floor; on a sunlit windowsill; on a rough wooden crate; on a mirror surface showing a faint reflection")
PLIGHT = P("soft even studio light; a single window light from the left with a gentle shadow; warm low evening light; crisp bright daylight; soft overhead light with a faint shadow beneath; moody side light with deep shadow")
PANGLE = P("a straight-on front view; a three-quarter view from slightly above; a low angle view from the side; a top-down flat view; a close detail view of the material and stitching")
PACK = P("a cardboard box, which is a plain brown folded box with a tape seal; a glass jar, which is a clear round jar with a metal screw lid; a tin can, which is a plain metal can with a ring pull lid; a paper bag, which is a flat-bottomed bag of kraft paper with folded top; a bottle with a cork, which is a dark glass bottle with a natural cork stopper; a cloth pouch, which is a small drawstring bag of undyed cotton; a squeeze tube, which is a soft aluminium tube with a screw cap; a wooden crate, which is a slatted box with rope handles; a blister pack, which is a clear moulded plastic shell on a card back; a gift box, which is a rigid box with a lift-off lid and a satin ribbon; a wax paper wrapper, which is a folded wrap of pale paper tied with string; a glass bottle with a pump, which is a tall frosted bottle with a metal pump top; a cylinder tube, which is a round cardboard tube with a metal base and a lid; a mesh produce bag, which is a loose net bag with a drawstring; a pillow pack, which is a sealed foil bag with crimped ends; a spray bottle, which is a rounded plastic bottle with a trigger spray top; a jute sack, which is a coarse woven sack tied at the neck; a pizza-style flat box, which is a thin square box with a folded lid; a milk-style carton, which is a gable-topped paper carton with a pour spout; a glass tumbler pot with a lid, which is a short wide glass jar with a snug lid")
PLABEL = P("a plain white label with simple black lettering; a hand-written brown paper label; a tall narrow label with a thin border; a round sticker label with a small drawing of a plant; a printed band wrapped around the middle; no label at all, only the bare material; a stamped mark pressed into the surface; a tied paper tag on a string; a cream label with small neat text and a simple pattern border")
PFIN = P("a matte finish; a glossy finish; a recycled paper texture; a soft-touch coating; an embossed pattern; a plain unprinted surface")

SIGN = P("a hand-painted wooden shop sign; a hanging metal pub-style sign; a lit neon sign in a window; a chalkboard menu sign on the pavement; a painted brick wall sign; a road sign on a metal post; an enamel plate sign on a wall; a carved stone plaque; a banner hung across a street; a paper notice taped to a door; a printed poster on a wall; a market stall board; a lit box sign above a door; a stencilled warehouse wall sign; a small brass plaque beside a door; a painted ship name board")
SIGNTXT = P("tall painted capital letters; thin elegant curved script lettering; bold block letters with a thick outline; small neat serif lettering; hand-drawn rounded letters; glowing tube lettering; chipped gold leaf letters with a dark edge; stencil lettering with gaps; large simple sans-serif letters; faded old-fashioned lettering")
SIGNMSG = P("OPEN; CLOSED; WELCOME; FRESH BREAD; HOT COFFEE; BOOKS; TICKETS; EXIT; PUSH; PULL; NO PARKING; SLOW; TOILETS; MARKET; GARDEN; REPAIRS; ROOMS; BAKERY; FLOWERS; QUIET PLEASE; WAY IN; PRIVATE; FISH AND CHIPS; PHARMACY; WORKSHOP; THIS WAY; LOST AND FOUND; TEA ROOM; FRUIT; LIVE MUSIC")

# ---------------- condition system ----------------
KINDS = {
 'building': dict(parts=P("main walls; roof or top; entrance; windows or openings; base; railings; stonework or cladding; paintwork; ground floor; edges"), subject=['__arch_%s_prompt__' % t for t in ('apartment_block','barn','bridge','castle','house','lighthouse','market_hall','skyscraper','temple')]),
 'vehicle': dict(parts=P("body or frame; paintwork; wheels or running gear; fittings; front end; rear end; edges; surface; woodwork or metalwork; joints"), subject=['__veh_%s_prompt__' % t for t in ('aeroplane','bicycle','boat','bus','car','cart','motorbike','tractor','train')]),
 'furniture': dict(parts=P("top surface; legs or base; frame; finish; joints; edges; sides; fittings; corners; underside"), subject=['__furn_armchair_prompt__', '__furn_bed_prompt__', '__furn_bench_prompt__', '__furn_bedside_table_prompt__', '__furn_bathtub_prompt__', '__furn_blanket_chest_prompt__']),
 'clothing': dict(parts=P("main fabric; seams; edges; fastenings; lining; trim; stitching; surface; colour; shape"), subject=['__wear_prompt__']),
 'object': dict(parts=P("handle or grip; main body; surface finish; working end; fittings; markings; edges; joint or hinge; coating; body"), subject=['__tool_prompt__']),
 'sign': dict(parts=P("lettering; painted surface; frame; mounting; edges; background; lower corner; hanging chains; border; face"), subject=['__sign_prompt__']),
 'book': dict(parts=P("cover; spine; pages; corners; binding; edges; title lettering; endpapers; clasp; page edges"), subject=['__book_item__']),
 'statue': dict(parts=P("surface; base; plinth; head; face; outline; edges; carved details; stonework; shoulders"), subject=['__statue_item__']),
}
BOOKS = P("A thick hardback book with a cloth cover and gold title lettering; A slim paperback with a soft card cover; A large leather-bound volume with raised bands on the spine; A stack of three old books tied with string; A hand-bound notebook with a thread-stitched spine; A large flat atlas with a stiff board cover; A pocket-sized book with a ribbon marker; An open book lying face down on a table")
STATUES = P("A life-size stone figure of a robed person standing on a plinth; A bronze figure of a seated person with an open book; A marble bust of a person with a calm expression on a square base; A stone figure of a person on a horse; A carved wooden figure of a standing person holding a staff; A small bronze figure of a dancing person on a round base; A large stone figure of a seated person with folded hands; A weathered stone figure of a kneeling person beside a fountain")
G3 = {  # generic families: (light, moderate, heavy) with {p}
 'damage': ("a small chip on the {p}", "a clear crack running across the {p}", "the {p}, badly broken and split open"),
 'missing': ("a small piece missing from the {p}", "the {p}, partly missing", "the {p}, gone completely, leaving a gap"),
 'wear': ("light wear on the {p}", "the {p}, visibly worn and rubbed smooth", "the {p}, worn almost away"),
 'dirt': ("a light layer of dust on the {p}", "the {p}, stained and grubby", "the {p}, caked in thick dirt"),
 'graffiti': ("a small spray-painted tag on the {p}", "colourful spray-painted lettering and shapes across the {p}", "the {p}, covered in layers of graffiti"),
 'faded': ("the {p}, slightly sun-faded", "the {p}, faded and peeling in patches", "the {p}, bleached almost colourless and flaking"),
 'burnt': ("a faint smoke mark on the {p}", "scorch marks and blackening on the {p}", "the {p}, charred and burnt through"),
}
K3 = {  # kind specific families
 'decay': {
  'building': ("a little moss on the {p}", "damp stains, moss and creeping ivy on the {p}", "the {p}, overgrown with plants and crumbling with rot"),
  'vehicle': ("small spots of rust on the {p}", "orange rust patches spreading across the {p}", "the {p}, eaten through with rust"),
  'furniture': ("small dull patches on the {p}", "the {p}, dried out, cracked and warped", "the {p}, rotten and crumbling with woodworm holes"),
  'clothing': ("a few loose threads on the {p}", "small moth holes and frayed edges on the {p}", "the {p}, full of holes and falling apart"),
  'object': ("small spots of rust on the {p}", "the {p}, pitted and covered with orange rust", "the {p}, seized solid with thick rust"),
  'sign': ("small blisters of paint on the {p}", "the {p}, peeling and rusting", "the {p}, rotted and flaking away"),
  'book': ("slight brown spotting on the {p}", "the {p}, stained, spotted and slightly mouldy", "the {p}, damp-swollen, mouldy and crumbling"),
  'statue': ("a little green moss on the {p}", "the {p}, stained with lichen and moss", "the {p}, eroded, crumbling and covered with lichen")},
 'repair': {
  'building': ("a neat patch of fresh mortar on the {p}", "the {p}, visibly mended with mismatched new material", "the {p}, held together by many rough repairs and props"),
  'vehicle': ("a neat welded repair on the {p}", "the {p}, mended with a different coloured panel", "the {p}, held together with welds, tape and patches"),
  'furniture': ("a neat glued repair on the {p}", "the {p}, mended with visible screws and metal plates", "the {p}, held together with clamps, wire and patches"),
  'clothing': ("a neat small stitched patch on the {p}", "the {p}, mended with bright contrasting stitches and patches", "the {p}, covered in layers of patches and darning"),
  'object': ("a neat repair on the {p}", "the {p}, mended with wire and a clamp", "the {p}, held together with tape, wire and patches"),
  'sign': ("a neat repainted patch on the {p}", "the {p}, mended with a bolted metal plate", "the {p}, patched together from several pieces"),
  'book': ("a neat strip of tape on the {p}", "the {p}, re-glued and mended with cloth tape", "the {p}, held together with string, tape and patches"),
  'statue': ("a neat filled crack in the {p}", "the {p}, mended with visible metal pins and fresh filler", "the {p}, pieced together from many repaired fragments")},
 'fine': {
  'building': ("the {p}, clean and well kept", "the {p}, beautifully finished with fine detail", "the {p}, exquisite, with superb craftsmanship and rich detail"),
  'vehicle': ("the {p}, clean and polished", "the {p}, flawless and gleaming", "the {p}, concours-quality, perfect in every detail"),
  'furniture': ("the {p}, smooth and well made", "the {p} shows fine joinery and a deep glowing finish", "the {p}, masterfully made with perfect joints and a flawless finish"),
  'clothing': ("the {p}, with neat even stitching", "the {p}, beautifully tailored with fine detail", "the {p}, superbly crafted with flawless hand finishing"),
  'object': ("the {p}, smooth and well made", "the {p}, precisely made and finely finished", "the {p}, of the highest quality, flawless and gleaming"),
  'sign': ("the {p}, crisp and clean", "the {p}, beautifully painted with fine detail", "the {p}, a masterpiece of sign painting with perfect gilding"),
  'book': ("the {p}, clean and well bound", "the {p}, finely bound with crisp detail", "the {p}, a superb piece of bookbinding with gold detail"),
  'statue': ("the {p}, smooth and well carved", "the {p}, finely carved with lifelike detail", "the {p}, a masterpiece of carving with astonishing fine detail")},
 'cheap': {
  'building': ("the {p}, slightly uneven", "the {p}, crudely built with visible gaps", "the {p}, shoddy, crooked and badly put together"),
  'vehicle': ("the {p}, slightly uneven", "the {p}, thin, wavy and badly finished", "the {p}, flimsy, dented and badly put together"),
  'furniture': ("the {p}, slightly rough", "the {p}, thin, wobbly and poorly finished", "the {p}, flimsy, crooked and falling apart"),
  'clothing': ("the {p}, with slightly uneven stitching", "the {p}, thin with loose, crooked stitching", "the {p}, flimsy, twisted and coming apart"),
  'object': ("the {p}, slightly rough", "the {p}, thin, rough and poorly finished", "the {p}, flimsy, crooked and barely holding together"),
  'sign': ("the {p}, with slightly uneven lettering", "the {p}, crudely painted with wobbly lines", "the {p}, badly made, crooked and messy"),
  'book': ("the {p}, slightly crooked", "the {p}, thin, badly trimmed and loosely glued", "the {p}, flimsy, crooked and falling out"),
  'statue': ("the {p}, slightly rough", "the {p}, crudely carved with uneven proportions", "the {p}, clumsy, lumpy and badly formed")}}
ST = ('light', 'moderate', 'heavy')
def build(final=FINAL):
    G = {}
    G['medium_name'] = MEDIUM; G['medium_palette'] = PALETTE; G['medium_finish'] = FINISH; 
    G['medium_prompt'] = ['__medium_subject__, as __medium_name__, with __medium_palette__ and __medium_finish__.']
    G['medium_on_subject_prompt'] = ['__frame_clarity__ __medium_subject__, as __medium_name__, with __medium_palette__ and __medium_finish__.']
    G['prod_item'] = PROD; G['prod_set'] = PSET; G['prod_light'] = PLIGHT; G['prod_angle'] = PANGLE
    G['prod_prompt'] = ['A product shot of __prod_item__. It sits __prod_set__, seen from __prod_angle__, in __prod_light__.']
    G['pack_type'] = PACK; G['pack_label'] = PLABEL; G['pack_finish'] = PFIN
    G['pack_prompt'] = ['A packaging shot of __pack_type__ with __pack_label__ and __pack_finish__, __prod_set__, seen from __prod_angle__, in __prod_light__.']
    G['sign_lettering'] = SIGNTXT; G['sign_message'] = SIGNMSG
    G['sign_prompt'] = ['__sign_type__, with the words "__sign_message__" in __sign_lettering__.']
    G['book_item'] = [x + '.' for x in BOOKS]; G['statue_item'] = [x + '.' for x in STATUES]
    G['sign_type'] = [x[0].upper() + x[1:] for x in SIGN]; G['medium_subject'] = [x[0].upper() + x[1:] for x in SUBJ_FOR_ART]
    fams = list(G3) + list(K3)
    for kind, d in KINDS.items():
        parts = d['parts']
        for fam in fams:
            for si, s in enumerate(ST):
                if fam in G3: tpl = G3[fam][si]
                else: tpl = K3[fam][kind][si]
                G['cond_%s_%s_%s' % (kind, fam, s)] = [tpl.format(p=p) for p in parts]
            G['cond_%s_%s' % (kind, fam)] = ['__cond_%s_%s_%s__' % (kind, fam, s) for s in ST]
        for s in ST: G['cond_%s_%s' % (kind, s)] = ['__cond_%s_%s_%s__' % (kind, f, s) for f in fams]
        G['modify_%s' % kind] = ['__cond_%s_%s__' % (kind, f) for f in fams]
        G['cond_subject_%s' % kind] = list(d['subject'])
        G['condition_%s_prompt' % kind] = ['__cond_subject_%s__ Its condition shows %s.' % (kind, '__modify_%s__' % kind)]
        for s in ST: G['condition_%s_%s_prompt' % (kind, s)] = ['__cond_subject_%s__ Its condition shows __cond_%s_%s__.' % (kind, kind, s)]
        G['condition_%s_good_prompt' % kind] = ['__cond_subject_%s__ It is in excellent condition, __cond_%s_fine__.' % (kind, kind)]
    G['condition_prompt'] = ['__condition_%s_prompt__' % k for k in KINDS]
    G['condition_ruined_prompt'] = ['__condition_%s_heavy_prompt__' % k for k in KINDS]
    G['v62_entry_points'] = ['medium_prompt', 'prod_prompt', 'pack_prompt', 'sign_prompt', 'condition_prompt', 'condition_ruined_prompt']
    return G
def run(final): return run_mod(sys.modules[__name__], final)
def export_aoo(out): return export_aoo_mod(build(FINAL), out, skip=('medium_on_subject_prompt',))
if __name__ == '__main__': run(FINAL)
