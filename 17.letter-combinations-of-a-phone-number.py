#
# @lc app=leetcode id=17 lang=python3
#
# [17] Letter Combinations of a Phone Number
#

# @lc code=start
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        result = []
        digit_map = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        
        def dfs(start_idx, path):
            if start_idx == len(digits):
                if path:
                    result.append("".join(path))
                return
        
            for letter in digit_map[digits[start_idx]]:
                path.append(letter)
                dfs(start_idx + 1, path)
                path.pop()

        dfs(0, [])
        return result
# @lc code=end
