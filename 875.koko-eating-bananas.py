#
# @lc app=leetcode id=875 lang=python3
#
# [875] Koko Eating Bananas
#

# @lc code=start
class Solution:
    def workableSpeed(self, k: int, piles: List[int], limit: int) -> bool:
        hours = 0
        for pile in piles:
            # number of bananas in pile / k rounded up
            hours += ceil(pile / k)

        return hours <= limit

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)

        res = -1
        while left <= right:
            mid = (left + right) // 2

            if self.workableSpeed(mid, piles, h):
                res = mid
                right = mid - 1
            else:
                left = mid + 1

        return res

        
# @lc code=end
