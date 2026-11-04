"""v77 stage B - people interacting: pairs and small groups of adults in set interactions (handing over, dancing, duelling, chasing, heists, arguments, embraces).
Positions are given left to right. People come from the existing any_person_age*_w_clothes_short pools. Adults only."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from famlib import P
AGES = ['18_24', '25_34', '35_44', '45_54', '55_64', '65_74', '75_84']
PERSON = ['__any_person_age%s_w_clothes_short__' % a for a in AGES[:5] * 2 + AGES[5:]]
ORD = ['First', 'Second', 'Third', 'Fourth', 'Fifth', 'Sixth']
# key|label|arrangement (what the two people are doing, with left and right)
PAIR = """hand_over|handing something over|The person on the left holds out an object and the person on the right takes it with both hands.
gift|giving a gift|The person on the left offers a small wrapped gift and the person on the right looks surprised and pleased.
dance_ballroom|ballroom dancing|They dance in a formal hold, the person on the left leading, in mid-turn.
dance_folk|folk dancing|They dance together with joined hands and bent knees, both laughing.
dance_slow|slow dancing|They sway close together with their foreheads almost touching.
duel_swords|fighting with swords|They face each other with raised swords, blades crossed between them.
duel_fists|in a boxing match|They face each other with raised fists and a wide stance, in a boxing stance.
duel_pistols|in a pistol duel|They stand back to back and then turn, each with a raised pistol, in a tense moment.
chase|in a chase|The person on the right runs ahead, looking back, while the person on the left sprints after them.
heist|in the middle of a heist|They crouch beside a safe, the person on the left listening with a stethoscope and the person on the right holding a bag.
argument|in an argument|They stand close and lean toward each other, the person on the left pointing a finger and the person on the right with arms crossed.
embrace|in an embrace|They hold each other tightly, the person on the left with their eyes closed.
reunion|at a reunion|The person on the right runs in with arms open and the person on the left drops a bag to catch them.
toast|making a toast|They clink glasses and smile, each holding a raised glass.
whisper|sharing a secret|The person on the left leans in to whisper to the person on the right, who raises an eyebrow.
teaching|teaching a skill|The person on the left guides the hands of the person on the right through a careful task.
carry|one carrying the other|The person on the left carries the person on the right on their back, both laughing.
helping_up|helping up|The person on the left reaches a hand down and pulls the person on the right up from the ground.
handshake|shaking hands|They shake hands firmly and look into each other's eyes.
back_to_back|standing back to back|They stand back to back with arms folded, both looking in opposite directions.
cards|playing cards|They sit across a small table, each holding a hand of cards, the person on the right bluffing with a half smile.
chess|playing chess|They sit across a board, the person on the left reaching to move a piece and the person on the right with a chin on one hand.
cooking|cooking together|They stand side by side at a counter, the person on the left stirring a pot and the person on the right chopping vegetables.
photo|taking a photo|The person on the left holds a camera up to frame the person on the right, who strikes a pose.
selfie|taking a selfie|They squeeze close and hold a phone out together, both smiling.
rescue|in a rescue|The person on the left lowers a rope toward the person on the right, who hangs on with both hands.
bandage|tending a wound|The person on the left kneels and wraps a bandage around the forearm of the person on the right.
repair|repairing something|They crouch over an open machine, the person on the left holding a torch and the person on the right turning a wrench.
interview|in an interview|They sit facing each other, the person on the left holding a notepad and the person on the right speaking and gesturing.
arm_wrestle|arm wrestling|They sit across a table with locked hands, both straining and grinning.
piggyback_race|racing each other|They run side by side at full speed, the person on the right just ahead.
hug_goodbye|saying goodbye|They hug at a doorway, the person on the left holding a suitcase.
proposal|in a marriage proposal|The person on the left kneels and holds up a small open box, and the person on the right covers their mouth.
lesson_dance|in a dance lesson|The person on the left shows a step and the person on the right copies it, looking down at their feet.
lift_box|lifting a box|They carry a large box together, the person on the left walking backward.
shelter|sharing an umbrella|They walk close together under one umbrella in rain, the person on the left holding it high.
comfort|comforting|The person on the left sits with an arm around the person on the right, who wipes their eyes.
laugh|laughing together|They lean on each other laughing helplessly.
confess|in a confrontation|The person on the left slams a folder on the table, and the person on the right looks away.
stare_down|in a stare down|They stand nose to nose, neither blinking.
pull_rope|in a tug of war|They pull opposite ends of a rope, leaning hard backward.
pass_baton|passing a baton|The person on the left runs in and puts a baton into the open hand of the person on the right.
trade|trading goods|They stand at a market stall, the person on the left handing over coins and the person on the right wrapping a parcel.
kiss_cheek|greeting with a kiss on the cheek|The person on the left leans in to kiss the person on the right on the cheek.
read_together|reading together|They sit shoulder to shoulder with one open book across their laps.""".split('\n')
REL = P("They are a married couple; They are old friends; They are rivals; They are colleagues; They are siblings; They are strangers who have just met; They are partners in crime; They are teacher and student; They are business partners; They are neighbours; They are a long-time couple; They are former enemies")
SET = P("on a busy city street; in a warm kitchen; on a rooftop at dusk; in a quiet library; on a sunlit beach; in an old warehouse; in a snowy park; in a crowded market; at a train station; on a country road; in a ballroom; in a workshop; in a neon-lit alley; in a lamplit living room; on a wooden dock; in an open field; in a hotel corridor; in a small cafe; in a gym; on a staircase")
MOOD = P("with warm, natural light; with dramatic side light; with soft evening light; with cold overcast light; with golden hour light; with strong contrast and deep shadow; with bright, clean daylight")
CAM = P("in a medium shot showing both people from the knees up; in a full-length shot of both; in a close shot of both faces and hands; from a low angle; from slightly above; in a wide shot with the setting around them; over the shoulder of the person on the left")
# group scenes
GROUP = """crew|as a heist crew|A crew of {n} in dark clothes crouches in a dim hall, the person on the left holding a map, one in the middle picking a lock and the person on the right keeping watch.|{n}
dance_circle|in a dance circle|A circle of {n} dancers holds hands and spins, laughing, with their skirts and coats flying.|{n}
band|as a band|A band of {n} plays together on a small stage, one with a guitar, one at a drum kit and one singing into a microphone.|{n}
dinner|at a dinner table|A group of {n} sits around a crowded dinner table, passing dishes, laughing and talking over each other.|{n}
argument|in an argument at a table|A group of {n} argue at a table, the person on the left standing and pointing while the others lean back or cover their faces.|{n}
chase|in a crowd chase|A group of {n} runs down a street in a line, looking back over their shoulders at something unseen.|{n}
tug|in a tug of war|Two teams pull opposite ends of a rope, {n} people in all, leaning back with straining arms.|{n}
photo|posing for a group photo|A group of {n} squeezes together for a photograph, the tallest at the back and the shortest kneeling at the front.|{n}
meeting|in a meeting|A group of {n} sits around a long table, the person on the left presenting a chart while the others listen or whisper.|{n}
toast|making a toast|A group of {n} raises glasses together in a toast around a small table, all smiling at the person in the middle.|{n}
lineup|in a police line-up|{n} people stand in a row against a height chart, all looking straight ahead, with a numbered card at their feet.|{n}
huddle|in a huddle|A tight huddle of {n} players with arms around each other's shoulders, heads down and bent together.|{n}
carry|lifting a crate together|A group of {n} carries a long wooden crate on their shoulders, walking in step.|{n}
rescue|in a rescue chain|A group of {n} forms a chain, each holding the arm of the next, reaching toward the person at the end.|{n}""".split('\n')
def build(final=None):
    G = {'pi_person': PERSON, 'pi_relationship': REL, 'pi_setting': SET, 'pi_light': MOOD, 'pi_camera': CAM}
    keys = []
    for row in PAIR:
        k, label, arr = row.split('|')
        G['pi_%s_arrangement' % k] = [arr]
        G['pi_%s_prompt' % k] = ['A scene of two people %s. __pi_relationship__. 2 people, described from left to right. %s The scene is %s, shown __pi_camera__, __pi_light__. First person. __pi_person__ Second person. __pi_person__' % (label, arr, '__pi_setting__')]
        G['pi_%s_short' % k] = ['Two people %s. %s First person. __pi_person__ Second person. __pi_person__' % (label, arr)]
        keys.append(k)
    G['pi_pair_prompt'] = ['__pi_%s_prompt__' % k for k in keys]; G['pi_pair_short'] = ['__pi_%s_short__' % k for k in keys]
    gk = []
    for row in GROUP:
        k, label, arr, _ = row.split('|')
        for n in (4, 5, 6):
            people = ' '.join('%s person. __pi_person__' % ORD[i] for i in range(n))
            G['pi_group_%s_%d_prompt' % (k, n)] = ['A scene of a group %s. %d people, described from left to right. %s The scene is __pi_setting__, shown __pi_camera__, __pi_light__. %s' % (label, n, arr.format(n=n), people)]
        G['pi_group_%s_prompt' % k] = ['__pi_group_%s_%d_prompt__' % (k, n) for n in (4, 5, 6)]
        gk.append(k)
    G['pi_group_prompt'] = ['__pi_group_%s_prompt__' % k for k in gk]
    G['pi_prompt'] = ['__pi_pair_prompt__', '__pi_group_prompt__']
    G['pi_action_names'] = [r.split('|')[1] for r in PAIR]
    G['v77_pi_entry_points'] = ['pi_prompt', 'pi_pair_prompt', 'pi_group_prompt'] + ['pi_%s_prompt' % k for k in keys]
    return G
if __name__ == '__main__': print(len(build()))
