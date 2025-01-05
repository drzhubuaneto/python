class Vehicle():
    def __init__(self, speed, fuel):
        self._speed = speed
        self._fuel = fuel

    def __str__(self):
        return f"speed is {self._speed} and it needs {self._fuel}"
    
class Car(Vehicle):
    def __init__(self, speed, fuel):
        super().__init__(speed, fuel)

    def __str__(self):
        return "Car " + super().__str__()
    
class Motorcycle(Vehicle):
    def __init__(self, speed, fuel):
        super().__init__(speed, fuel)

    def __str__(self):
        return "Motorcycle " + super().__str__()
    
class Truck(Vehicle):
    def __init__(self, speed, fuel):
        super().__init__(speed, fuel)

    def __str__(self):
        return "Truck " + super().__str__()
    

class VehicleFactory:
    @staticmethod
    def get_vehicle(type, speed, fuel):
        try:
            if type == "car":
                return Car(speed, fuel)
            elif type == "motorcycle":
                return Motorcycle(speed, fuel)
            elif type == "truck":
                return Truck(speed, fuel)
            else:
                raise ValueError(f"Invalid vehicle type: {type}")
        except ValueError as e:
            print(f"Error: {e}")
            

if __name__ == "__main__":        
    car = VehicleFactory.get_vehicle("ca", 150, "petrol")
    motorcycle = VehicleFactory.get_vehicle("motorcycle", 200, "petrol")
    truck = VehicleFactory.get_vehicle("truck", 100, "oil")

    print(car)
    print(motorcycle)
    print(truck)
