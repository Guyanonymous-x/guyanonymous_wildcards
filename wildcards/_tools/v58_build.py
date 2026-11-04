"""v58 - outerwear, hats, bags, scarves, gloves and belts built from parts (random assembly)."""
import os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from paths import FINAL
from famlib import P, slug, an, fams, run_mod, export_aoo_mod
COL = P("black; charcoal grey; navy blue; forest green; olive green; burgundy; camel brown; chocolate brown; sand beige; cream white; rust orange; mustard yellow; dusty pink; sky blue; teal; deep purple; bright red; slate grey; ochre; off-white; plum; khaki; denim blue; terracotta")
PAT = P("plain; fine stripes; a houndstooth check; a large plaid; a herringbone weave; small polka dots; a subtle tone-on-tone pattern; a bold block-colour design; a faded camouflage print; a woven geometric pattern")
COND = P("brand new and crisp; lightly worn; softly broken in; faded along the seams; patched at the elbows; heavily worn with frayed edges; carefully mended; spotless and pressed; creased from use")
CATS = {
 'outerwear': dict(material=P("heavy wool; waxed cotton; soft leather; quilted nylon; corduroy; denim; fleece; cotton canvas; tweed; suede; waterproof coated fabric; padded down-filled fabric; boiled wool; linen"), lining=P("a smooth satin lining; a warm fleece lining; a quilted lining; a plain cotton lining; a checked wool lining; no lining; a bright contrasting lining"), closure=P("a row of large buttons; a heavy zip; snap fasteners; toggles and loops; a tie belt; a double-breasted button front; hooks and eyes; an open front"),
   pockets=P("two deep side pockets; flap chest pockets; hidden inner pockets; large patch pockets; slanted hand-warmer pockets; no pockets"), collar=P("a wide pointed collar; a high stand collar; a fur-trimmed hood; a plain turned-down collar; a funnel neck; a shawl collar"), cuffs=P("ribbed cuffs; buttoned cuffs; elasticated cuffs; plain hemmed cuffs; turned-back cuffs")),
 'hats': dict(material=P("felt; woven straw; wool; leather; cotton canvas; knitted wool; velvet; denim; silk; waxed cotton; fur felt; linen"), band=P("a plain ribbon band; a braided leather band; a thin cord; a wide striped band; no band; a small metal buckle band"), lining=P("a plain cotton lining; a satin lining; a sweat band; a fleece lining; no lining"), trim=P("a small feather; a woven badge; a button on top; stitched decoration; a plain finish; a pinned brooch")),
 'bags': dict(material=P("soft leather; canvas; woven straw; nylon; patent leather; suede; waxed cotton; woven rope; recycled fabric; jute; quilted fabric"), strap=P("a long adjustable shoulder strap; two short rolled handles; a thin chain strap; a wide padded strap; a top handle and a detachable strap; woven rope handles"), closure=P("a zip along the top; a magnetic flap; a drawstring; a buckled strap; a twist lock; an open top"), pockets=P("a zipped outer pocket; two inner pockets; a padded laptop sleeve; a hidden back pocket; no extra pockets"), hardware=P("brass hardware; silver-coloured hardware; matt black hardware; gold-coloured hardware; plain stitched edges")),
 'scarves': dict(material=P("soft wool; silk; cotton; cashmere-like wool blend; linen; fine knit; fleece; light viscose; crinkled cotton"), fringe=P("a twisted fringe; a plain hemmed edge; tassels at each end; a rolled edge; a lace trim; a bound edge"), size=P("a long, narrow length; a wide, generous square; a medium rectangle; an extra-long length; a small neat square"), wear=P("wrapped twice around the neck; tied loosely in front; draped over the shoulders; knotted at the side; worn over the head")),
 'gloves': dict(material=P("soft leather; knitted wool; fleece; suede; cotton; waterproof fabric; silk; padded nylon"), cuff=P("a long cuff; a short cuff; a ribbed knit cuff; a buttoned wrist strap; an elasticated wrist"), lining=P("a warm fleece lining; a smooth silk lining; no lining; a quilted lining; a wool lining"), grip=P("grip patches on the palm; plain palms; stitched finger seams; reinforced fingertips")),
 'belts': dict(material=P("smooth leather; woven fabric; braided cord; suede; canvas webbing; embossed leather; elastic; rope"), buckle=P("a plain metal frame buckle; a large decorative buckle; a pin buckle; a hook closure; a sliding clasp; a twist buckle"), width=P("a very narrow strip; a medium width; a wide band; an extra-wide cinch"), detail=P("evenly spaced holes; stitched edges; small metal studs; a keeper loop and a tail end; a contrasting edge colour")),
}
TYPES = {
 'outerwear': {'trench coat': 'a knee-length double-breasted coat with a belt, storm flap and epaulettes', 'parka': 'a thick hooded jacket that sits at mid-thigh with a drawcord waist', 'peacoat': 'a short, heavy, double-breasted wool coat with wide lapels', 'puffer jacket': 'a short jacket with horizontal quilted baffles that puff out', 'bomber jacket': 'a short, fitted jacket with a ribbed hem and cuffs', 'denim jacket': 'a short jacket with a boxy cut, yoke seams and chest pockets', 'leather jacket': 'a fitted, short jacket with an asymmetric zip and wide lapels', 'overcoat': 'a long, tailored coat that reaches the knees with a single-breasted front', 'rain poncho': 'a loose waterproof sheet with a hood and an open side', 'cloak': 'a long, sleeveless cape that fastens at the neck and hangs to the calves', 'anorak': 'a pull-over hooded jacket with a kangaroo pocket', 'windbreaker': 'a light, loose jacket with a stand collar and a zipped front', 'duffle coat': 'a mid-length hooded coat with rope toggles and a wide patch pocket', 'quilted vest': 'a sleeveless padded jacket with a zipped front', 'blazer': 'a tailored jacket with notch lapels and two buttons', 'kimono-style jacket': 'a loose, open jacket with wide straight sleeves and a long front panel'},
 'hats': {'wide-brim hat': 'a hat with a broad flat brim and a rounded crown', 'bucket hat': 'a soft hat with a short sloping brim all around', 'beanie': 'a close-fitting knitted cap with a turned-up cuff', 'flat cap': 'a rounded cap with a small stiff peak at the front', 'baseball cap': 'a curved-peak cap with a six-panel crown and an adjustable strap', 'fedora': 'a soft felt hat with a pinched crown and a medium brim', 'beret': 'a flat, round, soft hat worn tilted on the head', 'sun hat': 'a lightweight hat with a very wide brim to shade the face', 'top hat': 'a tall, flat-topped cylindrical hat with a narrow brim', 'turban': 'a long length of cloth wound round the head into a rounded shape', 'cowboy hat': 'a hat with a high crown, a creased top and a wide curved brim', 'headscarf': 'a square of cloth tied over the hair'},
 'bags': {'backpack': 'a bag with two shoulder straps and a large main compartment', 'tote bag': 'a large open bag with two parallel handles', 'messenger bag': 'a flat bag with a long cross-body strap and a flap front', 'clutch': 'a small flat bag held in the hand with no handle', 'duffel bag': 'a large cylindrical bag with a wide opening and two handles', 'satchel': 'a rectangular bag with a flap front and a top handle', 'bucket bag': 'a rounded bag with a drawstring top and a single shoulder strap', 'belt bag': 'a small pouch worn at the waist on a strap', 'briefcase': 'a stiff, rectangular case with a top handle and two latches', 'basket bag': 'a rounded woven bag with two short handles', 'suitcase': 'a hard-shell rolling case with a telescopic handle and four wheels'},
 'scarves': {'wool scarf': 'a long thick scarf for warmth', 'silk scarf': 'a lightweight smooth square that drapes softly', 'bandana': 'a square cloth often folded into a triangle and tied around the neck or head', 'shawl': 'a large wrap worn around the shoulders', 'infinity scarf': 'a looped scarf with no ends', 'pashmina': 'a wide, soft wrap with a fine texture', 'neck gaiter': 'a tube of stretch fabric worn around the neck'},
 'gloves': {'leather gloves': 'fitted gloves that follow the shape of the hand', 'mittens': 'gloves with a single space for four fingers and a separate thumb', 'fingerless gloves': 'gloves that leave the fingertips bare', 'work gloves': 'thick, hard-wearing gloves with reinforced palms', 'evening gloves': 'long, smooth gloves that reach past the elbow', 'cycling gloves': 'short gloves with padded palms'},
 'belts': {'leather belt': 'a classic strap with a metal buckle', 'rope belt': 'a thick twisted cord tied at the waist', 'cinch belt': 'a wide belt that pulls in the waist', 'chain belt': 'a loose belt of linked metal rings', 'sash': 'a broad band of cloth tied around the waist', 'webbing belt': 'a flat woven strap with a sliding buckle'},
}
OV = {('bags', 'suitcase', 'material'): P('hard polycarbonate shell; hard aluminium shell; textured plastic shell; ribbed hard shell'),
 ('outerwear', 'rain poncho', 'material'): P('waterproof coated fabric; clear plastic film; waxed cotton; rubberised nylon'),
 ('hats', 'baseball cap', 'material'): P('cotton twill; nylon; canvas; mesh and cotton'),
 ('hats', 'beanie', 'material'): P('knitted wool; fleece; soft cotton knit; ribbed acrylic knit'),
 ('belts', 'leather belt', 'material'): P('smooth leather; embossed leather; suede; braided leather'),
 ('belts', 'chain belt', 'material'): P('polished metal links; brass links; silver-coloured links; gold-coloured links'),
 ('belts', 'rope belt', 'material'): P('twisted cotton rope; braided cord; thick jute rope'),
 ('gloves', 'evening gloves', 'material'): P('smooth satin; fine silk; stretch velvet; soft kid leather'),
 ('gloves', 'mittens', 'material'): P('knitted wool; fleece; padded waterproof fabric'),
 ('outerwear', 'blazer', 'material'): P('fine wool; tweed; linen; corduroy; cotton twill'),
('outerwear', 'rain poncho'): dict(cuffs=P("open sleeveless sides; sides joined by press studs"), closure=P("a pull-over head opening with a drawcord hood; a short front placket with snaps")),
 ('outerwear', 'cloak'): dict(cuffs=P("a free-hanging edge; a weighted hem"), closure=P("a clasp at the throat; a tie at the neck; a pin at the shoulder")),
 ('outerwear', 'quilted vest'): dict(cuffs=P("bound armholes; ribbed armholes")),
 ('hats', 'turban'): dict(band=P("neat overlapping wound layers; a loose end tucked in at the side"), lining=P("a plain cotton underlayer; a fitted inner cap"), trim=P("a small brooch pinned at the front; a plain finish")),
 ('hats', 'headscarf'): dict(band=P("tied in a knot at the nape; tied under the chin; knotted at the side"), lining=P("a single layer of fabric; a double layer of fabric"), trim=P("a plain finish; a hand-rolled edge")),
 ('hats', 'beanie'): dict(band=P("a turned-up cuff; a ribbed edge"), lining=P("a plain knit lining; a fleece lining"), trim=P("a pom-pom on top; a woven label on the cuff; a plain finish")),
 ('bags', 'suitcase'): dict(strap=P("a telescopic handle and four spinner wheels; a top carry handle and two wheels"), closure=P("a zip around the edge; two combination latches"), pockets=P("a zipped front pocket; an expandable lining; a plain interior with straps")),
 ('bags', 'briefcase'): dict(strap=P("a rigid top handle; a top handle and a detachable shoulder strap"), closure=P("two brass latches; a combination lock; a flap and a buckle")),
 ('bags', 'clutch'): dict(strap=P("a small wrist loop; no strap at all"), closure=P("a magnetic flap; a snap clasp; a short zip")),
 ('bags', 'belt bag'): dict(strap=P("an adjustable waist strap with a clip buckle"), closure=P("a zip along the top; a flap and a snap")),
 ('bags', 'duffel bag'): dict(strap=P("two sturdy handles and a detachable shoulder strap"), closure=P("a zip along the top; a drawstring and a clasp")),
 ('bags', 'backpack'): dict(strap=P("two padded shoulder straps and a top grab handle; two wide adjustable shoulder straps")),
 ('bags', 'basket bag'): dict(strap=P("two short woven handles; two rope handles"), closure=P("an open top; a flap and a toggle")),
 ('belts', 'rope belt'): dict(buckle=P("knotted ends; a simple loop and toggle"), detail=P("twisted strands; frayed tassels at each end")),
 ('belts', 'sash'): dict(buckle=P("tied in a bow; tied in a knot with long ends"), detail=P("a fringed edge; a plain hemmed edge")),
 ('belts', 'chain belt'): dict(buckle=P("a hook clasp; a ring and bar clasp"), detail=P("alternating large and small links; a dangling charm")),
 ('scarves', 'neck gaiter'): dict(fringe=P("a plain hemmed edge; a smooth stitched edge"), wear=P("pulled up over the nose and mouth; worn loose around the neck; pulled up over the head")),
 ('scarves', 'infinity scarf'): dict(fringe=P("a plain stitched seam; a smooth edge"), wear=P("looped twice around the neck; draped long in front")),
 ('scarves', 'bandana'): dict(fringe=P("a plain hemmed edge; a rolled edge"), wear=P("tied around the neck; tied around the head; folded as a headband"))}
