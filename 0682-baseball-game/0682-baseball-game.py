class Solution:
    def calPoints(self, operations: List[str]) -> int:
        
        stack = []
        
        for num in operations:
            if num.lstrip('-+').isdigit():
                stack.append(int(num))
            elif num == "C":
                stack.pop()
            elif num == "D":
                stack.append(stack[-1]*2)
            elif num == "+":
                first = stack[-1]
                second = stack[-2]
                stack.append(first+second)
        
        res = 0
        while len(stack) > 0:
            res += stack.pop()
        
        return res
                
            
        