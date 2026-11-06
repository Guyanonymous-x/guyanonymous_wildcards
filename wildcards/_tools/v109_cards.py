"""v109 - trading card generator (user 2026-11-06): sports cards, movie cards, artist and musician cards, and more.
Everything on the cards is invented: towns, teams, leagues, films, studios, bands, people and set names come from the name generators,
and every piece of text on a card is quoted with its position. Cards follow the look of their decade (1930s to 2020s), and can be shown
front or back, raw, in a toploader, in a graded case, in a binder page or straight out of a pack.

Files (tc_ prefix):
  tc_decade_<d>_design / tc_decade_design            card design by decade (border, picture style, lettering)
  tc_finish, tc_feature, tc_condition, tc_present, tc_present_graded, tc_photo, tc_set_name, tc_team, tc_mascot, tc_league, tc_number, tc_serial
  tc_<cat>_subject / _action / _setting / _front_text / _back_text / _card / _prompt / _back_prompt     one set per card category
  tc_sports_prompt, tc_movie_prompt, tc_artist_prompt, tc_any_prompt, tc_any_back_prompt, tc_any_decade_<d>_prompt
"""

DECADES = ['1930s', '1950s', '1970s', '1980s', '1990s', '2000s', '2020s']
DESIGN = {
 '1930s': ['a small 1930s card of thin cream board with a softly painted colour picture inside a narrow printed border, the lettering in small dark capitals beneath the picture',
           'a 1930s card with a hand-tinted picture, a decorative printed frame of thin lines and a pale plain back'],
 '1950s': ['a 1950s card with a painted portrait against a flat bright colour background, a white border and a small shield-shaped crest in one corner',
           'a 1950s card with a painted head-and-shoulders picture, a thick white border and bold rounded lettering in a coloured box'],
 '1970s': ['a 1970s card with a slightly faded colour photograph inside a coloured frame with rounded inner corners and a bold colour band across the bottom',
           'a 1970s card with a grainy action photograph, a thick border in two colours and a round coloured disc in the corner'],
 '1980s': ['a 1980s card with a thick border of diagonal coloured stripes around a rectangular photograph and blocky lettering',
           'a 1980s card with a glossy photograph, a border fading from one bright colour to another and a small star in the corner'],
 '1990s': ['a 1990s card with a borderless action photograph, metallic foil lettering and a holographic stripe down one side',
           'a 1990s card with a bold graphic background of swirling colour behind a cut-out action photograph and embossed foil lettering'],
 '2000s': ['a 2000s card with a shimmering mirror-like metallic finish that throws rainbow reflections, a cut-out photograph and sharp angular graphics',
           'a 2000s card with an outer edge cut into a shape that follows the picture, a metallic surface and a small clear window'],
 '2020s': ['a 2020s card with a photograph that runs right out to every edge, minimal thin white lettering and a slim coloured stripe at the bottom',
           'a 2020s card with a clean studio photograph on a gradient background, a thin foil frame and small neat lettering'],
}
FINISH = ['a glossy surface', 'a matte surface', 'a holographic foil surface that shines in rainbow colours', 'a shiny gold foil layer over the whole card', 'a sparkling foil surface patterned like shattered ice',
          'a mirror-like metallic surface that splits the light into rainbow colours', 'a textured surface like canvas', 'a solid black border', 'a silver foil border', 'an embossed raised surface']
FEATURE = ['A small round badge in the top corner reads "ROOKIE".', 'The same name is signed by hand in blue ink across the lower half of the picture.',
           'A small stamped number in the corner reads "__tc_serial__".', 'A small clear window cut into the front holds a square of real worn shirt fabric.',
           'A gold foil stamp in the corner reads "FIRST EDITION".', 'A small round badge in the top corner reads "ALL STAR".', '', '', '', '']
SERIAL = ['01/25', '07/99', '12/50', '03/10', '44/99', '1/1', '19/75', '88/199', '05/05', '23/250']
PRESENT = ['A single trading card lying flat on a dark walnut desk, photographed from directly above with soft window light.',
           'A trading card held between a thumb and two fingers in front of a softly blurred room.',
           'A trading card in a clear rigid plastic sleeve, propped upright against a small stack of other cards on a table.',
           'A trading card standing in a small clear acrylic display stand on a shelf, lit by a warm lamp.',
           'A trading card lying on top of a torn-open foil card pack and its scattered wrapper on a table.',
           'A trading card lying on a white sheet of paper, photographed from directly above in even studio light.',
           'A trading card held up close to the camera by a hand, with a second card blurred behind it.',
           'A trading card lying on a felt table mat beside a magnifying glass and a pair of tweezers.']
