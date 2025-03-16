from project.campaigns.high_budget_campaign import HighBudgetCampaign
from project.campaigns.low_budget_campaign import LowBudgetCampaign
from project.influencers.premium_influencer import PremiumInfluencer
from project.influencers.standard_influencer import StandardInfluencer


class InfluencerManagerApp:
    VALID_INFLUENCERS = {"PremiumInfluencer": PremiumInfluencer, "StandardInfluencer": StandardInfluencer}
    VALID_CAMPAIGNS = {"HighBudgetCampaign": HighBudgetCampaign, "LowBudgetCampaign": LowBudgetCampaign}

    def __init__(self):
        self.influencers: list = []
        self.campaigns: list = []

    def register_influencer(self, influencer_type: str, username: str, followers: int, engagement_rate: float):
        if influencer_type not in self.VALID_INFLUENCERS:
            return f"{influencer_type} is not an allowed influencer type."

        influencer = self.get_object_by_username(self.influencers, username)
        if influencer:
            return f"{username} is already registered."

        new_influencer = self.VALID_INFLUENCERS[influencer_type](username, followers, engagement_rate)
        self.influencers.append(new_influencer)
        return f"{username} is successfully registered as a {influencer_type}."

    def create_campaign(self, campaign_type: str, campaign_id: int, brand: str, required_engagement: float):
        if campaign_type not in self.VALID_CAMPAIGNS:
            return f"{campaign_type} is not a valid campaign type."

        campaign = self.get_object_by_id(self.campaigns, campaign_id)
        if campaign:
            return f"Campaign ID {campaign_id} has already been created."

        new_campaign = self.VALID_CAMPAIGNS[campaign_type](campaign_id, brand, required_engagement)
        self.campaigns.append(new_campaign)
        return f"Campaign ID {campaign_id} for {brand} is successfully created as a {campaign_type}."

    def participate_in_campaign(self, influencer_username: str, campaign_id: int):
        influencer = self.get_object_by_username(self.influencers, influencer_username)
        if not influencer:
            return f"Influencer '{influencer_username}' not found."

        campaign = self.get_object_by_id(self.campaigns, campaign_id)
        if not campaign:
            return f"Campaign with ID {campaign_id} not found."

        eligibility = campaign.check_eligibility(influencer.engagement_rate)
        if not eligibility:
            return (f"Influencer '{influencer_username}' does not meet the eligibility criteria "
                    f"for the campaign with ID {campaign_id}.")

        payment = influencer.calculate_payment(campaign)
        if payment > 0:
            campaign.approved_influencers.append(influencer)
            campaign.budget -= payment
            influencer.campaigns_participated.append(campaign)
            return (f"Influencer '{influencer_username}' has successfully participated in the "
                    f"campaign with ID {campaign_id}.")

    def calculate_total_reached_followers(self):
        total_reached_followers = {}
        for influencer in self.influencers:
            for campaign in influencer.campaigns_participated:
                followers = influencer.reached_followers(campaign.__class__.__name__)
                if followers > 0:
                    total_reached_followers[campaign] = followers

        return total_reached_followers


    def influencer_campaign_report(self, username: str):
        influencer = self.get_object_by_username(self.influencers, username)

        if not influencer.campaigns_participated:
            return f"{username} has not participated in any campaigns."

        return influencer.display_campaigns_participated()

    def campaign_statistics(self):
        result = ["$$ Campaign Statistics $$"]
        sorted_campaigns = sorted(self.campaigns, key=lambda c: (len(c.approved_influencers), -c.budget))

        for campaign in sorted_campaigns:
            total_reached_followers = 0
            for influencer in campaign.approved_influencers:
                followers_number = influencer.reached_followers(campaign.__class__.__name__)
                total_reached_followers += followers_number
            result.append(f"  * Brand: {campaign.brand}, "
                          f"Total influencers: {len(campaign.approved_influencers)}, "
                          f"Total budget: ${campaign.budget:.2f}, "
                          f"Total reached followers: {total_reached_followers}")

        return "\n".join(result)


    @staticmethod
    def get_object_by_username(object_list, username):
        found_object = next((obj for obj in object_list if obj.username == username), None)
        return found_object

    @staticmethod
    def get_object_by_id(object_list, id_):
        found_object = next((obj for obj in object_list if obj.campaign_id == id_), None)
        return found_object


