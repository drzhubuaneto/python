# ÚKOL 1
import json


def validate_and_create_warrior(attributes, params):
    required_attributes = {"INT", "ATK", "DEF", "CON", "WIT", "DEX"}
    missing_attributes = required_attributes - set(params.keys())

    if len(params) < 4:
        raise ValueError("Nelze vytvořit bojovníka - příliš málo parametrů.")

    if missing_attributes:
        print(f"Chybí následující parametry: {missing_attributes}")

    warrior = {key: params.get(key, None) for key in required_attributes}

    with open("warrior.json", "w") as file:
        json.dump(warrior, file, indent=4)

    return warrior

# Příklad použití:
attributes = ["INT", "ATK", "DEF", "CON"]
params = {
    "INT": 10,
    "ATK": 15,
    "DEF": 8,
    "CON": 12,
    "WIT": 5,
    "DEX": 7
}

warrior = validate_and_create_warrior(attributes, params)
print("Vytvořen bojovník:", warrior)

# ÚKOL 2
import yaml


def save_to_file(data, filename, mode="w"):
    if filename.endswith(".json"):
        with open(filename, mode) as file:
            if mode == "a":
                file.seek(0, 2)  # Move the cursor to the end of the file
                file.write(",\n")
                json.dump(data, file, indent=4)
            else:
                json.dump(data, file, indent=4)

    elif filename.endswith(".yaml"):
        with open(filename, mode) as file:
            yaml.dump(data, file)
    else:
        raise ValueError("Nepodporovaný formát souboru. Použijte .json nebo .yaml.")

def load_from_file(filename):
    if filename.endswith(".json"):
        with open(filename, "r") as file:
            return json.load(file)

    elif filename.endswith(".yaml"):
        with open(filename, "r") as file:
            return yaml.safe_load(file)

    else:
        raise ValueError("Nepodporovaný formát souboru. Použijte .json nebo .yaml.")

# Test funkcí:
data = {
    "INT": 10,
    "ATK": 15,
    "DEF": 8,
    "CON": 12,
    "WIT": 5,
    "DEX": 7
}

save_to_file(data, "warrior.json")
loaded_data = load_from_file("warrior.json")
print("Načtený bojovník:", loaded_data)

# Test s přidáním dalších bojovníků
new_data = {
    "INT": 8,
    "ATK": 18,
    "DEF": 10,
    "CON": 14,
    "WIT": 6,
    "DEX": 9
}
save_to_file(new_data, "warrior.json", mode="a")
