import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from paths import wc_dir, DATA, TOOLS
WC = wc_dir(); TPL = os.path.join(DATA, 'src_templates'); AUDIT = os.path.join(TOOLS, 'audit'); os.makedirs(AUDIT, exist_ok=True)
from wcbuild import build
from gender import IS_M
SRC = OUT = WC + os.sep   # the weighted files are rebuilt in place (options are read first, then the file is rewritten)
T={}
# weights = rough likelihood among adult women worldwide (relative); none_pct = share of blank lines
T['eye_color']=(0,[
("deep chocolate brown irises",22),("almost black dark brown irises",16),("rich chestnut brown eyes",12),
("golden honey brown irises",8),("dark obsidian irises",6),("dull muddy brown irises",4),
("warm hazel irises with gold flecks",3),("warm golden hazel eyes",1.5),("speckled green-brown irises",1),
("rare pale amber irises",2),
("striking piercing blue irises",3),("pale washed-out light blue eyes",1.5),("cool ice blue irises",1),
("bright sapphire blue eyes",1.5),("pale watery blue irises",1),
("vibrant emerald green irises",1),("olive green irises",1),
("cool dark grey irises",0.6),("pale translucent grey eyes",0.3),("dark charcoal grey irises",0.2),
("clear brilliant cyan eyes",0.1),("deep violet-tinged irises",0.02),
("mismatched blue and brown heterochromia eyes",0.15),("reddish albino pink irises",0.01),
("cloudy milky grey cataract-affected eyes",0.4),("faded cloudy aged irises",0.8),
("yellowish jaundiced hazel eyes",0.05),("turbid yellowish eyes",0.03)])
T['hair_color']=(0,[
("jet black dark shiny hair",22),("dark raven black hair",14),("jet black with blue sheen",3),
("rich chocolate brown hair",12),("dark brown with dark roots",1.5),("golden chestnut brown hair",3.5),
("warm hazelnut brown hair",3),("ash brown dull hair",3),("dull greyish brown hair",1.2),
("salt-and-pepper grey mixed hair",4),("silver grey aging hair",4),("pure snowy white hair",2),("mottled grey-brown hair",1.5),
("natural honey blonde hair",1.2),("dirty blonde hair",1.5),("light ash blonde hair",0.8),("golden wheat blonde hair",0.8),
("natural strawberry blonde hair",0.3),("platinum blonde bleached hair",1.5),("bleached brassy yellow hair",0.8),
("vibrant fiery red auburn hair",0.6),("copper red hair",0.6),("deep burgundy red hair",1.0),("bright orange-red hair",0.2),
("bright neon dyed magenta hair",0.1),("faded pink pastel hair",0.2),("faded dye green-tinted hair",0.05),("vibrant royal blue dyed hair",0.1)])
# hair_style is built by hair_build.py (hair-type layer), not here
T['hair_texture']=(0,[
("fine silky smooth hair strands",14),("silky soft hair texture",8),("silky shiny hair texture",5),("smooth polished glossy hair",5),
("glossy healthy hair strands",6),("soft velvety hair texture",2),("supple bouncy hair strands",3),("smooth sleek liquid-like hair",3),
("soft fluffy cloud-like hair",3),("dense springy resilient hair",3),("coarse thick wire-like hair strands",8),("coarse rough natural hair",4),
("thick heavy dense hair strands",5),("rough untamed coarse hair",1),("coarse wiry grey hair",2),("frizzy flyaway unmanageable hair",3),
("frizzy dry coarse hair",2),("dry brittle straw-like hair",2.5),("damaged bleached dry hair strands",2),("dry split-ended damaged hair",3),
("chemically treated stiff hair",1.5),("thin wispy fragile hair strands",2.5),("fine thinning sparse hair",2.5),("brittle breakable thin hair",1),
("dull lifeless limp hair",2.5),("greasy matted limp hair",0.7),("rough weather-beaten hair",0.8),("gritty dusty dirty hair",0.3)])
T['dem_tone']=(0,[
("medium golden-tan skin with warm golden undertones",18),("medium beige skin with neutral balanced undertones",14),("olive skin with greenish undertones",12),("light pink-beige skin with cool pinkish undertones",6),
("light peach skin with peach undertones",5),("tan skin with golden undertones",5),("medium brown skin with earthy brown undertones",10),("bronze skin with warm bronze undertones",6),("copper-brown skin with copper undertones",2),
("deep ebony-brown skin with rich ebony undertones",5),("deep mahogany-brown skin with reddish undertones",4),("deep reddish-brown skin with deep red undertones",1.5),("dark brown skin with cool bluish undertones",2),
("pale porcelain-white skin with faint pale undertones",2),("pale alabaster-white skin with faint undertones",1.5),("ivory skin with cool undertones",2),("light grey-beige skin with ashy neutral undertones",1.5),
("fair skin with a flushed ruddy-red undertone",1.5),("ashen grey-pale skin with grey undertones",0.3),("weathered bronze-brown skin with bronze undertones",1),("sallow yellow-beige skin with yellowish undertones",1.5),
("sunburned red-pink skin over a fair base",0.8),("fair rosy-pink skin with sanguine undertones",1),("dull pale beige skin with muted undertones",0.5),("medium brown skin with uneven hyperpigmented patches",1),
("yellow-tinged jaundiced skin with warm undertones",0.05),("bluish-pale cyanotic skin with cool undertones",0.03),("pale sickly greenish-white skin with cool undertones",0.2)])
T['body_build']=(0,[
("slender delicate frail body build",2.0),("slender athletic build",7),("slender graceful build",8),("petite compact small build",8),
("hourglass curvy proportioned build",8),("lean wiry athletic build",3),("athletic toned fit muscular build",4),("firm toned compact build",2.5),
("broad shoulder athletic build",1.0),("muscular bodybuilder build",0.15),("broad stocky muscular build",0.6),("solid muscular heavy build",0.4),
("square blocky thick build",2),("compact stocky build",2.5),("pear-shaped heavy-bottom build",5),("soft plump chubby build",5),
("plump soft rounded build",4),("soft rounded full build",5),("soft fleshy voluptuous build",2.5),("fleshy heavy full-figured build",4),
("thick heavy-set build",3),("heavy thick-set broad build",2),("heavily overweight obese body build",7),("tall gangly awkward build",0.4),
("skinny bony fragile build",2),("severely underweight frail build",0.5),("bony emaciated thin build",0.15),("tall gaunt emaciated build",0.1)])
T['body_height']=(0,[
("average medium height stature",16),("medium balanced height",10),("average natural height",10),("average sturdy height",4),("slender medium height",6),
("below-average short stature",8),("petite short small stature",6),("petite small stature",3),("petite slender height",4),("very short petite frame",2),
("petite delicate short frame",2),("compact squat short height",2),("short compact sturdy stature",3),("short thick-set stature",2),
("short heavy-set height",1.5),("short stocky frame",2),("frail short diminished stature",0.6),
("above-average tall stature",5),("slender tall graceful height",3),("tall statuesque height",1.5),("tall imposing broad frame",0.5),
("broad tall imposing stature",0.4),("tall gangly long-limbed stature",0.5),("very tall towering stature",0.6),("exceptionally tall leggy stature",0.3),
("towering broad stature",0.1),("towering thin stature",0.1),("dwarfism short-stature frame",0.03)])
T['skin_wrinkle']=(0,[
("smooth unwrinkled youthful skin",14),("smooth tight unblemished skin",6),("smooth firm skin with no lines",5),("faint subtle expression lines",8),
("subtle laugh lines",6),("fine smile lines around eyes",7),("soft faint facial lines",4),("fine dry skin lines",3),("etched forehead worry lines",6),
("deep crow's feet around eyes",5),("crinkled under-eye wrinkles",4),("deep marionette lines around mouth",3),("wrinkled upper lip smoker lines",1.5),
("papery crinkled skin wrinkles",2.5),("fine papery crinkles",2),("deeply furrowed brow wrinkles",1.5),("sun-damaged leathery creased skin",1.2),
("wrinkled sagging neck and cheek skin",2),("wrinkled sagging jawline skin",1.2),("wrinkled sagging chin skin",0.8),("deeply creased aging skin",2),
("heavy drooping skin folds",1.0),("weather-etched deep wrinkles",1.0),("deeply carved facial wrinkles",0.8),("creased sun-aged face",0.8),
("deeply etched cheek creases",0.8),("papery dry forehead wrinkles",0.8),("deep aged facial creases",0.9)])
# optional-feature files: blank lines = "none"
T['dem_unique']=(65,[
("deep dimples on both cheeks",3),("single prominent cheek dimple",5),("cleft chin feature",3),("freckle constellation across nose",3),
("dramatic freckled nose bridge",2),("prominent beauty mark above lip",1.5),("distinctive lip mole",0.8),("prominent forehead mole",1.0),
("distinct facial birthmark",2),("unique skin pigmentation pattern",0.5),("hyper-pigmented facial patch",1.0),("pronounced facial port-wine stain",0.3),
("facial hemangioma mark",0.2),("striking complete heterochromia",0.06),("partial iris heterochromia",0.3),("pronounced albinism traits",0.006),
("subtle albino coloring",0.01),("widespread vitiligo patches across skin",0.15),("marked vitiligo on eyelids",0.05),("distinct depigmented skin spot",0.3),
("poliosis hair patch",0.1),("unique facial asymmetry",3),("congenital facial asymmetry",0.5),("unusual eye shape asymmetry",1.5),
("split eyebrow gap",0.5),("microphthalmia trait",0.01),("prominent ear shape variation",1),("unique jawline dimple",0.3)])
T['mark_tattoo']=(88,[
("small subtle fine-line wrist tattoo",14),("fine-line minimalist tattoo",8),("subtle tiny anchor tattoo",4),("small symbol tattoo behind ear",4),
("delicate script text tattoo on collarbone",6),("colorful watercolor flower tattoo",6),("geometric black ink tattoo",6),("colorful botanical sleeve tattoo",4),
("intricate full sleeve traditional tattoo",3),("bold blackwork tribal tattoo",3),("faded blurred old ink tattoo",5),("faded blurry arm tattoo",3),
("faded linework tattoo patch",2),("faded greenish blue old tattoo",2),("vibrant fresh dark ink tattoo",3),("clean detailed portrait tattoo",1),
("dramatic full back tattoo piece",1.5),("dramatic chest piece tattoo",1),("sprawling dragon back tattoo",0.8),("japanese irezumi style body tattoo",0.8),
("heavy solid black ink tattoo",1.5),("dark bold lettering tattoo",2),("neck tattoo extending to jaw",0.8),("facial tattoo under eye",0.4),
("rough homemade prison style tattoo",0.5),("rough crude hand tattoo",0.6),("patchy incomplete tattoo work",1.0),("scarred laser-removed tattoo shadow",1.0)])

