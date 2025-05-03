#
# @lc app=leetcode id=98 lang=python3
#
# [98] Validate Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validate(node, min_val=float('-inf'), max_val=float('inf')):
            if not node:
                return True

            # current node must be in the valid range (vals from parents)
            if node.val <= min_val or node.val >= max_val:
                return False

            return validate(node.left, min_val, node.val) and validate(node.right, node.val, max_val)

        return validate(root)
# @lc code=end
