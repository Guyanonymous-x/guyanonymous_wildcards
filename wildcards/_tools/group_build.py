"""Builds the GROUP prompts (files named grp_*):  two people (two men, two women, a man and a woman) and three people (MMM, WWW, MMW, MWW).
Runs AFTER the women's and men's libraries are merged (build_all.py calls it) because it reuses their age-bracket / body-type / clothing files.

  grp_person_f, grp_person_m          one compact, complete person (age, look, build and matching clothes), chosen by population share
  grp_2_mm  grp_2_ww  grp_2_mw   grp_3_mmm  grp_3_www  grp_3_mmw  grp_3_mww      finished group prompts (every one stays positive / in-between / negative in tone)
  grp_prompt_master_2 / _3 / grp_prompt_master      pickers (2 people, 3 people, all)
  grp_interact_2_<tone>, grp_interact_3_<tone>      interaction sentences only (use them in your own templates).  tone = positive | mixed | negative
  grp_expression_2_<tone>, grp_expression_3_<tone>  facial expressions that match the tone     grp_relation_<tone>   how the people are related
EVERY line of every interaction file has all the people actively engaged WITH EACH OTHER (touching, facing, talking, arguing, helping, ...),
never standing apart. People are called 'the first / second / third person' so no pronouns have to match."""
import os, sys, random, itertools
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from paths import FINAL
WC = sys.argv[1] if len(sys.argv) > 1 and os.path.isdir(sys.argv[1]) else FINAL
os.environ.setdefault('WC_GENDER', 'f')
from age_model import BRACKETS, BRACKET_SHARE, bname
from body_model import ARCH, SHARE, BAND_OF
from wcbuild import allocate
def w(name, lines): open(os.path.join(WC, name + '.txt'), 'w', encoding='utf8', newline='\n').write('\n'.join(lines) + '\n')
def ex(n): return os.path.exists(os.path.join(WC, n + '.txt'))
def res(g, n):                 # shared (unprefixed) file if it exists, else the f_/m_ one
    if ex(n): return n
    if ex(f'{g}_{n}'): return f'{g}_{n}'
    sys.exit(f'missing wildcard file for {g}: {n}')
# ---------------- persons ----------------
def build_persons():
    for g, noun in (('f', 'woman'), ('m', 'man')):
        pick = []
        for b, cb in zip(BRACKETS, allocate(BRACKET_SHARE, 1000)):
            p = bname(b); band = BAND_OF[b]; lines = []
            for a, ca in zip(ARCH, allocate(SHARE[b], 400)):
                for _ in range(ca):
                    lines.append(f"a {noun} who is __{res(g, p + '_age_years')}__, with __{res(g, p + '_eye_color')}__, __{res(g, p + '_hair_color')}__ and __dem_tone__, "
                                 f"a build described as __{res(g, f'bt_{a}_{band}_body_build')}__, wearing __{res(g, f'{p}_clothing_{a}')}__")
            random.Random(len(lines) + ord(g)).shuffle(lines); w(f'grp_{g}_{p}', lines)
            pick += [f"__grp_{g}_{p}__"] * cb
        random.Random(7).shuffle(pick); w(f'grp_person_{g}', pick)
