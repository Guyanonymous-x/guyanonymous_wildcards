"""v107 - fills gaps found while building the body-feature showcase: an areola/nipple size ladder, anal-area shape files for women and men
(no skin colour), and fuller yoga, dance-class and martial-arts action, clothes, equipment and setting lists."""
import os, random, re
AREOLA = ['a very small areola about the width of a thumbnail', 'a small, tight areola about two centimetres across', 'a medium areola about three and a half centimetres across',
          'a wide areola about five centimetres across', 'a very wide areola about seven centimetres across that covers much of the front of the breast']
NIPPLE = ['a tiny flat nipple that barely rises', 'a small neat nipple', 'a medium nipple standing a little proud', 'a long prominent nipple', 'a thick wide nipple', 'an inverted nipple that draws inward',
          'a puffy nipple with the areola rising in a soft dome']
TEXT = ['a shade darker than the surrounding skin', 'clearly darker than the surrounding skin and smooth', 'a little darker than the surrounding skin, with small raised bumps near its edge',
        'only slightly darker than the surrounding skin', 'with a softly wrinkled surface']
def nipples(old):
    r = random.Random(107); out = [l for l in old if not re.search(r'centimetres|thumbnail', l)]
    for a in AREOLA:
        for n in NIPPLE:
            out.append('her breasts have %s set in %s, the areola %s' % (n, a, r.choice(TEXT)))
    return out
FANUS = ['a small, tight rosette of fine radial folds, smooth and hairless around it', 'a soft rosette with relaxed radial folds and a light dusting of dark hair around it',
 'a slightly raised rosette ringed by a few small folds', 'a flat, smooth rosette with very faint folds', 'a wide rosette with deep, clear radial folds',
 'a puckered rosette drawn tightly closed', 'a rosette framed by a ring of dense dark hair', 'a rosette with a few scattered fine hairs near its edge',
 'a rosette with a slightly darker ring around it than the surrounding skin', 'a neat rosette set between full, rounded cheeks with a deep crease',
 'a rosette set between flat, narrow cheeks with a shallow crease', 'a soft rosette with a faintly raised ring of skin around it',
 'a small rosette with a smooth, hairless ring around it and fine folds', 'a loosely folded rosette with soft, deep creases and a few pale hairs',
 'a rosette in a lightly freckled, smooth area with fine folds', 'a rosette slightly off the centre line between uneven cheeks']
MANUS = ['a small, tight rosette of fine radial folds with a few dark hairs near it', 'a rosette ringed by dense, dark, curly hair', 'a rosette with a light scatter of fine hairs',
 'a smooth, hairless rosette with fine folds', 'a puckered rosette drawn tightly closed between hard, flat cheeks', 'a wide rosette with deep radial folds between heavy cheeks',
 'a soft rosette framed by thick hair running up the crease', 'a rosette with a slightly darker ring of skin around it', 'a rosette set deep in a long crease between round, muscular cheeks',
 'a rosette with a faintly raised ring of skin and sparse hairs', 'a loosely folded rosette with soft creases and a few pale hairs', 'a neat rosette set between narrow cheeks with a shallow crease']
YOGA = ['holding a balanced tree pose on one leg with the sole of the other foot against the inner thigh', 'folding forward over straight legs with both hands flat on the floor', 'in a downward dog with hips high and arms and legs straight',
 'sitting cross-legged in a lotus pose with the hands resting on the knees', 'in a low lunge with both arms raised overhead', 'in warrior two with the arms stretched out and the front knee bent',
 'in a bridge with the hips lifted and the hands clasped under the back', 'sitting in a twist with one knee crossed over the other and one hand behind the back', 'in a cobra with the chest lifted off the mat',
 'in a child pose with the arms stretched forward on the mat', 'in a standing back bend with the hands on the lower back', 'in a triangle pose with one hand on the shin and the other reaching up',
 'sitting in a wide-legged forward fold', 'in a camel pose kneeling with the hands on the heels', 'standing in a half moon pose with one hand on the floor and the top leg raised', 'in a plank with the body straight and the arms locked',
 'lying on the back with both knees drawn to the chest', 'in a boat pose balanced on the sitting bones with the legs raised', 'standing in a mountain pose with the palms pressed together at the chest',
 'in a crow pose balanced on the hands with the knees on the upper arms', 'in a pigeon pose with one leg folded in front and the other stretched behind', 'in a chair pose with the knees bent and the arms overhead', 'in an eagle pose with the arms and legs wrapped around each other', 'lying in a final rest with the arms open']
