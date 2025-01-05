class Vehicle:
    def __init__(self, brand:str, name:str):
        self.brand=brand
        self.name=name

    def print_vehicle_info(self)->None:
        return f"Vehicle of brand:{self.brand} and model name:{self.name}"

class Car(Vehicle):
    def __init__(self,brand:str,name:str,color:str,engine:str):
        super().__init__(brand=brand,name=name)
        self.color=color
        self.engine=engine
    
    def print_vehicle_info(self) -> None:
        return super().print_vehicle_info()+f" of color:{self.color} and engine:{self.engine}"
    
class Bicycle(Vehicle):
    def __init__(self,brand:str,name:str,color:str):
        super().__init__(brand=brand,name=name)
        self.color=color

if __name__=="__main__":
    c0=Car("Oppel","Astra","black","1.7 DTI")
    # print(c0.print_vehicle_info())
    b0=Bicycle("KTM","Rychly","green")
    # print(b0.print_vehicle_info())
    l_vehicles=[c0,b0]
    for vehicle in l_vehicles:
        print(vehicle.print_vehicle_info())
