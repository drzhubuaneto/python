from abc import ABC, abstractmethod


class Observer(ABC):
    @abstractmethod
    def update(self, message: str)->str:
        pass

class Customer(Observer):
    def __init__(self, name: str):
        self.name = name

    def update(self, message: str) -> str:
        return f"{self.name} obdrzel zpravu: {message}"
    
class Observable(ABC):
    @abstractmethod
    def register_observer(self, observer: Observer)->None:
        pass
    @abstractmethod
    def notify(self, message: str)->None:
        pass

class Store(Observable):
    def __init__(self):
        self.customers = []

    def register_observer(self, customer: Observer)->None:
        self.customers.append(customer)

    def notify(self, message: str)->None:
        for customer in self.customers:
            print(customer.update(message))

if __name__ == "__main__":
    store = Store()
    customer1 = Customer("Pepa")
    customer2 = Customer("Jirka")
    store.register_observer(customer1)
    store.register_observer(customer2)
    store.notify("Dnes je sleva na pivo")
    store.notify("Zitra bude sleva na vino")
