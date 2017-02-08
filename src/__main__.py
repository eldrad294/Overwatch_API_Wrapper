import src.wrappers.patch_notes as pn, \
       src.wrappers.platform as pl
import sys
from src.constants import *
#
# Param Checks
if len(sys.argv) < 1 and sys.argv[0] is None:
    exit(1)
#
# Receive script params
command = sys.argv[0]
tag = sys.argv[1]
platform = sys.argv[2]
region = sys.argv[3]
mode = sys.argv[4]
#
# Cleaning Params
try:
    command = str.strip(str.lower(command))
    tag = tag.replace("#", "-")
except Exception as e:
    print("Stat retrieval failed. Incorrect command/s.\n" + str(e))
#
# Call API Wrappers
if command in PATCH_NOTES:
    for patch_note in pn.get_patch_notes():
        print(patch_note.display_api_obj())
elif command in ACHIEVEMENTS:
    print(pl.get_achievements(tag, platform, region).display_api_obj())
elif command in PLATFORMS:
    for platform in pl.get_platforms(tag, platform, region):
        print(platform.display_api_obj())
elif command in PROFILES:
    print(pl.get_profile(tag, platform, region).display_api_obj())
elif command in ALL_HEROES_STATS:
    print(pl.get_all_heroes_stats(tag, platform, region, mode).display_api_obj())
else:
    print("Stat retrieval failed. Incorrect command/s")