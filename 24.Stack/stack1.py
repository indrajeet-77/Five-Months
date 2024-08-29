# In This we implemented Stack Using Array
class Stack:
    def __init__(self) -> None:
        self.items = []

    def push(self, element):
        self.items.append(element)

    def pop(self):
        if len(self.items) == 0:
            print("Stack is empty")
            return
        e = self.items.pop()
        return e

    def top(self):
        if len(self.items) == 0:
            print("Stack is empty")
            return
        return self.items[-1]

    def is_empty(self):
        if len(self.items) == 0:
            print("Stack is empty")
            return True
        return False

    def traverse(self):
        for i in range(len(self.items)):
            print(self.items[i])


s = Stack()
# s.push(10)
# s.push(20)
# s.push(99)
# s.pop()
s.is_empty()
s.traverse()
