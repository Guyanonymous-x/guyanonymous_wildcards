"""Global period dress (period_*).  Per era slice (37 slices from the Palaeolithic to the 2010s, every one mixing regions of the whole world):
period_<key>_garment/_head/_foot/_jewel/_bag/_accessory/_material/_ornament, period_<key>_outfit, period_<key>_prompt;
global pickers period_garment/_head/_foot/_jewel/_bag/_accessory/_material/_ornament/_outfit/_prompt/_era/_era_prompt.
Adult people only.  Original descriptive wording, no brands or real people.  Deterministic."""
import os, sys, re, random, zlib, shutil
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from paths import FINAL
import vocab_period5 as V
SL = V.SL; CAT = dict(G='garment', H='head', F='foot', J='jewel', B='bag', A='accessory')

REG = [
 ('arctic', r'Inuit|Sami|Siberian|Ainu|Arctic|Yup|Chukchi|Aleut|reindeer|sealskin|Nenets|Evenki'),
 ('oceania', r'Polynesian|Maori|Hawaiian|Tahitian|Lapita|Pacific|Pasifika|Aboriginal|Australian|Melanesian|Micronesian|Samoan|Tongan|Fijian|Papua|tapa|Oceani'),
 ('americas', r'Peruvian|Andes|Teotihuacan|early Americas|Maya|Aztec|Mexica|Inca|Andean|Toltec|Olmec|Moche|Nazca|Chimu|Tiwanaku|Anasazi|Navajo|Cherokee|Haudenosaunee|Plains|Powhatan|Mississippian|Tupinamba|Brazilian|Mexican|Chicana|Hopewell|Clovis|Paracas|Caral|Taino|Chavin|Wari|Zapotec|Mixtec|Pueblo|Cahokia|Native|Pomo|Chumash|Inuit-Yupik|Caribbean|Harlem|Hollywood|American|Mohawk|Lakota|Apache|Hopi|Amazon'),
 ('africa', r'Sahara|African|Africa|Yoruba|Igbo|Hausa|Ashanti|Ghana|Mali|Songhai|Benin|Kush|Nubian|Meroitic|Aksum|Ethiopian|Zulu|Xhosa|Swahili|Zimbabwe|Kongo|Dahomey|Nok|Sahel|Kanem|Fulani|Maasai|Himba|San |Khoi|Nigerian|Ghanaian|Ife|Ugandan|Kenyan|kente|Igbo-Ukwu|Bantu|Nile|Kerma|Sudan'),
 ('middle_east', r'Judean|Palmyrene|Baghdad|Hellenistic|Egypt|Persia|Sumer|Mesopotam|Babylon|Assyri|Hittite|Phoenic|Canaan|Hebrew|Israelite|Anatolia|Ottoman|Safavid|Qajar|Abbasid|Fatimid|Mamluk|Seljuk|Ilkhanid|Timurid|Moroccan|Almohad|Andalus|Cordob|Nabataean|Arab|Bedouin|Parthian|Sassanian|Sasanian|Achaemenid|Zand|Middle East|Levant|Turkish|Egyptian|Coptic|Berber|Tuareg|Carthagin|Libyan|Kushan|Persian|Parsi|Elam|Phrygian|Lydian|Judaean|Syrian|abaya|Tanzimat|Young Turk|Tutankhamun'),
 ('south_asia', r'Indian|India|Indus|Harappa|Maurya|Gupta|Chola|Pala|Mughal|Rajput|Maratha|Vijayanagara|Delhi|Bengal|Tamil|Kashmir|Sikh|Pakistani|Bollywood|Sri Lanka|Nepal|Tibetan|Bhutan|Mauryan|Satavahana|Sultanate|Awadh|Kolhapuri|sari|dhoti|Gandhara|Vedic|Dravidian|Sabyasachi|chikankari|Pagan|Burmese'),
 ('east_asia', r'Liangzhu|Yamato|Chinese|China|Han |Tang|Song |Ming|Qing|Yuan |Zhou|Shang|Qin |Jin |Sui |Heian|Kamakura|Muromachi|Momoyama|Edo|Meiji|Taisho|Showa|Japan|Joseon|Korea|Goryeo|Silla|Baekje|Yayoi|Jomon|Kofun|Manchu|Shanghai|Hong Kong|Harajuku|Shibuya|K-pop|Lolita|Mongol|Liao|Xiongnu|Xianbei|hanbok|kimono|qipao|Hanfu|Bohai|Nara|Asuka|Gojoseon|Hmong'),
 ('southeast_asia', r'Funan|Mon-Dvaravati|Khmer|Angkor|Javanese|Java|Balinese|Bali|Thai|Siam|Ayutthaya|Burma|Vietnam|Dong Son|Champa|Srivijaya|Majapahit|Filipino|Philippin|Indonesian|Malay|Batik|batik|Lao|Sumatra|Borneo|Dayak|Toraja|sampot|Southeast Asia'),
 ('central_asia', r'Uyghur|Hunnic|Scythian|Sarmatian|Steppe|steppe|Central Asia|Sogdian|Bactrian|Uzbek|Kazakh|Turkic|Silk Road|Tarim|Khwarezm|Hun |Huns|Kyrgyz|Altai|Pazyryk|Saka|Yuezhi|Tocharian'),
 ('europe', r'Constantinopolitan|Goth |Goth$|Briton|Oak-coffin|Denmark|Florentine|mi-parti|Rhingrave|chemise a la reine|rational dress|morning coat|hobble|Greek|Roman|Celtic|Etruscan|Minoan|Mycenaean|Viking|Norse|Saxon|Norman|Gothic|Tudor|Elizabethan|Georgian|Regency|Victorian|Edwardian|Baroque|Rococo|Renaissance|Burgundian|Venetian|Italian|French|Spanish|English|German|Dutch|Carolingian|Byzantine|Kievan|Russian|Hallstatt|La Tene|Frankish|Gaul|Visigoth|Ostrogoth|Lombard|Ottonian|Plantagenet|Medici|Landsknecht|Cavalier|Puritan|Dandy|dandy|Napoleonic|Biedermeier|Empire|Pre-Raphaelite|Art Nouveau|Art Deco|Jazz Age|flapper|Chanel|punk|grunge|mod |Teddy|hippie|disco|rockabilly|New Look|Edwardian-revival|Alpine|Iceman|Neolithic farmer|Bronze Age Danish|Danish|Scandinav|Irish|Scottish|British|Swiss|Polish|Hungarian|Balkan|Thracian|Dacian|Cypriot|Maltese|Iberian|Basque|Pictish|Frisian|Bohemian|Slavic|Rus |Muscovite|Baltic|Estonian|Finnish|Hanseatic|Hanse|Carnaby|Brummell|Macaroni|sans-culotte|Poiret|Directoire|Gibson|Wiener|Surrealist|Memphis|Y2K|normcore|hipster|streetwear|athleisure|Coachella|Rubik'),
]
REGRX = [(n, re.compile(x)) for n, x in REG]
def region(item):
    for n, rx in REGRX:
        if rx.search(item): return n
    return 'any'
