# In this we implented stack using Singly Linked List
class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None


class Stack:
    def __init__(self) -> None:
        self.head = None  # this will point to the top of the stack

    def is_empty(self):
        if self.head == None:
            return True
        return False

    # push
    # pop
    # peek
    # display

    def push(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def pop(self):
        if self.head is None:
            print("Stack is empty")
            return
        poppedele = self.head.value
        self.head = self.head.next
        return poppedele

    def peek(self):
        if self.head is None:
            print("Stack is empty")
            return
        return self.head.value

    def display(self):
        if self.head is None:
            print("Stack is empty")
            return
        temp = self.head
        while temp is not None:
            print(temp.value, end=" -> ")
            temp = temp.next
        print()


s = Stack()
s.push(10)
s.push(20)
s.push(99)
s.push(101)
s.display()
s.pop()
s.display()
