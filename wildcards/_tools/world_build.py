"""World-proportional random person.  Two entry points:
  world_person             BROAD: picks one of 14 world regions in proportion to its adult population, then a country in that region in proportion to population
  world_person_by_country  FINE: picks any of ~190 countries directly in proportion to adult population (identical odds, direct control)
Per region:   world_r_<region>_person        Per country: world_c_<country>_person  (+ world_c_<country>_<W|K|S|C> = that country's ethnic-background lines by hair group)
Each person is a full prompt: sex/gender identity by approximate world shares, age band by the country's age profile (and sex ratio by age), body type from the existing weighted
body tables with a regional factor on heavy builds, hair group and background from the country's own lines.  No photographic style or camera tokens are included.
Adults only (18-120).  Estimates are rough and meant to be edited (world_data.py)."""
import os, sys, re, random, zlib, shutil
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from paths import FINAL
import world_data as WD
HERE = os.path.dirname(os.path.abspath(__file__))
def rg(*k): return random.Random(zlib.crc32('|'.join(map(str, k)).encode()))
def slug(s): return re.sub(r'[^a-z0-9]+', '_', s.lower().replace('è', 'e').replace('ã', 'a').replace('é', 'e').replace('ã', 'a').replace('é', 'e')).strip('_')
src = open(os.path.join(HERE, 'demo_build.py'), encoding='utf8').read()
IDENT = {}; exec(src[src.index('IDENT = {'):src.index('ATTR = {')], {}, (ns := {})); IDENT = ns['IDENT']
def rd(wc, n):
    p = os.path.join(wc, n + '.txt')
    return [l.rstrip('\n') for l in open(p, encoding='utf8') if l.strip()] if os.path.exists(p) else []
def wchoice(r, items, weights):
    return r.choices(items, weights=weights, k=1)[0]
def build(wc):
    rows = WD.parse(); F = {}
    ethn = {g: rd(wc, f'countries_ethnic_prompts_{g}') for g in 'WKSC'}
    cache = {}
    def cached(n):
        if n not in cache: cache[n] = rd(wc, n)
        return cache[n]
    ids = list(IDENT); idw = [IDENT[i][4] for i in ids]
    adult = {}
    for dem, pop, reg, ap in rows: adult[dem] = pop * WD.REGIONS[reg][1]
    for dem, pop, reg, ap in rows:
        sl = slug(dem); lines_by_g = {g: [l for l in ethn[g] if l.startswith(dem + ' ')] for g in 'WKSC'}
        for g, ls in lines_by_g.items():
            if ls: F[f'world_c_{sl}_{g}'] = ls
        groups = [g for g in 'WKSC' if lines_by_g[g]]; gw = [len(lines_by_g[g]) for g in groups]
        n = 90 if pop > 100 else 70 if pop > 20 else 55 if pop > 3 else 45
        r = rg('world', dem); out = []; heavyf = WD.REGIONS[reg][2]
        tries = 0
        while len(out) < n and tries < n * 6:
            tries += 1
            iid = wchoice(r, ids, idw); noun, pron, bases, gid, share = IDENT[iid]
            band = wchoice(r, WD.BANDS, WD.AGEP[ap]); a = 'age' + band
            if iid == 'cis_woman' or bases == 'f': sex = 'f'
            elif iid == 'cis_man' or bases == 'm': sex = 'm'
            else: sex = 'f' if r.random() < WD.FEMALE_SHARE[band] else 'm'
            if iid in ('cis_man', 'cis_woman') or bases in ('f', 'm'):
                pass
            elif False: pass
            if iid == 'cis_man': sex = 'm'
            if iid == 'cis_woman': sex = 'f'
            if iid not in ('cis_man', 'cis_woman') and bases in ('f', 'm'): sex = bases
            # cis person: sex follows the sex ratio for this age band
            if iid in ('cis_man', 'cis_woman'):
                sex = 'f' if r.random() < WD.FEMALE_SHARE[band] else 'm'; iid = 'cis_woman' if sex == 'f' else 'cis_man'; noun, pron, bases, gid, share = IDENT[iid]
            bts = re.findall(r'__%s_%s_prompt_master_([a-z]+)__' % (sex, a), '\n'.join(cached(f'{sex}_{a}_prompt_master')))
            if not bts: continue
            uniq = sorted(set(bts)); w = []
            for b in uniq:
                x = bts.count(b)
                if b in ('heavy', 'vheavy'): x *= heavyf
                elif b in ('thin', 'slim', 'frail'): x *= heavyf ** -.5
                w.append(x)
            bt = wchoice(r, uniq, w)
            master = cached(f'{sex}_{a}_prompt_master_{bt}'); phys = cached(f'{sex}_{a}_prompt_char_physical_{bt}')
            G = wchoice(r, groups, gw)
            ps = [p for p in phys if f'identity_anchored_{G}__' in p] or [p for p in phys if 'identity_anchored_' in p]
            ancs = cached(f'{sex}_{a}_prompt_char_identity_anchored_{G}')
            if not master or not ps or not ancs: continue
            p = r.choice(ps); m = r.choice(master)
            anc = r.choice(ancs).replace(f'__countries_ethnic_prompts_{G}__', f'__world_c_{sl}_{G}__')
            p = re.sub(r'__%s_%s_prompt_char_identity_anchored_[WKSC]__' % (sex, a), lambda _: anc, p)
            line = re.sub(r'__%s_%s_prompt_char_physical_%s__' % (sex, a, bt), lambda _: p, m)
            line = re.sub(r'__[fm]_prompt_style__ ?| ?__prompt_camera_light__', '', line).strip()
            if iid not in ('cis_man', 'cis_woman'):
                ctx = {'he': 'he', 'she': 'she', 'they': 'they'}[pron]
                line = f'Subject: {noun}. __demo_body_{iid}__ ' + line
            out.append(line)
        F[f'world_c_{sl}_person'] = out
    # regional + global pickers
    regs = {}
    for dem, pop, reg, ap in rows: regs.setdefault(reg, []).append(dem)
    radult = {k: sum(adult[d] for d in v) for k, v in regs.items()}
    for reg, ds in regs.items():
        tot = sum(adult[d] for d in ds); lines = []
        for d in ds: lines += [f'__world_c_{slug(d)}_person__'] * max(1, round(600 * adult[d] / tot))
        rg('rl', reg).shuffle(lines); F[f'world_r_{slug(WD.REGIONS[reg][0])}_person'] = lines
    gt = sum(radult.values()); lines = []
    for reg in regs: lines += [f'__world_r_{slug(WD.REGIONS[reg][0])}_person__'] * max(1, round(3000 * radult[reg] / gt))
    rg('gl').shuffle(lines); F['world_person'] = lines
    at = sum(adult.values()); lines = []
    for d in adult: lines += [f'__world_c_{slug(d)}_person__'] * max(1, round(5000 * adult[d] / at))
    rg('gc').shuffle(lines); F['world_person_by_country'] = lines
    F['world_region_list'] = [f'{WD.REGIONS[k][0]}: about {100 * radult[k] / gt:.1f}% of the world\'s adults' for k in regs]
    F['world_country_list'] = [f'{d}: about {100 * adult[d] / at:.2f}% of the world\'s adults' for d in sorted(adult, key=lambda x: -adult[x])]
    return F
