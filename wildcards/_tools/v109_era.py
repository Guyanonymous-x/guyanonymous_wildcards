"""v109 - era-specific object descriptions (user 2026-11-06). For every object in v109_era_data.ERA:
ob_<key>_era_<period>  how the object looked in that period (before_1800, 1800s, 1900_1945, 1946_1979, 1980_1999, 2000_present)
ob_<key>_period        one random period the object existed in
ob_<key>_full          now era-matched: the period description, then a condition that suits any period (ob_era_condition), and the object's quoted text if it has any
The period description carries form, material and colour together so they agree with the period; the generic colour and date pools are not used."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from v109_era_data import ERA
# Text pools for era objects whose builder had none (quoted text, linked to the name generators).
EXTRA_TEXT = {
 'newspaper': ['with the masthead "__name_newspaper__" across the top and the headline "__name_headline__" below it', 'with the headline "__name_headline__" in large letters across the front page'],
 'ticket': ['printed with "__name_town__" on the first line and "ADMIT ONE" on the second line', 'printed with "__name_town__ to __name_town__" across the middle'],
 'cassette': ['with a label reading "__name_album__" on the first line and "__name_band__" on the second line', 'with a label reading "__name_band__"'],
}
# Paper, cloth and leather goods get a condition pool without dents, chips or polish.
SOFT = {'newspaper', 'magazine', 'book', 'map', 'postcard', 'envelope', 'notebook', 'ticket', 'banknote', 'stamp', 'hat', 'cap', 'coat', 'jacket', 'shoe', 'boot',
        'trainer', 'sandal', 'glove', 'handbag', 'bag', 'backpack', 'rucksack', 'wallet', 'swimsuit', 'apron', 'tie', 'wig', 'tent', 'puppet', 'doll', 'umbrella', 'parasol', 'puzzle'}
# Built-in fixtures (and other fixed fittings) get a condition pool without storage dust or dents.
from v109_fixtures import FIX as _FIX
FIXED = set(_FIX) | {'radiator', 'fireplace', 'bath', 'bathtub', 'toilet', 'sink', 'basin', 'shower', 'atm', 'meter', 'cctv', 'turnstile', 'kiosk', 'letterbox', 'doorbell', 'intercom', 'switchboard', 'chandelier', 'sconce'}
PERIODS = ['before_1800', '1800s', '1900_1945', '1946_1979', '1980_1999', '2000_present']
def fix(G, final):
    def have(k): return k in G or os.path.exists(os.path.join(final, k + '.txt'))
    done = []
    for key, eras in ERA.items():
        if not have('ob_%s_full' % key): raise KeyError('v109_era: no builder for %s' % key)
        bad = [p for p in eras if p not in PERIODS]
        if bad: raise KeyError('v109_era: unknown period %s for %s' % (bad, key))
        for p in PERIODS:
            if eras.get(p): G['ob_%s_era_%s' % (key, p)] = list(eras[p])
        G['ob_%s_period' % key] = ['__ob_%s_era_%s__' % (key, p) for p in PERIODS if eras.get(p)]
        if key in EXTRA_TEXT and not have('ob_%s_text' % key): G['ob_%s_text' % key] = list(EXTRA_TEXT[key])
        text = ', __ob_%s_text__' % key if have('ob_%s_text' % key) else ''
        cond = 'ob_era_condition_soft' if key in SOFT else 'ob_era_condition_fixed' if key in FIXED else 'ob_era_condition'
        G['ob_%s_full' % key] = ['__ob_%s_period__, __%s__%s' % (key, cond, text)]
        done.append(key)
    G['ob_era_condition'] = ['in good condition', 'in near-perfect condition', 'well used and lightly worn', 'scuffed from daily use', 'polished smooth by years of handling',
        'dusty from long storage', 'freshly cleaned', 'carefully restored', 'worn at the edges', 'faded by sunlight', 'slightly dented', 'chipped in one place',
        'showing its age', 'looking almost new', 'marked with small scratches', 'with a soft patina of age']
    G['ob_era_condition_soft'] = ['in good condition', 'in near-perfect condition', 'well used and lightly worn', 'dusty from long storage', 'freshly cleaned',
        'carefully kept', 'worn at the edges', 'faded by sunlight', 'creased from handling', 'slightly frayed at one corner', 'showing its age', 'looking almost new']
    G['ob_era_condition_fixed'] = ['in good repair', 'freshly painted', 'well kept', 'showing its age', 'worn by years of use', 'carefully restored', 'weathered', 'slightly faded',
        'newly fitted', 'scuffed in places', 'cleaned and polished', 'cracked in one corner']
    G['ob_era_objects'] = done
    return G
