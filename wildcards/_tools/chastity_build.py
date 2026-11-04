"""Chastity belts and chastity devices as ACCESSORIES (acc_chastity*): historic through modern. Object descriptions only: form, parts, materials, finish, closures, comfort and condition."""
import os, re, sys, random, zlib
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from paths import FINAL
def S(x): return [i.strip() for i in x.split(';') if i.strip()]
def R(*k): return random.Random(zlib.crc32('|'.join(map(str, k)).encode()))
# class -> (types, forms: how the device is built, part pools)
BELT = S("a medieval-style chastity belt; a Renaissance-style engraved chastity belt; a Victorian-style chastity belt; a modern stainless-steel chastity belt; a titanium chastity belt; a lightweight silicone-coated chastity belt; a leather chastity belt; a chain-and-strap chastity belt; a museum-piece chastity belt; a novelty chastity belt; a discreet under-clothing chastity belt; a ceremonial jewelled chastity belt; a fabric-and-steel chastity belt; a locking mesh chastity belt; a thigh-strap chastity belt; a minimalist band-and-shield chastity belt")
CAGE = S("a short steel chastity cage with a slim base ring; a tube-style chastity device with a curved tube and a separate base ring; a clear polycarbonate chastity cage; a silicone chastity cage; a ventilated chastity cage with open bars; a titanium chastity cage with a hinged ring; a closed-tube chastity device with a hole at the tip; a two-piece chastity cage with a lock at the base; a micro chastity cage; a long curved chastity cage; a chastity cage with a spiked-looking but blunt inner shield; a resin chastity cage; a chastity cage with a hinged back plate; a brass chastity cage with a patina; a gold-plated chastity cage; a locking ring chastity device with a short cage")
SHIELD = S("a rigid chastity shield on a waist band; a curved chastity plate with a locked hip strap; a chastity panty with a steel panel; a chastity brief with a locking panel; a bra-style chastity cup set with locks; a chastity harness of straps and rings; a chastity thong with a steel mesh pouch; a chastity girdle with a locking zip; a belt with a detachable crotch strap; a locking chain harness")

