import random


# Funkce pro generování 2D listu
def generate_2d_list(rows, cols, min_val=0, max_val=9):
    return [[random.randint(min_val, max_val) for _ in range(cols)] for _ in range(rows)]

# Generalizovaná funkce pro výpis 2D listu
def print_2d_list(matrix):
    for row in matrix:
        print(" ".join(map(str, row)))

# Vygenerování 2D listu 6x6
matrix_6x6 = generate_2d_list(6, 6)
print("Původní 6x6 matice:")
print_2d_list(matrix_6x6)

# Výpočet součtu pro řádky a sloupce
row_sums = [sum(row) for row in matrix_6x6]
col_sums = [sum(matrix_6x6[i][j] for i in range(6)) for j in range(6)]

print("\nSoučty řádků:")
for i, row_sum in enumerate(row_sums):
    print(f"Řádek {i}: {row_sum}")

print("\nSoučty sloupců:")
print(" ".join(map(str, col_sums)))

# Redukce na 3x3 matice
matrix_3x3 = [[sum(matrix_6x6[i][j] for j in range(c*2, c*2+2)) for c in range(3)] for i in range(0, 6, 2)]

print("\nRedukovaná 3x3 matice:")
print_2d_list(matrix_3x3)

# Najít prvky >= 7 a jejich pozice
elements_gte_7 = [(i, j, matrix_3x3[i][j]) for i in range(3) for j in range(3) if matrix_3x3[i][j] >= 7]

# Formátovaná funkce pro výpis výsledků
def format_positions(positions):
    formatted = [f"Řádek {i}, Sloupec {j}, Hodnota {value}" for i, j, value in positions]
    return "\n".join(formatted)

print("\nPrvky >= 7 v redukované 3x3 matici:")
if elements_gte_7:
    print(format_positions(elements_gte_7))
else:
    print("Žádné prvky >= 7 nenalezeny.")