NOWORD = {'no lining': 'an unlined interior', 'no pockets': 'a clean front with no pockets', 'no band': 'a bare crown without a band', 'no extra pockets': 'a smooth plain back', 'no strap at all': 'no strap, carried in the hand', 'no decoration': 'a plain finish', 'no extra': 'a plain finish'}
def cleanp(v): return [NOWORD.get(x, x) for x in v]
def build(final=FINAL):
    G = {'wear_colour': COL, 'wear_pattern': PAT, 'wear_condition': COND}
    for cat, tdict in TYPES.items():
        shared = CATS[cat]
        for k, v in shared.items(): G['wear_%s_%s' % (cat, k)] = cleanp(v)
        keys = [k for k in shared if k != 'material']
        for t, shape in tdict.items():
            ts = slug(t); refs = {}
            for k in shared:
                if (cat, t, k) in OV:
                    G['wear_%s_%s_%s' % (cat, ts, k)] = cleanp(OV[(cat, t, k)]); refs[k] = '__wear_%s_%s_%s__' % (cat, ts, k)
                elif (cat, t) in OV and k in OV[(cat, t)]: G['wear_%s_%s_%s' % (cat, ts, k)] = cleanp(OV[(cat, t)][k]); refs[k] = '__wear_%s_%s_%s__' % (cat, ts, k)
                else: refs[k] = '__wear_%s_%s__' % (cat, k)
            G['wear_%s_%s_prompt' % (cat, ts)] = ['%s, which is %s. It is made of %s in __wear_colour__ with __wear_pattern__, with %s. It is __wear_condition__.' % (an(t), shape, refs['material'], ', '.join(refs[k] for k in keys))]
        G['wear_%s_names' % cat] = sorted(tdict)
        G['wear_%s_prompt' % cat] = ['__wear_%s_%s_prompt__' % (cat, slug(t)) for t in tdict]
    G['frame_animal_quad_prompt'] = ['__frame_clarity__ __frame_ratio__ The image is divided into four equal panels by thin white lines, two across and two down. Each panel shows a different animal, the whole animal entirely inside its own panel and nothing cut off by the panel edges, with natural light and true-to-life colour. Top left panel. __animal_prompt__ Top right panel. __animal_prompt__ Bottom left panel. __animal_prompt__ Bottom right panel. __animal_prompt__']
    G['wear_prompt'] = ['__wear_%s_prompt__' % c for c in TYPES]
    G['v58_entry_points'] = ['wear_prompt'] + ['wear_%s_prompt' % c for c in TYPES]
    return G
def run(final): return run_mod(sys.modules[__name__], final)
def export_aoo(out): return export_aoo_mod(build(FINAL), out)
if __name__ == '__main__': run(FINAL)
