from sudoku.canvas import draw_sudoku
from sudoku.utils import is_valid_sudoku, parse_template


def play_game(file_path):
    sudoku = parse_template(file_path)
    draw_sudoku(sudoku)

    while True:
        user_input = input("Zadejte koordináty a hodnotu (např. [0,0,8]): ")
        try:
            move = eval(user_input)
            if len(move) == 3 and isinstance(move[0], int) and isinstance(move[1], int) and isinstance(move[2], int):
                row, col, value = move
                sudoku[row][col] = value
                if is_valid_sudoku(sudoku):
                    draw_sudoku(sudoku)
                else:
                    print("Neplatný tah. Sudoku obsahuje chybu.")
            else:
                print("Chybný formát.")
        except Exception as e:
            print(f"Chyba: {e}")
