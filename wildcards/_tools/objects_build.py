"""Builds the object / furniture / room-item files (each up to 2,500 lines, mostly unique) and the enlarged acc_props (held items) and env_props.
Catalogues are in objects_data.py.  The 28 original options of acc_props.txt and env_props.txt (data/*_original.txt) are kept once each.
Files: obj_furniture, obj_room_items, obj_table_items, obj_outdoor_items, obj_toys, obj_held_items, obj_scene_interior, obj_scene_exterior, acc_props, env_props."""
import os, sys, random
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from paths import wc_dir, DATA
from objects_data import *
WC = wc_dir(); N = 2500
def write(name, lines, seed):
    random.Random(seed).shuffle(lines)
    open(os.path.join(WC, name + '.txt'), 'w', encoding='utf8', newline='\n').write('\n'.join(lines) + '\n')
def uniq_fill(maker, n, seed, start=()):
    R = random.Random(seed); out = list(start); seen = set(out); tries = 0
    while len(out) < n and tries < n * 60:
        tries += 1; x = maker(R)
        if x not in seen: seen.add(x); out.append(x)
    return out
def orig(name): return list(dict.fromkeys(l.strip() for l in open(os.path.join(DATA, name), encoding='utf8') if l.strip()))
furn = lambda R: f"{art(R.choice(F_STYLE) + ' ' + R.choice(F_TYPE))} {R.choice(F_PLACE)}"
room = lambda R: f"{art(R.choice(R_ITEM))} {R.choice(R_STATE)}" if R.random() < .8 else f"{art(R.choice(R_ITEM))} and {art(R.choice(R_ITEM))} {R.choice(R_STATE)}"
table = lambda R: R.choice(T_ITEM) if R.random() < .55 else f"{R.choice(T_ITEM)} and {R.choice(T_ITEM)}"
outd = lambda R: R.choice(O_ITEM) if R.random() < .6 else f"{R.choice(O_ITEM)} and {R.choice(O_ITEM)}"
def toy(R):
    t = R.choice(TOYS); return t if R.random() < .4 else f"{t} {R.choice(['on the floor','on a shelf','on the ground','in a corner','on a chair','in a basket','on a rug','on a doorstep','beside a bag'])}"
def held(R):
    adj = R.choice(H_ADJ); it = R.choice(H_ITEM); a = art(adj + it) if adj else art(it)
    if it.startswith(('pair of', 'bunch of', 'stack of', 'bag of', 'box of', 'bowl of', 'cup of', 'plate of', 'pot of', 'pile of', 'sack of', 'tray of', 'basket of', 'handful of', 'string of', 'armful of', 'roll of')): a = ("a " + adj + it) if adj else "a " + it
    return f"{a} {R.choice(H_VERB)}"
def prop_pair(R): return f"{R.choice(F_STYLE)} {R.choice(F_TYPE)} and {art(R.choice(R_ITEM))}"
def env_prop(R):
    r = R.random()
    if r < .4: return f"{R.choice(F_STYLE)} {R.choice(F_TYPE)} and {R.choice(R_ITEM)}"
    if r < .7: return f"{R.choice(R_ITEM)} and {R.choice(R_ITEM)}"
    if r < .85: return f"{R.choice(O_ITEM).replace('a ', '', 1)} and {R.choice(O_ITEM).replace('a ', '', 1)}"
    return f"{R.choice(F_STYLE)} {R.choice(F_TYPE)} with {R.choice(T_ITEM)}"
if __name__ == '__main__':
    write('obj_furniture', uniq_fill(furn, N, 1), 11); write('obj_room_items', uniq_fill(room, N, 2), 12)
    write('obj_table_items', uniq_fill(table, N, 3), 13); write('obj_outdoor_items', uniq_fill(outd, N, 4), 14)
    write('obj_toys', uniq_fill(toy, N, 5, start=list(TOYS)), 15)
    write('acc_props', uniq_fill(held, N, 6, start=orig('acc_props_original.txt')), 16)
    write('obj_held_items', uniq_fill(held, N, 7), 17)
    write('env_props', uniq_fill(env_prop, N, 8, start=orig('env_props_original.txt')), 18)
    write('obj_scene_interior', uniq_fill(lambda R: f"{furn(R)}, {room(R)} and {table(R)}", N, 9), 19)
    write('obj_scene_exterior', uniq_fill(lambda R: f"{outd(R)}, {R.choice(O_ITEM)} and {room(R)}", N, 10), 20)
    print('object files written')
