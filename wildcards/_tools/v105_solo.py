"""v105 - larger solo masturbation pools (levels 1-5), varied rooms, postures and garments, so grids do not repeat."""
import random, os
R = random.Random(10599)
LIGHT = ' The light is __apose_light__.'
F = '__apose_person_f__'; M = '__apose_person_m__'
# (level, sex) -> (garments, skeletons).  {G} = garment phrase
G = {
(1,'f'): (['a long denim skirt and a striped shirt','a green wool dress','a leather jacket and black jeans','a white linen jumpsuit','a pleated skirt and a cardigan','an oversized football shirt and leggings','a flowered pinafore dress','a yoga top and leggings','a red raincoat and tights','a knitted tunic and wide trousers'],
  ["sits cross-legged on a rug, her right hand resting against the top of her thigh and her left hand pressed to her collarbone, her head tipped back and her eyes closed.",
   "leans back against a kitchen counter, her right hand flat low on her stomach and her left hand gripping the counter edge, her eyes closed and her lower lip between her teeth.",
   "lies on her stomach on a bed with her chin on a pillow, her right hand tucked beneath her hips and her left arm folded under her head, her eyes closed.",
   "sits in an armchair with one leg hooked over the arm, her right hand pressed between her thighs over the fabric and her head back against the cushion.",
   "stands in a doorway with her back against the frame, her right hand on her inner thigh over the fabric and her left hand covering her mouth, her eyes shut.",
   "sits on a staircase with her knees drawn up, her right hand pressed low on her belly and her forehead resting on her left forearm.",
   "lies on her back on a lawn with her knees bent, her right hand flat on her stomach and her left arm flung above her head, her eyes closed and her face flushed.",
   "sits on a desk chair with her feet on the seat and her knees together, her right hand gripping her own knee and her left hand over her eyes, her head tipped back."]),
(1,'m'): (['a checked shirt and corduroys','a hoodie and joggers','a work shirt with the tie loosened and dark trousers','a football shirt and shorts','a denim jacket and jeans','a cable-knit jumper and chinos','a mechanic\'s boiler suit','a tracksuit','a linen shirt and cotton shorts','a leather jacket and black jeans'],
  ["sits cross-legged on a rug, his right hand resting against the top of his thigh and his left hand pressed to his chest, his head tipped back and his eyes closed.",
   "leans back against a kitchen counter, his right hand flat low on his stomach and his left hand gripping the counter edge, his eyes closed and his jaw tight.",
   "lies on his stomach on a bed with his chin on a pillow, his right hand tucked beneath his hips and his left arm folded under his head, his eyes closed.",
   "sits in an armchair with one leg hooked over the arm, his right hand pressed over his lap on top of the fabric and his head back against the cushion.",
   "stands in a doorway with his back against the frame, his right hand pressed over his lap on top of the fabric and his left hand over his mouth, his eyes shut.",
   "sits on a staircase with his knees apart, his right hand pressed flat over his lap and his forehead resting on his left forearm.",
   "lies on his back on a lawn with his knees bent, his right hand flat on his stomach and his left arm flung above his head, his eyes closed.",
   "sits on a desk chair with his legs spread, his right hand gripping his own knee and his left hand over his eyes, his head tipped back."]),
(2,'f'): (['a lace bra and matching briefs','a satin camisole and french knickers','a sports bra and cotton briefs','a mesh bodysuit','a silk slip and lace shorts','a cotton vest and high-waisted briefs','a balconette bra and a thong','a ribbed bralette and briefs'],
  ["lies on her side on a bed with her knees drawn up, her right hand slid inside the front of her underwear so that the fabric is stretched over her wrist, her left hand under the pillow and her eyes closed.",
   "sits on the edge of a bath with her knees apart, her right hand pressed flat over the front of her underwear and her left hand gripping the rim, her head back.",
   "stands against a bedroom wall with one foot raised on a chair, her right hand inside the front of her underwear and her left palm flat on the wall, her eyes closed.",
   "lies on a sofa with her feet on the armrest, her right hand beneath the waistband of her underwear and her left hand over her own mouth.",
   "kneels on a bed leaning forward on her left forearm, her right hand between her thighs inside her underwear, her face turned into the pillow.",
   "sits on a kitchen stool with her heels hooked on the rung, her right hand beneath the front of her underwear and her left hand on the counter, her head dropped forward.",
   "lies on the floor on her back with her knees bent, her right hand inside the front of her underwear and her left arm over her eyes.",
   "sits in a window seat with her knees apart, her right hand pressed over the front of her underwear and her cheek against the glass, her eyes closed."]),
(2,'m'): (['tight cotton briefs','boxer shorts','a jockstrap','fitted boxer briefs','silk boxer shorts','low-cut briefs','a thin pair of swim trunks','long cotton boxers'],
  ["lies on his side on a bed with his knees drawn up, his right hand slid inside the front of his underwear so that the fabric moves over his wrist, his left hand under the pillow and his eyes closed.",
   "sits on the edge of a bath with his knees apart, his right hand pressed over the front of his underwear and his left hand gripping the rim, his head back.",
   "stands against a bedroom wall, his right hand inside the front of his underwear and his left palm flat on the wall, his eyes closed and his jaw tight.",
   "lies on a sofa with his feet on the armrest, his right hand beneath the waistband of his underwear and his left forearm over his eyes.",
   "kneels on a bed leaning forward on his left forearm, his right hand inside the front of his underwear, his face turned into the pillow.",
   "sits on a kitchen stool with his legs apart, his right hand inside the front of his underwear and his left hand on the counter, his head dropped forward.",
   "lies on the floor on his back with his knees bent, his right hand inside the front of his underwear and his left arm over his eyes.",
   "sits in a deck chair with his legs apart, his right hand pressed over the front of his underwear and his head tipped back, his eyes closed."]),
(3,'f'): (['a white sheet pulled up over her hips','a towel draped across her lap','a soft grey blanket over her thighs','a silk robe lying open over her lap','a folded duvet across her hips','a beach sarong spread over her thighs','a knitted throw across her lap','a bath towel wrapped loosely around her hips'],
  ["lies nude on her back on a bed with {G}, her breasts bare, her right hand moving beneath it between her thighs so that it rises and falls over her wrist, her left hand on her own breast, her eyes closed.",
   "sits nude in an armchair with {G}, her breasts bare, her right hand beneath it between her thighs and her left hand gripping the armrest, her head tipped back and her mouth open.",
   "lies nude on her side on a sofa with {G}, her breasts bare, her right hand moving between her thighs out of sight beneath it, her left arm under her head and her eyes closed.",
   "sits nude on the edge of a bath with {G}, her breasts bare, her right hand beneath it between her thighs and her left hand on the bath rim, her head back.",
   "lies nude on a rug on her back with {G}, her breasts bare, her right hand moving beneath it and her left hand flat on her stomach, her face flushed.",
   "kneels nude on a bed with {G}, her breasts bare, her right hand beneath it between her thighs and her left hand on the headboard, her eyes shut."]),
(3,'m'): (['a white sheet pulled up over his hips','a towel draped across his lap','a soft grey blanket over his thighs','a silk robe lying open over his lap','a folded duvet across his hips','a beach sarong spread over his thighs','a knitted throw across his lap','a bath towel wrapped loosely around his hips'],
  ["lies nude on his back on a bed with {G}, his chest bare, his right hand moving beneath it so that it rises and falls over his wrist, his left hand gripping the pillow, his eyes closed.",
   "sits nude in an armchair with {G}, his chest bare, his right hand beneath it and his left hand gripping the armrest, his head tipped back and his mouth open.",
   "lies nude on his side on a sofa with {G}, his chest bare, his right hand moving out of sight beneath it, his left arm under his head and his eyes closed.",
   "sits nude on the edge of a bath with {G}, his chest bare, his right hand beneath it and his left hand on the bath rim, his head back.",
   "lies nude on a rug on his back with {G}, his chest bare, his right hand moving beneath it and his left hand flat on his stomach, his face flushed.",
   "kneels nude on a bed with {G}, his chest bare, his right hand beneath it and his left hand on the headboard, his eyes shut."]),
(4,'f'): (['',],
  ["lies nude on her back on a bed with her knees bent and her thighs apart, two fingers of her right hand rubbing in slow circles over her clitoris, her left hand holding her own breast, her vulva plainly visible, her eyes closed.",
   "sits nude in an armchair with her legs over its arms, her right middle and ring fingers moving over her clitoris and her left hand on her thigh, her vulva plainly visible, her head back.",
   "stands nude in front of a mirror with her feet apart and her right hand between her thighs, two fingers moving over her clitoris, her left hand on the wall, her vulva visible, her eyes half closed.",
   "lies nude on her side on a rug with her top knee raised, her right hand between her thighs with two fingers moving over her clitoris, her left arm under her head, her vulva visible.",
   "kneels nude on a bed with her knees wide, her right hand between her thighs rubbing her clitoris and her left hand gripping the headboard, her vulva visible, her head tipped back.",
   "sits nude on the edge of a bathtub with her legs apart, her right hand between her thighs with two fingers circling her clitoris and her left hand on the rim, her vulva visible, her eyes closed.",
   "lies nude on her stomach propped on her left forearm, her right hand beneath her hips between her thighs, her buttocks and the back of her thighs visible, her face turned into the pillow.",
   "sits nude on a kitchen floor against a cabinet with her knees up and apart, her right hand between her thighs moving over her clitoris, her left hand over her mouth, her vulva visible."]),
(4,'m'): (['',],
  ["lies nude on his back on a bed with his knees bent, his right hand wrapped around his erect penis and stroking slowly, his penis and scrotum visible, his left hand on his stomach, his eyes closed.",
   "sits nude in an armchair with his legs over its arms, his right hand around his erect penis, the head visible above his fist, his left hand gripping the armrest, his head back.",
   "stands nude in front of a mirror with his feet apart, his right hand around his erect penis, his left palm on the wall, his head down and his eyes half closed.",
   "lies nude on his side on a rug with his top knee raised, his right hand around his erect penis, his penis and scrotum visible, his left arm under his head.",
   "kneels nude on a bed with his knees apart, his right hand stroking his erect penis and his left hand on the headboard, his head tipped back and his mouth open.",
   "sits nude on the edge of a bathtub with his legs apart, his right hand around his erect penis and his left hand on the rim, his eyes closed.",
   "lies nude on his stomach propped on his left forearm, his right hand beneath his hips, his buttocks and the back of his thighs visible, his face turned into the pillow.",
   "sits nude on a kitchen floor against a cabinet with his knees up and apart, his right hand around his erect penis, his left hand over his mouth."]),
(5,'f'): (['',],
  ["lies nude on her back on a bed with her knees wide, a slim vibrator pressed against her clitoris in her right hand, her left hand gripping the sheet, her vulva visible, her eyes closed.",
   "sits nude against the headboard with her legs wide, the index and ring fingers of her right hand inside her vagina curling in a come-hither motion and her left thumb on her clitoris, her vulva visible, her head back.",
   "lies nude on her stomach with a pillow under her hips, her right hand between her thighs from beneath, her face turned to the camera, her mouth open.",
   "sits nude on a chair with her legs over its arms, a glass dildo held in her right hand and moving slowly in and out of her vagina, her left hand on her breast, her vulva visible.",
   "lies nude on her back with her legs raised and apart, a vibrating wand held against her vulva in her right hand, her left hand gripping the pillow, her face flushed.",
   "kneels nude over a pillow, her hips lowered onto it, her right hand between her thighs, her left hand holding the headboard, her head tipped back."]),
(5,'m'): (['',],
  ["lies nude on his back on a bed with his knees bent, a stretchy black ring at the base of his erect penis, his right hand stroking the shaft, his penis visible, his eyes closed.",
   "kneels nude on a bed, his right hand stroking his erect penis and his left hand holding a lilac vibrator under his scrotum, his head back and his mouth open.",
   "sits nude in an armchair with his legs apart, his right hand around his erect penis and his left hand cupping his testicles, his head tipped back.",
   "stands nude in a shower with water running over his chest, his right hand around his erect penis and his left hand on the tiled wall, his eyes closed.",
   "lies nude on his side on a bed, his right hand around his erect penis and stroking it quickly, his left hand holding the pillow, his eyes shut.",
   "sits nude on the floor against a sofa with his knees up and apart, his right hand around his erect penis, his left forearm over his eyes."])}
def build(final):
    out = {}; ep = []
    for (L, sx), (gs, sk) in G.items():
        name = 'adult_l%d_masturbation_%s' % (L, sx)
        old = [l.rstrip('\n') for l in open(os.path.join(final, name + '.txt'), encoding='utf8') if l.strip()]
        lines = list(old); who = 'A woman %s,' % F if sx == 'f' else 'A man %s,' % M
        pr = 'in {G}, ' if L <= 2 else ''
        for i, s in enumerate(sk):
            gg = R.choice(gs) if gs and gs[0] else ''
            body = (pr.format(G=gg) if pr else '') + s.replace('{G}', gg)
            lines.append('%s %s%s' % (who, body, LIGHT))
        out[name] = list(dict.fromkeys(lines)); ep.append(name)
    out['v105_solo_entry_points'] = ep
    return out
