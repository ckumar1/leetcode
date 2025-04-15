#
# @lc app=leetcode id=348 lang=python3
#
# [348] Design Tic-Tac-Toe
#

# @lc code=start
class TicTacToe:
    # cleaned up O(N) implementation

    def __init__(self, n: int):
        self.board = [ [0] * n for _ in range(n) ]
        self.size = n
        self.winPossible = {
            "rows": [True] * n,
            "cols": [True] * n,
            # index 0 is for diag row==col, index 1 is for row + col = n-1
            "diag": True,
            "antidiag": True,
            }

    def check_row(self, row: int, player: int) -> int:
        if not self.winPossible["rows"][row]:
            return False

        count = 0
        for i in range(self.size):
            current_block = self.board[row][i]
            if current_block == player:
                count += 1
            elif current_block == 0:
                return False
            else:
                self.winPossible["rows"][row] = False
                return False
            
        return count == self.size

    def check_col(self, col: int, player: int) -> int:
        if not self.winPossible["cols"][col]:
            return False

        count = 0
        for i in range(self.size):
            current_block = self.board[i][col]
            if current_block == player:
                count += 1
            elif current_block == 0:
                return False
            else:
                self.winPossible["cols"][col] = False
                return False
            
        return count == self.size
        
    def check_diag(self, row: int, player: int) -> int:
        if not self.winPossible["diag"]:
            return False

        count = 0
        for i in range(self.size):
            current_block = self.board[i][i]
            if current_block == player:
                count += 1
            elif current_block == 0:
                return False
            else:
                self.winPossible["diag"] = False
                return False
            
        return count == self.size

    def check_antidiag(self, row: int, player: int) -> int:
        if not self.winPossible["antidiag"]:
            return False

        count = 0
        for i in range(self.size):
            current_block = self.board[i][self.size - 1 - i]
            if current_block == player:
                count += 1
            elif current_block == 0:
                return False
            else:
                self.winPossible["antidiag"] = False
                return False
            
        return count == self.size

    def move(self, row: int, col: int, player: int) -> int:
        # set the board
        self.board[row][col] = player

        if self.check_row(row, player):
            return player

        if self.check_col(col, player):
            return player

        if row == col and self.check_diag(row, player):
            return player

        if row + col == self.size-1 and self.check_antidiag(row, player):
            return player

        # if no win condition is met
        return 0
        # Check if the current player has won after this move


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)
# @lc code=end
