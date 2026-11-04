"""Gender switch for the build scripts (set by build_all.py through the WC_GENDER environment variable: f or m)."""
import os, re
G = os.environ.get('WC_GENDER', 'f'); IS_M = (G == 'm'); PFX = G + '_'
_MAP = [(r'\bshe she\b', 'he'), (r'\bShe\b', 'He'), (r'\bshe\b', 'he'), (r'\bHer\b', 'His'), (r'\bher\b', 'his'), (r'\bherself\b', 'himself'), (r'\bwoman\b', 'man'), (r'\bWoman\b', 'Man'), (r'\bwomen\b', 'men'), (r'\bsisters\b', 'brothers'), (r'\bsister\b', 'brother')]
def pron(t):
    """female wording -> male wording when building the male library (no-op for the female build)"""
    if not IS_M: return t
    for a, b in _MAP: t = re.sub(a, b, t)
    return t
