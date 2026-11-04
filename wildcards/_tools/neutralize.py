"""Cross-file neutrality pass (runs after the merge, before demo_build).  A file may only control the thing it is about.
Colour words in files that are NOT about that colour contradict the files that are:  hair_color / eye_color / dem_tone / countries_ethnic_prompts decide the colours of hair, eyes and skin.
So in every OTHER body file the colour words are removed or made relative ("darker than the surrounding skin", "the same colour as the hair").
Also: aging words are removed from young age brackets and 'youthful' words from old brackets (replaced by another line of the same file, so line counts stay).
Not touched on purpose: clothing / shoes / props / settings / makeup / nail polish / tattoo ink / lighting colours (those are their own objects), eye-white and gum colours (anatomy independent of skin tone),
and the explicit anatomy files (body_nipples ...) and medical conditions, which are listed in docs/CROSS_FILE_AUDIT.txt."""
import os, re, sys, random
from paths import FINAL
WC = sys.argv[1] if len(sys.argv) > 1 and os.path.isdir(sys.argv[1]) else FINAL
def fam(n):
    n = re.sub(r'^(f_|m_)', '', n); n = re.sub(r'^age\d+_\d+_', '', n)
    n = re.sub(r'_(thin|slim|avg|athl|curvy|heavy|vheavy|musc|frail)$', '', n); n = re.sub(r'^bt_[a-z]+_[a-z]_', 'bt_', n); return n
