"""v81 stage C - maker_ reference files built from the research notes (real and fictional robots, handheld gadgets, computers). Real and fictional names live only here."""
import os, sys, re
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
DOCS = '/home/claude/w/docs'
def clean(s):
    s = re.sub(r'\[[^\]]*\]', '', s)
    s = re.sub(r'\((?:v|verified)[^)]*\)', '', s)
    s = re.sub(r'\s+', ' ', s).strip(' ;,.')
    s = s.replace(':', ' -').replace('{', '').replace('}', '').replace('|', ' ')
    return s
def art(w): return 'an' if w[:1].lower() in 'aeiou' else 'a'
def ok(x): return len(x) > 2 and x.lower() not in ('none', 'n/a', '-', 'unknown')
def rows(fn, n):
    out = []
    for l in open(os.path.join(DOCS, fn), encoding='utf8'):
        if l.startswith(('#', 'Format', 'FORMAT', '==')) or '|' not in l: continue
        f = [clean(x) for x in l.rstrip('\n').split('|')]
        if len(f) == n: out.append(f)
    return out
def robots(fn):
    L = []
    for name, yr, role, body, head, arms, legs, mat, col, size in rows(fn, 10):
        parts = [p for p in (body, ('with ' + head) if ok(head) else '', 'arms and hands are ' + arms if ok(arms) else '', legs, ('made of ' + mat) if ok(mat) else '', ('in ' + col) if ok(col) else '', ('about ' + size) if ok(size) else '') if ok(p)]
        if len(parts) >= 4: L.append('%s (%s), %s %s, %s.' % (name, yr, art(role), role, ', '.join(parts)))
    return L
def gadgets(fn):
    L = []
    for ref, desc, yr, cat, shape, size, screen, ctrl, mat, col, feat in rows(fn, 11):
        if not ok(ref) or not ok(shape) or not ok(mat) or not ok(col): continue
        parts = [shape, ('about %s cm' % size) if ok(size) else '', ('screen - ' + screen).replace(' - ', ' is ') if ok(screen) else '', ('controls - ' + ctrl).replace(' - ', ' are ') if ok(ctrl) else '', 'made of ' + mat, 'in ' + col, feat if ok(feat) else '']
        parts = [p for p in parts if p]
        if len(parts) >= 5: L.append('%s (%s), %s, %s %s, %s.' % (ref, yr, desc, art(cat), cat, ', '.join(parts)))
    return L
def build(final=None):
    G = {'maker_robot_real_models': robots('robots_real.txt'), 'maker_robot_fiction_models': robots('robots_fiction.txt'),
         'maker_gadget_models': gadgets('gadgets_handheld.txt'), 'maker_computer_models': gadgets('gadgets_computers.txt')}
    G['v81_maker_entry_points'] = ['maker_robot_real_models', 'maker_robot_fiction_models', 'maker_gadget_models', 'maker_computer_models']
    return G
if __name__ == '__main__':
    G = build()
    for k, v in G.items(): print(k, len(v)); print(v[0][:300] if v else '')
