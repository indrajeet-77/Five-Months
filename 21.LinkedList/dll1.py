class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None
        self.prev = None


node1 = Node(10)
node2 = Node(20)
node3 = Node(30)
node4 = Node(40)


# Basic initialization

# # for node 1
# node1.prev = None
# node1.next = node2

# # for node 2
# node2.prev = node1
# node2.next = node3

# # for node 3
# node3.prev = node2
# node3.next = node4

# # for node 4
# node4.prev = node3
# node4.next = None

# print(node1.next.next.next.value)
# print(node4.prev.prev.prev.value)


class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None
        self.prev = None


class DoublyLinkedList:  # Fixed class name from DoublyLinkdList to DoublyLinkedList
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
        new_node.prev = temp
        temp.next = new_node

    def traverse(self):
        if self.head is None:
            print("DLL is empty")  # Fixed string from "Dll is empty" to "DLL is empty"
            return
        temp = self.head
        while temp:
            print(
                temp.value, end=" <-> " if temp.next else "\n"
            )  # Fixed end logic for the last node
            temp = temp.next

    def deleteHead(self):  # Fixed method name from deletehead to deleteHead
        if self.head is None:
            print(
                "Cannot delete head, DLL is empty"
            )  # Fixed string from "Can not delete head, DLL is empty" to "Cannot delete head, DLL is empty"
            return
        if self.head.next is None:  # Added condition to handle single node case
            self.head = None
        else:
            self.head = self.head.next
            self.head.prev = None

    def deleteTail(self):  # Fixed method name from deleteTail to deleteTail
        if self.head is None:
            print(
                "Cannot delete, DLL is empty"
            )  # Fixed string from "can Not delete ,dll is empty" to "Cannot delete, DLL is empty"
            return
        if self.head.next is None:  # Added condition to handle single node case
            self.head = None
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.prev.next = None

    def deleteByValue(
        self, value
    ):  # Fixed method name from deletebyValue to deleteByValue
        if self.head is None:
            print(
                "Cannot delete, DLL is empty"
            )  # Fixed string from "Can Not delete ,DLL is empty" to "Cannot delete, DLL is empty"
            return
        if self.head.value == value:
            self.deleteHead()
            return
        temp = self.head
        while temp:
            if temp.value == value:
                break
            temp = temp.next
        if temp is None:  # Added condition to handle value not found
            print(f"Value {value} not found in DLL")
            return
        if temp.next:
            temp.next.prev = temp.prev
        if temp.prev:
            temp.prev.next = temp.next

    def insertAtHead(
        self, value
    ):  # Fixed method name from insertAthead to insertAtHead
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def insertAtIndex(
        self, value, index
    ):  # Fixed method name from insertATindex to insertAtIndex
        if index == 0:
            self.insertAtHead(value)
            return
        new_node = Node(value)
        temp = self.head
        count = 0
        while temp and count < index - 1:
            temp = temp.next
            count += 1
        if temp is None:
            print(
                f"Index {index} out of bounds"
            )  # Added condition to handle index out of bounds
            return
        if temp.next is None:
            self.append(value)
        else:
            new_node.next = temp.next
            new_node.prev = temp
            temp.next.prev = new_node
            temp.next = new_node


# Testing the corrected code
dll = DoublyLinkedList()
dll.append(10)
dll.append(20)
dll.append(30)
dll.append(40)

dll.insertAtIndex(50, 4)
dll.insertAtIndex(60, 0)
dll.traverse()
