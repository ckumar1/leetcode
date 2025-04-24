#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest, window_length = 0, 0
        left = 0 

        window = set()
        for right in range(len(s)):
            while s[right] in window:
                window.remove(s[left])
                left += 1
            
            window.add(s[right])
            window_length = right - left + 1
            longest = max(longest, window_length)

        return longest
# @lc code=end
