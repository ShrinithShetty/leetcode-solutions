# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """

        serialized_list = []
        self.preorder_serialize(root, serialized_list)
        return ','.join(serialized_list)

    
    def preorder_serialize(self, node, serialized_list):
        if node is None:
            serialized_list.append('#')
            return

        serialized_list.append(str(node.val))
        self.preorder_serialize(node.left, serialized_list)
        self.preorder_serialize(node.right, serialized_list)

    
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        node_val = iter(data.split(','))
        return self.build_tree(node_val)

    def build_tree(self, values):

        val = next(values)

        if val == '#':
            return None

        node = TreeNode(int(val))
        node.left = self.build_tree(values)
        node.right = self.build_tree(values)
        return node
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))