GRADED = 'A trading card sealed inside a thick clear hard plastic case from a card grading service, with a printed label strip at the top reading "%s" on the first line and "__tc_set_name__" on the second line, lying on a dark desk.'
PRESENT_GRADED = [GRADED % g for g in ('GEM MINT 10', 'MINT 9', 'GRADE 9.5', 'NEAR MINT 8', 'GRADE 8.5', 'NEAR MINT 7')]
PRESENT_GRADED_MINT = [GRADED % g for g in ('GEM MINT 10', 'MINT 9', 'GRADE 9.5')]
PRESENT_GRADED_NEAR = [GRADED % g for g in ('NEAR MINT 8', 'GRADE 8.5', 'NEAR MINT 7')]
# Loose cards: light that shows wear. Graded cards: clean product light.
PHOTO = ['Close-up photograph in low raking side light that picks out every crease, dent, scuff and worn corner on the card.', 'Natural light photograph, the card in sharp focus so its wear, marks and rounded corners show clearly.',
         'Close-up macro photograph showing the printed dots, the frayed edges and every scratch on the surface.', 'Honest snapshot of the card on the table, true colours, every flaw visible.']
PHOTO_GRADED = ['Sharp product photograph with true colours and fine detail of the print and surface.', 'Clean studio photograph with soft shadows and crisp focus on the case and the card.']
MASCOT = ['Falcons', 'Comets', 'Rovers', 'Wolves', 'Harriers', 'Mariners', 'Stags', 'Otters', 'Thunder', 'Kestrels', 'Badgers', 'Lynx', 'Ravens', 'Pioneers', 'Rangers',
          'Sparks', 'Owls', 'Herons', 'Bison', 'Foxes', 'Hornets', 'Pilots', 'Miners', 'Royals', 'Tides', 'Storm', 'Blaze', 'Anchors', 'Hawks', 'Quakers']
TEAM = ['__name_town__ __name_team_mascot__', '__name_town__ United', '__name_town__ City', 'Athletic __name_town__', '__name_town__ __name_team_mascot__', '__name_town__ __name_team_mascot__', 'FC __name_town__', '__name_town__ Rovers']
LEAGUE = ['__name_town__ District League', 'Northern Counties League', 'Coastal Premier League', 'Valley Conference', 'Grand Union League', 'Highland Cup', 'Lakes Division']
SETNAME = ['__name_brand__ Series One', '__name_brand__ Stars', '__name_brand__ Heritage Collection', 'Legends of the __tc_league__', '__name_brand__ All-Stars',
           '__name_brand__ Chrome Edition', '__name_brand__ Golden Age Set', 'Champions of __name_town__']
NUMBER = ['No. __name_number_small__', '#__name_number_small__', 'CARD __name_number_small__']
PERSON_Y = {'w': 'a woman with __age25_34_hair_color__ and __dem_tone__', 'm': 'a man with __age25_34_hair_color__ and __dem_tone__'}
PERSON_ANY = {'w': 'a woman in her __tc_decade_of_life__ with __age35_44_hair_color__ and __dem_tone__', 'm': 'a man in his __tc_decade_of_life__ with __age35_44_hair_color__ and __dem_tone__'}

