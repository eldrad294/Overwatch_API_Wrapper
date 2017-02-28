from src.contracts.api_contract import APIContract
from src.utils import html_stripper as hs
#
class Profile(APIContract):
    #
    def __init__(self, username, level, quick_win_total, competitive_win_total, competitive_loss_total,
                 quick_hours_total, competitive_hours_total, avatar, competitive_rank):
        self.username = hs.html_stripper(username)
        self.level = hs.html_stripper(level)
        self.quick_win_total = hs.html_stripper(quick_win_total)
        self.competitive_win_total = hs.html_stripper(competitive_win_total)
        self.competitive_loss_total = hs.html_stripper(competitive_loss_total)
        self.quick_hours_total = hs.html_stripper(quick_hours_total)
        self.competitive_hours_total = hs.html_stripper(competitive_hours_total)
        self.avatar = hs.html_stripper(avatar)
        self.competitive_rank = hs.html_stripper(competitive_rank)
    #
    def display_api_obj(self):
        print("Username: ", self.username,
              "\nLevel ", self.level,
              "\nTotal hours (Quick): ", self.quick_hours_total,
              "\nTotal hours (Competitive): ", self.competitive_hours_total,
              "\nTotal competitive games played: ", (int(self.competitive_win_total) + int(self.competitive_loss_total)),
              " (Wins - ", self.competitive_win_total, " / Losses - ", self.competitive_loss_total, ")",
              "\nCompetitive rank: ", self.competitive_rank,
              "\nTotal wins (quick games): ", self.quick_win_total,
              "\n", self.avatar,
              "\n------------------------------------------")