YCLOTHES = ['loose stretchy clothes', 'a fitted leotard and leggings', 'a fitted sports top and yoga leggings', 'a fitted sleeveless top and yoga shorts', 'a fitted bodysuit', 'a short sports top and high-waisted leggings']
YEQUIP = ['a rolled mat', 'a folded blanket', 'a wooden block', 'a strap and a bolster', 'a round cushion', 'a rolled towel']
YSET = ['a bright studio', 'a clifftop at sunrise', 'a garden lawn', 'a quiet room with a wooden floor', 'a beach at dawn', 'a sunlit living room']
DANCE = ['stepping through a dance routine', 'spinning with arms wide', 'stretching at the barre', 'standing in a ballet first position with the arms rounded', 'balanced on one leg in an arabesque with the arms stretched out',
 'leaping with the legs split in the air', 'sinking into a deep plie at the barre', 'turning a pirouette on one foot', 'holding a ballet fifth position with the arms overhead', 'swaying a hip in a salsa step with one arm out',
 'mid-spin with a skirt flared out', 'dropping into a low squat in a hip-hop move', 'in a freeze with one hand on the floor and the legs in the air', 'stretching one leg straight along the barre',
 'arching the back in a contemporary backbend', 'jumping with the knees tucked', 'lunging forward with the arms open', 'kneeling and reaching one arm to the side in a floor move', 'standing in a jazz pose with the hips cocked and the hands out', 'in a deep side stretch with an arm over the head']
DCLOTHES = ['a fitted leotard and tights', 'a leotard and a short wrap skirt', 'a fitted tank top and loose dance trousers', 'a fitted t-shirt and jazz pants', 'a fitted bodysuit and leg warmers']
DEQUIP = ['a ballet barre', 'a mirror along one wall', 'a pair of dance shoes', 'a sprung wooden floor', 'a small speaker']
DSET = ['a mirrored dance studio', 'a rehearsal hall with a wooden floor', 'a school gym with the floor cleared', 'a stage with the curtains open']
MARTIAL = ['performing a high kick', 'holding a stance with raised fists', 'bowing at the edge of the mat', 'in a low horse stance with the fists at the hips', 'throwing a straight punch with the other fist drawn back',
 'blocking with a raised forearm', 'in a front stance with one arm extended forward', 'balanced in a crane stance on one leg with the arms raised', 'delivering a roundhouse kick', 'in a ready stance with the guard raised',
 'holding a knife-hand strike pose', 'in a flying kick in mid-air', 'in a sparring crouch with the knees bent', 'sitting in a kneeling position with the hands on the thighs', 'in a back stance with one hand pushing forward', 'stepping through a kata with a low sweep',
 'standing with the feet together and the fists at the sides', 'in a side kick with the leg fully extended', 'twisting into a spinning kick', 'in a deep lunge with a forearm strike']
MCLOTHES = ['a plain white training suit tied with a belt', 'a black training suit with a coloured belt', 'a loose white jacket and wide trousers', 'a fitted sleeveless top and loose training shorts', 'a plain white jacket tied with a black belt and wide trousers']
MEQUIP = ['a padded mat', 'a heavy bag', 'a wooden training dummy', 'a pair of gloves', 'a row of belts on a rack']
MSET = ['a training hall with mats', 'a bare dojo', 'a courtyard at sunrise', 'a gym with a ring in the corner']
def build(final):
    old = [l.rstrip('\n') for l in open(os.path.join(final, 'f_body_nipples.txt'), encoding='utf8') if l.strip()]
    return {'f_body_nipples': nipples(old), 'f_body_anus': FANUS, 'm_body_anus': MANUS,
            'act_yoga_action': YOGA, 'act_yoga_clothes': YCLOTHES, 'act_yoga_equip': YEQUIP, 'act_yoga_setting': YSET,
            'act_dance_classes_action': DANCE, 'act_dance_classes_clothes': DCLOTHES, 'act_dance_classes_equip': DEQUIP, 'act_dance_classes_setting': DSET,
            'act_martial_arts_action': MARTIAL, 'act_martial_arts_clothes': MCLOTHES, 'act_martial_arts_equip': MEQUIP, 'act_martial_arts_setting': MSET}
