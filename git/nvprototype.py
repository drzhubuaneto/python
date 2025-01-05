from copy import deepcopy


class Product:
    def __init__(self, name, price, category):
        self._name = name
        self._price = price
        self._category = category

    def clone(self):
        return deepcopy(self)
    
    def change_price(self, new_price):
        self._price = new_price
    
    def __str__(self):
        return f"Product {self._name} costs {self._price} and belongs to {self._category}"
    

product1 = Product("Laptop", 10000, "Electronic")
product2 = product1.clone()

print(product1)
print(product2)

product3 = product1.clone()
product3.change_price(15000)
print(product3)
