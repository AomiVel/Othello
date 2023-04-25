from checkers import Checker

black_text = "\033[30m"
white_text = "\033[7m"
gb_text = "\033[42m"
end_text = "\033[0m"
placeable_text = "\033[46m"

def show_board(board):
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


checker = Checker()

def patch_placeable(board, me):
    placeable_list = []
    for y, row in enumerate(board):
        for x in range(len(row)):
            if checker.check_all(x, y, board, me):
                placeable_list.append((x, y))

    for x, y in placeable_list:
        board[y][x] = 3
    
    return board