"""Medical wraps (casts, splints, bandages, plasters) as accessories: acc_medwrap_*.
Wound and injury overlay, clinical wording: body_wound_*. Descriptions only, adults only, detached tone."""
import os, re, sys, random, zlib
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from paths import FINAL
def S(x): return [i.strip() for i in x.split(';') if i.strip()]
def R(*k): return random.Random(zlib.crc32('|'.join(map(str, k)).encode()))
CASTCOL = S("white; bright blue; hot pink; black; red; green; purple; orange; yellow; neon green; silver; camouflage-patterned; tie-dyed; teal; grey; striped in two colours; glitter-flecked")
WRAPCOL = S("skin-tone beige; white; navy; black; neon pink; olive; tan; grey; bright red; striped; patterned with small dots; transparent")
WEAR = S("new and clean; grubby at the edges; covered in signatures and drawings; stained with food and dirt; frayed at the ends; wrapped in a plastic cover for the shower; worn smooth after weeks; padded with extra layers; slightly loose; cut open along one side; with toes or fingers visible at the end; decorated with stickers")
CASTS = S("a full-body spica cast from the chest to the ankles; a hip spica cast covering the pelvis and both thighs; a single-leg hip spica cast; a long-arm cast from the knuckles to the upper arm with the elbow bent; a short-arm cast from the knuckles to below the elbow; a thumb spica cast; a long-leg cast from the toes to the upper thigh; a short-leg walking cast with a rubber heel; a cylinder cast covering the full knee; a cast shoe over a toe cast; a fibreglass wrist cast with the fingers free; a clamshell cast split along two sides; a body jacket cast around the torso; a Minerva cast around the neck and chest; a plaster slab on the back of the forearm held by an elastic wrap; a full-arm cast held in a sling; a cast on one arm and one leg; a double-leg cast joined by a bar; a cast with a window cut to access a wound; a walking boot cast with velcro straps; a sugar-tong splint along both sides of the forearm")
SPLINTS = S("a finger splint of aluminium and foam; a mallet-finger splint holding the tip straight; a buddy-taped pair of fingers; a wrist brace with a metal stay; a thumb brace with a rigid shell; a moulded thermoplastic hand splint; an ankle air-cast stirrup brace; a knee brace with hinged side bars; a rigid-collar neck brace; a soft foam cervical collar; a halo brace with a vest and metal ring; a shoulder immobiliser strap; a figure-of-eight clavicle strap; a rib belt around the chest; a back brace with a rigid shell; an elbow hinge brace; a malleable SAM splint moulded around the forearm; a crutch-assist boot splint; a cock-up wrist splint; a foam toe separator with a post-surgery shoe")
SLINGS = S("a triangular cloth sling tied at the neck; a padded sling with a strap and a waist belt; a sling with an abduction pillow; a collar-and-cuff sling; a makeshift sling made from a scarf; a sling with a small supporting bar")
WRAPS = S("an elastic compression bandage wrapped around the ankle in a figure of eight; a gauze roll wrapped around the forearm and fixed with tape; a tubular net bandage over a dressing; a cohesive wrap around the knee; a head bandage wound around the crown and forehead; a bandage wrapped around the whole head covering one ear; a chest wrap around the ribs; a triangular head bandage tied behind; a thick wrap on one hand with fingertips free; a bandage wrapped around the neck; a wrap over the eye held by tape; a layered gauze dressing taped to the scalp; a pressure bandage around the thigh; a stack of padded gauze strapped to the shoulder; kinesiology tape in a fan pattern over the shoulder; kinesiology tape along the calf; white athletic tape around the wrist and thumb; a wrapped foot with a surgical shoe")
PLASTERS = S("a small rectangular adhesive bandage on a fingertip; a fabric-style strip across a knuckle; a large square plaster over the knee; a round spot plaster on the cheek; an adhesive patch on the elbow; a butterfly closure holding a cut together; a waterproof clear plaster on the heel; a hydrocolloid blister plaster on the back of the heel; a fingertip cap bandage; a pair of crossed plasters over a scrape; a pack of plasters in assorted sizes; a strip of paper surgical tape across the eyebrow; a plaster with a patterned print of stripes or stars; a skin-tone plaster that blends in; a bright-coloured novelty plaster; a plaster peeling off at one corner; a soaked plaster fraying at the edges; a dressing pad held with hypoallergenic tape; a transparent film dressing over a stitched cut; an eye patch held by an elastic band; an eye shield taped over the eye")
def medwrap():
    G = {}
    G['acc_medwrap_cast'] = sorted({f"{c}, in {R('c', c, k).choice(CASTCOL)}, {R('cw', c, k).choice(WEAR)}" for c in CASTS for k in range(8)})
    G['acc_medwrap_splint'] = sorted({f"{c}, {R('s', c, k).choice(WRAPCOL)}, {R('sw', c, k).choice(WEAR)}" for c in SPLINTS for k in range(6)})
    G['acc_medwrap_sling'] = sorted({f"{c}, in {R('sl', c, k).choice(WRAPCOL)}, {R('slw', c, k).choice(WEAR)}" for c in SLINGS for k in range(6)})
    G['acc_medwrap_bandage'] = sorted({f"{c}, in {R('b', c, k).choice(WRAPCOL)}, {R('bw', c, k).choice(WEAR)}" for c in WRAPS for k in range(6)})
    G['acc_medwrap_plaster'] = sorted({f"{c}, {R('p', c, k).choice(WEAR)}" for c in PLASTERS for k in range(6)})
    G['acc_medwrap_colour_cast'] = CASTCOL; G['acc_medwrap_colour_wrap'] = WRAPCOL; G['acc_medwrap_wear'] = WEAR
    G['acc_medwrap_prompt'] = ['__acc_medwrap_cast__.', '__acc_medwrap_splint__.', '__acc_medwrap_sling__.', '__acc_medwrap_bandage__.', '__acc_medwrap_plaster__.']
    return G
