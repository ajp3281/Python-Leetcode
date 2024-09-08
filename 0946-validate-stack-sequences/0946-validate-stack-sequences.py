class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        '''
        run thru 
        stack = [0]
        popped = [1,0]
        '''

        # greedy - try to build popped array?
        self.stack = []
        self.pop = []
        j = 0
        for index in range(len(pushed)):
            self.stack.append(pushed[index])
            while j < len(popped) and self.stack and popped[j] == self.stack[-1]:
                self.pop.append(self.stack.pop())
                j += 1      
        return len(self.stack) == 0
                
            
            
        