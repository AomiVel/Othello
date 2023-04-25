# 0 - 空き
# 1 - 白
# 2 - 黒
# 3 - 設置可能(空色)
me = 1


if not me in (1, 2):
    print("Select your color")
    print("1 - White")
    print("2 - Black")
    me = input("Number[1/2]:")


white = '○'
black = '●'


black_text = "\033[30m"
white_text = "\033[7m"
gb_text = "\033[42m"
end_text = "\033[0m"
placeable_text = "\033[46m"


board = [
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 2, 0, 0, 0],
    [0, 0, 0, 2, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
]

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


def patch_placeable(color: int):
    for rindex, row in enumerate(board):
        for cindex, col in enumerate(row):
            if cindex in []
show_board()

