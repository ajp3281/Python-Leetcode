class Solution:
    def countSubstrings(self, s: str) -> int:
        
        def helper(left, right):
            if left < 0 or right >= len(s) or s[left] != s[right]:
                return 0
            if s[left] == s[right]:
                return 1 + helper(left - 1, right+1)

            
            
            
        res = 0
        for index in range(len(s)):
            res += helper(index, index)
            res += helper(index, index + 1)
        return res
            
            
        