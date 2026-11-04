"""v68 - patch release: fixes found while building the v57-v67 gallery (condition parts that did not fit every subject, sessile sea animals, world place wording)."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from paths import FINAL
def build(final=FINAL):
    return {'v68_entry_points': ['condition_prompt', 'ani2_prompt', 'world_place_prompt']}
def run(final):
    import v61_build, v62_build, v66_build
    from famlib import run_mod
    v61_build.run(final); v62_build.run(final); v66_build.run(final)
    return run_mod(sys.modules[__name__], final)
def export_aoo(out):
    import v61_build, v62_build, v66_build
    v61_build.export_aoo(out); v62_build.export_aoo(out); v66_build.export_aoo(out)
    return 0
if __name__ == '__main__': run(FINAL)
