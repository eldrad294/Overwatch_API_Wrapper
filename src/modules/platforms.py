from src.contracts.api_contract import APIContract
from utils import html_stripper as hs
#
class Platforms(APIContract):
    #
    def __init__(self, platform, region, hasAccount):
        self.platform = hs.html_stripper(platform)
        self.region = hs.html_stripper(region)
        self.hasAccount = hs.html_stripper(hasAccount)
    #
    def display_api_obj(self):
        print("Platform: ", self.platform,
              "\nRegion: ", self.region,
              "\nHas Account: ", self.hasAccount,
              "\n------------------------------------------")