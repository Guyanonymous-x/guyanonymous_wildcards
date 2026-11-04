"""Shared helpers for part-based families (v57+). A family has a type, named part lists and a sentence template using {part} markers."""
import os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from paths import FINAL
from v53_build import _wr, decolon, REF
def P(s): return [x.strip() for x in s.split(';') if x.strip()]
def slug(s): return re.sub(r'[^a-z0-9]+', '_', s.lower()).strip('_')
def an(w): return ('An ' if w[:1].lower() in 'aeiou' else 'A ') + w
def fams(prefix, DATA, TPL=None, subject=''):
    """DATA = {type: {part: [options]}}; TPL = {type: 'A thing with {part}, {part2}.'} -> files prefix_type_part, prefix_type_prompt, prefix_types, prefix_prompt"""
    G = {}; TPL = TPL or {}
    for t, parts in DATA.items():
        s = slug(t)
        for k, vals in parts.items(): G['%s_%s_%s' % (prefix, s, k)] = vals
        tpl = TPL.get(t)
        if not tpl: tpl = an(t) + ' with ' + ', '.join('{%s}' % k for k in parts) + '.'
        G['%s_%s_prompt' % (prefix, s)] = [re.sub(r'\{(\w+)\}', lambda m: '__%s_%s_%s__' % (prefix, s, m.group(1)), tpl)]
    G['%s_types' % prefix] = sorted(DATA)
    G['%s_prompt' % prefix] = ['__%s_%s_prompt__' % (prefix, slug(t)) for t in DATA]
    return G
def run_mod(mod, final):
    G = mod.build(final)
    for n, l in G.items(): _wr(final, n, l)
    print(mod.__name__, len(G), 'files; no-colon', decolon(final)); return G
def export_aoo_mod(G, out, prefix='aoo_', skip=()):
    G = {k: v for k, v in G.items() if k not in skip and not k.endswith('_entry_points')}; names_ = set(G); n = 0
    for name, lines in G.items():
        keep = list(dict.fromkeys(REF.sub(lambda m: '__' + prefix + m.group(1) + '__' if (m.group(1) in names_ or os.path.exists(os.path.join(out, prefix + m.group(1) + '.txt'))) else m.group(0), l) for l in lines))
        _wr(out, prefix + name, keep); n += 1
    decolon(out); return n
