import random as rnd

import defaults as df


class Fighter():
    def __init__(self,name:str,STR:int,DEX:int,CON:int,INT:int,DEF:int):
        self.name=name
        self.strength=STR*df.c_str
        self.dexterity=DEX*df.c_dex
        self.hp=CON*df.c_con
        self.spell_power=INT*df.c_int
        self.deffensive=DEF*df.c_def
    
    def get_attack(self) -> float:
        return round(rnd.uniform(self.strength/2, self.strength),1)
    
    def get_deff(self) -> float:
        return round(rnd.uniform(self.deffensive/4,self.deffensive),1)
    
    def get_spell_power(self) -> float:
        return self.spell_power
    
    def get_dexterity(self) -> float:
        return round(rnd.uniform(self.dexterity/2, self.dexterity))
    
    def decrease_hp(self,value:float) -> None:
        if value>0:
            self.hp-=value
            self.hp=int(self.hp)

    def __str__(self):
        return f"Fighter named:{self.name} has: {self.hp} hp"
    
# TODO: generate Docstrings
