from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass

    @classmethod
    def create_animal(cls,name):
        return cls(name)
    
    @staticmethod
    def is_good_fo_reels(animal):
        return animal in ["bobr","kocka","pes"]

class Dog(Animal):
    def __init__(self,name:str):
        self.name=name
    
    def make_sound(self):
        return "Haf"

class Cat(Animal):
    def __init__(self,name:str):
        self.name=name
    
    def make_sound(self):
        return "Mnau"

if __name__=="__main__":
    d=Dog("Alik")
    print(d.make_sound())
    # Test Class methody
    d0=Dog.create_animal("Maxik")
    c0=Cat.create_animal("Macek")
    print(c0.make_sound())
    # Test static method
    print(Animal.is_good_fo_reels("pes"))
    print(Animal.is_good_fo_reels("kravicka"))
