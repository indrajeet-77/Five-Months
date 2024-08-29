class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None
        self.prev = None


class doublyLinkedList:
    def __init__(self) -> None:
        self.head = None

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node
        new_node.prev = temp

    def traverse(self):
        if self.head is None:
            print("Can not Traverse , DLL is empty")
            return
        else:
            temp = self.head
            while temp:
                print(temp.value, end=" ")
                temp = temp.next
            print()

    def deletehead(self):
        if self.head is None:
            print("Dll is empty ")
            return
        else:
            self.head = self.head.next
            self.head.prev = None

    def deleteEnd(self):
        if self.head is None:
            print("Can not delete Node ")
            return
        else:
            temp = self.head
            while temp.next.next:
                temp = temp.next
            temp.next = None
            # [1]->[2]->[3]

    def insertAtStart(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node

        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node


dll = doublyLinkedList()
dll.append(10)
dll.append(22)
dll.append(999)
dll.append(1000)
# dll.deletehead()
# dll.deletehead()
# dll.deleteEnd()
dll.insertAtStart(111)
dll.traverse()
