import placers, checkers
from utils import show_board, is_board_filled
import random, json

me = 1

match me:
    case 1:
        enemy = 2
    case 2:
        enemy = 1

# import random
# for a in range(8):
#     for b in range(8):
#         board[a][b] = random.randint(0, 2)

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
with open("logs.json", "r", encoding="UTF-8") as f:
    logs: list = json.load(f)
result = []

try_count = 0
dupl_count = 0

try:
    while True:
        # my turn
        placeables = []
        for y in range(8):
            for x in range(8):
                if checkers.check_all(x, y, board, me):
                    placeables.append([x, y])
        
        if len(placeables) == 0:
            result.append([-1, -1])
        else:
            _x, _y = random.choice(placeables)
            board = placers.reverse_all(_x, _y, board, me, enemy)
            result.append([_x, _y])

        if is_board_filled(board):
            # print(result)
            # show_board(board)
            if not result in logs:
                logs.append(result)
                try_count += 1
                
            else:
                dupl_count += 1
            print("\r{} | {}".format(try_count, dupl_count), end="")
                
            result = []
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
            try_count += 1
            # break
            continue

        # enemy turn
        placeables = []
        for y in range(8):
            for x in range(8):
                if checkers.check_all(x, y, board, enemy):
                    placeables.append([x, y])
        
        if len(placeables) == 0:
            result.append([-1, -1])
        else:
            _x, _y = random.choice(placeables)
            board = placers.reverse_all(_x, _y, board, enemy, me)
            result.append([_x, _y])

        if is_board_filled(board):
            # print(result)
            # show_board(board)
            if not result in logs:
                logs.append(result)
                try_count += 1
                
            else:
                dupl_count += 1
            print("\r{} | {}".format(try_count, dupl_count), end="")
                
            result = []
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
            
            # break
            continue
        
        # show_board(board)
        # print("\033[17A", end="")

        if placers.is_both_unpleaceable(board):
            # show_board(board)
            # print(result)
            # show_board(board)
            if not result in logs:
                logs.append(result)
                try_count += 1
                
            else:
                dupl_count += 1
            print("\r{} | {}".format(try_count, dupl_count), end="")
                
            result = []
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
            
            # break
            continue

    
except KeyboardInterrupt:
    with open("logs.json", "w", encoding="UTF-8") as f:
        json.dump(logs, f)