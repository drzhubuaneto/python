def draw_sudoku(matrix):
    for row in matrix:
        print(" | ".join(map(str, row)))
        print("-" * (len(row) * 4 - 1))
