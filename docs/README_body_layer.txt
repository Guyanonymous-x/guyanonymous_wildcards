NOTE: file names in this README are the women's base names; in the combined folder they carry an f_ prefix (men: m_). See FILE_NAMING.txt.
BODY-TYPE LAYER v1 (builds on wildcards_age_v1.zip)

PROBLEM: build, composition, bones, shoulders/arms/chest/abs/hips/legs, veins and neck were rolled independently
("heavily overweight" + "chiseled abs" + "gaunt legs"). In my 6,000-prompt test ~59% of body descriptions contained such a clash.

HOW IT WORKS NOW
  age bracket -> body ARCHETYPE (thin, slim, avg, athl, curvy, heavy, musc, frail; shares differ by bracket) -> every body slot comes from that archetype's files.
  Each option is placed on three axes from its wording (fat / muscle / frailty); an archetype is a target region on those axes.
  weight(option) = base x archetype fit x (softened) age factor, so sagging/loose skin, varicose veins, frailty etc. still rise with age inside an archetype.
  Options that say nothing about build (asymmetry, scars, alignment) are kept but at 35% weight. Every original option is present at least once in every file.

FILES (464)
  bt_<archetype>_<y|m|o>_<attribute>   16 attributes x 8 archetypes x 3 age bands (y 18-44, m 45-64, o 65+), 1000 lines each:
        body_build, body_compos, body_bones, body_ratio, body_proprtn, musc_shldr/arms/chest/abs/hips/legs/veins, neck_length/muscle/clav/crease
  bt_<archetype>_age<lo>_<hi>_prompt_char_body   body paragraph templates (3 phrasings) wired to the files above
  age<lo>_<hi>_prompt_char_body    OVERWRITES the age_v1 file: now a picker that chooses the archetype by that bracket's share
  age<lo>_<hi>_prompt_char_face    OVERWRITES the age_v1 file: neck sentence removed (neck now follows body type in the body section)
  See OBSOLETE_FILES.txt for 96 age_v1 files no longer used.

ARCHETYPE SHARES (% of adult women; rough placeholders from BMI patterns - verify): 
  overall  thin 4.6 | slim 15.9 | average 25.4 | athletic 7.1 | curvy 20.6 | heavy 22.2 | muscular 2.0 | frail 2.3
USE: unchanged - __prompt_master_by_age__
body_affinity_audit.csv lists every option's share in every archetype/band file.

REBUILD: python _tools/build_all.py --only body     (run from the wildcards folder; see HOW_TO_RUN.txt)
