"""v83 - brand style wildcards: 'In the style of <Company>, <distilled style>'. Real company names live only in maker_ files."""
import os, sys, re, glob
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from famlib import slug
HERE = os.path.dirname(os.path.abspath(__file__))
FINAL = '/home/claude/w/wildcards'
def clean(t):
    t = t.replace(':', ' -').replace(';', ',').replace('{', '').replace('}', '').replace('|', ' ').replace('__', '_').replace('"', "'")
    return re.sub(r'\s+', ' ', t).strip()
def era_bucket(e):
    m = re.search(r'(1[0-9]{3}|20[0-9]{2})', e)
    if m: y = int(m.group(1))
    elif re.search(r'(\d+)(st|nd|rd|th) century', e): y = (int(re.search(r'(\d+)(st|nd|rd|th) century', e).group(1)) - 1) * 100
    else: y = 2000
    if 'ancient' in e.lower() or 'medieval' in e.lower(): y = min(y, 1500)
    return 'before_1900' if y < 1900 else '1900_1945' if y < 1946 else '1946_1979' if y < 1980 else '1980_present'
def load():
    B = []; seen = set()
    for fn in sorted(glob.glob(HERE + '/v83_bs_*.py')):
        ns = {}
        exec(open(fn, encoding='utf8').read(), ns)
        grp = os.path.basename(fn)[7:-3]
        for name, region, era, ind, text in ns['B']:
            key = slug(name)
            if key in seen: continue
            seen.add(key)
            t = clean(text)
            if not t.lower().startswith('in the style of'): t = 'In the style of %s, %s' % (name, t)
            B.append((clean(name), region, era, ind, t, grp))
    return B

