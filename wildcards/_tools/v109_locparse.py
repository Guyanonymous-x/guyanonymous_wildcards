"""v109 - parser for the complete Location Inventory export (docs/location_inventory/Location_Inventory_complete.md, pandoc markdown of the
350 Locations document). Returns one dict per record: cat, title, fields {name: text}, tags. 'Dimensions & fit' is read but never used (user, 2026-11-06).
The first tab (short 350-record overview) is skipped because every one of its records has a full-depth version in a later tab."""
import os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from famlib import slug
SRC = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), 'docs', 'location_inventory', 'Location_Inventory_complete.md')
if not os.path.exists(SRC): SRC = '/home/claude/w/docs/location_inventory/Location_Inventory_complete.md'
TABS = [('Location Inventory: 350 Spaces', None), ('Home Interior', 'home'), ('Home Exterior', 'ext'), ('Workplace', 'work'), ('Bathrooms', 'bath'),
        ('Food & Hospitality (expanded)', 'food'), ('Circulation', 'circ'), ('Retail', 'retail'), ('Culture', 'culture'), ('Civic', 'civic'),
        ('Transportation', 'transport'), ('Outdoor', 'outdoor'), ('Healthcare', 'health'), ('Unusual', 'odd'), ('Vehicle Interiors', 'vehicle'),
        ('Maintenance', 'depot'), ('Alternative', 'dwelling'), ('21 Secret', 'secret'), ('22 Vice', 'vice'), ('23.', 'wealth'), ('24.', 'edu')]
CATS = [c for _, c in TABS if c]
FIELD = re.compile(r'\*\*([A-Z][^*]{1,48}?):\*\*')
def tab_cat(h):
    for pre, c in TABS:
        if h.startswith(pre): return c, True
    return None, False
def paragraphs(lines):
    out, cur = [], []
    for l in lines:
        if not l.strip():
            if cur: out.append(' '.join(cur)); cur = []
        else: cur.append(l.strip())
    if cur: out.append(' '.join(cur))
    return out
def parse(path=SRC):
    L = open(path, encoding='utf-8').read().split('\n')
    recs, cat, head = [], None, None
    starts = [i for i, l in enumerate(L) if l.startswith('# ') and not l.startswith('# Contents')]
    for n, s in enumerate(starts):
        e = starts[n + 1] if n + 1 < len(starts) else len(L)
        cat, known = tab_cat(L[s][2:].strip())
        if not known: raise ValueError('unknown tab: ' + L[s])
        if cat is None: continue
        paras = paragraphs(L[s + 1:e]); head = None; cur = None
        for p in paras:
            m = re.match(r'#{2,4} (?:\d+[a-z]?\. )?(.+)', p)
            if m: head = re.sub(r'\s*\{#.*\}$', '', m.group(1)).strip(); continue
            if p.startswith('**Items:**'):
                cur = dict(cat=cat, title=head, f={}, tags=None); recs.append(cur)
            if cur is None: continue
            if p.startswith('**'):
                parts = FIELD.split(p)
                for j in range(1, len(parts) - 1, 2): cur['f'][parts[j].strip().lower()] = parts[j + 1].strip()
            elif p.startswith('Tags:'):
                cur['tags'] = [x.strip() for x in p[5:].split('|')]
    count = {}
    ALIAS = {'loc_circ_multi_story_parking_lot_ramp': 'loc_circ_multi_storey_car_park_ramp', 'loc_ext_fence_line_with_neighbor': 'loc_ext_fence_line_with_neighbour',
             'loc_home_front_parlor_rarely_used': 'loc_home_front_parlour_rarely_used', 'loc_odd_abandoned_hospital_operating_room': 'loc_odd_abandoned_hospital_operating_theatre',
             'loc_odd_deserted_gas_station': 'loc_odd_deserted_petrol_station', 'loc_work_call_center_floor': 'loc_work_call_centre_floor',
             'loc_work_data_center_hall': 'loc_work_data_centre_hall', 'loc_work_site_office_site_office': 'loc_work_site_office_portakabin',
             'loc_work_staff_parking_lot': 'loc_work_staff_car_park'}  # v75 pilot IDs kept where the document's titles changed spelling
    for r in recs:
        base = 'loc_%s_%s' % (r['cat'], slug(r['title'])[:44]); c = count.get(base, 0); count[base] = c + 1
        r['id'] = base if c == 0 else '%s_%d' % (base, c + 1)
        r['id'] = ALIAS.get(r['id'], r['id'])
    return recs
if __name__ == '__main__':
    R = parse(); from collections import Counter
    print(len(R), 'records', Counter(r['cat'] for r in R))
    print(Counter(k for r in R for k in r['f']).most_common(20))
