# game.py

from enemy import Enemy
from item import Item, Potion, Weapon
from player import Player
from room import Room
from utils import oddelit, pomaly_vypis
from yaml_loader import load_game_data


class Game:
    def __init__(self):
        # Načteme veškerá data o místnostech, nepřátelích, předmětech z YAML
        self.data = load_game_data("game_data.yaml")
        
        # Inicializace hráče
        self.hrac = Player("Nevědomý Výzkumník")
        
        # Vytvoření (načtení) místností
        self.rooms = {}
        self.vytvor_mistnosti_z_dat()

        # Počáteční místnost
        self.current_room = self.rooms.get("Hala")

    def vytvor_mistnosti_z_dat(self):
        """
        Načte definice místností z YAML a vytvoří Room instance.
        """
        # Projdeme definice v YAML (list nebo dict)
        for room_info in self.data["rooms"]:
            nazev = room_info["nazev"]
            popis = room_info["popis"]
            locked = room_info.get("locked", False)

            room = Room(nazev=nazev, popis=popis, locked=locked)
            # Pokud má místnost definované nepřátele
            if "enemy" in room_info:
                e = room_info["enemy"]
                enemy_obj = Enemy(
                    jmeno=e["jmeno"],
                    popis=e["popis"],
                    hp=e["hp"],
                    attack=e["attack"]
                )
                room.enemy = enemy_obj

            # Pokud má místnost definované předměty
            if "items" in room_info:
                for it in room_info["items"]:
                    typ = it.get("typ", "item")
                    nazev_item = it["nazev"]
                    popis_item = it.get("popis", "")
                    
                    if typ == "weapon":
                        damage = it.get("damage", 5)
                        w = Weapon(nazev_item, popis_item, damage)
                        room.items.append(w)
                    elif typ == "potion":
                        healing = it.get("healing", 10)
                        p = Potion(nazev_item, popis_item, healing)
                        room.items.append(p)
                    else:
                        # Obecný Item (např. klíč)
                        i = Item(nazev_item, popis_item)
                        room.items.append(i)

            # Uložíme do slovníku
            self.rooms[nazev] = room

    def start_game(self):
        oddelit()
        pomaly_vypis(self.data["intro_text"])
        oddelit()

        while True:
            # Kontrola, zda je hráč naživu
            if not self.hrac.is_alive():
                pomaly_vypis("Upadáte do mdlob... Vaše tělo už nevydrží...\nKONEC HRY.")
                break

            # Kontrola, jestli hráč nemá klíč od východu (konec hry)
            if self.check_game_end():
                break

            # Zobrazení informací o aktuální místnosti
            self.zobraz_info_o_mistnosti(self.current_room)

            # Hráčova volba akce
            volba = input("Co chcete dělat? [prozkoumat / jít / inventář / konec] ").strip().lower()

            if volba == "prozkoumat":
                self.prozkoumat_mistnost(self.current_room)
            elif volba == "jít":
                self.jit_do_mistnosti()
            elif volba == "inventář":
                self.zobraz_inventar()
            elif volba == "konec":
                pomaly_vypis("Hra byla ukončena hráčem.")
                break
            else:
                pomaly_vypis("Nerozumím... Zkuste jinou akci.")

    def zobraz_info_o_mistnosti(self, room):
        oddelit()
        pomaly_vypis(f"Akt. místnost: {room.nazev}")
        pomaly_vypis(room.popis)
        if room.enemy:
            pomaly_vypis(f"Nepřítel: {room.enemy.jmeno} – {room.enemy.popis}")
        oddelit()

    def prozkoumat_mistnost(self, room):
        # Pokud je nepřítel, nastane boj
        if room.enemy:
            self.boj_s_nepritelem(room.enemy, room)
        else:
            # Když nepřítel není, můžeme sbírat předměty
            if room.items:
                pomaly_vypis("V místnosti jste našli:")
                for idx, item in enumerate(room.items):
                    pomaly_vypis(f"{idx+1}. {item}")
                vyber = input("Vyberte číslo předmětu, který chcete sebrat (0 pro zrušení): ")
                try:
                    cislo = int(vyber)
                    if 1 <= cislo <= len(room.items):
                        sebrany_predmet = room.items[cislo-1]
                        self.sebrat_predmet(sebrany_predmet, room)
                    else:
                        pomaly_vypis("Nic jste nesebrali.")
                except ValueError:
                    pomaly_vypis("Neplatná volba.")
            else:
                pomaly_vypis("V místnosti už není nic zajímavého.")

    def sebrat_predmet(self, item, room):
        # Pokud je to zbraň, porovnáme a případně nasadíme
        if isinstance(item, Weapon):
            pomaly_vypis(f"Sebrali jste zbraň: {item.nazev}")
            if self.hrac.weapon is None or item.damage > self.hrac.weapon.damage:
                pomaly_vypis(f"Nasazujete {item.nazev} jako svou aktivní zbraň.")
                self.hrac.weapon = item
            else:
                pomaly_vypis("Vaše současná zbraň je lepší. Ukládáte novou zbraň do inventáře.")
                self.hrac.inventory.append(item)
        elif isinstance(item, Potion):
            pomaly_vypis(f"Sebrali jste lektvar: {item.nazev}")
            self.hrac.inventory.append(item)
        else:
            # Obecný Item (např. klíč)
            pomaly_vypis(f"Sebrali jste: {item.nazev}")
            self.hrac.inventory.append(item)

        room.items.remove(item)

    def boj_s_nepritelem(self, enemy, room):
        pomaly_vypis(f"Pustili jste se do boje s {enemy.jmeno}!")
        while self.hrac.is_alive() and enemy.hp > 0:
            pomaly_vypis(f"Váš život: {self.hrac.hp}, Život nepřítele: {enemy.hp}")
            akce = input("Vyberte akci [útok / lektvar / únik]: ").strip().lower()

            if akce == "útok":
                dmg = self.hrac.attack_damage()
                enemy.hp -= dmg
                pomaly_vypis(f"Způsobili jste nepříteli {dmg} poškození!")
                if enemy.hp <= 0:
                    pomaly_vypis(f"{enemy.jmeno} byl poražen!")
                    room.enemy = None
                    break

                # Nepřítel útočí
                self.hrac.hp -= enemy.attack
                pomaly_vypis(f"{enemy.jmeno} zaútočil a způsobil vám {enemy.attack} poškození.")

            elif akce == "lektvar":
                if not self.pouzit_lektvar():
                    pomaly_vypis("Nemáte žádný použitelný lektvar nebo jste zrušili použití.")
            elif akce == "únik":
                pomaly_vypis("Pokusili jste se utéct zpět...")
                break
            else:
                pomaly_vypis("Neplatná akce. Zkuste znovu.")

            if self.hrac.hp <= 0:
                pomaly_vypis("Vaše životy klesly na nulu. Hra končí.")
                return

    def pouzit_lektvar(self):
        # Najdeme lektvary v inventáři
        lektvary = [i for i in self.hrac.inventory if isinstance(i, Potion)]
        if not lektvary:
            return False

        pomaly_vypis("Dostupné lektvary:")
        for idx, lek in enumerate(lektvary):
            pomaly_vypis(f"{idx+1}. {lek.nazev} (+{lek.healing} HP)")
        vyber = input("Zadejte číslo lektvaru k použití (0 pro zrušení): ")
        try:
            cislo = int(vyber)
            if 1 <= cislo <= len(lektvary):
                vybrany_lektvar = lektvary[cislo-1]
                self.hrac.hp = min(self.hrac.hp + vybrany_lektvar.healing, self.hrac.max_hp)
                pomaly_vypis(f"Použili jste {vybrany_lektvar.nazev} a obnovili si {vybrany_lektvar.healing} HP.")
                self.hrac.inventory.remove(vybrany_lektvar)
                return True
        except ValueError:
            pass
        return False

    def jit_do_mistnosti(self):
        # Vypíšeme seznam místností
        vsechny_mistnosti = list(self.rooms.keys())  # např. ["Hala", "Biochemie", "Mikrobiologie", ...]
        pomaly_vypis("Dostupné dveře:")
        for i, m in enumerate(vsechny_mistnosti):
            locked_status = "zamčené" if self.rooms[m].locked else "odemčené"
            pomaly_vypis(f"{i+1}. {m} - {locked_status}")

        vyber = input("Zadejte číslo místnosti, do které chcete jít (0 pro zrušení): ")
        try:
            cislo = int(vyber)
            if 1 <= cislo <= len(vsechny_mistnosti):
                cilova_mistnost = self.rooms[vsechny_mistnosti[cislo-1]]
                if cilova_mistnost.locked:
                    # Pokus o odemčení
                    if self.zkus_odemknout(cilova_mistnost):
                        cilova_mistnost.locked = False
                        pomaly_vypis(f"Odemkli jste {cilova_mistnost.nazev}.")
                    else:
                        pomaly_vypis(f"Nemáte klíč pro {cilova_mistnost.nazev}!")
                        return
                self.current_room = cilova_mistnost
            else:
                pomaly_vypis("Zůstáváte v aktuální místnosti.")
        except ValueError:
            pomaly_vypis("Neplatná volba.")

    def zkus_odemknout(self, room):
        potrebny_klic = f"Čipová karta - {room.nazev}"
        for item in self.hrac.inventory:
            if item.nazev == potrebny_klic:
                return True
        return False

    def zobraz_inventar(self):
        if not self.hrac.inventory and not self.hrac.weapon:
            pomaly_vypis("Inventář je prázdný.")
            return

        oddelit()
        pomaly_vypis("Váš inventář:")
        if self.hrac.weapon:
            pomaly_vypis(f"- Aktuální zbraň: {self.hrac.weapon.nazev} (DMG: {self.hrac.weapon.damage})")

        if self.hrac.inventory:
            for idx, item in enumerate(self.hrac.inventory):
                if isinstance(item, Weapon):
                    pomaly_vypis(f"- {idx+1}: [Zbraň] {item.nazev} (DMG: {item.damage})")
                elif isinstance(item, Potion):
                    pomaly_vypis(f"- {idx+1}: [Lektvar] {item.nazev} (+{item.healing} HP)")
                else:
                    pomaly_vypis(f"- {idx+1}: {item.nazev}")
        oddelit()

    def check_game_end(self):
        """
        Zkontroluje, jestli hráč získal klíč od dveří (tj. "Klíč od dveří" v inventáři)
        a tím pádem může hru ukončit (probudí se, byl to jen sen).
        """
        for i in self.hrac.inventory:
            if i.nazev == "Klíč od dveří":
                pomaly_vypis(
                    "Našli jste klíč od východu! Otevíráte dveře... "
                    "Najednou vás oslní světlo a probouzíte se. Všechno to byl jen sen!"
                )
                pomaly_vypis("KONEC HRY.")
                return True
        return False
