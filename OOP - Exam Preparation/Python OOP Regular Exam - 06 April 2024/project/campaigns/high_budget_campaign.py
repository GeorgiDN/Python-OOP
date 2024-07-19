from project.campaigns.base_campaign import BaseCampaign


class HighBudgetCampaign(BaseCampaign):
    CAMPAIGN_IDS = []
    RATE_INCREMENT = 1.2
    BUDGET = 5000.0
    TYPE = "HighBudgetCampaign"

    def __init__(self, campaign_id: int, brand: str, required_engagement: float):
        super().__init__(campaign_id, brand, self.BUDGET, required_engagement)

    def enough_eligibility(self, engagement_rate: float):
        return self.check_eligibility(engagement_rate)
