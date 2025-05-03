#
# @lc app=leetcode id=297 lang=python3
#
# [297] Serialize and Deserialize Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque
from typing import List


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        # [1, 2, x, x, 3, 4, x, x, 5, x, x]
        def write_tree(root, encoded = None):
            if encoded is None:
                encoded = []

            if not root:
                encoded.append('x')
            else:
                encoded.append(str(root.val))
                write_tree(root.left, encoded)
                write_tree(root.right, encoded)

            return encoded
        
        # [1, 2, x, x, 3, 4, x, x, 5, x, x]
        return ",".join(write_tree(root))

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        def build_tree(encoded_queue):
            if not encoded_queue:
                return None
                
            val = encoded_queue.popleft()
            if val == 'x':
                return None
            else:
                node = TreeNode(val)
                node.left = build_tree(encoded_queue)
                node.right = build_tree(encoded_queue)
                return node
        
        encoded = deque(data.split(","))
        return build_tree(encoded)

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
# @lc code=end
