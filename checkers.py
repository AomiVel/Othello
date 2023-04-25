class Checker:
    def check_all(self, x, y, board, me):
        self.board = board
        self.me = me

        match me:
            case 1:
                self.enemy = 2
            case 2:
                self.enemy = 1

        return any([
            self._check_above(x, y),
            self._check_upright(x, y),
            self._check_right(x, y),
            self._check_bottomright(x, y),
            self._check_bottom(x, y),
            self._check_bottomleft(x, y),
            self._check_left(x, y),
            self._check_upleft(x, y)
        ])

    def _check_above(self, x, y):
        if y in [0, 1]:
            return False
        
        # 空きじゃなければ不可
        if self.board[y][x] != 0:
            return False

        # 設置確認場所より上のスペースの状態を取得
        disk_list = []
        for r in range(y):
            disk_list.append(self.board[y - (r+1)][x])
        
        # 設置確認場所の真上が敵のもの以外だったら不可
        if disk_list[0] != self.enemy:
            return False
        
        # 真上のを削除
        del disk_list[0]

        for disk in disk_list:
            if disk == self.enemy:
                continue
            elif disk == self.me:
                return True
            elif disk == 0:
                return False
        return False

    def _check_upright(self, x, y):
        if y in [0, 1]:
            return False
        if x in [6, 7]:
            return False
        
        # 空きじゃなければ不可
        if self.board[y][x] != 0:
            return False

        up = y
        right = 7 - x

        disk_list = []
        for r in range(min((up, right))):
            disk_list.append(self.board[y - (r+1)][x + r + 1])
        
        if disk_list[0] != self.enemy:
            return False
        
        del disk_list[0]

        for disk in disk_list:
            if disk == self.enemy:
                continue
            elif disk == self.me:
                return True
            elif disk == 0:
                return False
        return False

    def _check_right(self, x, y):
        if x in [6, 7]:
            return False
        
        if self.board[y][x] != 0:
            return False

        disk_list = []
        for r in range(7 - x):
            disk_list.append(self.board[y][x + r + 1])
        
        if disk_list[0] != self.enemy:
            return False
        
        del disk_list[0]

        for disk in disk_list:
            if disk == self.enemy:
                continue
            elif disk == self.me:
                return True
            elif disk == 0:
                return False
        return False

    def _check_bottomright(self, x, y):
        if y in [6, 7]:
            return False
        if x in [6, 7]:
            return False
        
        # 空きじゃなければ不可
        if self.board[y][x] != 0:
            return False

        bottom = 7 - y
        right = 7 - x

        disk_list = []
        for r in range(min((bottom, right))):
            disk_list.append(self.board[y + r + 1][x + r + 1])
        
        if disk_list[0] != self.enemy:
            return False
        
        del disk_list[0]

        for disk in disk_list:
            if disk == self.enemy:
                continue
            elif disk == self.me:
                return True
            elif disk == 0:
                return False
        return False

    def _check_bottom(self, x, y):
        if y in [6, 7]:
            return False
        
        # 空きじゃなければ不可
        if self.board[y][x] != 0:
            return False

        # 設置確認場所より上のスペースの状態を取得
        disk_list = []
        for r in range(7 - y):
            disk_list.append(self.board[y + r + 1][x])
        
        # 設置確認場所の真上が敵のもの以外だったら不可
        if disk_list[0] != self.enemy:
            return False
        
        # 真上のを削除
        del disk_list[0]

        for disk in disk_list:
            if disk == self.enemy:
                continue
            elif disk == self.me:
                return True
            elif disk == 0:
                return False
        return False

    def _check_bottomleft(self, x, y):
        if y in [6, 7]:
            return False
        if x in [0, 1]:
            return False
        
        # 空きじゃなければ不可
        if self.board[y][x] != 0:
            return False

        bottom = 7 - y
        left = x

        disk_list = []
        for r in range(min((bottom, left))):
            disk_list.append(self.board[y + r + 1][x - (r+1)])
        
        if disk_list[0] != self.enemy:
            return False
        
        del disk_list[0]

        for disk in disk_list:
            if disk == self.enemy:
                continue
            elif disk == self.me:
                return True
            elif disk == 0:
                return False
        return False

    def _check_left(self, x, y):
        if x in [0, 1]:
            return False
        
        if self.board[y][x] != 0:
            return False

        disk_list = []
        for r in range(x):
            disk_list.append(self.board[y][x - (r + 1)])
        
        if disk_list[0] != self.enemy:
            return False
        
        del disk_list[0]

        for disk in disk_list:
            if disk == self.enemy:
                continue
            elif disk == self.me:
                return True
            elif disk == 0:
                return False
        return False

    def _check_upleft(self, x, y):
        if y in [0, 1]:
            return False
        if x in [0, 1]:
            return False
        
        # 空きじゃなければ不可
        if self.board[y][x] != 0:
            return False

        disk_list = []
        for r in range(min((x, y))):
            disk_list.append(self.board[y - (r+1)][x - (r+1)])
        
        if disk_list[0] != self.enemy:
            return False
        
        del disk_list[0]

        for disk in disk_list:
            if disk == self.enemy:
                continue
            elif disk == self.me:
                return True
            elif disk == 0:
                return False
        return False