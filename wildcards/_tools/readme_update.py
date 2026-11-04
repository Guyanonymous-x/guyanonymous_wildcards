"""usage: readme_update.py N PREV TOTAL_FILES TOOL_FILES "intro" "bullet1" "bullet2" ... ; last-but-one arg style: bullets are passed as separate args; changelog line = intro-short via env CL"""
import sys, re, os
N, P, total, tools, intro = sys.argv[1:6]; bullets = sys.argv[6:]; CL = os.environ['CL']
p = '/home/claude/guyanonymous_wildcards/README.md'; s = open(p, encoding='utf8').read()
s = s.replace('**Current version: v%s**' % P, '**Current version: v%s**' % N)
s = s.replace("[What's New in v%s](#whats-new-in-v%s)" % (P, P), "[What's New in v%s](#whats-new-in-v%s)" % (N, N))
s = re.sub(r"about [\d,]+ wildcard text files \([\d,]+ `\.txt` files in \[`wildcards/`\]\(wildcards/\) at v%s, plus [\d,]+ build" % P,
           "about %s wildcard text files (%s `.txt` files in [`wildcards/`](wildcards/) at v%s, plus %s build" % (('{:,}'.format(round(int(total.replace(',', '')), -2))), total, N, tools), s)
new = "## What's New in v%s\n\n%s ([docs/INDEX_v%s.txt](docs/INDEX_v%s.txt), research notes in [docs/RESEARCH_v%s.txt](docs/RESEARCH_v%s.txt)). Since v%s it adds:\n\n%s\n- **Showcase:** 40 prompts at 1024 and 1408 sizes, a key file and 100 sample prompts in [docs/showcase/](docs/showcase/), built by `_tools/v%s_showcase.py`.\n\nThe full list of v%s entry points is in `wildcards/v%s_entry_points.txt`.\n\n" % (N, intro, N, N, N, N, P, '\n'.join('- ' + b for b in bullets), N, N, N)
s = s.replace("## What's New in v%s\n" % P, new + "## What's New in v%s\n" % P, 1)
s = re.sub(r"## What's New in v\d+\n.*?(?=\n## )", '', s, count=0, flags=re.S) if False else s
secs = list(re.finditer(r"## What's New in v\d+\n.*?(?=\n## )", s, re.S))
if len(secs) > 2: s = s[:secs[2].start()] + s[secs[2].end():].lstrip('\n')

s = s.replace("### v%s\n" % P, "### v%s\n%s See [What's New in v%s](#whats-new-in-v%s).\n\n### v%s\n" % (N, CL, N, N, P), 1)
open(p, 'w', encoding='utf8').write(s)
