"""Shared path helper. The tools live in <wildcards folder>/_tools/ and work on the wildcards folder (the parent).
During a build, each gender is built in its own workspace folder (WC_DIR env var) and then merged into the wildcards folder (see build_all.py)."""
import os, sys
TOOLS = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(TOOLS, 'data')
FINAL = os.path.dirname(TOOLS) if os.path.basename(TOOLS) == '_tools' else TOOLS
def wc_dir():
    if os.environ.get('WC_DIR'): return os.environ['WC_DIR']
    if len(sys.argv) > 1 and os.path.isdir(sys.argv[1]): return os.path.abspath(sys.argv[1])
    return FINAL
def gender(): return os.environ.get('WC_GENDER', 'f')
