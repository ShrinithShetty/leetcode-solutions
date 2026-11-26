class Solution:
    def createBinaryTree(self, descriptions: list[list[int]]) -> TreeNode | None:
        nodes: dict[int, TreeNode] = {}
        children: set[int] = set()

        for parent, child, is_left in descriptions:
            nodes.setdefault(parent, TreeNode(parent))
            nodes.setdefault(child, TreeNode(child))
            children.add(child)
            
            if is_left:
                nodes[parent].left = nodes[child]
            else:
                nodes[parent].right = nodes[child]

        root_val = (set(nodes.keys()) - children).pop()
        return nodes[root_val]
