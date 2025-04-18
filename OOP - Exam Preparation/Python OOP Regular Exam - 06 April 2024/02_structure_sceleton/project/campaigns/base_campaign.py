from abc import ABC, abstractmethod


class BaseCampaign(ABC):
    CAMPAIGN_IDS = []
    RATE_INCREMENT = 1  # just example value

    def __init__(self, campaign_id: int, brand: str, budget: float, required_engagement: float):
        self.campaign_id = campaign_id
        self.brand = brand
        self.budget = budget
        self.required_engagement = required_engagement
        self.approved_influencers: list = []

    @property
    def campaign_id(self):
        return self.__campaign_id

    @campaign_id.setter
    def campaign_id(self, value):
        if value <= 0:
            raise ValueError("Campaign ID must be a positive integer greater than zero.")
        elif value in self.CAMPAIGN_IDS:
            raise ValueError(f"Campaign with ID {value} already exists. Campaign IDs must be unique.")
        self.CAMPAIGN_IDS.append(value)
        self.__campaign_id = value

    @abstractmethod
    def enough_eligibility(self, engagement_rate: float):
        pass

    def check_eligibility(self, engagement_rate: float):
        return engagement_rate >= self.required_engagement * self.RATE_INCREMENT
