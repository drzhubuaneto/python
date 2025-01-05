from copy import deepcopy


class Animal:
    def __init__(self, name):
        self.name = name

    def clone(self):
        return deepcopy(self)
    
    def __str__(self):
        return f"Zvire je {self.name}"
    
a0 = Animal("Pejsek")
a1 = a0.clone()	
a2 = a0.clone()

a1.name = "Kocicka"

print(a0)
print(a1)
print(a2)
