from abc import ABC, abstractmethod


class Observer(ABC):
    @abstractmethod
    def update(self,message:str)->str:
        pass

class Customer(Observer):
    def __init__(self,name):
        self.name=name
    def update(self,msg:str)->str:
        return f"Pro zakaznika:{self.name} prisla zprava:{msg}"
    
class Observable(ABC):
    @abstractmethod
    def register_observer(self,observer:Observer)->None:
        pass
    @abstractmethod
    def notify(self,message:str)->None:
        pass

class Store(Observable):
    def __init__(self):
        self.customers=[]
    
    def register_observer(self, customer):
        self.customers.append(customer)
    
    def notify(self,message:str)->None:
        for cus in self.customers:
            print(cus.update(message)) # Nyni print, protoze update nam vraci string.
    
if __name__=="__main__":
    # Vytvorime zakazniky
    c0=Customer("Pepik")
    c1=Customer("Max")
    # Create concreete observable
    store=Store()
    # Add observers
    store.register_observer(c0)
    store.register_observer(c1)
    store.notify("Vsichni zakaznici musi neprodlene opustit nakupni stredisko.")
    store.notify("Vsichni zakaznici maji slevu na ovoce 50%")
