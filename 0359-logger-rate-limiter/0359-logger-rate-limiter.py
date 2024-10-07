from collections import deque
class Logger:

    def __init__(self):
        self.map = {}
        
    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message not in self.map:
            self.map[message] = timestamp + 10
            return True
        else:
            if timestamp < self.map[message]:
                return False
            else:
                self.map[message] = timestamp + 10
                return True
            
        


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)