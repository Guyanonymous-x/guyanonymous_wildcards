"""v48: rooms and locations. room_<type>_prompt_brief / room_<type>_prompt_full for 35 room types (house, office, public, gyms, weight-training gyms, pools, yoga studios, saunas and more). Rooms describe the space only (no people, no poses) and call the furniture, object and gear files by reference. Idempotent."""
import os, re, sys, glob, random, zlib
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from paths import FINAL
import v44_build as B4, v46_build as B6, v48_data as D
_wr = B6._wr
def an(w): return ('an ' if w[0].lower() in 'aeiou' else 'a ') + w
def build():
    G = {}
    for k, rows in D.GEAR.items(): G.update(B6.support('gear_' + k, rows, k))
    G['room_size'] = D.SIZE; G['room_floor'] = D.FLOOR; G['room_walls'] = D.WALLS; G['room_light'] = D.LIGHT; G['room_condition'] = D.COND; G['room_style'] = D.STYLE
    briefs, fulls = [], []
    for key, (label, br, fu) in D.R.items():
        b = f'The room is {an(label)}, __room_size__, in the __room_style__ style, with __{br[0]}__ and __{br[1]}__.'
        G[f'room_{key}_prompt_brief'] = [b]
        lines = []
        for v in range(6):
            items = fu[:]; random.Random(zlib.crc32(f'{key}{v}'.encode())).shuffle(items)
            s = [f'The room is {an(label)}. It is __room_size__ and in the __room_style__ style, and it is __room_condition__.', 'The floor is __room_floor__ and the walls are __room_walls__.', 'The light comes from __room_light__.']
            s += [('It contains ' if i == 0 else ('Nearby there is ' if i % 2 else 'Also in the room there is ')) + f'__{it}__.' for i, it in enumerate(items)]
            lines.append(' '.join(s))
        G[f'room_{key}_prompt_full'] = lines
        briefs.append(f'__room_{key}_prompt_brief__'); fulls.append(f'__room_{key}_prompt_full__')
    G['room_prompt_brief'] = briefs; G['room_prompt_full'] = fulls
    G['room_types'] = [v[0] for v in D.R.values()]
    G['v48_entry_points'] = ['__room_prompt_brief__', '__room_prompt_full__']
    return G
def run(final):
    G = build()
    for n, l in G.items(): _wr(final, n, l)
    print('v48:', len(G), 'files'); return G
def export_aoo(out, prefix='aoo_'):
    G = build(); names_ = set(G); ref = re.compile(r'__([A-Za-z0-9_\-/]+)__'); n = 0
    for name, lines in G.items():
        keep = list(dict.fromkeys(ref.sub(lambda m: '__' + prefix + m.group(1) + '__' if (m.group(1) in names_ or os.path.exists(os.path.join(out, prefix + m.group(1) + '.txt'))) else m.group(0), l) for l in lines))
        if not name.endswith(('brief', 'full')) and 'entry_points' not in name and not name.endswith('prompt'): random.Random(zlib.crc32(name.encode())).shuffle(keep)
        _wr(out, prefix + name, keep); n += 1
    return n
if __name__ == '__main__':
    a = [x for x in sys.argv[1:] if os.path.isdir(x)]; run(os.path.abspath(a[0]) if a else FINAL)
