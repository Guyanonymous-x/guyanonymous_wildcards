"""v82 - art forms that are neither illustration nor photography (af_). Four families (sculpture, craft, fibre, render/installation), each with forms that carry their own
subjects, materials, techniques, finishes, colours, scales and wear, and shared display, light and shot pools per family. Real artists/makers only in maker_ files."""
import os, sys, re
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from famlib import P
DISP = {}
FAMS = ['sculpt', 'craft', 'fibre', 'render']
LABEL = ['a small brass plaque that reads "Untitled No. 4"', 'a small card label that reads "Study in Stone"', 'a printed museum tag that reads "Gift of an anonymous donor"', 'a handwritten price tag that reads "Sold"', 'a stamped maker mark that reads "No. 12"', 'a tiny engraved date that reads "1987"', 'a small paper label that reads "Handle with care"', 'a plaque beside it that reads "The Long Wait"', 'a numbered tag that reads "3 of 20"', 'a gallery wall label that reads "Mixed materials"', 'a small signature scratched in that reads "M. K."', 'a printed card that reads "Please do not touch"', 'no label or mark at all', 'no label or mark at all']
def an(n): return ('An ' if n[:1].lower() in 'aeiou' else 'A ') + n
def pl(n):
    if n.endswith('s'): return n
    if n.endswith('y') and n[-2] not in 'aeiou': return n[:-1] + 'ies'
    if n.endswith(('ch', 'sh', 'x')): return n + 'es'
    return n + 's'
def wear_fix(x):
    if x.startswith('with '): return 'marked ' + x
    if re.match(r'^(a|an|the) ', x) and not re.match(r'^a (little|bit|few|slight)', x): return 'showing ' + x
    return x
def load():
    FORMS = {}; SHARED = {}; DISP.clear()
    for f in FAMS:
        try: m = __import__('v82_af_' + f)
        except ImportError: continue
        for k, v in m.FORMS.items(): FORMS[(f, k)] = v
        SHARED[f] = m.SHARED
        for k, v in getattr(m, 'DISPLAY', {}).items(): DISP[(f, k)] = v
    return FORMS, SHARED
def build(final=None):
    FORMS, SHARED = load(); G = {}; ep = []; kinds = {f: [] for f in FAMS}
    G['af_marks'] = ['with ' + x if not x.startswith('no ') else 'with ' + x for x in LABEL]
    for f, s in SHARED.items():
        for part in ('display', 'light', 'shot'): G['af_%s_%s' % (f, part)] = P(s[part])
        if s.get('marks'): G['af_%s_marks' % f] = P(s['marks'])
    for (f, k), (noun, subj, mat, tech, fin, col, scale, wear) in FORMS.items():
        n = '%s_%s' % (f, k)
        G['af_%s_subject' % n] = P(subj); G['af_%s_material' % n] = P(mat); G['af_%s_technique' % n] = P(tech); G['af_%s_finish' % n] = P(fin)
        G['af_%s_colour' % n] = P(col); G['af_%s_scale' % n] = P(scale); G['af_%s_wear' % n] = [wear_fix(x) for x in P(wear)]
        G['af_%s_look' % n] = ['It depicts __af_%s_subject__. It is made of __af_%s_material__, made by __af_%s_technique__. Its surface shows __af_%s_finish__, in __af_%s_colour__.' % ((n,) * 5),
                                'Made of __af_%s_material__ by __af_%s_technique__, it shows __af_%s_subject__. The surface has __af_%s_finish__, and the colours are __af_%s_colour__.' % ((n,) * 5)]
        if (f, k) in DISP: G['af_%s_display' % n] = P(DISP[(f, k)])
        dref = 'af_%s_display' % (n if (f, k) in DISP else f)
        mk = 'af_%s_marks' % f if SHARED[f].get('marks') else 'af_marks'
        G['af_%s_prompt' % n] = ['This is __af_%s_scale__ %s. __af_%s_look__ It is __af_%s_wear__, __%s__. It is __%s__, in __af_%s_light__, and the image is __af_%s_shot__.' % (n, noun, n, n, mk, dref, f, f)]
        G['af_%s_short' % n] = ['%s of __af_%s_material__ showing __af_%s_subject__, in __af_%s_colour__.' % (an(noun), n, n, n)]
        G['af_%s_group_prompt' % n] = ['Three %s are shown together __%s__. The first is made of __af_%s_material__ and shows __af_%s_subject__. The second is made of __af_%s_material__ and shows __af_%s_subject__. The third is made of __af_%s_material__ and shows __af_%s_subject__. They are in __af_%s_light__.' % ((pl(noun), dref) + (n, n) * 3 + (f,))]
        kinds[f].append(n); ep.append('af_%s_prompt' % n)
    for f in FAMS:
        if not kinds[f]: continue
        for s_ in ('prompt', 'group_prompt', 'short'): G['af_%s_%s' % (f, s_)] = ['__af_%s_%s__' % (n, s_) for n in kinds[f]]
        ep += ['af_%s_prompt' % f]
    allk = [n for f in FAMS for n in kinds[f]]
    for s_ in ('prompt', 'group_prompt', 'short'): G['af_' + s_] = ['__af_%s_%s__' % (n, s_) for n in allk]
    G['af_forms'] = [FORMS[tuple(n.split('_', 1))][0] for n in allk]
    G['v82_af_entry_points'] = ['af_prompt', 'af_group_prompt', 'af_short'] + ep
    return G
if __name__ == '__main__':
    G = build(); print(len(G))
