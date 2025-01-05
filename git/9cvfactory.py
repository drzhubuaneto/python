class Animal:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        pass

class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)

    def make_sound(self):
        return "Haf"

class Cat(Animal):
    def __init__(self, name):
        super().__init__(name)

    def make_sound(self):
        return "Mnau"
    
class AnimalFactory:
    @staticmethod
    def create_animal(type, name):
        if type == "dog":
            return Dog(name)
        elif type == "cat":
            return Cat(name)
        else:
            raise Exception ("Tohle zvire udelat neumim")
        

if __name__ == "__main__":
    d0 = AnimalFactory.create_animal("dog", "Rex")
    c0 = AnimalFactory.create_animal("cat", "Micka")

    print(d0.make_sound())
    print(c0.make_sound()) 
    pass
