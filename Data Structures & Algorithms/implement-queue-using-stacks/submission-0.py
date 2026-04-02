# we use 2 stacks, one to store the elements and the second stack to store the elements when pop func is called

class MyQueue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, x: int) -> None:
        if len(self.stack1) == 0:
            self.stack2.append(x)
        else:
            self.stack1.append(x)
        return

    def pop(self) -> int:
        x = self.change_stack()

        self.shift_stack()
        return x
        

    def peek(self) -> int:
        x = self.change_stack()
        if len(self.stack1) != 0:
            self.stack1.append(x)
        else:
            self.stack2.append(x)
        
        self.shift_stack()
        return x
        

    def empty(self) -> bool:
        return len(self.stack1) == 0 and len(self.stack2) == 0
    
    def change_stack(self) -> int:
        if len(self.stack1) == 0:
            while len(self.stack2) != 1:
                self.stack1.append(self.stack2.pop())
            x = self.stack2.pop()
        
        else:
            while len(self.stack1) != 1:
                self.stack2.append(self.stack1.pop())
            x = self.stack1.pop()
        
        return x

    def shift_stack(self) -> None:
        if len(self.stack1) != 0:
            while len(self.stack1) != 0:
                self.stack2.append(self.stack1.pop())
        
        else:
            while len(self.stack2) != 0:
                self.stack1.append(self.stack2.pop())
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()