from src.contracts.api_contract import APIContract
#
class Profile(APIContract):
    #
    def __init__(self, username, level, quick_win_total, competitive_win_total, competitive_loss_total,
                 quick_hours_total, competitive_hours_total, avatar, competitive_rank):
        self.username = username
        self.level = level
        self.quick_win_total = quick_win_total
        self.competitive_win_total = competitive_win_total
        self.competitive_loss_total = competitive_loss_total
        self.quick_hours_total = quick_hours_total
        self.competitive_hours_total = competitive_hours_total
        self.avatar = avatar
        self.competitive_rank = competitive_rank
    #
    def display_api_obj(self):
        print("Username: " + self.username +
              "\nLevel " + self.level +
              "\nTotal hours played: " + self.quick_hours_total + self.competitive_hours_total +
              " (Quick - " + self.quick_hours_total + " / Competitive - " + self.competitive_hours_total + ")" +
              "\nTotal competitive games played: " + self.competitive_win_total + self.competitive_loss_total +
              " (Wins - " + self.competitive_win_total + " / Losses - " + self.competitive_loss_total + ")" +
              "\nCompetitive rank: " + self.competitive_rank +
              "\nTotal wins (quick games): " + self.quick_win_total +
              "\n" + self.avatar)