"""50 illustration-style prompts, one distinct style each, unique fitting scene, short people, quoted text. usage: python3 illus50.py"""
import sys, os, re, random
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import expand as E
from paths import FINAL
files = E.load([FINAL])
LB = re.compile(r'nude|naked|topless|bottomless|no clothing|lingerie|bikini|swimsuit|underwear|\bbra\b|bra-style|briefs|boxer|sheer|see-through|sensuous|fetish|latex|costume|cosplay|robe\b|pyjama|loungewear|shirtless|bare|leotard|speedo|thong|corset', re.I)
def rd(n): return [l.strip() for l in open(os.path.join(FINAL, n + '.txt'), encoding='utf8') if l.strip()]
def pick(names, sub):
    for n in names:
        for l in rd(n):
            if l.lower().startswith(sub.lower()): return l
    raise SystemExit('missing: ' + sub)
LIN = ['illustration_lineage_' + x for x in 'african_and_diasporic americas comics_and_animation contemporary_digital east_asian european_folk historical_movements illustration_eras south_and_west_asian technical_and_scientific vernacular'.split()]
MED = ['illustration_medium_' + x for x in 'printmaking wet_media dry_media cut_and_constructed digital_tool'.split()]
SUB = ['illustration_medium_substrate']; CM = ['illustration_color_color_mode']; PAL = ['illustration_color_palette_character']; LQ = ['illustration_line_quality']
KID = re.compile(r'\b(child|children|kid|kids|boy|boys|girl|girls|teen|teens|baby|babies|toddler|toddlers|infant|infants|student|students|schoolchildren|pupils?)\b', re.I)
def scene(ref, seed):
    r = random.Random(seed)
    for _ in range(400):
        t = ' '.join(E.clean(E.expand(files, ref, r)).split())
        if not LB.search(t) and not KID.search(t): return t
    raise SystemExit('scene filter failed ' + ref)
def person(ref, seed, long=False):
    r = random.Random(seed)
    for _ in range(3000):
        t = ' '.join(E.clean(E.expand(files, ref, r)).split())
        if LB.search(t) or ' wearing ' not in t: continue
        f = t.split('. ', 1)
        if len(f) == 2 and ' years old' not in f[0] and len(f[0]) < 90: t = f[1]
        return t
    raise SystemExit('person filter failed')
