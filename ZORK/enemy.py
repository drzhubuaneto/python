# enemy.py

class Enemy:
    """Nepřítel - nemoc se jménem, popisem, životy a sílou útoku."""
    def __init__(self, jmeno, popis, hp, attack):
        self.jmeno = jmeno
        self.popis = popis
        self.hp = hp
        self.attack = attack
