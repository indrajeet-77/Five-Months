# To create  a node we need A VALUE ->val , and nextaddress->next which we set to none by default
class Node:
    def __init__(self, val) -> None:
        self.val = val
        self.next = None


# Manual setting
# This is how we create nodes
node1 = Node(50)  # 50 is val
node2 = Node(11)
node3 = Node(99)
node4 = Node(15)
node5 = Node(22)

# Initial setup  connection of nodes(interconnection)
# node1.next = node2
# node2.next = node3
# node3.next = node4
# node4.next = node5
# node5.next = None


# # if we print node1 we get address of node1(which is an object(object address) )
# print(node1)

# # to print value of node1 we do
# print(node1.val)

# # to print node2 value we can aslo do
# print(node1.next.val)
# # to print node4 value we can als


# Here we have set head value as none by default cause at initial point singly linked list contains head set at none
class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.length = 0

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
            print(" Sll is empty, Can not traverse")
            return
        temp = self.head
        while temp is not None:
            print(temp.val, end=" ")
            temp = temp.next
        print()

    def insertAtStart(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def insert(self, value, index):
        new_node = Node(value)
        if index == 0:
            self.insertAtStart(value)
        else:
            count = 0
            temp = self.head
            while temp:
                count += 1
                temp = temp.next
                if count == index:
                    break
            new_node = temp.next
            temp.next = new_node


sll = SinglyLinkedList()
sll.append(200)
sll.append(9000)
sll.append(100)
sll.append(102)
sll.append(103)


sll.traverse()
# sll.insertAtStart(999)
# sll.traverse()

print("_____")
sll.insert(1992, 3)
sll.traverse()


# Notes etc

# sll = SinglyLinkedList()
# # if we print sll (which is an obj of singlylinkedlist class it will print address of that OBJECT sll)
# print(sll)
# # if we print sll.head  it will print None
# print(sll.head)
# # Now we will set head to the first node1 and other nodes
# sll.head = node1

# sll.head.next = node2
# # or
# node1.next = node2
# node2.next = node3
# node3.next = node4
# node4.next = node5
# # # now the head of sll is node 1 so it will print adress of node 1
# # # Both follwing are printing address of node1 (same address)
# # print(sll.head)
# # print(node1)
# # to print we can also do this to print node4
# print(node1.next.next.next.val)


# # So above everthing is manually did so its hard
# # so here we take help of traversing,delete ,insert etc
