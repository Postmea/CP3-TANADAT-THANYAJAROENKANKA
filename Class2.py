class Vehicle:
    licenseCode = ""
    serialCode = ""
    color = ""
    def turnOnAirCondition(self):
        print("Turn on : Air")

class Car(Vehicle):
    def turnOnAirCondition(self):
        print("Turn on : Air")
    def sayHello(self):
        print("Hello world")

class Pickup(Vehicle):
    def turnOnAirCondition(self):
        print("Turn on : Air")

Pickup1 = Pickup()
Pickup1.turnOnAirCondition()

Car1 = Car()
Car1.turnOnAirCondition()
Car1.sayHello()