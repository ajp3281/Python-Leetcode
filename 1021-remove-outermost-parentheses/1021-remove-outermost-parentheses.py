class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        # primitive decomp continues until we reach an open ( with empty stack?
        primitives = []
        # (()())
        
        # stack is = (()())
        stack = []
        i = 0
        count = 0
        for character in s:

            if character == '(':
                stack.append(character)
                count += 1
            if character == ')':
                stack.append(character)
                count -= 1
                if count == 0:
                    primitives.append(stack.copy())
                    stack.clear()

                    
        strings = []
        for primitive in primitives:
            strings.append(primitive[1:len(primitive)-1])
            
        res = ""
        for string in strings:
            res += "".join(string)
        return res
        
        