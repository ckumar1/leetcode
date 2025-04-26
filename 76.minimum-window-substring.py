    #
    # @lc app=leetcode id=76 lang=python3
    #
    # [76] Minimum Window Substring
    #

    # @lc code=start
from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        window_count  =  {}
        check_count = {}


        for c in t:
            check_count[c] = check_count.get(c, 0) + 1

        satisfied, required = 0, len(check_count)

        minimum = float("infinity")
        result = (-1, -1)

        left = 0
        for right in range(len(s)):
            letter = s[right]
            if letter in check_count:
                window_count[letter] = window_count.get(letter, 0) + 1
                if window_count[letter] == check_count[letter]:
                    satisfied += 1

            while(satisfied == required):
                size = right - left + 1
                if size < minimum:
                    minimum = size
                    result = (left, right)
                if s[left] in check_count:
                    window_count[s[left]] -= 1
                    if window_count[s[left]] < check_count[s[left]]:
                        satisfied -= 1
                left += 1

        l, r = result
        return s[l:r + 1]

# @lc code=end
