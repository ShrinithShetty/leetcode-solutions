from collections import defaultdict, deque
from typing import List, Optional

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        # column → list of (row, value)
        column_map = defaultdict(list)
        leftmost = rightmost = 0

        queue = deque([(root, 0, 0)])  # (node, column, row)

        while queue:
            node, col, row = queue.popleft()

            column_map[col].append((row, node.val))

            leftmost = min(leftmost, col)
            rightmost = max(rightmost, col)

            if node.left:
                queue.append((node.left, col - 1, row + 1))
            if node.right:
                queue.append((node.right, col + 1, row + 1))

        result = []
        for col in range(leftmost, rightmost + 1):
            # Sort by row first, then by value (required by LeetCode 987)
            column = sorted(column_map[col])
            result.append([val for row, val in column])

        return result