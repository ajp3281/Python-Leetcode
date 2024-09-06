class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        
        # dp - what are base cases?
        # if we reach end of right string valid case
        # if we reach end of left string not valid
        
        def helper(left, right, memo):
            if (left, right) in memo:
                return memo[(left,right)]
            if right == len(t):
                memo[(left,right)] = 1
                return 1
            if left == len(s):
                memo[(left,right)] = 0
                return 0
            
            take = 0
            if s[left] == t[right]:
                take += helper(left + 1, right + 1, memo)
            take += helper(left + 1, right, memo)
            
            memo[(left,right)] = take
            return take
        
        return helper(0,0, {})
        