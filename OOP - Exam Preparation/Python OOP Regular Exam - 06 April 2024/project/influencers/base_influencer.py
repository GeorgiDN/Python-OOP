from abc import ABC, abstractmethod

# from project.campaigns.base_campaign import BaseCampaign
# from project.campaigns.high_budget_campaign import HighBudgetCampaign
# from project.campaigns.low_budget_campaign import LowBudgetCampaign


class BaseInfluencer(ABC):
    HIGH_BUDGET_CAMPAIGN_MULTIPLIER = 2  # just for test
    LOW_BUDGET_CAMPAIGN_MULTIPLIER = 1
    TYPE = "BaseInfluencer"
    PAYMENT_PERCENT = 1.0

    def __init__(self, username: str, followers: int, engagement_rate: float):
        self.username = username
        self.followers = followers
        self.engagement_rate = engagement_rate
        self.campaigns_participated: list = []

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, value):
        if not value.strip():
            raise ValueError("Username cannot be empty or consist only of whitespace!")
        self.__username = value

    @property
    def followers(self):
        return self.__followers

    @followers.setter
    def followers(self, value):
        if value < 0:
            raise ValueError("Followers must be a non-negative integer!")
        self.__followers = value

    @property
    def engagement_rate(self):
        return self.__engagement_rate

    @engagement_rate.setter
    def engagement_rate(self, value):
        if value < 0.0 or value > 5.0:
            raise ValueError("Engagement rate should be between 0 and 5.")
        self.__engagement_rate = value

    @abstractmethod
    def calculate_payment(self, campaign):
        pass

    def reached_followers(self, campaign_type: str):
        if campaign_type == "HighBudgetCampaign":
            result = (self.followers * self.engagement_rate) * self.HIGH_BUDGET_CAMPAIGN_MULTIPLIER
        elif campaign_type == "LowBudgetCampaign":
            result = (self.followers * self.engagement_rate) * self.LOW_BUDGET_CAMPAIGN_MULTIPLIER
        return int(result)

    def display_campaigns_participated(self):
        if not self.campaigns_participated:
            return f"{self.username} has not participated in any campaigns."

        result = f"{self.TYPE} :) {self.username} :) participated in the following campaigns:\n"
        for campaign in self.campaigns_participated:
            result += f"  - Campaign ID: {campaign.campaign_id}, Brand: {campaign.brand}, Reached followers: {self.reached_followers(campaign.TYPE)}\n"
        return result.strip()


    # def display_campaigns_participated(self):
    #     if not self.campaigns_participated:
    #         return f"{self.username} has not participated in any campaigns."
    #
    #     campaign_info = []
    #     for campaign in self.campaigns_participated:
    #         reached_followers = self.reached_followers(campaign.__class__.__name__)
    #         campaign_info.append(
    #             f"  - Campaign ID: {campaign.campaign_id}, Brand: {campaign.brand}, Reached followers: {reached_followers}")
    #
    #    return f"{self.__class__.__name__} :) {self.username} :) participated in the following campaigns:\n" + '\n'.join(campaign_info)
