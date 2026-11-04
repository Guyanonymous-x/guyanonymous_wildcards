"""50 photography-style prompts: one signature per prompt from photostyle_sig_*, unique fitting scene, short people, quoted text."""
import sys, os, re, random
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import illus50 as I
from paths import FINAL
def sig(fam, n): return I.rd('photostyle_sig_' + fam)[n - 1]
# id, family, line number, scene ref (None), person (age, 'short'|'long'|None), quoted text, ratio
S = [
('P01','street',1,'city_metro_prompt',None,None,(4,5)),
('P02','street',7,'city_food_street_prompt',None,None,(3,2)),
('P03','street',11,'city_alley_prompt',None,None,(2,3)),
('P04','street',13,'city_station_prompt',None,None,(3,2)),
('P05','street',25,'city_night_prompt',None,None,(16,9)),
('P06','street',35,'city_market_prompt',None,None,(3,2)),
('P07','street',39,'city_bus_stop_prompt',None,'OPEN ALL NIGHT',(4,5)),
('P08','street',43,'loc_food_coffee_shop_scene',('35_44','short'),'CAFE',(1,1)),
('P09','documentary',23,'land_farmland_prompt',None,None,(3,2)),
('P10','documentary',25,'city_airport_prompt',None,None,(3,2)),
('P11','documentary',35,'city_festival_prompt',None,None,(3,2)),
('P12','documentary',37,'land_rolling_hills_prompt',('55_64','short'),None,(3,2)),
('P13','documentary',15,'city_plaza_prompt',('45_54','short'),None,(4,5)),
('P14','early_modernist',3,'city_street_empty_prompt',None,None,(4,5)),
('P15','early_modernist',5,'land_moorland_prompt',None,None,(3,2)),
('P16','early_modernist',31,'city_bridge_prompt',None,None,(2,3)),
('P17','early_modernist',25,'land_rocky_desert_prompt',None,None,(3,2)),
('P18','early_modernist',45,'city_skyline_prompt',None,None,(2,3)),
('P19','early_modernist',35,'act_dance_classes_scene_prompt',None,None,(4,5)),
('P20','fashion',37,'land_desert_dunes_prompt',None,None,(3,2)),
('P21','fashion',29,None,None,None,(2,3)),
('P22','fashion',27,None,None,None,(4,5)),
('P23','fashion',39,'maker_car_scene_prompt',None,None,(3,2)),
('P24','fashion',13,'land_vineyard_valley_prompt',None,None,(3,2)),
('P25','fine_art',13,'city_residential_prompt',None,None,(3,2)),
('P26','fine_art',15,None,None,None,(3,2)),
('P27','fine_art',7,'city_library_empty_prompt',None,None,(1,1)),
('P28','fine_art',33,'land_savanna_prompt',None,None,(3,2)),
('P29','fine_art',5,'city_harbour_prompt',None,None,(1,1)),
('P30','global',1,None,('35_44','long'),None,(1,1)),
('P31','global',31,'city_arcade_prompt',None,'JAZZ',(2,3)),
('P32','global',39,'culture_maghreb_amazigh_prompt',None,None,(3,2)),
('P33','global',43,'culture_andes_scene_prompt',None,None,(3,2)),
('P34','global',35,'loc_food_steam_room_scene',None,None,(3,2)),
('P35','landscape',1,'land_mountain_range_prompt',None,None,(3,2)),
('P36','landscape',5,None,None,None,(16,9)),
('P37','landscape',19,'land_tropical_beach_prompt',None,None,(3,2)),
('P38','landscape',21,'land_glacier_prompt',None,None,(3,2)),
('P39','landscape',31,'land_volcano_prompt',None,None,(3,2)),
('P40','landscape',29,'land_rocky_coast_prompt',None,None,(3,2)),
('P41','landscape',43,'land_night_prompt',None,None,(4,5)),
('P42','new_color',19,'city_stadium_empty_prompt',None,None,(3,2)),
('P43','new_color',35,'city_plaza_empty_prompt',None,'MOTEL POOL',(3,2)),
('P44','new_color',27,None,None,None,(3,2)),
('P45','new_color',47,'land_steppe_prompt',None,None,(3,2)),
('P46','portrait',5,None,('45_54','long'),None,(4,5)),
('P47','portrait',37,None,('25_34','long'),None,(4,5)),
('P48','portrait',45,None,('55_64','long'),None,(4,5)),
('P49','still_life_architecture',47,'bld_v_machiya_scene',None,None,(3,2)),
('P50','still_life_architecture',49,'land_fjord_prompt',None,None,(3,2)),
]
def strip_light(t):
    out = [s for s in re.split(r'(?<=\.) ', t) if not re.match(r'(The light is|The scene is in|Through the glass)', s)]
    return ' '.join(out)
def build(off=0):
    res = []
    for n, (i, fam, ln, sc, pe, tx, ratio) in enumerate(S):
        sd = off + 6000 + n * 13
        s = sig(fam, ln); s = s[0].upper() + s[1:].rstrip('.') + '.'
        parts = [s]
        if sc: parts.append('In the frame: ' + strip_light(I.scene('__%s__' % sc, sd)))
        if pe:
            a, kind = pe
            pt = I.person((I.LG if kind == 'long' else I.SH)(a), sd + 1)
            if kind == 'long': pt = ' '.join(x for x in re.split(r'(?<=\.) ', pt) if not re.search(r'\b(wearing|wears|dressed|outfit)\b', x))
            parts.append(('The subject of the portrait is this person. ' if kind == 'long' else 'A person in the frame. ') + pt)
        if tx: parts.append('The sign reads "%s".' % tx)
        parts.append('The whole image has the look and finish of this one photograph.')
        res.append((i, '%s: %s' % (fam.replace('_', ' '), ln), ratio, ' '.join(parts)))
    return res
