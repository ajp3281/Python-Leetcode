class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        
        stack = []
        res = 0
        for character in s:
            if character == '(':
                stack.append(character)
            if character == ')':
                if stack:
                    stack.pop()
                else:
                    res += 1
                    
        
        return len(stack) + res
        