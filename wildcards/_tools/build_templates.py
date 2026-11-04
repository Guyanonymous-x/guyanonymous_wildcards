"""Writes the global (non-age) prompt template files from data/src_templates/*.tpl, plus opt_unique, opt_tattoo and clothing_pool.
   To change prompt wording, edit the .tpl files in data/src_templates (or edit the .txt files directly if you never re-run the build).
   Usage: python build_templates.py [wildcards_folder]"""
import os, sys, shutil
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from paths import wc_dir, DATA, gender
from gender import IS_M, pron
WC = wc_dir(); TPL = os.path.join(DATA, 'src_templates_m' if IS_M else 'src_templates')
for f in sorted(os.listdir(TPL)):
    if f.endswith('.tpl'): shutil.copyfile(os.path.join(TPL, f), os.path.join(WC, f[:-4] + '.txt'))
def wr(name, lines): open(os.path.join(WC, name + '.txt'), 'w', encoding='utf8', newline='\n').write('\n'.join(lines) + '\n')
def art(s): return ("an " if s[0].lower() in "aeiou" else "a ") + s
NOART = {"deep dimples on both cheeks", "striking complete heterochromia", "partial iris heterochromia", "pronounced albinism traits", "widespread vitiligo patches across skin", "marked vitiligo on eyelids", "subtle albino coloring", "congenital facial asymmetry"}
def sentence_file(src, noart=(), some=()):
    out = []
    for l in open(os.path.join(WC, src + '.txt'), encoding='utf8').read().split('\n')[:-1]:
        l = l.strip()
        if not l: out.append(''); continue
        out.append(pron(f"She has some {l}." if l in some else f"She has {l}." if l in noart else f"She has {art(l)}."))
    return out
wr('opt_unique', sentence_file('dem_unique', NOART)); wr('opt_tattoo', sentence_file('mark_tattoo', some={"patchy incomplete tattoo work"}))
wr('clothing_pool', ['__clothing_everyday__'] * 95 + ['__clothing_full__'] * 5)
print('templates written to', WC)
