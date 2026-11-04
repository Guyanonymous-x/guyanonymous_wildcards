"""Integrates the two style packs (data/style_packs/illustration_wildcards and photostyle_wildcards) into the wildcards folder.

  * copies every pack file into the folder (prompt_NN_* of the illustration pack become illustration_prompt_NN_*)
  * removes '#' comment lines, converts { } | and N$$ choices into small opt_ext_* files (no { } | stay in any file)
  * keeps the library adult-only: option lines that depict a child or teenager are dropped (lines about the authorship or audience of art,
    e.g. "a child's drawing", "made for children", "a children's picture book illustration", are kept)
  * photographic trait files used in the bridge blocks lose lines that name a gender or relationship, so they cannot clash with the generated person
  * writes the bridge files that connect the packs to the person prompts:
        style_photo_block, style_illustration_block                    (style slots)
        f_prompt_photostyled / m_prompt_photostyled                    (the normal master prompt + a photographic style block)
        f_prompt_illustrated / m_prompt_illustrated                    (+ _by_age versions)   (the person described as an illustration)
Usage: python style_packs.py [wildcards_folder]       (build_all.py runs it last)       export_aoo(outdir) feeds simple_build.py
"""
import os, re, sys, random, zlib, shutil, collections
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from paths import FINAL, DATA
SRC = os.path.join(DATA, 'style_packs')
PACKS = ['illustration_wildcards', 'photostyle_wildcards']

MINOR = re.compile(r"\b(child|children|child's|children's|kid|kids|boy|boys|girl|girls|teen|teens|teenage|teenager|teenagers|toddler|toddlers|toddler's|infant|infants|baby|babies|"
                   r"schoolgirl|schoolboy|schoolchildren|newborn|preschool|kindergarten|adolescent|adolescents|juvenile|youngster|youngsters|youth|youths|minor|minors|"
                   r"nursery|playground|prom|cub scout|scout troop)\b", re.I)
KEEP_MINOR = re.compile(r"(children's (picture book|art class|educational|book)|a child's drawing|a toddler's scribble|made for (toddlers|children))", re.I)
GENDER = re.compile(r"\b(woman|women|man|men|girl|boy|mother|father|mothers|fathers|she|he|her|his|him|lady|ladies|gentleman|bride|groom|couple|husband|wife|daughter|son|sister|brother|"
                    r"male|female|feminine|masculine|nude|naked|bare skin)\b", re.I)
BRIDGE_TRAITS = ['lighting', 'color_palette', 'mood', 'era', 'grain_texture', 'process_color', 'finish', 'editing', 'atmosphere', 'lens', 'camera', 'lens_filter',
                 'focus_dof', 'exposure_key', 'viewpoint', 'distance', 'motion', 'tonality_bw', 'process_bw', 'composition', 'artifacts', 'polish', 'visual_strategy']
GROUP = re.compile(r'\{([^{}]*)\}')
MULTI = re.compile(r'^\s*(\d+)(?:-(\d+))?\$\$(.*?)\$\$(.*)$', re.S)

def rd(p): return [l.rstrip('\n') for l in open(p, encoding='utf8', errors='replace')]

def minor_line(l, name):
    if name.startswith('illustration_childart') or name.startswith('illustration_prompt_26') or name.startswith('illustration_prompt_27'): return False
    return bool(MINOR.search(l)) and not KEEP_MINOR.search(l)

def wr(out, name, lines):
    open(os.path.join(out, name + '.txt'), 'w', encoding='utf8', newline='\n').write('\n'.join(lines) + '\n')

def convert(line, made):
    """replace every { } group by a reference to an opt_ext_* file (created in `made`)"""
    for _ in range(6):
        def sub(m):
            body = m.group(1); mm = MULTI.match(body)
            if mm:
                lo = int(mm.group(1)); hi = int(mm.group(2) or lo); sep = mm.group(3); items = [x.strip() for x in mm.group(4).split('|') if x.strip()]
                rng = random.Random(zlib.crc32(body.encode('utf8'))); combos = set(); tries = 0
                target = 240
                while len(combos) < target and tries < target * 6:
                    tries += 1; k = min(len(items), rng.randint(lo, hi)); combos.add(sep.join(rng.sample(items, k)))
                lines = sorted(combos); rng.shuffle(lines)
            else:
                if '|' not in body: return body
                lines = [x.strip() for x in body.split('|')]
            if all(x == '' for x in lines): return ''
            name = 'opt_ext_%08x' % (zlib.crc32('\n'.join(lines).encode('utf8')) & 0xffffffff); made[name] = lines
            return '__' + name + '__'
        new = GROUP.sub(sub, line)
        if new == line: break
        line = new
    return line

