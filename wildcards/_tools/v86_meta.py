import re as _re
import v86_build as _B
_G = _B.build()
_cnt = lambda pat: sum(len(v) for k, v in _G.items() if _re.fullmatch(pat, k))
_n_pb = _cnt(r'pinback_(?!prompt).*'); _n_ins = _cnt(r'insignia_(?!.*prompt).*'); _n_ach = _cnt(r'acc_(meritbadge|medal|pin|badge)_adult_(?!.*prompt).*')
_n_g = _cnt(r'adult_l[1-6]_(kilts|pony|torn)'); _n_e = _cnt(r'adult_l6_ejaculate_extras')
ONELINE = 'pinback buttons, emergency and military insignia, adult achievement badges, kilts L4-L6, pony and torn clothing L1-L6'
BULLETS = ["Pinback buttons (`pinback_prompt`, %d lines): slogans, music, fandom, causes, identity, events, adult, plain designs - each a round button with size, border, print finish, picture, words and safety-pin back." % _n_pb,
 "Police, fire, ambulance and military insignia (`insignia_prompt`, `insignia_medal/pin/badge_prompt`, %d lines) with invented towns, units and names; as patches, medals, enamel pins and badges." % _n_ins,
 "Adult achievement merit badges, medals, enamel pins and badges for dating, kink, sex and fetish (`acc_meritbadge_adult_prompt` and siblings, %d lines)." % _n_ach,
 "Adult kilts for L4-L6, pony-play gear and torn or ripped-off clothing for L1-L6 (`adult_kilts_levels`, `adult_pony_levels`, `adult_torn_levels`, %d lines), and L6 ejaculate extras (%d lines)." % (_n_g, _n_e),
 "A 40-image prompt showcase at 1024 and 1408 pixel counts, steps 50, cfg 3.75, no trailing blank line, and 100 random sample prompts."]
README = """Guyanonymous' Wildcards v86 - pinback buttons, insignia, adult achievements, kilts, pony, torn clothing
Pinbacks       pinback_prompt, pinback_<slogans|music|fandom|cause|identity|event|adult|designs>
Insignia       insignia_prompt, insignia_<medal|pin|badge>_prompt, insignia_<police|fire|ambulance|military>
Achievements   acc_<meritbadge|medal|pin|badge>_adult_<dating|kink|sex|fetish>, *_adult_prompt
Adult gear     adult_<kilts|pony|torn>_levels, adult_lN_<kilts|pony|torn>, adult_l6_ejaculate_extras
"""
GEN_ROW = '("pinback_*, insignia_*","%d","v86 pinback buttons and insignia."),' % (_n_pb + _n_ins)
DOCS = ['/home/claude/w/docs/INDEX_v86.txt', '/home/claude/w/docs/RESEARCH_v86_buttons.txt']
SAMPLES = [('pinback', '__pinback_prompt__', 30), ('insignia', '__insignia_all_prompt__', 20), ('adult achievements', '__adult_achievement_prompt__', 15), ('kilts', '__adult_kilts_levels__', 10), ('pony', '__adult_pony_levels__', 10), ('torn', '__adult_torn_levels__', 10), ('ejaculate extras', '__adult_l6_ejaculate_extras_prompt__', 5)]
