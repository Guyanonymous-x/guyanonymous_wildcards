"""Pick a photographic lighting line that suits the scene text: indoor scenes avoid sky/sun/street light, outdoor scenes avoid studio gear and room lamps, unknown scenes get neutral light only."""
import re
OUT_L = re.compile(r'\b(sun|sunlight|sunrise|sunset|dawn|dusk|moon|moonlight|stars?|sky|skies|horizon|eclipse|golden hour|blue hour|overcast|clouds?|cloudy|fog|mist|rain|storm|snow|winter|summer|autumn|street|streetlight|city glow|sodium|aurora|lightning|twilight|noon|midday|morning|afternoon|evening|desert|beach|forest|canopy|shade|daylight)\b', re.I)
GEAR_L = re.compile(r'\b(softbox|octabox|strobe|strobes|flash|reflector|gobo|beauty dish|umbrella|snoot|barn doors?|gelled|studio|backdrop|ring light|continuous|speedlight|tungsten|projector|lamp|lamps|window|windows|candle|candles|screen|phone|neon|fairy lights|fireplace|flashlight|torch|spotlight|monitor)\b', re.I)
IN_S = re.compile(r'\b(bed|bedroom|sofa|couch|studio|gym|sauna|bathroom|bath|shower|kitchen|living-room|living room|room|rug|hotel|apartment|sheets|mattress|armchair|dressing|changing|hall|loft|lounge|office|workshop|tub|dungeon|cabin|salon|wrestling ring|arena|ballroom|stage)\b', re.I)
OUT_S = re.compile(r'\b(beach|field|street|garden|park|forest|woods|mountain|hill|lake|river|sand|dune|meadow|farm|barn|fairground|courtyard|rooftop|balcony|terrace|campsite|yard|roadside|trail|cliff|riverbank|stable|paddock|marsh|snow|desert|pier|dock|quarry|orchard|vineyard|backyard|poolside|mud pit)\b', re.I)
PLACE = re.compile(r'\b(supermarket|skyscrapers?|streets?|dressing-room|mirror|shops?|stores?|diner|subway|train|carriage|tunnel|elevator|stage|clubs?|cinema|theatre|theater|airport|offices?|hospital|warehouse|church|cathedral|library|museum|kitchen|bars?|restaurant|alley|bridge|tower|cities|city|town|vehicle|car|cars|bus|garage|laundromat|classroom|school|petrol|gas station|motel|parking|billboard|shopfront|windshield|fridge|refrigerator|aquarium|submarine|cockpit|hangar|factory|bathroom|pool|steam|smoke|fog|dust)\b', re.I)
def mode(scene):
    i = len(IN_S.findall(scene)); o = len(OUT_S.findall(scene))
    if i and i >= o: return 'in'
    if o: return 'out'
    return 'unk'
GEN = re.compile(r'\b(softbox|octabox|key light|fill|rim light|rim|backlight|backlit|sidelight|side light|window light|north-facing|overcast|golden hour|sunset|sunrise|candle|candlelight|lamp|bounce|bounced|diffus\w*|reflector|loop lighting|rembrandt|butterfly|split lighting|short lighting|broad lighting|clamshell|beauty dish|ring flash|on-camera flash|flash|strobe|spotlight|chiaroscuro|low-key|high-key|hard light|soft light|raking|halo|twilight|blue hour|dappled|morning|afternoon|noon|studio|north light|ambient|three-quarter|dramatic|warm|cool|soft)\b', re.I)
WEIRD = re.compile(r'\b(vending|dashboard|miner|emergency|exit sign|smithy|coals|keyhole|crack|tent|helmet|headlamp|gas mantle|19th|century|neon sign|laser|disco|police|siren|traffic|sign|lantern|bonfire|campfire|welding|furnace|kiln|x-ray|blacklight|uv|infrared|thermal|night vision|lightning|aurora|bioluminescent|underwater|submerged|firework|sparkler|lava|volcano|eclipse|planetarium|projector|film|cinema|tv|television|airplane|match|cigarette|lighter|leaves|tear|water|books|shoji|oil lamp|monitor|computer|sunlit|curtain|ceiling|fluorescent|ripples)\b', re.I)
def fits(light, m):
    if PLACE.search(light) or WEIRD.search(light) or not GEN.search(light): return False
    o = bool(OUT_L.search(light)); g = bool(GEAR_L.search(light))
    if m == 'in': return not o
    if m == 'out': return not g
    return not o and not g
def pick(scene, one, seed, ref='__photostyle_lighting__'):
    m = mode(scene)
    for k in range(60):
        s = one(ref, seed + k * 1009).rstrip('.')
        if fits(s, m): return s
    return one(ref, seed).rstrip('.')