# ---------------- interactions ----------------
ACT2 = {
 'positive': ["{A} and {B} hug warmly", "{A} laughs while {B} tells a story", "{A} leans in to whisper something to {B}", "{A} and {B} dance together", "{A} helps {B} up from the ground", "{A} puts an arm around {B}'s shoulders",
  "{A} and {B} share a toast, glasses touching", "{A} hands {B} a gift and {B} opens it", "{A} and {B} high-five", "{A} comforts {B} with a hand on {B}'s back", "{A} and {B} walk arm in arm, looking at each other",
  "{A} and {B} study a map together, heads close", "{A} and {B} cook together at a counter", "{A} feeds {B} a bite of food", "{A} and {B} play a board game across a table", "{A} and {B} share a pair of headphones",
  "{A} and {B} take a selfie together", "{A} and {B} page through a photo album", "{A} and {B} hold hands, facing each other", "{A} rests a head on {B}'s shoulder", "{A} teaches {B} a dance step",
  "{A} and {B} share an umbrella in the rain", "{A} and {B} lean back to back, laughing", "{A} braids {B}'s hair", "{A} and {B} kiss gently", "{A} and {B} tap their foreheads together",
  "{A} and {B} sit side by side sharing a blanket", "{A} swings {B} around in a joyful hug", "{A} and {B} sing together, close to one microphone", "{A} and {B} toast marshmallows over a fire",
  "{A} gives {B} a piggyback ride", "{A} holds {B}'s face in both hands and smiles", "{A} and {B} bow to each other respectfully", "{A} shakes {B}'s hand warmly, with the other hand on {B}'s arm",
  "{A} and {B} plant a tree together, hands on the same spade", "{A} and {B} examine an old book, pointing at the same page", "{A} straightens {B}'s collar fondly", "{A} and {B} fold laundry together, laughing"],
 'mixed': ["{A} and {B} talk seriously, standing face to face", "{A} explains something while {B} listens with raised eyebrows", "{A} and {B} negotiate across a table", "{A} hesitates while {B} waits expectantly",
  "{A} offers an apology that {B} considers", "{A} and {B} greet each other awkwardly", "{A} and {B} bargain over an object", "{A} looks sceptically at {B}, who defends an idea", "{A} and {B} sit in a tense, quiet silence side by side",
  "{A} and {B} politely disagree, each with a polite smile", "{A} gives {B} bad news gently", "{A} and {B} reunite after a long time, unsure how to begin", "{A} interviews {B} with a notebook", "{A} and {B} arm-wrestle with grins",
  "{A} teases {B}, who pretends to be annoyed", "{A} and {B} share a long, uncertain look", "{A} consoles {B}, who is not quite ready to be consoled", "{A} asks {B} for a favour, and {B} thinks it over",
  "{A} and {B} study a contract together, frowning", "{A} slips {B} a note, which {B} reads warily", "{A} confides in {B}, who listens guardedly", "{A} and {B} play chess, eyes locked on the board",
  "{A} lectures {B}, who tolerates it with folded arms", "{A} and {B} stand close but neither will speak first", "{A} and {B} share a cautious handshake", "{A} gives {B} directions, pointing, while {B} looks doubtful"],
 'negative': ["{A} and {B} argue loudly, faces close", "{A} points an accusing finger at {B}, who recoils", "{A} shoves {B}, who stumbles back and glares", "{A} and {B} stand toe to toe in a standoff",
  "{A} turns away from {B}, who reaches after {A} angrily", "{A} shouts and {B} shouts back", "{A} and {B} wrestle over a bag", "{A} grabs {B} by the collar", "{A} and {B} grapple, locked together",
  "{A} slams a hand on the table in front of {B}", "{A} sneers at {B}, who clenches both fists", "{A} and {B} glare at each other across a table", "{A} cries while {B} stands cold and unmoved",
  "{A} blocks {B}'s path, and {B} pushes back", "{A} snatches something from {B}'s hands", "{A} and {B} trade insults, jaws set", "{A} slaps {B}'s hand away", "{A} and {B} tug at opposite ends of a coat",
  "{A} backs {B} against a wall, and {B} stares back defiantly", "{A} throws a glass of water at {B}", "{A} and {B} circle each other with fists raised", "{A} refuses to look at {B}, who keeps demanding an answer",
  "{A} tears up a letter in front of {B}", "{A} accuses {B} while {B} shakes a head in denial", "{A} and {B} scream at each other, mouths wide"]}
ACT3 = {
 'positive': ["{A}, {B} and {C} hug in a group embrace", "{A} and {B} dance while {C} claps along", "{A}, {B} and {C} share a toast around a table", "{A} tells a joke and {B} and {C} burst into laughter",
  "{A}, {B} and {C} take a group selfie, heads together", "{A} and {B} lift {C} in celebration", "{A} and {B} help {C} up from the ground", "{A}, {B} and {C} walk arm in arm", "{A}, {B} and {C} play cards, leaning in",
  "{A} comforts {C} while {B} hands {C} a tissue", "{A}, {B} and {C} sit in a circle sharing food", "{A} wraps a blanket around {B} and {C}", "{A}, {B} and {C} sing together, arms over shoulders",
  "{A} and {B} push {C} on a swing, laughing", "{A}, {B} and {C} huddle over a phone, laughing", "{A} dances with {B} while {C} films them, grinning", "{A}, {B} and {C} cook together, passing ingredients",
  "{A}, {B} and {C} raise their arms together in a cheer", "{A} and {B} each take one of {C}'s hands and swing {C} between them", "{A}, {B} and {C} study a map together, heads close"],
 'mixed': ["{A} mediates between {B} and {C}, who disagree politely", "{A} and {B} whisper while {C} watches, curious", "{A}, {B} and {C} huddle over a plan, frowning", "{A} and {B} compete while {C} referees",
  "{A} brings news to {B} and {C}, who react with surprise", "{A} and {C} exchange wary glances as {B} speaks", "{A}, {B} and {C} talk in a tight triangle, voices low", "{A} explains while {B} nods and {C} looks unconvinced",
  "{A}, {B} and {C} bargain over a table of goods", "{A} asks a question and {B} and {C} each give a different answer", "{A}, {B} and {C} share an awkward silence at a table", "{A} introduces {B} to {C}, and the two size each other up",
  "{A} and {B} tease {C}, who pretends to sulk", "{A}, {B} and {C} wait together, eyes darting from face to face", "{A} reads a letter aloud while {B} and {C} react differently"],
 'negative': ["{A} and {B} argue while {C} tries to separate them", "{A} and {B} gang up on {C}, who backs away", "{A}, {B} and {C} shout at each other in a triangle", "{A} blocks {B} from reaching {C}",
  "{A} accuses {B} while {C} stands between them", "{A} and {B} restrain {C}, who struggles", "{A}, {B} and {C} stand in a three-way standoff, each glaring at another", "{A} pushes {B} while {C} grabs {A}'s arm",
  "{A} and {C} turn on {B}, who is cornered", "{A} drags {B} away from {C}, who yells after them", "{A}, {B} and {C} trade accusations, pointing at each other", "{A} throws something at {B}, and {C} ducks while shouting at both",
  "{A} and {B} pull at opposite ends of a bag while {C} tries to grab it", "{A} threatens {B} while {C} looks on, scared", "{A}, {B} and {C} circle each other tensely"]}
