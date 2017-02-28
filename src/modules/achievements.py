from src.contracts.api_contract import APIContract
from src.utils import html_stripper as hs
#
class Achievements(APIContract):
    #
    def __init__(self, total_number_of_achievements, number_of_achievements, finished_achievements):
        self.total_number_of_achievements = hs.html_stripper(total_number_of_achievements)
        self.number_of_achievements = hs.html_stripper(number_of_achievements)
        self.finished_achievements = hs.html_stripper(finished_achievements)
    #
    def display_api_obj(self):
        print("Total number of achievments: ", self.total_number_of_achievements,
              "\nNumber of achievements: ", self.total_number_of_achievements,
              "\nFinished achievements: ", self.finished_achievements,
              "\n------------------------------------------")