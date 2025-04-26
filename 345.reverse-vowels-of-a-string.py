#
# @lc app=leetcode id=345 lang=python3
#
# [345] Reverse Vowels of a String
#

# @lc code=start
class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        l, r = 0, len(s) - 1
        res = list(s)
        
        while l < r:
            while l < r  and res[l] not in vowels:
                l += 1
            while l < r and res[r] not in vowels:
                r -= 1
            
            # Swap when both l and r point at vowels
            res[l], res[r] = res[r], res[l]
            l += 1
            r -= 1
        
        return "".join(res)


# @lc code=end
