"""Rebuilds the generated wildcard layers for BOTH genders and merges them into the wildcards folder.  No arguments are required:
      python _tools/build_all.py
   Optional:   python _tools/build_all.py --gender m            (rebuild only that gender, then merge with the other gender's last build)
               python _tools/build_all.py --list                 (show the steps)
               python _tools/build_all.py --only age,body        (run just those steps)
               python _tools/build_all.py --from hair            (run that step and everything after it)
               python _tools/build_all.py <wildcards_folder>     (if the tools are not inside the wildcards folder)
   How it works: each gender is built in its own workspace (_tools/work/f and _tools/work/m) from the SOURCE files; then merge(): a file that comes out
   byte-identical for both genders (and only refers to shared files) stays shared and unprefixed; every other file is written as f_<name> or m_<name>
   with its __references__ rewritten to match."""
import os, sys, subprocess, time, json, re, shutil
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from paths import FINAL, TOOLS
STEPS = [('weights', 'pilot_body.py', 'likelihood-weighted body files (eye/hair colour, build, height, tattoos ...)'),
         ('everyday', 'clothing_everyday.py', 'clothing_everyday (2,500 generated everyday outfits)'),
         ('objects', 'objects_build.py', 'object, furniture and room-item files; acc_props, env_props'),
         ('templates', 'build_templates.py', 'prompt templates, opt_unique, opt_tattoo, clothing_pool'),
         ('outfits', 'build_outfit_lists.py', 'outfit_* attribute lists, outfit_cosplay, outfit_*_mixed'),
         ('age', 'age_build.py', 'age-bracket layer'),
         ('eyewear', 'eyewear_build.py', 'eyewear: acc_glasses + age<lo>_<hi>_opt_eyewear (5,000 lines each)'),
         ('body', 'body_build.py', 'body-type layer'),
         ('access', 'access_build.py', 'accessories, aids, settings and poses by age and body type'),
         ('hair', 'hair_build.py', 'hair-type layer + hair_style'),
         ('clothing', 'clothing_build.py', 'age/body-conditioned clothing + random clothing mix + master prompts')]
OBSOLETE = ["age{b}_" + n for n in "body_build body_compos body_bones musc_shldr musc_arms musc_chest musc_abs musc_hips musc_legs musc_veins neck_muscle neck_crease hair_texture hair_volume prompt_wardrobe".split()]
BR = ["18_24", "25_34", "35_44", "45_54", "55_64", "65_74", "75_84", "85_94", "95_120", "85_120"]
REF = re.compile(r'__([A-Za-z0-9_\-/]+)__')
def manifest(): return json.load(open(os.path.join(HERE, 'data', 'sources_manifest.json')))
def prepare(g, final):
    m = manifest(); work = os.path.join(TOOLS, 'work', g)
    if os.path.exists(work): shutil.rmtree(work)
    os.makedirs(work)
    have = {f[:-4] for f in os.listdir(final) if f.endswith('.txt')}
    def unprefix(data):        # a previous merge rewrote references to f_/m_ names; turn them back into the workspace's plain names
        return REF.sub(lambda mm: f'__{mm.group(1)[2:]}__' if mm.group(1).startswith(g + '_') and mm.group(1) in have else mm.group(0), data.decode('utf8', 'replace')).encode('utf8')
    for f in os.listdir(final):          # option files made by normalize.py in an earlier build (sources may refer to them)
        if f.startswith('opt_inl_') or f.startswith(g + '_opt_inl_'): open(os.path.join(work, f[2:] if f.startswith(g + '_') else f), 'wb').write(unprefix(open(os.path.join(final, f), 'rb').read()))
    for n in m['neutral']: shutil.copyfile(os.path.join(final, n + '.txt'), os.path.join(work, n + '.txt'))
    for n in m['gendered'] + m['f_only' if g == 'f' else 'm_only']:
        p = os.path.join(final, f'{g}_{n}.txt')
        if os.path.exists(p): open(os.path.join(work, n + '.txt'), 'wb').write(unprefix(open(p, 'rb').read()))
    return work
def run_steps(work, g, run):
    env = dict(os.environ, WC_DIR=work, WC_GENDER=g)
    for k, f, d in STEPS:
        if k not in run: continue
        t = time.time(); print(f'  [{g}] {k}: {d}', flush=True)
        r = subprocess.run([sys.executable, os.path.join(HERE, f)], env=env, stdout=subprocess.DEVNULL if os.environ.get('WC_QUIET') else None)
        if r.returncode: sys.exit(f'Step "{k}" failed for gender {g} - see the message above.')
    subprocess.run([sys.executable, os.path.join(HERE, 'normalize.py')], env=env, check=True)
    if 'clothing' in run:
        for pat in OBSOLETE:
            for b in BR:
                p = os.path.join(work, pat.format(b=b) + '.txt')
                if os.path.exists(p): os.remove(p)
