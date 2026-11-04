"""v75 stage B - Location Inventory pilot converter. Reads the exported location records (docs/location_inventory/*.md) and writes per-location pools:
loc_<id>_items / furniture / installed / signature / materials / palette / light / traces / condition, a clean scene (loc_<id>_clean), a full scene (loc_<id>_scene),
a scene with anywhere items (loc_<id>_scene_plus), tag indexes (loc_tag_<value>) and 'anywhere' pools compiled from phrases shared by 2 or more locations.
Re-runnable: re-export the doc files, run this stage again."""
import os, re, sys, glob
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from famlib import slug
DOCS = '/home/claude/w/docs/location_inventory'
FILES = [('Home_Interior_80.md', 'home'), ('Home_Exterior_50.md', 'ext'), ('Workplace_70.md', 'work'), ('Circulation_Thresholds.md', 'circ'),
         ('Bathrooms_expanded.md', 'bath'), ('Food_Hospitality_expanded.md', 'food'), ('Unusual_Atmospheric_250.md', 'odd')]
TAGNAMES = ['enclosure', 'access', 'function', 'scale', 'era', 'light', 'occupancy', 'condition', 'climate', 'acoustic', 'materials', 'camera']
FIELD = re.compile(r'\*\*([^*]+?):\*\*')
def clean_phrase(t):
    t = t.replace(' — ', ', ').replace(' – ', ', ').replace('—', ', ').replace('–', '-').replace(':', ' -')
    t = t.strip().rstrip('.').strip()
    t = re.sub(r'\s+', ' ', t)
    return t
def split_commas(t):
    out, depth, cur = [], 0, ''
    for ch in t:
        if ch == '(': depth += 1
        if ch == ')': depth = max(0, depth - 1)
        if ch == ',' and depth == 0: out.append(cur); cur = ''
        else: cur += ch
    out.append(cur)
    return [clean_phrase(x) for x in out if clean_phrase(x) and not clean_phrase(x).lower().startswith(('none', 'n/a'))]
def split_semi(t): return [clean_phrase(x) for x in t.split(';') if clean_phrase(x)]
def parse(path, cat):
    L = open(path, encoding='utf-8').read().split('\n'); recs = []; head = None; n = 0
    for i, l in enumerate(L):
        m = re.match(r'#{2,4} (?:\d+[a-z]?\. )?(.+)', l)
        if m: head = m.group(1).strip()
        if l.startswith('**Items:**'):
            parts = FIELD.split(l); f = {}
            for j in range(1, len(parts) - 1, 2): f[parts[j].strip().lower()] = parts[j + 1].strip()
            tags = None
            for k in range(i + 1, min(i + 8, len(L))):
                if L[k].startswith('Tags:'): tags = [x.strip() for x in L[k][5:].split('|')]; break
            n += 1; recs.append(dict(cat=cat, n=n, title=head, f=f, tags=tags))
    return recs
def article(t):
    return 'an' if t[:1].lower() in 'aeiou' else 'a'
