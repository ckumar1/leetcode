#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution:
    # Insight: Every closing bracket must be 
    # immediately precedeed by a opening bracket 
    # of the same type
    # Use stack to allow for fast LIFO operations
    # Use hash to map to closing and opening braes
    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 1:
            return False

        stack = []
        bracketMatch = {')': '(', '}': '{', ']': '['}
        for bracket in s:
            # Add every opening bracket to stack
            if bracket not in bracketMatch:
                stack.append(bracket)
            # Validate every closing bracket
            elif bracket in bracketMatch:
               # Handle the case if no opening brackets precede a closing bracket
               # and ensure the closing bracket is immediately preceded by the correct opening bracket
               if not stack or stack.pop() != bracketMatch[bracket]:
                   return False
        # string is valid if all opening brackets have a closing bracket... 
        # i.e. stack is empty
        return not stack
        # return len(stack) == 0
        

        
# @lc code=end

