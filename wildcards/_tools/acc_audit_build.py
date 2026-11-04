"""v39 accessory audit: removes body-part words that leaked in from the shoe pools into other families (e.g. 'across the ankle' on a scarf) by swapping in a part that the item really has. Post-processes acc_<family>_* files in place."""
import os, re, sys, glob
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from paths import FINAL
FIX = {
 'glove': ('wrist', 'cuff'), 'fan': ('edge of the fan', 'fan'), 'handkerchief': ('border', 'hem'),
 'necktie': ("tie's blade", 'blade'), 'scarf': ('end of the scarf', 'end'),
}
DET = {
 'apron': "It ties at the waist with long straps and hangs in front of the body, covering the chest or hips and sitting over the clothes; the edges are hemmed and a pocket is sewn across the front.",
 'belt': "It is a long strap that circles the waist, closed with a buckle or clasp at the front and threaded through the loops of the clothes.",
 'bodyjewel': "It is a piece of jewellery worn on the body rather than the ears or fingers, joined with small clasps and sitting lightly against the skin.",
 'brooch': "It has a decorative face a few centimetres across and a pin on the back with a safety catch, so it fastens to the cloth of a garment.",
 'charm': "It is a small ornament about the size of a thumbnail, with a tiny loop at the top so that it hangs from a chain, bracelet or clasp.",
 'cigcase': "It is a slim, flat, hinged case that fits in a pocket, with a snap closure and a spring or elastic band inside to hold the contents in place.",
 'contact': "They are thin, curved, soft lenses that rest directly on the surface of the eye, covering the coloured part and showing the pattern from the front.",
 'cufflink': "It is a small decorated face joined by a short post or chain to a toggle that turns flat behind the cuff, fastening the two sides of a shirt cuff.",
 'earring': "It hangs from the ear lobe on a small hook, post or hoop, with the decorative part sitting just below or against the lobe.",
 'fan': "It is held in one hand and moved back and forth in front of the face; it has a grip at the base and a flat surface that moves the air.",
 'glove': "It covers the hand, reaching to the wrist or beyond, and fits close to the hand.",
 'hairpiece': "It sits in or on the hair and is held with a clip, comb, pin or band, so that it stays above or against the hair without slipping.",
 'handkerchief': "It is a square of cloth with hemmed edges, folded into the pocket, held in the hand or tied; the corners and border are finished with a narrow hem.",
 'keychain': "It is a small decorated tag or figure fastened to a split ring, hanging from the ring with the keys.",
 'lanyard': "It is a loop of cord or strap that goes around the neck or wrist and ends in a small metal clip, holding keys or a card.",
 'lighter': "It is a pocket-sized case that holds fuel and a small striker, producing a flame when a thumb flicks the wheel or presses the button.",
 'necktie': "It is a long strip of cloth that hangs down the front of the shirt, with a wide blade at the front and a narrower tail behind, joined by a knot at the collar.",
 'pouch': "It is a small bag closed with a drawstring, flap or zip, carried by a strap, cord or loop, and sized to hold a few small items.",
 'scarf': "It is a long strip of cloth worn round the neck or shoulders, with finished ends and a soft drape.",
 'tights': "They are a single stretch garment that covers each leg from the waist down and fits close to the skin with a snug waistband.",
 'umbrella': "It has a round canopy of cloth stretched over a folding frame of ribs, held up by a central shaft with a handle for the hand.",
 'watch': "It is worn on the wrist, with a round or rectangular face on top and a strap or bracelet that fastens round the wrist with a buckle or clasp.",
}
THIN = 9
def thicken(folder, prefix=''):
    import zlib; n = 0
    for fam, add in DET.items():
        for f in glob.glob(os.path.join(folder, f'{prefix}acc_{fam}_cluster_odd_*.txt')):
            out = []; ch = False
            for l in open(f, encoding='utf8').read().split('\n'):
                if l and '. ' in l and len(l.split('. ', 1)[1].split()) < THIN and add not in l:
                    l = l.rstrip() + ' ' + add; ch = True
                out.append(l)
            if ch: open(f, 'w', encoding='utf8', newline='\n').write('\n'.join(out)); n += 1
    return n
def fix(folder, prefix=''):
    n = 0
    for fam, (place, _) in FIX.items():
        for f in glob.glob(os.path.join(folder, f'{prefix}acc_{fam}_*.txt')):
            t = open(f, encoding='utf8').read()
            u = re.sub(r'\b(across|at|around|along|on|over) the ankles?\b', lambda m: f'{m.group(1)} the {place}', t)
            u = re.sub(r'\bankles?\b', place, u)
            if u != t: open(f, 'w', encoding='utf8', newline='\n').write(u); n += 1
    return n
def run(final): n = fix(final); m = thicken(final); print('accessory audit: fixed', n, 'files, extended', m); return n
def export_aoo(out, prefix='aoo_'): fix(out, prefix); thicken(out, prefix); return 0
if __name__ == '__main__':
    a = [x for x in sys.argv[1:] if os.path.isdir(x)]; run(os.path.abspath(a[0]) if a else FINAL)
