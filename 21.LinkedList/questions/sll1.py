class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None


class SinglyLinkedList:
    # def append
    # def insert at head or between
    # def delete head or between
    # traverse

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
            temp.next = new_node

    def traverse(self):
        if self.head == None:
            print("Can nit traverse sll is empty")
            return
        temp = self.head
        while temp:
            print(temp.value, end=" ")
            temp = temp.next
        print()

    def insertAthead(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def insertAt(self, value, index):
        new_node = Node(value)
        if index == 0:
            self.insertAthead(new_node)
        else:
            count = 0
            temp = self.head
            while temp:
                count += 1
                if count == index:
                    break
                temp = temp.next
            new_node.next = temp.next
            temp.next = new_node

    def deletehead(self):
        if self.head is None:
            print("Can not delete head,sll is empty")
            return
        else:
            self.head = self.head.next

    def deletebyindex(self, index):
        if self.head is None:
            print("Cannnot delete sll is empty")
            return
        if index == 0:
            self.head = self.head.next
            return

        temp = self.head
        count = 0

        while temp and count < index - 1:
            temp = temp.next
            count += 1
        if temp is None or temp.next is None:
            return
        temp.next = temp.next.next

    # [3]->[9]->[2]->[11]
    def deletebyvalue(self, value):
        if self.head is None:
            print("Sll is empty can not delete node.")
            return
        temp = self.head
        while temp:
            flag = False
            prev = temp
            temp = temp.next
            if temp.value == value:
                flag = True
                break
            if flag:
                prev.next = temp.next
            else:
                # print("Node not found in sll")
                return

    def searchelement(self, value):
        if not self.head:
            print("Can Not search SLL is empty")
        flag = False
        temp = self.head
        while temp:
            if temp.value == value:
                flag = True

            temp = temp.next
        if flag:
            print("True")
        # else:
        # print("Node not found in sll")


# s = SinglyLinkedList()
# s.append(10)
# s.append(11)
# s.append(1299)
# s.append(101)
# s.insertAt(77, 4)
# # s.searchelement(12)
# s.deletebyvalue(99)
# s.deletehead()
# s.traverse()
# s.deletebyindex(0)
# s.traverse()
