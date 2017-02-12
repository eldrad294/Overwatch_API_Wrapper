import json
import urllib
from urllib.request import urlopen
import src.constants as const
from src.modules import achievements as a, platforms as pl, profile as pr, all_heroes as ah
#
def get_achievements(tag, platform="pc", region="eu"):
    """ API wrapper method which returns an achievement object """
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
        exit(1)
    except Exception as e:
        print("An error occurred:\n " + str(e))
        exit(1)
#
def get_platforms(tag, platform="pc", region="eu"):
    """ API wrapper method which returns a platform object """
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
        exit(1)
    except Exception as e:
        print("An error occurred:\n " + str(e))
        exit(1)
#
def get_profile(tag, platform="pc", region="eu"):
    """ API wrapper method which returns a profile object """
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
        exit(1)
    except Exception as e:
        print("An error occurred:\n " + str(e))
        exit(1)
#
def get_all_heroes_stats(tag, platform="pc", region="eu", mode="quickplay"):
    """ API wrapper method which  returns an all_heroes object """
    #
    try:
        all_heroes = json.load(
            const.codec(urlopen(const.URL + platform + "/" + region + "/" + tag + "/" + mode + "/allHeroes/")))
        result = ah.AllHeroes(all_heroes['MeleeFinalBlows'],
                              all_heroes['SoloKills'],
                              all_heroes['ObjectiveKills'],
                              all_heroes['FinalBlows'],
                              all_heroes['DamageDone'],
                              all_heroes['Eliminations'],
                              all_heroes['EnvironmentalKills'],
                              all_heroes['Multikills'],
                              all_heroes['HealingDone'],
                              all_heroes['Eliminations-MostinGame'],
                              all_heroes['FinalBlows-MostinGame'],
                              all_heroes['DamageDone-MostinGame'],
                              all_heroes['HealingDone-MostinGame'],
                              all_heroes['DefensiveAssists-MostinGame'],
                              all_heroes['OffensiveAssists-MostinGame'],
                              all_heroes['ObjectiveKills-MostinGame'],
                              all_heroes['ObjectiveTime-MostinGame'],
                              all_heroes['Multikill-Best'],
                              all_heroes['SoloKills-MostinGame'],
                              all_heroes['TimeSpentonFire-MostinGame'],
                              all_heroes['MeleeFinalBlows-Average'],
                              all_heroes['TimeSpentonFire-Average'],
                              all_heroes['SoloKills-Average'],
                              all_heroes['ObjectiveTime-Average'],
                              all_heroes['ObjectiveKills-Average'],
                              all_heroes['HealingDone-Average'],
                              all_heroes['FinalBlows-Average'],
                              all_heroes['Deaths-Average'],
                              all_heroes['DamageDone-Average'],
                              all_heroes['Eliminations-Average'],
                              all_heroes['Deaths'],
                              all_heroes['EnvironmentalDeaths'],
                              all_heroes['Cards'],
                              all_heroes['Medals'],
                              all_heroes['Medals-Gold'],
                              all_heroes['Medals-Silver'],
                              all_heroes['Medals-Bronze'],
                              all_heroes['GamesPlayed'] if mode == "competitive" else None,
                              all_heroes['GamesWon'],
                              all_heroes['TimeSpentonFire'],
                              all_heroes['ObjectiveTime'],
                              all_heroes['TimePlayed'],
                              all_heroes['MeleeFinalBlow-MostinGame'],
                              all_heroes['GamesTied'] if mode == "competitive" else None,
                              all_heroes['GamesLost'] if mode == "competitive" else None,
                              all_heroes['DefensiveAssists'],
                              all_heroes['DefensiveAssists-Average'],
                              all_heroes['OffensiveAssists'],
                              all_heroes['OffensiveAssists-Average'])
        return result
    except urllib.error.URLError as e:
        print("An error occurred when fetching stats\n" + str(e))
        exit(1)
    except Exception as e:
        print("An error occurred:\n " + str(e))
        exit(1)