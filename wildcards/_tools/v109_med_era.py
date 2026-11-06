"""v109 - decade versions of the medical scenes (user 2026-11-06): the same examinations and operations shown in the decade they could
happen in, with the rooms, equipment, clothing, light and photographic look of that decade.
Decades: 1700s, 1880s, 1920s, 1950s, 1970s, 1990s, 2010s. Each examination lists the first decade it can be shown in (and a last one where it
stopped), and its equipment at each change point; a decade uses the latest change point at or before it.
Files: med_decade_<d>_room/_ward/_theatre/_light/_frame/_outfit_<role>/_dress_<kind>,
       med_exam_<k>_<d>_equipment, med_exam_<k>_<d>_scene, med_exam_<k>_decade_scene (one random valid decade),
       med_surgery_<k>_<d>_scene, med_surgery_<k>_decade_scene, med_exam_decade_any, med_surgery_decade_any, med_scene_decade_any."""
import os, re
from v109_med import gsplit
D = ['1700s', '1880s', '1920s', '1950s', '1970s', '1990s', '2010s']
MIDCENTURY = re.compile(r'\b(second screen|wall screen|digital|laptop|tablet|computer|LED|pulse oximeter|nitrile|disposable|doppler|pump|touch)\b', re.I)
MODERN = re.compile(r'\b(digital|screen|monitor|laptop|tablet|computer|keyboard|printing|print|pump|doppler|nitrile|disposable|plastic|sticky|electrode|LED|pulse oximeter)\b', re.I)

