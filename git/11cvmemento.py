from copy import deepcopy


class Memento:
    def __init__(self, state):
        self.state = deepcopy(state)

class Originator:
    def __init__(self, state:set = None):
        self.state = state

    def save_to_memento(self) -> Memento:
        return Memento(self.state)
    
    def restore_from_memento(self, memento: Memento):
        self.state = memento.state

class Caretaker:
    def __init__(self):
        self.mementos = []

    def add_memento(self, memento: Memento):
        self.mementos.append(memento)

    def get_memento(self, index: int) -> Memento:
        return self.mementos[index]
    
if __name__ == "__main__":
    orig = Originator()
    caretaker = Caretaker()

    orig.state = "State 1"
    caretaker.add_memento(orig.save_to_memento())

    print(orig.state)
    orig.state = "State 2" 
    caretaker.add_memento(orig.save_to_memento())
    print(f"Current state: {orig.state}")
    orig.restore_from_memento(caretaker.get_memento(0))
    print(f"Current state: {orig.state}")
