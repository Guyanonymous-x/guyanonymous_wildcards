"""Season and weather outfit prompts. Files wx_*. Garment/outfit descriptions only (no brands)."""
import os, re, sys, random, zlib
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from paths import FINAL
def S(x): return [i.strip() for i in x.split(';') if i.strip()]
def R(*k): return random.Random(zlib.crc32('|'.join(map(str, k)).encode()))
C = {  # condition: (weather description, tops, bottoms, outer, head, feet, extras)
'hot_dry': ("a hot, dry, sunny day", "a loose linen shirt; a sleeveless cotton top; a thin vest top; a short-sleeved camp shirt; a light tunic; a mesh sports tee", "linen shorts; a flowing midi skirt; light cotton trousers; wide-leg linen pants; board shorts; a light sarong", "no outer layer; a thin open overshirt; a sheer cover-up; a light kaftan", "a wide-brimmed straw hat; a cap; a light scarf over the head; a bandana", "open sandals; canvas slip-ons; light sneakers; espadrilles", "sunglasses; a water bottle; a light tote bag; sunscreen-streaked shoulders"),
'hot_humid': ("a hot, humid day with sticky air", "a damp-looking singlet; a thin cotton tee; a breathable mesh top; a loose short-sleeved shirt; a light halter top", "light shorts; a thin skirt; loose cotton pants; quick-dry shorts", "no outer layer; a thin rain poncho folded in a bag", "a visor; a bandana; a light cap", "flip-flops; sport sandals; breathable sneakers", "a hand fan; a small towel around the neck; a sweat-darkened collar"),
'heatwave': ("a scorching heatwave", "the lightest sleeveless top; a bare minimum vest; a loose pale shirt worn open", "short shorts; a thin wrap skirt; the lightest loose trousers", "no outer layer; a damp cooling cloth over the shoulders", "a wide hat; a wet cloth under a cap", "slides; open sandals", "a spray bottle; a portable fan; a cooling neck wrap"),
'spring_mild': ("a mild spring day with a light breeze", "a light cotton blouse; a long-sleeved tee; a thin knit; a floral shirt; a light polo", "jeans; a knee-length skirt; chinos; cropped trousers", "a light jacket; a denim jacket; a cardigan; a thin trench coat", "no hat; a light cap; a silk scarf", "canvas sneakers; loafers; ballet flats; low boots", "a tote bag; a thin scarf; flowers in a bag"),
'spring_rain': ("a drizzly spring day", "a long-sleeved tee; a light sweater; a plain shirt", "jeans; water-resistant trousers; a mid-length skirt with boots", "a hooded rain jacket; a light trench; a transparent raincoat", "a hood; a bucket hat; a small umbrella held up", "rubber boots; waterproof sneakers; ankle boots", "an umbrella; a waterproof tote; damp hair"),
'autumn_cool': ("a cool, crisp autumn day with falling leaves", "a knit sweater; a flannel shirt; a turtleneck; a chunky cardigan", "dark jeans; corduroy trousers; a wool skirt with tights; chinos", "a wool coat; a leather jacket; a quilted vest; a waxed jacket", "a beanie; a wool scarf; a flat cap", "leather boots; suede boots; sturdy sneakers", "a scarf; fingerless gloves; a thermos"),
'autumn_windy': ("a windy autumn afternoon", "a thick knit sweater; a hoodie; a layered shirt and vest", "jeans; heavy cotton trousers; leggings under a skirt", "a windbreaker; a long coat buttoned to the chin; a zipped jacket", "a hat pulled down; a beanie; a tied scarf", "boots; high-top sneakers", "hair blown across the face; a flapping coat hem"),
'winter_cold': ("a cold winter day", "a thermal base layer; a heavy wool jumper; a fleece midlayer; a turtleneck", "lined trousers; thermal leggings under jeans; wool tights under a skirt", "a long down coat; a padded parka; a heavy wool overcoat", "a wool hat; a fleece headband; a fur-lined hood", "insulated boots; felt-lined boots; leather boots with thick socks", "thick gloves; a long scarf; a hot drink"),
'winter_freezing': ("a freezing, bitter winter day", "two thermal layers and a thick sweater; a fleece-lined hoodie; a high-neck knit", "insulated snow trousers; double-layered trousers; thermal tights under heavy skirts", "an expedition parka with a fur-trimmed hood; a quilted long coat; a down jacket with a high collar", "a balaclava; an ear-flap hat; a knit cap under a hood", "heavy snow boots; fur-lined boots", "mittens; a scarf over the face; chemical hand warmers"),
'snow': ("a snowy day with deep snow and falling flakes", "a ski base layer; a patterned wool sweater; a fleece", "insulated snow pants; waterproof trousers; thick leggings", "a waterproof ski jacket; a thick padded coat; a snow suit", "a bobble hat; goggles pushed up; a helmet", "snow boots; gaiter-covered boots", "gloves; a neck gaiter; snow on the shoulders"),
'blizzard': ("a blizzard with whiteout wind and blowing snow", "layers of thermal wear; a thick insulating jumper", "insulated overtrousers; snow pants", "a hard-shell parka zipped to the chin; a heavy down jacket", "a balaclava and goggles; a hood cinched tight", "insulated mountaineering boots", "mittens; a face mask; ice on the eyelashes"),
'rain': ("a heavy rainy day", "a waterproof top; a hooded jacket worn over a sweater", "waterproof trousers; jeans soaked at the hem; a skirt with boots", "a hooded raincoat; a long poncho; a yellow oilskin coat", "a rain hood; a wide umbrella; a waterproof cap", "rubber boots; waterproof walking boots", "an umbrella; a drenched look; puddle splashes on the trouser legs"),
'monsoon': ("a tropical monsoon downpour", "a quick-dry shirt; a light poncho over a tee", "quick-dry shorts; rolled trousers; a short skirt", "a plastic poncho; a thin waterproof jacket", "a wide rain hat; a hood", "sandals; waterproof sandals; bare feet", "a banana-leaf umbrella; soaked clothes clinging"),
'storm': ("a thunderstorm with gusting wind and rain", "a layered sweater; a waterproof shell", "waterproof overtrousers; jeans", "a storm jacket with a deep hood; a heavy coat", "a hood held with a hand; a sou'wester", "waterproof boots", "a bent umbrella; a bag held tight; wet hair"),
'fog': ("a thick foggy morning", "a wool sweater; a long-sleeved top; a turtleneck", "dark trousers; long skirt with tights", "a wool coat; a waxed jacket; a peacoat", "a scarf; a flat cap; a beanie", "boots; leather shoes", "a hot drink; breath visible; damp hair"),
'desert_dust': ("a hot desert day with blowing dust", "a long-sleeved loose shirt; a light wrap tunic", "loose long trousers; a long skirt; baggy pants", "a long light robe; a hooded wrap; a loose djellaba", "a turban-style headwrap; a face scarf; goggles", "closed sturdy boots; sandals with socks", "a water skin; a dust-covered cloak"),
'beach': ("a sunny day at the beach", "a swim top; a rash guard; a bikini top; a shirtless swim look in trunks", "swim trunks; a swim brief; a sarong; board shorts; a bikini bottom", "a light kaftan; an open shirt; a towel wrap", "a sun hat; a visor; sunglasses on the head", "bare feet; flip-flops; water shoes", "a beach bag; a towel; sand on the legs"),
'alpine': ("a clear alpine day with strong sun and thin cold air", "a base layer under a fleece; a long-sleeved hiking shirt", "hiking trousers; softshell pants", "a windproof shell; a light puffy jacket tied to the waist", "a sun hat; a buff; a beanie", "mountain boots; gaiters", "trekking poles; a backpack; sun-reddened cheeks"),
'sleet': ("a grey, wet sleety day", "a waterproof jacket over a jumper; a thermal layer", "waterproof trousers; lined jeans", "a hooded waterproof parka", "a hat with a brim; a hood", "waterproof boots", "wet gloves; slush-stained hems"),
'night_cool': ("a cool clear night", "a long-sleeved top; a thin knit; a hoodie", "jeans; long trousers; a skirt with tights", "a jacket; a coat; a blanket wrap", "a beanie; a light scarf", "closed shoes; boots", "a flashlight; breath visible"),
}
SEAS = S("early spring; mid spring; late spring; early summer; midsummer; late summer; early autumn; mid autumn; late autumn; early winter; midwinter; late winter; the rainy season; the dry season; the monsoon season; harvest time; the first snow; a heatwave week; a mild shoulder season; the long polar night; a midnight-sun summer")
def mk():
    G = {}
    for k, (desc, tops, bots, outer, head, feet, extras) in C.items():
        parts = {'top': S(tops), 'bottom': S(bots), 'outer': S(outer), 'head': S(head), 'feet': S(feet), 'extra': S(extras)}
        for p, l in parts.items(): G[f'wx_{k}_{p}'] = l
        G[f'wx_{k}'] = [f"During {desc}: __wx_{k}_top__, __wx_{k}_bottom__, __wx_{k}_outer__, __wx_{k}_head__, __wx_{k}_feet__, and __wx_{k}_extra__.",
                        f"Dressed for {desc}, wearing __wx_{k}_top__ with __wx_{k}_bottom__, topped with __wx_{k}_outer__, __wx_{k}_head__ and __wx_{k}_feet__.",
                        f"Weather and outfit: {desc}; __wx_{k}_top__, __wx_{k}_bottom__, __wx_{k}_feet__, __wx_{k}_extra__."]
    G['wx_weather'] = [v[0] for v in C.values()]
    G['wx_season'] = SEAS
    G['wx_outfit_any'] = [f'__wx_{k}__' for k in C]
    G['wx_outfit_warm'] = [f'__wx_{k}__' for k in ('hot_dry', 'hot_humid', 'heatwave', 'beach', 'spring_mild', 'desert_dust')]
    G['wx_outfit_cold'] = [f'__wx_{k}__' for k in ('autumn_cool', 'winter_cold', 'winter_freezing', 'snow', 'blizzard', 'sleet', 'alpine', 'night_cool')]
    G['wx_outfit_wet'] = [f'__wx_{k}__' for k in ('spring_rain', 'rain', 'monsoon', 'storm', 'fog', 'sleet')]
    G['wx_outfit_with_tan'] = [f'__wx_{k}__ Skin: __skin_tan_{lv}__.' for k in ('hot_dry', 'hot_humid', 'heatwave', 'beach') for lv in ('faint', 'light', 'moderate', 'deep', 'burn_red')]
    G['wx_outfit_prompt'] = ['In __wx_season__, __wx_outfit_any__', '__wx_outfit_warm__', '__wx_outfit_cold__', '__wx_outfit_wet__']
    return G
