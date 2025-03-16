from project.influencers.base_influencer import BaseInfluencer
# from project.campaigns.base_campaign import BaseCampaign


class PremiumInfluencer(BaseInfluencer):
    HIGH_BUDGET_CAMPAIGN_MULTIPLIER = 1.5
    LOW_BUDGET_CAMPAIGN_MULTIPLIER = 0.8
    TYPE = "PremiumInfluencer"
    PAYMENT_PERCENT = 0.85

    def __init__(self, username: str, followers: int, engagement_rate: float):
        super().__init__(username, followers, engagement_rate)

    def calculate_payment(self, campaign):
        return campaign.budget * self.PAYMENT_PERCENT



