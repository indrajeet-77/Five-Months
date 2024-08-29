# Definition for a binary tree node.
class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
def calheight(root):
        if root is None:
            return 0
        leftheight=calheight(root.left)
        rightheight=calheight(root.right)
        if leftheight==-1 or rightheight==-1:
            return -1
        if abs(leftheight-rightheight)>1:
            return -1
        return 1+max(leftheight,rightheight)
            
def isBalanced( root) -> bool:
        if root is None:
            return True
        result=calheight(root)
        if result>=0:
            return True
        return False
       

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
print(isBalanced(root))
        