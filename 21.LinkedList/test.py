class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None


class SinglyLinkedList:
    def __init__(self) -> None:
        self.head = None

    # methods: append,traverse,delete,inserytatstart ,insert
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = new_node

    def traverse(self):
        if self.head is None:
            print("SLL is empty")
        else:
            temp = self.head
            while temp is not None:
                print(temp.value, end=" ")
                temp = temp.next
            print()

    def insertAtStart(self, value):
        new_node = Node(value)
        if self.head is None:
            # new_node.next=self.head
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def insertAT(self, value, index):
        new_node = Node(value)
        if index == 0:
            self.insertAtStart(value)
        else:
            temp = self.head
            prev_node = None
            count = 0
            while temp is not None and count < index:

                prev_node = temp
                temp = temp.next
                count += 1

            new_node.next = temp
            prev_node.next = new_node

    def deletehead(self):
        if self.head is None:
            print("Singly Linked List is empty")
        else:
            self.head = self.head.next

    def deleteByvalue(slef, value):
        temp = slef.head
        found = False
        while temp is not None:
            if temp.value == value:
                found = True
                break
            prev = temp
            temp = temp.next
        prev.next = temp.next


# # creating nodes
# node1 = Node(10)
# node2 = Node(11)
# node3 = Node(12)
# node4 = Node(13)

# # initialize setup
# node1.next = node2
# node2.next = node3
# node3.next = node4

sll = SinglyLinkedList()
sll.append(99)
sll.append(101)
sll.append(1)
sll.append(5)
sll.append(2)
sll.append(0)
sll.insertAtStart(999)
sll.insertAT(177, 3)
# sll.deletehead()
sll.deleteByvalue(5)
sll.traverse()
