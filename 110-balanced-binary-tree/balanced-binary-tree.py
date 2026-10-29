# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode | None) -> bool:
        return self.dfs(root) != -1

    def dfs(self, node):
        if not node:
            return 0

        left_height = self.dfs(node.left)
        right_height = self.dfs(node.right)

        if left_height == -1 or right_height == -1:
             return -1
        if abs(left_height - right_height) > 1:
            return -1

        return 1 + max(left_height, right_height)