R = lambda p, r: (re.compile(p, re.I), r)
RULES = {
 r'^head_jaw$': [R(r'\bmasculine\b', 'strong')],
 r'^nose_bridge$': [R(r'\beuropean\b', 'defined')],
 r'^eye_brow$': [R(r'\b(?:grey|gray|white|silver)\b', 'faded'), R(r'\bpale blonde invisible\b', 'faint, nearly invisible'), R(r'\bdyed dark bold\b', 'dyed bold'), R(r'\b(?:dark|light|black|blonde?) ', '')],
 r'^eye_lash$': [R(r'\b(?:grey|gray)\b', 'faded'), R(r'\bwhite albino\b', 'very faint, unpigmented'), R(r'\bfine light-colored\b', 'fine'), R(r'\b(?:pale|dark|black|blonde?|light) ', ''), R(r'\bblack ', '')],
 r'^facial_hair$': [R(r'\b(?:salt-and-pepper|white|gray|grey|graying|greying) ', 'hair-coloured '), R(r'\blight stubble\b', 'faint stubble')],
 r'^skin_fuzz$': [R(r'\b(?:golden|light|pale|blonde?|dark) ', '')],
 r'^body_chesthair$': [R(r'\bgray-flecked\b', 'age-lightened'), R(r'\bfine blond chest hair\b', 'fine sparse chest hair'), R(r'\bwhite chest hair\b', 'sparse chest hair'), R(r'\bthick dark\b', 'thick'), R(r'\blight stubble\b', 'faint stubble')],
 r'^pubichair$': [R(r'\bdense dark curly\b', 'dense curly'), R(r'\bgraying\b', 'thinning'), R(r'\bfine light\b', 'fine sparse'), R(r'\bwith light regrowth\b', 'with faint regrowth')],
 r'^hair_shine$': [R(r'chalk-white sheen', 'chalky sheen'), R(r'silver-grey sheen', 'flat sheen')],
 r'^hairtex_[A-Z]$': [R(r'\bgrey ', '')],
 r'^head_temple$': [R(r'\bdark-shadowed\b', 'deeply shadowed'), R(r'\bpale veined\b', 'thin veined')],
 r'^head_cheek$': [R(r'\brosy cheeks\b', 'cheeks with a warm flush'), R(r'\bdark-shadowed\b', 'deeply shadowed'), R(r'\bsallow hollow\b', 'drained hollow'), R(r'\bsoft pale\b', 'soft smooth')],
 r'^hand_knuckl$': [R(r'\bred (inflamed|irritated)\b', r'\1'), R(r'\bdark-pigmented\b', 'darker-pigmented'), R(r'\bwhite bony\b', 'bony')],
 r'^hand_nails$': [R(r'\bthick dark stained\b', 'thick stained'), R(r'\bthick yellow ridged\b', 'thick ridged'), R(r'\bglossy pink natural\b', 'glossy natural'), R(r'\bclean short pale natural\b', 'clean short natural'),
                   R(r'\bdirty dark-rimmed\b', 'dirty grime-rimmed'), R(r'\bpale brittle\b', 'brittle')],
 r'^lip_fullness$': [R(r'\bpale ', ''), R(r'\bsoft pink lips\b', 'soft lips')],
 r'^lip_cupid$': [R(r'\bpale ', '')],
 r'^lip_corners$': [R(r'\bred mouth corners\b', 'inflamed mouth corners'), R(r'\bdark-pigmented\b', 'darker-pigmented')],
 r'^eye_lid$': [R(r'\bdiscolored dark\b', 'discolored, darker-pigmented'), R(r'\bwrinkled dark eyelid bags\b', 'wrinkled shadowed eyelid bags'), R(r'\bdark shadowed\b', 'shadowed'), R(r'\bred inflamed\b', 'inflamed')],
 r'^nose_philtr$': [R(r'\bflat pale\b', 'flat'), R(r'\bswollen red\b', 'swollen inflamed')],
 r'^(?:mark|skin)_scars$': [R(r'\bjagged pale scar (on|across) (chin|cheek)\b', r'jagged scar \1 \2, lighter than the surrounding skin'), R(r'\bfaded pale scar (on chin|line on cheek)\b', r'faded scar \1, lighter than the surrounding skin'),
                  R(r'\bfaded pale body scar\b', 'faded body scar, lighter than the surrounding skin'), R(r'\bthick dark hyperpigmented scar\b', 'thick hyperpigmented scar, darker than the surrounding skin'),
                  R(r'\bdark hyperpigmented scar mark\b', 'hyperpigmented scar mark, darker than the surrounding skin'), R(r'\bfresh red healed scar line\b', 'fresh healed scar line, deeper in colour than the surrounding skin'),
                  R(r'\bsmooth faint white scar line\b', 'smooth faint scar line, lighter than the surrounding skin')],
 r'^(?:bt_)?musc_veins$': [R(r'\b(?:pale|dark|blue|green)(?: green| blue)? (?=veins?|venous|veining|vascular|vein)', ''), R(r'\bpale translucent skin\b', 'translucent-looking skin'), R(r'\bpale thin skin\b', 'thin skin'),
                  R(r'\bbeneath translucent skin\b', 'beneath thin, translucent-looking skin')],
 r'^(?:heightweightdeform10000|weights_all|heights_all)$': [R(r'\bpale or raised\b', 'flat or raised'), R(r'\bred-purple birthmark\b', 'birthmark deeper in colour than the surrounding skin'), R(r'\bpurple stretch marks\b', 'stretch marks'),
                  R(r'\ba pale complexion\b', 'a drained complexion'), R(r'\bpale, tired\b', 'drained, tired'), R(r'\bloose pale skin\b', 'loose thin skin'), R(r'\bthin, pale frame\b', 'thin, delicate frame'),
                  R(r'\bgaunt, pale, thin frame\b', 'gaunt, thin frame'), R(r'\breddish or pale burn scars\b', 'burn scars'), R(r'\bred moon-shaped face\b', 'moon-shaped face'),
                  R(r'\bdark velvety skin patches\b', 'velvety skin patches, darker than the surrounding skin'), R(r'\blight brown flat spots\b', 'flat spots, slightly darker than the surrounding skin'),
                  R(r'\bwhite or pale blond hair\b', 'unpigmented hair'), R(r'\bfair hair\b', 'fine hair'), R(r'\bbluish-gray tinted eyes\b', 'unusually tinted eyes'), R(r'\bmilky white or pale blue eyes\b', 'cloudy, milky eyes'),
                  R(r'\bblack or skin-toned artificial hand\b', 'skin-toned artificial hand'), R(r'\bblack or skin-colored patch\b', 'plain patch'), R(r'\bred, scaly, raised plaques with silvery flakes\b', 'scaly, raised plaques with flaking'),
                  R(r'\bpale\b', 'drained')],
 r'^health_conditions$': [R(r'brilliant ice-blue eyes', 'strikingly vivid eyes'), R(r'a distinct streak or patch of white hair near the front hairline', 'a distinct streak or patch of pigment-free hair near the front hairline')],
}
AGEING = re.compile(r'\b(aging|ageing|aged|elderly|sagging|wrinkled|age spots?|liver spots?)\b', re.I)
YOUTH = re.compile(r'\b(youthful|baby-soft|baby-smooth|baby soft)\b', re.I)
AGEFILE = re.compile(r'^(?:f_|m_)?age(\d+)_(\d+)_(.+)$')
SKIP_AGE = re.compile(r'^(?:skin_wrinkle|skin_texture|nose_crease|aging_summary|age_years|hair_baby|opt_.*|prompt_.*|acc_.*|aids.*|.*master.*|.*anchored.*|.*independent.*)$')
NOAGE_FAMILIES = {'ear_lobe', 'ear_shape', 'head_brow', 'neck_muscle', 'neck_crease', 'nose_philtr', 'musc_abs', 'eye_lid', 'lip_corners', 'head_cheek', 'head_temple', 'skin_glow'}
def clean(s): return re.sub(r' {2,}', ' ', re.sub(r' ,', ',', s)).strip()
def main():
    changed = 0; leak = 0
    for fn in sorted(os.listdir(WC)):
        if not fn.endswith('.txt'): continue
        n = fn[:-4]; fa = fam(n); path = os.path.join(WC, fn)
        rules = next((r for k, r in RULES.items() if re.match(k, fa)), None)
        lines = open(path, encoding='utf8').read().split('\n'); new = lines
        if rules:
            new = []
            for l in lines:
                o = l
                for rx, rep in rules: l = rx.sub(rep, l)
                new.append(clean(l) if l != o else l)
        bt = re.match(r'^(?:f_|m_)?bt_[a-z]+_([ymo])_(.+)$', n)
        if bt and bt.group(1) in 'yo':          # body-type layers are split young / middle / old
            bad = AGEING if bt.group(1) == 'y' else YOUTH
            good = [l for l in new if l.strip() and not bad.search(l)]
            if good and any(bad.search(l) for l in new):
                Rn = random.Random(sum(map(ord, n))); out = []
                for l in new:
                    if l.strip() and bad.search(l): out.append(Rn.choice(good)); leak += 1
                    else: out.append(l)
                new = out
        elif not AGEFILE.match(n) and not bt and fa in NOAGE_FAMILIES:   # files that are used for every age: no age words at all
            good = [l for l in new if l.strip() and not AGEING.search(l)]
            if good and any(AGEING.search(l) for l in new):
                Rn = random.Random(sum(map(ord, n))); out = []
                for l in new:
                    if l.strip() and AGEING.search(l): out.append(Rn.choice(good)); leak += 1
                    else: out.append(l)
                new = out
        m = AGEFILE.match(n)
        if m:
            lo = int(m.group(1)); base = re.sub(r'_(thin|slim|avg|athl|curvy|heavy|vheavy|musc|frail)$', '', m.group(3))
            if not SKIP_AGE.match(base):
                bad = AGEING if lo < 45 else YOUTH if lo >= 55 else None
                if bad:
                    good = [l for l in new if l.strip() and not bad.search(l)]
                    if good:
                        Rn = random.Random(sum(map(ord, n)))
                        out = []
                        for l in new:
                            if l.strip() and bad.search(l): out.append(Rn.choice(good)); leak += 1
                            else: out.append(l)
                        new = out
        if new != lines: open(path, 'w', encoding='utf8', newline='\n').write('\n'.join(new)); changed += 1
    print(f'neutralize: {changed} files changed; {leak} age-inconsistent lines replaced')
if __name__ == '__main__': main()
