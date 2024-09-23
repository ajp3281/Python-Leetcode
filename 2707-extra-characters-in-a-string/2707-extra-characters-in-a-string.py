class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        # dp instead? 
        # check substr from every character
        # if none found - skip it
        # check min from each
        
        def helper(i, memo):
            if i in memo:
                return memo[i]
            if i >= len(s):
                memo[i] = 0
                return 0
            
            skip = helper(i+1, memo) + 1
            
            take = float("inf")
            for j in range(i,len(s)):
                if s[i:j+1] in dictionary:
                    take = min(take, helper(j+1, memo))
                    
            memo[i] = min(take,skip)
            return memo[i]
        
        return helper(0, {})
            
        
        