from abc import ABC, abstractmethod


class Command(ABC):
   @abstractmethod
   def execute(self) -> str:
      pass
   
class Light():
    def __init__(self, name):
      self._name = name
      self._on = False

    def turn_on(self):
       self._on = True

    def turn_off(self):
       self._on = False

    def get_state(self) -> bool:
       return self._on
    
    def __str__(self):
       return f"light with name {self._name} is " + ("on" if self._on else "off")
    
class Remote():
   def __init__(self, name, light: Light):
       self._name = name
       self._light = light
      
   def execute_command(self, command: Command):
         return command.execute(self)


   def __str__(self):
       return f"Remote with name {self._name} controlling {self._light}"
    
class TurnLightOn(Command):
   def execute(self, remote: Remote) -> str:
      remote._light.turn_on()
      return "Turning light on"
   
class TurnLightOff(Command):
   def execute(self, remote: Remote) -> str:
      remote._light.turn_off()
      return "Turning light off"
   
if __name__ == "__main__":
   light_kitchen = Light("Light kitchen")

   remote = Remote("Kitchen remote", light_kitchen)
   print(remote)

   commandDict = {"on": TurnLightOn(), "off": TurnLightOff()}

   print(remote.execute_command(commandDict["on"]))
   print(remote.execute_command(commandDict["off"]))
      
