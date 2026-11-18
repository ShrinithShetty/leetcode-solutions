# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode | None) -> bool:
        def is_valid(root, low = float('-inf') , high = float('inf')):
            if not root:
                return True

            if not (low < root.val < high):
                return False

            return is_valid(root.left, low, root.val) and is_valid(root.right, root.val, high)

        return is_valid(root)



            

            