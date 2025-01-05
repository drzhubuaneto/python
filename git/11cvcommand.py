from abc import ABC, abstractmethod


class Command(ABC):
    @abstractmethod
    def execute(self) -> str:
        pass



class Door:
    def __init__(self, door_name: str):
        self.door_name = door_name
        self.state = "Nezname"

    def __str__(self):
        return f"Dvere: {self.door_name} jsou ve stavu: {self.state}"


class UnlockDoorCommand(Command):
    def execute(self, door: Door) -> str:
        door.state = "Odemceno"
        return f"Odemykam dvere: {door.door_name}" 
        
class LockDoorCommand(Command):
    def execute(self, door: Door) -> str:
        door.state = "Zamknuto"
        return f"Zamykam dvere: {door.door_name}"
    
if __name__ == "__main__":
    door = Door("Dvere")
    
    commandDict = {"lock": LockDoorCommand(), "unlock": UnlockDoorCommand()}

    print(door)
    print(commandDict["lock"].execute(door))
    print(door)
    print(commandDict["unlock"].execute(door))
    print(door)
