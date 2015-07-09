def InvertBinaryTree(self, root):
#    if root:
#        invert = self.InvertBinaryTree
#        root.left, root.right = invert(root.right), invert(root.left)
#    return root
    stack = [root]
    while stack:
        node = stack.pop()
        if node:
            node.left, node.right = node.right, node.left
            stack += node.left, node.right
    return root
