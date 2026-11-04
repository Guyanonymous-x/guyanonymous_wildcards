"""Builds the promo (md + html) and CHANGELOG.txt for a version. Usage: promo_build.py N  (reads data/promo_master.json; releases[0] is the newest). To add a version: add_release(json, 'Version N', [bullets]) is done by promo_add.py."""
import json, re, sys, os, html, markdown
HERE = os.path.dirname(os.path.abspath(__file__)); M = json.load(open(os.path.join(HERE, 'data', 'promo_master.json'), encoding='utf8'))
def bold(line):
    m = re.match(r'^((?:[^.:]|\.(?=\w)){3,80}?[.:])(\s.*)?$', line)
    if line.startswith('**') or not m or not m.group(2) or len(m.group(1)) > 90: return line
    return f'**{m.group(1)}**{m.group(2) or ""}'
def build(n, counts=''):
    rel = M['releases']; cur = rel[0]; prev = int(re.search(r'\d+', cur[0]).group()) - 1
    out = [M['head'].replace('v43', f'v{n}').replace('v42', f'v{n}'), '', '## Short descriptions', '', counts_fix(M['short'], counts), '', f"## What's new since V{prev}", '', f"### {cur[0]} (this release)", '']
    out += ['- ' + bold(b) for b in cur[1]]
    out += ['', '## Features at a glance', '']
    out += [('- ' + bold(re.sub(r'^- ', '', l))) if l.strip() else l for l in M['features'].split('\n')]
    out += ['', '## Naming guide', '', M['naming'], '', '## Getting started', '', re.sub(r'Guyanonymous_Wildcards_v\d+\.zip', f'Guyanonymous_Wildcards_v{n}.zip', M['start']), '', '## Warning: files that point to other files', '', M['warning'], '', '## Social posts and release note', '', re.sub(r'\bv4\d\b', f'v{n}', M['social']), '', '## Full Changelog since V27', '']
    for t, items in rel:
        out += [f'### {t}' + (' (this release)' if t == cur[0] else ''), ''] + ['- ' + bold(b) for b in items] + ['']
    out += ['Since version 36 the files follow one naming structure. See the naming guide above, and `filename_changes.txt` for every old and new name.']
    return '\n'.join(out) + '\n'
def counts_fix(t, c): return t
def plain_changelog(n):
    L = [f"Guyanonymous' Wildcards - Changelog since V27 (current: V{n})", '=' * 60, '']
    for t, items in M['releases']:
        L += [t, '-' * len(t)] + ['* ' + re.sub(r'`', '', b) for b in items] + ['']
    return '\n'.join(L)
if __name__ == '__main__':
    n = int(sys.argv[1]); out = sys.argv[2] if len(sys.argv) > 2 else '/mnt/user-data/outputs'
    md = build(n); open(f'{out}/Guyanonymous_Wildcards_v{n}_promo.md', 'w', encoding='utf8').write(md)
    css = '<style>body{font-family:system-ui,sans-serif;max-width:50em;margin:2em auto;padding:0 1em;line-height:1.55}h1,h2,h3{line-height:1.25}h2{border-bottom:1px solid #8884;padding-bottom:.2em;margin-top:2em}code{background:#8882;padding:.1em .3em;border-radius:3px}</style>'
    open(f'{out}/Guyanonymous_Wildcards_v{n}_promo.html', 'w', encoding='utf8').write(f"<!doctype html><meta charset=\"utf-8\"><title>Guyanonymous' Wildcards v{n}</title>{css}<body>" + markdown.markdown(md, extensions=['extra']))
    open(f'{HERE}/../CHANGELOG.txt', 'w', encoding='utf8').write(plain_changelog(n)); print('ok')
