from fighter import Fighter


class Fight():
    def __init__(self,fighter0:Fighter, fighter1:Fighter):
        self.fighter0=fighter0
        self.fighter1=fighter1
        # Call main method to simulate fight
    
    def simulate(self):
        # Simulate spell attack before
        f0_spell=self.fighter0.get_spell_power()
        f1_spell=self.fighter1.get_spell_power()
        if f0_spell > f1_spell:
            self.fighter1.decrease_hp(f0_spell-f1_spell)
        else: 
            self.fighter0.decrease_hp(f1_spell-f0_spell)
        # Simulate fight
        while self.fighter0.hp>0 and self.fighter1.hp>0:
            # Generate who attack
            if self.fighter0.get_dexterity() > self.fighter1.get_dexterity():
                self.simulate_attack(self.fighter0,self.fighter1)
            else:
                self.simulate_attack(self.fighter1,self.fighter0)
            pass
        # End - slus, print winner winner chicken dinner
        print(self.get_winner())

    # Simulate attack
    def simulate_attack(self,attacker:Fighter,deffender:Fighter):
        deff=deffender.get_deff()
        attack=attacker.get_attack()
        deffender.decrease_hp(attack-deff)
        print(f"Attacker:{attacker.name} fights to defender:{deffender.name} \
              with power:{attack} and defenders hp reamins: {deffender.hp} hp.")
        # deffender.decrease_hp(deffender.get_deff()-attacker.get_attack())

    def get_winner(self):
        if self.fighter0.hp>0:
            return f"Winner is {self.fighter0.name}."
        return f"Winner is {self.fighter1.name}."
