"""Helpers for the vocabulary expansion.  Everything here is deterministic (seeded) so repeated builds give identical files."""
import random, zlib, itertools, re

def S(t):
    """comma/newline separated string -> list of stripped, non-empty items (no duplicates, order kept)"""
    out = []
    for x in t.replace('\n', ' ').split(','):
        x = ' '.join(x.split())
        if x and x not in out: out.append(x)
    return out

def seed_of(name): return zlib.crc32(name.encode()) & 0xffffffff

def sample(items, n, name='x'):
    """deterministic sample of n items (all items if there are fewer), original order kept"""
    items = list(dict.fromkeys(items))
    if len(items) <= n: return items
    idx = sorted(random.Random(seed_of(name)).sample(range(len(items)), n))
    return [items[i] for i in idx]

def product(fmt, *axes):
    """all combinations of the axes inserted into fmt ({0}, {1}, ...)"""
    return [fmt.format(*c) for c in itertools.product(*axes)]

def fix_articles(s):
    return re.sub(r'\b([Aa]) (?=[aeiouAEIOU])', lambda m: m.group(1) + 'n ', s)

def merge(orig, new, limit=None):
    """originals first (never dropped), then the new options; duplicates removed (case-insensitive)"""
    seen = set(); out = []
    for x in list(orig) + list(new):
        x = x.strip()
        k = x.lower()
        if x and k not in seen: seen.add(k); out.append(x)
    return out


# ---- contradiction filter: a generated phrase may not contain words from both sides of an opposing pair ----
_PAIRS = [
 ("wide broad generous", "narrow tight compressed pinched"), ("high tall", "low short"), ("long", "short"),
 ("thick heavy full plump fleshy padded", "thin slim lean sparse hollow sunken gaunt"),
 ("smooth", "creased lined wrinkled rough furrowed"), ("flat", "prominent pronounced projected protruding bulbous bulging"),
 ("upturned lifted upward", "downturned drooping downward"), ("symmetrical even balanced", "asymmetrical asymmetric uneven crooked"),
 ("straight", "curved arched bent crooked wavy curl"), ("round rounded", "angular square squared pointed"),
 ("deep pronounced", "shallow faint subtle barely"), ("defined crisp clear", "indistinct blurred undefined barely"),
 ("large big", "small tiny"), ("firm", "slack loose"), ("visible", "hidden invisible"), ("relaxed", "tense flexed tight"),
 ("close", "wide-set"), ("sharp", "soft blurred"), ("light", "heavy dark"), ("matte", "glossy shiny"),
 ("dry", "moist wet glossy hydrated"), ("calm", "intense"), ("thin", "thick"), ("hidden", "showing"),
]
_STEM = lambda w: re.sub(r'(ly|ed|s)$', '', w) if len(w) > 4 else w
_PAIRS_T = [([_STEM(w) for w in a.split()], [_STEM(w) for w in b.split()]) for a, b in _PAIRS]
def consistent(phrase):
    toks = {_STEM(t) for t in re.findall(r"[a-z'\-]+", phrase.lower())}
    toks |= {t for tt in list(toks) for t in tt.split('-')}
    for a, b in _PAIRS_T:
        if any(w in toks for w in a) and any(w in toks for w in b): return False
    return True
