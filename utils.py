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


def enemy_num(me: int):
    match me:
        case 1:
            enemy = 2
        case 2:
            enemy = 1
    
    return enemy

def is_board_filled(board):
    for r in board:
        if 0 in r:
            return False
    return True


