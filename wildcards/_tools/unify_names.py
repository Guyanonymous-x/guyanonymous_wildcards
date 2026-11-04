"""Unifies wildcard file names under category prefixes and rewrites every __reference__.
Usage: python unify_names.py <folder> [aoo_]   (the optional second argument is the file prefix used by the All Options Once edition)
Scheme (category_subject_...):  garment_*->clothing_garment_*, uniform_*->clothing_uniform_*, onesie_*->clothing_onesie_*, period_*->clothing_period_*,
clth_*->clothing_part_*, outfit_*->clothing_outfit_*, halloween_*->costume_halloween_*, weapon_*->obj_weapon_*, armor_*->obj_armor_*, surfboard_*->obj_surfboard_*.
acc_* (accessories, footwear acc_shoe_*), f_* / m_* (person prompts) and the rest stay as they are.  Writes filename_changes.txt (old -> new)."""
import os, re, sys
RULES = [('garment_', 'clothing_garment_'), ('uniform_', 'clothing_uniform_'), ('onesie_', 'clothing_onesie_'), ('period_', 'clothing_period_'), ('clth_', 'clothing_part_'), ('outfit_', 'clothing_outfit_'), ('halloween_', 'costume_halloween_'), ('weapon_', 'obj_weapon_'), ('armor_', 'obj_armor_'), ('surfboard_', 'obj_surfboard_')]
def newname(base, pre=''):
    b = base[len(pre):] if pre and base.startswith(pre) else base
    for a, c in RULES:
        if b.startswith(a): return pre + c + b[len(a):]
    return base
def main(folder, pre=''):
    files = [f[:-4] for f in os.listdir(folder) if f.endswith('.txt') and f != 'filename_changes.txt']
    mp = {f: newname(f, pre) for f in files}; mp = {a: b for a, b in mp.items() if a != b}
    taken = set(files) - set(mp); clash = [b for b in mp.values() if b in taken]
    assert not clash and len(set(mp.values())) == len(mp), clash[:5]
    ref = re.compile(r'__([A-Za-z0-9_\-/]+)__'); sub = lambda m: '__' + mp.get(m.group(1), m.group(1)) + '__'
    for f in files:
        p = os.path.join(folder, f + '.txt'); t = open(p, encoding='utf8').read(); n = ref.sub(sub, t)
        if n != t: open(p, 'w', encoding='utf8', newline='\n').write(n)
    for a, b in mp.items(): os.rename(os.path.join(folder, a + '.txt'), os.path.join(folder, b + '.txt'))
    open(os.path.join(folder, 'filename_changes.txt'), 'w', encoding='utf8', newline='\n').write('\n'.join(f'{a}.txt -> {b}.txt' for a, b in sorted(mp.items())) + '\n')
    print(f'renamed {len(mp)} files in {folder}'); return mp
if __name__ == '__main__': main(os.path.abspath(sys.argv[1]), sys.argv[2] if len(sys.argv) > 2 else '')
