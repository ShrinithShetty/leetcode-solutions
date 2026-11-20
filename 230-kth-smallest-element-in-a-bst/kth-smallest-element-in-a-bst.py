# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode | None, k: int) -> int:
        ans = [root.val]

        def dfs(root):
            nonlocal ans, k
            if not root:
                return
            
            dfs(root.left)

            k -= 1
            if k == 0:
                ans[0] = root.val
                return

            dfs(root.right)

        dfs(root)
        return ans[0]

