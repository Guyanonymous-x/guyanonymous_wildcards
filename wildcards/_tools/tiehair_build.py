"""Tie hardware (pins, clips, bars, bolo-tie slides and tips) and hair states (messy, bed head). Files acc_tiepin*, acc_tieclip*, acc_tiebar*, acc_bolo*, acc_tiehw_prompt, hair_state_*."""
import os, re, sys, random, zlib
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from paths import FINAL
def S(x): return [i.strip() for i in x.split(';') if i.strip()]
def R(*k): return random.Random(zlib.crc32('|'.join(map(str, k)).encode()))
MET = S("polished silver; brushed steel; yellow gold; rose gold; white gold; antique brass; gunmetal; copper; pewter; titanium; black enamel on steel; oxidised silver; gold-plated brass; platinum; hammered bronze; nickel; blackened iron")
STONE = S("a small onyx cabochon; a pearl; a tiny diamond; a garnet; an opal; a turquoise stone; a lapis lazuli bead; a jade disc; a sapphire; a ruby; a tiger's-eye stone; an amethyst; a moonstone; a mother-of-pearl inlay; a carved coral bead; no stone; a plain engraved surface; a champlevé enamel panel; a guilloche enamel panel; a mosaic inlay")
MOTIF = S("a crossed-key design; an anchor; a feather; a tiny compass rose; a star; a laurel leaf; a bee; a horseshoe; a chess knight; a gear; a dragonfly; a lotus; a geometric Art Deco fan; a Celtic knot; a sun disc; a moon crescent; a key; a quill; a ship's wheel; an oak leaf; a snake; a fish; a monogram; a Japanese crest; an Adinkra symbol; a zigzag line; a plain bar with no motif; a sunburst; a mountain; a small ruler; a bamboo stalk")
PIN = S("a straight stick pin with a decorative head and a safety guard; a jewelled tie tack on a chain; a bar pin that threads through the tie and shirt placket; a horizontal bar pin with ball ends; a bee-shaped tie tack with a chain; a pearl-headed stick pin; a barbell-style tie bar pin; a gem tie tack with a locking clutch back; a hat-pin-sized stick pin with a long shaft; a spring-loaded alligator tie pin")
CLIP = S("a slim spring tie clip with a plain face; a wide tie clip with a ridged face; a tie clip with an engraved monogram; a tie clip with a jewel set at one end; a tie clip with a rope-twist edge; a clip with a hinged catch and a chain; a sliding alligator clip; a lapel-width crocodile clip; a magnetic tie clip; a tie clip made from a coin edge; a skeleton-pierced tie clip; a black enamel tie clip with a metal rim")
BAR = S("a slim tie bar with rounded ends; a collar bar with ball ends that screws open; a collar bar with a clip at each end; a chain collar bar linking two collar points; a collar pin through two eyelets; a tab collar snap; a slotted collar stay with a decorative cap; a bolt-style collar bar with studs")
BOLO_SLIDE = S("a round silver slide set with turquoise; an oval slide of carved bone; a polished stone disc slide; a slide in the shape of a longhorn skull; a slide with a hand-stamped Navajo-style silver pattern; a slide made of a polished agate slice; a slide with a cowboy hat motif; a woven horsehair slide; a slide shaped like an eagle; a Western engraved scroll silver slide; a slide in the shape of a tiny saddle; a slide with an inlaid opal; a slide made from a coin; a minimalist round brass slide; a slide made from petrified wood; a slide with a mother-of-pearl inlay; a slide with a bronze scorpion; a slide shaped like a sun")
BOLO_CORD = S("a braided black leather cord; a flat brown leather lace; a round waxed cotton cord; a braided horsehair cord; a rawhide thong; a silk cord with a woven pattern; a two-tone twisted cord; a chain cord; a thin paracord braid; a knotted hemp cord")
BOLO_TIP = S("silver-capped metal tips; engraved metal tips with turquoise beads; pointed brass aglets; tassel ends; tips of carved horn; plain stainless tips with a ring; scrolled silver tips; enamelled tips; no tips, the cord ends knotted; feather charms at the ends")
STATE = S("brand new and shiny; slightly tarnished; worn smooth with age; scratched from daily use; engraved with initials; a family heirloom with a soft patina; a cheap plated pin showing brass at the edges; crooked on the tie; sitting a little low on the shirt; polished for a formal occasion")
def hair_states():
    lens = S("a buzz cut; short cropped hair; a short pixie length; chin-length hair; shoulder-length hair; mid-back hair; waist-length hair; a long braid; hair twisted in locs; short coily hair; an afro; long wavy hair; long straight hair; thick curly hair; fine thin hair; a short fade; hair in a topknot")
    msg = S("tangled and sticking up in every direction; flattened on one side and raised on the other; with a tuft standing straight up at the crown; with strands stuck across the forehead; with a cowlick pointing sideways; with flyaways catching the light; with loose ends escaping a half-undone tie; matted on the back of the head; with a flat patch where a pillow pressed; with dried product leaving stiff clumps; with one curl sprung loose and wild; windswept to one side; tousled with fingers run through it repeatedly; frizzed up after sleep; fluffed up with static; with a long strand sticking to the cheek; sleep-pressed on one side and puffed on the other; slept-in and unbrushed; with a bent wave from a pillow crease; with tight curls flattened on one side and a puffed shape on the other")
    SHORT = {'a buzz cut', 'short cropped hair', 'a short pixie length', 'a short fade', 'short coily hair', 'an afro'}
    ok = lambda l, m: not (l in SHORT and re.search(r'strand|tie|braid|loose ends|curl|matted|tuft|stuck|fingers|flyaways', m))
    G = {}
    G['hair_state_bedhead'] = sorted({f"{l}, {m}" for l in lens for m in msg if ok(l, m) and R('bh', l, m).random() < .45})
    G['hair_state_messy'] = sorted({f"{l} in a deliberately messy style, {m}" for l in lens for m in msg if ok(l, m) and R('ms', l, m).random() < .35})
    G['hair_state_length'] = lens; G['hair_state_look'] = msg
    G['hair_state_prompt'] = ['__hair_state_bedhead__.', '__hair_state_messy__.']
    return G
