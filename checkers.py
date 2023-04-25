from utils import enemy_num


def check_all(x: int, y: int, board: list, me: int):
    enemy = enemy_num(me)

    return any([
        check_above(x, y, board, me, enemy),
        check_upright(x, y, board, me, enemy),
        check_right(x, y, board, me, enemy),
        check_bottomright(x, y, board, me, enemy),
        check_bottom(x, y, board, me, enemy),
        check_bottomleft(x, y, board, me, enemy),
        check_left(x, y, board, me, enemy),
        check_upleft(x, y, board, me, enemy)
    ])


def check_above(x, y, board, me, enemy):
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

def check_upright(x, y, board, me, enemy):
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

def check_right(x, y, board, me, enemy):
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

def check_bottomright(x, y, board, me, enemy):
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

def check_bottom(x, y, board, me, enemy):
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

def check_bottomleft(x, y, board, me, enemy):
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

def check_left(x, y, board, me, enemy):
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

def check_upleft(x, y, board, me, enemy):
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