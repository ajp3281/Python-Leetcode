class CustomStack:

    def __init__(self, maxSize: int):
        self.size = 0
        self.capacity = maxSize
        self.stack = []
        
    def push(self, x: int) -> None:
        if self.size < self.capacity:
            self.stack.append(x)
            self.size += 1
        

    def pop(self) -> int:
        if self.stack:
            self.size -= 1
            return self.stack.pop()
        return -1

    def increment(self, k: int, val: int) -> None:
        if k > self.size:
            k = self.size
        
        for i in range(k):
            self.stack[i] += val
        


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)