def mk():
    G = {}
    for n, items, extra in [('acc_tiepin', PIN, None), ('acc_tieclip', CLIP, None), ('acc_tiebar', BAR, None)]:
        G[n + '_type'] = items
        G[n] = sorted({f"{it}, in {m}, with {R(n, it, m).choice(STONE)} and {R(n, m, it).choice(MOTIF)}, {R(n, it, m, 's').choice(STATE)}" for it in items for m in MET if R('t', n, it, m).random() < .45})
    G['acc_tiehw_metal'] = MET; G['acc_tiehw_stone'] = STONE; G['acc_tiehw_motif'] = MOTIF; G['acc_tiehw_state'] = STATE
    G['acc_bolo_slide'] = BOLO_SLIDE; G['acc_bolo_cord'] = BOLO_CORD; G['acc_bolo_tip'] = BOLO_TIP
    G['acc_bolo'] = sorted({f"a bolo tie with {s}, on {c}, finished with {t}, {R('b', s, c, t).choice(STATE)}" for s in BOLO_SLIDE for c in BOLO_CORD for t in BOLO_TIP if R('bo', s, c, t).random() < .25})
    G['acc_tiehw_prompt'] = ['__acc_tiepin__.', '__acc_tieclip__.', '__acc_tiebar__.', '__acc_bolo__.']
    G.update(hair_states()); return G
def build(): return mk()
def run(final):
    G = build()
    for n, l in G.items():
        assert l and all(l) and not any(c in x for x in l for c in '{}|'), n
        open(os.path.join(final, n + '.txt'), 'w', encoding='utf8', newline='\n').write('\n'.join(dict.fromkeys(l)) + '\n')
    print('ties/hair:', len(G), 'files'); return G
def export_aoo(out, prefix='aoo_'):
    G = build(); nm = set(G); ref = re.compile(r'__([A-Za-z0-9_\-/]+)__'); n = 0
    for name, lines in G.items():
        keep = list(dict.fromkeys(ref.sub(lambda m: '__' + prefix + m.group(1) + '__' if m.group(1) in nm else m.group(0), l) for l in lines))
        if not name.endswith('prompt'): random.Random(zlib.crc32(name.encode())).shuffle(keep)
        open(os.path.join(out, prefix + name + '.txt'), 'w', encoding='utf8', newline='\n').write('\n'.join(keep) + '\n'); n += 1
    return n
if __name__ == '__main__':
    a = [x for x in sys.argv[1:] if os.path.isdir(x)]; run(os.path.abspath(a[0]) if a else FINAL)