ROOM = {
 '1700s': ['The room has rough whitewashed walls, wide scrubbed floorboards, a heavy oak table, a pewter basin and candles in iron holders.'],
 '1880s': ['The room has dark green painted walls, a polished wooden floor, a horsehair couch covered in black leather, a marble-topped washstand with a jug and basin, and gas lamps on the walls.',
           'The room has brown varnished panelling, glass-fronted cabinets of brass instruments and brown glass bottles, and a coal fire in a small grate.'],
 '1920s': ['The room has cream-painted walls, a black and white tiled floor, an enamel sink with tall taps, a glass-fronted steel instrument cabinet and a frosted glass door.',
           'The room has pale green tiles to shoulder height, a white enamel trolley, a wooden desk with an inkstand and a heavy black telephone.'],
 '1950s': ['The room has pale green walls, a speckled linoleum floor, a steel-framed examination couch in black leather, a porcelain sink with long lever taps and a metal filing cabinet.',
           'The room has cream gloss walls, a wooden desk with a blotter and a bakelite telephone, glass jars of cotton wool and a folding screen of white cloth panels.'],
 '1970s': ['The room has orange and brown patterned curtains, beige walls, a vinyl examination couch in brown, wood-effect cabinets and a ceiling of square tiles with fluorescent strip lights.',
           'The room has mustard yellow walls, a cork noticeboard covered in leaflets, a steel trolley and a beige plastic telephone on a desk.'],
 '1990s': ['The room has pale blue walls with a coloured border strip, a grey vinyl floor, a beige computer with a deep curved monitor on the desk and a padded couch in blue vinyl.',
           'The room has magnolia walls, a speckled grey floor, a spiral-bound appointment book, a fax machine and racks of printed leaflets.'],
 '2010s': ['The room has white walls, a seamless grey vinyl floor, a height-adjustable couch, a wall-mounted hand gel dispenser, a slim computer screen and a soft-close bin.',
           'The room has bright white panels, a coloured feature wall, a disposable curtain on a ceiling track and wipe-clean surfaces.'],
}
THEATRE = {
 '1700s': ['The operating room is a bare whitewashed room with a heavy wooden table, a bucket of sawdust and instruments laid out on a cloth.'],
 '1880s': ['The operating theatre is a steep wooden horseshoe of standing galleries around a wooden table, lit by a skylight, with a sawdust box beneath the table and a brass carbolic spray on a stand.'],
 '1920s': ['The operating theatre has white tiled walls, a large round lamp of mirrored glass overhead, an iron operating table with a crank handle and enamel bowls on a glass shelf.'],
 '1950s': ['The operating theatre has pale green tiled walls, a big round chrome lamp overhead, a steel operating table, glass bottles of fluid on a stand and an anaesthetic machine of black rubber bags and dials.'],
 '1970s': ['The operating theatre has mint green walls, a heavy dome lamp on a ceiling arm, an anaesthetic trolley with chrome gas cylinders and a monitor with a green wavy trace.'],
 '1990s': ['The operating theatre has blue-grey walls, twin dish-shaped lights, a stack of grey monitors on a trolley and a large clock above the door.'],
 '2010s': ['The operating theatre has smooth white wall panels, ceiling-hung pendants carrying screens and lights, LED surgical lamps and a laminar airflow canopy over the table.'],
}
LIGHT = {
 '1700s': ['the warm flicker of candles and grey daylight from a small window'], '1880s': ['soft daylight from tall windows and the yellow glow of gas lamps'],
 '1920s': ['bright daylight from a large window and the hard light of a bare electric bulb'], '1950s': ['flat light from round ceiling lamps and a tall window'],
 '1970s': ['the cool flicker of fluorescent strip lights'], '1990s': ['bright fluorescent ceiling panels'], '2010s': ['clean bright LED panels'],
}
FRAME = {
 '1700s': ['Realistic period scene with warm dark tones and deep candlelit shadows.', 'Realistic period scene with dark wood tones and candlelit shadows, photographic detail.'],
 '1880s': ['Sepia-toned period photograph with soft focus at the edges and fine grain.', 'Realistic photograph with the brown warm tones of an old albumen print.'],
 '1920s': ['Black and white period photograph with fine grain and soft contrast.', 'Silver-toned documentary photograph with deep blacks and soft highlights.'],
 '1950s': ['Period colour photograph with warm saturated colours and soft grain, like an old colour slide.', 'Black and white documentary photograph with crisp contrast.'],
 '1970s': ['Period colour photograph with faded warm tones and a slight orange cast, like an old colour print.', 'Documentary photograph on grainy colour film with soft muted colours.'],
 '1990s': ['Documentary photograph on 35mm colour film with natural colour and fine grain.', 'Colour photograph with slightly flat flash lighting and true-to-life tones.'],
 '2010s': ['Sharp modern documentary photograph with natural colour and clean detail.', 'Crisp digital photograph with balanced exposure and true colour.'],
}
OUTFIT = {  # role class -> decade -> lines
 'doctor': {'1700s': ['M:a long brown coat with wide cuffs, a linen shirt and a powdered wig', 'F:a dark wool gown, a linen cap and a plain apron'], '1880s': ['M:a dark frock coat, a waistcoat with a watch chain and a high white collar', 'F:a high-necked dark wool dress with a white collar and a watch pinned at the chest', 'M:a black suit with a stiff collar and a stethoscope folded in one hand'],
   '1920s': ['M:a three-piece tweed suit with a white coat over the top and a head mirror on a band', 'a long white coat over a dark suit and tie'], '1950s': ['M:a white coat over a shirt and tie, with a stethoscope draped round the neck', 'F:a white coat over a blouse and a pleated skirt, with a stethoscope draped round the neck', 'F:a white coat over a sensible dress, with a stethoscope'],
   '1970s': ['M:a white coat over a wide-collared shirt and a broad patterned tie', 'a white coat over a polo-neck jumper'], '1990s': ['M:a white coat over a striped shirt and tie', 'F:a cardigan and blouse with a stethoscope', 'M:a pullover and open-necked shirt with a stethoscope'],
   '2010s': ['a short-sleeved shirt with a lanyard and an identity card reading "__name_first__", bare below the elbows', 'dark blue scrubs with an identity card reading "__name_first__"']},
 'nurse': {'1700s': ['F:a plain grey wool dress, a white apron and a linen cap', 'M:a plain wool coat and breeches with a linen apron'], '1880s': ['F:a long grey dress with a starched white apron, white cuffs and a frilled white cap', 'M:a white jacket buttoned to the neck and dark trousers'],
   '1920s': ['F:a long-sleeved striped dress, a starched white apron with a bib and a white veil-like cap', 'M:a white high-collared orderly jacket and dark trousers'], '1950s': ['F:a pale blue dress with a white starched apron, a belt with a silver buckle and a small white folded cap', 'M:a white short-sleeved tunic buttoned at the shoulder and dark trousers'],
   '1970s': ['F:a white nylon dress with a navy belt and a small paper cap', 'F:a pale blue tunic dress with short sleeves', 'M:a white tunic with epaulettes and dark trousers'], '1990s': ['a blue and white striped tunic with navy trousers'],
   '2010s': ['a navy tunic with white piping and dark trousers', 'light grey scrubs with a lanyard']},
 'technician': {'1920s': ['a long white coat and a heavy rubber apron'], '1950s': ['a white coat with a small radiation film clip on the pocket'], '1970s': ['a white tunic with a small radiation film clip'],
   '1990s': ['a maroon tunic with a small grey radiation dosimeter'], '2010s': ['navy scrubs with a small grey radiation dosimeter clipped at the chest']},
 'physio': {'1950s': ['F:a white short-sleeved tunic dress with a belt', 'M:a white short-sleeved tunic and white trousers'], '1970s': ['a white tunic over navy trousers'], '1990s': ['a white polo shirt and navy tracksuit trousers'], '2010s': ['a navy polo shirt and stretch trousers']},
 'dentist': {'1880s': ['M:a dark waistcoat and rolled shirt sleeves', 'F:a dark high-necked dress with a white apron'], '1920s': ['a white high-collared tunic buttoned at the side'], '1950s': ['a white side-buttoned tunic'],
   '1970s': ['a white tunic with short sleeves'], '1990s': ['a white tunic, a paper mask and latex gloves'], '2010s': ['white scrubs, a mask, a clear visor and gloves']},
 'surgeon': {'1700s': ['M:a long coat with the sleeves rolled up and a stained leather apron', 'F:a dark wool gown with the sleeves pinned up and a stained leather apron'], '1880s': ['M:a dark frock coat stiff with old stains and a waistcoat, shirt sleeves rolled to the elbow', 'F:a dark high-necked dress with the sleeves pinned back and a long white linen apron'],
   '1920s': ['a long white cotton gown, a cloth cap, a cloth mask and thick rubber gloves'], '1950s': ['a white cotton gown, a white cloth cap, a cloth mask and rubber gloves'],
   '1970s': ['a green cotton gown, a green cap, a paper mask and latex gloves'], '1990s': ['a blue paper gown, a cap, a mask and latex gloves'],
   '2010s': ['teal scrubs under a sterile blue gown, a patterned scrub cap, a mask, a visor and blue gloves']},
}
ROLECLASS = {'gp': 'doctor', 'specialist': 'doctor', 'historic_1700s': 'doctor', 'historic_1800s': 'surgeon', 'nurse': 'nurse', 'radiographer': 'technician', 'sonographer': 'technician',
             'physio': 'physio', 'dentist': 'dentist', 'surgeon': 'surgeon'}
