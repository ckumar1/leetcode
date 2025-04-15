#
# @lc app=leetcode id=348 lang=python3
#
# [348] Design Tic-Tac-Toe
#

# @lc code=start
class TicTacToe:
    # cleaned up O(1) implementation

    def __init__(self, n: int):
        self.size = n
        # Keep track of counts for each player for each possible win condition
        # once count for any row, col, diag, or anti-diag reaches n they have won
        self.rows = [ [0] * n for i in range(2) ]
        self.cols = [ [0] * n for i in range(2) ]
        self.diag = [0, 0]
        self.antidiag = [0, 0]

    def move(self, row: int, col: int, player: int) -> int:
        # set add to each relevant counter for the player's move
        player_index = player - 1
      
        # add row
        self.rows[player_index][row] += 1
        # add col
        self.cols[player_index][col] += 1
        # add diag if relevant
        if row == col:
          self.diag[player_index] += 1
        # add anti-diag if relevant
        if row + col == self.size - 1:
          self.antidiag[player_index] += 1

        # check win conditions
        if self.rows[player_index][row] == self.size:
            return player
        elif self.cols[player_index][col] == self.size:
            return player
        elif self.diag[player_index] == self.size:
            return player
        elif self.antidiag[player_index] == self.size:
            return player
        else:
          return 0

# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)
# @lc code=end
