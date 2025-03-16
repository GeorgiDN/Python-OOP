from project.influencers.base_influencer import BaseInfluencer


class PremiumInfluencer(BaseInfluencer):
    PAYMENT_PERCENTAGE = 0.85
    MULTIPLIERS = {"HighBudgetCampaign": 1.5, "LowBudgetCampaign": 0.8}

    def __init__(self, username: str, followers: int, engagement_rate: float):
        super().__init__(username, followers, engagement_rate)

    def reached_followers(self, campaign_type: str):
        return int((self.followers * self.engagement_rate) * self.MULTIPLIERS[campaign_type])