DRESS = {  # dress kind -> decade -> lines
 'clothed': {'1700s': ['F:a long linen shift and a wool shawl', 'M:a coarse wool coat and breeches'], '1880s': ['F:a high-necked dark dress with long sleeves', 'M:a dark wool suit with a waistcoat'],
   '1920s': ['F:a drop-waisted cotton dress', 'M:a wool suit and a collarless shirt'], '1950s': ['F:a knitted twinset and a pleated skirt', 'M:a shirt, tank top and wide trousers'],
   '1970s': ['flared trousers and a wide-collared shirt', 'F:a printed wrap dress'], '1990s': ['jeans and an oversized jumper', 'a denim shirt and chinos'], '2010s': ['a plain jumper and jeans', 'a hoodie and joggers']},
 'sleeve': {'1880s': ['a white shirt with one sleeve rolled high'], '1920s': ['a cotton shirt with one sleeve rolled high'], '1950s': ['F:a blouse with one sleeve rolled high', 'M:a shirt with one sleeve rolled high'],
   '1970s': ['a short-sleeved shirt in a bold print'], '1990s': ['a T-shirt with one sleeve pushed up'], '2010s': ['a short-sleeved T-shirt with one sleeve pushed up']},
 'gown': {'1700s': ['a long coarse linen shift'], '1880s': ['a long white cotton nightshirt'], '1920s': ['a plain white cotton gown with tapes at the back'], '1950s': ['a white cotton gown tied with tapes at the back'],
   '1970s': ['a faded floral hospital gown tied at the back'], '1990s': ['a pale blue gown with a small print'], '2010s': ['a pale blue gown with a small diamond print']},
 'gown_draped': {'1920s': ['a white cotton gown with a heavy white sheet across the lap and knees'], '1950s': ['a white cotton gown with a starched sheet over the lap and knees'],
   '1970s': ['a floral gown with a white sheet over the lap and knees'], '1990s': ['a blue gown with a paper sheet over the lap and knees'], '2010s': ['a blue gown with a paper sheet over the lap and knees']},
 'gown_side': {'1880s': ['a white nightshirt loosened at one shoulder with a sheet folded across the body'], '1920s': ['a white gown opened at one side with a sheet across the body'],
   '1950s': ['a white gown opened at one side with a sheet across the body'], '1970s': ['a floral gown opened at one side with a sheet across the body'],
   '1990s': ['a blue gown opened at one side with a sheet across the body'], '2010s': ['a blue gown opened at one side with a sheet across the body']},
 'shirt_off': {'1950s': ['a white vest and loose shorts'], '1970s': ['a towelling vest and short shorts'], '1990s': ['a cotton vest and cycling shorts'], '2010s': ['a sports vest and shorts']},
 'sedated': {'1970s': ['a floral gown, asleep under sedation with a blanket over the legs'], '1990s': ['a blue gown, asleep under sedation'], '2010s': ['a blue gown, sedated, with a clip on one finger']},
}
# exam key: (first decade, last decade or None, {decade: equipment lines})
EXAM_ERA = {
 'bp': ('1920s', None, {'1920s': ['a mercury blood pressure gauge, a tall glass column in a wooden box with a cloth cuff and a black rubber bulb'], '1970s': ['a wall-mounted mercury gauge with a long rubber tube and a grey cuff'],
        '1990s': ['an aneroid wall gauge with a round dial and a coiled tube'], '2010s': ['a white digital blood pressure monitor with its cuff']}),
 'auscultation': ('1880s', None, {'1880s': ['an early stethoscope with ivory earpieces and woven tubing'], '1920s': ['a stethoscope with red rubber tubing and a bell-shaped chest piece'],
        '1970s': ['a stethoscope with grey tubing and a chrome chest piece'], '2010s': ['a stethoscope with dark blue tubing']}),
 'ear': ('1880s', None, {'1880s': ['a round head mirror strapped to the brow, reflecting lamp light, and a small silver ear speculum'], '1950s': ['a chrome otoscope with a ribbed battery handle'], '2010s': ['a black otoscope with a lit cone tip']}),
 'eye': ('1880s', None, {'1880s': ['a hand ophthalmoscope with a brass wheel of tiny lenses and an oil lamp beside the patient\'s head'], '1950s': ['an electric ophthalmoscope in black and chrome'], '2010s': ['a handheld ophthalmoscope with a small bright light']}),
 'eye_test': ('1920s', None, {'1920s': ['a wire trial frame, a wooden case of loose lenses and a printed letter chart on the wall'], '1970s': ['a heavy grey refractor head on a swinging arm and a lit letter chart'],
        '2010s': ['a grey phoropter covered in dials and a letter chart glowing on a screen']}),
 'throat': ('1880s', None, {'1880s': ['a silver tongue spatula and a head mirror'], '1950s': ['a wooden tongue depressor and a chrome pen torch'], '2010s': ['a wooden tongue depressor and a pen torch']}),
 'abdomen': ('1880s', None, {'1880s': ['a black leather horsehair couch'], '1950s': ['a steel-framed couch with a black leather top'], '1990s': ['a blue vinyl couch covered with a paper roll'], '2010s': ['a paper-covered adjustable couch']}),
 'knee': ('1950s', None, {'1920s': ['a reflex hammer and a wooden goniometer'], '1990s': ['a plastic goniometer and a knee model'], '2010s': ['a goniometer and a knee joint model']}),
 'shoulder': ('1950s', None, {'1950s': ['a pulley rope hung from a wall bracket and a wooden wand'], '1990s': ['an exercise band and a shoulder model'], '2010s': ['a resistance band and a foam roller']}),
 'back': ('1920s', None, {'1920s': ['a reflex hammer and a wall chart of the spine'], '2010s': ['a spinal model on the desk']}),
 'reflex': ('1920s', None, {'1920s': ['a triangular rubber reflex hammer and a steel tuning fork'], '2010s': ['a reflex hammer with a red rubber head and a tuning fork']}),
 'skin': ('1950s', None, {'1950s': ['a large handheld magnifying glass'], '1990s': ['a ring-shaped magnifying lamp'], '2010s': ['a handheld dermatoscope with a lit glass disc']}),
 'blood': ('1950s', None, {'1950s': ['a reusable glass syringe, glass test tubes in a wire rack and a steel kidney dish'], '1990s': ['vacuum blood tubes with coloured caps and a sharps bin'], '2010s': ['a tray of colour-capped tubes and a yellow sharps bin']}),
 'vaccine': ('1880s', None, {'1880s': ['a small steel lancet and a glass vial of vaccine'], '1950s': ['a reusable glass syringe and a steel dish of needles'], '1970s': ['a jet injector gun'], '2010s': ['a tray of small syringes and plasters']}),
 'ecg': ('1920s', None, {'1920s': ['a room-sized ECG apparatus of brass and glass, with the patient\'s hands and one foot resting in jars of salt water'], '1950s': ['a wooden cabinet ECG on castors with rubber suction cups'],
        '1990s': ['a beige ECG cart printing a long paper strip'], '2010s': ['an ECG machine on a trolley with a colour screen']}),
 'spirometry': ('1880s', None, {'1880s': ['a water spirometer, a tall metal bell floating in a tank of water with a scale'], '1970s': ['a wedge-bellows spirometer drawing a line on paper'], '2010s': ['a handheld spirometer and a laptop']}),
 'hearing': ('1950s', None, {'1950s': ['a valve audiometer in a wooden case with large headphones'], '1990s': ['a beige audiometer with sliders'], '2010s': ['a slim audiometer and padded headphones']}),
 'breast': ('1950s', None, {'1950s': ['a steel-framed couch and a folding cloth screen'], '2010s': ['a paper-covered couch and a box of gloves']}),
 'mammogram': ('1970s', None, {'1970s': ['an early mammography machine, a heavy cream-painted x-ray unit with a cone and a flat plate'], '1990s': ['a grey mammography machine and a light box of x-ray films'], '2010s': ['a white mammography machine with a clear compression plate']}),
 'pap': ('1950s', None, {'1950s': ['a steel speculum, a wooden spatula and glass slides in a small box'], '1990s': ['a clear plastic speculum, a wooden spatula and glass slides'], '2010s': ['a clear plastic speculum, a slim brush and a small pot of liquid']}),
 'pelvic': ('1920s', None, {'1920s': ['a steel tray of instruments under a linen cloth'], '2010s': ['a steel tray under a paper cover and a gooseneck lamp']}),
 'prostate': ('1950s', None, {'1950s': ['a box of thick rubber gloves and a tube of jelly'], '2010s': ['a box of gloves and a sachet of gel']}),
 'rectal': ('1950s', None, {'1950s': ['a box of thick rubber gloves and a tube of jelly'], '2010s': ['a box of gloves and a sachet of gel']}),
 'testicular': ('1970s', None, {'1970s': ['a box of gloves and a printed leaflet'], '2010s': ['a box of gloves and a leaflet on self-checking']}),
 'pregnancy': ('1920s', None, {'1920s': ['a trumpet-shaped wooden listening horn for the baby\'s heartbeat'], '1970s': ['a wooden listening horn and a cloth tape measure'], '1990s': ['a handheld doppler with a small speaker'], '2010s': ['a handheld doppler and a paper tape measure']}),
 'ultrasound': ('1970s', None, {'1970s': ['an early ultrasound machine, a large grey cabinet with a small round screen and a probe on a jointed metal arm'], '1990s': ['a beige ultrasound machine with a small black and white screen'], '2010s': ['an ultrasound machine with a large screen and a keyboard']}),
 'pregnancy_scan': ('1970s', None, {'1970s': ['an early ultrasound cabinet with a small round screen showing a blurred shape'], '1990s': ['a beige ultrasound machine printing a small grey picture'], '2010s': ['an ultrasound machine with a large screen and a wall screen facing the patient']}),
 'xray_chest': ('1920s', None, {'1920s': ['a glass x-ray tube on a wooden stand with thick cables looping from the ceiling'], '1950s': ['a heavy x-ray tube on a steel column and a film cassette holder'], '1990s': ['an x-ray tube on a ceiling gantry and a light box of films'], '2010s': ['an x-ray tube on a ceiling gantry and a wall detector panel']}),
 'xray_limb': ('1920s', None, {'1920s': ['a glass x-ray tube over a wooden table'], '1950s': ['an x-ray table with a film cassette'], '1990s': ['an x-ray table and a light box'], '2010s': ['an x-ray table with a flat detector plate']}),
 'ct': ('1990s', None, {'1990s': ['a bulky beige CT scanner ring with a narrow bed'], '2010s': ['a large white CT scanner ring with a sliding bed']}),
 'mri': ('1990s', None, {'1990s': ['a long boxy cream MRI scanner with a narrow tunnel'], '2010s': ['a long white MRI scanner with a wide tunnel']}),
 'endoscopy': ('1970s', None, {'1970s': ['a fibre-optic endoscope with an eyepiece the doctor looks through and a cold light box'], '1990s': ['an endoscope linked to a small video screen'], '2010s': ['an endoscopy stack of screens and a coiled flexible camera tube']}),
 'colonoscopy': ('1970s', None, {'1970s': ['a fibre-optic scope with an eyepiece and a light box'], '1990s': ['a scope linked to a small screen'], '2010s': ['a trolley of screens and a coiled black scope']}),
 'dental': ('1880s', None, {'1880s': ['a red velvet dental chair and a foot-pedal drill'], '1950s': ['a chrome dental chair with a belt-driven drill on a jointed arm'], '1970s': ['a reclining orange dental chair and a high-speed drill'], '2010s': ['a modern dental chair with a swinging instrument tray']}),
 'foot': ('1950s', None, {'1950s': ['a padded chair with a footrest and a tray of small blades'], '2010s': ['a podiatry chair and a magnifying lamp']}),
 'wound': ('1880s', None, {'1880s': ['a brass carbolic spray hissing a mist, curved needles and silk thread'], '1950s': ['a steel tray of forceps, catgut sutures and gauze'], '2010s': ['a sterile dressing pack and sutures']}),
 'cast': ('1880s', None, {'1880s': ['a bucket of water and rolls of muslin dusted with plaster'], '1950s': ['a bowl of water and rolls of plaster bandage'], '2010s': ['rolls of coloured fibreglass cast tape']}),
 'physio': ('1950s', None, {'1950s': ['wooden parallel bars and wall bars'], '1990s': ['parallel bars and small weights'], '2010s': ['parallel bars, resistance bands and a balance board']}),
 'dialysis': ('1950s', None, {'1950s': ['a rotating drum kidney machine, a steel tank with a turning drum wound with tubing'], '1970s': ['a boxy dialysis machine with dials'], '2010s': ['a dialysis machine with a screen']}),
 'chemo': ('1970s', None, {'1970s': ['a glass drip bottle hung upside down on a steel stand'], '1990s': ['a plastic drip bag on a stand'], '2010s': ['an infusion pump on a drip stand']}),
 'triage': ('1990s', None, {'1990s': ['a tympanic thermometer, a finger pulse clip and a clipboard'], '2010s': ['a pulse oximeter, a tympanic thermometer and a tablet showing a form']}),
 'resus': ('1970s', None, {'1970s': ['a heavy defibrillator box with two paddles on curly cables'], '1990s': ['a grey defibrillator on a red trolley'], '2010s': ['a defibrillator on a red crash trolley']}),
 'pre_op': ('1970s', None, {'1970s': ['a weighing scale with sliding weights and a clipboard'], '2010s': ['a digital scale and a clipboard']}),
 'ward_round': ('1880s', None, {'1880s': ['an iron bed with a temperature chart hung on the foot rail'], '1950s': ['a steel bed with a chart on a clipboard'], '1990s': ['a bed with a chart and a drip stand'], '2010s': ['a bed with a drip stand and a computer on wheels']}),
 'iron_lung': ('1920s', '1950s', {'1920s': ['a long steel iron lung with portholes and a bellows'], '1950s': ['a cream-painted iron lung with portholes and a pressure gauge']}),
 'historic_ward': ('1700s', '1700s', {'1700s': ['a pewter cup and a jar of leeches on a stool']}),
}
SURG_ERA = {'hip': ('1970s', None), 'heart': ('1970s', None), 'brain': ('1920s', None), 'cataract': ('1950s', None), 'caesarean': ('1920s', None),
            'hand': ('1950s', None), 'spine': ('1950s', None), 'field': ('1920s', None), 'victorian': ('1880s', '1880s'), 'appendix_open': ('1880s', '1970s'),
            'appendix': ('1990s', None), 'gallbladder': ('1990s', None), 'knee_scope': ('1990s', None), 'robotic': ('2010s', None), 'cath': ('1990s', None),
            'dental_surg': ('1950s', None), 'skin_surg': ('1950s', None)}
