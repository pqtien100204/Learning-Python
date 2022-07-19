class Vehicle():
    def __init__(self, bodystyle):
        self.bodystyle = bodystyle

    def drive(self, speed):
        self.mode = "driving"
        self.speed = speed
    
class Car(Vehicle):
    def __init__(self, enginetype):
        super().__init__("Car")
        self.doors = 4
        self.wheels = 4
        self.enginetype = enginetype
    
    def drive(self, speed):
        super().drive(speed)
        print("Driving my", self.enginetype, "car at speed", self.speed)


class Motorcycle(Vehicle):
    def __init__(self, enginetype, hassidecar):
        super().__init__("Motorcycle")
        if (hassidecar):
            self.wheels = 3
        else:
            self.wheels = 2
        self.doors = 0
        self.enginetype = enginetype

    def drive(self, speed):
        super().drive(speed)
        print("Driving my", self.enginetype, "motorcycle at speed", self.speed)

car1 = Car("gas")
car2 = Car("electronic")
motoc = Motorcycle("gas", True)

print(motoc.wheels)
print(car1.doors)
print(car2.enginetype)

car1.drive(30)
car2.drive(40)
motoc.drive(50)