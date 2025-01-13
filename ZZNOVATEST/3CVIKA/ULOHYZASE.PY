# Úloha 8: Vytvoření bojovníka se slovníkem atributů a validací.

# Funkce pro vytvoření bojovníka
def create_warrior(attributes):
    # Povinné a nepovinné atributy
    mandatory_attrs = ["INT", "ATK", "DEF", "CON"]
    optional_attrs = ["WIT", "DEX"]

    # Kontrola minimálního počtu atributů
    if len(attributes) < 4:
        raise ValueError("Příliš málo parametrů pro vytvoření bojovníka.")

    # Sestavení bojovníka
    warrior = {}
    for attr in mandatory_attrs + optional_attrs:
        if attr in attributes:
            warrior[attr] = attributes[attr]
        elif attr in mandatory_attrs:
            raise ValueError(f"Parametr {attr} je povinný a chybí.")

    return warrior

# Vytvoření bojovníka
warrior = create_warrior({
    "INT": 10, "ATK": 8, "DEF": 9, "CON": 7, "WIT": 5, "DEX": 6
})
print("Úloha 8:\nVytvořený bojovník:", warrior)

# Uložení bojovníka do JSON souboru
import json
with open("warriors.json", "w") as file:
    json.dump([warrior], file, indent=4)
print("Bojovník byl uložen do souboru warriors.json.")






# Úloha 9: Funkce pro ukládání a načítání JSON/YAML souborů.
import yaml

# Funkce pro ukládání dat
def save_data(filename, data, mode="w"):
    if filename.endswith(".json"):
        with open(filename, mode) as file:
            json.dump(data, file, indent=4)
    elif filename.endswith(".yaml"):
        with open(filename, mode) as file:
            yaml.dump(data, file)
    else:
        raise ValueError("Nepodporovaný formát souboru.")

# Funkce pro načítání dat
def load_data(filename):
    if filename.endswith(".json"):
        with open(filename, "r") as file:
            return json.load(file)
    elif filename.endswith(".yaml"):
        with open(filename, "r") as file:
            return yaml.load(file, Loader=yaml.FullLoader)
    else:
        raise ValueError("Nepodporovaný formát souboru.")

# Přidání dalšího bojovníka a ukládání do souboru
def add_warrior_to_file(filename, new_warrior):
    existing_warriors = load_data(filename) if filename.endswith((".json", ".yaml")) else []
    existing_warriors.append(new_warrior)
    save_data(filename, existing_warriors, mode="w")

# Vytvoření nového bojovníka
new_warrior = {
    "INT": 12, "ATK": 7, "DEF": 10, "CON": 6, "WIT": 4, "DEX": 8
}

# Uložení do JSON souboru
add_warrior_to_file("warriors.json", new_warrior)
print("Nový bojovník byl přid