SURG_EXTRA = {'appendix_open': (['an operation to remove the appendix through a small cut'], ['operating_theater', 'cottage_hospital'],
    ['the lower right side of the abdomen, a short cut held open by small steel retractors inside a window of linen drapes'],
    ['the surgeon tying a ligature with gloved fingers', 'the assistant holding the retractors apart'], ['a tray of steel instruments and a bowl of gauze'], 'surgeon')}
POS = ['Medium-wide view at eye height showing both people and the equipment between them, sharp focus.', 'Candid view from beside the couch, both people fully visible from head to knee, calm and professional mood.',
       'Wide view from the doorway of the room, both people and the equipment in frame, unposed.', 'Over-the-shoulder view from behind the clinician, the patient and the equipment in clear view.']
POS_SURG = ['Wide view of the operating room from just outside the working area, the whole team and the table in frame.', 'Elevated view from the corner of the room looking down at the table and the team around it.',
            'Medium view at table height across the drapes, the team\'s faces and hands in focus.']
DEC_WORDS = {'1700s': 'the 1700s', '1880s': 'the 1880s', '1920s': 'the 1920s', '1950s': 'the 1950s', '1970s': 'the 1970s', '1990s': 'the 1990s', '2010s': 'the 2010s'}

def _span(first, last): return D[D.index(first): (D.index(last) + 1) if last else len(D)]
def _at(table, d):
    keys = [k for k in D[:D.index(d) + 1] if k in table]
    return table[keys[-1]] if keys else None
