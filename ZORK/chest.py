# chest.py

class Chest:
    def __init__(self, items=None, locked=False):
        self.locked = locked
        self.items = items if items else []

    def open_chest(self, player_inventory):
        if self.locked:
            # nějaká logika pro klíč atd.
            pass
        else:
            # přidat itemy do hráčova inventáře
            for i in self.items:
                player_inventory.append(i)
            self.items = []
