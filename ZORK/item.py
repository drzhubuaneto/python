# item.py

class Item:
    """Obecná třída pro jakýkoliv předmět ve hře."""
    def __init__(self, nazev, popis=""):
        self.nazev = nazev
        self.popis = popis

    def __str__(self):
        return f"{self.nazev}: {self.popis}"

class Weapon(Item):
    """Zbraň - specializovaný předmět s určitým poškozením (damage)."""
    def __init__(self, nazev, popis, damage):
        super().__init__(nazev, popis)
        self.damage = damage

class Potion(Item):
    """Lektvar - specializovaný předmět, který navrátí hráči životy."""
    def __init__(self, nazev, popis, healing):
        super().__init__(nazev, popis)
        self.healing = healing
