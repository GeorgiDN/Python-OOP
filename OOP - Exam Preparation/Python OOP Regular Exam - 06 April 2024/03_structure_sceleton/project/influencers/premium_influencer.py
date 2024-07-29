from project.influencers.base_influencer import BaseInfluencer


class PremiumInfluencer(BaseInfluencer):
    def __init__(self, username: str, followers: int, engagement_rate: float):
        super().__init__(username, followers, engagement_rate)

    def calculate_payment(self, campaign):
        return campaign.budget * 0.85

    def reached_followers(self, campaign_type: str):
        if campaign_type == "HighBudgetCampaign":
            res = (self.followers * self.engagement_rate) * 1.5
        elif campaign_type == "LowBudgetCampaign":
            res = (self.followers * self.engagement_rate) * 0.8
        return int(res)



# h = HighBudgetCampaign(1, "TechGurus", 10)
#
# p = PremiumInfluencer("JohnDoe", 2, 5)
# p.campaigns_participated.append(h)
# print(p.display_campaigns_participated())
# # print(p.calculate_payment(h))
