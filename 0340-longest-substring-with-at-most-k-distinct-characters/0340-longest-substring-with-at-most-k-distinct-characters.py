class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        
        
        # ecedeeeba
        visited = {}
        l = 0
        maxlen = 0
        if k == 0:
            return 0

        for r in range(len(s)):
            if s[r] in visited:
                visited[s[r]] += 1
            else:
                visited[s[r]] = 1
                while len(visited.keys()) > k:
                    visited[s[l]] -= 1
                    if visited[s[l]] == 0:
                        visited.pop(s[l])
                    l += 1
            print(l,r)
            maxlen = max(maxlen, r - l + 1)

        return maxlen
                
            
            