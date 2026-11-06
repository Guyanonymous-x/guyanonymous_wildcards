"""usage: python3 finish.py N   (needs vNN_build.py and vNN_meta.py).  Builds into the library + AOO, makes samples, docs, then starts rel.py/pack.py in the background."""
import sys, os, re, json, random, glob, subprocess, importlib, collections
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from paths import FINAL
N = int(sys.argv[1]); W = '/home/claude/w'; AOO = W + '/all_options_once'; V = '/tmp/release_scripts'; SCR = '/tmp/claude-0/-home-claude/f4f177e0-8597-507c-b7de-4fd3dcc5cfda/scratchpad'
B = importlib.import_module('v%d_build' % N); M = importlib.import_module('v%d_meta' % N)
G = B.run(FINAL)
nex = B.export_aoo(AOO); 
for f in glob.glob(f'{AOO}/aoo_v{N}_entry_points.txt'): os.remove(f)
print('aoo export', nex)
from expand import load, expand, clean
files = load([FINAL]); 
def chk(d):
    bad = []
    names = {f[:-4] for f in os.listdir(d) if f.endswith('.txt')}; skipn = {'CHANGELOG', 'README'}
    for f in names - skipn:
        for r in set(re.findall(r'__([A-Za-z0-9_\-/]+)__', open(f'{d}/{f}.txt', encoding='utf8').read())):
            if r not in names: bad.append((f, r))
    return bad
b1, b2 = chk(FINAL), chk(AOO); print('unresolved library', len(b1), b1[:3], 'aoo', len(b2), b2[:3])
if b1 or b2: sys.exit('unresolved references')
rng = random.Random(N * 101); S = []
# samples cover EVERYTHING the package can do: one entry point from every family (prefix), adult only as L1, plus the version staples
eps = sorted({l.strip() for fn in glob.glob(FINAL + '/v*_entry_points.txt') for l in open(fn, encoding='utf8') if l.strip()})
eps = [e for e in eps if e in files]
fam = collections.defaultdict(list)
for e in eps: fam[e.split('_')[0]].append(e)
for p in sorted(fam):
    if p == 'adult': continue
    c = [e for e in fam[p] if e.endswith('_prompt')] or fam[p]
    S.append(('family ' + p + ': ' + (e := rng.choice(c)), '__%s__' % e))
S += [('adult L1', '__adult_l1_full_prompt__')] * 3
for label, tpl, n in M.SAMPLES:
    if label != 'adult L1': S.append((label, tpl))
rng.shuffle(S); rows = []
for a, t in S:
    rows.append((a, ' '.join(clean(expand(files, t, rng)).split())))
k = 0
while len(rows) < 100:
    rows.append(('brand style any', ' '.join(clean(expand(files, '__bs_prompt__', rng)).split()))); k += 1
rows = rows[:100]
o = f'/mnt/user-data/outputs/Guyanonymous_Wildcards_v{N}_sample_prompts'
open(o + '.txt', 'w').write('\n'.join(r[1] for r in rows)); open(o + '_labelled.tsv', 'w').write('label\tprompt\n' + '\n'.join(f'{a}\t{b}' for a, b in rows))
print('samples', len(rows), 'leaks', sum(1 for r in rows if '__' in r[1] or re.search(r'[{}|]', r[1])))
json.dump(M.BULLETS, open(f'{V}/b{N}.json', 'w'), indent=1); open(f'{V}/r{N}.txt', 'w').write(M.README)
rd = '/tmp/pkg14_main/README.txt'; t = open(rd).read()
if not t.startswith(f'v{N}: '): open(rd, 'w').write(f'v{N}: {M.ONELINE}\n' + t)   # never add the version line twice on a re-run
g = open(f'{SCR}/gen.py').read(); anchor = ' ("room_<type>_prompt_brief/_full'
if M.GEN_ROW not in g: open(f'{SCR}/gen.py', 'w').write(g.replace(anchor, ' ' + M.GEN_ROW + '\n' + anchor, 1))
subprocess.run(['python3', 'gen.py'], cwd=SCR, check=True, capture_output=True)
for fn in getattr(M, 'DOCS', []): subprocess.run(['cp', fn, '/tmp/pkg14_main/docs/'])
subprocess.Popen(f'cd {V} && (python3 rel.py {N} b{N}.json r{N}.txt > rel{N}.log 2>&1 && cd {HERE} && python3 pack.py {N} >> {V}/rel{N}.log 2>&1 && echo ALLDONE{N} >> {V}/rel{N}.log)', shell=True)
print('release started')
