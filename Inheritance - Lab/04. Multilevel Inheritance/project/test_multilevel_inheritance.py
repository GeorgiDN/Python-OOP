from project.vehicle import Vehicle
from project.car import Car
from project.sports_car import SportsCar

vehicle = Vehicle()
print(vehicle.move())

car = Car()
print(car.drive())
print(car.move())

sportscar = SportsCar()
print(sportscar.race())
print(sportscar.move())
print(sportscar.drive())
