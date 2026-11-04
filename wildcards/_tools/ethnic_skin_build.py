"""Ethnicity descriptors tied to proportionate skin colour.
Files: dem_ethnicity_skin (descriptor + skin colour in one line, every line states a skin colour),
 dem_ethnicity_skin_<profile> (tone pools), and prompts f_WOMANprompt_ethnic_skin / m_MANprompt_ethnic_skin
 (the originals with the independent tone slot replaced by the tied one)."""
import os, re, sys, random, zlib
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from paths import FINAL
def R(*k): return random.Random(zlib.crc32('|'.join(map(str, k)).encode()))
# tone bucket -> leading phrase in dem_tone
B = ['very pale','pale','fair','light','light-medium','olive-medium','medium','tan','golden-brown','warm brown','medium-deep brown','deep brown','very deep brown','dark ebony-brown']
P = {
 'northern_european': dict(zip(B, [3,10,32,28,17,6,2,1,1,0,0,0,0,0])),
 'central_eastern_european': dict(zip(B, [1,5,25,30,22,10,5,1,1,0,0,0,0,0])),
 'southern_european_levant': dict(zip(B, [0,1,6,15,25,28,15,6,3,1,0,0,0,0])),
 'middle_east_north_africa_caucasus': dict(zip(B, [0,0,3,10,20,28,20,10,6,3,0,0,0,0])),
 'central_asia_siberia': dict(zip(B, [0,2,12,25,25,15,12,6,3,0,0,0,0,0])),
 'east_asia': dict(zip(B, [0,3,15,30,25,12,8,4,3,0,0,0,0,0])),
 'southeast_asia': dict(zip(B, [0,0,2,8,15,12,25,18,12,6,2,0,0,0])),
 'south_asia': dict(zip(B, [0,0,1,4,8,10,18,20,18,12,6,3,0,0])),
 'west_central_africa': dict(zip(B, [0,0,0,0,0,0,0,2,4,12,20,32,22,8])),
 'east_horn_africa': dict(zip(B, [0,0,0,0,0,0,2,5,10,25,28,20,8,2])),
 'southern_africa': dict(zip(B, [0,0,0,0,0,0,2,6,12,25,28,18,7,2])),
 'north_african_nile': dict(zip(B, [0,0,0,2,6,12,18,20,16,14,8,4,0,0])),
 'indigenous_americas': dict(zip(B, [0,0,0,3,10,12,22,22,16,10,5,0,0,0])),
 'pacific_islands': dict(zip(B, [0,0,0,0,2,4,12,20,22,24,12,4,0,0])),
 'aboriginal_melanesian': dict(zip(B, [0,0,0,0,0,0,2,4,8,18,28,26,12,2])),
 'arctic': dict(zip(B, [0,0,2,8,20,22,22,14,8,4,0,0,0,0])),
 'latin_caribbean_mixed': dict(zip(B, [0,1,5,12,16,16,18,14,10,6,2,0,0,0])),
 'african_diaspora': dict(zip(B, [0,0,0,0,1,3,8,12,16,22,20,12,5,1])),
 'mixed_creole': dict(zip(B, [0,1,4,8,12,14,16,16,12,9,5,3,0,0])),
 'broad': {b: 1 for b in B},
}
K = [  # (profile, keywords) first match wins
 ('aboriginal_melanesian', ['aboriginal','melanesian','papuan','torres strait','fijian']),
 ('arctic', ['inuit','yupik','aleut','sami']),
 ('pacific_islands', ['polynesian','micronesian','samoan','tongan','maori','tahitian','chamorro','marshallese','native hawaiian','hawaiian local']),
 ('indigenous_americas', ['andean','amazonian','indigenous native','apache','aymara','cherokee','cree','guarani','haida','lakota','mapuche','maya','mixtec','nahua','navajo','ojibwe','quechua','zapotec','mestizo','latin american']),
 ('african_diaspora', ['afro-','garifuna','gullah','haitian','cape verdean']),
 ('latin_caribbean_mixed', ['caribbean','colombian','cuban','dominican','venezuelan','chilean','argentine','texan']),
 ('mixed_creole', ['creole','cajun','mixed','appalachian','nubian']),
 ('north_african_nile', ['egyptian','sudanese','nubian','libyan','tunisian','algerian','moroccan','berber','tuareg','north african']),
 ('east_horn_africa', ['afar','amhara','oromo','somali','tigrayan','horn','luo','maasai','kikuyu','baganda','swahili','malagasy']),
 ('southern_africa', ['zulu','xhosa','sotho','tswana','shona','himba','khoisan']),
 ('west_central_africa', ['akan','hausa','igbo','yoruba','wolof','mandinka','sub-saharan']),
 ('middle_east_north_africa_caucasus', ['persian','kurdish','iraqi','yemeni','gulf arab','assyrian','armenian','georgian','azeri','turkish','levantine','middle eastern','sephardi','baloch','pashtun','hazara','kashmiri']),
 ('south_asia', ['punjabi','sindhi','gujarati','marathi','bengali','assamese','odia','kannada','malayali','tamil','telugu','nepali','sinhalese','bhutanese','south asian','roma']),
 ('southeast_asia', ['balinese','bugis','burmese','dayak','filipino','visayan','igorot','javanese','karen','khmer','lao','malay','minangkabau','shan','thai','vietnamese','hmong','southeast asian','taiwanese indigenous']),
 ('east_asia', ['ainu','cantonese','hakka','hokkien','japanese','korean','manchu','naxi','okinawan','taiwanese','tibetan','yi','zhuang','east asian','mongolian']),
 ('central_asia_siberia', ['buryat','evenki','kazakh','kyrgyz','tajik','turkmen','tuvan','uyghur','yakut','siberian','central asian']),
 ('southern_european_levant', ['albanian','basque','catalan','castilian','cypriot','galician','greek','maltese','portuguese','sardinian','sicilian','southern italian','mediterranean','balkan','macedonian','croatian','bosnian','serbian','romanian','bulgarian']),
 ('central_eastern_european', ['belarusian','czech','hungarian','latvian','lithuanian','polish','russian','slovak','slovenian','slavic','ukrainian','moldovan','estonian','german','austrian','swiss','pennsylvania','baltic','flemish','dutch','french','luxembourgish','northern italian']),
 ('northern_european', ['breton','cornish','danish','english','faroese','finnish','icelandic','irish','norwegian','scottish','swedish','welsh','celtic','nordic','scandinavian']),
]
def prof(name):
    n = name.lower()
    for p, kws in K:
        if any(k in n for k in kws): return p
    return 'broad'
