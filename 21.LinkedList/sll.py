# class Node:
#     def __init__(self, val) -> None:
#         self.val = val
#         self.next = None


# class SinglyLinkedList:
#     def __init__(self) -> None:
#         self.head = None

#     # Traverse
#     # Insert
#     # REmove
#     # Count


# node1 = Node(5)
# node2 = Node(76)
# node3 = Node(32)
# node4 = Node(90)
# sll = SinglyLinkedList()
# sll.head = node1
# sll.head.next = node2
# node2.next = node3
# node3.next = node4
# print(sll.head.val)
# print(sll.head.next.next.next.val)
# print(node1.next.next.next.val)


class Node:
    def __init__(self, val) -> None:
        self.val = val
        self.next = None


class SinglyLinkedList:
    def __init__(self) -> None:
        self.head = None

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = new_node  # type: ignore

    def traverse(self):
        if self.head is None:
            print("SLL is empty, cannot traverse")
            return
        temp = self.head
        while temp is not None:
            print(temp.val, end=" ")
            temp = temp.next
        print()

    def insertAtStart(self, value):
        pass


sll = SinglyLinkedList()
sll.append(100)
sll.append(200)
sll.append(500)
sll.append(300)
sll.traverse()
