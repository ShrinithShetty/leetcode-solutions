# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
max_sum = float("-inf")
class Solution:
    
    def maxPathSum(self, root: TreeNode | None) -> int:
        global max_sum
        max_sum = float("-inf")
        maxPathSum_helper(root)
        return max_sum

def maxPathSum_helper(node):
        global max_sum
        if not node:
            return 0

        left_sum = max(maxPathSum_helper(node.left), 0 )
        right_sum = max(maxPathSum_helper(node.right), 0)

        max_sum = max(max_sum, node.val + left_sum + right_sum)

        return node.val + max(left_sum, right_sum)
        