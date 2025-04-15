#
# @lc app=leetcode id=657 lang=python3
#
# [657] Robot Return to Origin
#

# @lc code=start
class Solution:
    def judgeCircle(self, moves: str) -> bool:
        x,  y = 0, 0

        for m in moves:
            if m == 'U':
                y += 1
            elif m == 'D':
                y -= 1
            elif m == 'R':
                x += 1
            elif m == 'L':
                x -= 1

        return x == 0 and y == 0
# @lc code=end
