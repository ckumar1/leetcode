#
# @lc app=leetcode id=105 lang=python3
#
# [105] Construct Binary Tree from Preorder and Inorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# from typing import List, Optional


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def dfs(preorder, inorder):
        
            if len(preorder) == 0:
                return None
            root = TreeNode(preorder[0])
            if len(preorder) == 1:
                return root


            i = inorder_map[root.val]

            inorder_left, inorder_right = inorder[:i], inorder[i+1:]
            preorder_left, preorder_right = preorder[1:i+1], preorder[i+1:]

            root.left = dfs(preorder_left, inorder_left)
            root.right = dfs(preorder_right, inorder_right)

            return root

        inorder_map = {v: i for i, v in enumerate(inorder)}
        root_index = inorder_map[preorder[0]] 

        return dfs(preorder, inorder)

    # def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
    #     def buildt(preorder, inorder):
    #         root_index = inorder_map[preorder[0]]

    #     inorder_map = {}
    #     for i, v in enumerate(inorder):
    #         inorder_map[v] = i

    #     left_inorder, right_inorder = (0, i), (i+1, len(inorder) - 1)
    #     left_preorder, right_preorder = (1, i+1), (i+2)
    #     root = TreeNode(preorder[0], buildt(), buildt())
# @lc code=end
