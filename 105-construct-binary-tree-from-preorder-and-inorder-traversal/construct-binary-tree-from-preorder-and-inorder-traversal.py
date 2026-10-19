# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode | None:
        inorder_map = {}
        preorder_index = 0
        for i, val in enumerate(inorder):
            inorder_map[val] = i

        def build_subtree(left, right):
            nonlocal preorder_index
            if left > right:
                return None

            val = preorder[preorder_index]
            inorder_index = inorder_map[val]
            node = TreeNode(val)

            preorder_index += 1

            node.left = build_subtree(left, inorder_index - 1)
            node.right = build_subtree(inorder_index + 1, right)

            return node

        return build_subtree(0 , len(inorder) - 1)