"""Collars (neck collars in the leather and bondage sense, dog-collar sense, decorative and posture collars) and mouth gags / mouth-opening devices as ACCESSORIES: acc_collar*, acc_gag*. Object descriptions only."""
import os, re, sys, random, zlib
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from paths import FINAL
def S(x): return [i.strip() for i in x.split(';') if i.strip()]
COLLAR = S("wide leather collar with a front D-ring and a buckle closure; slim leather day collar with a small ring; locking leather collar with a padlock and hasp; posture collar, a tall stiff leather band that keeps the head up; steel collar with a hinge and a lock; stainless-steel choker with a front ring; velvet choker with a ring; satin ribbon collar with a bow; lace choker with a pendant; studded leather collar with rows of metal studs; spiked leather collar with sharp-looking cones; bell collar with a small jingle bell; ID-tag dog collar in nylon with a quick-release buckle; leather dog collar with a brass nameplate and a leash ring; rhinestone-studded collar with a front charm; chain collar with a small padlock; double-ring collar with rings at the sides; rolled-leather collar with a ring; neoprene collar with a zip; padded collar with a soft lining; rope collar with a knot; riveted leather collar with a gold buckle; wide Gothic collar with metal spikes; reflective nylon collar with a plastic clip; martingale-style collar with a limited-slip loop; harness collar linked to a chest strap; collar with a detachable lead; ornate jewelled ceremonial collar; engraved metal torc collar; collar and leash set with a matching handle; sub-style leather collar with a small lock charm; locking silicone collar with a hidden clasp; cat-bell choker with a heart tag; breakaway collar with a safety buckle; full-length leather neck corset with lacing; braided leather collar with a rope ring; rubber collar with a smooth finish; studded dog-style collar with a name tag; spiked gladiator collar")
GAG = S("ball gag with a rubber ball and a buckled leather strap; silicone ball gag with an adjustable strap; breathable perforated ball gag; bit gag, a horizontal bar held between the teeth by cheek straps; leather bit gag with a steel bar; ring gag, an open metal ring that holds the mouth open; spider gag, a metal frame with arms that hold the mouth open; open-mouth gag with a rubber ring and straps; dental mouth opener, a clinical retractor that keeps the lips and jaw apart; cheek retractor, a flexible plastic frame holding the lips open; dental mouth prop, a rubber block that props the jaw open; steel mouth speculum with a screw adjust; inflatable gag with a pump and a bulb; muzzle-style gag with straps over the nose and jaw; leather muzzle with a mesh front; cleave gag, a strip of cloth tied across the mouth; padded gag with a soft cloth wad; harness gag with a head and chin strap; penetration-free open gag in clear acrylic; ring-and-strap open-mouth gag; whiffle gag, a perforated hollow ball; bridle-style gag with cheek straps; bite-block gag with a hard rubber block; locking buckle gag; spiked-look decorative gag in silicone; clown-nose-and-gag set; clear silicone gag with straps; padded leather gag with a zip mouth; neoprene gag mask; hood with a ball-gag mount; ornamental ball gag in polished wood")
CMAT = S("black leather; brown leather; patent leather; stainless steel; chrome-plated steel; brass; silicone; neoprene; velvet; nylon webbing; rope; satin; rubber; lace; braided leather; leather with metal studs; clear acrylic; hard plastic; polished wood; reflective nylon")
FEAT = S("a front O-ring; a D-ring at the front; a locking padlock; a quick-release buckle; a hasp lock; a brass buckle; a small bell; a name tag; rhinestones; metal studs; pyramid studs; spikes; rivets; a padded lining; a velvet lining; double stitching; engraved scrollwork; a detachable leash; a lacing at the back; a Velcro closure; a silicone coating; reflective stitching; a satin ribbon; a decorative charm")
def build():
    G = {}
    for nm, items, tail in (('collar', COLLAR, 'collar'), ('gag', GAG, 'gag')):
        out = []
        for t in items:
            for i in range(8):
                R = random.Random(zlib.crc32(f'{t}{i}'.encode()))
                mt = '' if any(w in t.lower() for w in ('leather', 'steel', 'velvet', 'satin', 'silicone', 'neoprene', 'nylon', 'rope', 'lace', 'rubber', 'acrylic', 'wood', 'metal', 'brass')) else f', in {R.choice(CMAT)}'
                out.append(f"{t.capitalize()}{mt}, with {R.choice(FEAT)} and {R.choice(FEAT)}.")
        G[f'acc_{nm}'] = sorted(set(out)); G[f'acc_{nm}_type'] = items
    G['acc_collar_material'] = CMAT; G['acc_collar_feature'] = FEAT; G['acc_gag_material'] = CMAT
    G['acc_collar_prompt'] = ['__acc_collar__', 'A __acc_collar_type__ made of __acc_collar_material__.']
    G['acc_gag_prompt'] = ['__acc_gag__', 'A __acc_gag_type__ with __acc_collar_feature__.']
    return G
def run(final):
    G = build()
    for n, l in G.items(): open(os.path.join(final, n + '.txt'), 'w', encoding='utf8', newline='\n').write('\n'.join(l) + '\n')
    print('collars and gags:', len(G), 'files'); return G
def export_aoo(out, prefix='aoo_'):
    G = build(); names_ = set(G); ref = re.compile(r'__([A-Za-z0-9_\-/]+)__'); n = 0
    for name, lines in G.items():
        keep = list(dict.fromkeys(ref.sub(lambda m: '__' + prefix + m.group(1) + '__' if m.group(1) in names_ else m.group(0), l) for l in lines))
        if not name.endswith('prompt'): random.Random(zlib.crc32(name.encode())).shuffle(keep)
        open(os.path.join(out, prefix + name + '.txt'), 'w', encoding='utf8', newline='\n').write('\n'.join(keep) + '\n'); n += 1
    return n
if __name__ == '__main__':
    a = [x for x in sys.argv[1:] if os.path.isdir(x)]; run(os.path.abspath(a[0]) if a else FINAL)
