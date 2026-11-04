"""Weapons of the world that do not use gunpowder: blades, bows, clubs, axes, polearms, thrown, chain and flexible weapons, siege engines; cultures across time. Object descriptions only, in original wording."""
import os, re, sys, random, zlib
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from paths import FINAL
def rg(*k): return random.Random(zlib.crc32('|'.join(map(str, k)).encode()))
def S(x): return [i.strip() for i in x.split(';') if i.strip()]
W = {}
def cat(k, rows): W[k] = [tuple(x.strip() for x in l.split('|')) for l in rows.strip().split('\n') if l.strip()]
cat('sword', """
longsword|medieval Europe|a double-edged straight blade with a long cross-guard and a hilt made for two hands
arming sword|medieval Europe|a single-handed double-edged blade with a cross-guard and a round pommel
claymore|Scotland|a two-handed sword with a long blade and down-sloped quillons ending in quatrefoil tips
rapier|Renaissance Spain and Italy|a long slender thrusting blade with a swept hilt that guards the hand
cutlass|maritime Europe|a short curved single-edged blade with a wide basket hilt
katana|Japan|a gently curved single-edged blade with a wavy temper line, a round guard and a wrapped hilt
wakizashi|Japan|a shorter curved blade carried with the long sword, with a small guard
tachi|Japan|a long, deeply curved sword with a slung scabbard and a decorated mount
scimitar|Middle East|a curved single-edged blade that widens toward the tip
shamshir|Persia|a strongly curved narrow blade with a lion-head pommel
talwar|India|a curved blade with a disc pommel and a knuckle guard
khanda|India|a straight double-edged blade that widens at the tip with a basket hilt
kilij|Turkey|a curved blade with a flared tip and a hooked guard
dao|China|a single-edged curved broadsword with a ring-ornamented back
jian|China|a straight double-edged sword with a tasselled pommel
gladius|Rome|a short broad double-edged blade with a pointed tip
spatha|Rome|a long straight blade for cavalry
xiphos|ancient Greece|a leaf-shaped double-edged short sword
khopesh|ancient Egypt|a sickle-shaped bronze blade with a long handle
kopis|ancient Greece|a forward-curving single-edged chopping blade
falcata|Iberia|a forward-curved blade with a horse-head hilt
seax|Anglo-Saxon England|a single-edged knife-sword with a thick back and a short grip
Viking sword|Scandinavia|a double-edged blade with a wide fuller and a lobed pommel
macuahuitl|Aztec Mexico|a flat wooden club set along its edges with sharp obsidian blades
katar blade-sword|India|a long blade attached to a punch handle
zweihander|Germany|an enormous two-handed sword with a double guard
flamberge|Europe|a flame-shaped wavy blade
estoc|Europe|a stiff, long thrusting sword with a diamond-section blade
dha|Southeast Asia|a long single-edged blade with a round handle
kampilan|Philippines|a single-edged blade with a cleft tip and a decorated hilt
panga machete blade|Africa|a broad, flat chopping blade
takoba|Tuareg Sahara|a straight blade with a cross-shaped guard and a decorated leather scabbard
kaskara|Sudan|a straight double-edged blade with a cross-guard and a leather-covered grip
shotel|Ethiopia|a sickle-shaped sword that curves sharply near the tip
nimcha|Morocco|a curved blade with a hooked guard and an ornamented hilt
ida|West Africa|a short curved sword with a carved wooden handle
""")
cat('knife', """
dagger|medieval Europe|a short, double-edged stabbing blade with a small guard
rondel dagger|medieval Europe|a stiff narrow blade with round disc guards at the hilt
stiletto|Italy|a slim needle-like blade with a round grip
kris|Indonesia and Malaysia|a wavy asymmetrical blade with an ornate carved hilt
kukri|Nepal|a heavy inward-curved blade with a notch near the grip
tanto|Japan|a short single-edged knife with a squared tip
kozuka|Japan|a small utility knife in a sheath
bowie knife|United States|a large single-edged blade with a clipped point
dirk|Scotland|a long dagger with a carved handle
skean dhu|Scotland|a small knife tucked in the boot
kard|Persia|a straight single-edged knife
jambiya|Arabia|a curved dagger with a carved handle and a wide curved blade
bichwa|India|a small curved blade with a loop handle
khanjar|Oman|a curved dagger in a silver sheath with a belt
main gauche|Europe|a parrying dagger
ulu|Inuit|a semicircular knife with a handle across the top
sgian|Scotland|a small knife with a carved top
panga|Africa|a long machete-style blade
throwing knife|world|a balanced fixed-blade knife with no guard
punch dagger|India|a blade with a handle perpendicular to the blade
tomahawk knife|North America|a hatchet-like knife with a thin head
karambit|Southeast Asia|a small, curved, claw-like blade with a ring in the handle
kunai|Japan|a flat-leaf-shaped tool with a ring pommel
sickle knife|Africa|a curved blade with a short grip
""")
cat('axe', """
battle axe|medieval Europe|a long-hafted axe with a broad single blade
bearded axe|Viking Scandinavia|an axe whose blade hooks downward in a beard shape
francisca|Franks|a short throwing axe with a curved head
tomahawk|North America|a light axe with a short handle and a smooth head
war hatchet|North America|a small single-handed axe
doloire|France|a long broad-bladed axe
tabar|Persia and India|a crescent-bladed axe on a short shaft
labrys|Minoan Crete|a double-headed ceremonial axe
pickaxe|world|a pointed head and a flat head on a wooden handle
poleaxe|medieval Europe|an axe, hammer and spike combined on a long shaft
danish axe|Viking Scandinavia|a long, broad-headed two-handed axe
kanabo axe|Japan|an iron-bound axe
nzappa zap|Central Africa|an ornate throwing blade
Zulu iklwa-axe|southern Africa|a small axe-headed tool
Chinese ge halberd|China|a dagger-blade on a long pole
bardiche|Eastern Europe|a long crescent blade on a long shaft
""")
cat('spear', """
spear|ancient world|a pointed head on a long wooden shaft
javelin|ancient Greece|a light throwing spear
pilum|Rome|a long iron shank on a wooden shaft
sarissa|Macedonia|an extremely long pike
trident|ancient Mediterranean|a three-pronged spear
glaive|medieval Europe|a long single-edged blade on a pole
halberd|Switzerland|an axe, spike and hook on a pole
naginata|Japan|a curved blade on a long pole
yari|Japan|a straight spear with a long head
guandao|China|a heavy curved blade on a long pole
qiang|China|a spear with a red tassel
pike|medieval Europe|a very long infantry spear
lance|medieval Europe|a long jousting spear with a hand guard
partisan|Europe|a spear with a broad double-edged blade
ranseur|Europe|a spear with side prongs
bill hook|England|a hooked blade on a long pole
assegai|southern Africa|a short throwing spear with a leaf-shaped blade
iklwa|Zulu southern Africa|a short stabbing spear with a long blade
harpoon|Arctic and Pacific|a barbed head on a line
fishing spear|Pacific|a multi-pronged spear
atlatl dart|North America|a long dart thrown with a spear-thrower
bo spear|Japan|a long staff-spear
vel|South India|a leaf-shaped spearhead
naga danda|India|a serpent-headed spear
pole-hook|Africa|a long hooked spear
""")
cat('club', """
mace|medieval Europe|a heavy head with flanges on a short shaft
morning star|Europe|a spiked-ball head on a shaft
flail|medieval Europe|a spiked ball on a chain attached to a handle
war hammer|Europe|a hammer head with a spike on a handle
maul|Europe|a heavy two-handed hammer
gada|India|a round-headed mace with a long handle
shishpar|Persia|a flanged mace
kanabo|Japan|a spiked iron-bound club
jitte|Japan|a metal truncheon with a hook guard
tonfa|Okinawa|a baton with a side handle
nunchaku|Okinawa|two sticks joined by a cord or chain
sai|Okinawa|a three-pronged metal truncheon
kiyoga|Africa|a knob-headed throwing club
knobkerrie|southern Africa|a wooden club with a round knob
war club|North America|a wooden club with a stone head
gunstock war club|North America|a wooden club shaped like a stock with a spike
mere|Maori New Zealand|a short flat paddle-shaped club of greenstone
patu|Maori New Zealand|a short flat club
wahaika|Maori New Zealand|a short club with a carved notched edge
taiaha|Maori New Zealand|a long staff with a carved tongue and a flat blade
leiomano|Hawaii|a paddle club edged with shark teeth
ula|Fiji|a throwing club with a round head
totokia|Fiji|a club with a beaked head
paddle club|Pacific|a carved wooden paddle
boomerang war club|Australia|a heavy curved club
waddy|Australia|a short wooden club
baton|world|a short stick for striking
cudgel|Europe|a thick wooden stick
bokken|Japan|a wooden sword
shillelagh|Ireland|a knobby blackthorn stick
quarterstaff|England|a long wooden staff
""")
cat('bow', """
longbow|medieval England|a tall self bow of yew
recurve bow|Asia|a curved bow made of horn, wood and sinew
composite bow|steppe Asia|a laminated bow of horn and sinew
horse bow|Mongolia|a short composite bow for riding
yumi|Japan|a very tall asymmetric bow
flatbow|North America|a broad flat wooden bow
self bow|world|a bow made from a single piece of wood
crossbow|medieval Europe|a stock with a horizontal bow and a trigger
repeating crossbow|China|a crossbow with a magazine on top
arbalest|Europe|a large steel-limbed crossbow
sinew-backed bow|North America|a short bow backed with animal sinew
pellet bow|Asia|a bow with a cradle for stones
blowgun|Amazon and Southeast Asia|a long hollow tube for firing darts
sling|ancient world|a pouch on cords for hurling stones
slingshot|world|a forked frame with an elastic band
atlatl|Mesoamerica|a spear-thrower with a hooked end
boomerang|Australia|a curved throwing stick
bolas|South America|weighted cords for tangling
throwing disc|world|a flat circular blade
chakram|India|a flat ring with a sharp edge
shuriken|Japan|a flat star-shaped blade
fukiya|Japan|a short blowgun
yumi arrow|Japan|a long arrow with a bamboo shaft
Mongol quiver|steppe Asia|a leather-covered case with painted arrows
Ethiopian bow|Africa|a simple wooden bow
Bhutanese bamboo bow|Himalaya|a long bamboo bow
trebuchet|medieval Europe|a siege engine with a swinging arm
catapult|ancient world|a throwing engine of tension
ballista|Rome|a giant crossbow-like bolt thrower
onager|Rome|a single-arm stone thrower
""")
cat('other', """
whip|world|a long braided flexible cord
kusarigama|Japan|a sickle with a weighted chain
meteor hammer|China|a weighted ball on a long rope
rope dart|China|a pointed dart on a long cord
three-section staff|China|three wooden sections joined by chain
nine-section whip|China|a chain of metal segments
cestus|ancient Rome|a hand wrap studded with metal
knuckle duster|world|a metal piece for the fist
bagh nakh|India|curved claws worn on the fingers
urumi|India|a coiled flexible sword with long blades
chain whip|China|segmented metal whip
hook swords|China|a pair of swords with hooked tips
butterfly swords|China|a pair of short broad swords
wushu fan|China|a folding war fan with iron ribs
tessen|Japan|an iron war fan
manriki|Japan|a short weighted chain
ankus|India|an elephant goad with a hook
net and trident|Rome|a weighted net and a three-pronged spear
gladiator's sica|Thrace|a curved short blade
shield-spike|world|a spike on the centre of a shield
saw sword|Pacific|a long saw-toothed sword
shark-tooth sword|Kiribati|a wooden blade set with shark teeth
whale-bone club|Arctic|a heavy club carved from bone
caltrops|ancient world|spiked metal pieces
""")
MAT = S("polished steel; blackened iron; bronze; hammered copper; folded layered steel; carved hardwood; ash wood; bamboo; ironwood; horn; bone; obsidian; flint; shark teeth; jade; greenstone; walnut; yew; rawhide-wrapped; sinew-wrapped")
HILT = S("a leather-wrapped grip; a carved wooden handle; a silver-wire grip; a gold-inlaid hilt; a cord-wrapped handle; a bone-inlaid handle; a jewel-set pommel; a ray-skin grip; a brass guard; a tassel at the pommel; a carved animal-head pommel; an engraved crossguard; a rope-wrapped haft; feather and bead decorations; painted geometric designs; a lacquered scabbard; a tooled leather sheath; a woven strap")
FIN = S("a battle-worn finish; a mirror polish; an etched pattern along the blade; a patterned surface; a dark patina; nicks and scratches from use; a clean ceremonial finish; engraved inscriptions; painted designs; carved spirals")
MATC = {'sword': S('polished steel; blackened iron; bronze; folded layered steel; hammered copper; patterned steel; iron with a bronze guard'), 'knife': S('polished steel; blackened iron; bronze; folded layered steel; obsidian; flint; bone; hammered copper'), 'axe': S('forged iron; bronze; polished steel; flint; greenstone; blackened steel with an ash-wood haft'), 'spear': S('an iron head on an ash shaft; a bronze head on a hardwood shaft; a flint head on a bamboo shaft; a steel head on an ironwood shaft; an obsidian head on a wooden shaft'), 'club': S('carved hardwood; ironwood; ash wood; whale bone; greenstone; iron with a wooden haft; stone-headed wood; bamboo'), 'bow': S('yew wood; bamboo; horn and sinew laminate; ash wood; ironwood; laminated wood and horn; carved hardwood'), 'other': S('forged iron; polished steel; braided leather; bronze; hardwood; woven cord with iron weights; shark teeth and wood')}
COND = S("new; ancient and weathered; ceremonial; museum-grade; battle-worn; ornate; plain and practical; lovingly restored; rusted; polished")
def build():
    G = {}; allw = []
    for k, rows in W.items():
        out = []
        for name, culture, desc in rows:
            for i in range(6):
                R = rg('wp', name, i)
                out.append(f"{R.choice(COND).capitalize()} {name} from {culture}: {desc}; made of {R.choice(MATC[k])}, with {R.choice(HILT)} and {R.choice(FIN)}.")
        G[f'weapon_{k}'] = sorted(set(out)); G[f'weapon_{k}_name'] = [f"{n} ({c})" for n, c, d in rows]; allw += out
    G['weapon'] = sorted(set(allw)); G['weapon_type'] = sorted({n for rows in W.values() for n, c, d in rows})
    G['weapon_culture'] = sorted({c for rows in W.values() for n, c, d in rows}); G['weapon_material'] = MAT; G['weapon_hilt'] = HILT; G['weapon_finish'] = FIN; G['weapon_condition'] = COND
    G['weapon_prompt'] = ['__weapon__', '__weapon_sword__', '__weapon_knife__', '__weapon_axe__', '__weapon_spear__', '__weapon_club__', '__weapon_bow__', '__weapon_other__', 'Two weapons side by side: __weapon__ and __weapon__']
    return G
def run(final):
    G = build()
    for n, l in G.items():
        assert l and all(l), n
        open(os.path.join(final, n + '.txt'), 'w', encoding='utf8', newline='\n').write('\n'.join(l) + '\n')
    print('weapons:', len(G), 'files;', len(G['weapon']), 'descriptions'); return G
def export_aoo(out, prefix='aoo_'):
    G = build(); names_ = set(G); ref = re.compile(r'__([A-Za-z0-9_\-/]+)__'); n = 0
    for name, lines in G.items():
        keep = list(dict.fromkeys(ref.sub(lambda m: '__' + prefix + m.group(1) + '__' if m.group(1) in names_ else m.group(0), l) for l in lines))
        if not name.startswith('weapon_prompt'): random.Random(zlib.crc32(name.encode())).shuffle(keep)
        open(os.path.join(out, prefix + name + '.txt'), 'w', encoding='utf8', newline='\n').write('\n'.join(keep) + '\n'); n += 1
    return n
if __name__ == '__main__':
    a = [x for x in sys.argv[1:] if os.path.isdir(x)]; run(os.path.abspath(a[0]) if a else FINAL)
