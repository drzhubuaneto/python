# room.py

class Room:
    """Místnost ve hře. Může obsahovat předměty, nepřátele a může mít zamčený vstup."""
    def __init__(self, nazev, popis, locked=False):
        self.nazev = nazev
        self.popis = popis
        self.locked = locked
        self.items = []   # seznam předmětů
        self.enemy = None # instance Enemy (nebo None)

    def __str__(self):
        return f"{self.nazev}: {self.popis}"
