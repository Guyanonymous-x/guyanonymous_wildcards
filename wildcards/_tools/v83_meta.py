import v83_build as _B, v83_bs as _S, v83_sd as _D
_G = _B.build(); _Bs = _S.load(); _SD = {k: v for k, v in _D.build().items() if not k.endswith('_entry_points')}
_nb = len(_Bs); _nsd = len(_SD); _nl = sum(len(v) for v in _SD.values()); _new = len(_G) - _nsd
import collections
_reg = collections.Counter(x[1] for x in _Bs)
ONELINE = 'global brand style wildcards (%d brands, all eras) and richer illustration and photography styles' % _nb
BULLETS = ["Brand styles (%d brands in %d files, `maker_bs_<brand>`, `maker_brand_style`). Each is one line, 'In the style of <Company>, ...', a distilled description of what that maker's products look like (shapes, materials, finishes, colours, lettering, patterns, mood), under 250 words. Companies, marques, houses and workshops from every era (ancient and 18th century houses to today) and every region: Europe %d, North America %d, East Asia %d, Russia and Eastern Europe %d, South Asia %d, Latin America %d, Oceania %d, Africa %d, Southeast Asia %d, Middle East %d." % (_nb, _new, _reg['Europe'], _reg['North America'], _reg['East Asia'], _reg['Russia and Eastern Europe'], _reg['South Asia'], _reg['Latin America'], _reg['Oceania'], _reg['Africa'], _reg['Southeast Asia'], _reg['Middle East']),
 "Browse by group, region, era or industry: `maker_brand_style_<group>` (cars, transport, fashion, tech, home, media, packaging, heritage, modern and world), `maker_brand_style_region_*`, `maker_brand_style_era_*` (before 1900, 1900-1945, 1946-1979, 1980-present) and `maker_brand_style_industry_*`. Ready prompts: `bs_prompt` and `bs_<group>_prompt`, with subject lists `bs_subject_*` and views `bs_view`.",
 "The existing vehicle maker files (`maker_<make>_style`) now also include the full style description for that make.",
 "Illustration and photography style lists enriched: %d files, %d lines rewritten with full visual descriptions (lineages and movements, media, textures, signature devices, photo eras, processes, cameras, lenses, filters, tonality, finishes, editing, artifacts, grain, lighting, atmosphere and signature photographic styles), same order and same slots." % (_nsd, _nl),
 "A 40-image prompt showcase for this release, in two sets (1024 and 1408 pixel counts) with varied image ratios, steps 50 and cfg 3.75.",
 "100 random sample prompts, one per line with no blank lines."]
README = """Guyanonymous' Wildcards v83 - global brand styles, richer illustration and photography styles
===========================================================================================
Brand styles   maker_bs_<brand> (one line each), maker_brand_style (all), maker_brand_style_<group|region_*|era_*|industry_*>
Prompts        bs_prompt, bs_<group>_prompt, bs_subject_<group>, bs_view, bs_cell_<brand> (short form for grids)
Enriched       illustration_lineage_*, illustration_medium_*, illustration_texture_*, illustration_presets_*, illustration_childart_*, photostyle_era / process / camera / lens / lens_filter / tonality / finish / editing / artifacts / grain / lighting / atmosphere / sig_*
Docs           docs/INDEX_v83.txt, docs/RESEARCH_v83.txt, docs/brands_*.txt, docs/styledetail_*.txt, showcase files
All Options Once includes all of these.
"""
GEN_ROW = '("bs_*","%d","v83 brand style prompts, subjects and short cells."),' % sum(1 for k in _G if k.startswith('bs_'))
DOCS = ['/home/claude/w/docs/INDEX_v83.txt', '/home/claude/w/docs/RESEARCH_v83.txt', '/home/claude/w/docs/BRIEF_v83.txt'] + sorted(__import__('glob').glob('/home/claude/w/docs/brands_*.txt')) + sorted(__import__('glob').glob('/home/claude/w/docs/styledetail_*.txt'))
SAMPLES = [('brand style any', '__bs_prompt__', 40), ('brand style cars', '__bs_cars_eu_prompt__', 8), ('brand style fashion', '__bs_fashion_world_prompt__', 8), ('brand style home', '__bs_home_prompt__', 8), ('brand style world', '__bs_world_a_prompt__', 8), ('brand style heritage', '__bs_heritage_prompt__', 8), ('plain style line', '__maker_brand_style__', 10), ('illustration lineage', '__illustration_lineage_historical_movements__', 5), ('photo era', '__photostyle_era__', 5)]
