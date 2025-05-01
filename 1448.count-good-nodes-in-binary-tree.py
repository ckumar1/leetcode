#
# @lc app=leetcode id=1448 lang=python3
#
# [1448] Count Good Nodes in Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(root, currMax):
            if not root:
                return 0
            
            visibleCount = 0
            if root.val >= currMax:
                visibleCount += 1
                currMax = root.val

            return visibleCount + dfs(root.left, currMax) + dfs(root.right, currMax)

        return dfs(root, root.val)
        
        
# @lc code=end
