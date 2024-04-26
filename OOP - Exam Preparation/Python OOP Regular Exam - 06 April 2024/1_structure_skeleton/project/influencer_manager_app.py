from project.campaigns.high_budget_campaign import HighBudgetCampaign
from project.campaigns.low_budget_campaign import LowBudgetCampaign
from project.influencers.premium_influencer import PremiumInfluencer
from project.influencers.standard_influencer import StandardInfluencer


class InfluencerManagerApp:
    VALID_INFLUENCERS = {"PremiumInfluencer": PremiumInfluencer, "StandardInfluencer": StandardInfluencer}
    VALID_CAMPAIGNS = {"HighBudgetCampaign": HighBudgetCampaign, "LowBudgetCampaign": LowBudgetCampaign}

    def __init__(self):
        self.influencers = []
        self.campaigns = []

    def register_influencer(self, influencer_type: str, username: str, followers: int, engagement_rate: float):
        if influencer_type not in self.VALID_INFLUENCERS:
            return f"{influencer_type} is not an allowed influencer type."

        found_influencer = self._find_influencer_by_username(self.influencers, username)
        if found_influencer:
            return f"{username} is already registered."

        current_influencer = self.VALID_INFLUENCERS[influencer_type](username, followers, engagement_rate)
        self.influencers.append(current_influencer)
        return f"{username} is successfully registered as a {influencer_type}."

    def create_campaign(self, campaign_type: str, campaign_id: int, brand: str, required_engagement: float):
        if campaign_type not in self.VALID_CAMPAIGNS:
            return f"{campaign_type} is not a valid campaign type."

        found_campaign = self._find_campaign_by_id(self.campaigns, campaign_id)
        if found_campaign:
            return f"Campaign ID {campaign_id} has already been created."

        current_campaign = self.VALID_CAMPAIGNS[campaign_type](campaign_id, brand, required_engagement)
        self.campaigns.append(current_campaign)
        return f"Campaign ID {campaign_id} for {brand} is successfully created as a {campaign_type}."

    def participate_in_campaign(self, influencer_username: str, campaign_id: int):
        influencer = self._find_influencer_by_username(self.influencers, influencer_username)
        campaign = self._find_campaign_by_id(self.campaigns, campaign_id)

        if not influencer:
            return f"Influencer '{influencer_username}' not found."

        if not campaign:
            return f"Campaign with ID {campaign_id} not found."

        participation = campaign.check_eligibility(influencer.engagement_rate)
        if participation is False:
            return f"Influencer '{influencer_username}' does not meet the eligibility criteria for the campaign with ID {campaign_id}."

        payment = influencer.calculate_payment(campaign)
        if payment > 0.0:
            campaign.approved_influencers.append(influencer)
            campaign.budget -= payment
            influencer.campaigns_participated.append(campaign)
            return f"Influencer '{influencer_username}' has successfully participated in the campaign with ID {campaign_id}."

    def calculate_total_reached_followers(self):
        campaigns_followers = {}

        for campaign in self.campaigns:
            total_followers = 0
            for influencer in campaign.approved_influencers:
                total_followers += influencer.reached_followers(type(campaign).__name__)
            if total_followers > 0:
                campaigns_followers[campaign] = total_followers

        return campaigns_followers

    # def calculate_total_reached_followers(self):
    #     total_campaigns_followers = {}
    #
    #     for influencer in self.influencers:
    #         for campaign in influencer.campaigns_participated:
    #             reached_followers = influencer.reached_followers(type(campaign).__name__)
    #             total_campaigns_followers[campaign] = total_campaigns_followers.get(campaign, 0) + reached_followers
    #
    #     return total_campaigns_followers

    def influencer_campaign_report(self, username: str):
        influencer = self._find_influencer_by_username(self.influencers, username)
        if influencer:
            return influencer.display_campaigns_participated()

    def campaign_statistics(self):
        sorted_campaigns = sorted(self.campaigns, key=lambda c: (len(c.approved_influencers), -c.budget))

        statistics = " $$ Campaign Statistics $$\n"
        for campaign in sorted_campaigns:
            statistics += f"  * Brand: {campaign.brand}, Total influencers: {len(campaign.approved_influencers)}, Total budget: ${campaign.budget:.2f}, Total reached followers: {self.calculate_total_reached_followers().get(campaign, 0)}\n"

        return statistics.strip()

    ###
    @staticmethod
    def _find_influencer_by_username(lst, name):
        searched_influencer = next((i for i in lst if i.username == name), None)
        return searched_influencer

    @staticmethod
    def _find_campaign_by_id(lst, _id):
        searched_campaign = next((c for c in lst if c.campaign_id == _id), None)
        return searched_campaign
