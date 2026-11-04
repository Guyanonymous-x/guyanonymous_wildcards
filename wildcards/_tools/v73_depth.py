"""v73 item 56: depth and occlusion modifier family (depth_*). Optional, called manually. One sentence each, physical, positive wording only.
 depth_foreground_clear, depth_foreground_object, depth_person_in_front, depth_behind_furniture, depth_side_by_side, depth_layered, depth_scale_rule,
 depth_tag (per-person depth label), depth_prompt (picks one family at random). --restore removes the files."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from paths import FINAL
D = {
'depth_foreground_clear': [
 'The floor between the camera and the people is open and bare, so every person is seen from head to feet.',
 'The camera looks across an open stretch of floor, with cushions, sofa arms and tables placed beside or behind the people, so each person is fully visible.',
 'Everything in front of the people is open space, and every chair, sofa and table sits beside them or behind them.',
 'The people stand or sit in a clear open area, with their whole bodies visible and their feet resting on visible ground.',
 'A wide clear gap of open floor lies between the lens and the people, and all furniture stands at their sides or behind their backs.',
 'The nearest thing to the camera is the person, whose whole body from head to shoes is visible along a clear line of sight.'],
'depth_foreground_object': [
 'A large potted plant stands in the near foreground at the left edge of the frame, softly out of focus, and the people stand beyond it in sharp, clear view.',
 'The edge of a wooden table crosses the bottom corner of the frame in the near foreground, slightly blurred, while the people behind it are sharp from head to feet.',
 'A tall vase of flowers stands in the near foreground at the right edge, soft and out of focus, with the people clear and sharp behind it.',
 'The curved arm of a sofa fills the lower left corner of the frame in the foreground, slightly blurred, and the people sit and stand clearly beyond it.',
 'A hanging lamp shade is seen blurred in the upper corner of the foreground, and the people below and behind it are sharp and fully visible.',
 'A stack of books sits on a low shelf in the near foreground, softly out of focus, and the people stand clearly in the middle distance.'],
'depth_person_in_front': [
 'The person on the left stands one step closer to the camera than the person on the right, so both are seen from head to feet with a clear gap between their shoulders.',
 'The person in front stands a full stride nearer the camera, and the second person stands behind and slightly to one side, so the second person\'s face, shoulders and feet are all visible.',
 'The nearest person is slightly larger in the frame, and the other person stands further back and a little to the side, with a gap of open floor between their feet.',
 'One person stands close to the camera on the left, the other stands further back on the right, and the line between them is clear so neither person hides the other.',
 'The person at the front is turned slightly sideways, so the person behind is seen clearly over a gap beside the front person\'s shoulder.'],
'depth_behind_furniture': [
 'The person sits behind a wooden table whose surface is at waist height, and the whole upper body, both arms and both hands are clearly visible above the tabletop.',
 'The person stands behind a low counter at hip height, with the whole upper body above it clearly in view.',
 'The person sits on a sofa with a low coffee table in front, set far enough away that the whole sofa seat, the lap and the feet are visible past it.',
 'The person sits at a desk turned sideways to the camera, so the whole figure from head to feet can be seen along the side of the desk.',
 'The person stands behind the back of a low chair, with the whole body from the shoes up visible above the chair back.'],
'depth_side_by_side': [
 'The people stand side by side in one row at the same distance from the camera, with an arm\'s length of open space between each of them.',
 'The people sit in a straight row along one bench, all at the same distance from the camera, each fully visible with a small gap between shoulders.',
 'The people stand in a wide shallow line facing the camera at three quarters, each person fully separate from the others and every face and pair of feet visible.',
 'The people walk in a loose row across the frame at the same distance from the camera, with a gap of open air between each one.'],
'depth_layered': [
 'One person stands close to the camera, one stands in the middle of the space and one stands far back near the wall, each clearly smaller than the one in front.',
 'The nearest person fills the lower left of the frame, the second person stands a few steps back in the centre, and the third person is small and distant near the back wall, all three fully visible.',
 'Three layers of depth are clear, with a person in the near foreground, a person in the middle distance and a person in the far distance, each one visibly smaller than the last.',
 'The first person stands close with the face large, the second person stands in the middle with the whole body visible, and the third person is small and soft in the distance.'],
'depth_scale_rule': [
 'Each step back makes a person smaller, the person in the middle distance about two thirds as tall in the frame as the nearest person and the person far back about one third as tall.',
 'The far figures are drawn about one third the height of the near figures, with the middle figures about two thirds the height.',
 'Perspective shrinks every figure steadily with distance, so the people far down the lane are small, slightly softer and about a third the height of the people nearest the camera.'],
'depth_tag': [
 'nearest to the camera, large in the frame',
 'in the middle distance, about two thirds the height of the nearest person',
 'far back, small and slightly soft, about one third the height of the nearest person'],
'depth_prompt': ['__depth_foreground_clear__', '__depth_foreground_object__', '__depth_person_in_front__', '__depth_behind_furniture__', '__depth_side_by_side__', '__depth_layered__'],
}
if '--restore' in sys.argv:
    for n in D:
        p = os.path.join(FINAL, n + '.txt')
        if os.path.exists(p): os.remove(p)
    print('removed'); sys.exit()
for n, ls in D.items(): open(os.path.join(FINAL, n + '.txt'), 'w', encoding='utf8', newline='\n').write('\n'.join(ls) + '\n')
print(len(D), 'files written')
