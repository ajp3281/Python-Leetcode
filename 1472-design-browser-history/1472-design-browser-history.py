class ListNode:
    def __init__(self, homepage: str):
        self.next = None
        self.prev = None
        self.val = homepage
        
class BrowserHistory:

    def __init__(self, homepage: str):
        self.head = ListNode(homepage)
        self.current = self.head
        
    def visit(self, url: str) -> None:
        self.current.next = ListNode(url)
        temp = self.current
        self.current = self.current.next
        self.current.prev = temp

    def back(self, steps: int) -> str:
        i = 0
        while i < steps:
            if not self.current.prev:
                return self.current.val
            self.current = self.current.prev
            i += 1
        return self.current.val

    def forward(self, steps: int) -> str:
        i = 0
        while i < steps:
            if not self.current.next:
                return self.current.val
            self.current = self.current.next
            i += 1
        
        return self.current.val
            
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)