# Sports: key -> (sport label, kit, actions, settings, position words, back stat lines)
SPORTS = {
 'bat_ball': ('bat-and-ball baseball-style', 'a pinstriped button-front shirt printed with "__name_team__" across the chest and the number "__name_jersey_number__" below it, a peaked cap and long socks', ['swinging a wooden bat with both hands, eyes on the ball', 'winding up to throw from a raised mound', 'diving to catch a ball in a leather glove', 'sliding feet first into a base in a cloud of dust'], ['a sunny ballpark with a green outfield and a packed stand', 'a dusty infield under floodlights'], ['PITCHER', 'CATCHER', 'SHORTSTOP', 'OUTFIELD'], ['"RUNS 87" on the first line', '"HITS 164" on the second line', '"AVERAGE .312" on the third line']),
 'basketball': ('basketball', 'a sleeveless jersey printed with "__name_team__" across the chest and the number "__name_jersey_number__" below it, loose shorts and high-top shoes', ['rising for a one-handed dunk at the hoop', 'dribbling low past a defender', 'releasing a jump shot with the wrist flicked'], ['a polished wooden court under bright arena lights', 'an outdoor court with a chain-link fence'], ['GUARD', 'FORWARD', 'CENTRE'], ['"POINTS 24.6" on the first line', '"REBOUNDS 8.1" on the second line', '"ASSISTS 5.3" on the third line']),
 'football': ('football (soccer)', 'a short-sleeved striped shirt printed with "__name_team__" across the chest and the number "__name_jersey_number__" below it, shorts, long socks and studded boots', ['striking the ball with the laces in mid-stride', 'leaping to head the ball', 'celebrating with both arms raised', 'diving full length to make a save in padded gloves'], ['a green pitch in a full stadium', 'a muddy pitch in the rain under floodlights'], ['STRIKER', 'MIDFIELD', 'DEFENDER', 'GOALKEEPER'], ['"GOALS 23" on the first line', '"MATCHES 38" on the second line', '"ASSISTS 11" on the third line']),
 'gridiron': ('gridiron football', 'a padded jersey printed with "__name_team__" across the chest and the number "__name_jersey_number__" below it, a hard helmet with a face guard and tight trousers', ['throwing a spiral pass with the arm cocked back', 'running with the ball tucked under one arm', 'stretching out to catch a pass'], ['a striped field under stadium lights', 'a snowy field with steam rising from the players'], ['QUARTERBACK', 'RECEIVER', 'LINEBACKER'], ['"YARDS 4,210" on the first line', '"TOUCHDOWNS 32" on the second line', '"SEASON __name_year__" on the third line']),
 'hockey': ('ice hockey', 'a padded jersey printed with "__name_team__" across the chest and the number "__name_jersey_number__" below it, a helmet with a visor, thick gloves and skates', ['carving a tight turn with ice spraying from the skates', 'taking a slapshot with the stick bent', 'crouched in front of the goal in heavy pads'], ['a white rink with boards and glass behind', 'a frozen outdoor pond lined with pine trees'], ['CENTRE', 'WING', 'DEFENCE', 'GOALTENDER'], ['"GOALS 41" on the first line', '"ASSISTS 52" on the second line', '"GAMES 82" on the third line']),
 'cricket': ('cricket', 'cream whites with "__name_team__" stitched on the chest, pads, gloves and a helmet', ['playing a cover drive with the bat flowing through', 'bowling with the arm high over the head', 'diving to take a catch near the ground'], ['a green oval with a white pavilion', 'a dry pitch under a hot sky'], ['BATTER', 'BOWLER', 'ALL-ROUNDER', 'WICKETKEEPER'], ['"RUNS 1,284" on the first line', '"WICKETS 46" on the second line', '"MATCHES 31" on the third line']),
 'rugby': ('rugby', 'a hooped shirt printed with "__name_team__" across the chest and the number "__name_jersey_number__" below it, shorts and studded boots', ['running hard with the oval ball in both hands', 'diving over the line to score', 'leaping in a lineout to catch the ball'], ['a muddy pitch with tall posts', 'a packed stadium in late sun'], ['WING', 'FLY-HALF', 'PROP', 'FULLBACK'], ['"TRIES 14" on the first line', '"CAPS 52" on the second line', '"POINTS 70" on the third line']),
 'tennis': ('tennis', 'a white polo shirt or tennis dress, a headband and court shoes', ['serving with the racket high overhead', 'hitting a two-handed backhand on the run', 'stretching for a volley at the net'], ['a grass court with white lines', 'a red clay court with the dust kicked up'], ['SINGLES', 'DOUBLES'], ['"TITLES 18" on the first line', '"WINS 412" on the second line', '"RANK 3" on the third line']),
 'golf': ('golf', 'a polo shirt, pressed trousers and a peaked cap', ['finishing a full swing with the club over the shoulder', 'crouching to read a putt on the green', 'chipping out of a sand bunker'], ['a green fairway lined with trees', 'a putting green with a flag'], ['PROFESSIONAL', 'CHAMPION'], ['"WINS 9" on the first line', '"BEST ROUND 63" on the second line', '"MAJORS 2" on the third line']),
 'boxing': ('boxing', 'satin shorts with "__name_surname__" across the waistband, boots and padded gloves', ['throwing a straight punch', 'standing guard with gloves raised', 'raising one glove in victory'], ['a ring with ropes under hard white lights', 'a smoky old gym'], ['HEAVYWEIGHT', 'MIDDLEWEIGHT', 'LIGHTWEIGHT'], ['"WINS 31" on the first line', '"KNOCKOUTS 22" on the second line', '"LOSSES 2" on the third line']),
 'motor': ('motor racing', 'a fireproof racing suit of coloured panels with "__name_brand__" across the chest, and a full-face helmet', ['standing beside an open-wheel race car', 'leaning out of the cockpit with the visor up', 'spraying a bottle of fizzy drink from a podium'], ['a pit lane with mechanics', 'a race track with blurred grandstands'], ['DRIVER', 'CHAMPION'], ['"RACES 112" on the first line', '"WINS 17" on the second line', '"POLES 21" on the third line']),
 'athletics': ('athletics', 'a racing vest with a pinned paper race number reading "__name_jersey_number__" and spiked shoes', ['bursting out of the starting blocks', 'clearing a high bar in a back-arched leap', 'throwing a javelin with the arm stretched back'], ['a red running track in a stadium', 'a field event area under a blue sky'], ['SPRINT', 'HIGH JUMP', 'JAVELIN', 'DISTANCE'], ['"BEST 10.02" on the first line', '"MEDALS 6" on the second line', '"RECORDS 2" on the third line']),
 'cycling': ('road cycling', 'a tight jersey with "__name_team__" across the chest, cycling shorts, a helmet and sunglasses', ['climbing out of the saddle on a steep road', 'sprinting for the line with the bike thrown forward'], ['a mountain road lined with fans', 'a cobbled street'], ['CLIMBER', 'SPRINTER'], ['"STAGE WINS 12" on the first line', '"RACES 240" on the second line', '"TITLES 3" on the third line']),
 'skate': ('skateboarding', 'loose jeans, a T-shirt and skate shoes', ['flying above the lip of a bowl holding the board', 'grinding down a handrail'], ['a concrete skatepark', 'a city plaza with stone ledges'], ['STREET', 'PARK', 'VERT'], ['"CONTESTS 30" on the first line', '"PODIUMS 14" on the second line', '"STANCE GOOFY" on the third line']),
 'surf': ('surfing', 'a wetsuit', ['carving across the face of a big wave', 'crouched inside a curling tube of water'], ['a blue ocean with white spray', 'a sunset beach'], ['SHORTBOARD', 'LONGBOARD'], ['"HEATS WON 88" on the first line', '"TITLES 4" on the second line', '"HOME BREAK __name_town__" on the third line']),
}
# Other categories: key -> (label, subject templates, actions, settings, front text, back lines)
OTHER = {
 'movie_character': ('movie character', ['__tc_person_any__ dressed as a character in __tc_film_costume__'], ['posing in a dramatic stance', 'looking over one shoulder', 'standing with arms folded'],
    ['a dramatic film set with smoke and coloured light', 'a painted backdrop of a city at night', 'a desert landscape at dusk'],
    ['The title "__name_movie__" runs across the top of the card and the name "__name_person__" is printed in a banner at the bottom.'],
    ['"__name_movie__" on the first line', '"STARRING __name_person__" on the second line', '"__tc_studio__" on the third line']),
 'movie_scene': ('movie scene', ['a scene from a film in which __tc_person_any__ wears __tc_film_costume__'], ['running from an explosion of orange light', 'facing a giant shadowy shape', 'standing on a rooftop in the rain'],
    ['a wide cinematic frame with dramatic lighting'], ['The film title "__name_movie__" is printed in bold letters along the bottom, with "SCENE __name_number_small__" small in the corner.'],
    ['"__name_movie__" on the first line', '"SCENE __name_number_small__" on the second line', '"__tc_studio__" on the third line']),
 'movie_poster': ('movie poster', ['a tiny version of a film poster showing __tc_person_any__ in __tc_film_costume__'], ['looking boldly out at the viewer'], ['a painted poster background of bold shapes'],
    ['The title "__name_movie__" is printed across the top in large letters.'], ['"__name_movie__" on the first line', '"__tc_studio__" on the second line', '"RELEASED __name_year__" on the third line']),
 'painter': ('artist (painter)', ['__tc_person_any__ wearing a paint-spattered smock'], ['standing at an easel with a brush raised', 'stepping back to look at a large canvas', 'mixing colours on a wooden palette'],
    ['a sunlit studio full of canvases', 'an attic studio with a skylight'], ['The name "__name_person__" is printed at the bottom with the word "PAINTER" beneath it, and a small square on the card shows one of the artist\'s paintings, __tc_artwork__.'],
    ['"__name_person__" on the first line', '"BORN __name_town__" on the second line', '"WORKS 214" on the third line']),
 'musician': ('musician', ['__tc_person_any__ in stage clothes'], ['playing an electric guitar with the head thrown back', 'singing into a microphone on a stand', 'playing drums with sticks blurred', 'playing a saxophone under a spotlight', 'playing a grand piano'],
    ['a stage with coloured lights and haze', 'a small smoky club stage'], ['The band name "__name_band__" runs across the top and the name "__name_person__" is printed at the bottom.'],
    ['"__name_band__" on the first line', '"ALBUM __name_album__" on the second line', '"FORMED __name_year__" on the third line']),
 'dancer': ('dancer', ['__tc_person_y__ in a dance costume'], ['leaping in a split jump', 'spinning on one foot with arms raised', 'holding a deep backbend'], ['a dark stage with a single spotlight', 'a rehearsal studio with mirrors'],
    ['The name "__name_person__" is printed at the bottom with the word "DANCER" beneath it.'], ['"__name_person__" on the first line', '"COMPANY __name_town__ Ballet" on the second line', '"DEBUT __name_year__" on the third line']),
 'superhero': ('superhero', ['a superhero in __tc_hero_suit__'], ['flying with one fist forward', 'landing in a crouch with one hand on the ground', 'standing on a ledge above a city with the cape blowing'],
    ['a city skyline at night', 'a stormy sky full of lightning'], ['The hero name "__name_hero__" is printed in bold comic lettering at the bottom.'], ['"__name_hero__" on the first line', '"POWER __name_hero_power_tag__" on the second line', '"TEAM __name_hero_team__" on the third line']),
 'creature': ('fantasy creature', ['__tc_creature__'], ['rearing up with wings spread', 'prowling through mist', 'breathing a plume of fire', 'resting on a rock with the tail curled'], ['a misty mountain valley', 'a dark forest with glowing mushrooms', 'a ruined castle'],
    ['The creature name "__tc_creature_name__" is printed in a scroll banner at the bottom.'], ['"__tc_creature_name__" on the first line', '"HABITAT __tc_habitat__" on the second line', '"POWER __name_number_small__" on the third line']),
 'wildlife': ('wildlife', ['__tc_animal__'], ['in its natural habitat', 'mid-stride', 'looking straight at the camera'], ['its natural landscape in soft morning light'],
    ['The animal name "__tc_animal_name__" is printed at the bottom in a simple band.'], ['"__tc_animal_name__" on the first line', '"HABITAT __tc_habitat__" on the second line', '"CARD __name_number_small__ OF 100" on the third line']),
 'vehicle': ('vehicle', ['__tc_vehicle__'], ['racing at speed with the background blurred', 'parked at an angle in bright sunlight', 'taking off with smoke at the wheels'], ['a race circuit', 'an empty desert road', 'a runway at dawn'],
    ['A banner at the bottom reads "__tc_vehicle_name__" with "No. __name_number_small__" in a circle in the corner.'], ['"__tc_vehicle_name__" on the first line', '"TOP SPEED __name_number_small__0" on the second line', '"BUILT __name_year__" on the third line']),
 'space': ('space explorer', ['__tc_person_any__ in a white spacesuit with the helmet under one arm'], ['floating outside a spacecraft on a tether', 'standing on a grey moon surface', 'waving from the steps of a launch tower'], ['black space with the earth behind', 'a launch pad at dawn'],
    ['The name "__name_person__" is printed at the bottom with "MISSION __name_number_small__" beneath it.'], ['"__name_person__" on the first line', '"MISSIONS __name_number_small__" on the second line', '"FIRST FLIGHT __name_year__" on the third line']),
 'dinosaur': ('dinosaur', ['__tc_dinosaur__'], ['roaring with jaws wide open', 'wading through a swamp', 'standing on a ridge against the sky'], ['a prehistoric jungle with ferns and volcanoes'],
    ['The name "__tc_dinosaur_name__" is printed at the bottom in rough stone-style lettering.'], ['"__tc_dinosaur_name__" on the first line', '"LENGTH __name_number_small__ FT" on the second line', '"DIET __tc_diet__" on the third line']),
 'game_character': ('video game character', ['a video game character, __tc_game_hero__'], ['jumping across a gap', 'standing ready with a glowing weapon', 'running towards the viewer'], ['a bright cartoon world of floating platforms', 'a neon city at night'],
    ['The game title "__name_game_title__" is printed at the top and the character level "LEVEL __name_number_small__" at the bottom.'], ['"__name_game_title__" on the first line', '"LEVEL __name_number_small__" on the second line', '"SPECIAL __name_hero_power_tag__" on the third line']),
}
COSTUME = ['a dusty western duster coat and a wide-brimmed hat', 'a sleek silver spacesuit', 'a 1940s trench coat and a fedora', 'a suit of fantasy armour with a long cloak', 'an elegant 1800s ball gown or tailcoat',
           'a pirate coat with brass buttons', 'a futuristic black combat suit with glowing seams', 'a detective\'s tweed suit', 'a medieval knight\'s chainmail', 'a sparkling 1920s evening outfit']
