# player.py

class Player:
    def __init__(self, jmeno):
        self.jmeno = jmeno
        self.max_hp = 100
        self.hp = 100
        self.weapon = None
        self.inventory = []

    def attack_damage(self):
        """Vrátí poškození podle aktuální zbraně. Pokud hráč žádnou zbraň nemá, základ je 5."""
        if self.weapon:
            return self.weapon.damage
        return 5

    def is_alive(self):
        return self.hp > 0
