"""Detailed adult lingerie / underwear / sleepwear / accessory garment descriptions (original wording, no brands), 25 per shop-style section.
Row: name | front | back | covered | not covered | cut and fit | fabric | colourways (comma list).  Garments only; no people described."""
S = {}
def P(s): return [tuple(x.strip() for x in l.split('|')) for l in s.strip().split('\n') if l.strip()]
S['ultra'] = P("""
slit-cup embroidered tulle bra|plunging underwire cups with a vertical slit down each cup that leaves the nipple area open, floral embroidery on the tulle, a small bow at the centre gore|a three-hook closure with a narrow stretch band and thin adjustable shoulder straps|the lower and outer breast, the underbust and the sides|the nipples and the inner part of each breast through the slits|snug underwire fit, low centre gore, straps adjustable|embroidered tulle with a satin-bound edge|black and crimson, black and ivory, midnight and gold
crotchless open-back bikini|a low-rise bikini front with a scalloped lace waistband and a centre seam that opens between the legs|a bare back panel with only two crossing straps at the waist, so the buttocks are largely uncovered|the hips, the lower belly and the sides of the buttocks|the genital area and most of the buttocks|stretchy, mid-rise at the front, high-cut at the leg|embroidered tulle with lace trim|black and red, black and nude, deep plum
pearl crotchless thong|a narrow triangle of lace at the front, a single strand of pearls that runs from the front waistband down between the legs|a thin string at the waist and a pearl strand running to the back waistband|the pubic mound only through the lace triangle|the genital area and the buttocks|string-thin, low-rise, very high-cut leg|lace and glass pearls on elastic cord|ivory, black, blush
crotchless teddy with open back|a plunging halter bodice with underwire cups in sheer tulle, a deep V down to the navel, a crotch that is open between the legs|a completely open back down to the waist, crossing elastic straps above the buttocks|the breasts and the torso at the front|the back, the buttocks and the genital area|high-cut fitted leg, snug through the torso, halter tie at the neck|embroidered tulle with satin ribbon straps|black, crimson, midnight blue
leopard-print lace crotchless teddy|a leopard-print lace bodice with a scooped neckline, shaped cups with wire support, a narrow waist panel|a low scooped lace back with a hook-and-eye closure, a thong-back cut with an open gusset|the breasts and the torso|the genital area|snug at the bust, high-cut legs, stretchy|stretch lace in a leopard print with satin trim|leopard and black, leopard and red
crotchless bodystocking with illusion garters|a fishnet body that runs from a halter neckline to the thighs, with printed illusion garter straps and stocking tops at the thigh|the same fishnet at the back, with a seam up the centre and an open crotch|nothing opaque: fine fishnet over the whole torso and legs|the genital area is open; all other skin shows through the net|stretches to fit, one-size feel, snug on the legs|diamond-weave fishnet with an opaque printed garter panel|black, black with red bows, nude with black
fishnet crop top and panty set|a long-sleeved fishnet crop top that ends under the bust and a matching panty|a plain net back, the panty with a full-cut back|the arms and the panty area lightly through net|the bust and midriff show through the open net|stretchy, cropped, high-waisted panty|wide-gauge fishnet|black, white, hot pink
full-length crotchless fishnet bodystocking|a long-sleeved, high-necked net body that runs down to the ankles, the front seam open at the crotch|a net back with a flat centre seam and an open-gusset rear|nothing: all of the net is sheer|the entire body shows through, the genital area is open|extremely stretchy, snug from neck to ankle|fine micro-fishnet|black, nude, red
lace and fishnet teddy bodystocking|lace cups with scalloped edges above a fishnet torso panel that runs down to a high-cut leg|a lace-edged back panel with a low scoop, the rest in fishnet|the breasts through lace, the hips through lace trim|the stomach and the back through the net|stretchy, high-cut leg, sweetheart neckline|stretch lace and fishnet|black, burgundy, white
lace-top thigh-highs with a skinny garter belt|a narrow lace waistband belt with four thin suspender straps that clip to the stockings|the straps cross over the buttocks at the back and clip at the rear stocking tops|only the waist and thighs|the hips, the buttocks and everything between the suspender straps|adjustable straps, a snug elastic belt|sheer nylon stockings with lace tops, a lace belt|black, nude with black lace, red
O-ring open-cup bra|a bra with no fabric over the nipples, each cup is a lower shelf with a metal O-ring joining the straps at the centre|a hook-and-eye band at the back with thin straps and a crossing strap at the upper back|the underside of the breasts and the ribs|the breasts above the shelf, the nipples|underwire shelf, adjustable straps, snug|satin-covered underwire with elastic webbing and metal rings|black, red, leopard print
open-bust shelf bra|a bra with half-cups that only lift the breasts from underneath, the top edge scalloped|a three-hook back with a wide band|the lower half of the breasts and the underbust|the nipples and the upper half of each breast|firm lifting, underwire, wide band|stretch lace with lined shelf cups|black, nude, red
open-cup bustier with suspenders|a boned bustier with open cups that frame the breasts, a narrow waist and four suspender straps hanging below|a lace-up back with a ribbon tie and a long hook-and-eye placket|the ribs, the waist and the upper hip|the breasts and the nipples, the belly below the bustier hem is open|steel-boned, cinched waist, adjustable laces|satin with lace trim and steel boning|black, ivory, burgundy
caged strappy bra with open nipples|a harness-style cage of crossing straps over the breasts with open triangles at the nipples, a central O-ring|a crossed strap back with an adjustable buckle|the straps only|the breasts and the nipples|adjustable, fitted body harness|elastic webbing with metal hardware|black, red, white
zip-crotch lace bodysuit|a lace bodysuit with a deep V, long sleeves and a lace-trimmed leg opening, a zipper running through the crotch|a deep scoop lace back and a full-coverage seat|the torso and the seat through lace|the breasts show through the lace; the zipper opens the crotch|stretchy, snug, high-cut leg|stretch floral lace|black, red, blue
cut-out mesh teddy|a mesh teddy with two circular cut-outs over the cups and a sheer midsection, high-cut legs|an open diamond back with a thong cut|the hips and the sides|the nipples through cut-outs, the back and buttocks|stretchy, snug, high-cut|stretch mesh with elastic trim|black, nude, white
ring-front peek-a-boo thong|a small triangle with a front slit and a gold ring at the waistband centre|a string back with a narrow strap|a minimal amount of the front|the genital area is partly visible through the slit, the buttocks are bare|string-thin, low-rise|stretch satin with metal ring|black, red, gold
chain and leatherette body harness|a halter strap from the neck splits into chains over the breasts and down the torso, joined to a waist strap|crossed straps over the back with a buckle|none: it is a strap-only piece|the breasts, torso and back are uncovered|fully adjustable straps|faux leather with metal chains and buckles|black, black and silver, red
open-front sheer babydoll with G-string|a sheer babydoll with an open front tied at the bust, a flared hem to the hip|a flowing sheer back and a thong back on the matching G-string|the torso loosely through sheer fabric|the front opening, the breasts, and the buttocks show through|loose flared fit, adjustable halter ties|sheer mesh with satin bows|black, pink, ivory
open-bust corset with detachable garters|a longline corset that ends under the breasts, boning, a front busk|a lace-up back with modesty panel and a pair of detachable garter straps|the ribs, waist and hips|the breasts, the lower belly below the hem and the buttocks|steel boning, cinched waist, adjustable laces|satin and lace, steel boning|black, red, ivory
crotchless garter belt panty|a wide lace waistband panty with six garter straps and a crotch seam that opens|a high lace waistband and open lace seat panel with crossing straps|the hips and the waist|the genital area and parts of the buttocks|adjustable, snug, high-cut|stretch lace and satin straps|black, burgundy, ivory
lace-up crotchless catsuit|a long-sleeved catsuit with a plunging lace-up front, cup-free torso and a crotch seam that opens|a zipped or laced back|the arms, the legs and the torso through mesh|the chest and genital area are open|stretchy, snug, full length|stretch mesh with lace and ribbon lacing|black, red, white
open-front sheer lace robe|a long robe with an open front that hangs straight, lace sleeves, a tie belt|a sheer, floor-length back with a lace yoke|the arms, the back and the sides lightly|the whole front is open and everything underneath shows through|loose, floor length, drapey|sheer lace with chiffon|black, ivory, wine
wet-look zip-front mini dress|a glossy mini dress with a full zipper from neckline to hem, a halter neck and a short hem|a completely open back from neck to waist, a low scooped back|the breasts through the stretchy fabric, the hips and the belly|the back is open, the zipper can open the front fully|body-hugging, very short|stretch faux-latex wet-look fabric|black, red, silver
lace ouvert tanga with bow|a lace tanga with a centre panel that stays open and a satin bow at the waist|a ribbon tie back with thin string sides|the hips only|the genital area and the buttocks|string sides, very low rise|lace and satin|black, red, blush
""")
S['lingerie'] = P("""
lace and mesh V-wire bra|plunging lace cups with an underwire that forms a deep V, sheer mesh at the sides and a narrow centre gore|a three-hook band with a mesh back and thin straps|the breasts through lace, partly sheer through the mesh|the skin shows through the sheer mesh panels|underwire, low-cut, snug|stretch lace and mesh|midnight blue, wine, black
lace and pearl crotchless thong|a lace front triangle with a pearl strand through the centre, a satin bow|a string back with a pearl strand at the back|the front triangle only|the genital area and the buttocks|string-thin, low-rise|lace and glass pearls|burgundy, midnight, ivory
lace and mesh waist garter|a wide mesh waist cincher with a lace edge and four garter straps|a hook-and-eye closure and crossed straps at the back|the waist and hips|the genital area and buttocks are uncovered (worn over underwear or alone)|adjustable straps, snug band|stretch lace and mesh|wine, black, navy
lace and mesh chemise set|a knee-short chemise with lace bodice cups, mesh skirt layers, a plunging neckline and a matching thong|a low scoop back with ribbon straps and a flowing mesh back|the breasts and torso lightly through lace and mesh|the legs and hips show through the sheer skirt|loose fit below the bust, adjustable straps|lace and soft mesh|midnight blue, wine, black
halter babydoll with matching thong|a halter babydoll with a deep V, an empire seam under the bust and a sheer flared skirt that ends at the hips|a tie closure at the neck and a low open back, a tie at the waist|the breasts through lace|the midriff and hips show through the sheer skirt|flared, halter, hip-length|lace bodice and chiffon skirt|lipstick red, black, ivory
satin demi bra with lace trim|a demi cup with a scalloped lace edge and a small satin bow|a three-hook band with a plain back and adjustable straps|the lower breasts, partial coverage at the top|the upper breast at the top edge|underwire, balconette lift|satin with lace trim|red, champagne, black
satin and lace teddy|a lace bodice with a satin waist band and a high-cut leg, a plunge neckline|a low scoop back and a snap crotch|the breasts and torso|the legs and the sides|snug, high-cut|stretch lace and satin|ivory, black, blush
sheer mesh chemise with ruffle hem|a plunging chemise with narrow straps, a bodice in lace and a gathered mesh skirt that falls mid-thigh|a low lace back with a straight hem|the breasts through lace|the legs and hips through the mesh|loose and flowing, adjustable straps|mesh with lace|black, lavender, white
bodystocking with long sleeves|a high-necked diamond-net bodystocking with long sleeves and a high-cut leg|a plain back, a low scoop at the lower back|none, fully sheer|all skin shows through|stretches to fit, snug|fine net|black, nude, red
lace-up corset with suspenders|a satin corset with a busk front and four suspender straps|a lace-up back with a modesty panel|the ribs, waist and hips|the breasts and the legs|boned, cinched waist, adjustable|satin and lace with steel boning|black, red, ivory
bridal lace teddy|a white lace teddy with a plunging neckline, scalloped edges and a satin bow at the centre|a lace back with a keyhole, a snap crotch|the breasts and torso|the legs, with the sides high-cut|snug, high-cut|stretch lace|white, ivory, blush
satin kimono robe set|a short kimono robe with wide sleeves and an obi-style belt, with a matching slip|a plain satin back with a printed motif|the whole body when closed|the front opens to show the slip|loose, hip-length, wide sleeves|printed satin|floral, black, red
marabou-trimmed babydoll set|a short babydoll with feather trim on the neckline and the hem, an open front with ties at the bust|a plain satin back with a bow, a matching G-string|the bust and midriff when tied|the front is open when untied|loose, flared|satin and marabou feathers|pink, black, white
two-piece garter lingerie set|a lace bralette and matching high-waist garter panty with six suspenders|crossed straps and a lace waistband at the back|the breasts through lace, the hips|the stomach between the bralette and the panty|snug, high-waist|stretch lace|black, burgundy, navy
suspender body harness bodysuit|a mesh bodysuit with an elastic harness overlay across the chest and hips, suspender clips|the harness crosses the back, a thong back|the torso through mesh|everything shows through the mesh|snug, stretchy|mesh and elastic webbing|black, red, white
sheer lace bodysuit with plunging neckline|a deep V neckline to the navel, a lace bodice and a thong-back leg|a scoop-back with a snap crotch|the torso through lace|the breasts and the stomach through lace, the plunge shows skin|snug, stretchy|stretch lace|black, wine, ivory
strappy cage bra set|a bra of crossed elastic straps over a small lace triangle with a matching strappy thong|a crossing strap back, a thong back|the lace triangle and the front of the thong|the sides of the breasts, the hips and the buttocks|adjustable, harness-like|lace and elastic webbing|black, red, lilac
mesh bodystocking with garter prints|a sheer bodystocking with printed illusion garters, a halter neckline|a plain mesh back and a thong seat|none: all sheer|everything shows through|stretches to fit|fine mesh|black, nude, red
cupless lace corset|a lace corset with cups cut away so the breasts are free|a lace-up back with boning|the ribs and waist|the breasts and nipples|boned, cinched waist|lace and steel boning|black, burgundy, ivory
pleated chiffon and lace nightie|a plunging V-neck nightie with a pleated chiffon skirt and lace trim|a low scoop back and a thigh-high hem|the torso lightly through chiffon|the legs, partly sheer|loose and flowing, adjustable straps|chiffon and lace|blush, black, ivory
satin slip with lace insert|a bias-cut satin slip with a lace panel at the bust and hem|a low cowl back with thin straps|the body and thighs|the back is partly bare|slim, flowing|satin and lace|champagne, black, emerald
open-crotch babydoll panty set|a sheer babydoll with a matching panty with an open crotch seam|a sheer flowing back, string panty|the torso through sheer|the genital area|loose flared fit|mesh and lace|black, red, white
lace halter teddy with ring|a halter teddy with a ring at the cleavage, lace cups and a mesh midriff|an open back with a thong cut|the breasts|the back and the buttocks|snug, high-cut|lace and mesh|black, white, red
embroidered garter slip|a short slip with embroidered tulle cups, a satin skirt and four garter straps|a low scoop back, garter clips at the back|the torso and hips|the thighs|slim, flowing|embroidered tulle and satin|black, nude, rose
""")
S['bras'] = P("""
push-up balconette bra|wide-set cups with a deep padded lift and a horizontal neckline|a three-hook closure with a wide band and padded straps|about three-quarters of each breast|the upper edge and the cleavage line|underwire, push-up, rounded lift|lace over moulded foam|black, nude, red
plunge bra with open centre|deep plunging cups with a narrow centre gore, padded cups|a three-hook band and thin straps|the lower outer breast|the cleavage and the inner breast|underwire, low-cut|satin with lace trim|black, burgundy, ivory
open-cup shelf bra|half-cups that only support from below with a scalloped edge|a three-hook back and adjustable straps|the underside of the breasts|the nipples and upper breast|firm underwire shelf|stretch lace|black, red, nude
strapless bra with silicone grip|a strapless bra with moulded cups and silicone at the top edge|a six-hook band with a longline back|the whole breast|the shoulders and upper chest|boned and gripped|smooth microfibre|nude, black, white
T-shirt bra|a smooth moulded full cup with a rounded neckline and no seams|a three-hook back with a wide band|the entire breast|nothing|underwire, seamless|microfibre|nude, black, white
wireless cotton bralette|a pull-on bralette with a scoop neckline and a wide band|a racerback style with wide straps|the whole breast|nothing|soft, wire-free|ribbed cotton|white, grey, sage
lace unlined triangle bralette|soft triangle cups with a plunging V|tie-back strap and a slim band|the breasts through sheer lace|the nipples show through the lace|wire-free, slim|stretch lace|black, burgundy, ivory
longline bralette|a bralette that ends under the ribs, a sweetheart neckline|a hook-and-eye back with boning panels|the breasts and the ribs|nothing|snug longline|lace and satin|black, nude, blush
full-figure support bra|full cups with side support panels and a wide band|a four-hook closure with wide cushioned straps|the entire breast|nothing|underwire, firm support|stretch lace and microfibre|black, nude, red
sports bra with racerback|a high neckline compression bra with a seamless front|a racerback with a Y-shaped strap|the entire breast|nothing|compression, high impact|moisture-wicking knit|black, grey, navy
front-closure bra|a front clasp between smooth cups|a smooth racerback band|the whole breast|nothing|wire-free, smoothing|stretch microfibre|nude, black, white
nursing bra with clips|full cups with fold-down panels at the cup tops|a four-hook closure with a wide band|the entire breast when closed|the breast when the cup is dropped|wire-free soft support|cotton blend jersey|nude, black, white
bandeau bra|a straight strapless tube with no padding|a smooth band|the breasts|the shoulders|elastic, no wires|stretch microfibre|nude, black, white
corset-style bra|a boned bra with a lace-up front and wide straps|a hook-and-eye back with boning|the entire breast|nothing|boned, firm shaping|satin and lace|black, ivory, red
harness bra|a bra of crossing elastic straps over each breast with a front O-ring|a buckle on the back|the straps only|the breasts between the straps|fully adjustable|elastic webbing|black, white, red
halter bra|a halter neck with a triangle cup|a tied or clipped halter and a slim band|the breasts|the shoulders|wire-free, open back|satin and lace|black, white, red
half-cup push-up bra|low cups with a deep lift and a scalloped lace edge|a three-hook band|the lower half of the breasts|the top of the breasts|underwire, high lift|lace and satin|black, red, ivory
bra with mesh sides|solid cups with mesh side panels|a three-hook mesh back|the whole breast|nothing, the side panels are sheer|underwire|microfibre and mesh|black, nude, white
sheer mesh underwire bra|sheer mesh cups with an underwire, only a satin trim|a three-hook closure|the cup edges only|the nipples show through|unlined, underwire|sheer mesh|black, nude, red
satin bustier with suspenders|a boned bustier with satin cups, four suspender straps|a lace-up back|the breasts and the ribs|nothing|boned, shaped|satin|black, ivory, red
stick-on silicone cups|adhesive silicone cups that stick under the breasts|no back|the breasts|nothing|reusable adhesive|silicone|nude, black
pasty bra with tassels|a bra of two nipple covers joined by a thin strap|no back, just a strap|the nipples only|the rest of the breasts|adhesive plus strap|satin with tassels|black, red, gold
embellished crystal bra|cups with rows of crystals and a narrow band|a hook-and-eye back|the entire breast|nothing|underwire|satin and rhinestones|silver, gold, black
cut-out strappy bra|solid cups with circular cut-outs and straps|an X-strap back|the breasts|the skin through the cut-outs|wire-free|satin|black, red, white
longline lace bra|a bra that ends below the bust, scalloped lace, with a plunging neckline|a hook-and-eye back with two rows|the breasts and ribs|nothing|snug|stretch lace|black, ivory, nude
leopard-print unlined bra|unlined cups in a leopard print with a lace edge|a three-hook back|the breasts|nothing|underwire, unlined|stretch mesh with lace|leopard, black
""")
S['panties'] = P("""
slider-side satin thong|a satin thong with a small triangle front and adjustable slider rings on the side straps|a thin T-back with a narrow centre strap|the pubic area|the buttocks|string sides, low rise|satin and elastic|pink, black, red
printed liquid-satin hipster|a mid-rise hipster in glossy satin, a wide waistband and a full-cut leg|a full-coverage back|the hips and the buttocks|nothing|stretchy, high-cut leg|liquid satin|floral print, leopard, black
crotchless rope hipster|a hipster front with a rope accent and a wide waistband, the crotch opens at the centre|a full-coverage seat with a rope tie at the back|the hips and the buttocks|the genital area|snug|liquid satin and rope|crimson, black
pleated chiffon and lace thong|a pleated chiffon triangle trimmed with lace|a lace waistband and string back|the pubic area|the buttocks|low-rise, thin sides|chiffon and lace|blush and black, ivory
embroidered tulle bikini with open back|a low-rise bikini front in embroidered tulle|an open back with only crossing straps|the front only|the buttocks and the genital area|snug|embroidered tulle|black and red
pearl thong|a lace front triangle with pearls|a pearl strand back|the pubic mound|the buttocks and genitals|string-thin|lace and pearls|ivory, black
backless chiffon panty|a high waist with a chiffon front|a bare back with two straps|the front|the buttocks|snug|chiffon|blush, black
leopard-and-lace panty|a mid-rise brief with lace|a full-coverage lace back|the hips and buttocks|nothing|snug|stretch lace|leopard and black
crotchless liquid satin tanga|a tanga with an opening in the crotch seam|a tanga back covering half the buttocks|the hips|the genital area|low-rise|liquid satin|leopard, black
satin tanga|a low-rise tanga with narrow sides|a half-coverage back|the hips|the lower half of the buttocks|snug|satin|leopard, black, red
cotton hipster|a mid-rise hipster with a smooth waistband|a full back|the hips and buttocks|nothing|soft, mid-rise|cotton jersey|white, grey, pink
seamless brief|a no-show brief with laser-cut edges|a full back|the hips and buttocks|nothing|smooth fit|nylon microfibre|nude, black
boyshort with lace back|a plain cotton front with a lace trim at the leg|a lace panel at the back|the hips and buttocks|nothing|mid-thigh leg|cotton and lace|black, white
G-string with chain waist|a narrow triangle front with a chain at the waist|a string back|the pubic area|the buttocks|string-thin|satin and metal chain|black, red
open-back cheeky panty|a mid-rise front|an open lace-up back with straps|the front|the upper buttocks|cheeky fit|lace and satin|black, red
high-waist control brief|a high waist with smoothing front panel|a full back with a lifting seat|the belly, hips and buttocks|nothing|firm control|nylon and spandex|black, nude
mesh thong with ribbon|a sheer mesh front with a ribbon trim|a string back|the pubic area through the mesh|the buttocks|low-rise|mesh|black, white
fishnet brief|a fishnet front with a satin waistband|a fishnet back|the pubic area through the net|the skin through the net|snug|fishnet|black, red
V-string thong|a narrow V-shaped front|a V-shaped string back|the pubic area|the buttocks|string-thin|satin|black, pink
crotchless thong with ties|a thong with ties at the sides, open crotch|a string back|the pubic area|the genital area|adjustable|stretch lace|black, red
high-cut French knickers|a flowing front with a scalloped lace trim|a full back with a wide leg|the hips and buttocks|nothing|loose, wide legs|silk and lace|ivory, black
long-line control short|a mid-thigh short with smoothing panels|a full back|the hips, thighs and buttocks|nothing|firm smoothing|nylon spandex|nude, black
rhinestone G-string|a small triangle with rhinestones|a string back|the pubic area|the buttocks|string-thin|satin and crystals|silver, black
tie-side bikini|a bikini front with ties at the hips|a full back|the front and the buttocks|the hips between the ties|adjustable|satin|black, red, white
lace boyshort set of three|a lace-trimmed boyshort front|a full lace back|the hips and buttocks|nothing|comfortable|stretch lace|black, ivory
sheer tulle thong with bow|a sheer tulle triangle with a bow|a string back|the pubic area through the tulle|the buttocks|low-rise|tulle|black, blush
""")
S['clothing_sleep'] = P("""
bodysuit with plunging neckline|a long-sleeved bodysuit with a plunging V to the navel|a scoop back with a snap crotch|the torso, the arms and the hips|the chest through the plunge|snug, high-cut leg|stretch jersey|black, white, red
lace bodysuit with long sleeves|a high-neck lace bodysuit|a keyhole back with a thong seat|the torso through lace|the skin shows through the lace|snug|stretch lace|black, nude
shaping bodysuit|a smoothing bodysuit with a deep V|a low back with a snap crotch|the torso|nothing|firm shaping|nylon spandex|nude, black
satin bodysuit with ties|a halter bodysuit with a plunging neck and a tie|an open back|the torso|the back|snug|satin|black, red, champagne
corset with lace-up back|a boned corset with a front busk|a lace-up back|the ribs, the waist and hips|the breasts and the legs|boned|satin|black, red
corset dress|a strapless corset dress with a mini skirt|a zip back|the torso and hips|the shoulders|snug waist, short skirt|satin and mesh|black, red
bustier top|a boned bustier with sweetheart cups|a hook-and-eye back|the breasts and ribs|the stomach|snug|satin|black, ivory
slip dress|a bias-cut slip dress with thin straps|a cowl back|the whole body to mid-thigh|the shoulders|slim, flowing|satin|champagne, black
mini skirt with lace hem|a stretchy mini skirt with a lace trim|a back zip|the hips and the buttocks|the legs|short, snug|stretch crepe|black, red
shapewear slip|a smoothing slip with a lace trim|a low back|the torso|the shoulders|firm shaping|nylon|nude, black
cotton sleep set|a button-front top with piped trim and matching shorts|a plain back|the torso and thighs|the legs|relaxed|cotton|pink, grey, navy
satin sleepwear set|a camisole with lace trim and shorts|a smooth back|the torso and hips|the legs|relaxed|satin|champagne, black, emerald
sleep romper|a short romper with a scoop neck|a plain back|the torso and hips|the arms|loose|cotton jersey|pink, grey
satin robe|a knee-length satin robe with a tie belt|a plain back|the body when tied|the front when open|loose|satin|black, red, champagne
plush robe|a long robe with a shawl collar|a hood|the entire body|nothing|loose, long|plush fleece|grey, pink, ivory
long-sleeved sleep shirt|a button-front sleep shirt|a long back|the torso to mid-thigh|the legs|loose|cotton|white, striped
sleep slip|a short slip with a V-neck|a low back|the torso|the legs|loose|satin|black, rose
cami and short set|a lace-trimmed cami with matching short|a smooth back|the torso|the legs|relaxed|modal jersey|black, blush
chemise nightie|a deep V chemise|a low back|the torso to the hip|the legs|loose|chiffon|black, red
terry bathrobe|a belted bathrobe|a hood and plain back|the whole body|nothing|loose|terry cloth|white, grey
sleep dress|a long sleeve nightgown with ruffles|a back button|the whole body|nothing|loose|flannel|pink, plaid
cropped hoodie and shorts set|a cropped hoodie with shorts|a plain back|the torso|the midriff|relaxed|fleece|grey, black
leather-look mini dress|a zip-front mini dress|a back zip|the body to the thigh|the arms|snug|faux leather|black, red
fishnet bodystocking|a net body with a high neck|a net back|nothing|all skin through the net|stretches|fishnet|black
sheer mesh dress|a long sleeve mesh dress|a keyhole back|the body through mesh|all skin through the mesh|snug|mesh|black, nude
""")
S['accessories'] = P("""
rhinestone tassel pasties|two round nipple covers with rhinestone fronts and swinging tassels|an adhesive back that sticks to the skin|the nipples|the rest of the breasts|adhesive, round|satin, rhinestones and fringe|black, gold
star-shaped pasties|two star-shaped adhesive nipple covers|sticky back|the nipples|the rest of the breasts|adhesive|faux leather|black, red
rhinestone V-neck bra|a bra with a V neckline and dangling chains|a hook back|the breasts|nothing|underwire|satin and rhinestones|gold, silver
rhinestone V-front panty|a V-front panty with crystal strands|a string back|the pubic area|the buttocks|low-rise|satin and crystals|gold, silver
X-crossed rhinestone bustier|a bustier with rhinestone crossing straps|a lace-up back|the breasts|nothing|boned|satin|silver, gold
chain harness|a draped chain harness over the shoulders and chest|a buckle back|the chain only|the whole torso|adjustable|faux leather and chain|black, silver
chain garter|a draped chain garter for the thigh|a clasp|the thigh band|the leg|adjustable|metal chain|black, silver
lace-top thigh-high stockings|sheer stockings with a lace welt|a seam up the back|the legs|the skin through the sheer|stay-up grip|sheer nylon|black, red
lace garter belt|a wide lace belt with six suspender straps|a hook back with crossing straps|the waist|the hips|adjustable|lace|black, red
garter belt and thigh-highs set|a narrow belt with four clips|a lace back|the waist and thighs|the hips|adjustable|nylon and lace|black
fishnet thigh-highs|net stockings with a lace top|a back seam|the legs through net|all skin|stay-up|fishnet|black
body chain set|a chain from the neck to the waist with a belly chain|an open back|the chain only|the whole body|adjustable|metal|gold, silver
rhinestone boxchain bra straps|a pair of chain straps|a clip|the straps|nothing|adjustable|chain and crystals|silver
opera gloves|a long glove with a ruched top|a button wrist|the arm|the fingertips|stretchy|satin|black, red, ivory
choker with ring|a velvet choker with a ring|a buckle|the neck|nothing|adjustable|velvet|black, red
thigh-high socks|knitted with a bow|a plain back|the legs|nothing|stretchy|cotton knit|white, black
feather boa|a long feather stole|plain|the shoulders|nothing|draped|marabou|black, pink
leg garter with bow|an elastic band with a bow|plain|the thigh|nothing|stretchy|lace|white, blue
lace mask|a lace eye mask|a tie back|the eyes|the nose and mouth|adjustable|lace|black, red
""")
S['sale'] = P("""
satin gown with monowire cutouts|a floor-length satin gown with a plunging neckline and cutouts at the waist|an open back with ties|the torso and hips through satin|the cutouts and the back|loose skirt, fitted bodice|satin|mauve, burgundy
unlined corset-cup bra|corset-style cups|a hook back|the breasts through mesh|the skin shows through the mesh|underwire|satin and mesh|mauve
corset-cup babydoll|a babydoll with corset cups and a sheer skirt|a flowing back|the torso lightly|the legs|flared|satin and mesh|mauve
corseted plunge teddy|a plunging corseted teddy|a lace-up back|the breasts and torso|the legs|boned|satin|burgundy
crotchless leopard teddy|a leopard mesh teddy with a plunging neckline|a thong back with an open crotch|the torso through mesh|the genital area|snug|leopard mesh|leopard
halter chain teddy|a halter teddy with a chain at the neck|an open back|the torso|the back|snug|liquid satin|black
open underbust bra|a leopard-mesh underwire bra that cups only the lower breasts|a hook back|the underside|the upper breasts|firm|mesh|leopard
chemise and G-string set|a leopard-mesh chemise with underwire cups|a flowing back|the torso through mesh|the legs|loose|mesh|leopard
embroidered babydoll set|a satin babydoll with embroidered lace cups|a ribbon back|the breasts|the midriff|flared|satin and lace|ivory
strappy cutout bra|a bra with straps and cutouts|a hook back|the breasts|the skin through cutouts|underwire|satin|ivory
rhinestone halter bra|a halter bra with rhinestone cups|a tie back|the breasts|the back|wire-free|satin|silver
lace-up bustier|a lace-up front bustier|a zip back|the breasts and ribs|nothing|boned|satin|black, red
silk chemise|a bias-cut silk chemise|a low back|the torso|the legs|loose|silk|ivory, black
fishnet dress|a long sleeve fishnet dress|a keyhole back|none|all skin|snug|fishnet|black
sheer robe|a long sheer robe|an open front|none|all skin|loose|chiffon|black, pink
lace garter slip|a lace garter slip|a low back|the torso|the legs|slim|lace|black
satin teddy with tie|a satin teddy|a tie back|the torso|the legs|snug|satin|red, black
mesh babydoll|a mesh babydoll with lace|a flowing back|the torso lightly|the legs|flared|mesh|pink, black
open-cup bustier|an open-cup bustier|a lace-up back|the ribs|the breasts|boned|satin|black
pearl chemise|a chemise with pearl straps|a low back|the torso|the legs|loose|satin|ivory
velvet babydoll|a velvet babydoll|a ribbon back|the torso|the legs|flared|velvet|burgundy
sheer bodystocking|a sheer bodystocking|a plain back|none|all skin|stretches|mesh|black
corset set with garters|a corset with garters|a lace-up back|the waist|the legs|boned|satin|black
lace halter set|a halter bra and thong|a tie back|the breasts|the back|wire-free|lace|black
leopard-print slip|a leopard satin slip|a low back|the torso|the legs|slim|satin|leopard
""")
