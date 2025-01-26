class Solution:
    def maximumLengthSubstring(self, s: str) -> int:

        # sliding window problem
        # keep a hashmap set to count

        # if we reach an elem that already has a count of 2
        # keep increase left until its equal to that elemenet

        l = 0
        r = 0
        hashmap = defaultdict(int)
        res = 0
        for r in range(len(s)):
            while hashmap[s[r]] == 2:
                l += 1
                hashmap[s[l]] -= 1
                

            hashmap[s[r]] += 1
            res = max(res, r-l+1)

        return res
                