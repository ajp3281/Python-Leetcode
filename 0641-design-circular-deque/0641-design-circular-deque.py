class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None
        
class MyCircularDeque:

    def __init__(self, k: int):
        self.size = 0
        self.capacity = k
        self.head = None
        self.tail = None
        

    def insertFront(self, value: int) -> bool:
        print(self.size, self.capacity)
        if self.size == self.capacity:
            return False
        if self.size == 0:
            self.head = self.tail = Node(value)
            self.size += 1
            return True
        current = self.head
        self.head = Node(value)
        self.head.next = current
        current.prev = self.head
        self.size += 1
        return True
        
    def insertLast(self, value: int) -> bool:
        if self.size == self.capacity:
            return False
        if self.size == 0:
            self.head = self.tail = Node(value)
            self.size += 1
            return True
        current = self.tail 
        self.tail = Node(value)
        self.tail.prev = current
        current.next = self.tail 
        self.size += 1
        return True

    def deleteFront(self) -> bool:
        if self.size == 0:
            return False
        if self.size == 1:
            self.size -= 1
            self.head = self.tail = None
            return True
        self.head = self.head.next 
        self.head.prev = None
        self.size -= 1
        return True

    def deleteLast(self) -> bool:
        if self.size == 0:
            return False
        if self.size == 1:
            self.size -= 1
            self.head = self.tail = None
            return True
        self.tail = self.tail.prev 
        self.tail.next = None
        self.size -= 1
        return True

    def getFront(self) -> int:
        if self.size != 0:
            return self.head.val
        return -1
        

    def getRear(self) -> int:
        if self.size != 0:
            return self.tail.val
        return -1
        
    def isEmpty(self) -> bool:
        return self.size == 0
        
    def isFull(self) -> bool:
        return self.size == self.capacity


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()