"""v46: setting / pose / interaction separation. Seat, lying-surface and leaning-support wildcards; pose files by support (free, sitting on the ground, sitting on a seat, lying, leaning, floating); interaction files (two, three, person with object); setting files; audit report. Person and object files stay free of setting, pose and interaction text. Idempotent."""
import os, re, sys, glob, random, zlib
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from paths import FINAL
import v44_build as B4, v46_data as D
from v40_build import art
def cap(s): return s[0].upper() + s[1:]
def strip_s(t, noun='the seat'): return t.replace('{S}', noun)
def support(pre, rows, label):
    G = B4.grp(pre, rows, 5)
    ph = []
    for name, desc, mats in rows:
        for m in mats[:3]: ph.append(f'{art(name)}, which is {desc}, made of {m}')
    G[pre + '_phrase'] = ph; G[pre + '_prompt'] = [f'__{pre}__']
    return G
def build():
    G = {}
    G.update(support('seat', D.SEAT, 'seat')); G.update(support('surface_lie', D.LIE, 'surface')); G.update(support('support_lean', D.LEAN, 'support'))
    def pose(name, items, key=None, noun=None):
        nn = {'seat': 'the seat', 'surface_lie': 'the surface', 'support_lean': 'the support'}.get(key, 'the seat')
        if key is None: G[name] = [cap(strip_s(t)) + '.' for t in items]; return
        full, short = [], []
        for t in items:
            p = cap(strip_s(t, nn))
            full.append(f'{p}. {noun} is __{key}_phrase__.'); short.append(f'{p}. {noun} is __{key}_short__.')
        G[name] = full; G[name + '_short'] = short
    free = sorted({l.strip() for l in open(os.path.join(FINAL, 'pose_action.txt'), encoding='utf8') if l.strip() and not re.search(r'sit|seat|perch|squat|crouch|kneel|lying|lie\b|recline|sprawl|lean|against|propp|rest(ing)? on|chair|stool|bench|sofa|couch|bed\b|table|desk|ladder|stair|step|horse|bike|bicycle|rail|counter|window|door|swing|car\b|boat|rock|wall|fence|log\b|lounging|float|swim|dive|jump|leap', l, re.I)})
    free = [cap(x.rstrip('.')) + '.' for x in free]
    G['pose_free'] = free
    pose('pose_sitting', D.SIT_GROUND); pose('pose_sitting_w_seat', D.SIT_SEAT, 'seat', 'The seat')
    pose('pose_lying', D.LIE_GROUND); pose('pose_lying_w_surface', D.LIE_SURF, 'surface_lie', 'The surface')
    pose('pose_leaning', D.LEAN_FREE); pose('pose_leaning_w_support', D.LEAN_SUP, 'support_lean', 'The support')
    pose('pose_floating', D.FLOAT)
    G['pose_prompt'] = ['__pose_free__'] * 6 + ['__pose_sitting__', '__pose_sitting_w_seat__', '__pose_lying__', '__pose_lying_w_surface__', '__pose_leaning__', '__pose_leaning_w_support__']
    G['pose_prompt_no_support'] = ['__pose_free__'] * 4 + ['__pose_sitting__', '__pose_lying__', '__pose_leaning__']
    # interactions
    G['interact_two'] = [cap(t) + '.' for t in D.TWO]; G['interact_three'] = [cap(t) + '.' for t in D.THREE]; G['interact_object'] = [cap(t) + '.' for t in D.OBJ]
    G['interact_two_w_seat'] = [f'{cap(strip_s(t))}. The seat is __seat_phrase__.' for t in D.TWO_SEAT]; G['interact_three_w_seat'] = [f'{cap(strip_s(t))}. The seat is __seat_phrase__.' for t in D.THREE_SEAT]
    G['interact_two_prompt'] = ['__interact_two__', '__interact_two_w_seat__']; G['interact_three_prompt'] = ['__interact_three__', '__interact_three_w_seat__']
    # settings (place + light, no people, no poses)
    env = sorted({l.strip() for l in open(os.path.join(FINAL, 'env_setting.txt'), encoding='utf8') if l.strip()})
    ins = [l for l in env if re.search(r'interior|indoor|room|cafe|café|shop|studio|library|kitchen|hall|gallery|museum|church|temple|office|bar\b|restaurant|gym|hospital|school|station|mall|theatre|theater|lobby|bedroom|apartment|loft|cabin|bakery|clinic|workshop|warehouse|spa|ballroom|bank', l, re.I)]
    out = [l for l in env if l not in ins]
    G['setting_interior_place'] = ins; G['setting_exterior_place'] = out
    G['setting_interior'] = ['The setting is __setting_interior_place__, __scene_arch_light__.']
    G['setting_exterior'] = ['The setting is __setting_exterior_place__, __scene_landscape_light__. The weather is __env_weather__.']
    G['setting_prompt'] = ['__setting_interior__', '__setting_exterior__']
    G['v46_entry_points'] = ['__pose_prompt__', '__pose_prompt_no_support__', '__interact_two_prompt__', '__interact_three_prompt__', '__interact_object__', '__setting_prompt__', '__seat_prompt__', '__surface_lie_prompt__', '__support_lean_prompt__']
    return G