HERO_SUIT = ['a sleek red and gold suit with a flowing cape', 'a dark blue armoured suit with a glowing chest emblem shaped like a star', 'a green suit with lightning-bolt patterns down the sides', 'a silver suit with a visor mask',
             'a purple and black suit with a hood', 'an orange suit with flame patterns and goggles']
CREATURE = ['a dragon with emerald green scales, leathery wings and smoke curling from its nostrils', 'a griffin with the head and wings of an eagle and the body of a lion', 'a stone golem covered in moss',
            'a phoenix of red and gold flame feathers', 'a sea serpent with blue-green scales rising from the waves', 'a unicorn with a spiral silver horn and a white mane', 'a giant wolf with frost-white fur and glowing blue eyes']
CREATURE_NAME = ['EMBERWING', 'STONEHIDE', 'FROSTFANG', 'TIDECOIL', 'SUNPLUME', 'GLOOMCLAW', 'IRONHORN', 'MISTRUNNER']
ANIMAL = [('a snow leopard with thick spotted grey fur', 'SNOW LEOPARD'), ('a bald eagle with spread wings', 'BALD EAGLE'), ('an African elephant with dusty grey skin', 'ELEPHANT'),
          ('a red fox in the snow', 'RED FOX'), ('a humpback whale breaching', 'HUMPBACK WHALE'), ('a tiger with bold black stripes', 'TIGER'), ('a giant panda chewing bamboo', 'GIANT PANDA'),
          ('a barn owl with a heart-shaped white face', 'BARN OWL'), ('a green sea turtle', 'SEA TURTLE'), ('a grey wolf', 'GREY WOLF')]