def rg(*k): return random.Random(zlib.crc32('|'.join(map(str, k)).encode()))
def cap(s): return s[:1].upper() + s[1:]
def fit(lines, seed, n=260, lo=210):
    seen = set(); out = []
    for l in lines:
        l = re.sub(r'\b([Aa]) (?=[aeiAEI]|o(?!ne\b))', r'\1n ', l)
        if l and l not in seen: seen.add(l); out.append(l)
    rg(seed).shuffle(out)
    return out[:n]
FR = ['{i}', '{i} made of {m}', '{i} with {o}', '{i} of {m} with {o}', '{i} in {m}, decorated with {o}', '{i} worn with {o} detailing', '{i} with a trim of {m}', '{i} of {m} and {m2}', '{i} patterned with {o} in {m}']
def item_lines(key, cat, items, M, O):
    r = rg('it', key, cat); out = []; reps = max(3, -(-420 // (len(items) * (len(FR) - 1))))
    for i in items:
        for fr in FR:
            for _ in range(reps if fr != '{i}' else 1):
                m, m2 = r.sample(M, 2) if len(M) > 1 else (M[0], M[0]); o = r.choice(O)
                out.append(fr.format(i=i, m=m, m2=m2, o=o))
        if len(out) > 4000: break
    return fit(out, ('it', key, cat))
def combo(items, key, tag, others=()):
    r = rg('co', key, tag); out = list(items)
    for a in items:
        for b in items:
            if a != b: out.append(f'{a} and {b}')
    for _ in range(1500):
        t = r.sample(items, min(3, len(items))); out.append(', '.join(t[:-1]) + ' and ' + t[-1])
    for a in items:
        for o in others: out.append(f'{a} with {o}')
    return fit(out, ('co', key, tag))
def outfit_lines(key, d, mode='coh', n=260):
    r = rg('of', key, mode); out = []
    byreg = {c: {} for c in 'GHFJBA'}
    for c in byreg:
        for it in d[c]: byreg[c].setdefault(region(it), []).append(it)
    def pick(c, rgn):
        pool = byreg[c].get(rgn, []) if mode == 'coh' else d[c]
        if mode == 'coh' and rgn != 'any' and not pool: pool = byreg[c].get('any', [])
        if mode == 'coh' and rgn == 'any': pool = byreg[c].get('any', []) or d[c]
        return r.choice(pool) if pool else None
    for _ in range(n * 8):
        g = r.choice(d['G']); rgn = region(g); parts = [g]
        for c, p, fmt in (('H', .8, 'with %s'), ('F', .75, '%s'), ('J', .7, 'adorned with %s'), ('B', .5, 'carrying %s'), ('A', .5, '%s')):
            if r.random() < p:
                x = pick(c, rgn)
                if x: parts.append(fmt % x)
        line = parts[0] if len(parts) == 1 else ', '.join(parts[:-1]) + ' and ' + parts[-1]
        if r.random() < .4: line += ', worked in ' + r.choice(d['M']) + ' with ' + r.choice(d['O'])
        out.append(line)
    return fit(out, ('of', key, mode), n)
def build():
    F = {}; glob = {k: [] for k in CAT.values()}; gm = []; go = []; gout = []; gpr = []; gmix = []; gmp = []
    for key, d in SL.items():
        lab = d['label']; M, O = d['M'], d['O']
        for c, nm in CAT.items():
            F[f'period_{key}_{nm}'] = item_lines(key, nm, d[c], M, O)
            glob[nm] += [cap(x) if False else x for x in F[f'period_{key}_{nm}'][:40]]
        F[f'period_{key}_material'] = combo(M, key, 'm', O)
        F[f'period_{key}_ornament'] = combo(O, key, 'o', M)
        F[f'period_{key}_outfit'] = outfit_lines(key, d)
        F[f'period_{key}_mix'] = outfit_lines(key, d, 'mix')
        F[f'period_{key}_prompt'] = [f'{x}, in the fashion of {lab}' for x in F[f'period_{key}_outfit']]
        F[f'period_{key}_mix_prompt'] = [f'{x}, in a mixed global style of {lab}' for x in F[f'period_{key}_mix']]
        gmix += [f'{x}, in a mixed global style of {lab}' for x in F[f'period_{key}_mix'][:8]]; gmp += F[f'period_{key}_mix_prompt'][:8]
        gm += F[f'period_{key}_material'][:12]; go += F[f'period_{key}_ornament'][:12]
        gout += [f'{x}, in the fashion of {lab}' for x in F[f'period_{key}_outfit'][:8]]
        gpr += F[f'period_{key}_prompt'][:8]
    for nm, l in glob.items(): F['period_' + nm] = fit(l, ('g', nm), 1500)
    F['period_material'] = fit(gm, 'gm', 1500); F['period_ornament'] = fit(go, 'go', 1500)
    F['period_outfit'] = fit(gout, 'gout', 1500); F['period_prompt'] = fit(gpr, 'gpr', 1500)
    F['period_mix'] = fit(gmix, 'gmix', 1500); F['period_mix_prompt'] = fit(gmp, 'gmp', 1500)
    F['period_era'] = [d['label'] for d in SL.values()]
    F['period_era_prompt'] = [f'__period_{k}_prompt__' for k in SL]
    F['period_era_mix_prompt'] = [f'__period_{k}_mix_prompt__' for k in SL]
    return F
def run(final):
    F = build()
    for n, l in F.items():
        assert l and all(l) and not any(re.search(r'[{}|]', x) or re.match(r'\d+::', x) for x in l), n
        open(os.path.join(final, n + '.txt'), 'w', encoding='utf8', newline='\n').write('\n'.join(l) + '\n')
    small = sorted((len(l), n) for n, l in F.items() if len(l) < 200 and not n.startswith('period_era'))[:5]
    print('period:', len(F), 'files; smallest', small); return F
def export_aoo(out, prefix='aoo_'):
    tmp = os.path.join(out, '_p_tmp'); os.makedirs(tmp, exist_ok=True); F = run(tmp); shutil.rmtree(tmp)
    names = set(F); ref = re.compile(r'__([A-Za-z0-9_\-/]+)__'); n = 0
    for name, lines in F.items():
        keep = list(dict.fromkeys(l for l in lines if l.strip()))
        keep = [ref.sub(lambda m: '__' + prefix + m.group(1) + '__' if m.group(1) in names else m.group(0), l) for l in keep]
        if 'prompt' not in name: random.Random(zlib.crc32(name.encode())).shuffle(keep)
        open(os.path.join(out, prefix + name + '.txt'), 'w', encoding='utf8', newline='\n').write('\n'.join(keep) + '\n'); n += 1
    return n
if __name__ == '__main__':
    a = [x for x in sys.argv[1:] if os.path.isdir(x)]; run(os.path.abspath(a[0]) if a else FINAL)