def build(final=None):
    G = {}; allrecs = []
    for fn, cat in FILES:
        p = os.path.join(DOCS, fn)
        if os.path.exists(p): allrecs += parse(p, cat)
    count = {}; idx = {}; pool_counts = {'items': {}, 'furniture': {}, 'installed': {}, 'traces': {}, 'light': {}}
    for r in allrecs:
        s = slug(r['title'])[:44]; base = 'loc_%s_%s' % (r['cat'], s); c = count.get(base, 0); count[base] = c + 1
        r['id'] = base if c == 0 else '%s_%d' % (base, c + 1)
    for r in allrecs:
        f = r['f']; I = r['id']
        def get(*names):
            for nme in names:
                for k, v in f.items():
                    if k.startswith(nme): return v
            return ''
        items = split_commas(get('items')); furn = split_commas(get('furniture')); inst = split_commas(get('installed')); sig = split_commas(get('signature'))
        mat_raw = split_semi(get('materials')); light = split_semi(get('light')); trace = split_commas(get('human traces')); cond = split_semi(get('condition'))
        mats = [m for m in mat_raw[:1]]; pal = mat_raw[1:2]
        if not (items and furn and mats and light): continue
        title = r['title'][0].lower() + r['title'][1:]
        for key, vals in (('items', items), ('furniture', furn), ('installed', inst), ('signature', sig), ('materials', mats), ('palette', pal), ('light', light), ('traces', trace), ('condition', cond)):
            if vals: G['%s_%s' % (I, key)] = vals
        for k, vals in (('items', items), ('furniture', furn), ('installed', inst), ('traces', trace), ('light', light)):
            for v in vals: pool_counts[k][v] = pool_counts[k].get(v, 0) + 1
        clean = 'The place is %s %s. Its materials are __%s_materials__' % (article(title), title, I) + (', and the palette is __%s_palette__' % I if pal else '') + '. The light is __%s_light__.' % I
        if sig: clean += ' A distinguishing detail is __%s_signature__.' % I
        G['%s_clean' % I] = [clean]
        two = lambda key, n: ('__%s_%s__ and __%s_%s__' % (I, key, I, key)) if n >= 8 else '__%s_%s__' % (I, key)
        body = ' The loose items include %s. The furniture and equipment include %s.' % (two('items', len(items)), two('furniture', len(furn)))
        if inst: body += ' The built-in features include %s.' % two('installed', len(inst))
        if trace: body += ' Signs of people include __%s_traces__.' % I
        if cond: body += ' This version of the place is __%s_condition__.' % I
        body += ' The view is __loc_shot__.'
        G['%s_scene' % I] = ['__%s_clean__%s' % (I, body)]
        G['%s_scene_plus' % I] = ['__%s_scene__ Also here are __loc_anywhere_items__ and __loc_anywhere_traces__.' % I]
        idx.setdefault('all', []).append(I); idx.setdefault(r['cat'], []).append(I)
        if r['tags'] and len(r['tags']) >= 12:
            for nme, val in zip(TAGNAMES, r['tags']):
                for v in val.split(','):
                    v = slug(v.strip())
                    if v and v != 'varies': idx.setdefault('tag_%s_%s' % (nme, v), []).append(I)
    for k, v in pool_counts.items():
        shared = sorted([x for x, c in v.items() if c >= 2 and len(x) < 90])
        if shared: G['loc_anywhere_%s' % k] = shared
    for k, ids in idx.items():
        name = 'loc_scene' if k == 'all' else ('loc_%s_scene' % k if not k.startswith('tag_') else 'loc_%s' % k)
        G[name] = ['__%s_scene__' % i for i in ids]
        if k == 'all': G['loc_clean'] = ['__%s_clean__' % i for i in ids]; G['loc_scene_plus'] = ['__%s_scene_plus__' % i for i in ids]
        if k in ('home', 'ext', 'work', 'circ', 'bath', 'food', 'odd'): G['loc_%s_clean' % k] = ['__%s_clean__' % i for i in ids]
    G['loc_shot'] = ['a wide establishing view of the whole space', 'a close view on the most telling detail', 'a view through the doorway from the next room', 'a low angle near the floor looking along the space', 'a corner view in three-quarter perspective', 'a symmetrical straight-on view', 'a high angle looking down into the space']
    for c in ('home', 'ext', 'work', 'circ', 'bath', 'food', 'odd'):
        if c in idx: G['loc_%s_scene_plus' % c] = ['__%s_scene_plus__' % i for i in idx[c]]
    G['v75_loc_entry_points'] = ['loc_scene', 'loc_scene_plus', 'loc_clean'] + ['loc_%s_scene' % k for k in ('home', 'ext', 'work', 'circ', 'bath', 'food', 'odd') if k in idx]
    return G
if __name__ == '__main__':
    G = build(); print(len(G), 'files;', len(G.get('loc_scene', [])), 'locations')
