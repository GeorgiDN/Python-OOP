from abc import ABC, abstractmethod


class BaseClient(ABC):
    VALID_MEMBERSHIP_TYPES = ["Regular", "VIP"]
    TOTAL_POINTS = 0

    def __init__(self, name: str, membership_type: str):
        self.name = name
        self.membership_type = membership_type
        self.points: int = self.TOTAL_POINTS

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value.strip():
            raise ValueError("Client name should be determined!")
        self.__name = value
        
    @property
    def membership_type(self):
        return self.__membership_type
    
    @membership_type.setter
    def membership_type(self, value):
        if value not in self.VALID_MEMBERSHIP_TYPES:
            raise ValueError("Invalid membership type. Allowed types: Regular, VIP.")
        self.__membership_type = value

    @abstractmethod
    def earning_points(self, order_amount: float):
        pass

    def apply_discount(self):
        discount_points = 0
        discount_percentage = 0
        if self.points >= 100:
            discount_points = 100
            discount_percentage = 10
        elif 50 <= self.points < 100:
            discount_points = 50
            discount_percentage = 5
        self.points -= discount_points
        return (discount_percentage, self.points)


# client = BaseClient("gosho", "VIP")
# client.points = 100
# print(client.earning_points(20.2))
# print(client.points)