SH = lambda a: '__any_person_age%s_w_clothes_short__' % a
LG = lambda a: '__any_person_age%s_w_clothes__' % a
# id, style, lineage, medium, substrate, colour mode, palette, line, scene, person(age, 'short'|'long'|None), text, ratio
S = [
('I01','ukiyo-e woodblock','ukiyo-e','woodcut','bright white','a limited palette','a faded vintage','clean confident','city_bridge_prompt',('35_44','short'),None,(3,2)),
('I02','sumi-e ink painting','sumi-e','sumi ink','rough cold','black and white','a muted tonalist','loose gestural','land_bamboo_grove_prompt',None,None,(2,3)),
('I03','Persian miniature','Persian miniature','gouache','smooth hot','full color','a jewel-tone','clean confident','city_park_prompt',('25_34','short'),None,(1,1)),
('I04','Tibetan thangka','Tibetan thangka','gouache','fabric calico','full color','a jewel-tone','clean confident','land_alpine_lake_prompt',None,None,(4,5)),
('I05','Byzantine icon','Byzantine icon','egg tempera','a wood panel','a limited palette','an earthy','clean confident','city_library_prompt',('55_64','long'),None,(4,5)),
('I06','medieval illuminated manuscript','medieval illuminated','gilding','translucent vellum','a moderate palette','a jewel-tone','clean confident','city_market_prompt',('45_54','short'),'MARKET DAY',(4,5)),
('I07','Art Nouveau poster','Art Nouveau','lithograph','bright white','a moderate palette','a faded vintage','wavy rippling','land_river_delta_prompt',('25_34','short'),'SPRING SALON',(2,3)),
('I08','Art Deco travel poster','Art Deco','gouache','smooth hot','a limited palette','a jewel-tone','clean confident','city_station_prompt',('35_44','short'),'GRAND EXPRESS',(2,3)),
('I09','Constructivist poster','Constructivism','screen print','newsprint','duotone','a primary-color','clean confident','city_construction_prompt',('45_54','short'),'BUILD',(4,5)),
('I10','Pop Art','Pop Art','screen print','bright white','flat spot colors','a candy','clean confident','city_food_street_prompt',('18_24','short'),'POP!',(1,1)),
('I11','1960s psychedelic poster','1960s psychedelic','screen print','bright white','a moderate palette','a neon rainbow','wavy rippling','city_festival_prompt',('25_34','short'),'SUMMER FESTIVAL',(2,3)),
('I12','Swiss International Style','Swiss International','letterpress','bright white','flat spot colors','a corporate','clean confident','city_airport_prompt',None,'ARRIVALS',(4,5)),
('I13','Polish School of Posters','Polish School','lithograph','newsprint','a limited palette','a muted tonalist','broken dashed','city_night_prompt',None,None,(2,3)),
('I14','1930s WPA silkscreen poster','1930s WPA','screen print','toned kraft','a limited palette','an earthy','clean confident','land_canyon_prompt',('35_44','short'),'SEE THE CANYON',(4,5)),
('I15','mid-century modern illustration','mid-century modern','gouache','smooth hot','a limited palette','a faded vintage','smooth vector','city_residential_prompt',('35_44','short'),None,(3,2)),
('I16','Golden Age of Illustration','Golden Age','watercolor','rough cold','a moderate palette','a natural local','clean confident','land_temperate_forest_prompt',('25_34','short'),None,(3,2)),
('I17','Victorian engraving','Victorian engraving','wood engraving','bright white','black and white','a sepia','hatched','city_harbour_prompt',('55_64','short'),None,(3,2)),
('I18','botanical plate','botanical illustration','watercolor','smooth hot','a moderate palette','a natural local','clean confident','land_rainforest_prompt',None,'PLATE 12',(4,5)),
('I19','field-guide plate','field-guide plate','etching','old ledger','single-hue tonal color','a sepia','hatched','land_savanna_prompt',None,None,(3,2)),
('I20','Cubism','Cubism','oil paint','canvas','a limited palette','a muted tonalist','clean confident','act_violin_scene_prompt',('35_44','short'),None,(4,5)),
('I21','Surrealism','Surrealism','oil paint','canvas','a moderate palette','a natural local','clean confident','land_salt_flat_prompt',('45_54','short'),None,(3,2)),
('I22','German Expressionist woodcut','Expressionism','woodcut','bright white','duotone','a primary-color','scratchy','city_alley_prompt',('25_34','short'),None,(2,3)),
('I23','Fauvism','Fauvism','oil paint','canvas','full color','a candy','loose gestural','land_tropical_beach_prompt',('25_34','long'),None,(1,1)),
('I24','Impressionism','Impressionism','oil paint','canvas','full color','a pastel','loose gestural','city_canal_prompt',('35_44','short'),None,(3,2)),
('I25','Pre-Raphaelite','Pre-Raphaelite','oil paint','a wood panel','full color','a jewel-tone','clean confident','land_river_valley_prompt',('25_34','long'),None,(4,5)),
('I26','Baroque','Baroque','oil paint','canvas','a limited palette','a muted tonalist','clean confident','act_orchestra_scene_prompt',('45_54','short'),None,(3,2)),
('I27','Romanticism','Romanticism','oil paint','canvas','a moderate palette','a muted tonalist','loose gestural','land_fjord_prompt',('35_44','short'),None,(3,2)),
('I28','shonen manga','shonen manga','fineliner','bright white','black and white','a primary-color','clean confident','city_metro_prompt',('18_24','short'),None,(2,3)),
('I29','anime cel','anime cel','clean, smooth vector','a clean digital','flat spot colors','a pastel','smooth vector','city_rooftop_prompt',('18_24','short'),None,(16,9)),
('I30','ligne claire comics','ligne claire','fineliner','bright white','flat spot colors','a faded vintage','clean confident','city_skyline_prompt',None,None,(3,2)),
('I31','1930s rubber-hose cartoon','1930s rubber-hose','dip pen and ink','bright white','black and white','a sepia','wobbly naive','city_arcade_prompt',None,'OPEN LATE',(4,5)),
('I32','UPA limited animation','UPA-style','gouache','toned kraft','a limited palette','a faded vintage','smooth vector','city_bus_stop_prompt',('35_44','short'),None,(3,2)),
('I33','American superhero comics','American superhero','alcohol marker','bright white','full color','a primary-color','clean confident','city_stadium_prompt',('25_34','short'),None,(2,3)),
('I34','1960s underground comix','1960s underground','dip pen and ink','newsprint','a limited palette','a candy','scratchy','city_street_prompt',('35_44','short'),None,(4,5)),
('I35','Korean minhwa folk painting','Korean minhwa','gouache','rough cold','a limited palette','an earthy','clean confident','land_rolling_hills_prompt',None,None,(3,2)),
('I36','Madhubani painting','Madhubani','fineliner','rough cold','a limited palette','an earthy','hatched','land_farmland_prompt',('45_54','short'),None,(1,1)),
('I37','Warli art','Warli','paint made from mud','a painted wall mural','a limited palette','an earthy','clean confident','land_steppe_prompt',None,None,(3,2)),
('I38','Pakistani truck art','Pakistani truck art','acrylic paint','cardboard','full color','a neon rainbow','clean confident','maker_truck_scene_prompt',None,'SAFE TRAVELS',(16,9)),
('I39','Mexican papel picado','Mexican papel picado','cut paper','translucent vellum','flat spot colors','a candy','clean confident','city_plaza_prompt',None,None,(3,2)),
('I40','Polish wycinanki paper cut','Polish wycinanki','cut paper','black paper','a limited palette','a primary-color','clean confident','land_vineyard_valley_prompt',None,None,(4,5)),
('I41','stained glass window','Arts and Crafts','stained glass','a clean digital','full color','a jewel-tone','clean confident','city_museum_prompt',None,None,(2,3)),
('I42','cyanotype print','Symbolism','cyanotype','rough cold','single-hue tonal color',None,'clean confident','land_wetland_prompt',None,None,(4,5)),
('I43','claymation','adult animation','plasticine claymation','a clean digital','full color','a candy','wobbly naive','act_baking_scene_prompt',('35_44','short'),None,(3,2)),
('I44','paper craft diorama','Scandinavian folk art','papercraft origami','bright white','a moderate palette','a pastel','clean confident','land_glacier_prompt',None,None,(3,2)),
('I45','isometric illustration','isometric illustration','clean, smooth vector','a clean digital','a moderate palette','a pastel','smooth vector','city_campus_prompt',None,None,(1,1)),
('I46','16-bit pixel art','16-bit pixel art','a pixel brush','a clean digital','a limited palette','a neon synthwave','clean confident','land_volcano_prompt',None,None,(16,9)),
('I47','vaporwave','vaporwave','a soft airbrush','a clean digital','a limited palette','a neon synthwave','smooth vector','loc_food_diner_booth_scene',None,'VAPOR',(3,2)),
('I48','low-poly art','low-poly art','sharp lasso-cut','a clean digital','a moderate palette','a pastel','smooth vector','land_mountain_range_prompt',None,None,(16,9)),
('I49','traditional tattoo flash','traditional tattoo flash','dip pen and ink','bright white','a limited palette','a primary-color','clean confident','land_rocky_coast_prompt',None,'ANCHOR',(4,5)),
('I50','chalkboard art','chalkboard art','chalk','black paper','a limited palette','a pastel','sketchy','loc_food_coffee_shop_scene',None,'TODAY: SOUP',(4,5)),
]
def build(off=0):
    out = []
    for n, (i, name, lin, med, sub, cm, pal, lq, sc, pe, tx, ratio) in enumerate(S):
        L = pick(LIN, lin); M = pick(MED, med); Sb = pick(SUB, sub); C = pick(CM, cm); P = pick(PAL, pal) if pal else None; Q = pick(LQ, lq)
        sd = off + 5000 + n * 17
        head = 'An illustration in the tradition of %s, made as %s on %s, in %s%s, drawn with %s.' % (L, M, Sb, C, (' with ' + P) if P else '', Q)
        body = scene('__%s__' % sc if not sc.startswith('__') else sc, sd)
        parts = [head, 'The scene: ' + body]
        if pe:
            a, kind = pe
            pt = person((LG if kind == 'long' else SH)(a), sd + 1)
            parts.append(('A close-up portrait of this person in the scene. ' if kind == 'long' else 'A small figure in the scene. ') + pt)
        if tx: parts.append('The words "%s" appear as lettering in the image.' % tx)
        parts.append('The whole image, the setting, the buildings and any people, is rendered as one flat hand-made artwork in this single style.')
        out.append((i, name, ratio, ' '.join(parts)))
    return out