def load_pack_files():
    """-> dict name -> list of lines (comments removed, minor lines dropped), plus a report"""
    files = {}; rep = collections.Counter()
    for pack in PACKS:
        d = os.path.join(SRC, pack)
        for f in sorted(os.listdir(d)):
            if not f.endswith('.txt'): continue
            name = f[:-4]
            if pack == 'illustration_wildcards' and name.startswith('prompt_'): name = 'illustration_' + name
            lines = [l for l in rd(os.path.join(d, f))]
            while lines and lines[-1] == '': lines.pop()
            kept = []
            for l in lines:
                if l.startswith('#'): rep['comment lines removed'] += 1; continue
                if minor_line(l, name): rep['lines about children/teens dropped'] += 1; continue
                short = name.replace('photostyle_', '')
                if pack == 'photostyle_wildcards' and short in BRIDGE_TRAITS and GENDER.search(l): rep['gender/relationship lines dropped from trait files'] += 1; continue
                kept.append(l)
            files[name] = kept
    # rename references to the renamed prompt files
    ren = re.compile(r'__(prompt_\d\w*)__')
    for n in files: files[n] = [ren.sub(lambda m: '__illustration_' + m.group(1) + '__', l) for l in files[n]]
    return files, rep

def bridge(f_prefix_ok=True):
    """bridge files: dict name -> lines"""
    P = lambda t: f'__photostyle_{t}__'
    photo = [f"Photographic style: {P('lighting')}, {P('color_palette')}, {P('mood')}. Camera: {P('camera')}, {P('lens')}. {P('process_color')}, {P('grain_texture')}.",
             f"{P('exposure_key')}, {P('lighting')}, {P('atmosphere')}, {P('finish')}, shot on {P('camera')} with {P('lens')}, {P('focus_dof')}.",
             f"The photograph has {P('era')}, {P('color_palette')}, {P('viewpoint')}, {P('distance')}, {P('editing')}.",
             f"Lit by {P('lighting')}, with {P('atmosphere')}. {P('composition')}. Finish: {P('finish')}, {P('grain_texture')}.",
             f"Photographed {P('distance')}, {P('viewpoint')}. {P('lens')} with {P('lens_filter')}. {P('process_color')}. {P('polish')}.",
             f"{P('lighting')}, {P('mood')}, {P('color_palette')}, {P('artifacts')}, {P('editing')}.",
             f"Black-and-white photograph. {P('tonality_bw')}. {P('process_bw')}. {P('lighting')}. {P('grain_texture')}. {P('lens')}."]
    I = lambda t: f'__illustration_{t}__'
    ill = [f"Rendered {I('medium_production_method')} in {I('medium_dry_media')}, {I('line_quality')}, {I('color_harmony')}, {I('shape_shape_language')}, {I('texture_overall_texture')}.",
           f"{I('medium_production_method')} using {I('medium_wet_media')}. Line: {I('line_weight')}, {I('line_quality')}. Colour: {I('color_temperature')}, {I('color_saturation')}. Light: {I('light_light_source')}.",
           f"Illustration style: {I('shape_stylization')}, {I('line_presence')}, {I('color_color_mode')}, {I('light_shading_method')}, {I('texture_finish')}, {I('dimension_render_look')}.",
           f"{I('medium_printmaking')} look, {I('color_palette_character')}, {I('shape_silhouette')}, {I('texture_grain_type')}, {I('composition_framing')}, {I('mood_emotional_tone')}.",
           f"{I('medium_digital_tool')} work with {I('line_weight')}, {I('color_harmony')}, {I('light_form_rendering')}, {I('texture_brush_texture')}, {I('shape_edge_quality')}.",
           f"In the tradition of {I('lineage_historical_movements')}: {I('medium_production_method')}, {I('color_harmony')}, {I('line_quality')}, {I('texture_overall_texture')}.",
           f"{I('medium_cut_and_constructed')} style, {I('color_palette_character')}, {I('shape_geometry_source')}, {I('texture_pattern')}, {I('mood_era_feel')}."]
    out = {'style_photo_block': photo, 'style_illustration_block': ill}
    for g, who in (('f', 'woman'), ('m', 'man')):
        person = f'__{g}_prompt_master__'
        out[f'{g}_prompt_photostyled'] = [f'__{g}_prompt_master_by_age__ __style_photo_block__', f'__style_photo_block__ __{g}_prompt_master_by_age__', f'__{g}_prompt_master_short__ __style_photo_block__']
        out[f'{g}_prompt_illustrated'] = [f'An illustration of a person. __{g}_prompt_char_physical__ __{g}_prompt_wardrobe__ __{g}_prompt_pose_expression__ __{g}_prompt_setting__ __style_illustration_block__',
                                          f'__style_illustration_block__ The subject: __{g}_prompt_char_physical__ __{g}_prompt_wardrobe__ __{g}_prompt_pose_expression__ __{g}_prompt_setting__',
                                          f'A painted portrait. __{g}_prompt_char_face__ __{g}_prompt_char_hair__ __{g}_prompt_wardrobe__ __{g}_prompt_setting__ __style_illustration_block__']
    return out

