class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.left = None
        self.right = None

def diameter(root):
    maxdia=0
    if root is None:
        return 0
    left_height = diameter(root.left)
    right_height = diameter(root.right)
    dia=left_height+right_height
    maxdia=max(maxdia,dia)
    return max(left_height, right_height) + 1


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

print(diameter(root))
