#
# @lc app=leetcode id=110 lang=python3
#
# [110] Balanced Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):
            if not root:
                return 0
            
            leftHeight = dfs(root.left)
            rightHeight = dfs(root.right)

            # check if either any of the children are imbalanced
            if leftHeight is -1 or rightHeight is -1:
                return -1

            # return -1 if current tree at node is imbalanced
            if abs(leftHeight - rightHeight) > 1:
                return -1

            # return height if current subtree is balanced
            return 1 + max(leftHeight, rightHeight)
        
        return dfs(root) is not -1
# @lc code=end
