class Car:
    def move(self):
        print("The car is moving faster")

class Bike:
    def move(self):
        print("The bike is moving slowly")

def moving(vehicle):
    vehicle.move()

car = Car()
bike = Bike()

moving(car)
moving(bike)
