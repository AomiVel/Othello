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

# import random
# for a in range(8):
#     for b in range(8):
#         board[a][b] = random.randint(0, 2)

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
            if check_placeable(x, y):
                placeable_list.append((x, y))
            
    
    for x, y in placeable_list:
        board[y][x] = 3


def check_placeable(x, y):
    return any([
        check_above(x, y),
        check_upright(x, y),
        check_right(x, y),
        check_bottomright(x, y),
        check_bottom(x, y),
        check_bottomleft(x, y),
        check_left(x, y),
        check_upleft(x, y)
    ])

def check_above(x, y):
    if y in [0, 1]:
        return False
    
    # 空きじゃなければ不可
    if board[y][x] != 0:
        return False

    # 設置確認場所より上のスペースの状態を取得
    disk_list = []
    for r in range(y):
        disk_list.append(board[y - (r+1)][x])
    
    # 設置確認場所の真上が敵のもの以外だったら不可
    if disk_list[0] != enemy:
        return False
    
    # 真上のを削除
    del disk_list[0]

    for disk in disk_list:
        if disk == enemy:
            continue
        elif disk == me:
            return True
        elif disk == 0:
            return False
    return False

def check_upright(x, y):
    if y in [0, 1]:
        return False
    if x in [6, 7]:
        return False
    
    # 空きじゃなければ不可
    if board[y][x] != 0:
        return False

    up = y
    right = 7 - x

    disk_list = []
    for r in range(min((up, right))):
        disk_list.append(board[y - (r+1)][x + r + 1])
    
    if disk_list[0] != enemy:
        return False
    
    del disk_list[0]

    for disk in disk_list:
        if disk == enemy:
            continue
        elif disk == me:
            return True
        elif disk == 0:
            return False
    return False

def check_right(x, y):
    if x in [6, 7]:
        return False
    
    if board[y][x] != 0:
        return False

    disk_list = []
    for r in range(7 - x):
        disk_list.append(board[y][x + r + 1])
    
    if disk_list[0] != enemy:
        return False
    
    del disk_list[0]

    for disk in disk_list:
        if disk == enemy:
            continue
        elif disk == me:
            return True
        elif disk == 0:
            return False
    return False

def check_bottomright(x, y):
    if y in [6, 7]:
        return False
    if x in [6, 7]:
        return False
    
    # 空きじゃなければ不可
    if board[y][x] != 0:
        return False

    bottom = 7 - y
    right = 7 - x

    disk_list = []
    for r in range(min((bottom, right))):
        disk_list.append(board[y + r + 1][x + r + 1])
    
    if disk_list[0] != enemy:
        return False
    
    del disk_list[0]

    for disk in disk_list:
        if disk == enemy:
            continue
        elif disk == me:
            return True
        elif disk == 0:
            return False
    return False

def check_bottom(x, y):
    if y in [6, 7]:
        return False
    
    # 空きじゃなければ不可
    if board[y][x] != 0:
        return False

    # 設置確認場所より上のスペースの状態を取得
    disk_list = []
    for r in range(7 - y):
        disk_list.append(board[y + r + 1][x])
    
    # 設置確認場所の真上が敵のもの以外だったら不可
    if disk_list[0] != enemy:
        return False
    
    # 真上のを削除
    del disk_list[0]

    for disk in disk_list:
        if disk == enemy:
            continue
        elif disk == me:
            return True
        elif disk == 0:
            return False
    return False

def check_bottomleft(x, y):
    if y in [6, 7]:
        return False
    if x in [0, 1]:
        return False
    
    # 空きじゃなければ不可
    if board[y][x] != 0:
        return False

    bottom = 7 - y
    left = x

    disk_list = []
    for r in range(min((bottom, left))):
        disk_list.append(board[y + r + 1][x - (r+1)])
    
    if disk_list[0] != enemy:
        return False
    
    del disk_list[0]

    for disk in disk_list:
        if disk == enemy:
            continue
        elif disk == me:
            return True
        elif disk == 0:
            return False
    return False

def check_left(x, y):
    if x in [0, 1]:
        return False
    
    if board[y][x] != 0:
        return False

    disk_list = []
    for r in range(x):
        disk_list.append(board[y][x - (r + 1)])
    
    if disk_list[0] != enemy:
        return False
    
    del disk_list[0]

    for disk in disk_list:
        if disk == enemy:
            continue
        elif disk == me:
            return True
        elif disk == 0:
            return False
    return False

def check_upleft(x, y):
    if y in [0, 1]:
        return False
    if x in [0, 1]:
        return False
    
    # 空きじゃなければ不可
    if board[y][x] != 0:
        return False

    disk_list = []
    for r in range(min((x, y))):
        disk_list.append(board[y - (r+1)][x - (r+1)])
    
    if disk_list[0] != enemy:
        return False
    
    del disk_list[0]

    for disk in disk_list:
        if disk == enemy:
            continue
        elif disk == me:
            return True
        elif disk == 0:
            return False
    return False


show_board()
patch_placeable()
show_board()
