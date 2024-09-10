class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        # sliding window - keep track of length of visited at every pt 
        # what are conditions to increase or decrease window?
        # if s[r] not in visited and len(visited) == 2: decrease
        # how to handle decrease?
        # while s[l] in visited: we can remove and recalculate if count of s[l] > 0
        # need to use hashmap for duplicate handling
        # else: increase
        
        visited = {}
        l = 0
        res = 0
        for r in range(len(s)):
            if s[r] not in visited and len(visited) == 2:
                print(visited,l,r)
                # remove whatever element is at l 
                while len(visited) == 2:
                    visited[s[l]] -= 1
                    if visited[s[l]] == 0:
                        visited.pop(s[l])
                    l += 1
            if s[r] in visited:
                visited[s[r]] += 1
            else:
                visited[s[r]] = 1
            res = max(res, r - l + 1)
        return res