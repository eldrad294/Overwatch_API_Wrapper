from src.contracts.api_contract import APIContract
#
class Platforms(APIContract):
    #
    def __init__(self, platform, region, hasAccount):
        self.platform = platform
        self.region = region
        self.hasAccount = hasAccount
    #
    def display_api_obj(self):
        print("Platform: " + self.platform +
              "Region: " + self.region +
              "Has Account: " + self.hasAccount)