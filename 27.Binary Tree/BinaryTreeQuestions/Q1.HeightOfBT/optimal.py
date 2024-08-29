class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.left = None
        self.right = None


def maxheight(root):
    if root is None:
        return 0
    left_height = maxheight(root.left)
    right_height = maxheight(root.right)
    return max(left_height, right_height) + 1


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

print(maxheight(root))
