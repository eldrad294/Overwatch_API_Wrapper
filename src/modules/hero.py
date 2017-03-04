from src.contracts.api_contract import APIContract
from src.contracts.hero_contract import HeroContract
#
class Hero(APIContract, HeroContract):
    #
    def __init__(self, eliminations, final_blows, solo_kills, shots_fired, shots_hit, critical_hits, damage_done,
                 objective_kills, multi_kill, critical_hits_per_minute, critical_hits_accuracy, eliminations_per_life,
                 weapon_accuracy, teleporter_pad_destroyed, turrets_destroyed, self_healing, eliminations_mil,
                 damage_done_mil, weapon_accuracy_big, kill_streak_best, damage_done_mig, eliminations_mig,
                 final_blows_mig, objective_kills_mig, objective_time_mig, solo_kills_mig, critical_hits_mig,
                 critical_hits_mil, self_healing_mig, self_healing_avg, deaths_avg, solo_kills_avg, objective_time_avg,
                 objective_kills_avg, final_blows_avg, eliminations_avg, damage_done_avg, deaths, environmental_deaths,
                 medals_bronze, medals_silver, medals_gold, medals, card, time_played, games_won, objective_time,
                 time_spent_on_fire, multi_kill_best):
        self.eliminations = eliminations
        self.final_blows = final_blows
        self.solo_kills = solo_kills
        self.shots_fired = shots_fired
        self.shots_hit = shots_hit
        self.critical_hits = critical_hits
        self.damage_done = damage_done
        self.objective_kills = objective_kills
        self.multi_kill = multi_kill
        self.critical_hits_per_minute = critical_hits_per_minute
        self.critical_hits_accuracy = critical_hits_accuracy
        self.eliminations_per_life = eliminations_per_life
        self.weapon_accuracy = weapon_accuracy
        self.teleporter_pad_destroyed = teleporter_pad_destroyed
        self.turrets_destroyed = turrets_destroyed
        self.self_healing = self_healing
        self.eliminations_mil = eliminations_mil
        self.eliminations_per_life = eliminations_per_life
        self.damage_done_mil = damage_done_mil
        self.weapon_accuracy_big = weapon_accuracy_big
        self.kill_streak_best = kill_streak_best
        self.damage_done_mig = damage_done_mig
        self.eliminations_mig = eliminations_mig
        self.final_blows_mig = final_blows_mig
        self.objective_kills_mig = objective_kills_mig
        self.objective_time_mig = objective_time_mig
        self.solo_kills_mig = solo_kills_mig
        self.critical_hits_mig = critical_hits_mig
        self.critical_hits_mil = critical_hits_mil
        self.self_healing_mig = self_healing_mig
        self.self_healing_avg = self_healing_avg
        self.deaths_avg = deaths_avg
        self.solo_kills_avg = solo_kills_avg
        self.objective_time_avg = objective_time_avg
        self.objective_kills_avg = objective_kills_avg
        self.final_blows_avg = final_blows_avg
        self.eliminations_avg = eliminations_avg
        self.damage_done_avg = damage_done_avg
        self.deaths = deaths
        self.environmental_deaths = environmental_deaths
        self.medals_bronze = medals_bronze
        self.medals_silver = medals_silver
        self.medals_gold = medals_gold
        self.medals = medals
        self.card = card
        self.time_played = time_played
        self.games_won = games_won
        self.objective_time = objective_time
        self.time_spent_on_fire = time_spent_on_fire
        self.multi_kill_best = multi_kill_best
    #
    def display_api_obj(self):
        print("Eliminations: ", self.eliminations,
              "\nFinal Blows: ", self.final_blows,
              "\nSolo Kills: ", self.solo_kills,
              "\nShots Fired: ", self.shots_fired,
              "\nShots Hit: ", self.shots_hit,
              "\nCritical Hits: ", self.critical_hits,
              "\nDamage Done: ", self.damage_done,
              "\nObjective Kills: ", self.objective_kills,
              "\nMulti Kill: ", self.multi_kill,
              "\nCritical Hits Per Minute: ", self.critical_hits_per_minute,
              "\nCritical Hits Accuracy: ", self.critical_hits_accuracy,
              "\nEliminations Per Life: ", self.eliminations_per_life,
              "\nWeapon Accuracy: ", self.weapon_accuracy,
              "\nTeleporter Pad Destroyed: ", self.teleporter_pad_destroyed,
              "\nTurrets Destroyed: ", self.turrets_destroyed,
              "\nSelf Healing: ", self.self_healing,
              "\nEliminations (Most In Game): ", self.eliminations_mil,
              "\nEliminations Per Life: ", self.eliminations_per_life,
              "\nDamage Done (Most In Game): ", self.damage_done_mil,
              "\nEliminations (Most In Game): ", self.eliminations_mig,
              "\nFinal Blows (Most In Game): ", self.final_blows_mig,
              "\nObjective Kills (Most In Game): ", self.objective_kills_mig,
              "\nObjective Time (Most In Game): " ,self.objective_time,
              "\nSolo Kills (Most In Game): ", self.solo_kills_mig,
              "\nCritical Hits (Most In Game): ", self.critical_hits_mig,
              "\nCritical Hits (Most In Life): ", self.critical_hits_mil,
              "\nSelf Healing (Most In Game): ", self.self_healing_mig,
              "\nSelf Healing (Average): " ,self.self_healing_avg,
              "\nDeaths (Average): ", self.deaths_avg,
              "\nSolo Kills (Average): ", self.solo_kills_avg,
              "\nObjective Time (Average): ", self.objective_time_avg,
              "\nObjective Kills (Average): ", self.objective_kills_avg,
              "\nFinal Blows (Average): ", self.final_blows_avg,
              "\nEliminations (Average): ", self.eliminations_avg,
              "\nDamage Done (Average): ", self.damage_done_avg,
              "\nDeaths: ", self.deaths,
              "\nEnvironmental Deaths: ", self.environmental_deaths,
              "\nMedals Bronze: ", self.medals_bronze,
              "\nMedals Silver: ", self.medals_silver,
              "\nMedals Gold: ", self.medals_gold,
              "\nMedals: ", self.medals,
              "\nCard: ", self.card,
              "\nTime Played: ", self.time_played,
              "\nGames Won: ", self.games_won,
              "\nObjective Time: ", self.objective_time,
              "\nTime Spent On Fire: ", self.time_spent_on_fire,
              "\nMulti Kill Best: ", self.multi_kill_best,
              "\n------------------------------------------")
    #
    def get_medals(self):
        print("Medals: ", self.medals,
              "\nGold Medals: ", self.medals_gold,
              "\nSilver Medals: ", self.medals_silver,
              "\nBronze Medals: ", self.medals_bronze,
              "\n------------------------------------------")
    #
    def get_kills(self):
        print("Objective Kills: ", self.objective_kills,
              "\nSolo Kills: ", self.solo_kills,
              "\nSolo Kills Best: ", self.solo_kills_mig,
              "\nMulti Kill Best: ", self.multi_kill_best,
              "\nFinal Blows: ", self.final_blows,
              "\nEliminations: ", self.eliminations,
              "\nDeaths: ", self.deaths,
              "\n------------------------------------------")
    #
    def get_time(self):
        print("Time Spent On Fire: ", self.time_spent_on_fire,
              "\nObjective Time: ", self.objective_time,
              "\nTime Played: ", self.time_played,
              "\n------------------------------------------")
    #
    def get_games(self):
        print("Games Won: ", self.games_won,
              "\n------------------------------------------")
    #
    def get_objectives(self):
        print("Objective Kills: ", self.objective_kills,
              "\nObjective Kills (MIG): ", self.objective_kills_mig,
              "\nObjective Kills Average: ", self.objective_kills_avg,
              "\nObjective Time (MIG): ", self.objective_time_mig,
              "\nObjective Time Average: ", self.objective_time_avg,
              "\nObjective Time: ", self.objective_time,
              "\n------------------------------------------")
