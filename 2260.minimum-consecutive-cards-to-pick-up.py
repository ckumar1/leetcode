from typing import List, int

#
# @lc app=leetcode id=2260 lang=python3
#
# [2260] Minimum Consecutive Cards to Pick Up
#

# @lc code=start
class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        shortest = len(cards) + 1
        counter = {}
        left = 0

        for right in range(len(cards)):
            if cards[right] in counter:
                counter[cards[right]] += 1 
            else:
                counter[cards[right]] = 1

            while counter[cards[right]] >= 2:
                shortest = min(shortest, right - left + 1)
                counter[cards[left]] -= 1
                left += 1
        
        if shortest > len(cards):
            return -1
        else:
            return shortest
        
# @lc code=end
