"""Creates data/src_templates_m/*.tpl (male prompt templates) from the female ones: pronoun/noun swap plus male-specific sections
(facial hair, grooming instead of makeup, hair paragraph without 'baby hairs').  Run once; the results are stored in data/src_templates_m."""
import os, re, sys
os.environ['WC_GENDER'] = 'm'
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gender import pron
HERE = os.path.dirname(os.path.abspath(__file__)); SRC = os.path.join(HERE, 'data', 'src_templates'); OUT = os.path.join(HERE, 'data', 'src_templates_m'); os.makedirs(OUT, exist_ok=True)
HAIR = ["His hair has __hair_line__, and he wears it as __hair_style__. The curl pattern is __hair_curl__, and the strands are __hair_texture__, with __hair_volume__ and __hair_shine__.{ His hair is moving: __hair_motion__.|||}",
        "He wears __hair_style__. His hair has __hair_curl__, and the hair itself shows __hair_texture__, __hair_volume__ and __hair_shine__. At the forehead there is __hair_line__.",
        "His hairstyle is __hair_style__. The curl pattern is __hair_curl__, the texture is __hair_texture__, and the hair has __hair_volume__ with __hair_shine__; the hairline shows __hair_line__.{ His hair is moving: __hair_motion__.||||}"]
for f in sorted(os.listdir(SRC)):
    if not f.endswith('.tpl'): continue
    L = [l for l in open(os.path.join(SRC, f), encoding='utf8').read().split('\n') if l.strip()]
    name = f[:-4]
    if name in ('prompt_style', 'prompt_camera_light'): out = L                      # identical for both genders -> shared files
    elif name == 'prompt_char_hair': out = HAIR
    else:
        out = [pron(l) for l in L]
        if name == 'prompt_char_face': out = [l.rstrip() + ' His lower face has __facial_hair__.' for l in out]
        if name == 'prompt_char_details':
            out = [re.sub(r"\{ His makeup is [^}]*\}", "{ His grooming: __grooming__.||}", l) for l in out]
            out = [re.sub(r"\{ He wears makeup with [^}]*\}", "{ His grooming: __grooming__.|||}", l) for l in out]
    open(os.path.join(OUT, f), 'w', encoding='utf8', newline='\n').write('\n'.join(out) + '\n')
    if name in ('prompt_char_face', 'prompt_char_details', 'prompt_char_identity_independent', 'prompt_wardrobe'): print('##', name); [print('  ', x[:330]) for x in out[:2]]
