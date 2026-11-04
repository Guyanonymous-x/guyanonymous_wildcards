"""v40: true-purse family (purses only), haute couture and silly fashion, outerwear, extreme-weather gear, diving gear, trades tools and equipment. All descriptions are of items only."""
import os, re, sys, glob, random, zlib
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from paths import FINAL
import v40_data_a as A, v40_data_b as B, v40_data_c as C
def RR(*k): return random.Random(zlib.crc32('|'.join(map(str, k)).encode()))
def cap(s): return s[0].upper() + s[1:]
def art(n):
    m = n.split(' with ')[0]
    if m.endswith('s') and not m.endswith(('ss', 'glass')) and not m.endswith('us'): return 'a pair of ' + n
    return ('an ' if n[0].lower() in 'aeiou' else 'a ') + n
COL = A.COUT_COL
CLOTHCOL = ["black", "navy", "charcoal", "ivory", "forest green", "burgundy", "camel", "olive", "grey", "tan", "cream", "mustard yellow", "dark brown", "rust red", "teal", "bright red", "white", "sky blue", "plum", "stone"]
PURSECOL = ["black", "red", "navy", "tan", "cream", "burgundy", "green", "pale pink", "mustard", "grey", "gold", "silver", "brown", "turquoise"]
CW = set(CLOTHCOL + PURSECOL + COL + ['yellow','orange','blue','red','silver','gold','brown','green','pink','white','black','grey'])
def group(pre, items, colours, n_per=6, verb='Made of', short_verb='made of', shortfmt=None):
    """items: (name, desc, mats[, kind]). Returns dict of files."""
    lines, shorts, types, mats = [], [], [], set()
    for it in items:
        name, desc, ms = it[0], it[1], it[2]; types.append(f"{name}, which is {desc}")
        combos = [(m, c) for m in ms for c in (['' if any(w in m.lower().split() for w in CW) else c for c in (colours or [''])])]
        combos = list(dict.fromkeys(combos))
        R = RR(pre, name); R.shuffle(combos)
        for m, c in combos[:n_per]:
            mats.add(m)
            col = f", in {c}" if c else ''
            lines.append(f"{cap(name)}, {desc}. {verb} {m}{col}.")
            shorts.append(shortfmt.format(a=art(name), m=m, c=col) if shortfmt else f"{art(name)} {short_verb} {m}{col}")
    G = {pre: sorted(set(lines)), f'{pre}_type': types, f'{pre}_short': sorted(set(shorts)), f'{pre}_material': sorted(mats)}
    return G
def build():
    G = {}
    # purses
    G.update(group('acc_purse', A.PURSE, PURSECOL, 8))
    G['acc_purse_prompt'] = ['__acc_purse__', 'Carrying __acc_purse_short__.']
    # couture
    G.update(group('clothing_couture_haute', A.COUTURE, None, 5))
    G['clothing_couture_haute_prompt'] = ['__clothing_couture_haute__', 'Wearing a couture creation, __clothing_couture_haute_short__.']
    G.update(group('clothing_couture_silly', A.FUNNY, None, 5))
    G['clothing_couture_silly_prompt'] = ['__clothing_couture_silly__', 'Wearing __clothing_couture_silly_short__.']
    G['clothing_couture_prompt'] = ['__clothing_couture_haute_prompt__', '__clothing_couture_silly_prompt__']
    # outerwear
    G.update(group('clothing_outerwear', B.OUTER, CLOTHCOL, 6))
    G['clothing_outerwear_prompt'] = ['__clothing_outerwear__', 'Wearing __clothing_outerwear_short__.']
    G.update(group('clothing_weather_extreme', B.WEATHER, CLOTHCOL, 4))
    G['clothing_weather_extreme_prompt'] = ['__clothing_weather_extreme__', 'Equipped with __clothing_weather_extreme_short__.']
    G.update(group('clothing_diving', B.DIVE, ["black", "navy", "yellow", "orange", "grey", "blue", "red", "silver"], 4))
    G['clothing_diving_prompt'] = ['__clothing_diving__', 'Equipped with __clothing_diving_short__.']
    # trades
    allt = []; kinds = {'hand': [], 'power': [], 'gear': []}; tp = []
    for trade, rows in C.TRADES.items():
        pre = f'tool_{trade}'; items = [(n, d, m) for n, d, m, k in rows]
        G.update(group(pre, items, None, 4, 'Made from', shortfmt='{a} ({m})'))
        G[f'{pre}_prompt'] = [f'__{pre}__', f'Holding __{pre}_short__.']
        tp.append(f'__{pre}_prompt__')
        for n, d, m, k in rows:
            allt.append((n, d, m)); kinds[k].append((n, d, m))
    TF = dict(verb='Made from', shortfmt='{a} ({m})')
    G.update(group('tool_all', allt, None, 3, **TF))
    for k, rows in kinds.items(): G.update(group(f'tool_{k}', rows, None, 3, **TF))
    G['tool_prompt'] = tp
    G['tool_trades'] = [t.replace('_', ' ') for t in C.TRADES]
    G['v40_entry_points'] = ['__acc_purse_prompt__', '__clothing_couture_prompt__', '__clothing_outerwear_prompt__', '__clothing_weather_extreme_prompt__', '__clothing_diving_prompt__', '__tool_prompt__']
    return G
def _write(folder, name, lines): open(os.path.join(folder, name + '.txt'), 'w', encoding='utf8', newline='\n').write('\n'.join(lines) + '\n')
def run(final):
    for f in glob.glob(os.path.join(final, 'acc_purse*.txt')): os.remove(f)
    G = build()
    for n, l in G.items(): _write(final, n, l)
    print('v40:', len(G), 'files'); return G
def export_aoo(out, prefix='aoo_'):
    for f in glob.glob(os.path.join(out, prefix + 'acc_purse*.txt')): os.remove(f)
    G = build(); names_ = set(G); ref = re.compile(r'__([A-Za-z0-9_\-/]+)__'); n = 0
    for name, lines in G.items():
        keep = list(dict.fromkeys(ref.sub(lambda m: '__' + prefix + m.group(1) + '__' if m.group(1) in names_ else m.group(0), l) for l in lines))
        if not name.endswith('prompt') and 'entry_points' not in name: random.Random(zlib.crc32(name.encode())).shuffle(keep)
        _write(out, prefix + name, keep); n += 1
    return n
if __name__ == '__main__':
    a = [x for x in sys.argv[1:] if os.path.isdir(x)]; run(os.path.abspath(a[0]) if a else FINAL)
