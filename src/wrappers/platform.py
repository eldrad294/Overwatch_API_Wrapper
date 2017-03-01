import json
import urllib
from urllib.request import urlopen
import src.constants as const
from src.modules import achievements as a, platforms as pl, profile as pr, all_heroes as ah
import ssl
#
def get_achievements(tag, platform="pc", region="eu"):
    """ API wrapper method which returns an achievement object """
    #
    try:
        context = ssl._create_unverified_context()
        achievements = json.load(
            const.codec(urlopen(const.URL + platform + "/" + region + "/" + tag + "/achievements", context=context)))
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
        context = ssl._create_unverified_context()
        platforms = json.load(
            const.codec(urlopen(const.URL + platform + "/" + region + "/" + tag + "/get-platforms", context=context)))
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
        context = ssl._create_unverified_context()
        profile = json.load(
            const.codec(urlopen(const.URL + platform + "/" + region + "/" + tag + "/profile", context=context)))
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
        context = ssl._create_unverified_context()
        all_heroes = json.load(
            const.codec(urlopen(const.URL + platform + "/" + region + "/" + tag + "/" + mode + "/allHeroes/", context=context)))
        result = ah.AllHeroes(all_heroes['MeleeFinalBlows'] if 'MeleeFinalBlows' in all_heroes else all_heroes['MeleeFinalBlow'],
                              all_heroes['SoloKills'] if 'SoloKills' in all_heroes else all_heroes['SoloKill'],
                              all_heroes['ObjectiveKills'] if 'ObjectiveKills' in all_heroes else all_heroes['ObjectiveKill'],
                              all_heroes['FinalBlows'] if 'FinalBlows' in all_heroes else all_heroes['FinalBlow'],
                              all_heroes['DamageDone'],
                              all_heroes['Eliminations'] if 'Eliminations' in all_heroes else all_heroes['Elimination'],
                              all_heroes['EnvironmentalKills'] if 'EnvironmentalKills' in all_heroes else all_heroes['EnvironmentalKill'],
                              all_heroes['Multikills'] if 'Multikills' in all_heroes else all_heroes['Multikill'],
                              all_heroes['HealingDone'],
                              all_heroes['Eliminations-MostinGame'] if 'Eliminations-MostinGame' in all_heroes else all_heroes['Elimination-MostinGame'],
                              all_heroes['FinalBlows-MostinGame'] if 'FinalBlows-MostinGame' in all_heroes else all_heroes['FinalBlow-MostinGame'],
                              all_heroes['DamageDone-MostinGame'],
                              all_heroes['HealingDone-MostinGame'],
                              all_heroes['DefensiveAssists-MostinGame'] if 'DefensiveAssists-MostinGame' in all_heroes else (all_heroes['DefensiveAssist-MostinGame'] if 'DefensiveAssist-MostinGame' in all_heroes else None),
                              all_heroes['OffensiveAssists-MostinGame'] if 'OffensiveAssists-MostinGame' in all_heroes else all_heroes['OffensiveAssist-MostinGame'],
                              all_heroes['ObjectiveKills-MostinGame'] if 'ObjectiveKills-MostinGame' in all_heroes else all_heroes['ObjectiveKill-MostinGame'],
                              all_heroes['ObjectiveTime-MostinGame'],
                              all_heroes['Multikill-Best'],
                              all_heroes['SoloKills-MostinGame'] if 'SoloKills-MostinGame' in all_heroes else all_heroes['SoloKill-MostinGame'],
                              all_heroes['TimeSpentonFire-MostinGame'],
                              all_heroes['MeleeFinalBlows-Average'] if 'MeleeFinalBlows-Average' in all_heroes else all_heroes['MeleeFinalBlow-Average'],
                              all_heroes['TimeSpentonFire-Average'],
                              all_heroes['SoloKills-Average'] if 'SoloKills-Average' in all_heroes else all_heroes['SoloKill-Average'],
                              all_heroes['ObjectiveTime-Average'],
                              all_heroes['ObjectiveKills-Average'] if 'ObjectiveKills-Average' in all_heroes else all_heroes['ObjectiveKill-Average'],
                              all_heroes['HealingDone-Average'],
                              all_heroes['FinalBlows-Average'] if 'FinalBlows-Average' in all_heroes else all_heroes['FinalBlow-Average'],
                              all_heroes['Deaths-Average'] if 'Deaths-Average' in all_heroes else all_heroes['Death-Average'],
                              all_heroes['DamageDone-Average'],
                              all_heroes['Eliminations-Average'] if 'Eliminations-Average' in all_heroes else all_heroes['Elimination-Average'],
                              all_heroes['Deaths'] if 'Deaths' in all_heroes else all_heroes['Death'],
                              all_heroes['EnvironmentalDeaths'] if 'EnvironmentalDeaths' in all_heroes else all_heroes['EnvironmentalDeath'],
                              all_heroes['Cards'] if 'Cards' in all_heroes else all_heroes['Card'],
                              all_heroes['Medals'] if 'Medals' in all_heroes else all_heroes['Medal'],
                              all_heroes['Medals-Gold'] if 'Medals-Gold' in all_heroes else all_heroes['Medal-Gold'],
                              all_heroes['Medals-Silver'] if 'Medals-Silver' in all_heroes else all_heroes['Medal-Silver'],
                              all_heroes['Medals-Bronze'] if 'Medals-Bronze' in all_heroes else all_heroes['Medal-Bronze'],
                              all_heroes['GamesPlayed'] if mode == "competitive" else None,
                              all_heroes['GamesWon'] if 'GamesWon' in all_heroes else all_heroes['GameWon'],
                              all_heroes['TimeSpentonFire'],
                              all_heroes['ObjectiveTime'],
                              all_heroes['TimePlayed'],
                              all_heroes['MeleeFinalBlows-MostinGame'] if 'MeleeFinalBlows-MostinGame' in all_heroes else all_heroes['MeleeFinalBlow-MostinGame'],
                              all_heroes['GamesTied'] if mode == "competitive" else None,
                              all_heroes['GamesLost'] if mode == "competitive" else None,
                              all_heroes['DefensiveAssists'] if 'DefensiveAssists' in all_heroes else (all_heroes['DefensiveAssist'] if 'DefensiveAssist' in all_heroes else None),
                              all_heroes['DefensiveAssists-Average'] if 'DefensiveAssists-Average' in all_heroes else None,
                              all_heroes['OffensiveAssists'] if 'OffensiveAssists' in all_heroes else all_heroes['OffensiveAssist'],
                              all_heroes['OffensiveAssists-Average'] if 'OffensiveAssists-Average' in all_heroes else all_heroes['OffensiveAssist-Average'])
        return result
    except urllib.error.URLError as e:
        print("An error occurred when fetching stats\n" + str(e))
        exit(1)
    except Exception as e:
        print("An error occurred:\n " + str(e))
        exit(1)