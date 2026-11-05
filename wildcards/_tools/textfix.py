"""Library-wide text fix (v97). Rewrites trigger nouns that make the image model print words (sign, poster, banner, graffiti, label, tag, logo, lettering, badge...)
into plain visual nouns, and turns engraved names / initials / monograms into quoted invented text. Skips lines that already contain quoted text.
usage: python3 textfix.py [--dry] DIR [DIR...]"""
import re, sys, os, glob, collections
SKIP_PREFIX = ('name_', 'text_', 'sign_', 'maker_', 'bs_', 'pinback_', 'insignia_', 'v94', 'letter_')
KEEP = r'(?<!design )(?<!de)'   # placeholder
R = []
def rule(pat, rep, flags=re.I): R.append((re.compile(pat, flags), rep, pat))
# negations
rule(r',? (?:with )?no (?:readable )?(?:text|words|lettering|writing),?(?= |\.|,|;|$)', '')
# names / initials / monograms (defined text)
rule(r"(?:the )?(?:client|owner|wearer|buyer|customer)'s name", 'the name "__name_person__"')
rule(r"(?:the )?(?:client|owner|wearer|buyer|customer)'s initials", 'the letters "__name_initial__ __name_initial__"')
rule(r'\ba monogram\b', 'a monogram of the letters "__name_initial__ __name_initial__"')
rule(r'\bmonograms\b', 'woven pictorial motifs')
rule(r'\btext-quote tattoo\b', 'tattoo of a short quote reading "__name_merch_slogan__"')
# environment / scene
rule(r'\bhand-painted posters\b', 'hand-painted pictures')
rule(r'(?<!four-)(?<!four )\bposters\b', 'picture panels')
rule(r'(?<!four-)(?<!four )\bposter\b(?! bed)', 'picture panel')
rule(r'\bbanners\b', 'cloth pennants'); rule(r'\bbanner\b', 'cloth pennant')
rule(r'\bmenu boards?\b', 'glowing panel')
rule(r'\bsigns\b(?! of\b)', 'lit panels')
rule(r'\bsign\b(?! (?:of|language|up|in|off|on|that)\b)(?!-)', 'lit panel')
rule(r'\bgraffiti tags\b', 'spray-painted shapes'); rule(r'\bgraffiti\b', 'spray-painted shapes')
rule(r'\bnewspapers\b', 'folded paper sheets'); rule(r'\bnewspaper\b', 'folded paper sheet')
rule(r'\bbillboards?\b', 'large painted panel')
rule(r'\bplacards?\b', 'plain board')
# garments and accessories
rule(r'\bwith stitched lettering\b', 'with stitched borders')
rule(r'\bbadges\b', 'patches'); rule(r'\bbadge\b', 'patch')
rule(r'\blabelled\b', 'detailed')
rule(r'\blabels\b', 'tabs'); rule(r'\blabel holder\b', 'tab holder'); rule(r'\blabel\b', 'tab')
rule(r'\bhang tags?\b', 'small plain tab'); rule(r'(?<!dog )(?<!ear )\btags\b(?! team)', 'tabs'); rule(r'(?<!dog )(?<!ear )\btag\b(?! team)(?!line)', 'tab')
rule(r'\bwordmarks?\b', 'motif'); rule(r'\blogos\b', 'motifs'); rule(r'\blogo\b', 'motif')
rule(r'\bslogans?\b', 'pattern'); rule(r'\blettering\b', 'pattern'); rule(r'\binscriptions\b', 'bands of pattern'); rule(r'\binscribed\b', 'decorated')
rule(r'\bcaptions?\b', 'picture')
QUICK = re.compile(r"posters?|banners?|menu board|signs?\b|graffiti|newspapers?|billboards?|placards?|lettering|badges?|labell?e?d?s?|label|tags?\b|wordmark|logos?|slogans?|inscri|captions?|monogram|text-quote|client's|owner's|wearer's|buyer's|customer's|no (?:readable )?(?:text|words|lettering|writing)", re.I)
def fix_line(l):
    if not QUICK.search(l): return l, ()
    if '"' in l or '__name_' in l or '__text_' in l: return l, ()
    hits = []
    for rx, rep, pat in R:
        l2 = rx.sub(rep, l)
        if l2 != l: hits.append(pat); l = l2
    return l, hits
def run(dirs, dry=False):
    stat = collections.Counter(); nfiles = 0; nlines = 0
    for d in dirs:
        for f in glob.glob(os.path.join(d, '*.txt')):
            b = os.path.basename(f)
            b2 = b[4:] if b.startswith('aoo_') else b
            if b2.startswith(SKIP_PREFIX) or any(s in b2 for s in ('badge', 'pinback', 'lapelpin', 'patch', 'sticker')): continue
            src = open(f, encoding='utf8').read().split('\n'); out = []; ch = False
            for l in src:
                n, h = fix_line(l)
                if h: ch = True; nlines += 1
                for p in h: stat[p] += 1
                out.append(n)
            if ch:
                nfiles += 1
                if not dry:
                    seen = []; ded = list(dict.fromkeys(out))   # re-dedupe after rewrites
                    open(f, 'w', encoding='utf8').write('\n'.join(ded))
    return nfiles, nlines, stat
if __name__ == '__main__':
    a = sys.argv[1:]; dry = '--dry' in a; dirs = [x for x in a if x != '--dry']
    nf, nl, st = run(dirs, dry); print('files', nf, 'lines', nl, 'dry' if dry else 'written')
    for p, n in st.most_common(): print(n, p)
