"""Assistive, mobility and health items shown as ordinary, positive everyday details: hearing, vision, mobility aids, limb and brace devices, medical devices, communication aids, service-animal gear. Object descriptions only. Files: acc_assist_<group>, acc_assist (all), obj_mobility_*."""
import os, re, sys, random, zlib
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from paths import FINAL
G0 = {}
def cat(k, rows): G0[k] = [tuple(x.strip() for x in l.split('|')) for l in rows.strip().split('\n') if l.strip()]
cat('hearing', """
behind-the-ear hearing aid|a small curved device that sits behind the ear with a thin clear tube or wire leading to a small ear piece in the ear canal
receiver-in-canal hearing aid|a slim device behind the ear with a very thin wire to a tiny speaker that sits in the ear canal
in-the-ear hearing aid|a small shell filling part of the outer ear bowl, in a skin-matching tone
in-the-canal hearing aid|a tiny custom shell that sits partly inside the ear canal
completely-in-canal hearing aid|a very small device sitting deep in the ear canal, almost invisible, with a tiny pull-out handle
open-fit hearing aid|a slim behind-the-ear casing with a thin tube and a small soft dome in the canal
cochlear implant sound processor|a round or oval processor worn behind the ear, attached by a short cable to a round magnetic coil that sits on the side of the head
bone-anchored hearing device|a small sound processor clipped onto a titanium abutment or held by a magnet on a headband
hearing-aid on a soft headband|a processor mounted on an elastic band worn around the head
colourful decorated hearing aid|a behind-the-ear hearing aid in a bright colour with stickers or a patterned case
glasses with built-in hearing aids|spectacle frames with small speakers on the arms that direct sound to the ear
hearing protection earmuffs|large padded ear cups on a headband that cover the ears
rechargeable hearing aid with charging case|a pair of hearing aids resting in a small pocket-sized charging case
ear trumpet|a historic horn-shaped acoustic device held to the ear
""")
cat('vision', """
white cane|a long, slim, white folding cane with a red band and a rolling tip
folding white cane with a pencil tip|a segmented white cane that folds into short sections with an elastic cord
identification cane|a short, light white cane carried to show a visual impairment
support cane for visual impairment|a sturdier white cane with a crook handle
guide-dog harness|a rigid or soft handle and harness fitted to a guide dog's chest and back
tactile watch|a watch with a hinged cover over the face so the hands can be felt
braille display strip|a slim device with raised dots that update to read text
magnifying reading glasses|spectacles with thick lenses for close reading
handheld magnifier|a lens in a frame with a handle
eye patch|a soft patch worn over one eye with an elastic strap
prosthetic eye|a painted glass or acrylic shell matching the other eye
tinted low-vision glasses|glasses with deep amber or grey lenses to reduce glare
wraparound shield sunglasses|wide wraparound lenses that block light from the sides
smart glasses for audio description|glasses with a camera and bone-conduction speakers
""")
cat('mobility_worn', """
forearm crutches|a pair of lightweight crutches with a cuff around each forearm and a hand grip
underarm crutches|a pair of crutches with padded tops that rest under the arms
quad cane|a cane with four small feet at the base for stability
folding cane|a cane that folds in sections
walking stick with a carved handle|a wooden stick with a hand-carved animal-head grip
trekking-pole cane|a metal pole with a strap and a rubber tip
walker with front wheels|a four-legged frame with two front wheels and a hand grip on each side
rollator|a four-wheeled walker with brakes on the handles, a seat and a basket
knee scooter|a small wheeled platform that supports a bent knee for walking
ankle-foot orthosis|a rigid plastic brace running from under the foot up the back of the calf, strapped at the top
knee brace|a hinged support with metal side bars and straps around the knee
wrist brace|a supportive splint with a metal stay and straps across the wrist
back brace|a wide supportive corset-like band around the lower back with adjustable straps
neck brace|a padded rigid collar supporting the head and neck
arm sling|a fabric support holding the forearm across the chest with a neck strap
walking boot|a tall supportive boot with straps and a rocker sole
compression sleeves|snug elastic sleeves over the arms or legs
orthopedic shoe inserts|moulded insoles inside the shoes
""")
cat('limb', """
below-knee prosthetic leg|a socket on the residual limb with a pylon and a foot, with a visible metal tube or a cosmetic cover
above-knee prosthetic leg|a socket on the thigh with a mechanical knee joint, pylon and foot
running blade|a curved carbon-fibre blade replacing the foot and lower leg, with a rubber grip tread
prosthetic arm with a hook|a socket and harness with a split metal hook as the hand
prosthetic arm with a hand|a socket with a hand with fingers in a skin tone or in a bright colour
myoelectric hand|a bionic hand with moving fingers controlled by muscle signals
decorated prosthetic leg cover|a fairing over the leg shaped like a calf with a painted pattern
bionic arm in carbon fibre|a robotic arm with exposed carbon-fibre and metal parts
silicone cosmetic hand|a lifelike skin-toned hand with painted nails
prosthetic foot in a shoe|a flexible foot shape that fits inside a normal shoe
transparent socket prosthetic|a clear socket showing the shape of the limb inside
cosmetic finger prosthetics|individual fingertip prostheses in a skin tone
""")
cat('medical', """
insulin pump|a small device clipped to the waistband with a thin tube running to an infusion site on the skin
continuous glucose monitor|a small round sensor patch stuck on the upper arm or abdomen
insulin pen|a slim pen-shaped injector
oxygen concentrator|a portable device with a nasal cannula running to the nose
nasal cannula|a thin tube with two prongs sitting in the nostrils and looping over the ears
CPAP mask|a mask covering the nose or nose and mouth, held with head straps and a hose
tracheostomy tube|a short tube in the front of the neck, with a ribbon or a protective cover
feeding tube|a small tube entering the abdomen or nose, taped in place
ostomy pouch|a pouch attached to the abdomen, usually covered by clothing
medical alert bracelet|a metal or silicone bracelet with a medical symbol and engraved information
pacemaker scar and device bulge|a small lump under the skin below the collarbone
dialysis fistula|a raised vein ridge on the forearm
heart monitor patch|a small adhesive patch with a wire monitor
IV pole|a rolling metal pole with a bag and a tube
blood-pressure cuff|an inflatable cuff around the upper arm
pill organiser|a weekly pill box with a compartment for each day
inhaler|a small L-shaped device for breathing medicine
epinephrine auto-injector|a pen-like device carried in a case
wound dressing and bandages|gauze pads and stretch wraps on a limb
transcutaneous nerve stimulation unit|a small box clipped to a belt with wires to sticky pads
nebuliser mask|a small mask connected to a hose and a compressor
""")
cat('communication', """
AAC tablet with symbols|a tablet with a rubber case and a grid of picture buttons that speak
communication board|a laminated board with symbols or letters to point to
eye-tracking communication device|a screen on a mount with a bar that follows eye movements
speech-generating device on a wheelchair mount|a screen on an adjustable arm
sign-language interpreter glove|a glove with sensors that translate gestures
alphabet board|a flat board with letters to spell words
voice amplifier headset|a headset microphone connected to a small speaker worn on the waist
electrolarynx|a small handheld device pressed to the neck to produce speech
lanyard with a communication card|a neck cord with a card explaining how to communicate
sunflower lanyard|a green cord decorated with sunflowers that signals an invisible disability
noise-cancelling headphones|large padded headphones that reduce sound
fidget tools|small handheld tactile items like a ring, cube or spinner
""")
cat('service_animal', """
guide-dog harness with handle|a rigid U-shaped handle on a harness around a dog's chest
service-dog vest|a coloured vest with patches reading 'service dog'
mobility-assistance dog harness|a sturdy harness with a handle on the back for balance
seizure-alert dog collar|a collar with a medical alert tag
hearing-dog vest|a bright orange vest on a dog
dog leash with a quick-release|a short leash with a loop handle
emotional-support animal vest|a light vest with a patch
service-animal cart|a small wheeled support for a dog's back legs
""")
cat('adaptive_clothing', """
shirt with magnetic closures|a shirt that looks like a button-up but closes with hidden magnets
trousers cut for seated wear|trousers with a higher back and lower front, no bulky seams at the seat
tops with open back and snap shoulders|easy-dress tops that fasten at the sides and shoulders
wheelchair cape|a waterproof poncho with a seat-length drape
velcro-fastening jacket|a jacket with hook-and-loop closures
side-opening trousers|trousers that open fully down the side seam
shoes with wide zip openings|a shoe with a full-length zip
elastic-lace shoes|slip-on shoes with stretchy laces
sensory-friendly clothing|soft garments with tagless labels and flat seams
catheter-friendly trousers|trousers with a discreet opening and a leg-bag pocket
compression garment with zip|a snug top or leggings with a zip front
bib protector|a washable cover for eating
seated coat|a coat cut shorter at the back and longer in front
""")
FIN = "matte black; glossy white; light grey; bright blue; bright red; teal; lilac; sunflower yellow; forest green; metallic silver; rose gold; patterned with stars; patterned with flowers; skin-toned; clear; neon pink; orange".split('; ')
USE = ["worn every day as an ordinary part of the person's outfit", "shown plainly as a normal accessory", "worn with confidence and personal style", "customised with a personal pattern or sticker", "shown clearly and naturally"]
def build():
    G = {}; allx = []
    for k, rows in G0.items():
        out = []
        for name, desc in rows:
            for i in range(5):
                R = random.Random(zlib.crc32(f'{name}{i}'.encode()))
                out.append(f"{name.capitalize()}: {desc}; in {R.choice(FIN)}, {R.choice(USE)}.")
        G[f'acc_assist_{k}'] = sorted(set(out)); G[f'acc_assist_{k}_name'] = [n for n, d in rows]; allx += out
    G['acc_assist'] = sorted(set(allx)); G['acc_assist_finish'] = FIN
    G['acc_assist_prompt'] = ['__acc_assist__'] + [f'__acc_assist_{k}__' for k in G0]
    wheel = [l.split('|') for l in """
manual wheelchair|a lightweight folding frame with two large rear wheels with push rims, two small front casters, a padded seat and back, armrests and footrests
rigid ultralight wheelchair|a fixed-frame chair with a low back, angled wheels and a compact footplate
sports wheelchair|a chair with strongly cambered wheels, a low seat and an anti-tip wheel, for fast turns
power wheelchair|a battery-powered chair with a joystick on the armrest, a padded seat and a wide base
tilt-in-space power chair|a chair whose seat tilts back as a unit
all-terrain wheelchair|a chair with large knobby wheels or tracks
standing wheelchair|a chair that raises the user to a standing position
mobility scooter|a three- or four-wheeled scooter with a seat, a handlebar tiller and a basket
transport chair|a folding chair with four small wheels pushed by a helper
rollator with a built-in seat|a walker with a built-in seat and handbrakes
beach wheelchair|a chair with large balloon tyres for sand
hand cycle|a low three-wheeled cycle powered by arm cranks
stairlift|a motorised seat on a rail along a staircase
patient lift|a hoist with a sling
""".strip().split('\n')]
    out = []
    for n, d in wheel:
        for i in range(6):
            R = random.Random(zlib.crc32(f'{n}{i}'.encode())); out.append(f"{n.capitalize()}: {d}; frame in {R.choice(FIN)}, {R.choice(USE)}.")
    G['obj_mobility'] = sorted(set(out)); G['obj_mobility_name'] = [n for n, d in wheel]
    return G
def run(final):
    G = build()
    for n, l in G.items(): open(os.path.join(final, n + '.txt'), 'w', encoding='utf8', newline='\n').write('\n'.join(l) + '\n')
    print('assistive:', len(G), 'files;', len(G['acc_assist']), 'items'); return G
def export_aoo(out, prefix='aoo_'):
    G = build(); names_ = set(G); ref = re.compile(r'__([A-Za-z0-9_\-/]+)__'); n = 0
    for name, lines in G.items():
        keep = list(dict.fromkeys(ref.sub(lambda m: '__' + prefix + m.group(1) + '__' if m.group(1) in names_ else m.group(0), l) for l in lines))
        if not name.endswith('prompt'): random.Random(zlib.crc32(name.encode())).shuffle(keep)
        open(os.path.join(out, prefix + name + '.txt'), 'w', encoding='utf8', newline='\n').write('\n'.join(keep) + '\n'); n += 1
    return n
if __name__ == '__main__':
    a = [x for x in sys.argv[1:] if os.path.isdir(x)]; run(os.path.abspath(a[0]) if a else FINAL)
