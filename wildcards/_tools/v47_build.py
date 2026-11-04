"""v47: furniture, household and office objects, bottles and closures, perfume bottles and samplers, liquids. Objects are described alone (no rooms, no people, no poses); rooms (v48) call them. Idempotent."""
import os, re, sys, glob, random, zlib
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from paths import FINAL
import v44_build as B4, v46_build as B6, v47_data as D
def build():
    G = {}; fp = []; hp = []
    for g, rows in D.FURN.items():
        pre = f'furn_{g}'; G.update(B6.support(pre, rows, g)); fp.append(f'__{pre}_prompt__')
    fp.append('__seat_prompt__'); G['furn_prompt'] = fp
    allf = [r for rows in D.FURN.values() for r in rows]; G.update(B4.grp('furn_all', allf, 3)); G['furn_all_prompt'] = ['__furn_all__']
    for g, rows in D.HOME.items():
        pre = ('office_' + g.replace('office_', '')) if g == 'office_supplies' else f'home_{g}'
        pre = 'office_supplies' if g == 'office_supplies' else pre
        G.update(B6.support(pre, rows, g)); hp.append(f'__{pre}_prompt__')
    G['home_prompt'] = hp
    allh = [r for rows in D.HOME.values() for r in rows]; G.update(B4.grp('home_all', allh, 3)); G['home_all_prompt'] = ['__home_all__']
    G.update(B6.support('bottle', D.BOTTLE, 'bottle')); G.update(B6.support('closure', D.CLOSURE, 'closure')); G.update(B6.support('perfume', D.PERFUME, 'perfume'))
    # liquids
    for k, v in D.LIQ.items(): G[f'liquid_{k}'] = [x[0].upper() + x[1:] + '.' for x in v]
    L = D.LIQLOOK; R = random.Random(4701)
    G['liquid_look'] = [f'{"An" if False else "A"} {R.choice(L["colour"])} liquid that is {R.choice(L["transparency"])} and {R.choice(L["viscosity"])}, {R.choice(L["extras"])}.' for _ in range(160)]
    G['liquid_look_phrase'] = [x[0].lower() + x[1:].rstrip('.') for x in G['liquid_look']]
    G['liquid_prompt'] = ['__liquid_look__', '__liquid_liquor__', '__liquid_medical__', '__liquid_strange__']
    G['liquid_in_bottle'] = ['__bottle_phrase__, filled with __liquid_look_phrase__, and closed with __closure_phrase__.']
    G['liquid_in_perfume_bottle'] = ['__perfume_phrase__, filled with __liquid_look_phrase__.']
    G['v47_entry_points'] = ['__furn_prompt__', '__furn_all_prompt__', '__home_prompt__', '__home_all_prompt__', '__office_supplies_prompt__', '__bottle_prompt__', '__closure_prompt__', '__perfume_prompt__', '__liquid_prompt__', '__liquid_in_bottle__', '__liquid_in_perfume_bottle__']
    return G
_wr = B6._wr
def run(final):
    G = build()
    for n, l in G.items(): _wr(final, n, l)
    print('v47:', len(G), 'files'); return G
def export_aoo(out, prefix='aoo_'):
    G = build(); names_ = set(G); ref = re.compile(r'__([A-Za-z0-9_\-/]+)__'); n = 0
    for name, lines in G.items():
        keep = list(dict.fromkeys(ref.sub(lambda m: '__' + prefix + m.group(1) + '__' if (m.group(1) in names_ or os.path.exists(os.path.join(out, prefix + m.group(1) + '.txt'))) else m.group(0), l) for l in lines))
        if not name.endswith('prompt') and 'entry_points' not in name: random.Random(zlib.crc32(name.encode())).shuffle(keep)
        _wr(out, prefix + name, keep); n += 1
    return n
if __name__ == '__main__':
    a = [x for x in sys.argv[1:] if os.path.isdir(x)]; run(os.path.abspath(a[0]) if a else FINAL)
