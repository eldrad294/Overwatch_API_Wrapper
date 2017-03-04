import json
import urllib
from urllib.request import urlopen
import src.constants as const
from src.modules import achievements as a, platforms as pl, profile as pr, all_heroes as ah, hero as h
import ssl
import src.utils.dictionary_checker as dc
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
        result = ah.AllHeroes(dc.get_dic_obj(all_heroes, "MeleeFinalBlows", "MeleeFinalBlow"),
                              dc.get_dic_obj(all_heroes, "SoloKills", "SoloKill"),
                              dc.get_dic_obj(all_heroes, "ObjectiveKills", "ObjectiveKill"),
                              dc.get_dic_obj(all_heroes, "FinalBlows", "FinalBlow"),
                              dc.get_dic_obj(all_heroes, "DamageDone"),
                              dc.get_dic_obj(all_heroes, "Eliminations", "Elimination"),
                              dc.get_dic_obj(all_heroes, "EnvironmentalKills", "EnvironmentalKill"),
                              dc.get_dic_obj(all_heroes, "Multikills", "Multikill"),
                              dc.get_dic_obj(all_heroes, "HealingDone"),
                              dc.get_dic_obj(all_heroes, "Eliminations-MostinGame", "Elimination-MostinGame"),
                              dc.get_dic_obj(all_heroes, "FinalBlows-MostinGame", "FinalBlow-MostinGame"),
                              dc.get_dic_obj(all_heroes, "DamageDone-MostinGame"),
                              dc.get_dic_obj(all_heroes, "HealingDone-MostinGame"),
                              dc.get_dic_obj(all_heroes, "DefensiveAssists-MostinGame", "DefensiveAssist-MostinGame"),
                              dc.get_dic_obj(all_heroes, "OffensiveAssists-MostinGame", "OffensiveAssist-MostinGame"),
                              dc.get_dic_obj(all_heroes, "ObjectiveKills-MostinGame", "ObjectiveKill-MostinGame"),
                              dc.get_dic_obj(all_heroes, "ObjectiveTime-MostinGame"),
                              dc.get_dic_obj(all_heroes, "Multikill-Best"),
                              dc.get_dic_obj(all_heroes, "SoloKills-MostinGame", "SoloKill-MostinGame"),
                              dc.get_dic_obj(all_heroes, "TimeSpentonFire-MostinGame"),
                              dc.get_dic_obj(all_heroes, "MeleeFinalBlows-Average", "MeleeFinalBlow-Average"),
                              dc.get_dic_obj(all_heroes, "TimeSpentonFire-Average"),
                              dc.get_dic_obj(all_heroes, "SoloKills-Average", "SoloKill-Average"),
                              dc.get_dic_obj(all_heroes, "ObjectiveTime-Average"),
                              dc.get_dic_obj(all_heroes, "ObjectiveKills-Average", "ObjectiveKill-Average"),
                              dc.get_dic_obj(all_heroes, "HealingDone-Average"),
                              dc.get_dic_obj(all_heroes, "FinalBlows-Average", "FinalBlow-Average"),
                              dc.get_dic_obj(all_heroes, "Deaths-Average", "Death-Average"),
                              dc.get_dic_obj(all_heroes, "DamageDone-Average"),
                              dc.get_dic_obj(all_heroes, "Eliminations-Average", "Elimination-Average"),
                              dc.get_dic_obj(all_heroes, "Deaths", "Death"),
                              dc.get_dic_obj(all_heroes, "EnvironmentalDeaths", "EnvironmentalDeath"),
                              dc.get_dic_obj(all_heroes, "Cards", "Card"),
                              dc.get_dic_obj(all_heroes, "Medals", "Medal"),
                              dc.get_dic_obj(all_heroes, "Medals-Gold", "Medal-Gold"),
                              dc.get_dic_obj(all_heroes, "Medals-Silver", "Medal-Silver"),
                              dc.get_dic_obj(all_heroes, "Medals-Bronze", "Medal-Bronze"),
                              dc.get_dic_obj(all_heroes, "GamesPlayed", "GamePlayed"),
                              dc.get_dic_obj(all_heroes, "GamesWon", "GameWon"),
                              dc.get_dic_obj(all_heroes, "TimeSpentonFire"),
                              dc.get_dic_obj(all_heroes, "ObjectiveTime"),
                              dc.get_dic_obj(all_heroes, "TimePlayed"),
                              dc.get_dic_obj(all_heroes, "MeleeFinalBlows-MostinGame", "MeleeFinalBlow-MostinGame"),
                              dc.get_dic_obj(all_heroes, "GamesTied", "GameTied") if mode == "competitive" else None,
                              dc.get_dic_obj(all_heroes, "GamesLost", "GameLost") if mode == "competitive" else None,
                              dc.get_dic_obj(all_heroes, "DefensiveAssists", "DefensiveAssist"),
                              dc.get_dic_obj(all_heroes, "DefensiveAssists-Average", "DefensiveAssist-Average"),
                              dc.get_dic_obj(all_heroes, "OffensiveAssists", "OffensiveAssist"),
                              dc.get_dic_obj(all_heroes, "OffensiveAssists-Average", "OffensiveAssist-Average")
                              )
        return result
    except urllib.error.URLError as e:
        print("An error occurred when fetching stats\n" + str(e))
        exit(1)
    except Exception as e:
        print("An error occurred:\n " + str(e))
        exit(1)
