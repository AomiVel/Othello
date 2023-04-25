import checkers


def patch_placeable(board, me):
    placeable_list = []
    for y, row in enumerate(board):
        for x in range(len(row)):
            if checkers.check_all(x, y, board, me):
                placeable_list.append((x, y))

    for x, y in placeable_list:
        board[y][x] = 3
    
    return board
