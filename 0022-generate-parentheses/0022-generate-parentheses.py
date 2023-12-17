class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # recursion
        # add set of parentheses at back?
        # add parantheses around each exising pair
        def backtrack(s='', opencount=0, closedcount=0):
            if len(s) == 2*n and opencount == closedcount:
                res.append(s)
            if opencount < n:
                backtrack(s+'(', opencount + 1, closedcount)
            if closedcount < opencount:
                backtrack(s+')', opencount, closedcount+1)
                
        res = []
        stck = []
        backtrack()
        return res
        
        
        
        
        