"""v106 DRAFT - structured three-person scenes added to adult_lN_group (levels 1-6) and explicit male wrestling at levels 4-6.
Every person is introduced once, every hand/arm/leg is placed, clothing or nudity and the camera are stated. Old one-sentence group lines are kept."""
import random, os, re
import v106_panels as P
R = random.Random(10610)
COMBOS = {'wwm': ['f', 'f', 'm'], 'wmm': ['f', 'm', 'm'], 'mmm': ['m', 'm', 'm'], 'www': ['f', 'f', 'f']}
ORD = ['', 'second ', 'third ']
def roles(c):
    seen = {'f': 0, 'm': 0}; out = []
    for sx in COMBOS[c]:
        k = seen[sx]; seen[sx] += 1; w = 'woman' if sx == 'f' else 'man'
        tot = COMBOS[c].count(sx)
        out.append(dict(sx=sx, p='her' if sx == 'f' else 'his', n=('the ' + ['first ', 'second ', 'third '][k] if tot > 1 else 'the ') + w,
                        intro=('a %s%s __apose_person_%s__' % (ORD[k], w, sx))))
    return out
def intro(rs): return 'This scene shows three adults: ' + '; '.join(r['intro'] for r in rs[:-1]) + '; and ' + rs[-1]['intro'] + '.'
def sent(t): return re.sub(r'(^|[.!?] )([a-z])', lambda m: m.group(1) + m.group(2).upper(), ' '.join(t.split()))
T_CLOTHED = [
 "{1}, {2} and {3} sit in a row on a sofa with their hips touching and {2} in the middle, {1}'s arm along the back of the sofa behind {2}'s shoulders and {3}'s hand resting on {2}'s knee, all three looking toward the camera.",
 "{1}, {2} and {3} stand shoulder to shoulder facing the camera with {1} in the middle, {1}'s arms around the waists of the other two, and the other two with their outer arms hanging relaxed at their sides.",
 "{1} lies on {1p} back on a bed, {2} lies on {2p} side against {1p} right side with {2p} head on {1p} chest, and {3} lies on {3p} side against {1p} left side with {3p} head on {1p} shoulder, all three looking toward the camera.",
 "{1}, {2} and {3} sit cross-legged in a circle on a rug with their knees touching, each with a hand resting on the next person's knee and their heads tipped toward the middle, laughing.",
 "{1} and {2} stand facing each other kissing with their torsos turned toward each other, {1}'s hands on {2}'s waist and {2}'s hands on {1}'s shoulders, while {3} stands behind {2} with both hands on {2}'s shoulders and {3p} chin on {2}'s shoulder.",
 "{1} sits on the edge of a bed with {1p} feet on the floor, {2} kneels on the bed behind {1} with both hands on {1}'s shoulders, and {3} sits cross-legged on the floor in front of {1} holding {1}'s hands."]
def attire(L, rs, nm):
    if L == 1:
        out = []; u = set()
        for r in rs:
            g = R.choice([x for x in (P.CLM if r['sx'] == 'm' else P.CLW) if x not in u]); u.add(g); out.append('%s wears %s.' % (r['n'].capitalize(), g))
        return ' ' + ' '.join(out)
    s = []; used = set(); usedf = set()
    for r in rs:
        if r['sx'] == 'f':
            pool = P.UNW if L == 2 else P.BOTF; gf = R.choice([x for x in pool if x not in usedf]); usedf.add(gf)
            s.append('%s wears %s.' % (r['n'].capitalize(), gf) if L == 2 else '%s is topless and wears %s.' % (r['n'].capitalize(), gf))
        else:
            g, t = P.pairm([x for x in (P.UNM if L == 2 else P.BOTM) if x not in used]); used.add(g)
            s.append(('%s wears %s' % (r['n'].capitalize(), g)) + ('' if L == 2 else ', shirtless') + '. The fabric over %s groin shows %s.' % (r['p'], t))
    return ' ' + ' '.join(s) + (' No one has a hand near a groin.' if L in (2, 3) else '')
