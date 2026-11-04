"""Item 59 check script: expands entry-point prompts many times and flags contradictions between independently drawn parts.
   python _tools/check_consistency.py            -> summary per rule, with examples
   python _tools/check_consistency.py 200 7      -> 200 expansions per entry point, seed 7
   python _tools/check_consistency.py --fail     -> exit code 1 if any rule fires (use as a build check)
Rules are (name, regex A, regex B): a line is flagged when BOTH match. Add rules at the bottom of RULES."""
import re, sys, os, random, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from expand import load, expand, clean
from paths import FINAL
FLIGHTLESS = r"penguin|ostrich|emu\b|kiwi|cassowary|rhea\b|kakapo|dodo|takah"
NIGHT = r"deep night|\bnight\b|midnight|after dark"
DAYWORDS = r"midday|windy day|sunny day|bright morning|early morning light|golden hour|late afternoon|broad daylight"
RULES = [
 ('night with day wording', NIGHT, DAYWORDS),
 ('snow with warm or summer', r"fresh snow|snow on the ground|snow-covered", r"warm still air|summer|heat haze|tropical|palm|sunbathing|sun-baked|beach towel"),
 ('flightless bird flying', FLIGHTLESS, r"flying|in flight|in formation|taking off|soaring|gliding through the air|above open water|spreading its wings on a post|perch"),
 ('spotless with decay', r"spotless|immaculate|pristine|brand new|freshly polished", r"falling apart|rusted|corroded|crumbling|decayed|broken|cracked and peeling"),
 ('young bird flying over water', r"\byoung\b|chicks?\b|fluffy", r"above open water|flying in formation|soaring"),
 ('daylight with lit windows only', r"bright midday light", r"lit windows|lamplight|neon glow|streetlights glowing"),
 ('rain with dry or clear', r"heavy rain|light drizzle|wet shining ground", r"clear dry air|warm still air|cloudless"),
 ('part does not exist', r"holding a fishing rod|holding a (pen|cup|plate|ball|bottle|hat)", r"the joint or hinge|hinges? (are|is) (squeaky|stiff)"),
 ('sport mismatch', r"skateboarding", r"\bnet\b|racket|goalposts|a ball and"),
]
def entry_points(files):
    pre = ('city_', 'fx_', 'ani2_', 'cond', 'maker_', 'act_', 'world_', 'env_', 'veh_', 'land_', 'wx_', 'job_', 'tool_', 'home_', 'room_', 'obj_', 'vx_')
    return sorted(n for n in files if n.endswith('_prompt') and n.startswith(pre))
def run(n=40, seed=1):
    files = load([FINAL]); rng = random.Random(seed); hits = collections.defaultdict(list); total = 0
    for ep in entry_points(files):
        for _ in range(n):
            t = clean(expand(files, '__' + ep + '__', rng)); total += 1
            for name, a, b in RULES:
                if re.search(a, t, re.I) and re.search(b, t, re.I): hits[name].append((ep, t))
    return total, hits
if __name__ == '__main__':
    args = [x for x in sys.argv[1:] if not x.startswith('--')]
    n = int(args[0]) if args else 40; seed = int(args[1]) if len(args) > 1 else 1
    total, hits = run(n, seed)
    print(f'{total} expansions checked, {sum(len(v) for v in hits.values())} flagged')
    for name, v in hits.items():
        eps = collections.Counter(e for e, _ in v)
        print(f'\n[{name}] {len(v)} hits in {len(eps)} entry points, most affected {eps.most_common(4)}')
        for e, t in v[:2]: print('   ', e, '->', t[:260])
    if '--fail' in sys.argv and hits: sys.exit(1)
