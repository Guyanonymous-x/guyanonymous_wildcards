"""Expand a wildcard prompt into plain text, for tools without wildcard support.
Usage (run inside this folder): python expand_prompt.py prompt_01_core.txt [count] [seed]"""
import re, random, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
def load(name):
    return [l for l in open(os.path.join(HERE, name + ".txt"), encoding="utf-8").read().splitlines() if l.strip()]
def expand(t):
    for _ in range(10):
        t = re.sub(r"\{(\d+)\$\$(.*?)\$\$([^{}]*)\}",
                   lambda m: m.group(2).join(random.sample(m.group(3).split("|"), min(int(m.group(1)), len(m.group(3).split("|"))))), t)
        t = re.sub(r"\{([^{}]*)\}", lambda m: random.choice(m.group(1).split("|")), t)
        t = re.sub(r"__(\w+?)__", lambda m: random.choice(load(m.group(1))), t)
    return t.strip()
def est_tokens(t):
    return int(max(len(t) / 3.8, len(t.split()) * 1.35))
if __name__ == "__main__":
    path = sys.argv[1]; n = int(sys.argv[2]) if len(sys.argv) > 2 else 1
    if len(sys.argv) > 3: random.seed(int(sys.argv[3]))
    src = open(os.path.join(HERE, os.path.basename(path)), encoding="utf-8").read()
    for _ in range(n): print(expand(src) + "\n")