def fmt(t, rs):
    d = {str(i + 1): r['n'] for i, r in enumerate(rs)}; d.update({'%dp' % (i + 1): r['p'] for i, r in enumerate(rs)})
    return re.sub(r'\{(\d p?)\}'.replace(' ', ''), lambda m: d[m.group(1)], t)
TAIL = ' The scene is in __apose_place__. The light is __apose_light__. The shot shows all three from head to knees.'
NUDE = {4: ' Everyone is nude, with breasts and penises and scrotums in view, the penises hanging soft.'}
ACTS = {
 'wwm': ["{1} lies on {1p} back on a bed with {1p} thighs apart and {1p} hands in {2}'s hair. {2} kneels between {1}'s thighs with {2p} face at {1}'s vulva and {2p} tongue on it. {3} kneels behind {2} holding {2}'s hips with both hands, {3}'s erect penis inside {2}'s vagina from behind.",
         "{3} lies on {3p} back on a bed. {1} sits astride {3}'s hips facing {3}, {3}'s erect penis inside {1}'s vagina and {1p} hands on {3}'s chest. {2} kneels over {3}'s face facing {1}, {2p} knees on the mattress either side of {3}'s head and {3}'s tongue on {2}'s vulva, while {1} and {2} hold each other's shoulders."],
 'wmm': ["{1} kneels on all fours on a bed with {1p} arms straight and {1p} back arched. {2} kneels behind {1} holding {1}'s hips with both hands, {2}'s erect penis inside {1}'s vagina from behind. {3} kneels in front of {1} with {3p} hands in {1}'s hair, {3}'s erect penis in {1}'s mouth.",
         "{2} lies on {2p} back on a bed. {1} sits astride {2}'s hips facing {2}'s feet, {2}'s erect penis inside {1}'s vagina and {1p} hands on {2}'s shins. {3} stands on the bed in front of {1} with {3p} hands in {1}'s hair, {3}'s erect penis in {1}'s mouth."],
 'mmm': ["{1} kneels on all fours on a bed with {1p} back arched. {2} kneels behind {1} holding {1}'s hips with both hands, {2}'s erect penis inside {1}'s anus. {3} kneels in front of {1} with {3p} hands on {1}'s shoulders, {3}'s erect penis in {1}'s mouth."],
 'www': ["{1} lies on {1p} back on a bed with {1p} thighs apart and {1p} head on a pillow. {2} kneels between {1}'s thighs with {2p} face at {1}'s vulva and {2p} tongue on it. {3} kneels beside {1}'s head, bending to kiss {1} with one hand on {1}'s breast."]}
def finish(c):
    return {'wwm': " Semen leaves the tip of {3}'s penis __semen_amount__, and it lands on {2}'s lower back; it is __semen_look__. __semen_after__",
            'wmm': " Semen leaves the tip of {3}'s penis __semen_amount__, and it lands on {1}'s lips and chin; it is __semen_look__. __semen_after__",
            'mmm': " Semen leaves the tip of {3}'s penis __semen_amount__, and it lands on {1}'s chest; it is __semen_look__. __semen_after__"}.get(c, '')
HOLDS = [
 "{1} lies on {1p} back on a mat with {2} on top of {1}'s chest, {2} pinning {1}'s wrists to the mat above {1}'s head with both hands and {1}'s legs wrapped around {2}'s waist, both men's faces a hand apart.",
 "{1} and {2} stand face to face on a mat with each man's arms hooked under the other's, their foreheads together, their feet planted wide apart and their hips a hand's width apart.",
 "{2} lies face down on a mat while {1} sits on {2}'s lower back, holding {2}'s right arm bent behind {2}'s back in one hand with {1}'s other hand flat between {2}'s shoulder blades.",
 "{1} kneels behind {2} with one arm around {2}'s neck and the other forearm across {2}'s chest, while {2} kneels upright with both hands gripping {1}'s forearm.",
 "{1} lies on {1p} side on a mat with {1}'s legs scissored around {2}'s waist while {2} lies on {2p} back, both men's hands gripping each other's upper arms.",
 "{1} stands with {1p} back against a wall while {2} presses chest to chest against {1}, {2}'s hands pinning {1}'s forearms to the wall either side of {1}'s head and {1}'s raised knee against {2}'s thigh."]
