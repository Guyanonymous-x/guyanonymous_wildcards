"""ONE-TIME maintenance script (already applied to the delivered settings10000.txt):  python _tools/fix_settings.py [path_to_settings10000.txt]
Reduces the repeated whimsical tail clauses and the rubber-duck scenes in settings10000.txt and replaces them with diverse everyday objects (objects_data.py).
Every distinct tail clause and scene type stays present at least a couple of times."""
import os, sys, re, random, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from paths import FINAL
from objects_data import extra_clauses
path = sys.argv[1] if len(sys.argv) > 1 else os.path.join(FINAL, 'settings10000.txt')
L = [l.rstrip('\n') for l in open(path, encoding='utf8')]
WHIM = ["a goat wearing a tiny hat", "balloon animals twisting in the air", "a bubble machine blowing foam", "people laughing in clown wigs", "a dog dressed as a pirate", "a giant foam finger",
        "a rubber chicken on a pedestal", "a man in a banana costume", "an oversized inflatable duck", "a very serious judge in a ridiculous wig", "confetti falling everywhere", "a mascot waving wildly"]
KEEP = 12            # lines per whimsical clause that stay as they were (the oversized duck keeps 2)
EX = extra_clauses(4000, seed=3); R = random.Random(5); seen = collections.Counter(); out = []; ei = 0
RIVER = [("a dragon boat race", "teams paddling in time to a drum, a cheering crowd on the bridge"), ("a lantern-floating ceremony", "hundreds of paper lanterns drifting downstream, spectators on the bank"),
         ("a rowing regatta", "slim racing boats sliding toward a finish line, supporters along the towpath"), ("a riverside fishing contest", "anglers lined up along the bank on folding stools, a weigh-in table"),
         ("a kite festival", "paper kites high over the water, children running along the embankment"), ("a river clean-up day", "volunteers in waders hauling nets, full sacks piled on the bank"),
         ("a paper-boat regatta", "hundreds of tiny folded boats racing downstream, children cheering from the bridge"), ("a floating market", "narrow boats piled with fruit and flowers, haggling across the water"),
         ("a charity swim", "swimmers in bright caps crossing the river, kayaks guiding them, a cheering crowd on the bridge"), ("a boat blessing", "decorated boats lined up for a priest, flower garlands on the prows"),
         ("a sailing club open day", "small dinghies tacking in the breeze, families on the pontoon"), ("a fireworks night by the river", "rockets bursting over the water, crowds along the quay")]
duck_races = 0
for l in L:
    if 'rubber duck race' in l:
        duck_races += 1
        if duck_races > 2:
            ev, det = R.choice(RIVER)
            l = re.sub(r'a rubber duck race on the river', ev + ' on the river', l)
            l = l.replace('thousands of yellow ducks bobbing downstream, a cheering crowd on the bridge', det)
    for w in WHIM:
        if l.rstrip('.').endswith(', ' + w):
            seen[w] += 1
            if seen[w] > (2 if 'duck' in w else KEEP):
                l = l[: l.rindex(', ' + w)] + ', ' + EX[ei % len(EX)] + ('.' if l.endswith('.') else ''); ei += 1
            break
    out.append(l)
open(path, 'w', encoding='utf8', newline='\n').write('\n'.join(out) + ('\n' if L and L[-1] == '' or True else ''))
print('duck lines left:', sum('duck' in x.lower() for x in out), '| lines changed:', sum(a != b for a, b in zip(L, out)))
