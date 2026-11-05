"""v104 - concrete wording for semen and squirting fluid in adult lines (appearance, source, direction)."""
import re
SEM = '__semen_look__'
FL = 'thin, clear, watery fluid'
TAIL = 'out of her vaginal opening __squirt_form__'
SQ_ING = 'with ' + FL + ' pulsing ' + TAIL
R_EJV = re.compile(r'\bejaculat(es|ed|ing) (onto|on|over|across|into|inside)\b', re.I)
R_FIN = re.compile(r'\bfinish(es|ed|ing) (onto|on|over|across)\b', re.I)
R_EJN = re.compile(r'\b(?:(?:thick|creamy|warm|pearly|milky) )*(?:white )?ejaculate\b', re.I)
R_SQSPRAY = re.compile(r'\bsquirt(s|ing|ed)? (?:a )?(?:thick |thin )?clear (?:spray|fluid) from (?:her|the) (?:vulva|vagina)\b', re.I)
R_SQN = re.compile(r'\b(two|three|four) squirting (women|woman)\b', re.I)
R_AFTER = re.compile(r'\bafter (?:she has |she )?squirt(?:ed|ing)\b', re.I)
R_MAKES = re.compile(r'\bmakes? (her|him|them) squirt\b', re.I)
R_SQF = re.compile(r'\bsquirted fluid\b', re.I)
R_SQ = re.compile(r'\bsquirt(?:ing|s|ed)\b|\bsquirt\b', re.I)
R_SPRAY = re.compile(r'\b(?:a )?(?:thick |thin )?clear spray\b', re.I)
R_CLR = re.compile(r'\bclear fluid\b', re.I)
SEMV = {'es': 'shoots', 'ed': 'shot', 'ing': 'shooting'}
def fix(l):
    if not re.search(r'ejaculat|squirt|clear fluid|clear spray|finish', l, re.I): return l
    l = R_EJV.sub(lambda m: SEMV[m.group(1).lower()] + ' ' + SEM + ' from the tip of the penis __semen_amount__ ' + m.group(2), l)
    l = R_FIN.sub(lambda m: SEMV[m.group(1).lower()] + ' ' + SEM + ' from the tip of the penis __semen_amount__ ' + m.group(2), l)
    l = R_EJN.sub(SEM, l)
    l = R_SQSPRAY.sub(lambda m: {'s': 'has ' + FL + ' pulse ' + TAIL, 'ed': 'had ' + FL + ' pulse ' + TAIL}.get((m.group(1) or '').lower(), SQ_ING), l)
    l = R_SQN.sub(lambda m: m.group(1) + ' women, each ' + SQ_ING, l)
    l = R_AFTER.sub('after ' + FL + ' pulsed ' + TAIL, l)
    l = R_MAKES.sub(lambda m: 'makes ' + FL + ' pulse ' + TAIL, l)
    l = R_SQF.sub('the fluid', l)
    first = [True]
    def sq(m):
        w = m.group(0).lower()
        if first[0]:
            first[0] = False
            if w == 'squirts': return 'has ' + FL + ' pulse ' + TAIL
            if w == 'squirted': return 'had ' + FL + ' pulse ' + TAIL
            if w == 'squirt': return 'let ' + FL + ' pulse ' + TAIL
            return SQ_ING
        return 'the pulsing fluid'
    l = R_SQ.sub(sq, l)
    has = 'vaginal opening' in l
    rep = 'the fluid' if has else FL
    l = R_SPRAY.sub(rep, l); l = R_CLR.sub(rep, l)
    return l
def fix_all(G):
    n = 0
    for k, v in G.items():
        if not k.startswith('adult_l'): continue
        new = [fix(l) for l in v]
        n += sum(a != b for a, b in zip(v, new)); G[k] = new
    return n
import os
KEEP = ['squirt_form', 'semen_look', 'semen_amount', 'semen_after', 'fluid_semen_flight', 'fluid_scene_semen', 'fluid_scene_squirt', 'fluid_finger_man_r', 'fluid_finger_man_l', 'fluid_finger_woman_r', 'fluid_finger_self'] + ['adult_l%d_masturbation_%s' % (L, x) for L in range(1, 7) for x in 'fm']
def build(final):
    K = {n: [l.rstrip('\n') for l in open(os.path.join(final, n + '.txt'), encoding='utf8') if l.strip()] for n in KEEP}
    return dict(K, **{
        'fluid_semen_look': ['__semen_look__ leaving the tip of the penis __semen_amount__', '__semen_look__ landing on the skin and running slowly downward'],
        'fluid_squirt_look': ['with thin, clear, watery fluid pulsing out of her vaginal opening in a short burst that arcs forward and falls in fine droplets onto the sheet beneath her','thin, clear, watery fluid released from the vaginal opening in a few quick pulses, arcing a short way forward and falling in fine droplets onto the sheet',
            'thin, transparent, watery fluid pulsing from the vaginal opening in short bursts, spreading in fine droplets and soaking the sheet beneath into a dark wet patch',
            'a brief burst of clear, watery fluid from the vaginal opening that fans out in fine droplets and falls downward onto the thighs and the bedding'],
    })
