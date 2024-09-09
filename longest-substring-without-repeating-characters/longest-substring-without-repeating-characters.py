class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        # sliding window
        # when to increment pointers?
        
        # use visited set, if right pointer is visited, move left up until not equal to right ptr
        # 
        if len(s) == 0:
            return 0
        
        maxlen = float('-inf')
        l = 0
        
        visited = set()
        
        for r in range(len(s)):
            
            while s[r] in visited:
                visited.remove(s[l])
                l += 1
                
            visited.add(s[r])
            maxlen = max(maxlen, r-l+1)
            
        return maxlen
        