VEHICLE = ['a low red sports car with sweeping curves', 'a blue open-wheel race car with a tall rear wing', 'a silver propeller fighter plane', 'a black steam locomotive with smoke pouring from the chimney',
           'a yellow rally car splattered with mud', 'a chrome-trimmed 1950s convertible', 'a white jet airliner', 'a heavy off-road truck on huge tyres']
VEHICLE_NAME = ['THUNDER GT', 'APEX RACER', 'SKY HAWK', 'IRON ARROW', 'DUST DEVIL', 'SILVER CRUISER', 'COMET JET', 'MOUNTAIN KING']
DINO = [('a tyrannosaurus with huge jaws and tiny arms', 'TYRANNOSAURUS'), ('a triceratops with three long horns and a bony frill', 'TRICERATOPS'), ('a long-necked brachiosaurus', 'BRACHIOSAURUS'),
        ('a stegosaurus with a row of tall back plates', 'STEGOSAURUS'), ('a velociraptor covered in short feathers', 'VELOCIRAPTOR'), ('a pteranodon with wide leathery wings', 'PTERANODON')]
GAME_HERO = ['a small round hero in a teal hood with big brass goggles', 'a knight in chunky blue armour with a glowing sword', 'a robot with round glowing eyes and spring legs', 'a fox-like creature in a green scarf', 'a space explorer in bulky orange armour with a round visor']
ARTWORK = ['a swirling landscape of bold blue and yellow strokes', 'a quiet still life of pears on a table', 'a portrait in soft dappled light', 'a bright abstract of overlapping coloured squares', 'a misty seascape at dawn']
HABITAT = ['MOUNTAINS', 'FOREST', 'OCEAN', 'SAVANNA', 'ARCTIC', 'JUNGLE', 'DESERT', 'WETLANDS', 'CAVES']
STUDIO = ['__name_brand__ Pictures', '__name_brand__ Studios', '__name_brand__ Films']

