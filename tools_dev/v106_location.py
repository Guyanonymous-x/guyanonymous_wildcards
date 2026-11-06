"""v106 DRAFT - structured single-person venue scenes appended to adult_lN_location (levels 1-6): venue, posture geometry, hands, clothing or nudity by level, light, camera.
Old one-sentence location lines are kept."""
import random, os, re
import v106_panels as P
R = random.Random(10620)
# (venue sentence fragment, f posture, m posture, hands at rest (f), hands at rest (m), hands in act (f), hands in act (m), camera)
V = [
 ("in a dim cedar sauna", "sits on the upper cedar bench with her back against the wall, her knees apart and her feet flat on the lower bench", "sits on the upper cedar bench with his back against the wall, his knees apart and his feet flat on the lower bench",
  "her hands resting on the bench either side of her hips", "his hands resting on the bench either side of his hips", "her right hand between her thighs and her left hand on her breast", "his right hand around his erect penis and his left hand on the bench", "The shot is from the lower bench, showing her from head to feet."),
 ("under an open-air shower at a beach resort", "stands under the shower with her feet apart and her face tilted up into the water", "stands under the shower with his feet apart and his face tilted up into the water",
  "her hands pushing her wet hair back", "his hands pushing his wet hair back", "her right hand between her thighs and her left hand flat on the tiled wall", "his right hand around his erect penis and his left hand flat on the tiled wall", "The shot is from the front, showing her from head to knees."),
 ("on the tiled edge of a steaming bathhouse plunge pool", "sits on the edge with her legs in the water to the knees and her thighs apart", "sits on the edge with his legs in the water to the knees and his thighs apart",
  "her hands on the tiles behind her", "his hands on the tiles behind him", "her right hand between her thighs and her left hand on the tiles behind her", "his right hand around his erect penis and his left hand on the tiles behind him", "The shot is from across the pool, showing the whole body."),
 ("on the wooden deck beside a hot tub at dusk", "sits on the deck with her knees bent and her feet flat, leaning back on her hands", "sits on the deck with his knees bent and his feet flat, leaning back on his hands",
  "her hands flat on the boards behind her", "his hands flat on the boards behind him", "her right hand between her thighs and her left hand on the boards behind her", "his right hand around his erect penis and his left hand on the boards behind him", "The shot is from the front at deck height, showing the whole body."),
 ("on a rooftop terrace lounger in the evening", "lies back on a cushioned lounger with her knees bent and her head on the raised end", "lies back on a cushioned lounger with his knees bent and his head on the raised end",
  "her arms folded under her head", "his arms folded under his head", "her right hand between her thighs and her left arm over her eyes", "his right hand around his erect penis and his left arm over his eyes", "The shot is from the foot of the lounger, showing the whole body."),
 ("on the wooden dock of a quiet forest lake", "sits at the end of the dock with her feet in the water and her knees apart", "sits at the end of the dock with his feet in the water and his knees apart",
  "her hands on the planks either side of her hips", "his hands on the planks either side of his hips", "her right hand between her thighs and her left hand on the plank beside her", "his right hand around his erect penis and his left hand on the plank beside him", "The shot is from behind and to the side, showing the whole body."),
 ("on a locker room bench", "sits on the bench with her back straight, her knees apart and her feet flat on the tiled floor", "sits on the bench with his back straight, his knees apart and his feet flat on the tiled floor",
  "her hands resting on her knees", "his hands resting on his knees", "her right hand between her thighs and her left hand gripping the bench edge", "his right hand around his erect penis and his left hand gripping the bench edge", "The shot is from the front, showing her from head to feet."),
 ("in a rope hammock in a shaded garden", "lies in the hammock on her back with her knees bent and one foot hanging over the edge", "lies in the hammock on his back with his knees bent and one foot hanging over the edge",
  "her arms stretched above her head", "his arms stretched above his head", "her right hand between her thighs and her left hand gripping the hammock rope", "his right hand around his erect penis and his left hand gripping the hammock rope", "The shot is from the side, showing the whole body."),
 ("in a steam room with white tiled walls", "sits on the tiled seat with her back against the wall and her legs apart, her feet on the floor", "sits on the tiled seat with his back against the wall and his legs apart, his feet on the floor",
  "her hands resting on her thighs", "his hands resting on his thighs", "her right hand between her thighs and her left hand flat on the tile beside her", "his right hand around his erect penis and his left hand flat on the tile beside him", "The shot is from the front, showing her from head to feet."),
 ("on a kitchen counter late at night", "sits on the counter with her knees apart and her feet hanging down, leaning back on her hands", "sits on the counter with his knees apart and his feet hanging down, leaning back on his hands",
  "her hands flat on the counter behind her", "his hands flat on the counter behind him", "her right hand between her thighs and her left hand flat on the counter behind her", "his right hand around his erect penis and his left hand flat on the counter behind him", "The shot is from the front, showing her from head to knees.")]
def build(final):
    out = {}
    for L in range(1, 7):
        name = 'adult_l%d_location' % L
        old = [l.rstrip('\n') for l in open(os.path.join(final, name + '.txt'), encoding='utf8') if l.strip()]; new = []
        for place, pf, pm, rf, rm, af, am, cam in V:
            for sx in ('f', 'm'):
                who = 'A woman __apose_person_f__,' if sx == 'f' else 'A man __apose_person_m__,'
                pos = pf if sx == 'f' else pm; pr = 'her' if sx == 'f' else 'his'
                hands = (rf if sx == 'f' else rm)
                if L == 1: st = ' %s wears %s.' % ('She' if sx == 'f' else 'He', R.choice(P.CLW if sx == 'f' else P.CLM))
                elif L == 2:
                    if sx == 'f': st = ' She wears %s.' % R.choice(P.UNW)
                    else: g, t = P.pairm(P.UNM); st = ' He wears %s. The fabric over his groin shows %s.' % (g, t)
                elif L == 3:
                    if sx == 'f': st = ' She is topless and wears %s.' % R.choice(P.BOTF)
                    else: g, t = P.pairm(P.BOTM); st = ' He is shirtless and wears %s. The fabric over his groin shows %s.' % (g, t)
                elif L == 4: st = (' She is nude, with her breasts and vulva in view.' if sx == 'f' else ' He is nude, with his penis and scrotum in view, the penis hanging soft.')
                else:
                    st = ' %s is nude.' % ('She' if sx == 'f' else 'He'); hands = af if sx == 'f' else am
                    if L == 6: st += (' Thin, clear, watery fluid comes out of her vaginal opening __squirt_form__; it is transparent, not white, and it falls downward.' if sx == 'f' else ' Semen leaves the tip of his penis __semen_amount__, and it lands on his stomach; it is __semen_look__. __semen_after__')
                new.append(' '.join(('%s %s, %s. The scene is %s.%s The light is __apose_light__. %s' % (who, pos, hands, place, st, cam if sx == 'f' else cam.replace('showing her', 'showing him'))).split()))
        out[name] = list(dict.fromkeys(old + new))
    return out
