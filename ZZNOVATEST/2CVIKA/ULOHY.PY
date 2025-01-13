## 1. Vytvořte s pomocí cyklů 2D list o 20x5 (20 řádků x 5 sloupečků), jenž bude obsahovat posloupnost čísel od 1 do 100.
list_2d = [[i + j * 5 + 1 for i in range(5)] for j in range(20)]
for row in list_2d:
    print(row)
##
list_2d = [[i + j * 5 + 1 for i in range(5)] for j in range(20)]
print("Úloha 1:\n", list_2d)

## 2. Vytvořte pomocí for cyklů 2D list o velikosti 5x5, naplňte jej hodnotou 0, na diagonále ale budou 1.
diagonal_2d = [[1 if i == j else 0 for j in range(5)] for i in range(5)]
for row in diagonal_2d:
    print(row)
##
diagonal_matrix = [[1 if i == j else 0 for i in range(5)] for j in range(5)]
print("Úloha 2:\n", diagonal_matrix)

## 3. BONUS: Vytvořte generátor 2D listu o velikosti N, jenž bude obsahovat náhodná čísla (0-9) a jejichž celkový součet v 2D listu bude roven dan hodnotě.
import random


def generate_2d_list_with_sum(n, target_sum):
    result = [[0] * n for _ in range(n)]
    numbers = [random.randint(0, 9) for _ in range(n * n)]
    while sum(numbers) > target_sum:
        numbers = [random.randint(0, 9) for _ in range(n * n)]
    
    for i in range(n):
        for j in range(n):
            result[i][j] = numbers.pop()
    return result

n = 5
target_sum = 50
result = generate_2d_list_with_sum(n, target_sum)
for row in result:
    print(row)
print("Total sum:", sum(sum(row) for row in result))

##
import random


def generate_2d_list(N, target_sum):
    while True:
        grid = [[random.randint(0, 9) for _ in range(N)] for _ in range(N)]
        if sum(sum(row) for row in grid) == target_sum:
            return grid

# Příklad použití
random_grid = generate_2d_list(5, 50)  # Velikost 5x5, celkový součet 50
print("Úloha 3:\n", random_grid)

## 4. Vytvořte 1D list o velikosti 100 obsahující náhodné hodnoty v rozmezí 0-50 (pomocí random.randint). 
# Následně vypište všechny pouze unikátní hodnoty v listu a vypište s pomocí bult-in funkce len() kolik těch unikátních průků je.
random_list = [random.randint(0, 50) for _ in range(100)]
unique_values = set(random_list)
print("Unique values:", unique_values)
print("Number of unique values:", len(unique_values))

##
import random

list_1d = [random.randint(0, 50) for _ in range(100)]  # Generování listu s 100 náhodnými hodnotami (0-50)
unique_values = list(set(list_1d))  # Získání unikátních hodnot
print("Úloha 4:\nUnikátní hodnoty:", unique_values)
print("Počet unikátních hodnot:", len(unique_values))  # Výpis počtu unikátních hodnot


## 5. Vytvořte si trojici listů (first_name,last_name,age) a naplňte je 5 hodnotami. 
# Následně vytvořte list tuplů, jenž bude kombinovat jméno, příjmení a věk. vypište vytvořené persony prostřednictvím for cyklu ve formátovaném stringu.
first_name = ["John", "Jane", "Alice", "Bob", "Charlie"]
last_name = ["Doe", "Smith", "Brown", "Johnson", "Davis"]
age = [25, 30, 22, 35, 28]

persons = list(zip(first_name, last_name, age))
for first, last, age in persons:
    print(f"Name: {first} {last}, Age: {age}")
    
##
first_name = ["Jan", "Petr", "Eva", "Anna", "Karel"]
last_name = ["Novak", "Svoboda", "Horak", "Dvorak", "Cerny"]
age = [25, 30, 22, 27, 35]

# Vytvoření seznamu tuple (jméno, příjmení, věk)
persons = list(zip(first_name, last_name, age))

# Výpis každé osoby ve formátovaném stringu
print("Úloha 5:")
for person in persons:
    print(f"Jméno: {person[0]}, Příjmení: {person[1]}, Věk: {person[2]}")

## 6. S pomocí funkce random.randint vytvořte list 100 náhodných čísel v rozmezí 0-20. 
# Zjistěte, jaké je největší číslo v listu, jaké je nejmenší, průměrnou hodnotu a kolikrát se tam vyskytuje číslo 5.
numbers = [random.randint(0, 20) for _ in range(100)]
print("Max value:", max(numbers))
print("Min value:", min(numbers))
print("Average value:", sum(numbers) / len(numbers))
print("Occurrences of 5:", numbers.count(5))

##
import random

# Generování listu 100 náhodných čísel v rozsahu 0–20
random_numbers = [random.randint(0, 20) for _ in range(100)]

# Zjištění požadovaných statistik
max_value = max(random_numbers)  # Největší číslo
min_value = min(random_numbers)  # Nejmenší číslo
avg_value = sum(random_numbers) / len(random_numbers)  # Průměrná hodnota
count_five = random_numbers.count(5)  # Počet výskytů čísla 5

# Výpis statistik
print("Úloha 6:")
print(f"Největší číslo: {max_value}")
print(f"Nejmenší číslo: {min_value}")
print(f"Průměrná hodnota: {avg_value:.2f}")
print(f"Počet pětek: {count_five}")

## 7. S pomocí listů hodnot z úlohy 2 a s pomocí knihovny random vytvořte 10 náhodných osob – jako slovníky s klíči: first_name, last_name, age.
names = ["John", "Jane", "Alice", "Bob", "Charlie", "Eve", "Grace", "Hank", "Ivy", "Jack"]
surnames = ["Doe", "Smith", "Brown", "Johnson", "Davis", "Taylor", "Anderson", "Thomas", "Jackson", "White"]

random_people = [
    {
        "first_name": random.choice(names),
        "last_name": random.choice(surnames),
        "age": random.randint(18, 60)
    }
    for _ in range(10)
]

for person in random_people:
    print(person)

##
import random

# Seznamy jmen, příjmení a věkový rozsah
first_name = ["Jan", "Petr", "Eva", "Anna", "Karel"]
last_name = ["Novak", "Svoboda", "Horak", "Dvorak", "Cerny"]

# Funkce pro vytvoření náhodné osoby
def generate_random_person():
    return {
        "first_name": random.choice(first_name),
        "last_name": random.choice(last_name),
        "age": random.randint(18, 60)
    }

# Generování seznamu 10 náhodných osob
random_people = [generate_random_person() for _ in range(10)]

# Výpis generovaných osob
print("Úloha 7:")
for person in random_people:
    print(person)