# manager = InfluencerManagerApp()
#
# # Register influencers
# print(manager.register_influencer("PremiumInfluencer", "JohnDoe", 50000, 4.2))
# print(manager.register_influencer("StandardInfluencer", "JaneSmith", 10000, 3.5))
# print(manager.register_influencer("PremiumInfluencer", "JohnDoe", 80000, 4.2))
# print(manager.register_influencer("InvalidInfluencer", "JohnDoe", 50000, 4.2))
# print(manager.register_influencer("StandardInfluencer", "AliceJohnson", 20000, 3.8))
# print(manager.register_influencer("PremiumInfluencer", "OliviaBennett", 80000, 4.5))
# print(manager.register_influencer("PremiumInfluencer", "DanielRodriguez", 90000, 4.8))
# print(manager.register_influencer("PremiumInfluencer", "EmilyTurner", 1000000, 5.0))
#
# # Create campaigns
# print(manager.create_campaign("LowBudgetCampaign", 1, "TechGurus", 4.0))
# print(manager.create_campaign("HighBudgetCampaign", 2, "FashionTrendz", 3.0))
# print(manager.create_campaign("LowBudgetCampaign", 1, "FashionTrendz", 3.0))
# print(manager.create_campaign("LowBudgetCampaign", 3, "QuantumFusion", 3.0))
# print(manager.create_campaign("InvalidCampaign", 4, "FoodieDelights", 2.5))
#
# # Participate in campaigns
# print(manager.participate_in_campaign("JohnDoe", 1))
# print(manager.participate_in_campaign("JaneSmith", 2))
# print(manager.participate_in_campaign("AliceJohnson", 2))
# print(manager.participate_in_campaign("AliceJohnson", 1))
# print(manager.participate_in_campaign("NonExistentInfluencer", 1))
# print(manager.participate_in_campaign("AliceJohnson", 3))
# print(manager.participate_in_campaign("JohnDoe", 2))
# print(manager.participate_in_campaign("JaneSmith", 4))
# print(manager.participate_in_campaign("JaneSmith", 1))
# print(manager.participate_in_campaign("OliviaBennett", 3))
# print(manager.participate_in_campaign("DanielRodriguez", 3))
# print(manager.participate_in_campaign("EmilyTurner", 3))
#
# # Print influencer campaign reports and campaign statistics
# print(manager.influencer_campaign_report("JohnDoe"))
# print(manager.influencer_campaign_report("JaneSmith"))
# print(manager.campaign_statistics())

"""
JohnDoe is successfully registered as a PremiumInfluencer.
JaneSmith is successfully registered as a StandardInfluencer.
JohnDoe is already registered.
InvalidInfluencer is not an allowed influencer type.
AliceJohnson is successfully registered as a StandardInfluencer.
OliviaBennett is successfully registered as a PremiumInfluencer.
DanielRodriguez is successfully registered as a PremiumInfluencer.
EmilyTurner is successfully registered as a PremiumInfluencer.
Campaign ID 1 for TechGurus is successfully created as a LowBudgetCampaign.
Campaign ID 2 for FashionTrendz is successfully created as a HighBudgetCampaign.
Campaign ID 1 has already been created.
Campaign ID 3 for QuantumFusion is successfully created as a LowBudgetCampaign.
InvalidCampaign is not a valid campaign type.
Influencer 'JohnDoe' has successfully participated in the campaign with ID 1.
Influencer 'JaneSmith' does not meet the eligibility criteria for the campaign with ID 2.
Influencer 'AliceJohnson' has successfully participated in the campaign with ID 2.
Influencer 'AliceJohnson' has successfully participated in the campaign with ID 1.
Influencer 'NonExistentInfluencer' not found.
Influencer 'AliceJohnson' has successfully participated in the campaign with ID 3.
Influencer 'JohnDoe' has successfully participated in the campaign with ID 2.
Campaign with ID 4 not found.
Influencer 'JaneSmith' does not meet the eligibility criteria for the campaign with ID 1.
Influencer 'OliviaBennett' has successfully participated in the campaign with ID 3.
Influencer 'DanielRodriguez' has successfully participated in the campaign with ID 3.
Influencer 'EmilyTurner' has successfully participated in the campaign with ID 3.
PremiumInfluencer :) JohnDoe :) participated in the following campaigns:
  - Campaign ID: 1, Brand: TechGurus, Reached followers: 168000
  - Campaign ID: 2, Brand: FashionTrendz, Reached followers: 315000
JaneSmith has not participated in any campaigns.
$$ Campaign Statistics $$
  * Brand: FashionTrendz, Total influencers: 2, Total budget: $412.50, Total reached followers: 406200
  * Brand: TechGurus, Total influencers: 2, Total budget: $206.25, Total reached followers: 236400
  * Brand: QuantumFusion, Total influencers: 4, Total budget: $4.64, Total reached followers: 4702000
"""
