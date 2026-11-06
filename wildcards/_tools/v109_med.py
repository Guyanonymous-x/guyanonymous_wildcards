"""v109 - medical examination, treatment and surgery scenes for the health locations (user 2026-11-06).
Clinical and nonsexual throughout. Adult patients only. Intimate examinations follow real clinical practice: gown, paper sheet or drape,
a chaperone present, the clinician gloved, and the view kept on the people, the equipment and the draping rather than on anatomy.
Surgery shows the team, the sterile drapes and the small framed operating area; nothing beyond iodine-stained skin, gauze and instruments.
Nothing here is referenced from adult_ files, and no child-related place is used.

Files:
  med_doctor / med_patient / med_surgeon            person sentences (clinicians 25-74, patients 18+), recast as 'The doctor is a woman, ...'
  med_outfit_<role>                                  clothing for gp, specialist, nurse, radiographer, sonographer, physio, dentist, surgeon, historic
  med_patient_dress_<kind>                           clothed, gown, gown_draped, top_off_gown, sedated, theatre
  med_chaperone, med_frame, med_frame_surgery, med_light_exam, med_light_theatre, med_glove
  med_exam_<k>_label/_clinician_pose/_patient_pose/_equipment/_detail/_room/_scene   one set per examination or treatment
  med_exam_any_scene                                 any examination scene
  med_surgery_<k>_label/_site/_team_action/_equipment/_room/_scene   one set per operation
  med_team_role, med_surgery_any_scene, med_scene_any
  med_pose_clinician_any / med_pose_patient_any      every clinician and patient pose, for use elsewhere
"""
import os, re

def _lines(final, name):
    with open(os.path.join(final, name + '.txt'), encoding='utf8') as f: return [l.rstrip('\n') for l in f if l.strip()]
OLDBUILD = re.compile(r'elderly|ninety|stooped|shrunken|spine-curved|frail|hunched|aged|old\b|senior', re.I)
YOUNG = ('age18_24', 'age25_34', 'age35_44', 'age45_54', 'age55_64')
FERTILE = ('age18_24', 'age25_34', 'age35_44')
def _recast(role, lines):
    out = []
    for l in lines:
        m = re.match(r'^A (woman|man), (.*)$', l)
        if not m: continue
        body = m.group(2)
        out.append('The %s is a %s, %s' % (role, m.group(1), body))
    return out
def gsplit(lines):
    f = [x[2:] if x.startswith('F:') else x for x in lines if not x.startswith('M:')]
    m = [x[2:] if x.startswith('M:') else x for x in lines if not x.startswith('F:')]
    return f, m
def builds(final, G):
    for g in 'fm':
        for fn in os.listdir(final):
            mm = re.match(r'^%s_bt_([a-z]+)_m_body_build\.txt$' % g, fn)
            if mm:
                keep = [x for x in _lines(final, fn[:-4]) if not OLDBUILD.search(x)]
                G['med_build_%s_%s' % (g, mm.group(1))] = keep or _lines(final, fn[:-4])
CLIN_AGES = ('age25_34', 'age35_44', 'age45_54', 'age55_64', 'age65_74')

OUTFIT = {
 'gp': ['a pale blue shirt with the sleeves rolled to the elbow, dark trousers and a lanyard with an identity card reading "__name_first__"', 'F:a navy knee-length dress with a grey cardigan and a lanyard with an identity card reading "__name_first__"',
        'a white short-sleeved tunic with dark trousers and a fob watch pinned at the chest', 'a checked shirt and chinos with a stethoscope hung around the neck',
        'F:a plain green blouse, dark trousers and a stethoscope hung around the neck'],
 'specialist': ['M:a long white coat over a striped shirt and tie, with a stethoscope in one pocket', 'F:a white coat over a navy blouse, with pens clipped in the breast pocket',
        'dark blue scrubs with an identity card clipped at the chest reading "__name_first__"', 'a white coat over a grey knitted jumper, with reading glasses pushed up on the head'],
 'nurse': ['a navy nurse\'s tunic with white piping, dark trousers and a fob watch pinned at the chest', 'a pale blue nurse\'s tunic with a silver buckled belt and dark trousers',
        'F:a white nurse\'s dress with a navy collar trim and a fob watch', 'light grey scrubs with a lanyard and a pen torch in the pocket'],
 'radiographer': ['a maroon tunic with dark trousers and a small grey radiation dosimeter clipped at the chest', 'navy scrubs with a heavy lead apron over the top and a small grey radiation dosimeter clipped at the chest'],
 'sonographer': ['a teal tunic with dark trousers and a lanyard with an identity card reading "__name_first__"', 'navy scrubs with the sleeves pushed up'],
 'physio': ['a white polo shirt with navy tracksuit trousers and trainers', 'a navy polo shirt with dark stretch trousers and trainers'],
 'dentist': ['white short-sleeved scrubs, a paper face mask, a clear face visor and pale blue gloves', 'a pale green dental tunic, a face mask and magnifying loupes on a headband'],
 'surgeon': ['teal scrubs under a sterile blue surgical gown, a patterned cloth scrub cap, a paper face mask and pale blue gloves',
        'green scrubs under a sterile gown, a blue scrub cap, a face mask, a clear visor and two layers of gloves',
        'blue scrubs under a sterile gown, a cap, a mask and magnifying loupes with a small headlight'],
 'historic_1800s': ['M:a dark wool frock coat stiff with old stains, a waistcoat and shirt sleeves rolled to the elbow', 'M:a long black coat, a high white collar and a dark cravat',
        'M:a white linen apron over a dark suit with the cuffs turned back', 'F:a high-necked dark dress with the sleeves pinned back and a long white linen apron'],
 'historic_1700s': ['M:a long brown coat with wide cuffs, a linen shirt and a leather apron', 'M:a dark coat and breeches, a powdered wig and a stained linen apron', 'F:a dark wool gown with a linen cap and a stained apron'],
}
DRESS = {
 'clothed': ['their everyday clothes, a plain jumper and jeans', 'their everyday clothes, a cotton shirt and trousers', 'F:a light summer dress and sandals',
             'a work shirt and dark trousers', 'a hooded sweatshirt and jogging bottoms', 'F:a smart blouse and a knee-length skirt'],
 'sleeve': ['a short-sleeved T-shirt with one sleeve pushed up above the elbow', 'a shirt with the left sleeve rolled up high on the arm', 'a vest top that leaves the upper arms bare'],
 'gown': ['a pale blue hospital gown with a small diamond print, tied at the back', 'a faded green hospital gown tied at the neck', 'a white cotton examination gown with short sleeves'],
 'gown_draped': ['a hospital gown, with a white paper sheet draped across the lap and over both knees', 'a pale blue gown, with a folded cotton sheet covering everything from the waist to the knees',
             'a short examination gown, with a disposable paper drape laid across the hips and thighs'],
 'gown_side': ['a hospital gown opened at one side only, with the other side and a sheet kept across the body', 'an examination gown loosened at one shoulder, with a cotton sheet folded across the waist'],
 'shirt_off': ['a sports vest and loose shorts', 'a fitted sports top and track pants', 'shorts and a vest top', 'a sleeveless running top and shorts'],
 'sedated': ['a hospital gown, lying asleep under light sedation with a blanket across the legs', 'a gown and a blue paper sheet, sedated and resting with a clip on one finger'],
}
CHAPERONE = ['A nurse in a navy tunic stands at the head of the couch as a chaperone, speaking quietly to the patient.',
             'A healthcare assistant in light grey scrubs stands to one side as a chaperone, holding a box of gloves.',
             'A nurse stays in the room as a chaperone, standing by the curtain with a calm expression.']
