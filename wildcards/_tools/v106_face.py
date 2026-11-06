"""v106 - chin wording. A cleft or dimple is a shallow vertical groove in the middle of the chin tip, about a thumbnail long, well below the lower lip;
the outline of the chin stays unbroken. 'deep cleft' wording split the chin into two lobes and ran the line up toward the lip."""
import os, re
GR = 'a small shallow dimple low on the middle of the chin tip, a soft spot of shadow about the size of a fingernail, not a long line'
ALT = ['a cleft chin, with ' + GR + ', the outline of the chin smooth and unbroken',
       'a cleft chin showing only ' + GR + ', the chin one smooth rounded shape on either side of it',
       'a chin with a faint dimple in the middle of its tip, no longer than a fingernail and well below the lower lip, no vertical line']
def build(final):
    old = [l.rstrip('\n') for l in open(os.path.join(final, 'head_chin.txt'), encoding='utf8') if l.strip()]
    out = []; k = 0
    for l in old:
        if l == 'deeply cleft chin': out.append(ALT[k % 3]); k += 1; continue
        if l.endswith('no definition') and l.startswith('cleft'): continue
        l = re.sub(r' with a deep central cleft$', ' with ' + GR, l)
        l = re.sub(r'^cleft chin with (a faint dimple|a smooth contour|a defined edge|a soft underside|a firm line|a slight curve|a pronounced tip|a gentle taper)$', r'chin with a faint small dimple in the middle of the tip and \1', l)
        l = re.sub(r'^dimpled chin with a deep central cleft$', 'chin with a small dimple in the middle of the tip', l)
        l = l.replace('dimpled chin center', 'a small dimple in the middle of the chin tip')
        out.append(l)
    out = [l for l in out]
    return {'head_chin': out}