EXPR2 = {'positive': ["both smiling broadly", "both laughing, eyes crinkled", "both looking happy and relaxed", "both beaming with affection", "one grinning, the other laughing, eyes locked", "both soft-eyed and tender"],
         'mixed': ["both wearing guarded, serious expressions", "one curious, one cautious, eyes meeting", "both looking uncertain, brows raised", "one smiling slightly, the other unreadable", "both thoughtful, eyes on each other", "tense but polite smiles"],
         'negative': ["both scowling, eyes locked", "one furious and the other defiant", "both enraged, teeth bared", "one in tears, the other cold", "both hostile and glaring", "one fearful, the other aggressive"]}
EXPR3 = {'positive': ["all three smiling and bright-eyed", "all three laughing together", "all three warm and relaxed, looking at each other", "two beaming while the third laughs", "all three delighted"],
         'mixed': ["three different expressions: curious, wary and amused", "all three serious, eyes darting between each other", "two uncertain and one calm", "a polite smile, a frown and a raised eyebrow", "all three guarded but attentive"],
         'negative': ["all three scowling, eyes locked on each other", "two angry and one frightened", "all three furious and shouting", "one crying, one cold, one livid", "all three hostile and wary"]}
REL = {'positive': ["close friends", "a loving couple", "siblings", "old friends", "colleagues who get along", "a family", "new friends", "teammates celebrating"],
       'mixed': ["acquaintances", "business partners", "former friends", "strangers who have just met", "an uneasy family", "colleagues of different ranks", "rivals who respect each other"],
       'negative': ["bitter rivals", "estranged relatives", "ex-partners", "enemies", "strangers in a dispute", "colleagues in a heated conflict", "a quarrelling couple"]}
ORD = ['the first person', 'the second person', 'the third person']
SETTING = ["__settings10000__", "Indoors: __obj_scene_interior__.", "Outdoors: __obj_scene_exterior__.", "The setting is __env_setting__, with __env_scene__ and __env_props__."]
STYLE = ["A candid, photorealistic photograph with __styl_color__ and __styl_detail__.", "A documentary-style photograph with __styl_color__.", "A realistic photograph with __styl_color__ and __styl_detail__.",
         "A cinematic still with __styl_color__.", "A natural, unposed photograph."]
CAMERA = "__prompt_camera_light__"
def write_interactions():
    for tone in ('positive', 'mixed', 'negative'):
        cap = lambda t: t[0].upper() + t[1:] + '.'
        a2 = [cap(x.format(A=ORD[0], B=ORD[1])) for x in ACT2[tone]]; a3 = [cap(x.format(A=ORD[0], B=ORD[1], C=ORD[2])) for x in ACT3[tone]]
        w(f'grp_interact_2_{tone}', a2); w(f'grp_interact_3_{tone}', a3)
        w(f'grp_expression_2_{tone}', EXPR2[tone]); w(f'grp_expression_3_{tone}', EXPR3[tone]); w(f'grp_relation_{tone}', REL[tone])
def line(types, n, tone, R):
    people = ' '.join(f"{o.capitalize()} is __grp_person_{"f" if t == "w" else t}__." for o, t in zip(ORD, types))
    return f"{R.choice(STYLE)} {n} adults: {people} They are __grp_relation_{tone}__. __grp_interact_{n}_{tone}__ Expressions: __grp_expression_{n}_{tone}__. {R.choice(SETTING)} {CAMERA}"
def build_prompts():
    R = random.Random(5); allp = {2: [], 3: []}
    types = {2: ['mm', 'ww', 'mw'], 3: ['mmm', 'www', 'mmw', 'mww']}
    for n, ts in types.items():
        for t in ts:
            orders = sorted(set(itertools.permutations(t)))
            lines = []
            for tone in ('positive', 'mixed', 'negative'):
                for _ in range(40): lines.append(line(R.choice(orders), n, tone, R))
            R.shuffle(lines); w(f'grp_{n}_{t}', lines); allp[n].append(f'grp_{n}_{t}')
        w(f'grp_prompt_master_{n}', [f"__{x}__" for x in allp[n]])
    w('grp_prompt_master', [f"__{x}__" for n in (2, 3) for x in allp[n]])
if __name__ == '__main__':
    build_persons(); write_interactions(); build_prompts(); print('group files written')