GLOVE = ['pale blue nitrile gloves', 'purple nitrile gloves', 'white latex-free gloves']
LIGHT_EXAM = ['bright, even ceiling light with a gooseneck examination lamp angled in', 'soft daylight from a frosted window and cool white overhead panels',
              'clean clinical lighting, white walls throwing the light back evenly', 'a single bright examination lamp pooling light over the couch and a dimmer room around it']
LIGHT_THEATRE = ['two large round surgical lights overhead pouring white light onto the operating area while the edges of the room fall into shadow',
                 'cool even theatre lighting with the overhead lamps focused tightly on the table', 'bright white light from a ring of overhead lamps and the green glow of monitors']
FRAME = ['Medium-wide documentary photograph at eye height showing both people and the equipment between them, sharp focus, natural colour.',
         'Candid medical photograph from beside the couch, both people fully visible from head to knee, calm and professional mood.',
         'Wide shot from the doorway of the room, both people and the equipment in frame, realistic and unposed.',
         'Over-the-shoulder view from behind the clinician, the patient and the equipment in clear view, shallow depth of field.']
FRAME_SURG = ['Wide documentary photograph of the operating room from just outside the sterile area, the whole team and the table in frame.',
              'Elevated view from the corner of the theatre looking down at the table and the team around it, sharp detail.',
              'Medium shot at table height across the sterile drapes, the team\'s masked faces and gloved hands in focus.',
              'Photograph from the head end beside the anaesthetic machine, the team working along the length of the table.']

def _scene_tpl(k, chaperone):
    ch = ' __med_chaperone__' if chaperone else ''
    return ('A medical scene showing __med_exam_%s_label__. __med_exam_%s_room__ __med_doctor__ The %s wears __med_outfit_%s__. __med_patient__ The patient wears __med_patient_dress_%s__. '
            'The %s is __med_exam_%s_clinician_pose__. The patient is __med_exam_%s_patient_pose__. Close at hand is __med_exam_%s_equipment__. __med_exam_%s_detail__%s The light is __med_light_exam__. __med_frame__')