def read_all(d): return {f[:-4]: open(os.path.join(d, f), 'rb').read() for f in os.listdir(d) if f.endswith('.txt')}
def merge(final, works):
    files = {g: read_all(w) for g, w in works.items()}; names = set(files['f']) | set(files['m'])
    shared = {n for n in names if n in files['f'] and n in files['m'] and files['f'][n] == files['m'][n]}
    changed = True
    while changed:
        changed = False
        for n in list(shared):
            if any(r not in shared for r in REF.findall(files['f'][n].decode('utf8', 'replace'))): shared.discard(n); changed = True
    out = {n: files['f'][n] for n in shared}; warn = []
    for g in ('f', 'm'):
        for n, data in files[g].items():
            if n in shared: continue
            def sub(mm, g=g, n=n):
                r = mm.group(1)
                if r in shared: return mm.group(0)
                if r not in files[g]: warn.append((f'{g}_{n}', r)); return mm.group(0)
                return f'__{g}_{r}__'
            out[f'{g}_{n}'] = REF.sub(sub, data.decode('utf8', 'replace')).encode('utf8')
    for f in os.listdir(final):
        if f.endswith('.txt'): os.remove(os.path.join(final, f))
    for n, data in out.items(): open(os.path.join(final, n + '.txt'), 'wb').write(data)
    nf = sum(1 for n in out if n.startswith('f_')); nm = sum(1 for n in out if n.startswith('m_'))
    print(f'Merged: {len(shared)} shared files | {nf} f_ files | {nm} m_ files | total {len(out)}')
    for w in warn[:10]: print('  warning: unresolved reference', w)
def main():
    a = sys.argv[1:]; final = FINAL
    for x in a:
        if os.path.isdir(x): final = os.path.abspath(x)
    a = [x for x in a if not os.path.isdir(x)]
    if '--list' in a:
        for i, (k, f, d) in enumerate(STEPS, 1): print(f'{i}. {k:10s} {f:24s} {d}')
        return
    names = [s[0] for s in STEPS]; run = names
    if '--only' in a: run = a[a.index('--only') + 1].split(',')
    if '--from' in a: run = names[names.index(a[a.index('--from') + 1]):]
    bad = [r for r in run if r not in names]
    if bad: sys.exit('Unknown step(s): ' + ', '.join(bad) + '   (use --list)')
    genders = ['f', 'm']
    if '--gender' in a: genders = [a[a.index('--gender') + 1]]
    print('Wildcards folder:', final)
    if '--no-vocab' not in a:
        import vocab_apply; vocab_apply.apply(final)          # expand the root option files (from the saved originals) before the layers are built
    works = {}
    for g in ('f', 'm'):
        if g in genders:
            print(f'\n== building {"female" if g == "f" else "male"} workspace'); w = prepare(g, final) if set(run) == set(names) else os.path.join(TOOLS, 'work', g)
            if set(run) != set(names) and not os.path.isdir(w): w = prepare(g, final)
            run_steps(w, g, run); works[g] = w
        else: works[g] = os.path.join(TOOLS, 'work', g)
    if not all(os.path.isdir(w) for w in works.values()): sys.exit('The other gender has not been built yet - run without --gender first.')
    print('\n== merging'); merge(final, works)
    subprocess.run([sys.executable, os.path.join(HERE, 'neutralize.py'), final], check=True)
    for extra in ('demo_build.py', 'group_build.py', 'shoe_build.py', 'shoe_rename.py', 'style_packs.py', 'art_build.py', 'period_build.py', 'uniform_build.py', 'onesie_build.py', 'tee_sewn_build.py', 'sweater_build.py', 'accessory_build.py', 'garment_build.py', 'garment_wear_build.py', 'garment_shop_build.py', 'surfboard_build.py', 'weapons_build.py', 'armor_build.py', 'chastity_build.py', 'bondage_acc_build.py', 'halloween_build.py', 'assist_build.py', 'bodypres_build.py', 'eyecollar_build.py', 'acc_audit_build.py', 'v40_build.py', 'lk_build.py', 'v41_final.py', 'charcos_build.py', 'subject_objects_build.py', 'wardrobe_index_build.py', 'places_build.py', 'wearmore_build.py', 'tiehair_build.py', 'injury_build.py', 'condition_build.py', 'tan_build.py', 'weather_build.py', 'ethnic_skin_build.py', 'world_build.py', 'v42_final.py', 'v42_people.py', 'v43_build.py', 'v44_build.py', 'v45_build.py', 'v46_build.py', 'v47_build.py', 'v48_build.py', 'v49_build.py', 'v50_build.py','v51_build.py','v52_build.py','v53_build.py','v54_build.py'):
        if os.path.exists(os.path.join(HERE, extra)): subprocess.run([sys.executable, os.path.join(HERE, extra), final], check=True)
    subprocess.run([sys.executable, os.path.join(HERE, 'expand.py'), final, '--check'])
if __name__ == '__main__': main()
