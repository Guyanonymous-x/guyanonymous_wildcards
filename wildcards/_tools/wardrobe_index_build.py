"""Wardrobe classification index. No renames: groups existing acc_<family>_prompt files by role.
 worn_dress   = shaped to cover or dress the body (footwear, hosiery, handwear, headwear, neckwear, waist, apron)
 adornment    = decoration worn on or attached to the body or clothing (jewellery, charms, hairpieces, body jewels)
 carried      = items carried, held or clipped on (bags, umbrella, fan, cane, wallet, keys, lighter)
 personal_tech = watch, contact lenses, eyewear, assistive items
"""
import os, re, sys, random, zlib
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from paths import FINAL
CLASSES = {
 'footwear_hosiery': ['shoe', 'sock', 'tights'],
 'handwear_headwear_neckwear': ['glove', 'hat', 'scarf', 'necktie', 'handkerchief'],
 'waist_apron': ['belt', 'apron'],
 'adornment': ['earring', 'necklace', 'bracelet', 'ring', 'brooch', 'cufflink', 'bodyjewel', 'charm', 'hairpiece'],
 'carried': ['backpack', 'purse', 'wallet', 'umbrella', 'fan', 'cane', 'pouch', 'keychain', 'lanyard', 'lighter', 'cigcase'],
 'personal_tech': ['watch', 'contact'],
}
def build(folder):
    G = {}; miss = []
    for c, fams in CLASSES.items():
        refs = []
        for f in fams:
            n = f'acc_{f}_prompt'
            if os.path.exists(os.path.join(folder, n + '.txt')): refs.append(f'__{n}__')
            else: miss.append(n)
        G[f'wardrobe_{c}'] = refs
    G['wardrobe_worn_dress'] = G['wardrobe_footwear_hosiery'] + G['wardrobe_handwear_headwear_neckwear'] + G['wardrobe_waist_apron']
    G['wardrobe_accessory_only'] = G['wardrobe_adornment'] + G['wardrobe_carried'] + G['wardrobe_personal_tech']
    G['wardrobe_everything_worn'] = G['wardrobe_worn_dress'] + G['wardrobe_adornment']
    G['v38_entry_points'] = ['__acc_assist_prompt__', '__body_makeup__', '__body_nails__', '__body_piercing__', '__body_art__', '__body_skin__', '__acc_eyewear__', '__costume_char_prompt__', '__obj_subject_prompt__', '__scene_prompt__', '__clothing_garment_more_prompt__', '__f_WOMANprompt_ethnic_skin__', '__acc_tiehw_prompt__', '__hair_state_prompt__', '__acc_medwrap_prompt__', '__body_wound_prompt__', '__acc_chastity_prompt__', '__wx_outfit_prompt__', '__skin_tan_level__', '__condition_prompt__']
    return G, miss
def run(final):
    G, miss = build(final)
    for n, l in G.items(): open(os.path.join(final, n + '.txt'), 'w', encoding='utf8', newline='\n').write('\n'.join(l) + '\n')
    print('wardrobe index:', len(G), 'files; missing', miss); return G
def export_aoo(out, prefix='aoo_'):
    G, miss = build(FINAL); n = 0
    for name, lines in G.items():
        keep = [re.sub(r'__([A-Za-z0-9_\-/]+)__', lambda m: '__' + prefix + m.group(1) + '__', l) for l in lines if 'WOMANprompt' not in l]
        keep = [l for l in keep if all(os.path.exists(os.path.join(out, r + '.txt')) for r in re.findall(r'__([A-Za-z0-9_\-/]+)__', l))]
        if not keep: continue
        open(os.path.join(out, prefix + name + '.txt'), 'w', encoding='utf8', newline='\n').write('\n'.join(keep) + '\n'); n += 1
    return n
if __name__ == '__main__':
    a = [x for x in sys.argv[1:] if os.path.isdir(x)]; run(os.path.abspath(a[0]) if a else FINAL)
