# Leetcode no 225 : Implement Stack using Queues


class MyStack(object):
    
    def __init__(self):
        self.queue1 = []
        self.queue2 = []

    def push(self, x):
        
        self.queue1.append(x)
        
        """
        :type x: int
        :rtype: None
        """
        

    def pop(self):
        
        while len(self.queue1) > 1:
            element = self.queue1.pop(0)
            self.queue2.append(element)
            
        elementfinal = self.queue1.pop(0)
        
        self.queue1, self.queue2 = self.queue2, self.queue1

        return elementfinal   
        
        """
        :rtype: int
        """
        
    def top(self):
        while len(self.queue1) > 1:
            element = self.queue1.pop(0)
            self.queue2.append(element)
        
        elementfinal = self.queue1.pop(0)
        self.queue2.append(elementfinal)
        
        self.queue1, self.queue2 = self.queue2, self.queue1
        return elementfinal  
        
        
        """
        :rtype: int
        """
        

    def empty(self):
        if len(self.queue1)>0:
            return False
        
        return True
        # """
        # :rtype: bool
        # """

def main():
    myStack = MyStack()
    myStack.push(1)
    myStack.push(2)

    
    # print(myStack)
    # print(myStack.pop())
    # myStack.push(3)
    # myStack.push(5)
    # myStack.push(8)
    print(myStack.top())
    print(myStack.pop())
    print(myStack.empty())

if __name__ == '__main__':
    main()
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()