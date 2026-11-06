"""v109 - art styles from the user's own tests (2026-11-06).
illustration_style_scribble_line_mild: the polished looping-scribble pen portrait look of the user's scribble-portrait test images, saved as an
art style at the user's request. The same description is added to the random style pool illustration_presets_signature_devices."""
import os
MILD = ('a fine black pen-and-ink illustration drawn as one long looping, scribbling line, a realistic likeness with precise eyes, brows and mouth, '
        'dense scribbled hatching and tangled loops building the dark hair and dark clothing, lighter skin made of loose overlapping loops and fine curved '
        'strokes, wide loose looping strokes and stretched ellipses swirling around the figure across a pure white background, high-contrast black line '
        'on white, energetic yet polished')
def fix(G, final):
    key = 'illustration_presets_signature_devices'
    if key not in G: G[key] = [l.rstrip('\n') for l in open(os.path.join(final, key + '.txt'), encoding='utf8') if l.strip()]
    if MILD not in G[key]: G[key] = G[key] + [MILD]
    G['illustration_style_scribble_line_mild'] = [MILD]
    return G