# ---------------------------------------------------------- wounds: catalogue x site x stage (see injury_data.py)
import injury_data as D
NOUN = {'gen': 'injury', 'bite': 'injury', 'fracture': 'injury', 'burn': 'burn', 'contagion': 'condition'}

def S2(x): return [i.strip() for i in x.split(';') if i.strip()]
DETAIL = {  # category -> pools of descriptive clauses (edges, colour, surrounding skin, extras)
 'minor': dict(edge=S2("the edges are clean and sharply defined; the edges are slightly ragged; the edges are red and slightly raised; the margin is faintly pink"), col=S2("bright red at the centre fading to pink; pale pink with a thin dark line; red with a yellowish crust forming; reddish-purple with a yellow rim"), around=S2("the surrounding skin is intact and slightly warm; the surrounding skin is mildly swollen; the skin around it is dry and flaking; the skin around it is unmarked")),
 'bite_sting': dict(edge=S2("each mark has a distinct round edge; the wound edges are torn and uneven; the edges are swollen and shiny; the margin is crisp with a clear red halo"), col=S2("red centre, pale ring, wider red halo; purple-red with yellow-green bruising at the margin; dark blue-black at the puncture points; hot pink with raised white wheals"), around=S2("the skin around is swollen, tight and warm; the surrounding tissue is bruised in a wide arc; small red streaks lead away from the site; blanched pale skin sits just inside the red zone")),
 'puncture': dict(edge=S2("the entry edge is small and round with a thin dark rim; the edge is inverted and neat; the exit edge is everted and irregular; the edges are pale and bruised"), col=S2("dark red with black dried blood around the edge; blue-purple around the rim and yellow further out; grey-white at the centre of the track; deep maroon at the centre"), around=S2("the surrounding skin is bruised in a ring; the area around the wound is swollen and tense; clothing near the site is soaked with blood; the surrounding tissue is warm to touch")),
 'laceration': dict(edge=S2("the edges are clean and sharply cut; the edges are jagged with small flaps; the edges are bruised and crushed; the edges are gaping about 1 cm apart; the edges lie neatly together"), col=S2("bright red blood in the depths with pale yellow fat at the base; dark red clotted blood along the edges; pink granulation tissue in the floor; white tendon or fascia visible at the base"), around=S2("the skin around is bruised blue-purple; the skin around is swollen and shiny; the surrounding skin is smeared with dried blood; the skin around the wound is clean and pale")),
 'bruise_sprain': dict(edge=S2("the bruise has a diffuse irregular edge; the swelling has a smooth rounded outline; the bruising has a sharp straight edge; the swelling spreads down the limb"), col=S2("fresh red-purple; deep blue-black; green and yellow at the older edge; brown and yellow in the late stage; purple at the centre with a yellow halo"), around=S2("the skin is tight and shiny over the swelling; the surrounding skin is warm; the swelling pits slightly when pressed; the joint looks puffy and rounded")),
 'fracture': dict(edge=S2("the limb is angled at an abnormal point; the contour is swollen and straightened; there is a visible step in the bone line; the limb is shortened and rotated"), col=S2("the skin over the break is red and then purple-blue; extensive bruising spreads down the limb; the skin is pale and taut over the break; yellow-green bruising marks the older break"), around=S2("the surrounding tissue is hot and swollen; the fingers or toes beyond the break are pale and cool; the skin is stretched and shiny; the limb is supported on a pillow or rigid support")),
 'burn': dict(edge=S2("the border is sharply defined; the edge is irregular with a splash pattern; the border is red with a pale inner ring; the margin is ragged where blisters have burst"), col=S2("bright red and blanching on pressure; white and waxy; mottled red, white and brown; charred black and brown with a leathery texture; shiny pink and moist; pale grey and dry"), around=S2("the skin around is red and swollen; clear fluid weeps from burst blisters; the surrounding skin is peeling in thin sheets; singed hair marks the border")),
 'contagion': dict(edge=S2("the lesions have a defined round border; the patches have raised scaly edges; the spots are scattered with clear skin between them; the lesions merge into larger plaques"), col=S2("pink to red against the natural skin tone; dark brown to purple on deeper skin tones; pale grey-white at the centre; yellow with honey-coloured crust; red with white pustule tops"), around=S2("the skin around is dry and itchy with scratch marks; nearby lymph nodes are visibly swollen; the surrounding skin is warm; the person appears flushed or pale")),
 'head_face': dict(edge=S2("the swelling is rounded and tight; the cut edges lie close together; the eyelid is swollen and shut; the margin of the bruise is sharply outlined"), col=S2("dark purple around the eye fading to green; red and swollen with pale centre; blue-black over bone; yellow-green around the older bruise"), around=S2("the skin of the face is puffy and asymmetric; hair around the wound is matted with blood; clear fluid or blood runs from the nose or ear; the eye is bloodshot")),
 'amputation': dict(edge=S2("the stump end is clean-cut with exposed bone surfaces; the end is rounded and padded; the tissue is torn and ragged at the margin; the skin edge is neatly closed over the end"), col=S2("white bone, red muscle and yellow fat at the cut surface; pink healed scar over the end; pale grey stump skin with a darker scar line; bright red bleeding controlled by pressure"), around=S2("a tourniquet is tightened above the injury; the dressing is soaked with blood; the remaining limb is pale and cool; a prosthetic socket liner sits on the stump")),
}
HEALED = dict(edge=S2("the mark is smooth and flat; the scar line is thin and slightly raised; the area is slightly depressed against the skin around; the border is faintly puckered"), col=S2("paler than the natural skin tone; slightly darker than the natural skin tone; pink fading to silver; shiny and tight; matching the surrounding skin closely"), around=S2("the surrounding skin is calm and unmarked; the skin around it is dry and slightly tight; no swelling remains; the area is slightly numb to light touch"))
FRACT_FACE = dict(edge=S2("the contour of the bone is flattened or uneven; the swelling is rounded and tight; the bone line shows a small step; the features look asymmetric"), col=S2("purple-blue bruising spreading outwards; yellow-green bruising at the older margin; red and swollen over the site; pale and taut over the bone"), around=S2("the surrounding tissue is hot and swollen; the eye or lip on that side is puffy; dried blood sits in the nostril or the corner of the mouth; the skin is tight and shiny"))
FRACT_TRUNK = dict(edge=S2("the chest or back contour is slightly uneven; the area is guarded and held still; the bone line cannot be seen through the swelling; the posture is stiff"), col=S2("deep purple bruising spreading across the skin; yellow-green bruising at the older margin; red and swollen over the site"), around=S2("the surrounding tissue is tender and swollen; breathing is shallow and guarded; the skin is warm over the injury; clothing is cut away to show the area"))
def wounds():
    G = {}; tiers = {}; cats = {}
    for cat, tier, name, region, tpl, st in D.C:
        locs = D.LOC[region]
        stages = D.STAGE[st]
        if st == 'fracture' and not region.startswith('bone_'): stages = [x for x in stages if not re.search('sling|cast|traction|external frame|splint', x)]
        if 'healed' in name: stages = ['healed, with a closed scar', 'healed, and settled into everyday use', 'long healed, with a pale mature scar']
        elif region == 'side': stages = [x for x in stages if 'infected' not in x and 'scab' not in x and 'leaving' not in x][:8]
        for loc in locs:
            for sg in stages:
                if R('w', name, loc, sg).random() < (1.0 if region == 'side' else min(1.0, 9.0 / (len(locs) * len(stages)) * 1.6)):
                    dd = DETAIL.get(cat, DETAIL['minor'])
                    if st == 'fracture' and not region.startswith('bone_'): dd = FRACT_FACE if region in ('face', 'head') else FRACT_TRUNK
                    if 'healed' in sg or 'leaving' in sg or 'long healed' in sg: dd = HEALED
                    rr = R('d', name, loc, sg)
                    line = f"{name}: {tpl.format(l=loc)}; the {NOUN[st]} is {sg}. Appearance: {rr.choice(dd['col'])}; {rr.choice(dd['edge'])}; {rr.choice(dd['around'])}."
                    tiers.setdefault(tier, []).append(line); cats.setdefault(cat, []).append(line)
    for t, l in tiers.items(): G[f'body_wound_{t}'] = sorted(set(l))
    for c, l in cats.items(): G[f'body_wound_cat_{c}'] = sorted(set(l))
    G['body_wound_site_arm'] = D.LOC['arm']; G['body_wound_site_leg'] = D.LOC['leg']; G['body_wound_site_head'] = D.LOC['head']; G['body_wound_site_torso'] = D.LOC['torso']
    G['body_wound_stage'] = D.STAGE['gen']; G['body_wound_stage_fracture'] = D.STAGE['fracture']; G['body_wound_stage_burn'] = D.STAGE['burn']; G['body_wound_stage_contagion'] = D.STAGE['contagion']
    G['body_wound_any'] = [f'__body_wound_{t}__' for t in ('minor', 'moderate', 'severe', 'critical')]
    G['body_wound_cat_any'] = [f'__body_wound_cat_{c}__' for c in cats]
    G['body_wound_prompt'] = ['Injury: __body_wound_minor__', 'Injury: __body_wound_moderate__', 'Injury: __body_wound_severe__', 'Injury: __body_wound_critical__', 'Injury: __body_wound_cat_any__', 'Dressing: __acc_medwrap_prompt__']
    return G
