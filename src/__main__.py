import sys
sys.path.append("..")
from src.constants import *
import src.wrappers.patch_notes as pn
import src.wrappers.platform as pl
from src.utils import help
#
# Param Checks
try:
    #
    # Receive script params
    command = sys.argv[1]
    tag = sys.argv[2] if len(sys.argv) > 2 else None
    platform = sys.argv[3] if len(sys.argv) > 3 else 'pc'
    region = sys.argv[4] if len(sys.argv) > 4 else 'eu'
    mode = sys.argv[5] if len(sys.argv) > 5 else 'quickplay'
except IndexError as e:
    print("Invalid Arguments.\n" + str(e))
    exit(1)
#
# Cleaning Params
try:
    command = str.strip(str.lower(command))
    if tag is not None and tag is not LATEST:
        tag = tag.replace("#", "-")
except Exception as e:
    print("Stat retrieval failed. Incorrect command/s.\n" + str(e))
    exit(1)
#
# Call API Wrappers
if command in HELP:
    help.get_help()
elif command in PATCH_NOTES:
    if tag is not None and tag in LATEST:
        pn.get_patch_notes()[0].display_api_obj()
    else:
        for patchnote in pn.get_patch_notes():
            patchnote.display_api_obj()
elif command in ACHIEVEMENTS:
    pl.get_achievements(tag, platform, region).display_api_obj()
elif command in PLATFORMS:
    for platform in pl.get_platforms(tag, platform, region):
        platform.display_api_obj()
elif command in PROFILES:
    pl.get_profile(tag, platform, region).display_api_obj()
elif command in ALL_HEROES_STATS:
    pl.get_all_heroes_stats(tag, platform, region, mode).display_api_obj()
else:
    print("Stat retrieval failed. Incorrect command/s")
    exit(1)