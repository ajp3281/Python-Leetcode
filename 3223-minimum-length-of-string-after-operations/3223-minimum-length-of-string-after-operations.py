class Solution:
    def minimumLength(self, s: str) -> int:

        # choose an idx - that has matching character to left and right
        # how do we make the optimal decision every time?

        # does the choice even matter?
        # choice does matter it appears?

        # abaacbcbb
        # remove b's first
        # remove by 2 * count // 3?

        s_counter = Counter(s)
        res = 0
        for val in s_counter.values():
            res += 2 * (val // 3)
            
        return len(s) - res
        