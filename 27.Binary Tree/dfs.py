class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.left = None
        self.right = None


def preorderTraversal(root):
    if root is None:
        return
    # [root-left-right]
    print(root.value, end=" ")
    preorderTraversal(root.left)
    preorderTraversal(root.right)


def inorderTraversal(root):
    if root is None:
        return
    # [left-root-right]
    inorderTraversal(root.left)
    print(root.value, end=" ")
    inorderTraversal(root.right)


def postorderTraversal(root):
    if root is None:
        return
    postorderTraversal(root.left)
    postorderTraversal(root.right)
    print(root.value, end=" ")


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

print("Preorder Traversal: ")
preorderTraversal(root)

print("\nInorder Traversal: ")
inorderTraversal(root)

print("\nPostorder Traversal: ")
postorderTraversal(root)
