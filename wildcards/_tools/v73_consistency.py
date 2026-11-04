"""v73 consistency pass (item 59). Idempotent; --restore puts originals back (backup in _tools/backup_v72/).
 1. city_*: time and weather are drawn as consistent pairs (city_conditions, city_night_conditions); no night with a windy DAY, no midday with fog
 2. animals: penguins and flightless birds (ratites, kakapo) get their own species pools, behaviours and scenes, so they never fly; chicks wording removed from the flying-bird group pools
 3. condition_clothing_*: the clothing subject no longer carries its own random wear state (condw_ copies of the wear prompt chain without 'It is __wear_condition__' and *_wear__ details)
Run it LAST, after any rebuild, together with v71_build.py and the v72 scripts."""
import os, re, sys, shutil
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from paths import FINAL
BK = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'backup_v72')
REF = re.compile(r'__([A-Za-z0-9_\-/]+)__')
def P(n): return os.path.join(FINAL, n + '.txt')
def rd(n): return [l.rstrip('\r\n') for l in open(P(n), encoding='utf8')]
def wr(n, lines): open(P(n), 'w', encoding='utf8', newline='\n').write('\n'.join(lines) + '\n')
def backup(n):
    os.makedirs(BK, exist_ok=True)
    if os.path.exists(P(n)) and not os.path.exists(os.path.join(BK, n + '.txt')): shutil.copy(P(n), os.path.join(BK, n + '.txt'))
NEW = []   # files created by this script (removed on --restore)
def new(n, lines): wr(n, lines); NEW.append(n)

def restore():
    if not os.path.isdir(BK): print('no backup'); return
    for f in os.listdir(BK): shutil.copy(os.path.join(BK, f), os.path.join(FINAL, f))
    for n in open(os.path.join(BK, '_created.txt')).read().split() if os.path.exists(os.path.join(BK, '_created.txt')) else []:
        if os.path.exists(P(n)): os.remove(P(n))
    print('restored')

def city():
    TIMES = ['early morning light with long shadows', 'bright midday light', 'golden hour with warm low light', 'blue hour just after sunset', 'deep night with lit windows', 'soft late afternoon light']
    WX = ['clear dry air', 'light drizzle', 'heavy rain with umbrellas', 'fresh snow on the ground', 'warm still air', 'a windy day with blowing leaves', 'thin fog between the buildings', 'wet shining ground just after rain']
    def windy(t):
        if t.startswith('deep night'): return 'a windy night with blowing leaves'
        if t.startswith('blue hour'): return 'a windy evening with blowing leaves'
        if t.startswith('early morning'): return 'a windy morning with blowing leaves'
        return 'a windy day with blowing leaves'
    NO = {'bright midday light': {'light drizzle', 'heavy rain with umbrellas', 'thin fog between the buildings'},
          'golden hour with warm low light': {'heavy rain with umbrellas', 'thin fog between the buildings'},
          'soft late afternoon light': {'heavy rain with umbrellas'}}
    def combos(times):
        out = []
        for t in times:
            for w in WX:
                if w in NO.get(t, ()): continue
                out.append(f'{t}, with {windy(t) if w.startswith("a windy") else w}')
        return out
    new('city_conditions', combos(TIMES))
    new('city_night_conditions', combos(['deep night with lit windows', 'blue hour just after sunset']))
    n = 0
    for f in sorted(os.listdir(FINAL)):
        if f.startswith('city_') and f.endswith('_prompt.txt'):
            ls = rd(f[:-4]); tag = 'city_night_conditions' if '_night_' in f or f.startswith('city_night') else 'city_conditions'
            new_ls = [l.replace('__city_time__, with __city_weather__', f'__{tag}__') for l in ls]
            if new_ls != ls: backup(f[:-4]); wr(f[:-4], new_ls); n += 1
    print('city: prompts changed', n)

def species_split(pool, take, newpool):
    ls = rd(pool); tk = [l for l in ls if l.strip() in take]; rest = [l for l in ls if l.strip() not in take]
    if not tk: return 0
    backup(pool); new(newpool, tk); wr(pool, rest); return len(tk)

def weighted(prompt, extra_line, ratio):
    ls = rd(prompt)
    if extra_line in ls: return
    backup(prompt); wr(prompt, ls * ratio + [extra_line])

