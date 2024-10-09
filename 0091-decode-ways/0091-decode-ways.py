class Solution:
    def numDecodings(self, s: str) -> int:
        mapping = {str(i): chr(64 + i) for i in range(1, 27)}
        
        def helper(idx, memo):
            if idx in memo:
                return memo[idx]
            if idx > len(s):
                return 0
            if idx == len(s):
                return 1
            
            take_1 = 0
            take_2 = 0
            if s[idx] in mapping:
                take_1 = helper(idx + 1, memo)
            if s[idx:idx+2] in mapping:
                take_2 = helper(idx + 2, memo)
                
            memo[idx] = take_1 + take_2
            return take_1 + take_2
        
        return helper(0, {})
            