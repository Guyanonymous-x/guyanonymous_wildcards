import v82_af as _A
_G = _A.build(); _F, _S = _A.load()
def _n(f): return sum(1 for k in _G if k.startswith('af_' + f + '_'))
_c = {f: sum(1 for (ff, k) in _F if ff == f) for f in _A.FAMS}
ONELINE = 'art forms that are neither illustration nor photography'
BULLETS = ["Sculpture and carving (about %d files, `af_sculpt_`). %d forms: marble, bronze, granite, soapstone, alabaster, wood, chainsaw carving, totem, terracotta, plaster, welded steel, wire, assemblage, mobiles, ice, sand, relief, topiary and stone cairns." % (_n('sculpt'), _c['sculpt']),
"Ceramics, glass and decorative craft (about %d files, `af_craft_`). %d forms: stoneware, porcelain, raku, celadon, majolica, kintsugi, blown and fused glass, lampwork, mosaic, cloisonne, lacquer, marquetry, pyrography, scrimshaw-style engraving, leather, tiles, stucco and terrazzo." % (_n('craft'), _c['craft']),
"Fibre, paper and miniatures (about %d files, `af_fibre_`). %d forms: tapestry, quilt, embroidery, felt, crochet, macrame, lace, batik, quilling, origami, paper cutting, papier-mache, lanterns, dioramas, dollhouse rooms, model railways, puppets and ships in bottles." % (_n('fibre'), _c['fibre']),
"3D renders, toys and installations (about %d files, `af_render_`). %d forms: clay, product, low-poly, voxel, wireframe, toon and glass renders, claymation, felt puppet scenes, brick builds, vinyl toys, neon, LED and mirror-room installations, sand mandalas, chalk art, ice, sugar, fruit and floral art, fireworks and land art." % (_n('render'), _c['render']),
"Each form has its own subjects, materials, techniques, surface finishes, colours, scales, wear and display settings; plaques and labels carry their text in quotation marks.",
"A 40-image prompt showcase for this release, in two sets (1024 and 1408 pixel counts) with varied image ratios, steps 50 and cfg 3.75.",
"100 random sample prompts, one per line with no blank lines."]
README = """Guyanonymous' Wildcards v82 - art forms that are neither illustration nor photography
=====================================================================================
Mixes          af_prompt, af_group_prompt, af_short, af_forms; per family af_<family>_prompt (sculpt, craft, fibre, render)
Per form       af_<family>_<form>_prompt / _look / _short / _group_prompt, with _subject, _material, _technique, _finish, _colour, _scale, _wear and _display
Shared         af_<family>_display, _light, _shot (and _marks for render), af_marks (plaque and label text in quotes)
Docs           docs/INDEX_v82.txt, docs/RESEARCH_v82.txt, docs/artforms_*.txt, docs/showcase files
All Options Once includes all of these.
"""
GEN_ROW = '("af_*","%d","v82 art forms - sculpture, craft, fibre and render."),' % len(_G)
DOCS = ['/home/claude/w/docs/INDEX_v82.txt', '/home/claude/w/docs/RESEARCH_v82.txt', '/home/claude/w/docs/artforms_sculpture.txt', '/home/claude/w/docs/artforms_craft.txt', '/home/claude/w/docs/artforms_textile.txt', '/home/claude/w/docs/artforms_render_install.txt']
SAMPLES = [('sculpture', '__af_sculpt_prompt__', 20), ('craft', '__af_craft_prompt__', 20), ('fibre', '__af_fibre_prompt__', 20), ('render', '__af_render_prompt__', 22), ('mixed', '__af_prompt__', 8), ('group', '__af_group_prompt__', 10)]