def mk():
    G = medwrap(); G.update(wounds()); return G
def build(): return mk()
def run(final):
    G = build()
    for n, l in G.items():
        assert l and all(l) and not any(c in x for x in l for c in '{}|'), n
        open(os.path.join(final, n + '.txt'), 'w', encoding='utf8', newline='\n').write('\n'.join(dict.fromkeys(l)) + '\n')
    print('injury/wraps:', len(G), 'files'); return G
def export_aoo(out, prefix='aoo_'):
    G = build(); nm = set(G); ref = re.compile(r'__([A-Za-z0-9_\-/]+)__'); n = 0
    for name, lines in G.items():
        keep = list(dict.fromkeys(ref.sub(lambda m: '__' + prefix + m.group(1) + '__' if m.group(1) in nm else m.group(0), l) for l in lines))
        if not name.endswith('prompt') and name != 'body_wound_any': random.Random(zlib.crc32(name.encode())).shuffle(keep)
        open(os.path.join(out, prefix + name + '.txt'), 'w', encoding='utf8', newline='\n').write('\n'.join(keep) + '\n'); n += 1
    return n
if __name__ == '__main__':
    a = [x for x in sys.argv[1:] if os.path.isdir(x)]; run(os.path.abspath(a[0]) if a else FINAL)
