#!/usr/bin/env python3
"""
Wildcard expander for the photographic-style wildcard library.

Syntax (compatible with the Dynamic Prompts / "wildcards" convention):
  __photostyle_lighting__      -> random line from photostyle_lighting.txt (same folder as this script)
  {a|b|c}                            -> pick one option
  {2$$a|b|c}                         -> pick 2 distinct options, joined with ", "
  {2-4$$; $$a|b|c|d}                 -> pick 2 to 4 options, joined with "; "
  Lines starting with # in a wildcard file are ignored. Nesting is allowed.

Examples:
  python photostyle_expand_prompts.py -n 10
  python photostyle_expand_prompts.py -n 5 -t "__photostyle_mode_signature_hybrid__"
  python photostyle_expand_prompts.py -n 5 --subject "a lighthouse keeper at the top of the stairs"
  python photostyle_expand_prompts.py -n 50 --seed 7 -o prompts.txt
"""
import argparse
import random
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent
_cache = {}


def load(name):
    if name not in _cache:
        path = ROOT / f"{name}.txt"
        if not path.exists():
            raise FileNotFoundError(f"Wildcard file not found: {path}")
        lines = [l.strip() for l in path.read_text(encoding="utf-8").splitlines()]
        _cache[name] = [l for l in lines if l and not l.startswith("#")]
    return _cache[name]


def match_brace(s, i):
    depth = 0
    for j in range(i, len(s)):
        if s[j] == "{":
            depth += 1
        elif s[j] == "}":
            depth -= 1
            if depth == 0:
                return j
    raise ValueError(f"Unbalanced braces in: {s[i:i+80]}")


def split_top(s, sep):
    parts, depth, cur, i = [], 0, [], 0
    while i < len(s):
        if s[i] == "{":
            depth += 1
        elif s[i] == "}":
            depth -= 1
        if depth == 0 and s.startswith(sep, i):
            parts.append("".join(cur))
            cur = []
            i += len(sep)
            continue
        cur.append(s[i])
        i += 1
    parts.append("".join(cur))
    return parts


def choose(body, rng, overrides, depth):
    sections = split_top(body, "$$")
    if len(sections) == 1:
        return expand(rng.choice(split_top(body, "|")), rng, overrides, depth + 1)
    count, joiner = sections[0], ", "
    opts_str = sections[-1]
    if len(sections) == 3:
        joiner = sections[1]
    opts = split_top(opts_str, "|")
    if "-" in count:
        lo, hi = (int(x) for x in count.split("-"))
    else:
        lo = hi = int(count)
    k = min(rng.randint(lo, hi), len(opts))
    picked = rng.sample(opts, k)
    return joiner.join(expand(p, rng, overrides, depth + 1) for p in picked)


def expand(s, rng, overrides, depth=0):
    if depth > 40:
        raise RecursionError("Wildcard nesting too deep (circular reference?)")
    out, i = [], 0
    while i < len(s):
        if s[i] == "{":
            j = match_brace(s, i)
            out.append(choose(s[i + 1:j], rng, overrides, depth))
            i = j + 1
        elif s.startswith("__", i):
            k = s.find("__", i + 2)
            if k == -1:
                out.append(s[i:])
                break
            name = s[i + 2:k]
            if name in overrides:
                out.append(overrides[name])
            else:
                out.append(expand(rng.choice(load(name)), rng, overrides, depth + 1))
            i = k + 2
        else:
            out.append(s[i])
            i += 1
    return "".join(out)


def tidy(text):
    text = re.sub(r"\s+", " ", text)
    text = re.sub(r"\s+([.,;:])", r"\1", text)
    text = re.sub(r"\.{2,}", ".", text)
    text = re.sub(r"([.;:])\s*\.", r"\1", text)
    # capitalize first letter of each sentence
    text = re.sub(r"(^|[.!?]\s+)([a-z])", lambda m: m.group(1) + m.group(2).upper(), text)
    return text.strip()


def main():
    ap = argparse.ArgumentParser(description="Expand photographic-style wildcard prompts.")
    ap.add_argument("-n", "--count", type=int, default=5)
    ap.add_argument("-t", "--template", default="__photostyle_master__",
                    help='Template string or wildcard, e.g. "__photostyle_mode_atomic_color__"')
    ap.add_argument("--subject", help="Fix the subject instead of drawing one at random")
    ap.add_argument("--seed", type=int)
    ap.add_argument("-o", "--out", help="Write prompts to this file (one per line)")
    args = ap.parse_args()

    rng = random.Random(args.seed)
    overrides = {}
    if args.subject:
        for key in ("photostyle_subject", "photostyle_subj_people",
                    "photostyle_subj_places", "photostyle_subj_objects"):
            overrides[key] = args.subject

    prompts = [tidy(expand(args.template, rng, overrides)) for _ in range(args.count)]
    if args.out:
        Path(args.out).write_text("\n".join(prompts) + "\n", encoding="utf-8")
        print(f"Wrote {len(prompts)} prompts to {args.out}")
    else:
        for p in prompts:
            print(p, end="\n\n")


if __name__ == "__main__":
    main()
