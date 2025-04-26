#
# @lc app=leetcode id=680 lang=python3
#
# [680] Valid Palindrome II
#

# @lc code=start
class Solution:
    def validPalindrome(self, s: str) -> bool:

        def isPalindrome(s: str) -> bool:
            l, r = 0, len(s) -1
            while l < r:
                if s[l] != s[r]:
                    return False
                else:
                    l += 1
                    r -= 1
            return True

        l, r = 0, len(s) -1

        while l < r:
            if s[l] != s[r]:
                # check if omitting either char in s at l or r will be a palindrome
                return isPalindrome(s[l+1:r+1]) or isPalindrome(s[l:r])
            l += 1
            r -= 1 

        return True
        


        
        
# @lc code=end
