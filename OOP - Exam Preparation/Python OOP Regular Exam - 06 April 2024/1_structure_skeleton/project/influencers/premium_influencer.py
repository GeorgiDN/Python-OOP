from project.campaigns.base_campaign import BaseCampaign
from project.influencers.base_influencer import BaseInfluencer


class PremiumInfluencer(BaseInfluencer):
    PAYMENT_PERCENT = 0.85

    def __init__(self, username: str, followers: int, engagement_rate: float):
        super().__init__(username, followers, engagement_rate)

    def calculate_payment(self, campaign: BaseCampaign):
        calculated_payment = campaign.budget * self.PAYMENT_PERCENT
        return calculated_payment

    def reached_followers(self, campaign_type: str):
        if campaign_type == "HighBudgetCampaign":
            reached_followers = int(self.followers * self.engagement_rate * 1.5)
        elif campaign_type == "LowBudgetCampaign":
            reached_followers = int(self.followers * self.engagement_rate * 0.8)
        return reached_followers