def tone_pools(folder):
    tones = sorted({l.strip() for l in open(os.path.join(folder, 'dem_tone.txt'), encoding='utf8') if l.strip()})
    pools = {b: [] for b in B}
    for t in tones:
        for b in sorted(B, key=len, reverse=True):
            if t.startswith(b + ' skin') and 'undertone' in t: pools[b].append(t); break
    return pools
def build(folder):
    names = sorted({l.strip() for l in open(os.path.join(folder, 'dem_ethnicity.txt'), encoding='utf8') if l.strip()})
    base = sorted({re.sub(r' (ancestry|descent|heritage|lineage|roots|traits|features|phenotype|background|facial structure)$', '', n) for n in names})
    pools = tone_pools(folder); assert all(pools[b] for b in B), [b for b in B if not pools[b]]
    G = {}; lines = []
    for name in names:
        p = P[prof(name)]; r = R('es', name)
        for _ in range(8):  # 8 draws per descriptor, weighted by the profile
            b = r.choices(B, weights=[p[x] for x in B])[0]
            lines.append(f"{name}, with {r.choice(pools[b])}")
    G['dem_ethnicity_skin'] = sorted(set(lines))
    for pn, w in P.items():
        L = []
        for b in B:
            for t in pools[b][:max(1, int(w[b] // 4 + (1 if w[b] else 0))) if w[b] else 0]: L.append(t)
        G[f'dem_skin_profile_{pn}'] = L
    return G
def prompts(folder, prefix=''):
    out = {}
    for src, dst in (('f_WOMANprompt', 'f_WOMANprompt_ethnic_skin'), ('m_MANprompt', 'm_MANprompt_ethnic_skin')):
        p = os.path.join(folder, prefix + src + '.txt')
        if not os.path.exists(p): continue
        t = open(p, encoding='utf8').read()
        pat = re.compile(r'(She|He|They) is __%sdem_ethnicity__ and __%sdem_age__, exhibiting __%sdem_heritage__ with __%sdem_tone__, __%sdem_bone__, and __%sdem_unique__\.' % ((prefix,) * 6))
        pr = {'She': 'Her', 'He': 'His'}
        t, n = pat.subn(lambda m: f"{m.group(1)} is __{prefix}dem_age__, of __{prefix}dem_ethnicity_skin__, with __{prefix}dem_bone__ and __{prefix}dem_unique__.", t, count=1)
        assert n == 1, src
        t = t.replace(f'native of __{prefix}countries__', f'__{prefix}countries_ethnic_prompts__')
        assert 'dem_ethnicity_skin' in t and '__countries__' not in t, src
        out[prefix + dst] = t
    return out
def run(final):
    G = build(final)
    for n, l in G.items(): open(os.path.join(final, n + '.txt'), 'w', encoding='utf8', newline='\n').write('\n'.join(l) + '\n')
    for n, t in prompts(final).items(): open(os.path.join(final, n + '.txt'), 'w', encoding='utf8', newline='\n').write(t)
    print('ethnic skin:', len(G), 'lists;', len(G['dem_ethnicity_skin']), 'lines'); return G
def export_aoo(out, prefix='aoo_'):
    G = build(FINAL); n = 0
    for name, l in G.items():
        keep = list(l); random.Random(zlib.crc32(name.encode())).shuffle(keep)
        open(os.path.join(out, prefix + name + '.txt'), 'w', encoding='utf8', newline='\n').write('\n'.join(keep) + '\n'); n += 1
    for nme, t in prompts(out, prefix).items(): open(os.path.join(out, nme + '.txt'), 'w', encoding='utf8', newline='\n').write(t); n += 1
    return n
if __name__ == '__main__':
    a = [x for x in sys.argv[1:] if os.path.isdir(x)]; run(os.path.abspath(a[0]) if a else FINAL)
