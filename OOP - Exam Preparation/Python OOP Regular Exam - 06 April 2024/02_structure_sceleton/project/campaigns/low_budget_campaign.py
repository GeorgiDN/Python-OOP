from project.campaigns.base_campaign import BaseCampaign


class LowBudgetCampaign(BaseCampaign):
    CAMPAIGN_IDS = []
    RATE_INCREMENT = 0.9
    BUDGET = 2500.0
    TYPE = "LowBudgetCampaign"

    def __init__(self, campaign_id: int, brand: str, required_engagement: float):
        super().__init__(campaign_id, brand, self.BUDGET, required_engagement)

    def enough_eligibility(self, engagement_rate: float):
        return self.check_eligibility(engagement_rate)
