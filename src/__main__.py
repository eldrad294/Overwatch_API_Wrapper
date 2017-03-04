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
    hero = sys.argv[6] if len(sys.argv) > 6 else None
    #
except IndexError as e:
    print("Invalid Arguments.\n" + str(e))
    exit(1)
#
# Cleaning Params
try:
    command = str.strip(str.lower(command))
    if tag is not None and tag is not ALL:
        tag = tag.replace("#", "-")
except Exception as e:
    print("Stat retrieval failed. Incorrect command/s.\n" + str(e))
    exit(1)
#
# Call API Wrappers
if command in HELP:
    help.get_help()
elif command in PATCH_NOTES:
    if tag is not None and tag in ALL:
        for patchnote in pn.get_patch_notes(platform):
            patchnote.display_api_obj()
    else:
        pn.get_patch_notes(platform)[0].display_api_obj()
elif command in ACHIEVEMENTS:
    pl.get_achievements(tag, platform, region).display_api_obj()
elif command in PLATFORMS:
    for platform in pl.get_platforms(tag, platform, region):
        platform.display_api_obj()
elif command in PROFILES:
    pl.get_profile(tag, platform, region).display_api_obj()
elif hero is None:
    if command in ALL_HEROES_STATS:
        pl.get_all_heroes_stats(tag, platform, region, mode).display_api_obj()
    elif command in GET_MEDALS:
        pl.get_all_heroes_stats(tag, platform, region, mode).get_medals()
    elif command in GET_KILLS:
        pl.get_all_heroes_stats(tag, platform, region, mode).get_kills()
    elif command in GET_TIME:
        pl.get_all_heroes_stats(tag, platform, region, mode).get_time()
    elif command in GET_GAMES:
        pl.get_all_heroes_stats(tag, platform, region, mode).get_games()
    elif command in GET_OBJECTIVES:
        pl.get_all_heroes_stats(tag, platform, region, mode).get_objectives()
elif hero is not None:
    if command in ALL_HEROES_STATS:
        pl.get_heroes_stats(tag, hero, platform, region, mode).display_api_obj()
    elif command in GET_MEDALS:
        pl.get_heroes_stats(tag, hero, platform, region, mode).get_medals()
    elif command in GET_KILLS:
        pl.get_heroes_stats(tag, hero, platform, region, mode).get_kills()
    elif command in GET_TIME:
        pl.get_heroes_stats(tag, hero, platform, region, mode).get_time()
    elif command in GET_GAMES:
        pl.get_heroes_stats(tag, hero, platform, region, mode).get_games()
    elif command in GET_OBJECTIVES:
        pl.get_heroes_stats(tag, hero, platform, region, mode).get_objectives()
else:
    print("Stat retrieval failed. Incorrect command/s")
    exit(1)