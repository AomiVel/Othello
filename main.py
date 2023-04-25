from checkers import Checker


# 0 - 空き
# 1 - 白
# 2 - 黒
# 3 - 設置可能(空色)
me = 1

match me:
    case 1:
        enemy = 2
    case 2:
        enemy = 1

white = '○'
black = '●'


black_text = "\033[30m"
white_text = "\033[7m"
gb_text = "\033[42m"
end_text = "\033[0m"
placeable_text = "\033[46m"


board = [
#    0  1  2  3  4  5  6  7
    [0, 0, 0, 0, 0, 0, 0, 0], # 0
    [0, 0, 0, 0, 0, 0, 0, 0], # 1
    [0, 0, 0, 0, 0, 0, 0, 0], # 2
    [0, 0, 0, 1, 2, 0, 0, 0], # 3
    [0, 0, 0, 2, 1, 0, 0, 0], # 4
    [0, 0, 0, 0, 0, 0, 0, 0], # 5
    [0, 0, 0, 0, 0, 0, 0, 0], # 6
    [0, 0, 0, 0, 0, 0, 0, 0], # 7
]

import random
for a in range(8):
    for b in range(8):
        board[a][b] = random.randint(0, 2)

checker = Checker(board, me)


def show_board():
    for row in board:
        print(gb_text, "+---+---+---+---+---+---+---+---+", end_text, sep='')
        print(gb_text, '|', end_text, sep='', end='')

        for col in row:
            match col:
                case 0:
                    print(gb_text, "   ", end_text, sep='', end='')
                case 1:
                    print(white_text, "   ", end_text, sep='', end='')
                case 2:
                    print(black_text, "   ", end_text, sep='', end='')
                case 3:
                    print(placeable_text, "   ", end_text, sep='', end='')
            print(gb_text, '|', end_text, sep='', end='')
        print()

    print(gb_text, "+---+---+---+---+---+---+---+---+", end_text, sep='')

# ↑ ↗ → ↘ ↓ ↙ ← ↖
def patch_placeable():
    global board
    placeable_list = []
    for y, row in enumerate(board):
        for x, col in enumerate(row):
            if checker.check_all(x, y):
                placeable_list.append((x, y))
            
    
    for x, y in placeable_list:
        board[y][x] = 3



show_board()
patch_placeable()
show_board()
