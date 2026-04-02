# we have to use 2 queues, which follows fifo way, so we pop all the elements from queue and push the elements to a new queue
# the last element from the queue will be the last entered element

class MyStack:
    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()

    def push(self, x: int) -> None:
        if self.check_empty(self.q1):
            self.q2.append(x)
        else:
            self.q1.append(x)
        return
    
    def check_empty(self, q) -> bool:
        return len(q) == 0

    def shift(self) -> int:
        if self.check_empty(self.q1):
            while len(self.q2) != 1:
                self.q1.append(self.q2.popleft())
            x = self.q2.popleft()
        
        else:
            while len(self.q1) != 1:
                self.q2.append(self.q1.popleft())
            x = self.q1.popleft()
        
        return x

    def pop(self) -> int:
        num = self.shift()
        return num

    def top(self) -> int:
        num = self.shift()
        if self.check_empty(self.q1):
            self.q2.append(num) 
        else:
            self.q1.append(num)
        return num

    def empty(self) -> bool:
        return len(self.q1) == 0 and len(self.q2) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()