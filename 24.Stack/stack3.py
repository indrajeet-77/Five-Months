# implement stack using queue
from collections import deque
class Stackusingqueue:
    def __init__(self) -> None:
        self.queue=[]
        # push
        # pop
        # top
        # isempty
        # size
    def push(self,element):
        self.queue.append(element)
        for i in range(len(self.queue)-1):
            e=self.queue.pop(0)
            self.queue.append(e)
    
    def pop(self):
        if len(self.queue)==0:
            print("Stack is empty")
            return
        return self.queue.pop(0)
    
    def top(self):
        if len(self.queue)==0:
            print("Stack is empty")
            return
        return self.queue[0]
    
    def isempty(self):
        if len(self.queue)==0:
            return True
        return False
    
    def size(self):
        return len(self.queue)

stack=Stackusingqueue()
stack.push(1)
stack.push(2)
stack.push(3)
print(stack.pop())
print(stack.top())
print(stack.size())




    
    
    