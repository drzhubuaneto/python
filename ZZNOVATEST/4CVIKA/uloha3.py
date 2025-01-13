# Úloha 3
import random

# Generování listu s náhodnými hodnotami
random_values = [random.randint(1, 100) for _ in range(20)]

# Identifikace lichých čísel pomocí jejich indexů
odd_indices = [i for i, value in enumerate(random_values) if value % 2 != 0]

# Odstranění lichých čísel z původního listu
for index in sorted(odd_indices, reverse=True):
    random_values.pop(index)

# Kontrola správnosti (list by neměl obsahovat lichá čísla)
print("Výsledek po odstranění lichých hodnot:", random_values)
assert all(value % 2 == 0 for value in random_values), "V seznamu stále existují lichá čísla!"







# Úloha 3: Manipulace s listem náhodných hodnot.
import random

# Vytvoření listu náhodných hodnot (alespoň 20)
random_values = [random.randint(1, 100) for _ in range(20)]

# Seznam indexů lichých čísel
odd_indices = [index for index, value in enumerate(random_values) if value % 2 != 0]

# Odstranění lichých čísel pomocí pop
for index in sorted(odd_indices, reverse=True):
    random_values.pop(index)

# Výpis výsledků
print("Úloha 3:")
print("Seznam bez lichých hodnot:", random_values)
print("Odstraněné hodnoty na indexech:", odd_indices)