# key: label lines, rooms, role word, outfit, dress, chaperone, clinician poses, patient poses, equipment, detail
EXAMS = {
 'bp': (['a blood pressure check, a routine check-up in which the doctor measures blood pressure with an arm cuff'], ['gp_consulting_room', 'outpatient_clinic_room', 'pharmacy_consultation_room', 'pre_operative_assessment'], 'doctor', 'gp', 'sleeve', False,
   ['seated beside the desk, wrapping a grey blood pressure cuff around the patient\'s upper arm', 'leaning in to read the numbers on the small digital monitor while the cuff inflates', 'holding the patient\'s forearm steady on the desk with one hand and pressing the start button with the other'],
   ['seated with one arm resting flat on the desk, palm up, the cuff fastened around the bare upper arm', 'sitting upright with feet flat on the floor, watching the monitor'],
   ['a white digital blood pressure monitor with its cuff and tube', 'an aneroid blood pressure gauge with a round dial and a black rubber bulb'],
   ['The desk holds a keyboard, a computer screen showing a patient record and a box of tissues.', 'A height chart and a hand gel dispenser are fixed to the wall behind them.']),
 'auscultation': (['a chest examination, the doctor listening to the heart and lungs with a stethoscope'], ['gp_consulting_room', 'outpatient_clinic_room', 'a_e_minors', 'pre_operative_assessment'], 'doctor', 'gp', 'gown', False,
   ['standing behind the patient, pressing the stethoscope to the patient\'s upper back while looking at the floor in concentration', 'standing in front of the patient with the stethoscope earpieces in, holding the chest piece flat below the collarbone', 'leaning slightly forward, one hand on the patient\'s shoulder, listening'],
   ['sitting on the edge of the examination couch, breathing in slowly through the mouth', 'sitting upright with hands resting on the knees and shoulders relaxed'],
   ['a stethoscope with dark blue tubing', 'a stethoscope with black tubing and a steel chest piece'],
   ['A roll of paper sheet covers the examination couch.', 'A pale curtain on a ceiling track is half drawn around the couch.']),
 'ear': (['an ear examination with an otoscope'], ['gp_consulting_room', 'outpatient_clinic_room', 'a_e_minors'], 'doctor', 'gp', 'clothed', False,
   ['standing beside the patient, gently pulling the top of the ear back and up while looking through a lit otoscope', 'bending to the patient\'s side with the otoscope tip at the ear, the other hand resting on the head'],
   ['seated sideways on a chair with the head tilted slightly away', 'sitting very still, eyes looking forward'],
   ['a black otoscope with a small lit cone tip', 'a wall-mounted diagnostic set with an otoscope on a coiled cord'], ['A box of disposable ear-tip covers sits open on the desk.']),
 'eye': (['an eye examination with an ophthalmoscope in a darkened room'], ['gp_consulting_room', 'outpatient_clinic_room'], 'doctor', 'specialist', 'clothed', False,
   ['face close to the patient\'s face, peering through a small handheld ophthalmoscope into one eye', 'holding the ophthalmoscope up to one eye while steadying the patient\'s brow with a thumb'],
   ['seated, staring at a fixed point on the far wall', 'sitting upright with chin raised slightly, eyes wide'],
   ['a handheld ophthalmoscope with a small bright light', 'an eye chart of black letters lit on the far wall'], ['The blinds are drawn and only the small instrument light glows.']),
 'eye_test': (['an eye test on a phoropter, the large dial-covered lens frame used to measure for glasses'], ['outpatient_clinic_room'], 'optometrist', 'specialist', 'clothed', False,
   ['seated beside the patient, turning a dial on the phoropter', 'pointing to the eye chart with a pen while asking which lens is clearer'],
   ['seated in a padded chair with the face pressed to the phoropter', 'looking through the lenses at the chart on the far wall'],
   ['a grey phoropter on a swinging arm, covered in dials and small lens windows', 'a chart on the far wall reading "E" on the top line, "F P" on the second line and "T O Z" on the third line'], ['A trial frame and a case of loose lenses sit on the counter.']),
 'throat': (['a throat examination with a tongue depressor and pen torch'], ['gp_consulting_room', 'a_e_minors'], 'doctor', 'gp', 'clothed', False,
   ['shining a small pen torch into the patient\'s open mouth while pressing the tongue down with a flat wooden depressor'],
   ['seated with the head tipped back and mouth wide open'],
   ['a pen torch and a wooden tongue depressor', 'a jar of wrapped wooden tongue depressors'], ['A swab tube in a clear bag waits on the desk.']),
 'abdomen': (['an abdominal examination, the doctor pressing gently on the stomach to check for tenderness'], ['gp_consulting_room', 'a_e_majors', 'treatment_room'], 'doctor', 'gp', 'gown_side', False,
   ['standing at the side of the couch, pressing the flat of one hand gently on the patient\'s stomach with the other hand on top', 'watching the patient\'s face for any wince while feeling the lower right side of the stomach'],
   ['lying flat on the couch with arms by the sides and knees slightly bent', 'lying back with the head on a thin pillow, the gown folded up to the ribs and a sheet across the hips'],
   ['a paper-covered examination couch', 'a box of gloves on the side counter'], ['The curtain is fully drawn around the couch.']),
 'knee': (['a knee examination, testing the knee joint for injury'], ['gp_consulting_room', 'physiotherapy_gym', 'a_e_minors'], 'doctor', 'specialist', 'shirt_off', False,
   ['holding the patient\'s heel in one hand and the bent knee in the other, slowly straightening the leg', 'kneeling beside the couch, pressing the thumbs around the edges of the kneecap'],
   ['lying on the couch in shorts with one knee bent up', 'sitting on the couch edge with both legs hanging down'],
   ['a reflex hammer and a goniometer, a hinged plastic angle measure', 'an anatomical model of a knee joint on the desk'], ['A pair of crutches leans against the wall.']),
 'shoulder': (['a shoulder examination, checking the range of movement'], ['physiotherapy_gym', 'outpatient_clinic_room'], 'physiotherapist', 'physio', 'shirt_off', False,
   ['standing behind the patient with one hand on the shoulder blade and the other guiding the patient\'s raised arm', 'holding the patient\'s elbow and slowly rotating the arm outward'],
   ['standing with one arm raised out to the side', 'seated on a treatment bench, lifting an arm slowly overhead'],
   ['a long resistance band and a small foam roller', 'a skeleton model of the shoulder on a stand'], ['Exercise balls and wall bars fill the background.']),
 'back': (['a back and spine examination'], ['gp_consulting_room', 'physiotherapy_gym'], 'doctor', 'specialist', 'gown', False,
   ['standing behind the patient, running two fingers down the line of the spine', 'pressing gently with a thumb at the lower back and asking where it hurts'],
   ['standing with the gown open at the back, bending forward slowly to touch the knees', 'standing straight with arms by the sides'],
   ['a reflex hammer and a spinal model on the desk'], ['A poster of the spine hangs on the wall.']),
 'reflex': (['a reflex test with a rubber reflex hammer'], ['gp_consulting_room', 'outpatient_clinic_room'], 'doctor', 'specialist', 'clothed', False,
   ['tapping just below the patient\'s kneecap with a triangular rubber reflex hammer', 'holding the patient\'s relaxed forearm and tapping the inside of the elbow'],
   ['sitting on the couch edge with legs dangling loosely, the lower leg kicking forward', 'seated with arms resting loosely in the lap'],
   ['a reflex hammer with a red rubber head', 'a tuning fork and a small torch'], ['A neurology chart is pinned to the noticeboard.']),
 'skin': (['a skin check, examining a mole with a dermatoscope'], ['outpatient_clinic_room', 'gp_consulting_room'], 'dermatologist', 'specialist', 'shirt_off', False,
   ['bending close to the patient\'s shoulder with a small dermatoscope pressed against a mole', 'holding a magnifying lamp over the patient\'s upper back, studying a freckle'],
   ['sitting on the couch with the back turned to the doctor', 'standing with one arm held out to the side'],
   ['a handheld dermatoscope with a lit glass disc', 'a ring-shaped magnifying lamp on an adjustable arm'], ['A body map chart lies on the desk with small marks pencilled on it.']),
 'blood': (['a blood test, a phlebotomist drawing blood from the inside of the elbow'], ['phlebotomy_room', 'gp_consulting_room', 'oncology_day_unit'], 'phlebotomist', 'nurse', 'sleeve', False,
   ['seated at the patient\'s side, holding a slim needle in the crook of the patient\'s arm as a tube fills with dark red', 'tightening a blue tourniquet above the elbow and tapping the inside of the arm'],
   ['seated in a padded chair with one arm stretched out on the armrest, looking away', 'resting the arm on a padded support, fist clenched'],
   ['a tray of colour-capped blood tubes, cotton wool balls and a sharps bin', 'a blue tourniquet and a pack of alcohol wipes'], ['A rack of labelled tubes stands on the counter.']),
 'vaccine': (['a vaccination, an injection into the upper arm'], ['mass_vaccination_center', 'gp_consulting_room', 'pharmacy_consultation_room'], 'nurse', 'nurse', 'sleeve', False,
   ['holding a small syringe at the patient\'s upper arm, about to give the injection', 'pressing a small round plaster onto the patient\'s upper arm'],
   ['seated sideways, sleeve rolled up, looking at the far wall', 'sitting relaxed with one shoulder bare'],
   ['a tray of small syringes, alcohol wipes and plasters', 'a yellow sharps bin and a fridge of vaccine vials'], ['A queue of chairs is set out at spaced intervals in the background.']),
 'ecg': (['an ECG heart trace, with sticky electrodes on the chest wired to a machine'], ['treatment_room', 'a_e_majors', 'pre_operative_assessment'], 'nurse', 'nurse', 'gown_side', False,
   ['pressing small white sticky electrodes in a line across the patient\'s chest', 'watching the wavy green lines on the screen of the ECG machine'],
   ['lying back on the couch with wires running from the chest, arms resting at the sides'],
   ['an ECG machine on a wheeled trolley printing a long strip of pink graph paper', 'a box of small white electrode pads'], ['A curtain is pulled round the couch.']),
 'spirometry': (['a lung function test, blowing hard into a spirometer'], ['outpatient_clinic_room', 'gp_consulting_room'], 'nurse', 'nurse', 'clothed', False,
   ['holding the device steady and calling out encouragement', 'watching a curve rise on the laptop screen'],
   ['seated upright with a clip on the nose, blowing hard into a white tube', 'leaning forward, cheeks puffed, lips sealed round the mouthpiece'],
   ['a handheld spirometer with a cardboard mouthpiece and a nose clip', 'a laptop showing a rising breath curve'], ['A box of cardboard mouthpieces sits on the desk.']),
 'hearing': (['a hearing test in a soundproof booth'], ['outpatient_clinic_room'], 'audiologist', 'specialist', 'clothed', False,
   ['seated outside the booth window, pressing keys on an audiometer', 'adjusting the headphones on the patient\'s head'],
   ['seated in the booth wearing large headphones, raising a hand at each tone', 'holding a push button and listening with eyes closed'],
   ['an audiometer with sliders and keys', 'heavy padded headphones on a cable'], ['The booth walls are lined with grey foam panels.']),
 'breast': (['a clinical breast examination, a routine check for lumps, carried out with a chaperone present'], ['gp_consulting_room', 'outpatient_clinic_room'], 'doctor', 'gp', 'gown_side', True,
   ['standing at the side of the couch, the flat pads of the gloved fingers moving in small slow circles over the patient\'s chest beneath the opened side of the gown', 'gently pressing the side of the chest and the armpit with gloved fingertips, explaining each step'],
   ['lying back on the couch with one arm raised and the hand resting behind the head', 'lying on the couch looking at the ceiling, the gown and a sheet covering the other side of the body'],
   ['a box of gloves and a paper-covered couch', 'a diagram of a breast self-check on the wall'], ['The curtain is drawn and the door is shut.']),
 'mammogram': (['a mammogram, a breast x-ray in which a clear plate gently presses the breast flat'], ['x_ray_room'], 'radiographer', 'radiographer', 'gown_side', False,
   ['standing beside the patient, guiding her shoulder into position against the mammography machine', 'turning a knob to lower the clear plastic compression plate'],
   ['standing close against the tall mammography machine, the gown slipped from one shoulder, holding a handle on the far side', 'standing very still with the chin raised and one arm resting on top of the machine'],
   ['a tall white mammography machine with a clear plastic compression plate', 'a screen behind a protective glass panel showing a grey x-ray image'], ['A lead screen with a small window stands to one side of the room.']),
 'pap': (['cervical screening, also called a pap smear test, carried out with a chaperone present'], ['gp_consulting_room', 'treatment_room', 'outpatient_clinic_room'], 'nurse', 'nurse', 'gown_draped', True,
   ['seated on a low stool at the foot of the couch, behind the raised paper sheet, angling a gooseneck lamp', 'holding a slim brush and a small pot of liquid, explaining what will happen next'],
   ['lying back on the couch with knees bent up and apart under a paper sheet, feet together, looking at the ceiling', 'lying on the couch with head on a pillow, a paper sheet tented over the raised knees'],
   ['a tray holding a clear plastic speculum, a slim sampling brush and a small labelled pot of preservative liquid', 'a gooseneck examination lamp and a box of gloves'],
   ['A curtain is drawn around the couch and a modesty sheet covers the patient from the waist to the knees.', 'The paper sheet hides everything below the patient\'s waist from view.']),
 'pelvic': (['a gynaecology pelvic examination, carried out with a chaperone present'], ['outpatient_clinic_room', 'treatment_room'], 'gynaecologist', 'specialist', 'gown_draped', True,
   ['seated at the foot of the couch on a wheeled stool, hidden behind the draped sheet up to the shoulders', 'standing at the foot of the couch pulling on a fresh pair of gloves'],
   ['lying back with knees bent under a white sheet, head turned to talk to the chaperone'],
   ['a steel tray of instruments under a paper cover and a gooseneck lamp'], ['The sheet covers the patient from the waist to below the knees.']),
 'prostate': (['a prostate examination, a rectal check of the prostate, carried out with a chaperone present'], ['gp_consulting_room', 'outpatient_clinic_room'], 'doctor', 'gp', 'gown_draped', True,
   ['standing behind the patient, pulling on a glove and reaching for a sachet of lubricating gel', 'standing at the side of the couch, a hand resting on the patient\'s hip over the sheet, explaining each step'],
   ['lying on his left side on the couch, knees drawn up towards the chest, a paper sheet over the hips and legs', 'curled on one side facing the wall, the gown and a sheet covering him'],
   ['a box of gloves and a sachet of lubricating gel', 'a paper-covered couch and a roll of tissue'], ['The curtain is drawn fully around the couch.']),
 'rectal': (['a rectal examination, a routine check of the bowel, carried out with a chaperone present'], ['gp_consulting_room', 'a_e_majors', 'outpatient_clinic_room'], 'doctor', 'gp', 'gown_draped', True,
   ['standing behind the patient at the side of the couch in fresh gloves', 'pulling the curtain closed and talking the patient through what will happen'],
   ['lying on the left side with knees drawn up, a sheet covering the body', 'curled on one side, facing the wall'],
   ['a box of gloves, a sachet of gel and tissues', 'a paper-covered couch'], ['A roll of tissue sits on the side counter.']),
 'testicular': (['a testicular examination, a check for lumps, carried out with a chaperone present'], ['gp_consulting_room', 'outpatient_clinic_room'], 'doctor', 'gp', 'gown_draped', True,
   ['standing beside the patient in gloves, the view of the hands hidden by the gown and sheet', 'seated at the desk explaining a diagram before the examination'],
   ['lying on the couch with a sheet across the waist and thighs'],
   ['a box of gloves and a printed leaflet on self-checking'], ['The curtain is drawn around the couch.']),
 'pregnancy': (['a pregnancy check-up, a midwife measuring the bump with a tape measure'], ['outpatient_clinic_room', 'gp_consulting_room'], 'midwife', 'nurse', 'gown_side', False,
   ['running a soft paper tape measure over the curve of the patient\'s pregnant belly', 'pressing a handheld doppler to the belly, smiling as the heartbeat sounds'],
   ['lying back on the couch, the gown lifted over the round pregnant belly and a sheet across the hips', 'reclining against pillows with both hands resting on the bump'],
   ['a handheld doppler with a small speaker and a tube of gel', 'a paper tape measure and maternity notes in a folder'], ['A folded towel and a box of tissues sit on the side counter.']),
 'ultrasound': (['an ultrasound scan, a probe moved over gel on the skin'], ['ultrasound_room'], 'sonographer', 'sonographer', 'gown_side', False,
   ['seated beside the couch, sliding the ultrasound probe through clear gel on the patient\'s stomach while watching the screen', 'pointing at a grainy grey shape on the monitor'],
   ['lying back on the couch with the gown folded up, paper towel tucked along the waist', 'lying on one side facing the screen'],
   ['an ultrasound machine with a keyboard, a screen of grainy black and white images and a probe on a cable', 'a bottle of clear ultrasound gel and a roll of blue paper towel'], ['The room is dim so the screen can be seen clearly.']),
 'pregnancy_scan': (['a pregnancy ultrasound scan, the first look at the baby on screen'], ['ultrasound_room'], 'sonographer', 'sonographer', 'gown_side', False,
   ['moving the probe across the gel on the round belly and turning the screen towards the patient', 'freezing the image and printing a small black and white picture'],
   ['lying back with the belly uncovered and a paper towel at the waist, staring at the screen', 'lying back holding the hand of a partner seated beside the couch'],
   ['an ultrasound machine with a screen showing a grey curled shape', 'a strip of printed scan pictures'], ['A second screen on the wall faces the patient.']),
 'xray_chest': (['a chest x-ray'], ['x_ray_room'], 'radiographer', 'radiographer', 'gown', False,
   ['standing in the doorway behind a lead screen, finger on the exposure button', 'adjusting the height of the x-ray plate to the patient\'s shoulders'],
   ['standing with the chest pressed against a flat upright panel, hands on the hips and elbows forward', 'holding a deep breath with the chin up'],
   ['an x-ray tube on a ceiling gantry pointing at a wall-mounted detector panel', 'a lead apron hanging on a hook'], ['A heavy lead-lined door stands half open.']),
 'xray_limb': (['an x-ray of a wrist after a fall'], ['x_ray_room', 'a_e_minors'], 'radiographer', 'radiographer', 'sleeve', False,
   ['positioning the patient\'s hand flat on the detector plate', 'lowering the x-ray tube head and switching on the crosshair positioning light'],
   ['seated sideways at the x-ray table, one hand lying flat on the plate', 'wearing a lead apron over the lap, holding the injured wrist still'],
   ['an x-ray table with a flat detector plate and a tube head above it', 'a computer screen showing the bones of a hand'], ['A soft splint and a sling wait on the chair.']),
 'ct': (['a CT scan, the patient sliding through a large ring-shaped scanner'], ['ct_suite'], 'radiographer', 'radiographer', 'gown', False,
   ['standing at the side of the scanner bed, placing a foam pad under the patient\'s knees', 'seated at the control desk behind glass, watching slices of image appear'],
   ['lying flat on the narrow scanner bed with arms raised above the head', 'lying still as the bed slides into the ring'],
   ['a large white ring-shaped CT scanner with a sliding bed', 'a control desk with three screens behind a window'], ['A drip stand holds a bag of contrast fluid by the bed.']),
 'mri': (['an MRI scan in a long tunnel-shaped scanner'], ['mri_suite'], 'radiographer', 'radiographer', 'gown', False,
   ['handing the patient a call button and a pair of ear defenders', 'fitting a padded cage-like coil over the patient\'s head'],
   ['lying on the scanner bed with a coil over the head, about to slide into the tunnel', 'lying inside the bright white tunnel, only the feet visible'],
   ['a long white MRI scanner with a deep round tunnel', 'ear defenders and a rubber squeeze-ball call button'], ['Copper-lined walls and a window into the control room surround the scanner.']),
 'endoscopy': (['an endoscopy, a thin flexible camera tube passed to look inside the stomach'], ['endoscopy_suite'], 'consultant', 'specialist', 'sedated', False,
   ['feeding a long black flexible tube while watching a pink tunnel-like image on the screen', 'holding the control handle of the endoscope with one hand'],
   ['lying on the left side on a trolley, sedated, a plastic mouth guard between the teeth', 'lying on one side asleep under sedation with a nurse beside the head'],
   ['an endoscopy stack, a tall trolley of screens and units with a coiled flexible camera tube', 'a monitor showing the pink inside of the stomach'], ['A nurse watches the oxygen reading on a small monitor.']),
 'colonoscopy': (['a colonoscopy, a camera examination of the bowel under sedation'], ['endoscopy_suite'], 'consultant', 'specialist', 'sedated', False,
   ['standing behind the patient guiding the flexible scope, eyes on the large screen', 'turning the dials on the scope handle'],
   ['lying on the left side under sedation, covered from the waist down with a blue sheet', 'lying curled on one side, asleep, a blanket over the legs'],
   ['a screen showing the inside of the bowel', 'a trolley of screens and a coiled black scope'], ['A nurse adjusts the blanket over the patient.']),
 'dental': (['a dental check-up'], ['dental_surgery'], 'dentist', 'dentist', 'clothed', False,
   ['leaning over the patient with a small round mirror and a hooked probe in the open mouth', 'angling the overhead dental light down into the patient\'s mouth'],
   ['reclined in the dental chair with mouth wide open and protective glasses on', 'lying back in the chair, a paper bib clipped at the chest'],
   ['a dental chair with a swinging tray of small steel instruments and a bright overhead light', 'a suction tube and a small cup of pink mouthwash'], ['An x-ray image of teeth glows on a wall screen.']),
 'foot': (['a foot examination at a podiatry clinic'], ['podiatry_room'], 'podiatrist', 'specialist', 'clothed', False,
   ['seated on a low stool, holding the patient\'s bare foot in a gloved hand and testing the skin with a thin nylon filament', 'filing the patient\'s heel with a small rotary tool'],
   ['reclined in the podiatry chair with trouser legs rolled up and bare feet raised'],
   ['a podiatry chair with a footrest and a tray of small instruments', 'a magnifying lamp on an arm'], ['A model of a foot skeleton sits on the shelf.']),
 'wound': (['wound care, a nurse cleaning and stitching a cut on the forearm'], ['a_e_minors', 'treatment_room'], 'nurse', 'nurse', 'sleeve', False,
   ['seated beside the patient, drawing a fine stitch closed with small forceps on the forearm', 'cleaning around the cut with saline and a gauze pad'],
   ['seated with the forearm lying on a paper-covered pad on the trolley, looking away', 'holding very still, the other hand gripping the chair'],
   ['a dressing pack opened on a trolley, small steel forceps, gauze and a pack of sutures', 'a bright examination lamp on an arm'], ['A few bloodstained gauze pads lie in a steel bowl.']),
 'cast': (['a plaster cast being applied to a broken arm'], ['a_e_minors', 'treatment_room'], 'nurse', 'nurse', 'sleeve', False,
   ['wrapping wet white plaster bandage around the patient\'s forearm', 'smoothing the warm plaster with both palms'],
   ['seated with the forearm resting on a pillow, fingers spread', 'sitting very still while the cast sets'],
   ['a bowl of water, rolls of plaster bandage and a roll of soft padding', 'a plaster saw on a shelf'], ['A sling waits on the trolley.']),
 'physio': (['a physiotherapy session, guided exercises after an injury'], ['physiotherapy_gym', 'rehabilitation_gym'], 'physiotherapist', 'physio', 'shirt_off', False,
   ['crouching beside the patient, steadying the patient\'s knee as it bends', 'holding a resistance band while the patient pulls against it'],
   ['lying on a treatment bench lifting one straight leg', 'standing between parallel bars, taking careful steps'],
   ['parallel bars, a set of small weights and resistance bands', 'a large exercise ball and a balance board'], ['Wall bars and mirrors line the room.']),
 'dialysis': (['kidney dialysis, blood running through a machine'], ['dialysis_unit'], 'nurse', 'nurse', 'clothed', False,
   ['checking the lines and the screen on the dialysis machine', 'taping the tubing to the patient\'s forearm'],
   ['reclined in a large padded chair with a blanket over the knees and two tubes running from the forearm', 'reading a book while the machine hums beside the chair'],
   ['a dialysis machine with tubes filled with dark red blood running to a filter', 'a blood pressure cuff on the arm of the chair'], ['A row of identical chairs and machines stretches down the room.']),
 'chemo': (['chemotherapy, a drip feeding medicine into a vein'], ['oncology_day_unit'], 'nurse', 'nurse', 'clothed', False,
   ['hanging a bag of clear fluid on a drip stand and checking the bag against the patient\'s wristband', 'adjusting the speed on an infusion pump'],
   ['reclined in a padded chair with a fine line running to a port on the chest or the back of the hand', 'resting with eyes closed under a soft blanket'],
   ['a drip stand with an infusion pump and a bag of fluid', 'a cup of tea and a magazine on a side table'], ['A large window looks out onto a garden.']),
 'triage': (['triage at an emergency department, a nurse taking first observations'], ['triage_desk', 'a_e_majors'], 'nurse', 'nurse', 'clothed', False,
   ['clipping a pulse oximeter onto the patient\'s finger and noting the number', 'shining a small light into the patient\'s eyes'],
   ['seated on a chair, holding an injured arm close to the body', 'sitting on a trolley edge, pale and leaning forward'],
   ['a pulse oximeter, a tympanic thermometer and a tablet showing a form', 'a wheeled observations stand with a screen'], ['A busy waiting area shows through the open door.']),
 'resus': (['an emergency resuscitation, a team working to restart a heart'], ['resus_bay', 'a_e_majors'], 'emergency doctor', 'specialist', 'gown', False,
   ['standing at the head of the trolley calling out instructions while a colleague does chest compressions', 'holding the defibrillator paddles ready and calling for everyone to stand clear'],
   ['lying flat and unconscious on the trolley, an oxygen mask over the face and sticky pads on the chest'],
   ['a defibrillator on a red crash trolley', 'a bag-valve mask and an oxygen cylinder'], ['A team of four in scrubs surrounds the trolley, one pressing down on the chest with straight arms.']),
 'pre_op': (['a pre-operative assessment, the patient checked before surgery'], ['pre_operative_assessment'], 'nurse', 'nurse', 'clothed', False,
   ['measuring the patient\'s height against a wall chart', 'going through a printed checklist on a clipboard'],
   ['standing barefoot on a weighing scale', 'seated by the desk signing a consent form'],
   ['a weighing scale, a height measure and a clipboard', 'a blood pressure monitor on a stand'], ['A folded hospital gown waits on the chair.']),
 'ward_round': (['a ward round, a consultant reviewing a patient at the bedside with junior doctors'], ['nightingale_ward', 'high_dependency_unit', 'cottage_hospital', 'nineteen_sixties_tower_block_ward'], 'consultant', 'specialist', 'gown', False,
   ['standing at the foot of the bed reading the chart on a clipboard while two junior doctors listen', 'sitting on the edge of a chair at the bedside, talking to the patient'],
   ['sitting up in bed against a stack of pillows, a drip in the back of one hand', 'lying in bed under a white sheet and a pale blue blanket'],
   ['a bedside locker with a jug of water and a drip stand', 'a computer on a wheeled stand'], ['Other beds and curtained bays stretch down the ward.']),
 'iron_lung': (['a 1950s iron lung ward, a nurse tending a patient inside a breathing machine'], ['iron_lung_ward'], 'nurse', 'nurse', 'gown', False,
   ['reaching in through a round porthole in the side of the iron lung to adjust the patient\'s sheet', 'reading a newspaper to the patient'],
   ['lying inside the long metal cylinder with only the head outside, resting on a pillow and looking into an angled mirror above the face'],
   ['a long cream-painted iron lung with round portholes and a pressure gauge'], ['A row of iron lungs lines the ward, their bellows sighing.']),
 'historic_ward': (['an eighteenth-century infirmary, a physician visiting a patient'], ['eighteenth_century_infirmary_ward'], 'physician', 'historic_1700s', 'gown', False,
   ['standing at the bedside holding the patient\'s wrist to count the pulse against a pocket watch', 'examining a glass flask held up to the window light'],
   ['lying in a wooden bed under a coarse woollen blanket', 'propped up on a straw bolster, pale and tired'],
   ['a wooden bedside stool with a pewter cup and a jar of leeches', 'a brass pocket watch on a chain'], ['Long rows of wooden beds stand along whitewashed walls under tall windows.']),
}
EXAM_LABEL_EXTRA = {}

