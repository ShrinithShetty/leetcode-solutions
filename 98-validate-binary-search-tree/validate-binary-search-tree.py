# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode | None) -> bool:
        res = []
        def dfs(root):
            nonlocal res
            if not root:
                return

            dfs(root.left)
            res.append(root.val)
            dfs(root.right)

        dfs(root)
        i = 0
        while i + 1 < len(res):
            if res[i] >= res[i+1]:
                return False
            i += 1
        return True
