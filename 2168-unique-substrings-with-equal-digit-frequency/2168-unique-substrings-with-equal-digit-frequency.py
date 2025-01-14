class Solution:
    def equalDigitFrequency(self, s: str) -> int:
        from collections import Counter
class Solution:
    def equalDigitFrequency(self, s: str) -> int:

        # sliding window + hashmap?

        # dp to catch every substring?
        # or should we do worse approach first
        visited = set()
        for l in range(len(s)):
            mapping = {}
            for r in range(l,len(s)):

                current_string = s[l:r+1]
                        
                mapping[s[r]] = mapping.get(s[r],0) + 1
                freq_set = set(mapping.values())

                if len(freq_set) == 1:
                    visited.add(current_string)
        return len(visited)

        