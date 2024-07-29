from project.influencers.base_influencer import BaseInfluencer


class StandardInfluencer(BaseInfluencer):
    def __init__(self, username: str, followers: int, engagement_rate: float):
        super().__init__(username, followers, engagement_rate)

    def calculate_payment(self, campaign):
        return campaign.budget * 0.45

    def reached_followers(self, campaign_type: str):
        if campaign_type == "HighBudgetCampaign":
            res = (self.followers * self.engagement_rate) * 1.2
        elif campaign_type == "LowBudgetCampaign":
            res = (self.followers * self.engagement_rate) * 0.9
        return int(res)
