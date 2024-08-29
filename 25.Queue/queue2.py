class queueusingstack:
    # queue
    # 1)enqueue
    # 2)dequeue
    # 3)front
    # 4)rear
    # 5)isempty
    
    def __init__(self) -> None:
        self.stack1=[]
        self.stack2=[]
    
    
    def enqueue(self,x):
        while len(self.stack1 )>0:
            self.stack2.append(self.stack1.pop())
            
        self.stack1.append(x)
        
        while len(self.stack2)>0:
            self.stack1.append(self.stack2.pop())
    
    def dequeue(self):
        if len(self.stack1)==0:
            print("Stack is empty")
            return
        e=self.stack1.pop(-1)
        return e
    
    def front(self):
        if len(self.stack1)==0:
            print("stack is empty")
            return
        return self.stack1[-1]
    
    def rear(self):
        if len(self.stack1)==0:
            print("stack is empty")
            return
        return self.stack1[0]
    
    def isempty(self):
        if len(self.stack1)==0:
            return True
        return False
    
    
q1=queueusingstack()
q1.enqueue(1)
q1.enqueue(2)
q1.enqueue(3)
print(q1.dequeue())
q1.enqueue(99)
q1.enqueue(98)
q1.enqueue(97)
    
        
# [1,2,3] stack: pop=3
# [1,2,3] queue : dequeue=1

