class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        
        i = 0
        
        while i < len(s):
            
            if s[i] != ']':
                stack.append(s[i])
                
            else:
                current = ""
                while stack[-1] != '[':
                    current += stack.pop()
                stack.pop() # pop the '['
                number = ""
                while len(stack) > 0 and stack[-1] >= '0' and stack[-1] <= '9':
                    number += stack.pop() 
                print(number)
                number = int(number[::-1]) # pop the number
                print(number)
                stack.append(current * number)
        
            i += 1
            
        res = ""
        while len(stack) > 0:
            res += stack.pop()
            
        return res[::-1]
            
                
                
            
                
            
            
        