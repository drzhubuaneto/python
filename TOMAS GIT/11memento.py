from copy import deepcopy


class Memento:
    def __init__(self,state):
        self.state=deepcopy(state)
    
class Originator:
    def __init__(self,state:str=None):
        self.state=state
    
    def save_to_memento(self):
        return Memento(self.state)
    
    def restore_from_memento(self,memento):
        self.state=memento.state

class CareTaker:
    def __init__(self):
        self.mementos=[]
    
    def add_memento(self,memento:Memento):
        self.mementos.append(memento)
    
    def get_memento(self,index):
        return self.mementos[index]
    
if __name__=="__main__":
    orig=Originator()
    caretaker=CareTaker()

    orig.state="State1"
    caretaker.add_memento(orig.save_to_memento())
    print(orig.state)
    orig.state="State2"
    caretaker.add_memento(orig.save_to_memento())
    print(f"Current state is:{orig.state}")
    orig.restore_from_memento(caretaker.get_memento(0))
    print(f"Current state is:{orig.state}")
