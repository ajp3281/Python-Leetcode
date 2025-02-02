class Solution:
    def minimumPartition(self, s: str, k: int) -> int:
        
        # two ptr approach
        # keep increasing right if int val < k
        # can we do this and be greedy? it is min number of substrings

        # 165462 k = 60
        # 165 54 6 2

        l = 0
        r = 0
        res = 0
        while r < len(s):
            int_substring = int(s[l:r+1])

            if int_substring <= k:
                r += 1

            else:
                if r == l:
                    return -1
                l = r
                res += 1

        if l < len(s):
            res += 1
        return res
