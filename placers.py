import checkers


def is_both_unpleaceable(board):
    first = second = []

    for y, row in enumerate(board):
        for x in range(len(row)):
            if checkers.check_all(x, y, board, 1):
                first.append((x, y))
    
    for y, row in enumerate(board):
        for x in range(len(row)):
            if checkers.check_all(x, y, board, 2):
                second.append((x, y))
    
    if len(first) == len(second) == 0:
        return True
    return False


def patch_placeable(board, me):
    placeable_list = []
    for y, row in enumerate(board):
        for x in range(len(row)):
            if checkers.check_all(x, y, board, me):
                placeable_list.append((x, y))

    for x, y in placeable_list:
        board[y][x] = 3
    
    return board

def reset_placeable(board):
    for y in range(8):
        for x in range(8):
            if board[y][x] == 3:
                board[y][x] = 0
    return board

def reverse_all(x, y, board, me, enemy):
    result = board
    result = reverse_above(x, y, result, me, enemy)
    result = reverse_upright(x, y, result, me, enemy)
    result = reverse_right(x, y, result, me, enemy)
    result = reverse_bottomright(x, y, result, me, enemy)
    result = reverse_bottom(x, y, result, me, enemy)
    result = reverse_bottomleft(x, y, result, me, enemy)
    result = reverse_left(x, y, result, me, enemy)
    result = reverse_upleft(x, y, result, me, enemy)
    result[y][x] = me

    return result

def reverse_above(x, y, board, me, enemy):
    if not checkers.check_above(x, y, board, me, enemy):
        return board

    disk_list = []
    for r in range(y):
        disk_list.append([x, y - r - 1])
    
    for _x, _y in disk_list:
        disk = board[_y][_x]

        if disk == 0:
            return board
        elif disk == me:
            return board
        elif disk == enemy:
            board[_y][_x] = me
    
    return board

def reverse_upright(x, y, board, me, enemy):
    if not checkers.check_upright(x, y, board, me, enemy):
        return board

    disk_list = []
    for r in range(min(y, 7 - x)):
        disk_list.append([x + r + 1, y - r - 1])
    
    for _x, _y in disk_list:
        disk = board[_y][_x]

        if disk == 0:
            return board
        elif disk == me:
            return board
        elif disk == enemy:
            board[_y][_x] = me
    
    return board

def reverse_right(x, y, board, me, enemy):
    if not checkers.check_right(x, y, board, me, enemy):
        return board

    disk_list = []
    for r in range(7 - x):
        disk_list.append([x + r + 1, y])
    
    for _x, _y in disk_list:
        disk = board[_y][_x]

        if disk == 0:
            return board
        elif disk == me:
            return board
        elif disk == enemy:
            board[_y][_x] = me
    
    return board

def reverse_bottomright(x, y, board, me, enemy):
    if not checkers.check_bottomright(x, y, board, me, enemy):
        return board

    disk_list = []
    for r in range(min(7 - y, 7 - x)):
        disk_list.append([x + r + 1, y + r + 1])
    
    for _x, _y in disk_list:
        disk = board[_y][_x]

        if disk == 0:
            return board
        elif disk == me:
            return board
        elif disk == enemy:
            board[_y][_x] = me
    
    return board

def reverse_bottom(x, y, board, me, enemy):
    if not checkers.check_bottom(x, y, board, me, enemy):
        return board

    disk_list = []
    for r in range(7 - y):
        disk_list.append([x, y + r + 1])
    
    for _x, _y in disk_list:
        disk = board[_y][_x]

        if disk == 0:
            return board
        elif disk == me:
            return board
        elif disk == enemy:
            board[_y][_x] = me
    
    return board

def reverse_bottomleft(x, y, board, me, enemy):
    if not checkers.check_bottomleft(x, y, board, me, enemy):
        return board

    disk_list = []
    for r in range(min(7 - y, x)):
        disk_list.append([x - r - 1, y + r + 1])
    
    for _x, _y in disk_list:
        disk = board[_y][_x]

        if disk == 0:
            return board
        elif disk == me:
            return board
        elif disk == enemy:
            board[_y][_x] = me
    
    return board

def reverse_left(x, y, board, me, enemy):
    if not checkers.check_left(x, y, board, me, enemy):
        return board

    disk_list = []
    for r in range(x):
        disk_list.append([x - r - 1, y])
    
    for _x, _y in disk_list:
        disk = board[_y][_x]

        if disk == 0:
            return board
        elif disk == me:
            return board
        elif disk == enemy:
            board[_y][_x] = me
    
    return board

def reverse_upleft(x, y, board, me, enemy):
    if not checkers.check_upleft(x, y, board, me, enemy):
        return board

    disk_list = []
    for r in range(min(y, x)):
        disk_list.append([x - r - 1, y - r - 1])
    
    for _x, _y in disk_list:
        disk = board[_y][_x]

        if disk == 0:
            return board
        elif disk == me:
            return board
        elif disk == enemy:
            board[_y][_x] = me
    
    return board