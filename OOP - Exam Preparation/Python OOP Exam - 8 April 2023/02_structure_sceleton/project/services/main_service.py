from project.services.base_service import BaseService
# from project.robots.male_robot import MaleRobot


class MainService(BaseService):
    TYPE = 'MainService'
    TYPE_SERVICE = "Main"
    CAPACITY = 30

    def __init__(self, name: str):
        super().__init__(name, capacity=self.CAPACITY)

    def take_details(self):
        return self.details()


# TEST
# robot1 = MaleRobot("robot1", "kind1", 200.0)
# robot2 = MaleRobot("robot2", "kind2", 300.0)


# main_service = MainService("ServiceTechnicalsWorld")
# main_service.robots.append(robot1)
# main_service.robots.append(robot2)

# print(main_service.details())


