#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = {}
        for i, x in enumerate(nums):
            y = target - x
            if y in hash:
                return [i, hash[y]]
            hash[x] = i
        
# @lc code=end

