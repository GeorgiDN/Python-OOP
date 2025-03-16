from project.influencers.base_influencer import BaseInfluencer


class StandardInfluencer(BaseInfluencer):
    PAYMENT_PERCENTAGE = 0.45
    MULTIPLIERS = {"HighBudgetCampaign": 1.2, "LowBudgetCampaign": 0.9}

    def __init__(self, username: str, followers: int, engagement_rate: float):
        super().__init__(username, followers, engagement_rate)

    def reached_followers(self, campaign_type: str):
        return int((self.followers * self.engagement_rate) * self.MULTIPLIERS[campaign_type])
