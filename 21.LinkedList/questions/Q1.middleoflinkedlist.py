from sll1 import *


def middleofsll(self, head):
    prev = None
    temp = head
    while temp:
        front = temp.next
        temp.next = prev
        prev = temp
        temp = front
    print(prev)


sll = SinglyLinkedList()
sll.append(10)
sll.append(20)
sll.append(30)
sll.append(40)
sll.traverse()
sll.middleofsll(10)