# Surgery: label, rooms, site lines, team actions, equipment, outfit key
SURG = {
 'appendix': (['keyhole surgery to remove the appendix'], ['operating_theater', 'day_surgery_unit'],
   ['the lower right side of the abdomen, a small square of orange-brown iodine-stained skin framed by blue sterile drapes with three thin metal ports in it'],
   ['the surgeon steering long slim instruments through the ports while watching the screen', 'the assistant holding the camera steady'], ['a laparoscopy tower with a large screen showing the inside view, and slim keyhole instruments'], 'surgeon'),
 'gallbladder': (['keyhole gallbladder removal'], ['operating_theater', 'day_surgery_unit'],
   ['the upper abdomen, small ports set into a patch of iodine-stained skin inside a window of blue drapes'],
   ['the surgeon working two long instruments through the ports with eyes on the screen', 'the scrub nurse handing over a clip applicator'], ['a large wall screen showing the inside view and a stack of camera equipment'], 'surgeon'),
 'hip': (['a hip replacement operation'], ['operating_theater'],
   ['the side of the hip, a long window of exposed skin framed in sterile drapes and sticky clear film, the leg wrapped in a sterile stockinette and held by an assistant'],
   ['the surgeon working with a heavy power tool while the team holds the leg', 'the assistant fitting a gleaming metal implant from a sterile tray'], ['trays of steel instruments, a power drill and a set of metal hip implants in sealed packs'], 'surgeon'),
 'knee_scope': (['knee arthroscopy, keyhole surgery inside the knee'], ['day_surgery_unit', 'operating_theater'],
   ['the knee, the leg held in a padded leg holder and wrapped in sterile drapes with only the kneecap area showing'],
   ['the surgeon guiding a slim camera into the side of the knee while watching the screen', 'fluid running through clear tubes'], ['a screen showing the pale inside of the knee joint and bags of clear fluid'], 'surgeon'),
 'heart': (['open heart bypass surgery'], ['operating_theater'],
   ['the chest, fully screened by tall blue drapes so only the team\'s gloved hands and a steel retractor frame show at the centre'],
   ['two surgeons facing each other across the table, heads bowed over the work', 'the perfusionist watching the heart-lung machine'], ['a heart-lung bypass machine with rotating pumps and clear tubing, and a tall stack of monitors'], 'surgeon'),
 'brain': (['brain surgery under an operating microscope'], ['operating_theater'],
   ['the head, held still in a steel pin frame, covered in drapes with a small shaved area showing beneath the microscope'],
   ['the surgeon seated, eyes pressed to the binoculars of a large operating microscope', 'a second surgeon watching on a screen'], ['a large ceiling-hung operating microscope with a long arm and a navigation screen'], 'surgeon'),
 'cataract': (['cataract surgery on the eye'], ['day_surgery_unit'],
   ['one eye, the face covered by a sterile drape with a small clear window over the eye, held open by a fine wire clip'],
   ['the surgeon seated at the head, looking through an operating microscope', 'the nurse holding the patient\'s hand under the drape'], ['an operating microscope on a stand and a small tray of fine instruments'], 'surgeon'),
 'caesarean': (['a caesarean section, the birth of a baby by surgery'], ['operating_theater', 'delivery_room'],
   ['the lower abdomen, hidden from the patient by a raised blue drape screen across the chest'],
   ['the surgeon lifting a newborn baby above the drape screen for the mother to see', 'the midwife waiting with a warmed towel'], ['a neonatal resuscitation cot with a heater overhead'], 'surgeon'),
 'hand': (['hand surgery on a finger tendon'], ['day_surgery_unit'],
   ['the hand, laid out flat on an arm table, the rest of the arm wrapped in drapes with a tight cuff above the elbow'],
   ['two surgeons seated on either side of the arm table wearing magnifying loupes', 'fine stitches being placed with tiny instruments'], ['a narrow arm table and a tray of fine steel instruments'], 'surgeon'),
 'spine': (['spinal surgery with the patient lying face down'], ['operating_theater'],
   ['the lower back, a narrow window of iodine-stained skin in the drapes, the patient lying face down on padded supports'],
   ['the surgeon checking an x-ray image on a C-shaped scanner screen', 'the team working along the length of the back'], ['a large C-shaped mobile x-ray arm and screens showing the spine'], 'surgeon'),
 'robotic': (['robotic surgery, the surgeon controlling a robot from a console'], ['operating_theater'],
   ['the abdomen, covered in drapes with four robotic arms docked over it'],
   ['the surgeon seated at a console across the room, head pressed into the viewer and hands on the controls', 'a bedside assistant standing next to the robot arms'], ['a four-armed surgical robot wrapped in clear plastic covers and a large console'], 'surgeon'),
 'cath': (['a heart catheter procedure, a thin wire passed through the wrist to the heart'], ['catheter_lab'],
   ['the wrist, the arm laid on a board and wrapped in drapes, the patient awake under a sheet'],
   ['the cardiologist feeding a fine wire while watching live x-ray images', 'the team in heavy lead aprons'], ['a large C-arm x-ray scanner over the table and a bank of six screens'], 'radiographer'),
 'dental_surg': (['a wisdom tooth extraction at the dental surgery'], ['dental_surgery'],
   ['the open mouth, the face covered by a green paper drape with a hole for the mouth'],
   ['the dentist bracing the jaw and working with a steel elevator', 'the dental nurse holding the suction tube'], ['a tray of steel forceps and a suction unit'], 'dentist'),
 'skin_surg': (['minor skin surgery to remove a mole'], ['treatment_room', 'outpatient_clinic_room'],
   ['the shoulder, a small marked oval on iodine-stained skin inside a paper drape with a square hole'],
   ['the doctor making a small neat cut while the nurse dabs with gauze', 'the doctor tying a fine stitch'], ['a small sterile pack of instruments and a specimen pot'], 'specialist'),
 'field': (['emergency surgery in a field hospital tent'], ['field_hospital_tent'],
   ['the leg, wrapped in green drapes with a bandaged wound area at the centre'],
   ['two surgeons working by the light of a battery lamp', 'a medic holding a drip bag up by hand'], ['folding steel trays, a portable lamp and a generator cable across the floor'], 'surgeon'),
 'victorian': (['an 1880s surgical operation in an operating theatre lined with tiered seating for students'], ['victorian_operating_room'],
   ['the lower leg, with the rest of the body under white linen sheets and a folded towel laid beside the work'],
   ['the surgeon bending low over the wooden table', 'an assistant holding a cloth over the patient\'s face for ether', 'rows of students watching from the steep wooden gallery'], ['a wooden operating table, a tray of steel instruments with wooden handles and a sawdust box underneath'], 'historic_1800s'),
}
TEAM = ['an anaesthetist seated at the head of the table, watching the monitors and adjusting the breathing machine',
        'a scrub nurse standing at a draped instrument trolley, passing a steel instrument across',
        'a surgical assistant holding a retractor steady with both hands',
        'an operating department practitioner checking a count of gauze swabs on a whiteboard',
        'a circulating nurse opening a sterile pack by touching only its outer edges',
        'a junior doctor watching from behind the surgeon\'s shoulder']

