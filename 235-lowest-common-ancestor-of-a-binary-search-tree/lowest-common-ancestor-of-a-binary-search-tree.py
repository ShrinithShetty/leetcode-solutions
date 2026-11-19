# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        lca = [root.val]

        def dfs(root, p, q):
            nonlocal lca
            if not root:
                return 
            if p.val == root.val or q.val == root.val:
                lca[0] = root
                return

            if root.val > p.val and root.val > q.val:
                lca[0] = root.val
                dfs(root.left, p, q)
            elif root.val < p.val and root.val < q.val:
                lca[0] = root.val
                dfs(root.right, p, q)
            else:
                lca[0] = root
                return

        dfs(root, p, q)
        return lca[0]
            
