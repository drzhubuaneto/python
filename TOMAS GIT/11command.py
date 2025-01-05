from abc import ABC, abstractmethod


class Command(ABC):
    @abstractmethod
    def execute(self)->str:
        pass

class Door():
    def __init__(self,door_name:str):
        self.door_name=door_name
        self.state="Nezname"
    
    def __str__(self)->str:
        return f"Dvere:{self.door_name} jsou ve stavu:{self.state}"
    
class UnlockDoorCommand(Command):
    def execute(self,door:Door)->str:
        door.state="Odemcene"
        return f"Odemykam dvere: {door.door_name}"
    
class LockDoorCommand(Command):
    def execute(self,door:Door)->str:
        door.state="Zamknute"
        return f"Zamykam dvere: {door.door_name}"

if __name__=="__main__":
    door=Door("Dvere od B-520")
    commanddict={"lock":LockDoorCommand(),"unlock":UnlockDoorCommand()}
    print(door)
    print(commanddict.get("lock",None).execute(door))
    # **Stejne jako o radek vyse**
    # lock_command=LockDoorCommand()
    # lock_command.execute(door)
    # ****
    print(door)
    print(commanddict['unlock'].execute(door))
    print(door)
