from project import Vehicle
from project import Car
from project import SportsCar

vehicle = Vehicle()
print(vehicle.move())

car = Car()
print(car.drive())
print(car.move())

sportscar = SportsCar()
print(sportscar.race())
print(sportscar.move())
print(sportscar.drive())