WHAT = {
 # belts
 "a medieval-style chastity belt": "a rigid metal belt: a flat iron band that encircles the waist, with a curved plate that hangs from the front of the band, passes down between the legs and fastens to the band at the back, leaving small slots for hygiene",
 "a Renaissance-style engraved chastity belt": "a hinged metal waist band decorated with engraved panels, with a shaped plate that runs from the front of the band between the legs to the back and locks to the band, leaving narrow openings",
 "a Victorian-style chastity belt": "a padded waist band with a narrow metal strap that runs from the front of the band between the legs to the back, closed by a small lock at the back, with cloth lining against the skin",
 "a modern stainless-steel chastity belt": "a slim hinged stainless-steel waist band with a thin curved front shield and a short rear strap that clip together at the back with a lock, with smooth rounded edges",
 "a titanium chastity belt": "a very light waist band of titanium with a curved front plate and a rear strap, closed with a lock at the back and finished smooth",
 "a lightweight silicone-coated chastity belt": "a flexible belt with a thin metal core covered in soft silicone, a front panel that curves between the legs and a back strap that locks to the waist band",
 "a leather chastity belt": "a wide leather waist band with a leather strap that passes from the front between the legs to the back, fastened by buckles and a small lock",
 "a chain-and-strap chastity belt": "a waist loop made of metal chain, with a strap that hangs from the front of the chain, runs between the legs and attaches at the back, held with a padlock",
 "a museum-piece chastity belt": "an antique iron waist band with a curved plate and rear hinge, heavily marked by age, with a large old-fashioned keyhole",
 "a novelty chastity belt": "a playful belt with a cheap plated waist band and a thin front panel with a decorative shape, and a small toy lock",
 "a discreet under-clothing chastity belt": "a thin, flat belt with a low-profile front shield and a narrow rear strap, designed to lie flat beneath ordinary clothing, with a small hidden lock",
 "a ceremonial jewelled chastity belt": "a decorative belt with a waist band set with coloured stones and a shaped front plate that curves between the legs, fastened with an ornate lock",
 "a fabric-and-steel chastity belt": "a soft fabric belt with a steel front shield sewn into it and a rear strap that locks to the waist band",
 "a locking mesh chastity belt": "a waist band with a front panel of steel mesh that curves between the legs and a rear strap, fastened by a lock at the back",
 "a thigh-strap chastity belt": "a waist band and a front shield held in place by two leg straps that wrap the tops of the thighs and fasten with small locks",
 "a minimalist band-and-shield chastity belt": "a narrow waist band joined to a small front shield by a hinge, with a thin strap to the back, closed with a tiny lock",
 # cages
 "a short steel chastity cage with a slim base ring": "a small steel enclosure of narrow bars that fits over the penis, held by a slim ring that fits around the base, with the two parts joined by a small lock",
 "a tube-style chastity device with a curved tube and a separate base ring": "a hollow curved tube that slides over the penis, clipped to a separate ring that fits around the base, with a small lock holding the two together",
 "a clear polycarbonate chastity cage": "a see-through plastic cage with vertical slots that fits over the penis, with a ring around the base and a small lock",
 "a silicone chastity cage": "a soft, flexible silicone cage with slots that fits over the penis, with a rubbery ring around the base and a lock",
 "a ventilated chastity cage with open bars": "a cage made from several widely spaced metal bars that curve to form an enclosure over the penis, with a base ring and a lock",
 "a titanium chastity cage with a hinged ring": "a light titanium cage with a ring around the base that opens on a hinge and closes with a lock",
 "a closed-tube chastity device with a hole at the tip": "a closed tube that fully encloses the penis, with a small opening at the tip, joined to a ring at the base with a lock",
 "a two-piece chastity cage with a lock at the base": "a cage in two separate sections, a ring and a cover, that join together at the base around a lock",
 "a micro chastity cage": "a very small, short cage that tightly encloses the penis, held by a ring at the base",
 "a long curved chastity cage": "a long cage that curves downward, made of bars or a tube, held by a ring at the base with a lock",
 "a chastity cage with a spiked-looking but blunt inner shield": "a cage with an inner shield covered in rows of blunt, rounded ridges that face the skin, joined to a ring with a lock",
 "a resin chastity cage": "a cage cast from hard coloured resin with slots in the sides, fitted with a ring and a lock",
 "a chastity cage with a hinged back plate": "a cage whose back plate swings open on a hinge to fit around the body and closes with a lock",
 "a brass chastity cage with a patina": "a brass cage with a base ring and a lock, darkened and spotted with age",
 "a gold-plated chastity cage": "a cage with a base ring and a lock, covered in a thin layer of gold-coloured plating",
 "a locking ring chastity device with a short cage": "a ring that closes around the base with a lock, fitted with a short bar cage over the penis",
 # shields and harnesses
 "a rigid chastity shield on a waist band": "a stiff curved plate fixed to a waist band and sitting over the groin, with a lock at the band",
 "a curved chastity plate with a locked hip strap": "a curved plate held against the groin by a strap that goes around each hip and locks",
 "a chastity panty with a steel panel": "an underwear-style garment with a steel plate sewn in over the groin and a lock at the waist",
 "a chastity brief with a locking panel": "a brief with a stiff front panel that locks at the waistband",
 "a bra-style chastity cup set with locks": "a pair of rigid cups joined by straps like a brassiere, closed at the back with a lock",
 "a chastity harness of straps and rings": "a harness of narrow straps joined by metal rings that crosses the hips and groin, closed with small locks",
 "a chastity thong with a steel mesh pouch": "a thong-style garment with a steel mesh pouch at the front and a lock at the waistband",
 "a chastity girdle with a locking zip": "a stretch girdle covering the hips and lower body, with a zip fastener secured by a small lock",
 "a belt with a detachable crotch strap": "a waist belt with a separate strap that clips to the front and back, fastened by a small padlock",
 "a locking chain harness": "a harness of metal chain links that circle the waist and pass between the legs, secured with a padlock",
}
ALL = {'belt': BELT, 'cage': CAGE, 'shield': SHIELD}
MAT = S("polished stainless steel; brushed stainless steel; blackened iron; titanium; medical-grade silicone; vegetable-tanned leather; black leather; clear polycarbonate; cast resin; brass with a patina; velvet-lined steel; nylon webbing; gilded metal; hammered bronze; anodised aluminium; carbon-fibre-patterned composite; enamelled steel; chrome-plated steel; rubber-coated steel; blued steel")
FINISH = S("a mirror polish; a satin brushed finish; a matte black coating; an antique patina; a hammered texture; an engraved scrollwork border; an etched floral design; a gilded edge; a coloured anodised surface; a worn, rubbed-smooth finish; a lightly rusted surface; a glossy lacquer; an enamel inlay; a laser-etched pattern; a stamped serial number")
LOCK = S("a small brass padlock; a numbered disc lock; a combination lock; a tamper-proof screw lock; a magnetic lock; a barrel lock with a key; a plastic numbered security tag lock; a keyed cylinder lock; a hinged hasp with a loop for a padlock; a decorative key on a ribbon; a spring latch with a pin; a pair of locking screws; an old iron lock with a long key; a concealed lock under a cover plate")
COMFORT = S("rounded, polished edges; a soft leather lining; a velvet lining; a silicone edge liner; foam padding along the waist band; ventilation openings; drainage slots; a curved profile that follows the hip; a smooth inner surface; a flexible hinge at the waist band; an adjustable length; a removable washable pad; a wide waist band that spreads pressure; a narrow band that sits low on the hips; a breathable mesh inner layer")
STRUCT = {
 'belt': S("a waist band of {m} fastened at the back; a hinged waist band of {m} that closes with a lock; a flat waist band with a front shield of {m} and a narrow rear strap; a curved front plate of {m} attached to a waist band by hinges; a chain waist loop with a front shield of {m}; a leather waist strap with a plate of {m}; a rigid hoop waist band with a curved plate; a band of {m} with a perforated front panel; an adjustable band on slots and pins"),
 'cage': S("a base ring of {m} and a cage of narrow bars; a base ring of {m} with a hinged cage; a curved tube of {m} with a locking ring; a short cage of {m} with open slots; a clear shell with ventilation holes; a ring of {m} with a one-piece tube; a spring-hinged ring that snaps around the base; a cage with a rounded tip opening; a smooth tube with a removable base ring"),
 'shield': S("a panel of {m} with elastic leg openings; a mesh of {m} set into a fabric panel; a locking zip on a rigid panel of {m}; a set of rings and straps of {m}; a plate of {m} sewn into a brief; a chain of {m} linking rings at the hips; a locking buckle of {m} on each strap; a wide girdle band with a hinge"),
}
ERA = S("historic; medieval-style; Renaissance-style; Victorian-style; Edwardian-style; mid-century; modern; ultra-modern; lightweight; ornate; novelty; museum-piece; discreet; ceremonial; handmade; workshop-made; mass-produced; custom-fitted")
COND = S("new; polished; gently worn; scratched from use; antique; restored; unused in its box; lightly tarnished; heavily patinated; well-maintained")
def build():
    G = {}; out = []; types = []
    for cl, ts in ALL.items():
        for t in ts:
            types.append(t)
            for i in range(14):
                r = R('c', cl, t, i)
                m = r.choice(MAT); st = r.choice(STRUCT[cl]).format(m=m)
                parts = [(t[0].upper() + t[1:] if not t.startswith('a ') else 'A' + t[1:]) + ': ' + WHAT[t], (f"It is made mainly of {m}" if not re.search(r'steel|titanium|silicone|leather|polycarbonate|resin|brass|gold|iron|fabric|mesh|chain|jewelled|museum|antique|belt with', t) else f"It carries {r.choice(['no extra coating', 'a protective coating', 'a plain, unadorned surface'])}"), (f"The surface has {r.choice(FINISH)}" if not re.search(r'museum|patina', t) else "The surface shows its age"), f"It closes with {r.choice(LOCK)}", f"For comfort it has {r.choice(COMFORT)}"]
                pass
                out.append('. '.join(parts) + '.')
    G['acc_chastity'] = sorted(set(out))
    G['acc_chastity_type'] = types; G['acc_chastity_material'] = MAT; G['acc_chastity_finish'] = FINISH
    G['acc_chastity_lock'] = LOCK; G['acc_chastity_comfort'] = COMFORT; G['acc_chastity_era'] = ERA; G['acc_chastity_condition'] = COND
    G['acc_chastity_feature'] = FINISH + LOCK + COMFORT
    for cl in ALL: G[f'acc_chastity_{cl}'] = sorted({l for l in out if any(l.startswith(f"{R('x').choice(['a'])}") for _ in [0])} ) if False else [l for l in out if any(t[2:] in l[:90] for t in ALL[cl])]
    G['acc_chastity_prompt'] = ['__acc_chastity__', 'A __acc_chastity_type__ made of __acc_chastity_material__, with __acc_chastity_finish__, closed with __acc_chastity_lock__ and giving comfort through __acc_chastity_comfort__.']
    for k in list(G):
        if not G[k]: del G[k]
    return G
def run(final):
    G = build()
    for n, l in G.items(): open(os.path.join(final, n + '.txt'), 'w', encoding='utf8', newline='\n').write('\n'.join(dict.fromkeys(l)) + '\n')
    print('chastity accessories:', len(G), 'files'); return G
def export_aoo(out, prefix='aoo_'):
    G = build(); names_ = set(G); ref = re.compile(r'__([A-Za-z0-9_\-/]+)__'); n = 0
    for name, lines in G.items():
        keep = list(dict.fromkeys(ref.sub(lambda m: '__' + prefix + m.group(1) + '__' if m.group(1) in names_ else m.group(0), l) for l in lines))
        if not name.endswith('prompt'): random.Random(zlib.crc32(name.encode())).shuffle(keep)
        open(os.path.join(out, prefix + name + '.txt'), 'w', encoding='utf8', newline='\n').write('\n'.join(keep) + '\n'); n += 1
    return n
if __name__ == '__main__':
    a = [x for x in sys.argv[1:] if os.path.isdir(x)]; run(os.path.abspath(a[0]) if a else FINAL)
