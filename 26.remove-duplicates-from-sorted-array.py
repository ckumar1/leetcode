#
# @lc app=leetcode id=26 lang=python3
#
# [26] Remove Duplicates from Sorted Array
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        writer, reader = 0, 0
        for reader in range(len(nums)):
            if nums[reader] > nums[writer]:
                writer += 1
                nums[writer] = nums[reader]
        return  writer + 1 
# @lc code=end
