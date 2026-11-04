"""v83 - enriched illustration and photography style lists: copies from _tools_in/sd_* replace the library files (same lines, richer descriptions)."""
import os, sys, glob, re
IN = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data', 'v83_sd'); FINAL = '/home/claude/w/wildcards'
def build(final=None):
    G = {}
    for fn in sorted(glob.glob(IN + '/sd_*/*.txt')):
        name = os.path.basename(fn)[:-4]
        orig = os.path.join(FINAL, name + '.txt')
        new = [l.rstrip('\n') for l in open(fn, encoding='utf8')]
        while new and not new[-1].strip(): new.pop()
        if os.path.exists(orig):
            old = [l.rstrip('\n') for l in open(orig, encoding='utf8')]
            while old and not old[-1].strip(): old.pop()
            if len(old) != len(new): print('LINE MISMATCH skipped', name, len(old), len(new)); continue
        G[name] = new
    G['v83_sd_entry_points'] = []
    return G
if __name__ == '__main__': print(len(build()))
