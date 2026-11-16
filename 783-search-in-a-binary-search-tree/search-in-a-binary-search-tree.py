# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: TreeNode | None, val: int) -> TreeNode | None:
        res = [0]

        def dfs(root, val):
            nonlocal res
            if not root:
                return []

            if root.val == val:
                res[0] = root

            dfs(root.left, val)
            dfs(root.right, val)

        dfs(root, val)
        return res[0] if res[0] != 0 else None
            

