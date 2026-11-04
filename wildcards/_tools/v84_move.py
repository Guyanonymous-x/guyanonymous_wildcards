"""v84 - move the existing sex, BDSM and fetish object files under the adult_ prefix (references rewritten everywhere). Idempotent: reads either the old or the already-moved file."""
import os, sys, re
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
FINAL = '/home/claude/w/wildcards'
PRE = ('acc_dildo', 'acc_vibrator', 'acc_buttplug', 'acc_adulttoy', 'acc_pasties', 'acc_merkin', 'acc_gag', 'acc_sensation', 'acc_chastity', 'chastity_')
REF = re.compile(r'__([A-Za-z0-9_\-/]+)__')
def old_names(final=FINAL):
    S = set()
    for f in os.listdir(final):
        if not f.endswith('.txt'): continue
        n = f[:-4]
        if n.startswith(PRE): S.add(n)
        elif n.startswith('adult_') and n[6:].startswith(PRE): S.add(n[6:])
    return S
def rw(lines, S):
    return [REF.sub(lambda m: '__adult_' + m.group(1) + '__' if m.group(1) in S else m.group(0), l) for l in lines]
def rd(final, n):
    p = os.path.join(final, n + '.txt')
    return [l.rstrip('\n') for l in open(p, encoding='utf8')]
def build(final=FINAL):
    S = old_names(final); G = {}
    for n in sorted(S):
        src = n if os.path.exists(os.path.join(final, n + '.txt')) else 'adult_' + n
        G['adult_' + n] = rw(rd(final, src), S)
    # other files that referenced moved files
    for f in os.listdir(final):
        if not f.endswith('.txt'): continue
        n = f[:-4]
        if n in S or n.startswith('adult_'): continue
        L = rd(final, n); new = rw(L, S)
        if new != L: G[n] = new
    G['v84_move_entry_points'] = []
    return G
def cleanup(final=FINAL, aoo=None):
    S = old_names(final); n = 0
    for s in S:
        p = os.path.join(final, s + '.txt')
        if os.path.exists(p): os.remove(p); n += 1
    if aoo and os.path.isdir(aoo):
        for s in S:
            p = os.path.join(aoo, 'aoo_' + s + '.txt')
            if os.path.exists(p): os.remove(p); n += 1
        for f in os.listdir(aoo):
            if not f.endswith('.txt'): continue
            pa = os.path.join(aoo, f); t = open(pa, encoding='utf8').read()
            t2 = REF.sub(lambda m: '__aoo_adult_' + m.group(1)[4:] + '__' if m.group(1).startswith('aoo_') and m.group(1)[4:] in S else m.group(0), t)
            if t2 != t: open(pa, 'w', encoding='utf8').write(t2)
    return n
if __name__ == '__main__':
    G = build(); print(len(G), sorted(G)[:3])
