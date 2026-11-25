from collections import defaultdict
from typing import List, Optional

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        signature_to_id = {}
        id_count = defaultdict(int)
        result = []
        next_id = 1

        def dfs(node: Optional[TreeNode]) -> int:
            nonlocal next_id
            if not node:
                return 0

            left_id = dfs(node.left)
            right_id = dfs(node.right)
            signature = (left_id, node.val, right_id)

            if signature not in signature_to_id:
                signature_to_id[signature] = next_id
                next_id += 1

            sub_id = signature_to_id[signature]
            id_count[sub_id] += 1

            if id_count[sub_id] == 2:
                result.append(node)

            return sub_id

        dfs(root)
        return result
