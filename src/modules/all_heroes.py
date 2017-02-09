from src.contracts.api_contract import APIContract
#
class AllHeroes(APIContract):
    #
    def __init__(self, melee_final_blows, solo_kills, objective_kills, final_blows, damage_done, eliminations,
                 environmental_kills, multikills, healing_done, eliminations_mig, final_blows_mig, damage_done_mig,
                 healing_done_mig, defensive_assists_mig, offensive_assists_mig, objective_kills_mig,
                 objective_time_mig, multi_kill_best, solo_kills_mig, time_spent_on_fire_mig, melee_final_blows_avg,
                 time_spent_on_fire_avg, solo_kills_avg, objective_time_avg, objective_kills_avg, healing_done_avg,
                 final_blows_avg, deaths_avg, damage_done_avg, eliminations_avg, deaths, environmental_deaths,  cards,
                 medals, medals_gold, medals_silver, medals_bronze, games_played, games_won, time_spent_on_fire,
                 objective_time, time_played, melee_final_blow_mig, games_tied, games_lost, defensive_assists,
                 defensive_assists_avg, offensive_assists, offensive_assists_avg):
        self.melee_final_blows = melee_final_blows
        self.solo_kills = solo_kills
        self.objective_kills = objective_kills
        self.final_blows = final_blows
        self.damage_done = damage_done
        self.eliminations = eliminations
        self.environmental_kills = environmental_kills
        self.multikills = multikills
        self.healing_done = healing_done
        self.eliminations_mig = eliminations_mig
        self.final_blows_mig = final_blows_mig
        self.damage_done_mig = damage_done_mig
        self.healing_done_mig = healing_done_mig
        self.defensive_assists_mig = defensive_assists_mig
        self.offensive_assists_mig = offensive_assists_mig
        self.objective_kills_mig = objective_kills_mig
        self.objective_time_mig = objective_time_mig
        self.multi_kill_best = multi_kill_best
        self.solo_kills_mig = solo_kills_mig
        self.time_spent_on_fire_mig = time_spent_on_fire_mig
        self.melee_final_blows_avg = melee_final_blows_avg
        self.time_spent_on_fire_avg = time_spent_on_fire_avg
        self.solo_kills_avg = solo_kills_avg
        self.objective_time_avg = objective_time_avg
        self.objective_kills_avg = objective_kills_avg
        self.healing_done_avg = healing_done_avg
        self.final_blows_avg = final_blows_avg
        self.deaths_avg = deaths_avg
        self.damage_done_avg = damage_done_avg
        self.eliminations_avg = eliminations_avg
        self.deaths = deaths
        self.environmental_deaths = environmental_deaths
        self.cards = cards
        self.medals = medals
        self.medals_gold = medals_gold
        self.medals_silver = medals_silver
        self.medals_bronze = medals_bronze
        self.games_played = games_played
        self.games_won = games_won
        self.time_spent_on_fire = time_spent_on_fire
        self.objective_time = objective_time
        self.time_played = time_played
        self.melee_final_blow_mig = melee_final_blow_mig
        self.games_tied = games_tied
        self.games_lost = games_lost
        self.defensive_assists = defensive_assists
        self.defensive_assists_avg = defensive_assists_avg
        self.offensive_assists = offensive_assists
        self.offensive_assists_avg = offensive_assists_avg
#
    def display_api_obj(self):
        print("Melee Final Blows: ", self.melee_final_blows,
              "\nSolo Kills: ", self.solo_kills,
              "\nObjective Kills: ", self.objective_kills,
              "\nFinal Blows: ", self.final_blows,
              "\nDamage Done: ", self.damage_done,
              "\nEliminations: ", self.eliminations,
              "\nEnvironmental Kills: ", self.environmental_kills,
              "\nMulti Kills: ", self.multikills,
              "\nHealing Done: ", self.healing_done,
              "\nEliminations (MIG): ", self.eliminations_mig,
              "\nFinal Blows (MIG): ", self.final_blows_mig,
              "\nDamage Done (MIG): ", self.damage_done_mig,
              "\nHealing Done (MIG): ", self.healing_done_mig,
              "\nDefensive Assists (MIG): ", self.defensive_assists_mig,
              "\nOffensive Assists (MIG): ", self.offensive_assists_mig,
              "\nObjective Kills (MIG): ", self.objective_kills_mig,
              "\nObjective Time (MIG): ", self.objective_time_mig,
              "\nMulti Kill Best: ", self.multi_kill_best,
              "\nSolo Kills Best: ", self.solo_kills_mig,
              "\nTime Spent On Fire: ", self.time_spent_on_fire,
              "\nMelee Final Blows Average: ", self.melee_final_blows_avg,
              "\nTime Spent On Fire Average: ", self.time_spent_on_fire_avg,
              "\nSolo Kills Average: ", self.solo_kills_avg,
              "\nObjective Time Average: ", self.objective_time_avg,
              "\nObjective Kills Average: ", self.objective_kills_avg,
              "\nHealing Done Average: ", self.healing_done_avg,
              "\nFinal Blows Average: ", self.final_blows_avg,
              "\nDeaths Average: ", self.deaths_avg,
              "\nDamage Done Average: ", self.damage_done_avg,
              "\nEliminations Average: ", self.eliminations_avg,
              "\nDeaths: ", self.deaths,
              "\nEnvironmental Deaths: ",self.environmental_deaths,
              "\nCards: ", self.cards,
              "\nMedals: ", self.medals,
              "\nGold Medals: ", self.medals_gold,
              "\nSilver Medals: ", self.medals_silver,
              "\nBronze Medals: ", self.medals_bronze,
              "\nGames Played: ", self.games_played,
              "\nGames Won: ", self.games_won,
              "\nTime Spent On Fire: ", self.time_spent_on_fire,
              "\nObjective Time: ", self.objective_time,
              "\nTime Played: ", self.time_played,
              "\nMelee  Final Blow(MIG): ", self.melee_final_blow_mig,
              "\nGames Tied: ", self.games_tied,
              "\nGames Lost: ", self.games_lost,
              "\nDefensive Assists: ", self.defensive_assists,
              "\nDefensive Assists Average: ", self.defensive_assists_avg,
              "\nOffensive Assists: ", self.offensive_assists,
              "\nOffensive Assists Average", self.offensive_assists_avg,
              "\n------------------------------------------")