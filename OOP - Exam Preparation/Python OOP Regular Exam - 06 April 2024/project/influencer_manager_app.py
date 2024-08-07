from project.influencers.premium_influencer import PremiumInfluencer
from project.influencers.standard_influencer import StandardInfluencer
from project.campaigns.high_budget_campaign import HighBudgetCampaign
from project.campaigns.low_budget_campaign import LowBudgetCampaign


class InfluencerManagerApp:
    VALID_INFLUENCERS = {"PremiumInfluencer": PremiumInfluencer, "StandardInfluencer": StandardInfluencer}
    VALID_CAMPAIGNS = {"HighBudgetCampaign": HighBudgetCampaign, "LowBudgetCampaign": LowBudgetCampaign}

    def __init__(self):
        self.influencers: list = []
        self.campaigns: list = []

    def register_influencer(self, influencer_type: str, username: str, followers: int, engagement_rate: float):
        if influencer_type not in self.VALID_INFLUENCERS:
            return f"{influencer_type} is not an allowed influencer type."

        influencer = self._get_infuencer_by_username(self.influencers, username)
        if influencer in self.influencers:
            return f"{username} is already registered."

        new_influencer = self.VALID_INFLUENCERS[influencer_type](username, followers, engagement_rate)
        self.influencers.append(new_influencer)
        return f"{username} is successfully registered as a {influencer_type}."

    def create_campaign(self, campaign_type: str, campaign_id: int, brand: str, required_engagement: float):
        if campaign_type not in self.VALID_CAMPAIGNS:
            return f"{campaign_type} is not a valid campaign type."

        campaign = self._get_campaign_by_id(self.campaigns, campaign_id)
        if campaign in self.campaigns:
            return f"Campaign ID {campaign_id} has already been created."

        new_campaign = self.VALID_CAMPAIGNS[campaign_type](campaign_id, brand, required_engagement)
        self.campaigns.append(new_campaign)
        return f"Campaign ID {campaign_id} for {brand} is successfully created as a {campaign_type}."

    def participate_in_campaign(self, influencer_username: str, campaign_id: int):
        influencer = self._get_infuencer_by_username(self.influencers, influencer_username)
        campaign = self._get_campaign_by_id(self.campaigns, campaign_id)

        if influencer is None:
            return f"Influencer '{influencer_username}' not found."

        if campaign is None:
            return f"Campaign with ID {campaign_id} not found."

        eligible = campaign.enough_eligibility(influencer.engagement_rate)
        if not eligible:
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
                total_followers += influencer.reached_followers(campaign.TYPE)
            if total_followers > 0:
                campaigns_followers[campaign] = total_followers

        return campaigns_followers

    # def calculate_total_reached_followers(self):
    #     reached_followers = {}
    #     for campaign in self.campaigns:
    #         total_followers = sum(
    #             inf.reached_followers(type(campaign).__name__) for inf in campaign.approved_influencers)
    #         if total_followers > 0:
    #             reached_followers[campaign] = total_followers
    #     return reached_followers

    def influencer_campaign_report(self, username: str):
        influencer = self._get_infuencer_by_username(self.influencers, username)
        if influencer:
            return influencer.display_campaigns_participated()

    def campaign_statistics(self):
        sorted_campaigns = sorted(self.campaigns, key=lambda c: (len(c.approved_influencers), -c.budget))

        statistics = " $$ Campaign Statistics $$\n"
        for campaign in sorted_campaigns:
            statistics += (f"  * Brand: {campaign.brand}, Total influencers: {len(campaign.approved_influencers)}, "
                           f"Total budget: ${campaign.budget:.2f}, "
                           f"Total reached followers: {self.calculate_total_reached_followers().get(campaign, 0)}\n")

        return statistics.strip()

    # # Helper methods
    @staticmethod
    def _get_infuencer_by_username(influencers_list, username):
        found_influencer = next((i for i in influencers_list if i.username == username), None)
        return found_influencer

    @staticmethod
    def _get_campaign_by_id(campaigns_list, camp_id):
        found_campaign = next((c for c in campaigns_list if c.campaign_id == camp_id), None)
        return found_campaign