def _wr(folder, name, lines): open(os.path.join(folder, name + '.txt'), 'w', encoding='utf8', newline='\n').write('\n'.join(lines) + '\n')
AUD = re.compile(r'\b(standing|sitting|seated|lying|leaning|kneeling|walking|pose[sd]?|posing|studio|backdrop|background|lighting|lit by|sunlight|window light|outdoors?|indoors?|street|room|beach|forest)\b', re.I)
def audit(final):
    rows = []
    for f in sorted(glob.glob(os.path.join(final, '*.txt'))):
        n = os.path.basename(f)[:-4]
        if not re.match(r'(f|m|any)_(?!create_)|age\d|bt_|acc_|clothing_|obj_|costume_|tattoo_|body_', n) or n.startswith(('pose_', 'setting_', 'interact_')): continue
        hit = 0; tot = 0; ex = ''
        for l in open(f, encoding='utf8'):
            if not l.strip(): continue
            tot += 1
            if AUD.search(l): hit += 1; ex = ex or l.strip()[:100]
        if hit: rows.append((hit, tot, n, ex))
    rows.sort(reverse=True)
    return rows
def run(final):
    G = build()
    for n, l in G.items(): _wr(final, n, l)
    # old two-line setting prompts now point to the new setting files
    _wr(final, 'prompt_setting_exterior', ['__setting_exterior__']); _wr(final, 'prompt_setting_interior', ['__setting_interior__'])
    rows = audit(final); os.makedirs(os.path.join(HERE, 'audit'), exist_ok=True)
    open(os.path.join(HERE, 'audit', 'AUDIT_setting_pose_v46.txt'), 'w', encoding='utf8').write('Files that still contain setting, lighting, pose or interaction words (hits / non-blank lines / example)\n' + '\n'.join(f'{h}\t{t}\t{n}\t{e}' for h, t, n, e in rows[:400]) + '\n')
    print('v46:', len(G), 'files; audit rows', len(rows)); return G
def export_aoo(out, prefix='aoo_'):
    G = build(); names_ = set(G); ref = re.compile(r'__([A-Za-z0-9_\-/]+)__'); n = 0
    for name, lines in G.items():
        keep = list(dict.fromkeys(ref.sub(lambda m: '__' + prefix + m.group(1) + '__' if (m.group(1) in names_ or os.path.exists(os.path.join(out, prefix + m.group(1) + '.txt'))) else m.group(0), l) for l in lines))
        if not name.endswith('prompt') and 'entry_points' not in name: random.Random(zlib.crc32(name.encode())).shuffle(keep)
        _wr(out, prefix + name, keep); n += 1
    return n
if __name__ == '__main__':
    a = [x for x in sys.argv[1:] if os.path.isdir(x)]; run(os.path.abspath(a[0]) if a else FINAL)
