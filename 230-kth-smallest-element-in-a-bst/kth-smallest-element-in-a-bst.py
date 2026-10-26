# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode | None, k: int) -> int:
        node = root
        stk = []

        while stk or node:
            while node:
                stk.append(node)
                node = node.left
            
            node = stk.pop()
            k -= 1

            if k == 0:
                return node.val

            node = node.right