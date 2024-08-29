# Implementing queue using array
# arr= dequeue[0,1,2,3,4] enqueue
# operations
# enqueue==arr.append()
# dequeue==arr.pop(0)
# front=return arr[0]
# rear=return arr[-1]


# FIF0
class Queue:
    def __init__(self) -> None:
        # items is an ARRAY
        self.items = []

    def enqueue(self, value):
        self.items.append(value)

    def dequeue(self):
        if len(self.items) == 0:
            print("Queue is empty")
            return
        e = self.items.pop(0)
        return e

    def front(self):
        return print(self.items[0])

    def rear(self):
        return print(self.items[-1])

    def display(self):
        for i in self.items:
            print(i, end=" <-")
        print()


Q1 = Queue()
Q1.enqueue(99)
Q1.enqueue(90)
Q1.enqueue(101)
Q1.enqueue(88)
Q1.display()
Q1.front()
Q1.rear()
