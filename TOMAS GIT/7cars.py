# Nazev tridy
class Car():
    # Konstruktor
    def __init__(self, name:str, engine:str, brand:str, price:float, mileage:int):
        # Atributy/parametry tridy
        self.name=name
        self.engine=engine
        self.brand=brand
        self.price=price
        self.mileage=mileage
        # Mohou tu byt i metody
    
    def increase_price(self,value:float) -> None:
        self.price+=value
    
    def decrease_price(self,value:float) -> None:
        self.price-=value

    def make_it_vonavka(self,num:int) -> None:
        self.mileage = int(self.mileage - ((self.mileage/100)*num))
    
    def __str__(self):
        return f"""Car of brand:{self.brand} has model name:{self.name}
total mileage is: {self.mileage}, engine is: {self.engine} and the price is {self.price}"""
        

if __name__=="__main__":
    a0=Car(name="Astra",brand="Oppel",engine="1.6 DTI",price=199000,mileage=160000)
    print(a0.__str__())
    print(a0)
    # print(a0.price)
    # a0.increase_price(50000)
    # print(a0.price)
    # print(a0.mileage)
    # a0.make_it_vonavka(25)
    # print(a0.mileage)
    pass
