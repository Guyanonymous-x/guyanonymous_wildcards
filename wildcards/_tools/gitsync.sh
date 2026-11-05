#!/bin/bash
# usage: gitsync.sh N "summary"  -> copies library, tools and docs into the git repo, commits "vN: summary", pushes main and release/vN
N=$1; MSG=$2; R=/home/claude/guyanonymous_wildcards; S=/home/claude/w
cd $R || exit 1
find wildcards -maxdepth 1 -name "*.txt" -delete
(cd $S/wildcards && find . -maxdepth 1 -name "*.txt" -print0 | tar cf - --null -T -) | tar xf - -C wildcards/
(cd $S/wildcards/_tools && tar cf - --exclude='backup_*' --exclude=audit --exclude=__pycache__ --exclude='*.bak' --exclude=work .) | tar xf - -C wildcards/_tools
cp -r $S/docs/. docs/; mkdir -p docs/showcase
cp /mnt/user-data/outputs/Guyanonymous_Wildcards_v${N}_showcase_* /mnt/user-data/outputs/Guyanonymous_Wildcards_v${N}_sample_prompts.txt docs/showcase/ 2>/dev/null
git add -A
git commit -q -m "v$N: $MSG" -m "$(printf 'Co-Authored-By: Claude Sonnet 5.5 <noreply@anthropic.com>\nClaude-Session: https://claude.ai/code/session_018KvMVb8DffsnWKkNuF6ARo')"
git push -q origin main 2>&1 | tail -2
git branch -f release/v$N && git push -q -f origin release/v$N 2>&1 | tail -1
git log --oneline | head -2
