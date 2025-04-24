#
# @lc app=leetcode id=238 lang=python3
#
# [238] Product of Array Except Self
#
from typing import List

# @lc code=start
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        result = [1]*length
    
        left = 1
        for i in range(length):
            result[i] = left
            left *= nums[i]

        right = 1
        for i in reversed(range(length)):
            result[i] *= right
            right *= nums[i]

        return result 
# @lc code=end
