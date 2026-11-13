# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode | None, targetSum: int) -> list[list[int]]:
        res = []
        arr = []

        def dfs(root):
            nonlocal res, arr
            if not root:
                return
            arr.append(root.val)

            if not root.left and not root.right:
                if sum(arr) == targetSum:
                    res.append(arr.copy())

            dfs(root.left)
            dfs(root.right)
            arr.pop()
        dfs(root)
        return res
        