"""v56 - grammar pass (a/an in every library line) and the optional folder ('browse') edition."""
import os, re, sys, shutil, glob
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from paths import FINAL
REF = re.compile(r'__([A-Za-z0-9_\-/]+)__')
VOW_A = re.compile(r'\b([Aa]) (?=[aeiouAEIOU][a-z]{2})(?!uni|use|usu|one|eur|ubi|oun)')
CON_AN = re.compile(r'\b([Aa]n) (?=[bcdfgjklmnpqrstvwxzBCDFGJKLMNPQRSTVWXZ][a-z]{2})(?!hour|honest|heir|honou?r|Hour|Honest)')
def fix_line(l):
    if '__' in l:
        parts = re.split(r'(__[A-Za-z0-9_\-/]+__)', l)
        return ''.join(p if p.startswith('__') and p.endswith('__') and len(p) > 4 else fix_text(p) for p in parts)
    return fix_text(l)
def fix_text(t):
    t = VOW_A.sub(lambda m: m.group(1) + 'n ', t)
    t = CON_AN.sub(lambda m: m.group(1)[0] + ' ', t)
    return t
def run(final):
    n = lines = 0
    for p in glob.glob(os.path.join(final, '*.txt')):
        if os.path.basename(p) in ('README.txt', 'CHANGELOG.txt'): continue
        old = open(p, encoding='utf8').read().split('\n'); new = [fix_line(l) for l in old]
        c = sum(a != b for a, b in zip(old, new))
        if c: open(p, 'w', encoding='utf8', newline='\n').write('\n'.join(new)); n += 1; lines += c
    print('v56 a/an pass:', n, 'files,', lines, 'lines'); return n, lines
def export_aoo(out, prefix='aoo_'): return 0
FAMILIES = [('people', ('any_', 'f_', 'm_', 'age', 'demo_', 'names', 'countries', 'prompt_')), ('clothing', ('clothing_', 'outfit_', 'costume_', 'occasion_', 'badtaste_', 'onesie', 'uniform')), ('accessories', ('acc_', 'chastity_')),
 ('body', ('body_', 'skin_', 'hair_', 'wx_', 'bt_', 'tat')), ('pose_camera_style', ('pose_', 'cam_', 'lite_', 'photostyle_', 'illustration_', 'art_')), ('places', ('setting_', 'room_', 'world_', 'env_', 'furn_', 'home_', 'comp_')),
 ('groups', ('group_', 'grp_')), ('objects', ('obj_', 'tool_', 'gear_', 'sport_')), ('animals', ('animal_',)), ('nature_buildings_vehicles', ('plant_', 'arch_', 'veh_', 'machinery', 'nature_')), ('food_tableware', ('food_', 'ware_', 'table_', 'meal_'))]
def family(n):
    n = n[4:] if n.startswith('aoo_') else n
    for f, pre in FAMILIES:
        if n.startswith(pre): return f
    return 'other'
def browse(src, out):
    """folder edition. References become __family/name__ . Returns (files, folders)."""
    shutil.rmtree(out, ignore_errors=True); names = {os.path.basename(p)[:-4] for p in glob.glob(os.path.join(src, '*.txt'))}
    fam = {n: family(n) for n in names}
    for p in glob.glob(os.path.join(src, '*.txt')):
        n = os.path.basename(p)[:-4]
        if n in ('README', 'CHANGELOG'): continue
        d = os.path.join(out, fam[n]); os.makedirs(d, exist_ok=True)
        t = REF.sub(lambda m: '__%s/%s__' % (fam[m.group(1)], m.group(1)) if m.group(1) in fam else m.group(0), open(p, encoding='utf8').read())
        open(os.path.join(d, n + '.txt'), 'w', encoding='utf8', newline='\n').write(t)
    return len(names), len({v for v in fam.values()})
if __name__ == '__main__':
    a = [x for x in sys.argv[1:] if os.path.isdir(x)]; run(os.path.abspath(a[0]) if a else FINAL)
