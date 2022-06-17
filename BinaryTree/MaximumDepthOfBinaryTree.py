"""
Maximum Depth of Binary Tree
Easy

7281

130

Add to List

Share
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.



Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: 3
Example 2:

Input: root = [1,null,2]
Output: 2
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root) -> int:

        # m = 0
        return self._getMaxLength(root)

    def _getMaxLength(self, root):
        if root is None:
            return 0

        left = self._getMaxLength(root.left)
        right = self._getMaxLength(root.right)

        print(f"root.val: {root.val} , left: {left} right: {right}")
        return max(left, right) + 1




# [3,9,20,null,null,15,7]
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.left.left = TreeNode(None)
root.left.right = TreeNode(None)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)


# root = [1,null,2]
root = TreeNode(1)
root.left = TreeNode(None)
root.right = TreeNode(2)
s = Solution()
print(s.maxDepth(root))