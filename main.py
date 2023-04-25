import utils


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


utils.show_board(board)
board = utils.patch_placeable(board, me)
utils.show_board(board)
