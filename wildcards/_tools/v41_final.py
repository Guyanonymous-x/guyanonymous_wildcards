"""v41 final pass. (1) Label sweep: removes 'Label: text' phrasing (which makes image models print the words after the colon) by turning labels into natural clauses. (2) Gendered eyewear person-lines (f_/m_ acc_glasses and age*_opt_eyewear) now use the fully described frames from acc_eyewear_frame. Idempotent."""
import os, re, sys, glob
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from paths import FINAL
REPL = {'Subject': '', 'A funny detail': 'A funny detail is ', 'The scene': 'The scene is ', 'Setting and atmosphere': 'The setting and atmosphere are '}
LAB = re.compile(r"(^|[.!?;] |__ )((?:__[a-z0-9_]+__ )?)([A-Z][A-Za-z'’\- ]{1,50}): (?=\S)", re.M)
def lab(m):
    pre, tok, name = m.group(1), m.group(2), m.group(3)
    if name in REPL: return pre + tok + REPL[name]
    if len(name.split()) > 14: return m.group(0)
    return f"{pre}{tok}{name}, "
def sweep_text(t): return LAB.sub(lab, t)
EYE = re.compile(r"glasses|sunglasses|spectacles|monocle|pince|goggles|lorgnette|eyewear is|frames?\b", re.I)
SKIP = re.compile(r"contact lens|eyepatch|eye patch|__acc_eyewear", re.I)
def eyefix(final):
    n = 0
    for f in glob.glob(os.path.join(final, '[fm]_acc_glasses.txt')) + glob.glob(os.path.join(final, '[fm]_age*_opt_eyewear.txt')):
        out = []; ch = False
        for l in open(f, encoding='utf8').read().split('\n'):
            if l.strip() and EYE.search(l) and not SKIP.search(l):
                w = l.split()[0]
                l = {'She': 'She wears __acc_eyewear_frame__.', 'He': 'He wears __acc_eyewear_frame__.', 'Her': 'Her eyewear is __acc_eyewear_frame__.', 'His': 'His eyewear is __acc_eyewear_frame__.'}.get(w, l); ch = True
            out.append(l)
        if ch: open(f, 'w', encoding='utf8', newline='\n').write('\n'.join(out)); n += 1
    return n
def sweep(folder):
    n = 0
    for f in glob.glob(os.path.join(folder, '*.txt')):
        t = open(f, encoding='utf8').read(); u = sweep_text(t)
        if u != t: open(f, 'w', encoding='utf8', newline='\n').write(u); n += 1
    return n
def run(final): a = eyefix(final); b = sweep(final); print('v41 final: eyewear lines', a, 'files; label sweep', b, 'files'); return b
def export_aoo(out, prefix='aoo_'): sweep(out); return 0
if __name__ == '__main__':
    a = [x for x in sys.argv[1:] if os.path.isdir(x)]; run(os.path.abspath(a[0]) if a else FINAL)
