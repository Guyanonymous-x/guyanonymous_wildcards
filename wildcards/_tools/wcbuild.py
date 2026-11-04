"""Build a frequency-weighted wildcard file.
- every option already in the source file is kept at least once
- total lines <= N (default 2500); weights are relative (percent-like, need not sum to 100)
- none_pct reserves that share of lines as blank lines ("no feature")
"""
import random, sys

def read_options(path):
    seen = []
    for l in open(path, encoding='utf8'):
        l = l.strip()
        if l and l not in seen: seen.append(l)
    return seen

def allocate(weights, total, min_each=1):
    """largest-remainder allocation, each item >= min_each"""
    k = len(weights)
    spare = total - k * min_each
    assert spare >= 0, "too many options for line budget"
    s = float(sum(weights))
    raw = [w / s * spare for w in weights]
    base = [int(r) for r in raw]
    left = spare - sum(base)
    order = sorted(range(k), key=lambda i: raw[i] - base[i], reverse=True)
    for i in order[:left]: base[i] += 1
    return [b + min_each for b in base]

def build(src, out, table, none_pct=0.0, N=2500, seed=7, extra_share=0.25):
    """table = [(option, weight)].  Options in the source file that the table does not mention (added by vocab_apply) share extra_share of the
    file equally; options in the table that the source lacks are kept (the table is authoritative)."""
    opts = read_options(src)
    table = list(table)
    known = {t[0] for t in table}
    extra = [o for o in opts if o not in known] if extra_share > 0 else []
    if extra:
        tot = float(sum(t[1] for t in table)); each = tot * extra_share / (1 - extra_share) / len(extra)
        table += [(o, each) for o in extra]
    names = [t[0] for t in table]
    N = max(N, int(len(table) * 3 / max(0.05, 1 - none_pct / 100.0)) + 1)
    n_none = round(N * none_pct / 100.0)
    counts = allocate([t[1] for t in table], N - n_none)
    lines = []
    for (name, _), c in zip(table, counts): lines += [name] * c
    lines += [''] * n_none
    random.Random(seed).shuffle(lines)
    open(out, 'w', encoding='utf8', newline='\n').write('\n'.join(lines) + '\n')
    return dict(zip(names, counts)), n_none
