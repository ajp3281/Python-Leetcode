class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        visited = set()
        l = 0
        maxlen = 0
        for r in range(len(s)):

            if s[r] not in visited:
                visited.add(s[r])

            else:
                while s[r] in visited:
                    visited.remove(s[l])
                    l += 1

                visited.add(s[r])

            maxlen = max(maxlen, r - l + 1)

        return maxlen