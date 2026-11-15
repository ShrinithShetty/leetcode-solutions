from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode | None) -> list[list[int]]:
        res = []
        
        if not root:
            return res

        queue = deque()
        queue.append(root)

        while queue:
            lvl = []
            n = len(queue)

            for _ in range(n):
                node = queue.popleft()

                lvl.append(node.val)
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
            
            res.append(lvl)

        return res