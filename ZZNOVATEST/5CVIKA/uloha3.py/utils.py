def parse_template(file_path):
    with open(file_path, 'r') as f:
        return [list(map(int, line.strip().split())) for line in f]

def is_valid_sudoku(matrix):
    n = len(matrix)
    for i in range(n):
        if len(set(matrix[i])) != len(matrix[i]) or len(set(row[i] for row in matrix)) != n:
            return False
    return True