EXPL = [
 ("{1} lies on {1p} back on a mat and {2} kneels astride {1}'s hips facing {1}, {2}'s left hand pinning {1}'s right wrist to the mat beside {1}'s head and {2}'s right hand around {1}'s erect penis, stroking it.", " Semen leaves the tip of {1}'s penis __semen_amount__, and it lands on {1}'s stomach; it is __semen_look__. __semen_after__"),
 ("{2} lies face down on a mat with {1} lying on {2}'s back, {1}'s forearm across {2}'s shoulders holding {2} down and {2}'s fists gripping the mat. {1}'s erect penis is inside {2}'s anus.", " {1} has pulled out, and semen leaves the tip of {1}'s penis __semen_amount__, and it lands across {2}'s lower back; it is __semen_look__. __semen_after__"),
 ("{1} and {2} kneel facing each other on a mat, each gripping the other's shoulder with {1p} left hand while each man's right hand is around the other man's erect penis, stroking it, their foreheads together.", " Semen leaves the tip of {2}'s penis __semen_amount__, and it lands on {1}'s stomach; it is __semen_look__. __semen_after__"),
 ("{1} sits on a mat with {1p} legs apart and {2} kneels between {1}'s legs with {2}'s mouth around {1}'s erect penis, {1}'s hand gripping {2}'s hair and {2}'s other hand pinning {1}'s thigh to the mat.", " Semen leaves the tip of {1}'s penis __semen_amount__, and it lands on {2}'s lips and chin; it is __semen_look__. __semen_after__")]
def wres(L):
    out = []; rs = [dict(n='the first man', p='his', intro='a man __apose_person_m__'), dict(n='the second man', p='his', intro='a second man __apose_person_m__')]
    head = 'This scene shows two adults, both men: ' + rs[0]['intro'] + '; and ' + rs[1]['intro'] + '. They wrestle. '
    tail = ' The scene is in __apose_place__. The light is __apose_light__. The shot is from the side, at mat height, showing both bodies full length.'
    if L == 4:
        for h in HOLDS: out.append(sent(head + fmt(h, rs) + ' Both men are nude, with their penises and scrotums in view, hanging soft, and their skin shiny with sweat.' + tail))
    else:
        for h, f in EXPL: out.append(sent(head + fmt(h, rs) + ' Both men are nude.' + (fmt(f, rs) if L == 6 else '') + tail))
    return list(dict.fromkeys(out))
def build(final):
    out = {}
    for L in range(1, 7):
        name = 'adult_l%d_group' % L
        old = [l.rstrip('\n') for l in open(os.path.join(final, name + '.txt'), encoding='utf8') if l.strip()]; new = []
        if L <= 4:
            for c in COMBOS:
                for t in T_CLOTHED:
                    rs = roles(c); body = fmt(t, rs)
                    new.append(sent(intro(rs) + ' ' + body + (attire(L, rs, c) if L <= 3 else NUDE[4]) + TAIL))
        else:
            for c, ts in ACTS.items():
                for t in ts:
                    rs = roles(c); body = fmt(t, rs)
                    new.append(sent(intro(rs) + ' ' + body + ' Everyone is nude.' + (fmt(finish(c), rs) if L == 6 else '') + ' The scene is in __apose_place__. The light is __apose_light__. The shot is from the side showing all three bodies.'))
        out[name] = list(dict.fromkeys(old + [' '.join(x.split()) for x in new]))
    for L in (4, 5, 6):
        name = 'adult_l%d_wrestling_mm' % L
        out[name] = wres(L)
    out['v106_group_entry_points'] = list(out)
    return out
