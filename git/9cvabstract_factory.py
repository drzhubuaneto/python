from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def make_sound(self):
        pass

class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)

    def make_sound(self):
        return f"Pejsek jmeno {self.name} dela: haf"

class Cat(Animal):
    def __init__(self, name):
        super().__init__(name)

    def make_sound(self):
        return f"Kocicka jmeno {self.name} dela: mnau"
    
class AnimalFactory(ABC):
    @abstractmethod
    def create_dog(self, name:str = None) -> Animal:
        pass

    @abstractmethod
    def create_cat(self, name:str = None) -> Animal:
        pass

class KladnoAnimalFactory(AnimalFactory):
    def create_dog(self, name:str = None) -> Animal:
        return Dog(name = f"Kladensky {name}")

    def create_cat(self, name:str = None) -> Animal:
        return Cat(name = f"Kladenska {name}")
 
class ChebAnimalFactory(AnimalFactory):
    def create_dog(self, name:str = None) -> Animal:
        return Dog(name = f"Chebsky {name}")

    def create_cat(self, name:str = None) -> Animal:
        return Cat(name = f"Chebska {name}")       

class BigAnimalFactory:
    @staticmethod
    def get_factory(city:str, type) -> AnimalFactory:
        if city == "Kladno":
            if type == "dog":
                return KladnoAnimalFactory().create_dog()
            elif type == "cat":
                return KladnoAnimalFactory().create_cat()
        elif city == "Cheb":
            if type == "dog":
                return ChebAnimalFactory().create_dog()
            elif type == "cat":
                return ChebAnimalFactory().create_cat()
        else:
            raise Exception("Takovou tovarnu nezname")

if __name__ == "__main__":
    # Kladenska zviraza
    kladynko_factory = KladnoAnimalFactory()
    kl_dog = kladynko_factory.create_dog("Rex")
    kl_cat = kladynko_factory.create_cat("Micka")

    print(kl_dog.make_sound())
    print(kl_cat.make_sound())

    # Chebska zviraza
    pass
