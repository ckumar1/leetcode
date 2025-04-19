#
# @lc app=leetcode id=34 lang=python3
#
# [34] Find First and Last Position of Element in Sorted Array
#

# @lc code=start
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # binary search for left most element target in array 
        left, right = 0, len(nums) - 1
        start = -1
        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                start = mid
                right = mid - 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1

        # binary search for second element
        left, right = 0, len(nums) - 1
        end = -1
        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                end = mid
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        
        return [start, end]
# @lc code=end
