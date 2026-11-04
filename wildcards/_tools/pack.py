"""usage: pack.py N   -> after rel.py N. Builds the four zips named Guyanonymous_Wildcards_vN_{FLAT,FOLDERS,NOTPROPORTIONAL_FLAT,NOTPROPORTIONAL_FOLDER}.zip
 (AOO flat nested in FLAT, AOO folder nested in FOLDERS) and removes the old-style zips for N."""
import sys, os, glob, shutil, subprocess
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import v56_build as B
N = sys.argv[1]; OUT = '/mnt/user-data/outputs'; W = '/home/claude/w'; P = f'Guyanonymous_Wildcards_v{N}'
for z in set(glob.glob(f'{OUT}/Guyanonymous_Wildcards*_v{N}.zip') + glob.glob(f'{OUT}/Guyanonymous_Wildcards_Browse_v{N}.zip') + glob.glob(f'{OUT}/{P}_*.zip')): os.path.exists(z) and os.remove(z)
def zipdir(d, z): subprocess.run(f'cd {d} && zip -qr {z} .', shell=True, check=True)
# AOO
aoo_flat = f'{OUT}/{P}_NOTPROPORTIONAL_FLAT.zip'; zipdir(W + '/all_options_once', aoo_flat)
shutil.rmtree('/tmp/aoo_folders', ignore_errors=True); B.browse(W + '/all_options_once', '/tmp/aoo_folders')
open('/tmp/aoo_folders/README.txt', 'w').write(f"Guyanonymous' Wildcards v{N} - All Options Once (not proportional), folder edition. Every option listed once. References are __family/name__.\n")
aoo_fold = f'{OUT}/{P}_NOTPROPORTIONAL_FOLDER.zip'; zipdir('/tmp/aoo_folders', aoo_fold)
# main flat (docs + nested flat AOO)
shutil.copy(aoo_flat, f'/tmp/pkg14_main/{P}_NOTPROPORTIONAL_FLAT.zip')
for f in glob.glob('/tmp/pkg14_main/Guyanonymous_Wildcards_All_Options_Once_v*.zip'): os.remove(f)
zipdir('/tmp/pkg14_main', f'{OUT}/{P}_FLAT.zip'); os.remove(f'/tmp/pkg14_main/{P}_NOTPROPORTIONAL_FLAT.zip')
# main folders
shutil.rmtree('/tmp/folders_main', ignore_errors=True); B.browse(W + '/wildcards', '/tmp/folders_main/wildcards')
for sub in ('docs',): shutil.copytree('/tmp/pkg14_main/' + sub, '/tmp/folders_main/' + sub)
for f in ('README.txt', 'CHANGELOG.txt'): shutil.copy('/tmp/pkg14_main/' + f, '/tmp/folders_main/' + f)
open('/tmp/folders_main/FOLDER_EDITION.txt', 'w').write(f"Guyanonymous' Wildcards v{N} - folder edition.\nSame files as the flat edition, grouped into family folders. References are written __family/name__ (for example __animals/animal_dogs_prompt__).\nUse this with tools that support folder paths in wildcards. If yours does not, use the _FLAT edition.\n")
shutil.copy(aoo_fold, f'/tmp/folders_main/{P}_NOTPROPORTIONAL_FOLDER.zip')
zipdir('/tmp/folders_main', f'{OUT}/{P}_FOLDERS.zip')
print('packed', N, sorted(os.path.basename(x) for x in glob.glob(f'{OUT}/{P}_*.zip')))
# master zip (no suffix) holding the four edition zips; the loose zips are removed from the outputs folder
parts = sorted(glob.glob(f'{OUT}/{P}_*.zip'))
shutil.rmtree('/tmp/master_pkg', ignore_errors=True); os.makedirs('/tmp/master_pkg')
for z in parts: shutil.move(z, '/tmp/master_pkg/')
open('/tmp/master_pkg/WHICH_ZIP.txt', 'w').write(f"""Guyanonymous' Wildcards v{N} - which zip do I use?
_FLAT                         the full library in one folder. Works in every tool. Start here.
_FOLDERS                      the same library grouped into family folders (references are __family/name__). For tools that support folder paths.
_NOTPROPORTIONAL_FLAT         every option listed once (no weighting), one folder.
_NOTPROPORTIONAL_FOLDER       the same, grouped into family folders.
""")
zipdir('/tmp/master_pkg', f'{OUT}/{P}.zip'); print('master', os.path.getsize(f'{OUT}/{P}.zip'))
