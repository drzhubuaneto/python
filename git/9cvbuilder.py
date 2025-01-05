class Burger:
    def __init__(self):
        self.bun = None
        self.picle = None
        self.cheese = None
        self.beacon = None
        self.patty=None
        self.sauce = None

    def __str__(self):
        output = "Burger with "
        for key,val in self.__dict__.items():
            output += f"{val}, " if val is not None else ""
        return output
    
class BurgerBuilder:
    def __init__(self):
        self.burger = Burger()

    def add_bun(self, bun):
        self.burger.bun = bun
        return self

    def add_picle(self, picle):
        self.burger.picle = picle
        return self
    
    def add_cheese(self, cheese):
        self.burger.cheese = cheese
        return self
    
    def add_beacon(self, beacon):
        self.burger.beacon = beacon
        return self
    
    def add_patty(self, patty):
        self.burger.patty = patty
        return self
    
    def add_sauce(self, sauce):
        self.burger.sauce = sauce
        return self
    
    def build_burger(self):
        return self.burger
    


if __name__ == "__main__":
    builder = BurgerBuilder()
    mujBurger = builder.add_bun("sesame")\
                       .add_cheese("chedar")\
                       .add_beacon("smoked")\
                       .add_patty("beef")\
                       .add_sauce("ketchup")\
                       .build_burger()
    
    print(mujBurger)

    pass
