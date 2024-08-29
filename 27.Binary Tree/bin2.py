class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.left = None
        self.right = None


drinks = Node("Drinks")

hot = Node("hot")
cold = Node("cold")

tea = Node("tea")
coffee = Node("coffee")

fanta = Node("fanta")
coke = Node("coke")


hot.left = tea
hot.right = coffee

cold.left = fanta
cold.right = coke

drinks.left = hot
drinks.right = cold

print(drinks.left.right.value)
print(drinks.right.left.value)
