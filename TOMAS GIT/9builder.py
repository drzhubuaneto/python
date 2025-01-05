class Burger:
    def __init__(self):
        self.bun=None
        self.pickle=None
        self.cheese=None
        self.bacon=None
        self.patty=None
        self.sauce=None
    
    def __str__(self):
        output="Burger with, "
        for key,val in self.__dict__.items():
            output+=f"{val}, " if val is not None else ""
        return output

class BurgerBuilder:
    def __init__(self):
        self.burger=Burger()

    def add_bun(self,bun:str):
        self.burger.bun=bun
        return self
    
    def add_pickle(self,pickle:str):
        self.burger.pickle=pickle
        return self
    def add_cheese(self,cheese:str):
        self.burger.cheese=cheese
        return self
    def add_bacon(self,bacon:str):
        self.burger.bacon=bacon
        return self
    def add_patty(self,patty:str):
        self.burger.patty=patty
        return self
    def add_sauce(self,sauce:str):
        self.burger.sauce=sauce
        return self
    
    def build_burger(self):
        return self.burger

if __name__=="__main__":
    builder=BurgerBuilder()
    mujburger=builder.add_bun("Classic bun")\
                     .add_bacon("Extra portion of bacon")\
                     .add_cheese("One slice of cheddar cheese")\
                     .add_patty("Double patty")\
                     .add_sauce("classic Mayo")\
                     .build_burger()
    print(mujburger) 
