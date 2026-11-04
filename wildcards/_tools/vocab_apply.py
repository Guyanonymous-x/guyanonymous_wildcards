"""Applies the vocabulary expansion to the ROOT option files.  Idempotent: every run starts again from the saved originals in
data/orig_roots/, keeps every original option, and adds the new options from the vocab_* modules.

  * files that are 'uniform' (all options repeated about equally, or once)  -> every distinct option once
  * files that are likelihood-weighted (repeat counts differ a lot)         -> original lines are kept as they are and the new options are
    added as a block that makes up NEW_SHARE of the file, split evenly (the pilot_body / wcbuild step then keeps the original proportions)
  * blank lines ('none') keep their original share of the file

Run:  python vocab_apply.py [wildcards_folder]        (build_all.py runs this first)
"""
import os, sys, re, collections
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from paths import FINAL, DATA
ORIG = os.path.join(DATA, 'orig_roots')
NEW_SHARE = 0.25
BAD = re.compile(r'[{}|]|__|^\d+(\.\d+)?::')

def registry():
    import vocab_face, vocab_body, vocab_scene           # noqa  (they register into vocab_face.R)
    mods = ['vocab_people', 'vocab_misc']
    for m in mods:
        try: __import__(m)
        except ImportError as e:
            if m not in str(e): raise
    from vocab_face import R
    return {k: v for k, v in R.items() if v}

def read(path):
    return [l.rstrip('\n').strip() for l in open(path, encoding='utf8', errors='replace')]

def expand_file(name, fn, final):
    src = os.path.join(ORIG, name + '.txt')
    if not os.path.exists(src): return None
    lines = read(src)
    while lines and lines[-1] == '': lines.pop()
    blanks = sum(1 for l in lines if l == ''); nonblank = [l for l in lines if l]
    cnt = collections.Counter(nonblank)
    orig_opts = list(dict.fromkeys(nonblank))
    new = [x for x in fn(orig_opts) if x and not BAD.search(x)]
    seen = {o.lower() for o in orig_opts}; add = []
    for x in new:
        x = ' '.join(x.split())
        if x.lower() not in seen: seen.add(x.lower()); add.append(x)
    weighted = cnt and max(cnt.values()) / max(1, min(cnt.values())) > 2.0
    if weighted:
        body = nonblank[:]
        block = max(len(add), round(len(nonblank) * NEW_SHARE / (1 - NEW_SHARE)))
        each = max(1, round(block / max(1, len(add))))
        for x in add: body += [x] * each
    else:
        body = orig_opts + add
    share = blanks / max(1, len(lines))
    nb = round(len(body) * share / (1 - share)) if share and share < 1 else 0
    out = body + [''] * nb
    path = os.path.join(final, name + '.txt')
    open(path, 'w', encoding='utf8', newline='\n').write('\n'.join(out) + '\n')
    return len(orig_opts), len(set(body)), weighted

def apply(final=None, verbose=True):
    final = final or FINAL; R = registry(); done = {}
    for name, fn in sorted(R.items()):
        r = expand_file(name, fn, final)
        if r: done[name] = r
    if verbose:
        lo = sorted(done.items(), key=lambda kv: kv[1][1])[:8]
        print(f'vocab_apply: {len(done)} files expanded; smallest result: ' + ', '.join(f'{k}={v[1]}' for k, v in lo))
    return done

if __name__ == '__main__':
    d = [a for a in sys.argv[1:] if os.path.isdir(a)]
    apply(os.path.abspath(d[0]) if d else None)
