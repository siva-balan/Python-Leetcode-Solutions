class MyCircularQueue:

    def __init__(self, k: int):
        self.size = k
        self.queue = [None for i in range(self.size)]
        self.front = self.rear = -1

    def enQueue(self, value: int) -> bool:
        if ((self.rear +1) % self.size == self.front):
            return False
        elif self.front == -1:
            self.front,self.rear = 0,0
            self.queue[self.rear] = value
            return True
        else:
            self.rear = (self.rear+1)% self.size
            self.queue[self.rear] = value
            return True

    def deQueue(self) -> bool:
        if self.front == -1:
            return False
        elif self.front == self.rear:
            self.front,self.rear = -1,-1
            return True
        else:
            self.front = (self.front+1) % self.size
            return True

    def Front(self) -> int:
        if self.front == -1:
            return -1
        return self.queue[self.front]
            
    def Rear(self) -> int:
        if self.rear == -1:
            return -1
        return self.queue[self.rear]

    def isEmpty(self) -> bool:
        if self.front == self.rear == -1:
            return True

    def isFull(self) -> bool:
        if (self.rear +1) % self.size == self.front:
            return True
        else:
            return False


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
