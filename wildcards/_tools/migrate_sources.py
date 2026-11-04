"""One-time layout of the SOURCE files in the combined wildcards folder.
   python migrate_sources.py <female_canonical_folder> <male_sources_folder> <target_folder>
   neutral sources keep their names; gendered sources become f_<name> / m_<name>.  Writes data/sources_manifest.json."""
import os, re, sys, json, shutil
HERE = os.path.dirname(os.path.abspath(__file__))
FEM, MAL, OUT = sys.argv[1:4]; os.makedirs(OUT, exist_ok=True)
GENDERED = "body_build body_height body_ratio musc_hips musc_legs acc_jewelry acc_straps health_conditions extrasinphoto heightweightdeform10000 weights_all heights_all height weightkg names clothing_full poses_extended body_buttocks body_nipples pubichair eye_lash style_photographers_portrait".split()
F_ONLY = "WOMANprompt character_female_basic body_breasts body_labia body_labia2 body_vulva body_clitoris make_base make_eyes make_lips make_blush make_hlite hair_baby".split()
M_ONLY = "MANprompt character_male_basic body_pecs body_genitals body_chesthair grooming facial_hair".split()
GEN_RX = [r'^age\d+_\d+_.*$', r'^bt_.*$', r'^hairstyle_[SWCK]$', r'^hairtex_[SWCK]$', r'^hairvol_[SWCK]$', r'^hair_curl_[SWCK]$', r'^countries_ethnic_prompts_[SWCK]$', r'^prompt_.*$', r'^outfit_.*$', r'^opt_.*$', r'^clothing_(pool|random_mix|everyday)$', r'^hair_style$']
neutral = []
for f in sorted(os.listdir(FEM)):
    if not f.endswith('.txt'): continue
    n = f[:-4]
    if any(re.match(g, n) for g in GEN_RX) or n in GENDERED or n in F_ONLY: continue
    neutral.append(n); shutil.copyfile(os.path.join(FEM, f), os.path.join(OUT, f))
for n in GENDERED + F_ONLY: shutil.copyfile(os.path.join(FEM, n + '.txt'), os.path.join(OUT, f'f_{n}.txt'))
for n in GENDERED + M_ONLY:
    p = os.path.join(MAL, f'm_{n}.txt')
    if os.path.exists(p): shutil.copyfile(p, os.path.join(OUT, f'm_{n}.txt'))
    else: print('(no male source file for', n, '- written by the male pilot step instead)')
json.dump({'neutral': neutral, 'gendered': GENDERED, 'f_only': F_ONLY, 'm_only': M_ONLY}, open(os.path.join(HERE, 'data', 'sources_manifest.json'), 'w'), indent=1)
print('neutral sources', len(neutral), '| gendered', len(GENDERED), '| female-only', len(F_ONLY), '| male-only', len(M_ONLY))
