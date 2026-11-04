"""v73 item 54: expression intensity tiers. Rebuilds facialExpressionsFor_v10 and pose_emotion from data/expr_tiers.py
(68 emotions x mild / strong / extreme, each described physically: mouth, eyes, brows, head or shoulders; the emotion name stays as the label).
Also writes expr_mild, expr_strong, expr_extreme for manual intensity choice. Tier weights in the two main files: mild 3, strong 3, extreme 1.
Idempotent; --restore puts the old files back (backup in _tools/backup_v72/)."""
import os, sys, shutil
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__))); sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data'))
from paths import FINAL
from expr_tiers import T
BK = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'backup_v72')
P = lambda n: os.path.join(FINAL, n + '.txt')
def wr(n, ls): open(P(n), 'w', encoding='utf8', newline='\n').write('\n'.join(ls) + '\n')
if '--restore' in sys.argv:
    for n in ('facialExpressionsFor_v10', 'pose_emotion'):
        if os.path.exists(os.path.join(BK, n + '.txt')): shutil.copy(os.path.join(BK, n + '.txt'), P(n))
    for n in ('expr_mild', 'expr_strong', 'expr_extreme'):
        if os.path.exists(P(n)): os.remove(P(n))
    print('restored'); sys.exit()
os.makedirs(BK, exist_ok=True)
for n in ('facialExpressionsFor_v10', 'pose_emotion'):
    if not os.path.exists(os.path.join(BK, n + '.txt')): shutil.copy(P(n), os.path.join(BK, n + '.txt'))
face = {0: [], 1: [], 2: []}; pose = {0: [], 1: [], 2: []}
for emo, tiers in T.items():
    for i, (label, desc) in enumerate(tiers):
        face[i].append(f'{label}, with {desc}'); pose[i].append(f'{label}, shown by {desc}')
for i, n in enumerate(('expr_mild', 'expr_strong', 'expr_extreme')): wr(n, face[i])
W = (3, 3, 1)
wr('facialExpressionsFor_v10', [l for i in range(3) for l in face[i] for _ in range(W[i])])
wr('pose_emotion', [l for i in range(3) for l in pose[i] for _ in range(W[i])])
print('emotions', len(T), 'face lines', sum(len(face[i]) * W[i] for i in range(3)), 'distinct', sum(len(face[i]) for i in range(3)))