def run(final):
    files, rep = load_pack_files(); made = {}; n_out = 0
    for name, lines in files.items():
        if name.startswith('illustration_prompt_') or name.startswith('photostyle_mode_') or name == 'photostyle_master' or any(('{' in l or '|' in l) for l in lines):
            lines = [convert(l, made) for l in lines]
        wr(final, name, lines); n_out += 1
    for name, lines in made.items(): wr(final, name, lines)
    br = bridge()
    for name, lines in br.items(): wr(final, name, lines)
    # drop the prompt_00 reference master (about 1,300 tokens, too long for most uses) only if the user wants; kept
    print(f'style packs: {n_out} files + {len(made)} opt_ext_* + {len(br)} bridge files;', dict(rep))
    return files, made

# ---------------------------------------------------------------------------------------------------------------- all-options-once
def export_aoo(out, prefix='aoo_'):
    """writes the packs into the 'all options once' folder: every option once, random order, names prefixed"""
    files, rep = load_pack_files(); made = {}
    conv = {}
    for name, lines in files.items(): conv[name] = [convert(l, made) for l in lines] if (name.startswith('illustration_prompt_') or name.startswith('photostyle_mode_') or name == 'photostyle_master' or any(('{' in l or '|' in l) for l in lines)) else lines
    conv.update(made); conv.update(bridge())
    names = set(conv); ref = re.compile(r'__([A-Za-z0-9_\-/]+)__'); n = 0
    for name, lines in conv.items():
        if name.startswith(('f_', 'm_')): continue                         # gendered bridge prompts are replaced below
        keep = []; seen = set()
        for l in lines:
            if not l.strip() or l in seen: continue
            seen.add(l); keep.append(ref.sub(lambda m: '__' + prefix + m.group(1) + '__' if m.group(1) in names else m.group(0), l))
        tmpl = name.startswith(('illustration_prompt_', 'photostyle_mode_', 'photostyle_master', 'style_'))
        if not tmpl: random.Random(zlib.crc32(name.encode())).shuffle(keep)
        open(os.path.join(out, prefix + name + '.txt'), 'w', encoding='utf8', newline='\n').write('\n'.join(keep) + '\n'); n += 1
    p = lambda t: f'__{prefix}{t}__'
    open(os.path.join(out, prefix + 'prompt_photostyled.txt'), 'w', encoding='utf8').write('\n'.join([f'{p("prompt_full")} {p("style_photo_block")}', f'{p("style_photo_block")} {p("prompt_full")}']) + '\n')
    open(os.path.join(out, prefix + 'prompt_illustrated.txt'), 'w', encoding='utf8').write('\n'.join(
        [f'An illustration of an adult with {p("hair_color")}, {p("hair_style")}, {p("eye_color")}, {p("skin_tone")}, wearing {p("clothing_color")} {p("clothing_material")} {p("top")} and {p("clothing_color")} {p("bottom")}, {p("pose_action")}, in {p("env_setting")}. {p("style_illustration_block")}',
         f'{p("style_illustration_block")} The subject is an adult with {p("hair_color")}, {p("eye_color")}, {p("skin_tone")}, wearing {p("outfit_everyday")}, {p("pose_action")}, in {p("env_setting")}.']) + '\n')
    return n + 2

if __name__ == '__main__':
    a = [x for x in sys.argv[1:] if os.path.isdir(x)]
    run(os.path.abspath(a[0]) if a else FINAL)
