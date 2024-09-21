class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        
        # "a)((b(c)d"
        # first iteration
        # remove extra closed
        # s = "a((b(c)d"
        
        # remove extra open if we have any
        # d(c)b((a
        # reverse and do the same of keeping count of "(" 
        # only add 
        
        def make_valid(s, opened, closed):
            # first keep track of extra opened, remove closed if we dont need it
            stack = []
            count = 0
            for character in s:
                if character == opened:
                    count += 1
                    stack.append(opened)
                elif character == closed:
                    if count > 0:
                        stack.append(closed)
                        count -= 1
                else:
                    stack.append(character)

            res = ''.join(stack)
            if count == 0:
                return res
            else:
                return make_valid(res[::-1], ')', '(')[::-1]
                    
            

            
        return make_valid(s, '(', ')')
        
        