def animals():
    # --- penguins out of the waterbird pool
    pen = [l.strip() for l in rd('animal_waterbirds_and_seabirds') if 'Penguin' in l]
    k = species_split('animal_waterbirds_and_seabirds', set(pen), 'animal_penguins')
    if os.path.exists(P('animal_penguins')):
        new('ani_penguin_group', ['a colony on the rocks', 'a pair standing together', 'a huddle of birds against the wind', 'a lone bird at the water\'s edge', 'a small group walking in a line'])
        new('ani_penguin_behaviour', ['waddling in a line across the ground', 'standing upright and watchful', 'porpoising through the water', 'leaning into the wind', 'preening its feathers', 'calling with its beak raised and its flippers out', 'feeding in the shallows', 'resting with its feet tucked in', 'scratching its head with a foot'])
        new('ani_penguin_scene', ['on an ice shelf at dawn', 'on a rocky shore at sunset', 'on a sandy beach', 'beside open water', 'on a snowfield under a pale sky', 'on black volcanic sand'])
        new('ani_penguin_detail', ['close view of the beak', 'close view of the flippers', 'close view of the feathers', 'close view of the eye'])
        new('ani_penguin_young', ['fluffy chicks following a parent', 'a chick in a nest of stones', 'a downy chick sheltering against a parent'])
        r = 6
        weighted('ani2_waterbirds_and_seabirds_prompt', '__animal_penguins__, __ani_penguin_group__, __ani_penguin_behaviour__, __ani_penguin_scene__.', r)
        weighted('ani2_waterbirds_and_seabirds_closeup_prompt', '__animal_penguins__, __ani_penguin_detail__.', r)
        weighted('ani2_waterbirds_and_seabirds_young_prompt', 'A young __animal_penguins__, which is __ani_penguin_young__, __ani_penguin_scene__.', r)
    # --- flightless birds out of songbirds_and_other_birds and parrots
    fl = {'Cassowary', 'Emu', 'Kiwi', 'Ostrich', 'Rhea'}
    a = species_split('animal_songbirds_and_other_birds', fl, 'animal_flightless_birds')
    if a and os.path.exists(P('animal_parrots')):
        ls = rd('animal_parrots'); kk = [l for l in ls if l.strip() == 'Kakapo']
        if kk: backup('animal_parrots'); wr('animal_parrots', [l for l in ls if l.strip() != 'Kakapo']); wr('animal_flightless_birds', rd('animal_flightless_birds') + kk)
    if os.path.exists(P('animal_flightless_birds')):
        new('ani_flightless_group', ['a lone bird', 'a pair together', 'a small family group', 'a parent with chicks'])
        new('ani_flightless_behaviour', ['striding across open ground', 'pecking at the ground', 'running at speed', 'standing tall and watchful', 'scratching at the soil', 'preening its feathers', 'dust bathing', 'calling with its neck stretched', 'resting in the shade'])
        new('ani_flightless_scene', ['on open grassland at dawn', 'at the edge of a forest clearing', 'on a dry plain', 'beside a waterhole at dusk', 'on a mossy forest floor', 'in light scrub'])
        new('ani_flightless_detail', ['close view of the beak and eye', 'close view of the feathers', 'close view of the strong legs and feet', 'close view of the plumage pattern'])
        new('ani_flightless_young', ['fluffy chicks following a parent', 'a chick in the grass'])
        r = 28
        weighted('ani2_songbirds_and_other_birds_prompt', '__animal_flightless_birds__, __ani_flightless_group__, __ani_flightless_behaviour__, __ani_flightless_scene__.', r)
        weighted('ani2_songbirds_and_other_birds_closeup_prompt', '__animal_flightless_birds__, __ani_flightless_detail__.', r)
        weighted('ani2_songbirds_and_other_birds_young_prompt', 'A young __animal_flightless_birds__, which is __ani_flightless_young__, __ani_flightless_scene__.', r)
    # --- chicks wording in pools whose behaviours include flight; and no 'above open water' for young birds
    for pool, old, newl in (('ani_waterbird_group', 'a parent with chicks', 'a parent keeping watch over the water'), ('ani_raptor_group', 'a bird with its chicks', 'a bird beside its nesting ledge'), ('ani_songbird_group', 'a parent feeding chicks', 'a parent bird carrying food in its beak')):
        ls = rd(pool)
        if old in ls: backup(pool); wr(pool, [newl if l == old else l for l in ls])
    sc = [l for l in rd('ani_waterbird_scene') if l != 'above open water']
    new('ani_waterbird_scene_young', sc)
    y = 'ani2_waterbirds_and_seabirds_young_prompt'; ls = rd(y); backup(y)
    wr(y, [l.replace('__ani_waterbird_scene__', '__ani_waterbird_scene_young__') for l in ls])
    print('animals: penguins', k, 'flightless', a)

def condw():
    # closure of cond_subject_clothing, copies without wear state
    files = {f[:-4] for f in os.listdir(FINAL) if f.endswith('.txt')}
    seen = set(); st = ['wear_prompt']
    while st:
        n = st.pop()
        if n in seen or n not in files: continue
        seen.add(n)
        for l in rd(n): st += REF.findall(l)
    def strip(l):
        l = re.sub(r'\s*It is __wear_condition__\.', '', l)
        l = re.sub(r',\s*__[a-z0-9_]+_wear__', '', l)
        return l
    changed = {n for n in seen if any(strip(l) != l for l in rd(n))}
    # ancestors of changed
    par = True
    while par:
        par = False
        for n in seen - changed:
            if any(r in changed for l in rd(n) for r in REF.findall(l)): changed.add(n); par = True
    for n in sorted(changed):
        new('condw_' + n, [REF.sub(lambda m: f'__condw_{m.group(1)}__' if m.group(1) in changed else m.group(0), strip(l)) for l in rd(n)])
    f = 'cond_subject_clothing'; ls = rd(f); backup(f)
    wr(f, [l.replace('__wear_prompt__', '__condw_wear_prompt__') for l in ls])
    print('condw: copies', len(changed))

if __name__ == '__main__':
    if '--restore' in sys.argv: restore(); sys.exit()
    os.makedirs(BK, exist_ok=True)
    city(); animals(); condw()
    old = open(os.path.join(BK, '_created.txt')).read().split() if os.path.exists(os.path.join(BK, '_created.txt')) else []
    open(os.path.join(BK, '_created.txt'), 'w').write('\n'.join(sorted(set(old) | set(NEW))) + '\n')
    print('created files', len(NEW))
