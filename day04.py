# Leetcode no 232 : Implement Queue using Stacks

class MyQueue:
    
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
        

    def push(self, x: int) -> None:
        self.stack1.append(x)
        

    def pop(self) -> int:
        while (len(self.stack1)) > 1:
            self.stack2.append(self.stack1.pop())
        
        answer = self.stack1.pop()
        
        while (len(self.stack2)) > 0:
            self.stack1.append(self.stack2.pop())
        # self.stack1 , self.stack2 = self.stack2 , self.stack1
        
        return answer
            
        

    def peek(self) -> int:
        while (len(self.stack1)) > 1:
            self.stack2.append(self.stack1.pop())
        
        answer = -1
        
        if len(self.stack1):
            answer = self.stack1.pop()
            self.stack2.append(answer)
        
        while (len(self.stack2)) > 0:
            self.stack1.append(self.stack2.pop())
        # self.stack1 , self.stack2 = self.stack2 , self.stack1
        
        return answer
        
    
        

    def empty(self) -> bool:
        return len(self.stack1) > 0
        


# Your MyQueue object will be instantiated and called as such:
obj = MyQueue()
obj.push(1)
obj.push(2)
obj.push(3)

print(obj.pop())
print(obj.pop())
print(obj.pop())
print(obj.peek())
print(obj.empty())