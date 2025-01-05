from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass

    @classmethod
    def create_animal(cls, name):
        return cls(name)
    
    @staticmethod
    def is_good_fo_reels(animal):
        print()

class Dog(Animal):
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        print("Haf")
    
class Cat(Animal):
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        print("Mnau")

if __name__ == "__main__":
    d = Dog("Rex")
    d.make_sound()

    c = Cat("Micka")
    c.make_sound()
    pass