def build(final=None):
    G = {}
    for d in DECADES: G['tc_decade_%s_design' % d] = DESIGN[d]
    G['tc_decade_design'] = ['__tc_decade_%s_design__' % d for d in DECADES]
    G['tc_finish'] = FINISH; G['tc_feature'] = FEATURE; G['tc_serial'] = SERIAL; G['tc_present'] = PRESENT; G['tc_present_graded'] = PRESENT_GRADED; G['tc_present_graded_mint'] = PRESENT_GRADED_MINT; G['tc_present_graded_near'] = PRESENT_GRADED_NEAR; G['tc_photo'] = PHOTO; G['tc_photo_graded'] = PHOTO_GRADED
    # shared team name system (used on jerseys, cards and stickers)
    G['name_team_mascot'] = MASCOT; G['name_team'] = TEAM; G['name_jersey_number'] = [str(n) for n in range(0, 100)]
    G['tc_mascot'] = ['__name_team_mascot__']; G['tc_team'] = ['__name_team__']; G['tc_league'] = LEAGUE; G['tc_set_name'] = SETNAME; G['tc_number'] = NUMBER; G['tc_studio'] = STUDIO
    COND = {
     'mint': ['The card is perfect, with sharp square corners, clean edges and a bright glossy surface.', 'The card is flawless, as fresh as the day it was printed, with crisp corners and perfect colour.'],
     'near': ['The card is almost perfect, with a tiny touch of softness on one corner and otherwise clean edges.', 'The card is almost perfect, with one small white speck on an edge and a clean surface.'],
     'played': ['The card is well handled, with all four corners slightly rounded and white fuzz showing along the edges.', 'The card shows clear play wear, with soft rounded corners, a few surface scratches and small white flecks along the edges where the colour has worn away.',
                'The card is handled and worn, with __tc_card_corners__, __tc_card_edges__ and __tc_card_surface__.'],
     'worn': ['The card is heavily worn, with a deep white crease running right across the picture and all four corners rounded and fuzzy.', 'The card is badly worn, faded and yellowed, with a brown water stain in one corner and frayed edges.',
              'The card is very worn, bent in the middle with a crease line, rounded corners and a scuffed surface rubbed pale in patches.', 'The card is worn soft and floppy, with creases criss-crossing the picture and ink rubbed off the edges.'],
     'damaged': ['The card is damaged, with one corner torn away, a pinhole near the top and a large crease through the middle.', 'The card is damaged, with a strip of old yellowed sticky tape across the front and a torn edge.',
                 'The card is damaged, with a pen scribble across the border, a heavy crease and one corner folded over.', 'The card is damaged, water-warped and rippled, with the colours run and a dark stain spreading from one edge.'],
    }
    for k, v in COND.items(): G['tc_cond_%s' % k] = v
    G['tc_condition'] = ['__tc_cond_mint__'] + ['__tc_cond_near__'] * 2 + ['__tc_cond_played__'] * 3 + ['__tc_cond_worn__'] * 3 + ['__tc_cond_damaged__'] * 2
    G['tc_decade_of_life'] = ['twenties', 'thirties', 'forties', 'fifties']
    G['text_grade_plain'] = ['GEM MINT 10', 'MINT 9', 'NEAR MINT 8', 'EXCELLENT 6', 'GRADE 9.5', 'GRADE 8.5']
    G['tc_person_y_w'] = [PERSON_Y['w']]; G['tc_person_y_m'] = [PERSON_Y['m']]; G['tc_person_any_w'] = [PERSON_ANY['w']]; G['tc_person_any_m'] = [PERSON_ANY['m']]
    G['tc_name_w'] = ['__f_names__ __name_surname__']; G['tc_name_m'] = ['__m_names__ __name_surname__']
    G['tc_film_costume'] = COSTUME; G['tc_hero_suit'] = HERO_SUIT; G['tc_creature'] = CREATURE; G['tc_creature_name'] = CREATURE_NAME
    G['tc_vehicle'] = VEHICLE; G['tc_vehicle_name'] = VEHICLE_NAME; G['tc_game_hero'] = GAME_HERO; G['tc_artwork'] = ARTWORK; G['tc_habitat'] = HABITAT
    G['tc_diet'] = ['MEAT', 'PLANTS', 'FISH']
    # animals and dinosaurs: picture and name must match, so each is its own subject/front pair
    G['tc_animal'] = ['__tc_animal_%d__' % i for i in range(len(ANIMAL))]
    G['tc_dinosaur'] = ['__tc_dinosaur_%d__' % i for i in range(len(DINO))]
    cats, backs = [], []
    def an(w): return ('an ' if w[:1].lower() in 'aeiou' else 'a ') + w
    def add(k, label, subjects, actions, settings, front, back, extra=''):
        b = 'tc_%s' % k
        G[b + '_action'] = actions; G[b + '_setting'] = settings
        G[b + '_back_text'] = ['The back reads %s.' % ', '.join(back)]
        person = any('__tc_person_' in x for x in subjects)
        genders = ('w', 'm') if person else ('',)
        for g in genders:
            sfx = '_' + g if g else ''
            G[b + '_subject' + sfx] = [x.replace('__tc_person_y__', '__tc_person_y_%s__' % g).replace('__tc_person_any__', '__tc_person_any_%s__' % g) for x in subjects] if g else subjects
            G[b + '_front_text' + sfx] = [x.replace('__name_person__', '__tc_name_%s__' % g) for x in front] if g else front
        for d in DECADES:
            G['%s_%s_card' % (b, d)] = ['__tc_decade_%s_design__, %s card. __tc_condition__ The picture on the front shows __%s_subject%s__ __%s_action__, with __%s_setting__ behind. __%s_front_text%s__ __tc_feature__ The card has __tc_finish__.'
                                       % (d, an(label), b, ('_' + g if g else ''), b, b, b, ('_' + g if g else '')) for g in genders]
        G[b + '_card'] = ['__%s_%s_card__' % (b, d) for d in DECADES]
        G[b + '_short'] = ['%s card showing __%s_subject%s__' % (an(label), b, ('_' + g if g else '')) for g in genders]
        G[b + '_prompt'] = ['__tc_present__ It is __%s_card__ __tc_photo__' % b] * 8 + ['__tc_present_graded_mint__ Inside is __%s_gcard_mint__ __tc_photo_graded__' % b, '__tc_present_graded_near__ Inside is __%s_gcard_near__ __tc_photo_graded__' % b]
        G[b + '_back_prompt'] = ['The back of a trading card lying flat on a desk, photographed from above. It is printed in two colours on grey card board with a small portrait in the top corner and a ruled table. %s A thin border runs around the edge. __tc_photo__' % G[b + '_back_text'][0]]
        cats.append('__%s_prompt__' % b); backs.append('__%s_back_prompt__' % b)
        return b
    sports = []
    for k, (label, kit, acts, sets, pos, back) in SPORTS.items():
        G['tc_sport_%s_kit' % k] = [kit]; G['tc_sport_%s_position' % k] = pos
        front = ['A banner across the bottom reads "__name_person__", with "__tc_sport_%s_position__" in a small box in the corner.' % k,
                 'The name "__name_person__" is printed down one side of the card.', 'The name "__name_person__" is printed in a coloured box at the bottom, with "%s" in small letters beneath it.' % '__tc_sport_%s_position__' % k]
        subj = ['__tc_person_y__, wearing %s' % kit]
        b = add('sport_' + k, label, subj, acts, sets, front, back + ['"__tc_team__" on the fourth line'])
        sports.append('__%s_prompt__' % b)
    G['tc_sports_prompt'] = sports
    movie, art = [], []
    for k, (label, subj, acts, sets, front, back) in OTHER.items():
        if k == 'wildlife':
            for i, (desc, name) in enumerate(ANIMAL):
                G['tc_animal_%d' % i] = [desc]
            # the name is tied to the picture: one card line per animal
            b = add(k, label, ['__tc_animal__'], acts, sets, front, back)
            for d in DECADES:
                G['%s_%s_card' % (b, d)] = ['__tc_decade_%s_design__, a wildlife card. __tc_condition__ The picture on the front shows %s __%s_action__, with __%s_setting__ behind. The name "%s" is printed at the bottom in a simple band. __tc_feature__ The card has __tc_finish__.' % (d, desc, b, b, name) for desc, name in ANIMAL]
            G[b + '_back_prompt'] = [l.replace('"__tc_animal_name__"', '"%s"' % name) for name in [a[1] for a in ANIMAL] for l in G[b + '_back_prompt']]
            continue
        if k == 'dinosaur':
            for i, (desc, name) in enumerate(DINO): G['tc_dinosaur_%d' % i] = [desc]
            b = add(k, label, ['__tc_dinosaur__'], acts, sets, front, back)
            for d in DECADES:
                G['%s_%s_card' % (b, d)] = ['__tc_decade_%s_design__, a dinosaur card. __tc_condition__ The picture on the front shows %s __%s_action__, with __%s_setting__ behind. The name "%s" is printed at the bottom in rough stone-style lettering. __tc_feature__ The card has __tc_finish__.' % (d, desc, b, b, name) for desc, name in DINO]
            G[b + '_back_prompt'] = [l.replace('"__tc_dinosaur_name__"', '"%s"' % name) for name in [x[1] for x in DINO] for l in G[b + '_back_prompt']]
            continue
        b = add(k, label, subj, acts, sets, front, back)
        if k.startswith('movie'): movie.append('__%s_prompt__' % b)
        if k in ('painter', 'musician', 'dancer'): art.append('__%s_prompt__' % b)
    for k, pairs, word in (('wildlife', ANIMAL, '__tc_animal_name__'), ('dinosaur', DINO, '__tc_dinosaur_name__')):
        b = 'tc_' + k
        G[b + '_front_text'] = [l.replace(word, n) for n in [x[1] for x in pairs] for l in OTHER[k][4]]
        G[b + '_back_text'] = [l.replace(word, n) for n in [x[1] for x in pairs] for l in G[b + '_back_text']]
        G[b + '_subject'] = [x[0] for x in pairs]
        G[b + '_short'] = ['a %s card showing %s' % (k, x[0]) for x in pairs]
    for n in [n for n in G if n.startswith('tc_') and n.endswith('_card')]:
        for tier in ('mint', 'near'):
            G[n[:-5] + '_gcard_' + tier] = [l.replace('__tc_condition__', '__tc_cond_%s__' % tier).replace('_card__', '_gcard_%s__' % tier) for l in G[n]]
    G['tc_movie_prompt'] = movie; G['tc_artist_prompt'] = art
    G['tc_any_prompt'] = cats; G['tc_any_back_prompt'] = backs
    for d in DECADES:
        G['tc_any_decade_%s_prompt' % d] = ['__tc_present__ It is __tc_%s_%s_card__ __tc_photo__' % (c[len('__tc_'):-len('_prompt__')], d) for c in cats]
    G['tc_any_short'] = [c.replace('_prompt__', '_short__') for c in cats]
    G['tc_binder_prompt'] = ['A clear plastic binder page holding six trading cards in two rows of three, lying open on a table, all from one set in the style of __tc_decade_design__. The top row holds __tc_any_short__, __tc_any_short__ and __tc_any_short__. The bottom row holds __tc_any_short__, __tc_any_short__ and __tc_any_short__. __tc_photo__']
    return G
