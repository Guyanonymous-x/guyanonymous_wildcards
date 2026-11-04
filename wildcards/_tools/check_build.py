"""Standing build check (run before every release):  python _tools/check_build.py [--fail]
 1 references    every __name__ resolves
 2 symbols       curly quotes, en/em dashes, double hyphens, pipes outside {a|b}, <lora tags, (word:number) weights, stray colons (digit:digit is allowed), unbalanced __
 3 blank lines   files with blank lines (a 'none' option must be a single space), and files that end with a blank line
 4 pronoun leads long-form person piece files that still start a sentence with Her / His / Their
 5 contradictions  check_consistency.py (entry points expanded, rules for night vs day, snow vs summer, flightless birds, wear states)
 6 bare names    report only: very short lines in description-required pools (type / style / shape lists of objects)
 With --fail the exit code is 1 when checks 1 to 5 find anything."""
import os, re, sys, collections
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from paths import FINAL
bad = collections.OrderedDict()
files = {f[:-4]: os.path.join(FINAL, f) for f in sorted(os.listdir(FINAL)) if f.endswith('.txt')}
REF = re.compile(r'__([A-Za-z0-9_\-/]+)__')
txt = {n: open(p, encoding='utf8', errors='replace').read() for n, p in files.items()}
# 1
m = [(n, r) for n, t in txt.items() for r in set(REF.findall(t)) if r not in files]; bad['unresolved references'] = m
# 2
sym = {'curly quotes': re.compile('[‘’“”]'), 'en/em dash': re.compile('[–—]'), 'double hyphen': re.compile(r'--'),
       'lora tag': re.compile(r'<lora', re.I), 'emphasis weight': re.compile(r'\([^()\n]{1,60}:-?\d+(\.\d+)?\)'), 'stray colon': re.compile(r'(?<!\d):(?!\d)')}
for k, rx in sym.items(): bad['symbol: ' + k] = [n for n, t in txt.items() if rx.search(t)]
bad['symbol: unbalanced __'] = [n for n, t in txt.items() if any(l.count('__') % 2 for l in t.split('\n'))]
bad['symbol: pipe outside {a|b}'] = [n for n, t in txt.items() if re.search(r'\|', re.sub(r'\{[^{}]*\}', '', t))]
# 3
bl = []
for n, t in txt.items():
    ls = t.split('\n')
    if ls and ls[-1] == '': ls = ls[:-1]
    if any(l == '' for l in ls) or t.endswith('\n\n'): bl.append(n)
bad['blank lines'] = bl
# 4
LEAD = re.compile(r"(^|(?<=[.!?] ))(Her|His|Their) (?=[a-z])", re.M)
SEL = re.compile(r'^(f|m|any)_.*prompt_char_(face|hair|hair_[CKSW]|skin|body|details)$')
bad['pronoun-start sentences in person pieces'] = [n for n, t in txt.items() if SEL.match(n) and LEAD.search(t)]
# 5
try:
    import check_consistency
    total, hits = check_consistency.run(20, 11); bad['contradictions'] = [(k, len(v)) for k, v in hits.items()]
except Exception as e: bad['contradictions'] = [('check failed', repr(e))]
# 6 report only
bare = []
for n, t in txt.items():
    if re.search(r'_(type|style|shape|kind)$', n) and (n.startswith(('acc_', 'clothing_', 'furn_', 'tool_', 'veh_'))):
        ls = [l for l in t.split('\n') if l.strip()]
        if ls and sum(len(l.split()) <= 3 for l in ls) / len(ls) > 0.8: bare.append(n)
print('FILES', len(files))
fail = False
for k, v in bad.items():
    print(f'{"FAIL" if v else "ok  "}  {k}: {len(v)}', (list(v)[:6] if v else ''))
    fail = fail or bool(v)
print(f'INFO  pools of mostly bare names (3 words or fewer): {len(bare)}', bare[:8])
if '--fail' in sys.argv and fail: sys.exit(1)