def build(): return mk()
def run(final):
    G = build()
    for n, l in G.items():
        assert l and all(l) and not any(c in x for x in l for c in '{}|'), n
        open(os.path.join(final, n + '.txt'), 'w', encoding='utf8', newline='\n').write('\n'.join(dict.fromkeys(l)) + '\n')
    print('weather:', len(G), 'files'); return G
def export_aoo(out, prefix='aoo_'):
    G = build(); nm = set(G) | {f'skin_tan_{lv}' for lv in ('faint','light','moderate','deep','burn_red')}; ref = re.compile(r'__([A-Za-z0-9_\-/]+)__'); n = 0
    for name, lines in G.items():
        keep = list(dict.fromkeys(ref.sub(lambda m: '__' + prefix + m.group(1) + '__' if m.group(1) in nm else m.group(0), l) for l in lines))
        if not (name.startswith('wx_outfit') or name in ('wx_weather',)) : random.Random(zlib.crc32(name.encode())).shuffle(keep)
        open(os.path.join(out, prefix + name + '.txt'), 'w', encoding='utf8', newline='\n').write('\n'.join(keep) + '\n'); n += 1
    return n
if __name__ == '__main__':
    a = [x for x in sys.argv[1:] if os.path.isdir(x)]; run(os.path.abspath(a[0]) if a else FINAL)