FEMALE = {'breast', 'mammogram', 'pap', 'pelvic'}
PREGNANT = {'pregnancy', 'pregnancy_scan'}
MALE = {'prostate', 'testicular'}
UNGLOVED = {'eye_test', 'hearing', 'shoulder', 'physio', 'pre_op', 'ward_round', 'iron_lung', 'historic_ward', 'spirometry', 'dental'}
AWAKE = {'cataract', 'cath', 'skin_surg', 'hand', 'caesarean', 'dental_surg'}
SURG_FEMALE = {'caesarean'}

def patients(k):
    if k in PREGNANT: return [('med_patient_woman_fertile', 'f')]
    if k in FEMALE: return [('med_patient_woman', 'f')]
    if k in MALE: return [('med_patient_man', 'm')]
    return [('med_patient_woman', 'f'), ('med_patient_man', 'm')]

def build(final, src=None):
    G = {}
    src = src or {}
    W = src.get('f_create_random_woman_short') or _lines(final, 'f_create_random_woman_short')
    M = src.get('m_create_random_man_short') or _lines(final, 'm_create_random_man_short')
    for k, v in OUTFIT.items(): G['med_outfit_%s_f' % k], G['med_outfit_%s_m' % k] = gsplit(v)
    for k, v in DRESS.items(): G['med_patient_dress_%s_f' % k], G['med_patient_dress_%s_m' % k] = gsplit(v)
    cw = [l for l in W if any(a in l for a in CLIN_AGES)]; cm = [l for l in M if any(a in l for a in CLIN_AGES)]
    G['med_patient_woman'] = _recast('patient', W)
    G['med_patient_man'] = _recast('patient', M)
    G['med_patient_woman_fertile'] = _recast('patient', [l for l in W if any(a in l for a in FERTILE)])
    G['med_surgeon_w'] = _recast('lead surgeon', cw); G['med_surgeon_m'] = _recast('lead surgeon', cm)
    G['med_chaperone'] = CHAPERONE; G['med_glove'] = GLOVE
    G['med_light_exam'] = LIGHT_EXAM; G['med_light_theatre'] = LIGHT_THEATRE
    G['med_frame'] = FRAME; G['med_frame_surgery'] = FRAME_SURG; G['med_team_role'] = TEAM
    def room(ids):
        ok = [i for i in ids if os.path.exists(os.path.join(final, 'loc_health_%s_clean.txt' % i))]
        if len(ok) != len(ids): raise KeyError('v109_med: missing rooms %s' % sorted(set(ids) - set(ok)))
        return ['__loc_health_%s_clean__' % i for i in ok]
    exams, cpose, ppose = [], [], []
    for k, (lab, rooms, role, outfit, dress, chap, cp, pp, eq, det) in EXAMS.items():
        b = 'med_exam_%s' % k; rs = role.replace(' ', '_')
        if 'med_person_%s_w' % rs not in G: G['med_person_%s_w' % rs] = _recast(role, cw); G['med_person_%s_m' % rs] = _recast(role, cm)
        G[b + '_label'] = lab; G[b + '_room'] = room(rooms)
        G[b + '_clinician_pose'] = cp; G[b + '_patient_pose'] = pp; G[b + '_equipment'] = eq; G[b + '_detail'] = det
        glove = '' if k in UNGLOVED else ' and __med_glove__'
        ch = ' __med_chaperone__' if chap else ''
        G[b + '_scene'] = [('A medical scene showing __{b}_label__. __{b}_room__ __med_person_{rs}_{cg}__ The {r} wears __med_outfit_{o}_{cg2}__{g}. __{pat}__ The patient wears __med_patient_dress_{d}_{pg}__. '
                            'The {r} is __{b}_clinician_pose__. The patient is __{b}_patient_pose__. Close at hand is __{b}_equipment__. __{b}_detail__{ch} The light is __med_light_exam__. __med_frame__')
                           .format(b=b, rs=rs, r=role, o=outfit, g=glove, pat=pat, d=dress, ch=ch, cg=cg, cg2=cg[0].replace('w', 'f'), pg=pg)
                           for cg in ('w', 'm') for pat, pg in patients(k)]
        exams.append('__%s_scene__' % b); cpose.append('__%s_clinician_pose__' % b); ppose.append('__%s_patient_pose__' % b)
    G['med_exam_any_scene'] = exams
    surg = []
    for k, (lab, rooms, sites, acts, eq, outfit) in SURG.items():
        b = 'med_surgery_%s' % k
        G[b + '_label'] = lab; G[b + '_room'] = room(rooms); G[b + '_site'] = sites; G[b + '_team_action'] = acts; G[b + '_equipment'] = eq
        hist = outfit.startswith('historic')
        light = 'grey daylight falling from a large skylight over the table' if hist else '__med_light_theatre__'
        team = 'Around the table stand two assistants in dark coats with rolled-up sleeves.' if hist else 'Around the table are __med_team_role__, and __med_team_role__.'
        who = 'The patient, a woman,' if k in SURG_FEMALE else 'The patient'
        if k in AWAKE: patient = '%s lies on the table awake under local anaesthetic, covered by drapes except for __%s_site__.' % (who, b)
        elif hist: patient = 'The patient lies unconscious under ether on the table, covered by sheets except for __%s_site__.' % b
        else: patient = '%s lies asleep under general anaesthetic on the operating table, a breathing tube taped at the mouth, covered by sterile drapes except for __%s_site__.' % (who, b)
        G[b + '_scene'] = [('A surgical scene showing __{b}_label__. __{b}_room__ __med_surgeon_{sg}__ The lead surgeon wears __med_outfit_{o}_{sg2}__. {p} {t} The focus of the work is {a}. Close at hand is __{b}_equipment__. The light is {l}. __med_frame_surgery__')
                           .format(b=b, o=outfit, p=patient, t=team, a='__%s_team_action__' % b, l=light, sg=sg, sg2=sg.replace('w', 'f')) for sg in ('w', 'm')]
        surg.append('__%s_scene__' % b)
    G['med_surgery_any_scene'] = surg
    G['med_scene_any'] = exams + surg
    G['med_pose_clinician_any'] = cpose; G['med_pose_patient_any'] = ppose
    return G
