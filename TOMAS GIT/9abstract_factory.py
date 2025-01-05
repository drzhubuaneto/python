from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self,name):
        self.name=name

    @abstractmethod
    def make_sound(self):
        pass

class Dog(Animal):
    def __init__(self,name:str):
        super().__init__(name)
    
    def make_sound(self):
        return f"Pejsek jmenem:{self.name} dela: Haf!"

class Cat(Animal):
    def __init__(self,name:str):
        super().__init__(name)
    
    def make_sound(self):
        return f"Kocka jmenem:{self.name} dela: Mnau!"

class AnimalFactory(ABC):
    @abstractmethod
    def create_dog(self,name:str) -> Animal:
        pass
    @abstractmethod
    def create_cat(self,name:str) -> Animal:
        pass

class KladnoAnimalFactory(AnimalFactory):
    def create_dog(self, name: str) -> Animal:
        return Dog(name=f"Kladenskej {name}")
    
    def create_cat(self, name: str) -> Animal:
        return Cat(name=f"Kladenska {name}")

class ChebAnimalFactory(AnimalFactory):
    def create_dog(self, name: str) -> Animal:
        return Dog(name=f"Chebskej {name}")
    
    def create_cat(self, name: str) -> Animal:
        return Cat(name=f"Chebska {name}")

class BigAnimalFactory:
    @staticmethod
    def get_animal(type:str,city:str,name:str):
        if city.lower()=="kladno":
            if type.lower()=="dog":
                return KladnoAnimalFactory.create_dog(name)
            elif type.lower()=="cat":
                return KladnoAnimalFactory.create_cat(name)
            else:
                raise Exception("This animal on Kladno city cannot be created")
        elif city.lower()=="cheb" and type.lower()=="dog":
            return ChebAnimalFactory.create_dog(name)
        elif city.lower()=="cheb" and type.lower()=="cat":
            return ChebAnimalFactory.create_cat(name)
        else:
            raise Exception(f"This animal cannot be create in city:{city}")

if __name__=="__main__":
    # Kladenska zvirata
    kladynko_factory=KladnoAnimalFactory()
    kl_dog=kladynko_factory.create_dog("Vestaj")
    kl_cat=kladynko_factory.create_cat("Smeska")
    print(kl_dog.make_sound())
    print(kl_cat.make_sound())

    # Obdobne pro chebske

    # Pro BigAnimalFactory
    # d_kl=BigAnimalFactory.get_animal(type="dog",city="Kladno",name="Azor")
    # print(d_kl.make_sound())
    # TODO: need fix
