class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:

        # cost is equal to max dif between chars
        # must be substring
        # sliding window problem

        # two ptrs to keep track of currently changed substring
        # when to increase left/right ptrs - what are all edge cases
        # if cur_cost > max_cost - keep increasing left and subtracting cost
        # else keep increasing right
        # at every valid substring - record maxlen

        maxlen = 0
        l = 0
        cur_cost = 0
        for r in range(len(s)):

            cur_cost += abs(ord(s[r]) - ord(t[r]))
            if cur_cost > maxCost:
                cur_cost -= abs(ord(s[l]) - ord(t[l]))
                l += 1

            # need to handle wrap around
            maxlen = max(maxlen, r-l+1)

        return maxlen

        