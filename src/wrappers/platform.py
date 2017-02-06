from urllib.request import urlopen
import urllib
import src.constants as const
import json
from src.modules import achievements as a, platforms as pl, profile as pr
#
def get_achievements(tag, platform, region):
    #
    try:
        achievements = json.load(
            const.codec(urlopen(const.URL + platform + "/" + region + "/" + tag + "/achievements")))
        result = a.Achievements(achievements['totalNumberOfAchievements'],
                                achievements['numberOfAchievementsCompleted'],
                                achievements['finishedAchievements'])
        return result
    except urllib.error.URLError as e:
        print("An error occurred when fetching stats\n" + e)
#
def get_platforms(tag, platform, region):
    #
    platform_list = []
    try:
        platforms = json.load(
            const.codec(urlopen(const.URL + platform + "/" + region + "/" + tag + "/get-platforms")))
        for platform in platforms['profile']:
            result = pl.Platforms(platform['platform'],
                                 platform['region'],
                                 platform['hasAccount'])
            platform_list.append(result)
        return platform_list
    except urllib.error.URLError as e:
        print("An error occurred when fetching stats\n" + e)
#
def get_profile(tag, platform, region):
    #
    try:
        profile = json.load(
            const.codec(urlopen(const.URL + platform + "/" + region + "/" + tag + "/profile")))
        result = pr.Profile(profile['data']['username'],
                            profile['data']['level'],
                            profile['data']['games']['quick']['wins'],
                            profile['data']['games']['competitive']['wins'],
                            profile['data']['games']['competitive']['lost'],
                            profile['data']['playtime']['quick'],
                            profile['data']['playtime']['competitive'],
                            profile['data']['avatar'],
                            profile['data']['competitive']['rank'])
        return result
    except urllib.error.URLError as e:
        print("An error occurred when fetching stats\n" + e)