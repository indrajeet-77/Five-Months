def preorder(root):
    if root is None:
        return
    print(root.value)
    preorder(root.left)
    preorder(root.right)
