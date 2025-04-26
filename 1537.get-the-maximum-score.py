#
# @lc app=leetcode id=1537 lang=python3
#
# [1537] Get the Maximum Score
#

# @lc code=start
class Solution:
    def maxSum(self, nums1: List[int], nums2: List[int]) -> int:
        i, j = 0, 0
        score = 0

        sum1, sum2 = 0, 0  
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                sum1 += nums1[i]
                i += 1
            elif nums1[i] > nums2[j]:
                sum2 += nums2[j]
                j += 1
            else: # nums1[i] == nums2[j]
                score += max(sum1, sum2) + nums1[i]
                i += 1
                j += 1
                sum1, sum2 = 0, 0

        while i < len(nums1):
            sum1 += nums1[i]
            i += 1
        while j < len(nums2):
            sum2 += nums2[j]
            j += 1
            
        return (score + max(sum1, sum2)) % (10**9 + 7)
# @lc code=end
