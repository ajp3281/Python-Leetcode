class MyQueue:
    '''
    
    stack1 = [1,2,3,4]
    reversestack = [4,3,2,1]
    
    insert normally into stack 1 : every time we need to pop first element - we reverse it and store in reverse stack to then pop from there in o(1) - then clear reverse stack. how would we get original stack back? - just slice it?
    
    '''
    def __init__(self):
        self.stack = []
        self.reverse_stack = []
        

    def push(self, x: int) -> None:
        self.stack.append(x)
        
    def pop(self) -> int:
        for i in range(len(self.stack)-1, -1, -1):
            self.reverse_stack.append(self.stack[i])
        res = self.reverse_stack.pop()
        self.reverse_stack.clear()
        self.stack = self.stack[1:]
        return res
        

    def peek(self) -> int:
        return self.stack[0]
        
    def empty(self) -> bool:
        return len(self.stack) == 0
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()