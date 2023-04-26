import placers, checkers
from utils import show_board

me = 1

match me:
    case 1:
        enemy = 2
    case 2:
        enemy = 1

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

while True:
    for y in range(8):
        for x in range(8):
            board = placers.patch_placeable(board, me)
    
    show_board(board)
    board = placers.reset_placeable(board)
    
    x, y = input("Place at [x y] :").split()

    board = placers.reverse_all(int(x), int(y), board, me, enemy)
    show_board(board)

    for y in range(8):
        for x in range(8):
            board = placers.patch_placeable(board, enemy)
    
    show_board(board)
    board = placers.reset_placeable(board)

    x, y = input("Place at [x y] :").split()
    
    board = placers.reverse_all(int(x), int(y), board, enemy, me)