if IS_M:   # men: body_build / body_height are written from male tables (the female option lists are not valid for men)
    T['body_build']=(0,[("slender wiry build",7),("lean athletic build",8),("average everyday build",12),("slim narrow build",8),("toned fit build",6),("athletic V-taper build",4),("muscular build with broad shoulders",4),("bodybuilder-level muscular build",0.3),
        ("powerlifter thick strong build",0.6),("stocky solid build",5),("barrel-chested sturdy build",2.5),("burly heavyset build",3),("dad-bod soft midsection build",9),("soft rounded build",6),("overweight thick-set build",8),("heavy big-bellied build",6),
        ("heavily overweight obese build",6),("tall lanky gangly build",1.2),("skinny bony build",2.5),("severely underweight frail build",0.5),("bony emaciated build",0.15),("tall gaunt build",0.4),("compact muscular build",3),
        ("rugged weathered laborer's build",2),("swimmer's build with broad shoulders and a narrow waist",1.5),("runner's lean sinewy build",3),("wiry endurance build",1.5),("gentle soft low-slung build",1.5)])
    T['body_height']=(0,[("average medium height stature",16),("medium balanced height",10),("average natural height",10),("average sturdy height",4),("lean medium height",6),("below-average short stature",8),("short compact stature",5),("short stocky frame",3),
        ("short slight frame",3),("short thick-set stature",2),("short heavy-set height",1.5),("short wiry stature",2),("short broad stature",1.5),("frail short diminished stature",0.6),("above-average tall stature",7),("lean tall height",4),
        ("tall broad-shouldered stature",3),("tall imposing frame",1.5),("tall rangy long-limbed stature",2),("very tall towering stature",1.2),("exceptionally tall lanky stature",0.6),("towering broad stature",0.3),("towering thin stature",0.2),
        ("tall athletic stature",3),("tall heavyset stature",1.5),("tall slender stature",2),("slightly above-average height",8),("dwarfism short-stature frame",0.03)])
    for _f in ('body_build','body_height'):          # the builder checks the option list against the file, so write the option names first
        _have = [l.strip() for l in open(SRC+_f+'.txt',encoding='utf8') if l.strip()] if os.path.exists(SRC+_f+'.txt') else []
        _names = [o for o,_ in T[_f][1]]
        open(SRC+_f+'.txt','w',encoding='utf8').write('\n'.join(_names + [h for h in dict.fromkeys(_have) if h not in _names])+'\n')
import vocab_colors
T['eye_color']=(0,vocab_colors.eye_table()); T['hair_color']=(0,vocab_colors.hair_table())     # world-population proportions, 200+ options each
if __name__=='__main__':
    for f,(none,tab) in T.items():
        c,n=build(SRC+f+'.txt',OUT+f+'.txt',tab,none_pct=none,extra_share=0 if f in ('eye_color','hair_color') else 0.25)
        tot=2500; top=sorted(c.items(),key=lambda x:-x[1])[:3]
        print(f"{f:14s} none={n:4d} options={len(c)} min={min(c.values())} max={max(c.values())}  top: "+'; '.join(f"{k[:28]} {v/tot*100:.1f}%" for k,v in top))
