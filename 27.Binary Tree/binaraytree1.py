"""
            Drinks
    Hot                 Cold
Tea     Coffee       Fanta   Cola
"""


class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.left = None
        self.right = None


drinks = Node("drinks")
hot = Node("hot")
cold = Node("cold")
tea = Node("tea")
coffee = Node("coffee")
fanta = Node("fanta")
cola = Node("cola")

# Buttom -> Up 
hot.left = tea
hot.right = coffee
cold.left = fanta
cold.right = cola
drinks.left = hot
drinks.right = cold

print(drinks.left.left.value)
print(drinks.left.left.left)
print(cold.right.value)
