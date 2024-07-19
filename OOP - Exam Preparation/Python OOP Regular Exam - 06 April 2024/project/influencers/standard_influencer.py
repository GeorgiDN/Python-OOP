# from project.campaigns.high_budget_campaign import HighBudgetCampaign
from project.influencers.base_influencer import BaseInfluencer
# from project.campaigns.base_campaign import BaseCampaign


class StandardInfluencer(BaseInfluencer):
    HIGH_BUDGET_CAMPAIGN_MULTIPLIER = 1.2
    LOW_BUDGET_CAMPAIGN_MULTIPLIER = 0.9
    TYPE = "StandardInfluencer"
    PAYMENT_PERCENT = 0.45

    def __init__(self, username: str, followers: int, engagement_rate: float):
        super().__init__(username, followers, engagement_rate)

    def calculate_payment(self, campaign):
        return campaign.budget * self.PAYMENT_PERCENT