def P(x): return [i.strip() for i in x.split(';') if i.strip()]
SUBJ = {
 'vehicle': 'a two-door coupe; a four-door saloon car; a convertible with the roof down; a small hatchback; a family estate car; a pickup truck; an off-road utility vehicle; a delivery van; a sports car seen from the front corner; a city bus; a motorcycle; a scooter',
 'transport': 'a motorcycle standing on its kickstand; a bicycle leaning on a wall; a small propeller aircraft on a runway; a steam locomotive at a platform; a passenger train carriage; a river boat at a jetty; a tractor in a field; a heavy truck in a lay-by; a rocket on a launch pad; a speedboat on calm water; a city tram; a pair of roller skates',
 'fashion': 'a long coat on a mannequin; a handbag on a table; a pair of shoes on a plinth; a shirt folded flat; a dress on a hanger; a woollen jumper; a pair of trousers; a hat and scarf set; a leather jacket; a pair of boots; a woman in a full outfit standing in a doorway; a man in a full outfit leaning on a wall',
 'tech': 'a desktop radio; a handheld camera; a wristwatch on a cushion; a pair of headphones; a kitchen appliance on a worktop; a power drill on a bench; a portable record player; a desk lamp; a small computer with a keyboard; a games console with two controllers; a telephone; an electric guitar on a stand',
 'home': 'an armchair in a bright room; a dining chair beside a table; a table lamp; a ceramic teapot with cups; a glass vase with flowers; a set of dinner plates; a sofa against a wall; a wall clock; a cooking pot on a hob; a bookshelf with books; a rug on a wooden floor; a set of cutlery',
 'media': 'a lone adventurer standing in a landscape; a small group of friends in a street; a toy on a shelf; a movie-poster style scene with two characters; a book cover with an illustrated scene; a record sleeve with a bold design; a hero beside a creature; a village with a winding road; a character portrait from the chest up; a battle scene with several figures; a quiet kitchen with a cat; a castle on a hill',
 'packaging': 'a bottle on a counter; a tin on a shelf; a chocolate bar with its wrapper; a cafe interior with a counter; a shop front on a street; a cosmetics jar and box; a snack packet; a row of cans; an aircraft cabin interior; a hotel lobby; a gift box with tissue paper; a restaurant table set for two',
 'heritage': 'a handmade vase; a woven textile hanging on a wall; a pen on a writing desk; a musical instrument on a stand; a set of tea bowls; a carved wooden box; a printed page from a book; a metal jug and basin; a framed pattern tile; a piece of jewellery on velvet; a pair of ceramic figures; a folded rug',
 'modern_misc': 'a pair of trainers; a backpack on a rock; a camping stove on a table; a train station platform; a street sign on a pole; a stamp-like poster design; a metro entrance; a water bottle; a jacket on a hook; a stadium seen from the stands; a postal van; a bicycle helmet',
 'any': 'a chair; a jacket; a kettle; a car parked on a street; a shop front; a bowl and a cup; a lamp on a table; a bag on a bench; a pair of shoes; a packet of food; a clock on a wall; a person standing in a doorway',
}
GROUP_SUBJ = {'cars_eu': 'vehicle', 'cars_world': 'vehicle', 'transport': 'transport', 'fashion_eu': 'fashion', 'fashion_world': 'fashion', 'tech': 'tech', 'home': 'home', 'media': 'media', 'packaging': 'packaging', 'heritage': 'heritage', 'modern_misc': 'modern_misc'}
VIEW = P('shown in a clean studio photograph with soft even light; shown outdoors in natural daylight; shown in a warm indoor setting with window light; shown on a plain pale backdrop with a soft shadow; shown in a detailed close-up that fills the frame; shown in a wide view with its surroundings; shown at a three-quarter angle with a softly blurred background; shown in a styled magazine-like layout with plenty of space around it')
def build(final=None):
    B = load(); G = {}
    for name, region, era, ind, t, grp in B:
        G['maker_bs_' + slug(name)] = [t]
    G['maker_brand_style'] = [x[4] for x in B]
    for grp in sorted({x[5] for x in B}): G['maker_brand_style_' + grp] = [x[4] for x in B if x[5] == grp]
    for r in sorted({x[1] for x in B}): G['maker_brand_style_region_' + slug(r)] = [x[4] for x in B if x[1] == r]
    for e in ('before_1900', '1900_1945', '1946_1979', '1980_present'): G['maker_brand_style_era_' + e] = [x[4] for x in B if era_bucket(x[2]) == e]
    for i in sorted({x[3] for x in B}):
        L = [x[4] for x in B if x[3] == i]
        if len(L) >= 4: G['maker_brand_style_industry_' + slug(i)] = L
    for name, region, era, ind, t, grp in B:   # enrich thin existing make files
        fn = os.path.join(FINAL, 'maker_%s_style.txt' % slug(name))
        if os.path.exists(fn):
            old = [l.strip() for l in open(fn, encoding='utf8') if l.strip()]
            G['maker_%s_style' % slug(name)] = old + ['__maker_bs_%s__' % slug(name)]
    for name, region, era, ind, t, grp in B:
        body = re.sub(r'^In the style of [^,]*, ', '', t); w = body.split()[:26]; cut = ' '.join(w)
        if ',' in cut and len(w) >= 26: cut = cut[:cut.rfind(',')]
        G['bs_cell_' + slug(name)] = ['a typical product in the style of %s, %s' % (name, cut.rstrip(' ,.'))]
    for k, v in SUBJ.items(): G['bs_subject_' + k] = P(v)
    G['bs_view'] = VIEW
    grps = sorted({x[5] for x in B})
    for g in grps:
        sk = GROUP_SUBJ.get(g, 'any')
        G['bs_%s_prompt' % g] = ['__maker_brand_style_%s__ The subject is __bs_subject_%s__, designed completely in that style and __bs_view__.' % (g, sk)]
    G['bs_prompt'] = ['__bs_%s_prompt__' % g for g in grps]
    G['v83_bs_entry_points'] = ['bs_prompt', 'maker_brand_style'] + ['bs_%s_prompt' % g for g in grps]
    return G
if __name__ == '__main__':
    G = build(); print(len(G), len(load()))