def _place(final, room_id):
    l = open(os.path.join(final, 'loc_health_%s_clean.txt' % room_id), encoding='utf8').readline()
    m = re.match(r'(The place is [^.]+\.)', l); return m.group(1) if m else 'The place is a hospital room.'

def fix(G, final, med):
    for d in D:
        G['med_decade_%s_room' % d] = ROOM[d]; G['med_decade_%s_theatre' % d] = THEATRE[d]; G['med_decade_%s_light' % d] = LIGHT[d]; G['med_decade_%s_frame' % d] = FRAME[d]
        G['med_frame_position'] = POS; G['med_frame_position_surgery'] = POS_SURG
        for role, t in OUTFIT.items():
            v = _at(t, d)
            if v: G['med_decade_%s_outfit_%s_f' % (d, role)], G['med_decade_%s_outfit_%s_m' % (d, role)] = gsplit(v)
        for kind, t in DRESS.items():
            v = _at(t, d)
            if v: G['med_decade_%s_dress_%s_f' % (d, kind)], G['med_decade_%s_dress_%s_m' % (d, kind)] = gsplit(v)
    exams_all = []
    for k, (lab, rooms, role, outfit, dress, chap, cp, pp, eq, det) in med.EXAMS.items():
        first, last, equip = EXAM_ERA[k]; b = 'med_exam_%s' % k; rs = role.replace(' ', '_'); rc = ROLECLASS[outfit]
        G[b + '_place'] = [_place(final, r) for r in rooms]
        ch = ' __med_chaperone__' if chap else ''
        per = []
        for d in _span(first, last):
            rx = MODERN if D.index(d) < D.index('1950s') else MIDCENTURY if D.index(d) < D.index('1990s') else None
            keep = lambda xs: [x for x in xs if not (rx and rx.search(x))]
            cps = keep(cp) or ['standing beside the patient, explaining each step of the examination']
            pps = keep(pp) or ['seated quietly, following the instructions']
            dets = keep(det)
            if 'med_decade_%s_outfit_%s_f' % (d, rc) not in G or 'med_decade_%s_dress_%s_f' % (d, dress) not in G:
                raise KeyError('v109_med_era: no %s outfit or %s dress for %s in %s' % (rc, dress, k, d))
            e = b + '_' + d
            G[e + '_equipment'] = _at(equip, d); G[e + '_clinician_pose'] = cps; G[e + '_patient_pose'] = pps
            detail = ' __%s_detail__' % e if dets else ''
            if dets: G[e + '_detail'] = dets
            G[e + '_scene'] = [('A medical scene set in {dw}, showing __{b}_label__. __{b}_place__ __med_decade_{d}_room__ __med_person_{rs}_{cg}__ The {r} wears __med_decade_{d}_outfit_{rc}_{cf}__. '
                                '__{pat}__ The patient wears __med_decade_{d}_dress_{dr}_{pg}__. The {r} is __{e}_clinician_pose__. The patient is __{e}_patient_pose__. Close at hand is __{e}_equipment__.{det}{ch} '
                                'The light is __med_decade_{d}_light__. __med_frame_position__ __med_decade_{d}_frame__').format(dw=DEC_WORDS[d], b=b, d=d, rs=rs, r=role, rc=rc, pat=pat, dr=dress, e=e, det=detail, ch=ch, cg=cg, cf=cg.replace('w', 'f'), pg=pg)
                               for cg in ('w', 'm') for pat, pg in med.patients(k)]
            per.append('__%s_scene__' % e)
        G[b + '_decade_scene'] = per; exams_all.append('__%s_decade_scene__' % b)
    G['med_exam_decade_any'] = exams_all
    surg_all = []
    SURG = dict(med.SURG); SURG.update(SURG_EXTRA)
    for k, (lab, rooms, sites, acts, eq, outfit) in SURG.items():
        first, last = SURG_ERA[k]; b = 'med_surgery_%s' % k
        if k in SURG_EXTRA:
            G[b + '_label'] = lab; G[b + '_site'] = sites; G[b + '_team_action'] = acts; G[b + '_equipment'] = eq
        per = []
        for d in _span(first, last):
            e = b + '_' + d
            rx = MODERN if D.index(d) < D.index('1950s') else MIDCENTURY if D.index(d) < D.index('1990s') else None
            acts_d = [x for x in acts if not (rx and rx.search(x))] or ['the surgeon bent over the table working with steady hands']
            G[e + '_team_action'] = acts_d
            anaes = {'1700s': 'awake and held still by two assistants, a leather strap across the chest', '1880s': 'unconscious under ether dripped onto a cloth mask',
                     '1920s': 'asleep under ether given through a wire mask covered in gauze'}.get(d, 'asleep under general anaesthetic with a breathing tube taped at the mouth')
            if k in med.AWAKE and d not in ('1700s', '1880s', '1920s'): anaes = 'awake under local anaesthetic'
            G[e + '_scene'] = [('A surgical scene set in {dw}, showing __{b}_label__. __med_decade_{d}_theatre__ __med_surgeon_{sg}__ The lead surgeon wears __med_decade_{d}_outfit_surgeon_{sf}__. '
                                'The patient lies on the table {an}, covered by drapes except for __{b}_site__. Two assistants and a nurse in the same style of clothing stand around the table. '
                                'The focus of the work is __{e}_team_action__. The light is __med_decade_{d}_light__. __med_frame_position_surgery__ __med_decade_{d}_frame__').format(dw=DEC_WORDS[d], b=b, d=d, e=e, an=anaes, sg=sg, sf=sg.replace('w', 'f')) for sg in ('w', 'm')]
            per.append('__%s_scene__' % e)
        G[b + '_decade_scene'] = per; surg_all.append('__%s_decade_scene__' % b)
    G['med_surgery_decade_any'] = surg_all
    G['med_scene_decade_any'] = exams_all + surg_all
    return G