#
def get_heroes_stats(tag, hero, platform="pc", region="eu", mode="quickplay"):
    """ API Wrapper object which returns stats for a specific hero """
    try:
        context = ssl._create_unverified_context()
        hero_stats = json.load(
            const.codec(
                urlopen(const.URL + platform + "/" + region + "/" + tag + "/" + mode + "/hero/" + hero + "/", context=context)))
        result = h.Hero(
            dc.get_dic_obj(hero_stats, "Eliminations", "Elimination"),
            dc.get_dic_obj(hero_stats, "FinalBlows", "FinalBlow"),
            dc.get_dic_obj(hero_stats, "SoloKills", "SoloKill"),
            dc.get_dic_obj(hero_stats, "ShotsFired", "ShotFired"),
            dc.get_dic_obj(hero_stats, "ShotsHit", "ShotHit"),
            dc.get_dic_obj(hero_stats, "CriticalHits", "CriticalHit"),
            dc.get_dic_obj(hero_stats, "DamageDone"),
            dc.get_dic_obj(hero_stats, "ObjectiveKills", "ObjectiveKills"),
            dc.get_dic_obj(hero_stats, "Multikill", "Multikills"),
            dc.get_dic_obj(hero_stats, "CriticalHitsperMinute", "CriticalHitperMinute"),
            dc.get_dic_obj(hero_stats, "CriticalHitAccuracy"),
            dc.get_dic_obj(hero_stats, "EliminationsperLife", "EliminationperLife"),
            dc.get_dic_obj(hero_stats, "WeaponAccuracy"),
            dc.get_dic_obj(hero_stats, "TeleporterPadsDestroyed", "TeleporterPadDestroyed"),
            dc.get_dic_obj(hero_stats, "TurretsDestroyed", "TurretDestroyed"),
            dc.get_dic_obj(hero_stats, "SelfHealing"),
            dc.get_dic_obj(hero_stats, "Eliminations-MostinLife", "Elimination-MostinLife"),
            dc.get_dic_obj(hero_stats, "DamageDone-MostinLife"),
            dc.get_dic_obj(hero_stats, "WeaponAccuracy-BestinGame"),
            dc.get_dic_obj(hero_stats, "KillStreak-Best"),
            dc.get_dic_obj(hero_stats, "DamageDone-MostinGame"),
            dc.get_dic_obj(hero_stats, "Eliminations-MostinGame", "Elimination-MostinGame"),
            dc.get_dic_obj(hero_stats, "FinalBlows-MostinGame", "FinalBlow-MostinGame"),
            dc.get_dic_obj(hero_stats, "ObjectiveKills-MostinGame", "ObjectiveKill-MostinGame"),
            dc.get_dic_obj(hero_stats, "ObjectiveTime-MostinGame"),
            dc.get_dic_obj(hero_stats, "SoloKills-MostinGame", "SoloKill-MostinGame"),
            dc.get_dic_obj(hero_stats, "CriticalHits-MostinGame", "CriticalHit-MostinGame"),
            dc.get_dic_obj(hero_stats, "CriticalHits-MostinLife", "CrtiticalHit-MostinLife"),
            dc.get_dic_obj(hero_stats, "SelfHealing-Average"),
            dc.get_dic_obj(hero_stats, "Deaths-Average", "Death-Average"),
            dc.get_dic_obj(hero_stats, "SoloKills-Average", "SoloKill-Average"),
            dc.get_dic_obj(hero_stats, "ObjectiveTime-Average"),
            dc.get_dic_obj(hero_stats, "ObjectiveKills-Average", "ObjectiveKill-Average"),
            dc.get_dic_obj(hero_stats, "FinalBlows-Average", "FinalBlow-Average"),
            dc.get_dic_obj(hero_stats, "Eliminations-Average", "Elimination-Average"),
            dc.get_dic_obj(hero_stats, "DamageDone-Average"),
            dc.get_dic_obj(hero_stats, "Deaths", "Death"),
            dc.get_dic_obj(hero_stats, "EnvironmentalDeaths", "EnvironmentalDeath"),
            dc.get_dic_obj(hero_stats, "Medals-Bronze", "Medal-Bronze"),
            dc.get_dic_obj(hero_stats, "Medals-Silver", "Medal-Silver"),
            dc.get_dic_obj(hero_stats, "Medals-Gold", "Medal-Gold"),
            dc.get_dic_obj(hero_stats, "Medals", "Medal"),
            dc.get_dic_obj(hero_stats, "Cards", "Card"),
            dc.get_dic_obj(hero_stats, "TimePlayed"),
            dc.get_dic_obj(hero_stats, "GamesWon", "GameWon"),
            dc.get_dic_obj(hero_stats, "ObjectiveTime"),
            dc.get_dic_obj(hero_stats, "TimeSpentOnFire"),
            dc.get_dic_obj(hero_stats, "Multikill-Best"),
        )
        return result
    except urllib.error.URLError as e:
        print("An error occurred when fetching stats\n" + str(e))
        exit(1)
    except Exception as e:
        print("An error occurred:\n " + str(e))
        exit(1)