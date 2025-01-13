# Úloha 2
names = ["Anna", "Jan", "Eva", "Petr", "Tomáš", "Lenka", "David", "Marek", "Alena", "Jana"]
ages = [25, 17, 30, 14, 18, 22, 19, 16, 21, 20]

# Vytvoření slovníku pomocí zip
persons = dict(zip(names, ages))

# Rozdělení na mladší než 18 a 18+
under_18 = {name: age for name, age in persons.items() if age < 18}
above_or_equal_18 = {name: age for name, age in persons.items() if age >= 18}
# Rozdělení osob podle věku pomocí lambda a filter
adults = dict(filter(lambda x: x[1] >= 18, persons.items()))
minors = dict(filter(lambda x: x[1] < 18, persons.items()))


# Seřazení obou slovníků podle věku
under_18_sorted = dict(sorted(under_18.items(), key=lambda item: item[1]))
above_or_equal_18_sorted = dict(sorted(above_or_equal_18.items(), key=lambda item: item[1]))
# Seřazení slovníků podle věku
adults_sorted = dict(sorted(adults.items(), key=lambda x: x[1]))
minors_sorted = dict(sorted(minors.items(), key=lambda x: x[1]))

# Kontrola délky seznamů
if len(names) == len(ages):
    print("Délky obou seznamů jsou stejné.")
else:
    print("Délky seznamů nejsou stejné!")
# Kontrola, zda mají oba seznamy stejnou délku
if len(adults_sorted) == len(minors_sorted):
    print("Úloha 2: Délky obou slovníků jsou stejné.")
else:
    print("Úloha 2: Délky obou slovníků nejsou stejné.")

# Výpis výsledků
print("Persony mladší než 18:", under_18_sorted)
print("Persony 18 a starší:", above_or_equal_18_sorted)
