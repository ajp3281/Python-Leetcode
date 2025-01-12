from collections import Counter
class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        # hashmap counter
        # count pairs of matching counts?

        # count number of odd characters
        # if number of odd characters <= k it must be possible to make
        # logic : a palindrome cant have 2 sets of odd characters

        hash_map = Counter(s)
        count = 0
        for val in hash_map.values():
            if val % 2 != 0:
                count += 1

        return count <= k and len(s) >= k