def run(final):
    F = build(final)
    for n, l in F.items():
        assert l and not any(re.search(r'[{}|]', x) for x in l), n
        open(os.path.join(final, n + '.txt'), 'w', encoding='utf8', newline='\n').write('\n'.join(l) + '\n')
    print('world:', len(F), 'files;', len(F['world_person']), 'broad lines;', len(F['world_person_by_country']), 'country lines'); return F
def export_aoo(out, prefix='aoo_'):
    """All-options-once: the person prompts need the weighted master files (not part of that set), so it gets the ethnic-background lines by region instead."""
    F = build(FINAL); rows = WD.parse(); n = 0; allb = []
    for reg, (label, _, _) in WD.REGIONS.items():
        lines = []
        for dem, pop, rg_, ap in rows:
            if rg_ == reg:
                for g in 'WKSC': lines += F.get(f'world_c_{slug(dem)}_{g}', [])
        lines = list(dict.fromkeys(lines)); random.Random(zlib.crc32(reg.encode())).shuffle(lines); allb += lines
        open(os.path.join(out, f'{prefix}world_background_{slug(label)}.txt'), 'w', encoding='utf8', newline='\n').write('\n'.join(lines) + '\n'); n += 1
    random.Random(7).shuffle(allb)
    open(os.path.join(out, prefix + 'world_background.txt'), 'w', encoding='utf8', newline='\n').write('\n'.join(allb) + '\n')
    for k in ('world_region_list', 'world_country_list'):
        open(os.path.join(out, prefix + k + '.txt'), 'w', encoding='utf8', newline='\n').write('\n'.join(F[k]) + '\n'); n += 1
    return n + 1
if __name__ == '__main__':
    a = [x for x in sys.argv[1:] if os.path.isdir(x)]; run(os.path.abspath(a[0]) if a else FINAL)
