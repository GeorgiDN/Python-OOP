from typing import List
from project.customer import Customer
from project.trainer import Trainer
from project.equipment import Equipment
from project.exercise_plan import ExercisePlan
from project.subscription import Subscription


class Gym:
    def __init__(self):
        self.customers: List[Customer] = []
        self.trainers: List[Trainer] = []
        self.equipment: List[Equipment] = []
        self.plans: List[ExercisePlan] = []
        self.subscriptions: List[Subscription] = []

    def add_customer(self, customer: Customer):
        if customer not in self.customers:
            self.customers.append(customer)

    def add_trainer(self, trainer: Trainer):
        if trainer not in self.trainers:
            self.trainers.append(trainer)

    def add_equipment(self, equipment: Equipment):
        if equipment not in self.equipment:
            self.equipment.append(equipment)

    def add_plan(self, plan: ExercisePlan):
        if plan not in self.plans:
            self.plans.append(plan)

    def add_subscription(self, subscription: Subscription):
        if subscription not in self.subscriptions:
            self.subscriptions.append(subscription)

    def subscription_info(self, subscription_id: int):
        current_customer = self._find_object_by_id(self.customers, subscription_id)
        current_subscription = self._find_object_by_id(self.subscriptions, subscription_id)
        current_trainer = self._find_object_by_id(self.trainers, subscription_id)
        current_equipment = self._find_object_by_id(self.equipment, subscription_id)
        current_plan = self._find_object_by_id(self.plans, subscription_id)

        return (f"{str(current_subscription)}\n"
                f"{str(current_customer)}\n"
                f"{str(current_trainer)}\n"
                f"{str(current_equipment)}\n"
                f"{str(current_plan)}")

    @staticmethod
    def _find_object_by_id(lst, id_number):
        found_object = next((obj for obj in lst if obj.id == id_number), None)
        return found_object





